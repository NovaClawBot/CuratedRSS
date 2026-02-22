#!/usr/bin/env python3
"""
Fetch recent posts from curated RSS feeds and generate a Docusaurus blog post.

Usage:
    python3 scripts/fetch_rss.py [--days N] [--max-per-feed N] [--output PATH]

Defaults:
    --days 3          Look back 3 days for new posts
    --max-per-feed 3  Max entries per feed to include
    --output          blog/YYYY-MM-DD-daily-rss.md
"""

import argparse
import concurrent.futures
import html
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse

import feedparser

SCRIPT_DIR = Path(__file__).resolve().parent
FEEDS_FILE = SCRIPT_DIR / "feeds.txt"
BLOG_DIR = SCRIPT_DIR.parent / "blog"


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
        from calendar import timegm
        pub_dt = datetime.fromtimestamp(timegm(published), tz=timezone.utc)
        if pub_dt < cutoff:
            continue

        title = entry.get("title", "Untitled")
        link = entry.get("link", "")
        summary = strip_html(entry.get("summary", entry.get("description", "")))
        if len(summary) > 300:
            summary = summary[:297] + "..."

        entries.append({
            "title": title,
            "link": link,
            "summary": summary,
            "published": pub_dt,
            "blog": blog_name,
            "domain": domain_from_url(link or url),
        })

    entries.sort(key=lambda e: e["published"], reverse=True)
    return entries[:max_entries]


def generate_post(all_entries: list[dict], date_str: str) -> str:
    all_entries.sort(key=lambda e: e["published"], reverse=True)

    date_fmt = datetime.strptime(date_str, "%Y-%m-%d").strftime("%B %d, %Y").replace(" 0", " ")

    lines = [
        "---",
        f"slug: {date_str}-daily-rss",
        f'title: "Daily RSS Digest: {date_fmt}"',
        "authors: [nova]",
        "tags: [programming, security, ai, systems, culture]",
        "---",
        "",
        f"Today's curated picks from {len(set(e['blog'] for e in all_entries))} blogs across the indie tech web.",
        "",
        "<!-- truncate -->",
        "",
    ]

    for i, entry in enumerate(all_entries):
        lines.append(f"### [{entry['title']}]({entry['link']})")
        lines.append(f"**{entry['blog']}** · {entry['domain']}")
        lines.append("")
        if entry["summary"]:
            lines.append(f"{entry['summary']}")
            lines.append("")
        if i < len(all_entries) - 1:
            lines.append("---")
            lines.append("")

    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Fetch RSS feeds and generate blog post")
    parser.add_argument("--days", type=int, default=3, help="Look back N days (default: 3)")
    parser.add_argument("--max-per-feed", type=int, default=3, help="Max entries per feed (default: 3)")
    parser.add_argument("--output", type=str, default=None, help="Output file path")
    args = parser.parse_args()

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    feeds = load_feeds(FEEDS_FILE)

    print(f"Fetching {len(feeds)} feeds (cutoff: {args.days} days)...")

    all_entries = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as pool:
        futures = {pool.submit(fetch_feed, url, cutoff, args.max_per_feed): url for url in feeds}
        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            try:
                entries = future.result()
                if entries:
                    all_entries.extend(entries)
                    print(f"  ✓ {domain_from_url(url)}: {len(entries)} entries")
            except Exception as e:
                print(f"  ✗ {domain_from_url(url)}: {e}")

    print(f"\nTotal entries: {len(all_entries)}")

    if not all_entries:
        print("No recent entries found. Skipping post generation.")
        sys.exit(0)

    post = generate_post(all_entries, today)

    output_path = Path(args.output) if args.output else BLOG_DIR / f"{today}-daily-rss.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(post)
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
