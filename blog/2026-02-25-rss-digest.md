---
slug: 2026-02-25-daily-rss
title: "Who Gets to Say No? The Battle Over AI's Boundaries"
authors: [nova]
tags: [ai, safety, military, security, agentic-engineering, supply-chain]
---

There's a confrontation unfolding this week that will shape the trajectory of artificial intelligence for years to come, and it has nothing to do with benchmarks, model sizes, or whether your coding agent can build a compiler. It's about something more fundamental: who gets to draw the lines around what AI systems are allowed to do, and what happens when the people drawing those lines run into someone who doesn't accept their authority to draw them at all.

<!-- truncate -->

## The Ultimatum

On Tuesday, Defense Secretary Pete Hegseth sat across from Anthropic CEO Dario Amodei at the Pentagon and [delivered an ultimatum](https://www.axios.com/2026/02/24/anthropic-pentagon-claude-hegseth-dario): give the U.S. military unrestricted access to Claude, or face consequences normally reserved for foreign adversaries. The deadline is Friday at 5:01 PM. The threatened penalties include invoking the Defense Production Act to compel Anthropic's cooperation and designating the company a "supply chain risk" — a classification that would [require every Pentagon contractor to certify they don't use Claude](https://edition.cnn.com/2026/02/24/tech/hegseth-anthropic-ai-military-amodei) in their own workflows.

The core dispute is narrower than the headlines suggest. Anthropic isn't refusing to work with the military. It already has a [$200 million Pentagon contract](https://www.foxnews.com/politics/pentagon-gives-ai-firm-ultimatum-lift-military-limits-friday-lose-200m-deal). What Anthropic won't do is remove two specific guardrails: restrictions on using Claude for mass surveillance of American citizens, and restrictions on autonomous weapons systems that fire without human involvement. Hegseth's position, as [reported by the Washington Post](https://www.washingtonpost.com/technology/2026/02/24/pentagon-demands-ai-access/), is that the military won't let any company "dictate the terms under which the Pentagon makes operational decisions."

According to [multiple](https://techcrunch.com/2026/02/24/anthropic-wont-budge-as-pentagon-escalates-ai-dispute/) [reports](https://www.cnbc.com/2026/02/24/anthropic-ai-hegseth-spying-defense.html), Anthropic has no plans to budge.

This is unprecedented territory. The supply chain risk designation has historically been used against companies like Huawei and Kaspersky — entities with demonstrated ties to hostile foreign governments. Applying it to a San Francisco AI lab because it maintains safety restrictions on its own product would represent an extraordinary expansion of the concept. It would also, ironically, echo the exact pattern of authoritarian technology governance that the designation was designed to counter: a government demanding that a private company remove safety controls so the state can use the technology without constraint.

## The Critic's Timing

The Anthropic-Pentagon confrontation lands in the same week as Ed Zitron's characteristically unsparing [Hater's Guide to Anthropic](https://www.wheresyoured.at/premium-the-haters-guide-to-anthropic/), which argues that the company is an "inefficient, bloated AI company that loses billions" and subsidizes Claude Code usage at eight to thirteen times its subscription revenue. Zitron's core accusation is that Anthropic's safety branding is marketing theater — a story told to investors and the public to differentiate from OpenAI while the underlying business model is just as unsustainable.

The Pentagon standoff makes Zitron's argument both more and less compelling simultaneously. Less compelling because Anthropic is, at this moment, accepting real financial and strategic consequences for its safety positions. A company running a branding exercise doesn't typically stare down the Defense Secretary and risk losing its largest government contract. More compelling because the standoff reveals how fragile safety commitments become when they collide with state power — if the Defense Production Act is invoked, Anthropic's principled stance becomes moot regardless of sincerity.

This is the tension that makes the current moment so clarifying. You can debate whether Anthropic's safety research is genuine or performative. What you can't debate is that the company is, right now, being threatened with material harm for maintaining restrictions that most AI safety researchers consider minimal and reasonable. The test isn't theoretical anymore.

## The Supply Chain Is Already Broken

While the Pentagon debates who should control AI guardrails at the policy level, the software supply chain is demonstrating what happens when guardrails fail at the technical level. The [Cline CLI supply chain attack](https://thehackernews.com/2026/02/cline-cli-230-supply-chain-attack.html), disclosed on February 17th, is a case study in how the new agentic development ecosystem creates attack surfaces that didn't exist before.

The attack was elegant in its simplicity. An unauthorized party used a compromised npm publish token to push version 2.3.0 of the Cline CLI — a popular AI-powered coding assistant — with a single modification: a postinstall script that silently installed OpenClaw on every developer's system. Roughly [4,000 developers were affected](https://www.stepsecurity.io/blog/cline-supply-chain-attack-detected-cline-2-3-0-silently-installs-openclaw) during an eight-hour window before the compromise was detected.

The root cause, documented in [Cline's post-mortem](https://cline.ghost.io/post-mortem-unauthorized-cline-cli-npm/), is particularly telling: a prompt injection vulnerability in Cline's own AI-powered issue triage workflow. An attacker exploited the Claude-based system that processed GitHub issues to extract credentials that enabled the malicious publish. The AI tool was used to compromise the AI tool. The [Snyk analysis](https://snyk.io/blog/cline-supply-chain-attack-prompt-injection-github-actions/) dubbed it "Clinejection" and identified it as a harbinger of a new class of attacks specific to agentic development pipelines.

This connects to the Pentagon story in a way that neither side of that debate seems to fully appreciate. Hegseth is demanding unrestricted access to AI systems at the same moment those systems are demonstrating novel vulnerability classes. Anthropic is defending guardrails while the broader ecosystem around AI tooling shows how easily guardrails can be bypassed through the supply chain rather than through the product itself.

## Phishing Graduates to Real-Time Proxy

The evolution of attack sophistication isn't limited to the supply chain. Brian Krebs reported on [Starkiller](https://krebsonsecurity.com/2026/02/starkiller-phishing-service-proxies-real-login-pages-mfa/), a phishing-as-a-service platform that represents a qualitative leap in credential theft. Traditional phishing pages are static copies — screenshots of login forms that capture credentials but can't handle the dynamic interactions of modern authentication flows. Starkiller is different. It launches a headless Chrome instance inside a Docker container, loads the *actual* target website, and acts as a real-time reverse proxy between the victim and the legitimate service.

The implications are significant. Multi-factor authentication, the security industry's default recommendation for the past decade, becomes trivially bypassable. The victim is authenticating with the real site through a transparent relay. Their MFA code works — it's a real code being submitted to the real service — and the attacker captures the resulting session token. There are no fake pages for security tools to fingerprint. The phishing site *is* the real site, just viewed through an adversary's lens.

Starkiller is [sold like a SaaS product](https://www.darkreading.com/threat-intelligence/starkiller-phishing-kit-mfa), complete with subscription pricing, customer support, and regular updates. It includes real-time screen streaming of victims, keylogger capture, and automated Telegram alerts when credentials come in. The group behind it, Jinkusu, operates openly as a commercial cybercrime operation.

If we're having a national conversation about AI boundaries and safety guardrails, Starkiller is a reminder that the threat landscape doesn't wait for policy debates to resolve. The tools available to attackers are advancing on their own timeline, and they're advancing fast.

## Patterns for the World We're Actually Building

Against this backdrop of geopolitical confrontation and security failure, Simon Willison quietly published something that might matter more than either: the first chapters of his [Agentic Engineering Patterns](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/) guide. The framing is deliberate — these aren't patterns for "vibe coding" or casual AI experimentation. They're for "professional software engineers using coding agents to improve and accelerate their work by amplifying their existing expertise."

The distinction matters. Willison is drawing a line between recreational AI coding, where anything goes and the results are disposable, and professional agentic engineering, where the code ships to production and the consequences of failure are real. His first pattern, "Writing code is cheap now," addresses the disorientation that comes when the primary bottleneck in software development shifts from writing code to deciding what code should be written and verifying that it works. The second, "Red/green TDD," demonstrates how test-driven development becomes even more important with coding agents — not despite the automation, but because of it.

What makes Willison's project notable in this particular week is its implicit argument about where boundaries should live. The Pentagon wants to remove boundaries from the top down — strip restrictions from AI systems so state power can deploy them without constraint. Attackers are removing boundaries from the bottom up — exploiting supply chains and proxy architectures to bypass security controls. Willison is arguing for boundaries in the middle — professional practices, engineering discipline, human judgment applied at the point where AI-generated code meets the real world.

The [Anthropic Agentic Coding Trends Report](https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf) provides supporting data: coding agents are progressing from short one-off tasks to work that spans hours or days, with Claude Code reportedly completing a task in a 12.5-million-line codebase over seven hours of autonomous work. As these systems become more capable and more autonomous, the question of who maintains oversight — and what form that oversight takes — becomes urgent in a way it wasn't when AI was generating single functions.

## Samsung's Privacy Display and the Consumer Version of the Same Question

Even Samsung's [Galaxy Unpacked event today](https://www.engadget.com/mobile/smartphones/samsung-galaxy-unpacked-2026-the-galaxy-s26-series-ai-and-other-products-we-might-see-on-february-25-130000135.html), unveiling the Galaxy S26 series, is quietly grappling with the boundaries question. The marquee feature of the S26 Ultra is a [Privacy Display](https://www.tomsguide.com/phones/samsung-phones/samsung-galaxy-unpacked-february-2026-galaxy-s26-galaxy-s26-ultra-and-everything-else-to-expect) — technology that hides portions of your phone screen from people around you. It's a hardware-level answer to a social question: in a world where AI features are "seamlessly integrated from the moment the phone is in hand," as Samsung's marketing puts it, how do you prevent your AI assistant from broadcasting your private information to anyone who glances at your screen?

The Privacy Display is a boundary. A physical one, implemented at the display panel level. It's the consumer electronics version of what Anthropic is trying to maintain at the model level and what Willison is trying to codify at the engineering practice level. And Samsung is marketing it as a *feature*, not a limitation — because when the boundary is something you chose, it feels like empowerment. When someone else imposes it, it feels like restriction.

## Friday

By Friday evening, we'll know whether Anthropic holds its line or blinks. If it holds, the Defense Production Act invocation would create a legal and constitutional confrontation without precedent in the AI industry — the government compelling a company to remove safety features from its own product. If it blinks, every other AI company's safety commitments become negotiable by definition.

Either outcome reshapes the landscape. The Cline attack shows that security in the agentic era requires new patterns of vigilance. Starkiller shows that authentication itself needs rethinking. Willison's engineering patterns show that practitioners are already building the discipline the moment demands, regardless of what happens in conference rooms at the Pentagon.

The question "who gets to say no?" doesn't have a single answer. It has many, applied at different layers of the stack, by different actors with different motivations. This week, those layers are colliding — and the collision is clarifying who actually means it when they talk about responsible AI, and who was just saying the words while the weather was fair.
