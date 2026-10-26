# Build plan: skill-transfer coach (cooking-technique demo)

Decided 2026-10-26: build the skill-transfer coach, demoed on a simple cooking-technique task, using a phone camera and headphones. Fallback idea: energy retrofit agent (`research.md`).

## What it does

1. **Learn:** the expert films a short technique once (for example folding an omelette, dicing an onion, or shaping a dumpling) while narrating.
2. **Procedure:** the agent turns that into numbered steps, each with a plain-language check ("pan is hot enough when...", "fold is even") and the timestamp that shows it.
3. **Coach and verify:** a novice films their attempt. The agent says pass, fail or not sure for each step, shows the evidence frame behind every verdict, and explains the fix. When it cannot tell, it says so instead of guessing.

## Guardrails for the rules

- Coach technique only. No calories, nutrition, allergens, diets or food-safety medical claims, so it can't read as a nutrition coach or health advice.
- The agent loop (extract, observe, verify, abstain) is the centerpiece, not a single image-analysis call.
- Product code is written from Oct 27. Today is for planning and throwaway spikes only. The participant guide says the building period is Oct 27 to Nov 4 and the demo may show only work built in it.
- Credit any open-source libraries used. Public repo for the build is separate from this private research repo.

## Stack

- Next.js (TypeScript) web app, mobile-first so the phone browser streams the camera. Deployed on Vercel.
- Meta Model API through the OpenAI SDK pointed at `https://api.meta.ai/v1` (Responses API, structured output, tool calls).
- `muse-spark-1.3` for video understanding, step extraction and verification. SAM 3.1 for tracking tools and food in video (Tier 1). Muse Voice Transcribe realtime for headphone mic input. Browser speech synthesis for spoken feedback (Meta has no text-to-speech).
- Fallback if video upload is slow or unreliable: sample frames in the browser and send up to 50 images per request.

## Schedule (deadline Nov 4, 9 PM ET)

Vibhor's target: **all building done by Oct 31**, leaving Nov 1 to 3 for video prep and Nov 4 as buffer. Oct 31 is a hard feature freeze. Anything unfinished then is cut, not carried over.

| Date | Goal |
| --- | --- |
| Oct 26 (today) | Lock idea. Claim Meta credits (done) and add the API key as an environment secret. Spike only: send one 60-second cooking clip to Spark 1.3 and record latency, cost and step quality. Decide video versus frame-sampling. |
| Oct 27 | Create the public build repo. Tier 0 backend: expert video to structured steps JSON with checks and timestamps. Attend Agents 101. |
| Oct 28 | Tier 0: novice video to per-step verdicts with evidence frames and an explicit "not sure" path. Attend Agents 102 (verifiable agents) and apply it. |
| Oct 29 | Tier 0 web UI, deploy. **Tier 0 submitted** as the safe fallback entry (if the platform allows later edits). |
| Oct 30 | Tier 1: live phone-camera loop, headphone voice in with spoken feedback out, SAM 3.1 overlay. Attend the Fireworks session. |
| Oct 31 | Tier 1 hardening on a test set of clips (verdict accuracy, abstain behavior, error handling, spend cap). Tier 2 items only if they are already working; otherwise cut. **Feature freeze at end of day.** |
| Nov 1 | Demo script, shot list, and practice clips. Record take 1 of the 3-minute video. README and repo cleanup. |
| Nov 2 | Re-record and edit the final video. Optional Tier 2 polish only if it cannot break the demo (Glimmer local run, step cards). |
| Nov 3 | Final submission on the Cerebral Valley platform with repo, video and contributor list. Last day for questions to organizers. |
| Nov 4 | Buffer only: fix a broken link or upload, resubmit if needed. Hard deadline 9 PM ET. |

Tier 2 is now mostly a stretch beyond the freeze. The open-weights bonus (Glimmer) is the one Tier 2 item worth trying to land by Oct 31, since it adds a prize chance and shapes the story.

## Demo video (3 minutes), recorded Nov 1 to 2

Rehearse with a timer, write the script before recording, and open with the user problem. Every second should earn its place.

1. 0:00 to 0:20: the problem (experts hold know-how, novices struggle, nobody to watch them).
2. 0:20 to 1:00: expert films the technique, steps appear.
3. 1:00 to 2:20: novice attempts it live, agent catches a real mistake with the evidence frame, fix, retry, pass.
4. 2:20 to 2:50: show the "not sure" case and the verification detail, and name the Meta models used.
5. 2:50 to 3:00: where it goes next (other trades, glasses).

## Risks and checks

- **Video accuracy and latency:** unknown until the Oct 26 spike. If per-step verdicts are unreliable, narrow to steps with clear visual outcomes.
- **Submission edits:** confirm on the Cerebral Valley platform whether a submission can be updated after Tier 0.
- **Spend:** set a hard spend cap in code. The Discord notes say a spend-limit notification does not stop billing.
- **Credits:** $150 covers a lot of Spark use, but video and many verification calls add up. Cache and reuse expert-video results.
