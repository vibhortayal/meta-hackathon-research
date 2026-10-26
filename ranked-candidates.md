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
| 4c | **Faceless Studio** (voice or text idea to a persistent-persona comic; sports clips as a second mode) | about 6.8 | Plausible need, strong creative and viral shape | Crowded category; thin evidence; consistency untested; conflicts with the anti-slop theme unless human-authored and labelled (`faceless-creator-candidate.md`) |
| 4b | **Play to Comic** (game clip to comic or animated short) | about 6.7 | Best viral and demo shape; Muse Image is the star | Lowest Impact; no Meta video output so "animated" means stills plus motion; likeness policy and consistency untested; separate repo from Khelo (`play-to-comic-candidate.md`) |
| 2b | **Manual Whisperer** (variant of the live guide: manual PDF to live, verified assembly or repair guidance, fade-out) | about 7.4 | Same engine as cooking, no expert to film, no food-health risk, survey-backed everyday pain (about half assemble flat-pack wrongly at least once, Galaxus/YouGov) | Gemini Live and research prototypes exist; part vision and live lag untested; loses the real-expert-voice story (`screen-light-ideas.md`) |
| 4 | **Paper Games (teach it any game by talking)** | about 6.9 | Most shareable and finishable | Lowest Impact |
| 5 | **Scam second opinion for families** | about 6.1 | Vivid, local mode credible | Crowded with [Norton Genie](https://us.norton.com/products/genie-scam-detector); "simple analyzer" label; Meta docs show no audio-deepfake detector |
| 6 | **League and tournament organizer agent** | about 6.7 | Fits his own app, if it is close to this | Prior art for scheduling; the gap is untested; I do not know what his app does |
| 7 | Slop or fake-review shields | not scored | His own wish ("protect me from AI") | Thick prior art (on-device slop blockers, self-hosted digests) and thin evidence of unmet demand |

## Top two to compare head to head

1. **Home brain / chief of staff** for fit, passion, local-first, open weights.
2. **Cooking guide** for demo strength and rubric fit.

**Floor under both:** Paper Games as a small, finishable fallback or an in-product delight.
**Wildcard worth one conversation:** caregiver organizer, if he has first-hand access to caregivers.

## Hardware update (Vibhor, Oct 26)
No 24 GB GPU and none soon. A new Mac is possible next month, after the hackathon. No kitchen tablet, but he could get one; a phone is enough for the demo.

What changes:
- **For Oct 31, open-weights Glimmer runs hosted**, not on his machine: Fireworks, Together or OpenRouter (listed as hosts in the Glimmer docs), or Baseten and Modal credits for self-managed endpoints. Fireworks' $25 credit is only for shortlisted teams, so budget the $150 Meta credit and $100 Modal credit first.
- **The privacy story must say so plainly:** "model weights are open and portable; for the hackathon they ran on a hosted endpoint; the same code runs on your own hardware." Do not use "never leaves my machine" in the video. The claim that holds is: open weights, no vendor lock-in, your memory in your own database, and a documented local path.
- **Local path (documented, not demonstrated):** Glimmer Q4_K_M is 16.8 GB plus a 1.4 GB vision file, so it needs a Mac with roughly 32 GB unified memory or more to be comfortable. llama.cpp supports Apple Silicon in general, but I have **not verified** Glimmer speed or support on a Mac, nor MLX support. Say "designed for" and not "tested on" unless he tests it.
- **Open-weights bonus still fits** because the prize is about building on Glimmer or Spark Open, not about where it runs. A hosted-Glimmer entry with a clear local path is valid; a demonstrated local run would be stronger.
- **Kitchen tablet:** optional. The "board that answers back" demo can show the redrawn board on the phone.
- **Spikes:** run the whiteboard read on Spark 1.3 and on hosted Glimmer (not local). The pass thresholds are unchanged.

Project memory records his current laptop as a 2015 MacBook Pro with no GPU, so a local Glimmer test waits for the new Mac. No further hardware question is open.

## What decides it (cheap spikes today and tomorrow, before product code on Oct 27)
1. **Whiteboard read:** 5 photos of the real board to Spark 1.3 and to Glimmer. Pass at 85% of cells on Spark, 70% on Glimmer. Failing Spark kills option 1.
2. **Cooking day-1 test** from `build-plan.md`. Failing kills option 2.
3. **Office hours question** (Discord, 10 to 11 AM ET weekdays): does a local-only product satisfy "live product", and is a coach or planner acceptable?
4. **Two answers from Vibhor:** does he have a 24 GB GPU, and what does his tournament app do today?

If both pass, choose by what he will still use in December. If only one passes, that one wins.

## Rubric evaluation (Stage 1 and Stage 2) of the top three

Stage 1 is pass/fail: fits a theme ("Build for Your World" or "Push the Frontier") and genuinely uses Meta models. Stage 2 is scored 0 to 10 with weights Impact 30, Meta tooling 25, Demo 25, Depth 20. All scores are my judgement. **Assumption-based** means the score rests on something untested.

| Criterion | Household home brain | Cooking guide | Caregiver organizer |
| --- | --- | --- | --- |
| Stage 1 theme and real Meta use | Pass (Build for Your World; Spark vision, tools, Voice, hosted Glimmer) | Pass (same; video, SAM, Voice) | Pass (Spark vision, structured output, tools) |
| Impact (30%) | 6. Universal pain and real evidence for "time", but reads as convenience and the category is funded. Raise it by quantifying minutes saved over a week of real use and showing a second household. | 6. Relatable, but a cooking demo can look small. Raise it with the tradespeople knowledge-capture story and the fade-out measure. | 8. Specific person, strong numbers (63M caregivers, 27 hours a week). Raise it with a real caregiver's case. |
| Meta tooling (25%) | 8. Vision, tool calls, Voice Transcribe, structured output, hosted Glimmer, optional Muse Image. Raise it with Glimmer plus Spark escalation visible in the log. | 9. Video, SAM 3.1, Voice realtime, tool calls. | 7. Vision and structured output mainly. |
| Demo (25%) | 7. Board photo, redrawn week, a quiet nudge and the bad-day exit tell a story, but the payoff is an absence of chaos. **Assumption-based:** needs the whiteboard read to be accurate and a consenting staged household. | 9. Live attempt, real expert voice, visible fade-out. **Assumption-based:** live latency (2 to 5 s) and mistake detection are untested. | 6. Document photos to schedule is clear but less vivid. |
| Technical depth (20%) | 8. Persistent state, multi-source merge, conflict detection, code-enforced nudge policy, abstain-and-ask, egress log. **Assumption-based:** local-model tool calling is untested. | 7. Frame loop, step state machine, verification with abstain. | 6. Extraction pipeline; thinner agent loop. |
| **Weighted total** | **7.2** | **7.7** | **6.9** |
| What is still untested | Whiteboard handwriting accuracy; the capture habit; hosted Glimmer vs Spark quality | Live latency; mistake detection; Hindi clip quality | Document variety; medical-advice boundary |

Reading: cooking wins on rubric if its day-1 test passes; household is close behind and clearly wins on personal fit and open-weights story; the caregiver organizer wins on Impact alone but loses on Demo. Stage 3 (live finals) will favor whichever tells the clearer human story in 3 minutes.

## Household demo: the key moment
Tuesday, 5:40 PM. His wife's flight lands late and the whiteboard says chicken needs thawing. The agent, which read the board photo and the forwarded flight email, quietly rewrites the evening and sends one nudge. Then he taps "bad day": the plan is dropped, nudges go silent, dinner is re-planned in seconds, and the **board image redraws itself** with tomorrow reshuffled and no guilt. The final shot is the log showing exactly what left his machine (nothing, or one approved crop). If staged with synthetic or consenting data, the peak is the redrawn board plus the silence.

## Prior-art scan (live assistants)
See `prior-art-live-assistants.md`. Google, OpenAI and Meta already ship live camera chat, so "live camera assistance" is not a differentiator. Open: manual- or expert-grounded step state, shown evidence, ask-when-unsure, fade-out, Hindi-English, open weights. No scores changed; the mistake-catch test is the main risk (research reports persistent VLM weakness on procedural errors).
