# Shared spike plan: live guide engine (cooking and assembly)

2026-10-26. One test harness and one set of pass marks for the live guide, so the same engine can be judged on a cooking task and on a flat-pack assembly task. Marks come from `build-plan.md` (day-1 test) and are applied equally. Spikes are throwaway; product code starts Oct 27. **Every vision test needs the Meta API key, which waits on credit approval.** Everything before the first API call (buying, filming, labeling, writing the harness) can be done now.

## 1. Which flat-pack item to buy
Pick for testability, not for use. Criteria:
- **Small and low-risk:** a stool, side table, small shelf or shoe rack. Nothing load-bearing or safety-critical (no bunk beds, wardrobes, or wall-mounted units).
- **15 to 30 steps** in the manual, about 10 to 20 minutes to build.
- **A clear PDF manual you can download before buying.** Open the PDF, confirm the diagrams are legible and the steps are numbered. The product page link to the manual is the check. I did not research specific products, so verify these properties on the actual listing.
- **Look-alike parts:** at least two screw lengths that differ by a few millimetres, two similar dowels, and two panels that look alike but differ in drilled holes or edge finish. This makes wrong-part detection testable.
- **Reversible mistakes:** parts that can be installed backwards without damage, so you can stage errors and undo them.
- **Cost:** a low price is fine; buy two if the budget allows, so the staged mistakes do not wear out the one set.

## 2. What to film
Fixed phone position on a stand or stack of books, about 1 metre above the workspace, in normal room light, same position for all clips. Film each clip in landscape, 1080p, and note the start time of each step.
1. **Clean build:** one full uninterrupted run, narrated in your normal way, for the manual-to-steps and stage tests.
2. **Stage stills:** at the end of each step, hold still for 3 seconds. Cut 30 frames at known steps (this is the ground truth).
3. **Five deliberate mistakes**, each filmed as its own 20 to 40 second clip: a panel on backwards, the wrong screw length, a missing washer or cam lock, parts assembled in the wrong order, a step skipped.
4. **Five correct controls** of the same steps filmed the same way (for the false-alarm count).
5. **Voice commands:** record yourself saying "next", "repeat", "which screw is this?" and "wait, go back" in English, Hindi and a mix, with the phone at normal distance and kitchen or room noise.
For the cooking task, use the dish and clips from `build-plan.md` with the same structure: stage stills, five deliberate mistakes, five controls.

## 3. Ground truth and labeling
- One spreadsheet per task: step id, step name, plain-language check, expected state, timestamp, whether the clip is a mistake or a control, and the mistake type.
- Label before running any model. Do not tune prompts on the held-out set; keep 10 frames and 2 mistake clips aside for tuning and use the rest only for scoring.
- Save raw model outputs with the frame id, latency, token counts and cost per call.

## 4. Tests and pass marks (same for cooking and assembly)
| # | Test | How | Pass mark |
| --- | --- | --- | --- |
| 1 | **Stage or step recognition** | 30 frames at known steps; ask Spark 1.3 which step each shows, given the step list | at least 80% correct |
| 2 | **Mistake catch** | 5 mistake clips, 3 sampled frames each plus current step | catches at least 4 of 5 |
| 3 | **False alarms** | 5 correct control clips | at most 1 false alarm in 5 |
| 4 | **Manual or video to steps** | Assembly: manual PDF to numbered steps with checks. Cooking: expert video to steps. | no missing or invented steps in 3 of 3 manual sections or clips |
| 5 | **Latency** | 3-frame call with the current step, 20 calls | average under 5 seconds |
| 6 | **Voice commands** | Voice Transcribe on the 5 command phrases in 3 languages and noise | at least 80% of commands understood per language; report Hindi and mixed separately |
| 7 | **Abstain behavior** | 10 deliberately ambiguous frames (hand covering part, blur) | asks or waits on at least 7 of 10 instead of guessing |
| 8 | **Cost** | sum of cost per call | report cost per 10 minutes of guidance against the $150 credit |

## 5. Decision rules
- Same as `build-plan.md`: if tests 1 and 5 fail for a task, that task falls back. If test 2 fails but 1 and 5 pass, narrow the agent to coarse, visible claims (part present or absent, step done or not) and make it ask when unsure.
- **Choose the demo task after the spike:** assembly if test 1 and test 2 pass on assembly and cooking is weaker; cooking if the expert footage is strong and cooking passes; if both pass, choose by which has the better demo footage. If both fail, drop the live guide and compare the other finalists.
- A test counts only if run on frames not used for tuning.

## 6. Timeline
| When | What |
| --- | --- |
| Oct 26 evening | Pick and buy the kit (or buy in a local store if same-day), download and read the manual, set up the stand, write the labeling sheet, write the harness (frame cutting, call, scoring) with a dry run on stub outputs |
| Oct 26 to 27 | Film the clean build, stage stills, mistakes, controls and voice commands |
| Oct 27 morning | When the key arrives, run tests 1 to 8, record results in a table |
| Oct 27 noon | Decision on demo task; start product code with the winner |

## 7. Open items
- **Meta API key and credit approval:** needed for every vision test; nothing here runs without it.
- Whether the key is a team-level or personal key: not confirmed.
- The "live" latency in a real loop (frame capture, upload, reply) may be worse than the isolated API call in test 5; measure end to end in the first product prototype.
