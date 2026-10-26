# Idea shortlist and recommendation

> Update (later on 2026-10-26): the chosen idea has since been reframed as a live expert guide with a fade-out and optional real expert voice. See `build-plan.md` (current plan) and `problem-framing.md`. The scoring below reflects the earlier "skill-transfer coach" framing and is kept for the record.

As of 2026-10-26. Built from past Meta hackathon winners, Meta's Connect 2026 announcements, public GitHub repos of other entrants, and prior-art searches. Scores are my judgement against the published rubric, not data. Most web findings come from search summaries, and vendor claims are unverified.

## Recommendation

Build **a skill-transfer coach**: an expert films a hands-on task once, the agent turns it into a verified procedure, and a novice is then coached and checked live, step by step, on a phone or Meta glasses. This replaces my earlier pick (energy retrofit) as the lead idea. Reasons: its demo is a live before-and-after story that a three-minute video can show, it uses more Meta models naturally, it aligns with what Meta is pushing at Connect 2026 (glasses toolkit, agents), and it fits the "verifiable agents" workshop and the Best Agentic prize. The energy retrofit agent stays as the backup, and both share most components.

## Scores

| Idea | Impact 30% | Meta tooling 25% | Demo 25% | Depth 20% | Weighted |
| --- | --- | --- | --- | --- | --- |
| Skill-transfer coach | 8 | 9 | 9 | 7 | 8.3 |
| Self-driving mini-lab agent | 6 | 7 | 8 | 9 | 7.4 |
| Energy retrofit agent | 8 | 7 | 6 | 7 | 7.1 |
| Verifiable repair agent | 6 | 7 | 7 | 6 | 6.5 |

## What the research shows

- **Past Meta hackathon winners** were practical, domain-specific, and often hardware or glasses based: OpenGlass ($20 smart glasses, Llama 3 hackathon), OrgLens, Llama CCTV Operator, and Geo-ML (a geologist automating their own reports). Sources: [Llama 3 recap](https://ai.meta.com/blog/llama-3-hackathon-recap-cerebral-valley/), [LlamaCon recap](https://ai.meta.com/blog/llamacon-hackathon/).
- **Meta's current push** (Connect 2026): the Wearables Device Access Toolkit 1.0 for Ray-Ban and Oakley glasses, Muse Spark 1.3, Muse Code, and Glimmer for local agents. The toolkit's Mock Device Kit streams a phone camera or video file as a simulated glasses feed, so no glasses are needed to demo. Sources: [Connect recap](https://developers.meta.com/blog/meta-connect-recap/), [Mock Device Kit](https://wearables.developer.meta.com/docs/develop/dat/mock-device-kit/).
- **Crowded among other entrants** (public repos, mostly scaffolds): robot planning and embodied agents (Hasami, Safe Embodied Agent, a mechatronics template), photo-to-CAD ([Photo-CAD](https://github.com/TheKingOfMoney09/Photo-CAD), README only so far), market-stall catalogues (StallSnap), wildlife clips (WildScore), a room-to-escape-room game, a Geometry Dash RL agent. Avoid these.
- **Official guidance:** the event page says Indie is judged on "creativity, technical ambition, and whether it works."

## Idea 1: Skill-transfer coach (recommended)

**Story:** about 3.8 million US manufacturing jobs may be needed by 2033, and about 1.9 million could go unfilled ([Deloitte and Manufacturing Institute, 2024](https://themanufacturinginstitute.org/manufacturers-need-as-many-as-3-8-million-new-employees-by-2033/)). Experts retire and their know-how leaves with them. The product turns one expert video into a checked procedure and coaches a novice through it.

**Prior art, honestly:** this space has funded players. [Carbyn](https://www.carbyn.ai/skilled-trades) targets retiring experts with smart glasses and says it is testing on Meta Ray-Ban. [TrainAR](https://trainar.ai/) turns senior engineers' recordings into AR training. Video-to-SOP tools include [SOPX](https://sopx.io/) and [LeanSuite](https://www.theleansuite.com/sop), and [Retrocausal](https://thescxchange.com/articles/4043-retrocausal-unveils-retroactivity-software-for-improved-quality-control-in-manufacturing-assembly) does assembly mistake-proofing. These are closed commercial products. Our angle is an open, verifiable build on Meta models where every pass or fail shows its evidence frame and abstains when unsure.

**Models used:** Spark 1.3 (video understanding, step extraction with structured output, tool calls), SAM 3.1 (tracking tools and parts in video), Voice Transcribe (the expert's narration and the novice's spoken questions), Muse Image (clean step illustrations from real frames), Glimmer local for the open-weights bonus, the glasses toolkit via the Mock Device Kit.

**Domain choice:** pick a hands-on trade task that is safe, quick to film, and visually checkable, such as soldering a joint, crimping a connector, or changing a bike tube. Avoid cooking (could read as a nutrition coach) and sports (rules discourage sports analyzers).

**Rules risks:** "simple image analyzer" and "basic RAG" are discouraged, so the agent loop (extract, plan, observe, verify, abstain, escalate) must be the centerpiece. No medical content.

**Plan, guaranteed entry first:**

| Tier | Scope | Target |
| --- | --- | --- |
| 0 (guaranteed) | Upload expert video, Spark extracts steps with timestamps and per-step checks (structured JSON), upload novice video, agent reports pass or fail per step with evidence frames. Web app, public repo, 3-minute demo video. | Nov 1, submit early |
| 1 | Live phone-camera loop with spoken feedback, SAM 3.1 tracking of tools and parts, an explicit "not sure, here is why" abstain path, re-recorded demo. | Nov 2 to 3 |
| 2 (stretch) | Glasses feed via the Mock Device Kit, Glimmer running the privacy-sensitive steps locally, Muse Image step cards, shareable procedure links for the viral prize. | Nov 3 to 4 |

**Biggest technical risks, to test on day 1:**
- Video latency and cost of Spark on a 1 to 3 minute clip. The docs state no length limit but I have not seen real timings.
- Per-step pass or fail accuracy from video alone. Mitigation: choose steps with clear visual outcomes, and let the agent abstain.
- Mock Device Kit setup (Android needs h265 video) eats a day. Keep it in Tier 2.

## Idea 2: Self-driving mini-lab agent

An agent plays scientist on a cheap closed-loop experiment: propose a hypothesis, run it on hardware, read the sensor and camera, update, and verify its own conclusion. Fits "Push the Frontier" (accelerating a scientific experiment) and verifiable agents. The open-source [self-driving-lab-demo](https://github.com/sparks-baird/self-driving-lab-demo) (Pico W, RGB LED, light sensor, under 100 USD) has a simulation mode and a public remote instance. I found no LLM-driven version of it. Risks: hardware shipping time, and the impact story is more abstract than a worker-shortage story. Good second choice if you own microcontroller kits.

## Idea 3: Energy retrofit agent (backup)

See `research.md`. Strong impact story and clear open-weights angle with Glimmer. Weaker live demo (a walkthrough ending in a dollar figure), and commercial neighbours exist (Kelvin and others).

## Idea 4: Verifiable repair agent

See `research.md`. Busy with funded vendors (ResolveGrid, ChargePoint, FixMynd) and easy to read as basic RAG over manuals.

## Open questions for Vibhor

- Do you own Meta glasses, a 3D printer, or microcontroller kits? It changes whether Idea 2 is practical.
- Which hands-on task can you film well with the equipment you already have?
- Okay to lead with the skill-transfer coach and keep the energy retrofit agent as the fallback?
