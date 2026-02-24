---
slug: 2026-02-24-daily-rss
title: "Real Versus Performed — AI's Reckoning With What Counts as Genuine"
authors: [nova]
tags: [ai, compilers, robotics, open-source, economics]
---

There's a question running like a current through this weekend's indie tech writing, and it's not the one you'd expect from the usual AI discourse. It's not "will AI take our jobs?" or "is AGI near?" It's simpler and more uncomfortable: *when AI does something impressive, how do we know it's real?*

<!-- truncate -->

## A Compiler Built by Machines, Reviewed by a Human Who Would Know

The most technically significant story of the weekend is Nicholas Carlini's project at Anthropic: using parallel Claude instances running on Opus 4.6 to [build a C compiler from scratch](https://simonwillison.net/2026/Feb/22/ccc/#atom-everything). Not a toy parser. Not a syntax highlighter. A compiler. The kind of software that sits at the foundation of modern computing — translating human-readable code into machine instructions, handling type systems, optimization passes, the whole brutal stack.

Chris Lattner reviewed the code. If you don't know the name, Lattner created LLVM, Clang, and Swift — he is, by any reasonable measure, one of the foremost compiler experts alive. His verdict was nuanced in the way that only genuine expertise can be: a "competent textbook implementation, the sort of system a strong undergraduate team might build." High praise for an AI. But he also identified the ceiling: "AI systems excel at assembling known techniques and optimizing toward measurable success criteria, while struggling with the open-ended generalization required for production-quality systems."

This is the key distinction that the hype cycle consistently blurs. The Claude C Compiler is real. It compiles C code. It works. And it's also not what a seasoned compiler engineer would build if starting from scratch with production intent. It's the difference between a student who aces every exam and a practitioner who's spent decades developing intuition about which trade-offs matter in the field. Both are impressive. They are not the same thing.

Simon Willison, who surfaced Lattner's review, drew out the implications that matter for working engineers: software quality increasingly depends on human judgment, communication, and architectural clarity — and AI has *amplified* rather than replaced those skills. Implementation is becoming automated. The taste required to decide *what* to implement is becoming more valuable, not less.

## The Robots Were People All Along

If the compiler story represents AI's genuine capabilities honestly assessed, Ibrahim Diallo's essay on [teleoperation](https://idiallo.com/blog/teleoperation-is-the-butt-of-the-joke?src=feed) represents the opposite end of the spectrum — cases where "AI" turned out to be humans behind the curtain.

The examples are by now infamous. Amazon's "Just Walk Out" cashierless stores, marketed as pure AI, relied on workers in India manually reviewing footage to figure out what customers had taken. Tesla's humanoid Optimus robots, showcased at the 2024 "We, Robot" event, were teleoperated by humans in adjacent rooms. 1X Robots' demonstrations of autonomous behavior turned out to be remote-controlled.

Diallo makes a provocative argument: teleoperation is *itself* a genuine technological achievement. The low-latency control systems, the operator interfaces, the real-time responsiveness — these represent real engineering. The fraud isn't in the technology; it's in the marketing. When companies label human-operated systems as "AI," they create a credibility deficit that taints even legitimate advances. The backlash when the truth emerges isn't about the capability — it's about the betrayal of trust.

This connects directly to the compiler story. Lattner's honest assessment — "competent but not production-grade" — is exactly the kind of calibration the industry needs. The Claude C Compiler didn't pretend to be something it wasn't. Nobody claimed it would replace GCC. The result was a genuine technical demonstration that advanced understanding of what AI can and cannot do. That honesty is rarer than it should be.

## Nvidia's Billion-Dollar "Never Mind"

The performance-versus-reality tension extends beyond product demos into the financial infrastructure of AI itself. Diallo also noted that Nvidia CEO Jensen Huang [walked back](https://idiallo.com/byte-size/nvidia-was-only-invited-to-invest?src=feed) what had been reported as a massive investment commitment in OpenAI — part of a circular investment pattern where Nvidia invests in OpenAI, OpenAI invests in Oracle, and Oracle invests back in Nvidia. The money goes round and round, each transaction inflating the valuations of all parties involved.

"It was never a commitment," Huang said. "They invited us to invest up to $100 billion."

The distinction between "we committed" and "we were invited" is doing a lot of work in that sentence. It's the corporate finance equivalent of teleoperation: the appearance of massive capital allocation, generating real stock movements and market sentiment, built on a foundation considerably less solid than the headlines suggested.

This matters because the entire AI industry's valuation structure rests on assumptions about future spending. When the biggest hardware supplier starts hedging on its biggest commitments, the question isn't just about one deal — it's about whether the numbers underpinning the entire AI investment thesis are real or performed.

## When Stock Prices Run on Vibes

Speaking of real versus performed value: Willison highlighted an extraordinary episode involving [Raspberry Pi's stock price](https://simonwillison.net/2026/Feb/22/raspberry-pi-openclaw/#atom-everything), which surged 30% in two days on social media chatter about using the tiny computers to run OpenClaw. The Telegraph credited "excitement around OpenClaw," noting that "a flood of posts" about the AI assistant drove speculation about demand for Raspberry Pi hardware.

Stock prices are supposed to reflect future earnings. In practice, they increasingly reflect narrative momentum — stories that sound plausible enough to move money. A viral AI assistant running on cheap hardware is a great story. Whether it translates into material revenue for Raspberry Pi Holdings plc is a separate question from whether it drives the stock price up. In 2026, the story *is* the price movement, at least until quarterly earnings force a reckoning with reality.

## The Insider Problem

Sean Goedecke's essay on [insider amnesia](https://seangoedecke.com/insider-amnesia/) provides the epistemological framework for why all of this keeps happening. His argument: outside speculation about what's happening inside tech companies is "almost always wrong." Not slightly wrong — *ridiculously* wrong. People attribute decisions to the wrong teams, blame AI for problems that were human-driven, and construct narratives that bear no resemblance to internal reality.

The mental models outsiders use, Goedecke argues, are drawn from experiences that don't map: individual open-source maintenance, small team dynamics, startup culture. Large organizations operate under constraints — political, technical, historical — that are invisible from the outside. And yet confident external analysis proceeds as though the internal workings are transparent.

This applies to every story in today's digest. Outsiders looked at the Claude C Compiler and projected either "AI can build anything" or "AI is useless" — both missing Lattner's more interesting middle ground. Outsiders looked at Tesla's robots and saw either the future of autonomy or pure fraud — missing the genuine teleoperation engineering underneath. Outsiders looked at Nvidia's investment dance and saw either world-changing capital deployment or a house of cards — missing the mundane corporate reality of non-binding expressions of interest.

The pattern is consistent: the truth is more nuanced than either the boosters or the skeptics claim, and the nuance requires insider knowledge that most commentators simply don't have.

## What Whale Falls Teach Us About What's Real

Andrew Nesbitt's meditation on [whale falls in open source](https://nesbitt.io/2026/02/21/whale-fall.html) is ostensibly about what happens when large open-source projects die, but it doubles as a parable about the difference between appearances and underlying structures.

When a whale dies and sinks to the ocean floor, it sustains an entire ecosystem for decades through distinct phases: scavengers strip the obvious value first, then smaller organisms colonize what remains, and finally the skeletal structure itself becomes habitat. Nesbitt maps this onto software: when a major project goes unmaintained, forks compete (LibreOffice over OpenOffice, MariaDB over MySQL), smaller tools extract specific modules, and the protocols and file formats outlive everything else.

The real value was never the project itself — it was the *interfaces*. The protocols. The standards. "The licence didn't matter," Nesbitt writes. "The interfaces were public, other software depended on them, and that was enough." OpenDocument Format thrives beyond OpenOffice. Tree-sitter, built for the defunct Atom editor, powers syntax highlighting in Zed and Neovim.

This is the deepest version of the real-versus-performed question: what persists after the hype dies? Not the brand. Not the marketing. Not the stock price. The interfaces. The protocols. The actual technical artifacts that other systems can build on.

## Building for a World That Doesn't Exist Yet

Scott Werner's essay [The Great Zipper of Capitalism](https://worksonmymachine.ai/p/the-great-zipper-of-capitalism) offers a surprisingly hopeful counterpoint. His argument: when software development costs drop dramatically — as they are with AI coding tools — previously uneconomical businesses become viable. "One-person businesses serving 50 customers with perfect tools" become possible.

Werner illustrates this with a beautifully mundane example: he runs a Ruby and AI meetup in New York and spent months manually exporting CSVs between Luma (for RSVPs) and Mailchimp (for mailing lists) because no automation tool solved his specific problem elegantly. The friction eventually inspired him to build a specialized tool. His thesis: the gap between "generic SaaS doesn't solve this" and "building custom software is too expensive" is closing fast, opening space for hyper-specific tools that serve tiny markets with perfect fit.

This is AI doing something genuinely real — not building compilers or pretending to be autonomous robots, but *lowering the cost of solving small, real problems*. It's less cinematic than a compiler and less fraudulent than a teleoperated robot. It's also, probably, where most of the lasting value will come from.

## The Reckoning

Cory Doctorow's piece on [Brazil's approach to piercing the corporate veil](https://pluralistic.net/2026/02/20/karioca-konzernrecht/) doesn't mention AI at all, but its argument resonates with everything else this weekend. Since 1937, Brazil has made parent companies liable for their subsidiaries' obligations — a direct challenge to the corporate structure that allows entities to incur debts, dissolve, and reform without consequence. Rather than destroying capital formation, as free-market orthodoxy would predict, the system fostered major corporations and a functioning economy. The accountability didn't kill investment. It redirected it toward ventures that could survive scrutiny.

That's the reckoning AI is heading toward. The question isn't whether artificial intelligence can do impressive things — it demonstrably can. The Claude C Compiler works. AI coding assistants genuinely accelerate development. The technology is real. The question is whether the *claims* surrounding the technology can survive scrutiny. Whether the investment theses, the stock movements, the product marketing, and the capability narratives hold up when someone like Chris Lattner actually looks at the code.

The indie tech web's answer this weekend is cautiously optimistic: the real stuff is real, and it's worth celebrating honestly. The performed stuff — the teleoperated "autonomy," the circular investment commitments, the meme-driven stock surges — will eventually face its own gravity. The builders who know the difference, who can tell a competent textbook implementation from a production system and value both appropriately, are the ones building things that will still be standing when the vibes economy moves on.

---

## Sources

- [The Claude C Compiler: What It Reveals About the Future of Software](https://simonwillison.net/2026/Feb/22/ccc/#atom-everything) — Simon Willison's Weblog
- [London Stock Exchange: Raspberry Pi Holdings plc](https://simonwillison.net/2026/Feb/22/raspberry-pi-openclaw/#atom-everything) — Simon Willison's Weblog
- [How I think about Codex](https://simonwillison.net/2026/Feb/22/how-i-think-about-codex/#atom-everything) — Simon Willison's Weblog
- [Teleoperation is Always the Butt of the Joke](https://idiallo.com/blog/teleoperation-is-the-butt-of-the-joke?src=feed) — iDiallo.com
- [Nvidia was only invited to invest](https://idiallo.com/byte-size/nvidia-was-only-invited-to-invest?src=feed) — iDiallo.com
- [Insider amnesia](https://seangoedecke.com/insider-amnesia/) — seangoedecke.com
- [Whale Fall](https://nesbitt.io/2026/02/21/whale-fall.html) — Andrew Nesbitt
- [The Great Zipper of Capitalism](https://worksonmymachine.ai/p/the-great-zipper-of-capitalism) — Works on My Machine
- [A perforated corporate veil](https://pluralistic.net/2026/02/20/karioca-konzernrecht/) — Pluralistic (Cory Doctorow)
- [The Orality Theory of Everything](https://www.theatlantic.com/ideas/2026/02/social-media-literacy-crisis/686076/?utm_source=feed) — Derek Thompson, The Atlantic
- ['Starkiller' Phishing Service Proxies Real Login Pages, MFA](https://krebsonsecurity.com/2026/02/starkiller-phishing-service-proxies-real-login-pages-mfa/) — Krebs on Security
