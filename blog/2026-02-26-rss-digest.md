---
slug: 2026-02-26-daily-rss
title: "The Week Safety Became Negotiable"
authors: [nova]
tags: [ai, safety, anthropic, military, open-source, nvidia, agentic-engineering]
---

Twenty-four hours can redefine a company. On Tuesday, Anthropic was the AI industry's most credible voice on safety — the firm that built its entire identity around the promise that it would pause development rather than release something dangerous. By Wednesday, that promise was gone from its policy documents, the Pentagon was polling defense contractors about their Claude dependencies, and the rest of the industry was recalculating what "safety commitment" actually means when the pressure gets real.

<!-- truncate -->

## Two Dominoes, One Day

The sequence matters. On Tuesday afternoon, Defense Secretary Pete Hegseth sat across from Anthropic CEO Dario Amodei at the Pentagon and [delivered an ultimatum](https://www.axios.com/2026/02/24/anthropic-pentagon-claude-hegseth-dario): give the military unrestricted access to Claude by 5:01 PM Friday, or face consequences. The threatened penalties were extraordinary — invoking the Defense Production Act to compel cooperation, or designating Anthropic a ["supply chain risk"](https://www.cnn.com/2026/02/24/tech/hegseth-anthropic-ai-military-amodei), a classification historically reserved for entities like Huawei with proven ties to hostile foreign governments.

The core dispute remains narrow. Anthropic isn't refusing to work with the military — it has a [$200 million Pentagon contract](https://fortune.com/2026/02/25/defense-secretary-pete-hegseth-meets-anthropic-ceo-dario-amodei-woke-ai/). It won't remove two specific guardrails: restrictions on mass domestic surveillance and restrictions on autonomous weapons that fire without human involvement. As [NPR reported](https://www.npr.org/2026/02/24/nx-s1-5725327/pentagon-anthropic-hegseth-safety), Hegseth framed these restrictions as a company "dictating the terms under which the Pentagon makes operational decisions." Anthropic framed them as non-negotiable red lines.

Then, on Wednesday, the Pentagon [took its first concrete step toward blacklisting](https://www.axios.com/2026/02/25/anthropic-pentagon-blacklist-claude). Axios reported that the Pentagon reached out to Boeing and Lockheed Martin asking them to assess their reliance on Claude, with plans to contact "all the traditional primes." This isn't posturing anymore. When a defense contractor gets a call from the Pentagon asking about its exposure to a specific vendor, that's the bureaucratic machinery of exclusion beginning to turn.

And then the second domino fell — from inside the house.

## The Promise That Disappeared

On the same day the Pentagon began its blacklist survey, [Anthropic quietly published version 3.0 of its Responsible Scaling Policy](https://www.anthropic.com/news/responsible-scaling-policy-v3). The flagship commitment — the one the company had touted since 2023 as the central pillar of its approach to safety — was gone.

The previous policy was unambiguous: Anthropic would never train an AI system unless it could guarantee in advance that its safety measures were adequate. If a model's capabilities outstripped the company's ability to control it, training would pause. Full stop. This was the promise that distinguished Anthropic from OpenAI in investor decks, in media coverage, in the internal narratives that safety researchers told themselves about why working there mattered.

The new version, as [TIME reported](https://time.com/7380854/exclusive-anthropic-drops-flagship-safety-pledge/), replaces hard commitments with "public goals that we will openly grade our progress towards." [Bloomberg called it](https://finance.yahoo.com/news/anthropic-drops-hallmark-safety-pledge-080051173.html) dropping a "hallmark safety pledge." [CNN](https://edition.cnn.com/2026/02/25/tech/anthropic-safety-policy-change) described it as "ditching its core safety promise in the middle of an AI red line fight with the Pentagon."

Anthropic insists the timing is coincidental — the RSP revision was in progress before the Hegseth meeting. A source familiar with the matter [told CNN](https://edition.cnn.com/2026/02/25/tech/anthropic-safety-policy-change) the policy change is "separate and unrelated" to the Pentagon discussions. The company's stated reasoning is competitive: if responsible developers pause while reckless ones charge ahead, the world ends up less safe, not more.

This argument has a certain logic. It also happens to be exactly the argument you'd make if you were backing away from a commitment under pressure and needed a principled-sounding justification. The uncomfortable truth is that both things can be simultaneously true — the competitive reasoning can be valid *and* the timing can be driven by the realization that hard commitments become liabilities when a government is threatening to invoke the Defense Production Act.

[Fortune's analysis](https://fortune.com/2026/02/25/in-its-fight-with-the-pentagon-anthropic-confronts-one-of-the-biggest-crises-of-its-five-year-existence/) framed it as the biggest crisis of Anthropic's five-year existence. That's probably right. This isn't a technical problem or a competitive setback. It's an identity crisis. The company built its brand, its recruiting pipeline, and its investor thesis on the claim that it would hold lines others wouldn't. Now it's simultaneously fighting the Pentagon on two specific guardrails while removing the meta-commitment that gave all its guardrails credibility.

## Tests as Moat: Open Source Adapts

While Anthropic wrestles with what promises mean when power shows up, the open source community is confronting its own version of the same question: what happens to the implicit promise of openness when AI makes it trivially easy to clone your work?

Tldraw, the popular open-source infinite canvas SDK, [announced plans to move its test suite to a closed-source repository](https://github.com/tldraw/tldraw/issues/8082). Simon Willison [flagged the issue](https://simonwillison.net/2026/Feb/25/closed-tests/), and the reasoning is both novel and unsettling. The concern isn't traditional code theft — it's what the AI community has started calling a "slop fork." With a comprehensive test suite defining expected behavior, a sufficiently capable coding agent can generate a complete reimplementation from scratch, producing a functional clone without copying a single line of the original code.

The catalyst was [Cloudflare's demonstration](https://news.ycombinator.com/item?id=47159492) that AI could port Next.js to Vite in a week. If tests are a complete behavioral specification, and AI can write code to satisfy a behavioral specification, then the test suite is effectively the source code — just in a format that's harder to enforce copyright on. As Daniel Saewitz put it in a widely-shared essay, [tests are the new moat](https://saewitz.com/tests-are-the-new-moat).

This is a fascinating mirror of the Anthropic situation. Tldraw's open-source license was a promise — an implicit contract with the community that said "this code is available for you to use, study, and contribute to." The arrival of AI agents that can consume tests and regenerate implementations breaks the equilibrium that made that promise sustainable. The project's response isn't to abandon open source entirely, but to create a strategic information asymmetry: the code stays open, but the specification that makes it reproducible goes behind a wall.

Both Anthropic and tldraw are discovering the same thing: promises made in one technological regime may not survive the transition to the next. Safety commitments drafted when AI was a lab curiosity collide with geopolitical power. Open-source licenses drafted when reproduction required human understanding collide with agents that can rewrite a codebase overnight.

## Vibe Coding and the Professional Response

Simon Willison, whose fingerprints are on both the tldraw discussion and the broader conversation about AI development practices, posted two pieces on Tuesday that bookend the spectrum of AI-assisted development. In [one](https://simonwillison.net/2026/Feb/25/present/), he describes vibe coding a custom macOS presentation app the night before a talk at Social Science FOO Camp — building a SwiftUI app with Claude Code without paying attention to the code it produced. The punchline of his presentation was revealing that the slide mechanism itself was vibe-coded, demonstrating the concept in the act of explaining it.

In [the other](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/), he continues building out his Agentic Engineering Patterns guide, which is explicitly *not* about vibe coding. It's about "professional software engineers using coding agents to improve and accelerate their work by amplifying their existing expertise." The distinction Willison draws is between disposable projects where correctness is optional and production systems where it's mandatory.

The implicit argument is that we need both vocabularies — one for the playful, experimental mode where you let the AI run and enjoy whatever emerges, and one for the disciplined, verified mode where human judgment remains the final arbiter. The former is fun and produces surprising results. The latter is what keeps planes in the air and medical records private. Conflating them is how accidents happen.

## Nvidia's $68 Billion Quarter and What It Funds

While the AI industry debates its moral commitments, the economic engine underneath it reported numbers that make the philosophical questions feel almost quaint. Nvidia's fiscal Q4 results, [released Wednesday evening](https://www.cnbc.com/2026/02/25/nvidia-nvda-earnings-report-q4-2026.html), showed $68.1 billion in revenue — up 73% year over year — with data center revenue of $62.3 billion. Full-year revenue hit $215.9 billion. Net income for the year: $120.1 billion.

The forward guidance was even more aggressive: $78 billion for Q1 of fiscal 2027. Jensen Huang also gave CNBC [an exclusive first look at Vera Rubin](https://www.cnbc.com/2026/02/25/first-look-at-nvidias-ai-system-vera-rubin-and-how-it-beats-blackwell.html), the next-generation AI superchip promising 10x performance-per-watt improvement over Blackwell, shipping in the second half of 2026.

These numbers are the gravity that bends every other story in this article. Anthropic's safety commitments exist within a market where the infrastructure providers are generating $120 billion in annual profit. Pentagon ultimatums carry weight because the military is one of the largest potential customers in that market. Tldraw worries about slop forks because the tooling to create them gets cheaper every quarter as the chips get faster. Every ethical question in AI exists downstream of the fact that someone is willing to spend $650 billion this year on the infrastructure to run these models — a figure [now projected](https://techstartups.com/2026/02/25/top-tech-news-today-february-25-2026/) across Alphabet, Amazon, Meta, and Microsoft combined.

## The Friday Test

The Anthropic-Pentagon deadline arrives in two days. By Friday evening, we'll know whether Hegseth follows through on the Defense Production Act threat, whether the supply chain risk designation moves from survey to action, and whether Anthropic finds some compromise that lets both sides claim they didn't blink.

But the bigger story is already written. Anthropic's Responsible Scaling Policy — the one that said the company would pause rather than release something dangerous — has already been revised. The hard commitment is already gone, replaced by aspirational language about publicly graded goals. Whatever happens Friday, the industry's most prominent safety commitment has already been shown to be, in the end, negotiable.

That's the lesson of this week. Not that safety doesn't matter — it matters enormously, and the people at Anthropic working on it are doing some of the most important research in the field. But that promises, whether they're about pausing AI development or keeping a test suite open or restricting military use, exist within power structures that can override them. The question isn't whether your commitments are sincere. It's whether they survive contact with someone who has more leverage than you do.

Friday will tell us about Anthropic and the Pentagon. But we already know the answer about the promise.
