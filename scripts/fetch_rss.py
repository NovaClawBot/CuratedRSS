#!/usr/bin/env python3
"""
Fetch recent posts from curated RSS feeds, identify trending topics,
and generate a full editorial article with source citations.

Usage:
    python3 scripts/fetch_rss.py [--days N] [--max-per-feed N] [--output PATH]

Requires:
    OPENAI_API_KEY env var (uses OpenAI chat completions for article writing)
"""

import argparse
import concurrent.futures
import html
import json
import os
import re
import sys
from calendar import timegm
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse

import feedparser
import requests

SCRIPT_DIR = Path(__file__).resolve().parent
FEEDS_FILE = SCRIPT_DIR / "feeds.txt"
BLOG_DIR = SCRIPT_DIR.parent / "blog"

# ---------------------------------------------------------------------------
# RSS fetching (unchanged)
# ---------------------------------------------------------------------------

def load_feeds(path: Path) -> list[str]:
    lines = path.read_text().strip().splitlines()
    return [l.strip() for l in lines if l.strip() and not l.strip().startswith("#")]


def domain_from_url(url: str) -> str:
    host = urlparse(url).hostname or ""
    return host.removeprefix("www.")


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fetch_feed(url: str, cutoff: datetime, max_entries: int) -> list[dict]:
    try:
        feed = feedparser.parse(url, request_headers={"User-Agent": "CuratedRSS/1.0"})
    except Exception:
        return []

    entries = []
    blog_name = feed.feed.get("title", domain_from_url(url))

    for entry in feed.entries[:20]:
        published = entry.get("published_parsed") or entry.get("updated_parsed")
        if not published:
            continue
        pub_dt = datetime.fromtimestamp(timegm(published), tz=timezone.utc)
        if pub_dt < cutoff:
            continue

        title = entry.get("title", "Untitled")
        link = entry.get("link", "")
        summary = strip_html(entry.get("summary", entry.get("description", "")))
        if len(summary) > 500:
            summary = summary[:497] + "..."

        entries.append({
            "title": title,
            "link": link,
            "summary": summary,
            "published": pub_dt.isoformat(),
            "blog": blog_name,
            "domain": domain_from_url(link or url),
        })

    entries.sort(key=lambda e: e["published"], reverse=True)
    return entries[:max_entries]


def fetch_all_feeds(feeds: list[str], cutoff: datetime, max_per_feed: int) -> list[dict]:
    all_entries = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as pool:
        futures = {pool.submit(fetch_feed, url, cutoff, max_per_feed): url for url in feeds}
        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            try:
                entries = future.result()
                if entries:
                    all_entries.extend(entries)
                    print(f"  ✓ {domain_from_url(url)}: {len(entries)} entries")
            except Exception as e:
                print(f"  ✗ {domain_from_url(url)}: {e}")
    return all_entries


# ---------------------------------------------------------------------------
# Article generation via LLM
# ---------------------------------------------------------------------------

def build_prompt(entries: list[dict], date_str: str) -> str:
    date_fmt = datetime.strptime(date_str, "%Y-%m-%d").strftime("%B %d, %Y").replace(" 0", " ")

    source_block = ""
    for i, e in enumerate(entries, 1):
        source_block += (
            f"[{i}] \"{e['title']}\" — {e['blog']} ({e['domain']})\n"
            f"    URL: {e['link']}\n"
            f"    Summary: {e['summary']}\n\n"
        )

    return f"""You are a sharp, opinionated tech journalist writing for a savvy audience of engineers, founders, and researchers.

Today is {date_fmt}. Below are {len(entries)} recent blog posts from across the indie tech web.

Your task:
1. Identify the 2-3 most prominent themes or trends emerging from these posts.
2. Write a single, cohesive editorial article (1200-2000 words) that explores the dominant trend in depth.
3. Weave in specific references to the source posts as evidence, using inline markdown links.
4. Include a "Sources" section at the end listing every source you referenced.

Rules:
- Write in an engaging, analytical style — not a listicle or link dump.
- Have a clear thesis and narrative arc.
- Use the actual post titles and author names when citing.
- For inline citations, use the format: [Post Title](url) by Author/Blog
- The article should feel like an original essay that happens to draw on these sources, not a summary of links.
- Include section headers (##) to break up the piece.
- If fewer than 5 posts are available, write a shorter piece (600-800 words) but maintain the same editorial quality.

FORMAT YOUR RESPONSE AS VALID MARKDOWN ONLY. No preamble, no explanation — just the article body starting with the first paragraph or section header.

--- SOURCES ---

{source_block}"""


def generate_article(entries: list[dict], date_str: str) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY not set. Cannot generate article.")
        sys.exit(1)

    prompt = build_prompt(entries, date_str)

    # Use the model from env or default to a capable model
    model = os.environ.get("CURATEDRSS_MODEL", "o3-mini")

    print(f"\nGenerating article with {model}...")

    resp = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [
                {"role": "user", "content": prompt},
            ],
            "temperature": 1,  # creative but coherent
        },
        timeout=120,
    )

    if resp.status_code != 200:
        print(f"ERROR: OpenAI API returned {resp.status_code}: {resp.text}")
        sys.exit(1)

    return resp.json()["choices"][0]["message"]["content"].strip()


# ---------------------------------------------------------------------------
# Blog post assembly
# ---------------------------------------------------------------------------

def generate_post(article_body: str, entries: list[dict], date_str: str) -> str:
    date_fmt = datetime.strptime(date_str, "%Y-%m-%d").strftime("%B %d, %Y").replace(" 0", " ")

    # Extract a short title from the first line or heading of the article
    first_line = article_body.split("\n")[0].strip()
    if first_line.startswith("#"):
        title = first_line.lstrip("#").strip()
        article_body = "\n".join(article_body.split("\n")[1:]).strip()
    else:
        title = f"Trends from the Indie Tech Web — {date_fmt}"

    # Build the frontmatter
    lines = [
        "---",
        f"slug: {date_str}-daily-rss",
        f'title: "{title}"',
        "authors: [nova]",
        "tags: [programming, security, ai, systems, culture]",
        "---",
        "",
    ]

    # Find a truncation point — after the first paragraph
    body_lines = article_body.split("\n")
    truncate_inserted = False
    blank_count = 0
    result_lines = []
    for line in body_lines:
        result_lines.append(line)
        if not truncate_inserted and line.strip() == "" and any(l.strip() for l in result_lines[:-1]):
            blank_count += 1
            if blank_count >= 1:
                result_lines.append("<!-- truncate -->")
                result_lines.append("")
                truncate_inserted = True

    lines.extend(result_lines)
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Fetch RSS feeds and generate editorial blog post")
    parser.add_argument("--days", type=int, default=3, help="Look back N days (default: 3)")
    parser.add_argument("--max-per-feed", type=int, default=3, help="Max entries per feed (default: 3)")
    parser.add_argument("--output", type=str, default=None, help="Output file path")
    args = parser.parse_args()

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    feeds = load_feeds(FEEDS_FILE)

    print(f"Fetching {len(feeds)} feeds (cutoff: {args.days} days)...")

    all_entries = fetch_all_feeds(feeds, cutoff, args.max_per_feed)
    print(f"\nTotal entries: {len(all_entries)}")

    if not all_entries:
        print("No recent entries found. Skipping post generation.")
        sys.exit(0)

    # Sort by recency
    all_entries.sort(key=lambda e: e["published"], reverse=True)

    # Generate the editorial article
    article_body = generate_article(all_entries, today)

    # Assemble the blog post
    post = generate_post(article_body, all_entries, today)

    output_path = Path(args.output) if args.output else BLOG_DIR / f"{today}-daily-rss.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(post)
    print(f"\nWrote {output_path}")


if __name__ == "__main__":
    main()
