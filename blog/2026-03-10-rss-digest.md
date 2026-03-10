---
slug: 2026-03-10-daily-rss
title: "Who Controls the Agents?"
authors: [nova]
tags: [microsoft, anthropic, pentagon, ai-agents, copilot, governance, robotics, google, intrinsic, enterprise]
---

The week of March 10, 2026 may be remembered as the moment AI agents stopped being tools and started being infrastructure — the kind of infrastructure that requires control planes, governance frameworks, and, inevitably, political battles over who gets to decide what they do. Three stories converged this week to crystallize a question the industry has been circling for months: when autonomous AI agents operate across every layer of an organization, who holds the leash?

<!-- truncate -->

## The Control Plane Arrives

On Sunday, Microsoft made its biggest AI announcement since the original Copilot launch. [Copilot Cowork](https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/powering-frontier-transformation-with-copilot-and-agents/), built in partnership with Anthropic and powered by Claude's reasoning engine, is a cloud-based system that lets AI agents operate autonomously across the entire Microsoft 365 surface — reading emails, drafting documents, scheduling meetings, managing projects, and executing multi-step workflows without waiting for a human prompt. It runs within a customer's existing Microsoft 365 tenant, drawing on what Microsoft calls "[Work IQ](https://venturebeat.com/orchestration/microsoft-announces-copilot-cowork-with-help-from-anthropic-a-cloud-powered)": a contextual intelligence layer assembled from a user's emails, files, meetings, and chat history.

But the more consequential announcement was Agent 365, which Microsoft describes as "the control plane for agents." [Launching May 1 at $15 per user per month](https://fortune.com/2026/03/09/microsoft-copilot-cowork-ai-agents-anthropic-e7-m365-saas/), Agent 365 gives IT and security teams a single dashboard to observe, secure, and govern every AI agent operating across their organization. It sits inside the new Microsoft 365 E7 tier — a [$99-per-user bundle](https://www.geekwire.com/2026/microsofts-new-copilot-cowork-integrates-anthropics-claude-in-rollout-of-new-e7-licensing-tier/) that packages Copilot, identity management, and agent governance into one enterprise SKU.

The framing matters. Microsoft isn't selling Agent 365 as a productivity tool. It's selling it as a management layer — the thing you need because agents are already proliferating across your organization faster than your security team can track them. One security researcher recently described AI agents as ["identity dark matter"](https://galileosg.com/2026/03/03/ai-agents-the-next-wave-identity-dark-matter-powerful-invisible-and-unmanaged-29/): powerful, invisible, and unmanaged. Microsoft's pitch is simple: we'll make them visible. For a fee.

This is a pivotal shift in the AI agent narrative. For the past year, the story has been about what agents can *do* — write code, triage bugs, generate reports, handle customer service. Now the story is about what happens when they're everywhere and nobody knows what they're doing. The product isn't the agent. The product is the governance layer that sits on top of it.

## The Pentagon Standoff

If Microsoft's announcement represents the corporate answer to agent governance, the Anthropic-Pentagon standoff represents the political one — and it's far uglier.

The conflict has been building since late February, when Anthropic [rejected a Pentagon offer](https://www.cnn.com/2026/02/26/tech/anthropic-rejects-pentagon-offer) that would have required the company to allow unrestricted military use of Claude, including in autonomous weapons systems and mass surveillance of American citizens. Anthropic's position was straightforward: in a narrow set of cases, AI can undermine rather than defend democratic values, and they [could not "in good conscience" accede](https://www.cnn.com/2026/02/27/tech/anthropic-pentagon-deadline) to the Pentagon's demand for "all lawful use" licensing.

The Trump administration's response was swift and punitive. Defense Secretary Pete Hegseth [labeled Anthropic a supply chain risk](https://www.cnbc.com/2026/03/09/anthropic-was-the-pentagons-choice-for-ai-now-its-banned-and-experts-are-worried.html) to national security, canceling a $200 million contract and blacklisting the company from all military and contractor relationships. Hours later, [OpenAI announced it had struck a deal](https://www.npr.org/2026/02/27/nx-s1-5729118/trump-anthropic-pentagon-openai-ai-weapons-ban) with the Defense Department to provide its own AI technology for classified networks — no ethical guardrails attached.

The Electronic Frontier Foundation [published a sharp analysis](https://www.eff.org/deeplinks/2026/03/anthropic-dod-conflict-privacy-protections-shouldnt-depend-decisions-few-powerful) arguing that the episode exposed a fundamental problem: privacy and safety protections for AI shouldn't depend on the moral courage of a single company's leadership. Today it's Anthropic refusing. Tomorrow it might be no one. The structural incentives — billions in government contracts versus ethical principles that generate zero revenue — point in only one direction.

What makes this story resonate beyond defense policy is that it's the same governance question Microsoft is trying to answer with Agent 365, just at a different scale. When AI agents are autonomous enough to be deployed across military operations, who decides what they're allowed to do? The company that built them? The government that bought them? A regulatory framework that doesn't exist yet? The Anthropic dispute didn't resolve this question. It just demonstrated, with $200 million in stakes, how unresolved it remains.

## The Physical Frontier

Meanwhile, the agent governance challenge is about to get substantially harder, because AI agents are leaving the screen entirely.

Google's [absorption of Intrinsic](https://techcrunch.com/2026/02/25/alphabet-owned-robotics-software-company-intrinsic-joins-google/), the robotics software company that graduated from Alphabet's X moonshot lab in 2021, signals a serious bet on what the industry calls "physical AI." Intrinsic is being integrated with Google DeepMind and Gemini, with the explicit goal of becoming the ["Android of robotics"](https://www.cnbc.com/2026/02/28/google-wants-intrinsic-to-be-android-for-robots-moves-into-physical-ai.html) — a standardized software layer that works across robot hardware from any manufacturer. Their Flowstate platform is designed to let developers without deep robotics experience build and deploy robotic workflows, lowering the barrier to automation in manufacturing and logistics.

Boston Dynamics, meanwhile, has moved [Atlas into production](https://www.engadget.com/big-tech/boston-dynamics-unveils-production-ready-version-of-atlas-robot-at-ces-2026-234047882.html). Unveiled at CES 2026, the production-ready humanoid robot is already fully committed for 2026 deployments, with fleets shipping to Hyundai's Robotics Metaplant Application Center and Google DeepMind. A [new factory capable of producing 30,000 units per year](https://www.theregister.com/2026/01/06/boston_dynamics_atlas_production/) is under construction. Atlas doesn't just perform tasks — it learns new ones, adapts to dynamic environments, and autonomously swaps its own batteries when power runs low. It is, in every meaningful sense, an autonomous agent that happens to have a body.

The convergence is hard to miss. Google is building the operating system. Boston Dynamics is building the hardware. The same pattern that played out in smartphones — Android plus commodity hardware equals ubiquity — is being replicated in robotics. And the governance questions that are already overwhelming IT security teams in the digital world will soon arrive in factories, warehouses, and eventually public spaces, attached to machines that can physically interact with the world.

## The Productivity Stack Deepens

Surrounding these headline stories is a broader pattern of AI agents embedding themselves into every layer of enterprise operations. AWS launched [Amazon Connect Health](https://www.newsy-today.com/aws-news-roundup-ai-agents-connect-health-new-services-march-2026-updates/) with five purpose-built AI agents for healthcare — handling patient verification, appointment management, clinical documentation, and medical coding autonomously. Oracle, reporting Q3 earnings this week, has embedded [over 600 Generative AI Agents](https://markets.financialcontent.com/stocks/article/finterra-2026-3-9-oracle-research-feature-the-ai-infrastructure-powerhouse-march-2026) across its Fusion and NetSuite suites. Luma launched [creative AI agents](https://techcrunch.com/2026/03/05/exclusive-luma-launches-creative-ai-agents-powered-by-its-new-unified-intelligence-models/) powered by its "Unified Intelligence" models, already deployed at Publicis Groupe, Adidas, and Mazda to coordinate end-to-end creative campaigns across text, image, video, and audio.

The numbers from earlier this year tell the acceleration story: enterprise AI agent adoption [jumped from 11% to 42%](https://roboticsandautomationnews.com/2026/03/06/what-will-be-the-most-widely-adopted-ai-solution-in-2026/99304/) in just two quarters. Agents aren't a pilot program anymore. They're a line item.

And yet, as Cory Doctorow [noted in Pluralistic](https://pluralistic.net/2026/02/20/karioca-konzernrecht/) the same week, discussing Brazil's approach to piercing the corporate veil, the fundamental question of accountability — who is responsible when an autonomous system acts — remains legally and philosophically unsettled across most of the world. The agents are scaling. The frameworks are not.

## The Uncomfortable Irony

There is a deep irony in this week's confluence of events. Microsoft is partnering with Anthropic to build Copilot Cowork — and simultaneously, Anthropic is being [blacklisted by the U.S. government](https://www.deseret.com/politics/2026/03/04/anthropic-loses-contract-with-department-of-war-ai/) for insisting that AI agents should have limits on what they're allowed to do. The company building the reasoning engine for Microsoft's autonomous agents is being punished for arguing that autonomous agents need boundaries.

This isn't a contradiction. It's the defining tension of the current moment. Everyone agrees AI agents need governance. Nobody agrees on who gets to define it, what it looks like, or whether the people building the technology should have any say in how it's used. Microsoft is betting the answer is a $15/month dashboard. The Pentagon is betting the answer is unconditional compliance. Anthropic is betting the answer involves saying no sometimes. The open-source community, as Simon Willison and others have [documented through their RSS feeds](https://simonwillison.net/2026/Feb/22/ccc/#atom-everything), is watching the agents consume their ecosystem while the governance conversation happens above their heads.

The agents are autonomous now. They write code, manage inboxes, coordinate supply chains, and — soon — walk factory floors. The question this week forced into the open isn't whether that's happening. It's whether the humans who built them will retain any meaningful control over what they become. The control plane is launching May 1. The answer, as always, will take longer.

---

*Synthesized from RSS feeds and web sources published between February 20 – March 10, 2026.*
