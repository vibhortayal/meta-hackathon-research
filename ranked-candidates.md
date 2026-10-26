# Ranked candidates (synthesis of all research so far)

2026-10-26. Scores are my judgement, not data. Evidence strength comes from the sibling files: [literature-review.md](literature-review.md) (31 sources opened, 5 strong, 19 moderate, 6 weak, 1 anecdotal), [unmet-needs-landscape.md](unmet-needs-landscape.md) (about 40 sources, roughly half read via search summaries), [human-voices.md](human-voices.md) (about 38 quotes, Reddit blocked), [magical-ideas.md](magical-ideas.md), and [household-agent-candidate.md](household-agent-candidate.md). Immigration copilot was dropped by Vibhor.

## What the evidence supports, and where it is thin

- **Strong or moderate:** people's top fear is unreliability (26.7% of 80,508 Claude users in [Anthropic's interviews](https://www.anthropic.com/features/81k-interviews)); "life management" and "time freedom" are 24.6% of primary hopes in the same study (a sample of Claude users, so skewed toward AI fans); 71% of Americans expect AI to make personal information less secure ([Pew 2026](https://www.pewresearch.org/internet/2026/06/17/americans-and-ai-2026/)); cognitive labor (anticipating, deciding, monitoring) is a real, studied part of household work ([Daminger](https://dash.harvard.edu/server/api/core/bitstreams/0594bb9c-1c9d-4f31-bcde-00ad47bf3d7c/content), 76 couples, moderate); agents are inconsistent across repeats ([τ-bench](https://arxiv.org/abs/2406.12045)), which backs "ask or abstain" and a nudge budget; a cloud-dependent home robot company shut down and bricked its product ([The Register](https://www.theregister.com/2024/12/16/moxie_cloud_services_lessons/)).
- **Thin:** no peer-reviewed study of why family calendars get abandoned (the key paper was blocked); nothing tests whether a vision model can read a whiteboard; nothing tests small local models on personal tool calling; AI-specific scam figures are missing; notification-fatigue evidence is a 20-user study plus health-app literature.
- **Implication:** Vibhor's own account is the best evidence for the household problem. The numbers back "time" as a universal wish, not "this particular product works."

## Ranking

| Rank | Candidate | Weighted (mine) | Why | Biggest risk |
| --- | --- | --- | --- | --- |
| 1 | **Household chief of staff as the "home brain" (stage 0)**: builds the week from the whiteboard photo and forwards, nudge budget, bad-day exit, local-first on Glimmer, roadmap to an upgradable robot | about 7.1 | Only candidate that solves a problem he lives, keeps him building after Nov 4, has the best open-weights story, and the shutdown of Moxie gives a real reason for local-first | Weak demo payoff; capture depends on him photographing and forwarding; unproven whiteboard read |
| 2 | **Live expert guide with fade-out (cooking)** | about 7.4 (range 7.4 to 8.3) | Best demo and Meta-tool use; plan and day-1 test already exist | Coach label; live lag and accuracy unmeasured; lower personal pull |
| 3 | **Family caregiver handoff and paperwork organizer (non-medical)** | not scored by me; ranked 2 in the unmet-needs survey | Strongest sourced numbers (63M US family caregivers, 27 hours a week, 11% trained, per AARP and NAC 2025, as reported in the sibling file) and no direct competitor found | Medical-advice boundary; sensitive photos; weak personal fit unless he knows caregivers |
| 4 | **Paper Games (teach it any game by talking)** | about 6.9 | Most shareable and finishable | Lowest Impact |
| 5 | **Scam second opinion for families** | about 6.1 | Vivid, local mode credible | Crowded with [Norton Genie](https://us.norton.com/products/genie-scam-detector); "simple analyzer" label; Meta docs show no audio-deepfake detector |
| 6 | **League and tournament organizer agent** | about 6.7 | Fits his own app, if it is close to this | Prior art for scheduling; the gap is untested; I do not know what his app does |
| 7 | Slop or fake-review shields | not scored | His own wish ("protect me from AI") | Thick prior art (on-device slop blockers, self-hosted digests) and thin evidence of unmet demand |

## Top two to compare head to head

1. **Home brain / chief of staff** for fit, passion, local-first, open weights.
2. **Cooking guide** for demo strength and rubric fit.

**Floor under both:** Paper Games as a small, finishable fallback or an in-product delight.
**Wildcard worth one conversation:** caregiver organizer, if he has first-hand access to caregivers.

## What decides it (cheap spikes today and tomorrow, before product code on Oct 27)
1. **Whiteboard read:** 5 photos of the real board to Spark 1.3 and to Glimmer. Pass at 85% of cells on Spark, 70% on Glimmer. Failing Spark kills option 1.
2. **Cooking day-1 test** from `build-plan.md`. Failing kills option 2.
3. **Office hours question** (Discord, 10 to 11 AM ET weekdays): does a local-only product satisfy "live product", and is a coach or planner acceptable?
4. **Two answers from Vibhor:** does he have a 24 GB GPU, and what does his tournament app do today?

If both pass, choose by what he will still use in December. If only one passes, that one wins.
