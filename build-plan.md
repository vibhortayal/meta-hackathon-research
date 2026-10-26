# Build plan v2: live expert guide (working title, cooking demo)

Updated 2026-10-26 after the problem-first review (`problem-framing.md`). Items marked **Pending** need Vibhor's decision. Fallback idea if this fails the day-1 test: energy retrofit agent (`research.md`).

## One-line pitch

A hands-free AI that guides you through a hands-on skill while you do it, using an expert's real video as its knowledge, and gradually goes quiet as you get better, so you end up more capable instead of more dependent.

## Open decisions (Vibhor)

1. **Expert source for the demo.** Option A (recommended): a family member or friend films one dish for 3 to 5 minutes, talking naturally, and the agent plays back their real recorded words at the right moment. Option B: a generic expert video we film ourselves, with the fade-out feature as the main human story.
2. **Languages.** The expert may speak Hindi, English or a mix. Confirm which language the guidance should come in.
3. **Dish.** A simple technique with clear visual stages (for example folding an omelette, shaping a dumpling, dicing an onion).
4. **Setup items I'm waiting on:** the Meta API key as an environment secret (not in chat), and an empty public build repo (for example `vibhortayal/skill-coach`).

## What it does

1. **Learn:** the expert films a short technique once while narrating. Hindi, English or mixed.
2. **Procedure:** the agent turns the video into numbered steps. Each step has a plain-language check ("pan is hot enough when...", "fold is even"), the timestamp that shows it, and the expert's own spoken words for that moment.
3. **Live guide:** the user props up the phone and wears headphones. The agent watches sampled camera frames and guides the user through the steps, speaking up at step changes and on clear mistakes. The user can interrupt by voice with questions.
4. **Verify:** at each step the agent decides if the step is done, wrong or unclear, and keeps the evidence frame behind its call. When it cannot tell, it asks or waits instead of guessing.
5. **Fade out (the human story):** full guidance on the first attempt, fewer hints each time the user succeeds. The demo shows the agent going quiet on the second attempt. An independence measure (hints needed per attempt) falls over attempts and is shown on screen.
6. **Real expert voice (Option A, Pending):** the agent plays the expert's actual recorded clips at the right moment, chosen by what the camera sees, with a translated caption if the user's language differs. No voice cloning, and only with the expert's consent.

## What makes it an agent, not an analyzer or coach

The agent acts instead of only commenting. It keeps a step-by-step state machine, calls tools (starts a timer when the procedure says "rest 30 seconds", logs completed steps, pauses when the user's hands are busy), decides when to speak or stay quiet, asks when a frame is ambiguous, and converts an expert video into a reusable "expert" that others can load. The demo should show these actions. There is no record-and-review mode, because reviewing a recording is an analyzer, which the rules discourage.

## How "live" works, and its limits

- Meta's API takes video clips and images but has no streaming video session. The live loop is: the browser grabs a frame every 1 to 2 seconds, sends the latest few frames plus the current step and recent history to Spark, and plays the reply through the headphones.
- Voice in: Muse Voice Transcribe realtime. Voice out: the browser's speech synthesis (Meta has no text-to-speech), plus the expert's real clips in Option A.
- Expect 2 to 5 seconds of lag per reply. This is an estimate until the day-1 test measures it.
- If live is slow, fall back to a simpler live mode: lower frame rate, speak only at step changes, answer voice questions from the last few frames.

## Languages

- Voice Transcribe has a language-bias setting for 25 languages (list not confirmed). Glimmer was trained on 100+ languages. Spark's coverage is unconfirmed.
- Day-1 test: one Hindi clip, one English clip, one mixed Hindi-English clip. Check transcription quality, translation by Spark, and which language the spoken guidance can use.

## Rules, rights and guardrails

- Technique only. No calories, nutrition, allergens, diets, or food-safety health claims. No grief or memorial positioning; use living, consenting experts only.
- The agent loop (extract, observe, decide, act, verify, ask) is the centerpiece, not one image-analysis call.
- Product code is written from Oct 27. Today is for planning and throwaway spikes only. The participant guide says the building period is Oct 27 to Nov 4 and the demo may show only work built in it.
- The submitted demo uses only footage we film or have permission for. The product has no YouTube or Instagram downloader, and we do not download from those sites for tests, because YouTube's terms bar downloading and automated access without permission. Test with clips we film or creator-offered Creative Commons files.
- Credit any open-source libraries used. The public build repo is separate from this private research repo.

## Stack

- Next.js (TypeScript) web app, mobile-first so the phone browser streams the camera. Deployed on Vercel.
- Meta Model API through the OpenAI SDK pointed at `https://api.meta.ai/v1` (Responses API, structured output, tool calls).
- `muse-spark-1.3` for video understanding, step extraction, live guidance and verification. SAM 3.1 for tracking tools and food (Tier 1). Muse Voice Transcribe realtime for mic input. Browser speech synthesis for spoken guidance.
- Glimmer running locally for the privacy-sensitive parts is the open-weights bonus attempt (Tier 2).
- If video upload is slow or unreliable: sample frames in the browser and send up to 50 images per request.

## Tiers and schedule (deadline Nov 4, 9 PM ET)

Vibhor's target: **all building done by Oct 31**, leaving Nov 1 to 3 for video prep and Nov 4 as buffer. Oct 31 is a hard feature freeze. Anything unfinished then is cut.

- **Tier 0 (safe entry):** expert video to steps, working live guide with voice in and out, public repo, deployed.
- **Tier 1:** agent actions (state machine, timers, speak or stay quiet, ask when unsure), voice interruptions, fade-out with independence measure, SAM 3.1 tracking, real expert clips (Option A).
- **Tier 2 (stretch, only if Tier 1 is solid):** Glimmer local run for the open-weights bonus, shareable "expert" links.

| Date | Goal |
| --- | --- |
| Oct 26 (today) | Lock idea and open decisions. Add the API key as a secret. Spike only: one 60-second cooking clip to Spark 1.3 (latency, cost, step quality), plus the Hindi, English and mixed language test. Decide video versus frame sampling. |
| Oct 27 | Create the public build repo. Backend: expert video to structured steps JSON with checks, timestamps and expert quotes. Attend Agents 101. |
| Oct 28 | Minimal live loop: frames every 2 seconds plus current step to Spark, reply spoken through the headphones. Attend Agents 102 (verifiable agents) and apply it. |
| Oct 29 | Web UI and deploy. **Tier 0 submitted** as the safe entry (if the platform allows later edits). |
| Oct 30 | Tier 1: agent actions, voice interruptions, fade-out and independence measure, expert clip playback. Attend the Fireworks session. |
| Oct 31 | Tier 1 hardening on test runs (guidance accuracy, ask behavior, error handling, spend cap). Tier 2 only if already working. **Feature freeze at end of day.** |
| Nov 1 | Demo script, shot list, rehearsal. Record take 1 of the 3-minute video. README and repo cleanup. |
| Nov 2 | Re-record and edit the final video. Optional Glimmer polish only if it cannot break the demo. |
| Nov 3 | Final submission on the Cerebral Valley platform with repo, video and contributor list. Last day for questions to organizers. |
| Nov 4 | Buffer only. Hard deadline 9 PM ET. |

## Demo video (3 minutes), recorded Nov 1 to 2

Write the script first, rehearse with a timer, open with the person, not the technology.

1. 0:00 to 0:20: the problem (skills live in people's hands, AI that does things for us leaves us less capable).
2. 0:20 to 0:50: the expert films the dish once. Steps appear.
3. 0:50 to 2:10: first attempt, live. Agent guides, plays the expert's words, catches a real mistake with the evidence frame, asks when unsure.
4. 2:10 to 2:40: second attempt, the agent goes quiet. Independence measure drops. Name the Meta models used.
5. 2:40 to 3:00: where it goes next (retiring tradespeople's know-how, other languages).

## Scoring alignment

| Rubric | How the plan earns it |
| --- | --- |
| Impact 30% | Counters skill fade-out and loss of hands-on know-how; scales to trades (up to 3.8M US manufacturing jobs needed by 2033, about 1.9M could go unfilled per Deloitte and the Manufacturing Institute) |
| Meta tooling 25% | Spark video and tool calls, SAM 3.1 tracking, Voice Transcribe realtime, Glimmer local |
| Demo 25% | Live first and second attempt on camera, real expert voice, visible fade-out |
| Depth 20% | Frame-sampling live loop, step state machine, verification with abstain, expert-clip retrieval |

## Risks and checks

- **Live lag and accuracy:** unknown until the day-1 spike. If unreliable, narrow to steps with clear visual outcomes and speak only at step changes.
- **Reads as a coach:** mitigated by agent actions and the fade-out, but the judges' reading is not predictable.
- **Gimmick risk of the expert voice:** needs a good source clip. Option B remains available.
- **Submission edits:** confirm on the Cerebral Valley platform whether a submission can be updated after Tier 0.
- **Spend:** hard spend cap in code. The Discord notes say a spend-limit notification does not stop billing.
- **Credits:** $150 covers a lot of Spark use, but frequent live calls add up. Cache expert-video results and limit frames per call.
