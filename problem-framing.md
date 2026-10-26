# Problem-first check: does the idea solve a human problem and bring joy?

2026-10-26. Evidence quality is stated for each claim. Most is correlational or from press releases, so this is a reasoned argument, not proof.

## Human problems AI has not solved or has made worse

| Problem | Evidence | Evidence quality |
| --- | --- | --- |
| **AI does the task for us, and skills fade.** | The [International AI Safety Report 2026](https://arxiv.org/pdf/2602.21012) cites a study where clinicians' tumour detection without AI dropped 6% three months after AI support was introduced, and a 666-person study linking heavy AI use to lower critical-thinking self-scores via cognitive offloading. | One concrete clinical result. The rest is self-report and correlational. The report itself calls the research "nascent" and notes offloading can also free up effort. |
| **AI lives in a chat box, but the good parts of life are hands-busy.** | No study needed: today's assistants need your eyes on a screen and your hands on a keyboard. | Observation, not evidence. |
| **Know-how in people's hands is never written down, and leaves with them.** | A [UK grandparent survey](https://issuu.com/hubbubuk/docs/2018.09.17_kitchen_love_launch) found almost half had never cooked with their grandchildren. A [White Rose study](https://eprints.whiterose.ac.uk/74458) notes screens can distract children from absorbing tacit cooking skills. Journalists describe recipes as only part of what you need to know. | Company-linked press release plus a small qualitative study. Weak, but consistent. |
| **Doing something new or hard alone.** | Popular-press coverage links shared meals to higher social support and lower loneliness. A 2025 conference abstract found prosocial cooking predicted more positive affect. | Press coverage and an unreviewed abstract. Plausible, thinly supported. |

## What brings joy

Mastery (the pride of making something with your own hands), connection (doing it with someone), and flow (a task matched to your skill). A generic voice that says "lower the heat" delivers utility but not joy, and it sits close to the discouraged "coach" category.

## What this means for the idea

The live guide solves a real problem, but as first framed it is a generic coach. Two changes make it about the human problems above.

1. **Make it the opposite of deskilling: the agent fades out.** It gives full guidance on the first attempt, then fewer hints each time you succeed, and the demo shows it going quiet on the second attempt. An "independence score" (hints needed, falling over attempts) is a measurable, honest outcome. This counters the cognitive-offloading story directly and gives a clear Impact argument: AI that makes you capable instead of dependent.
2. **Make the expert a real person, not a generic voice: "cook with someone who taught you."** A family member or friend films one dish once while talking naturally. During your cook the agent plays back their actual recorded words at the right moment ("wait until it bubbles", "not that much salt"), chosen by what the camera sees. No voice cloning: it uses only their real clips, with their consent. That adds the connection and a reason to share it.

## Honest critique

- **Gimmick risk:** the recorded-voice idea only works if the source clip has natural, usable asides. It needs a good source person and a good dish.
- **Impact score (30%):** a cooking demo may look small. The argument is that the same engine captures retiring tradespeople's know-how, which is a large unfilled-jobs story ([Deloitte and Manufacturing Institute](https://themanufacturinginstitute.org/manufacturers-need-as-many-as-3-8-million-new-employees-by-2033/)). Cooking is the human, relatable demo of it.
- **Rules:** coach technique only, no nutrition, no health claims. Do not position it as grief or memorial technology; keep it to living, consenting people.
- **Technical risks unchanged:** frame-sampling lag (2 to 5 seconds, unmeasured) and verdict accuracy. Matching a recorded clip to the live moment adds a search step that needs testing.

## Decision needed from Vibhor

Is there someone (a family member or friend) who can film one simple dish for about 3 to 5 minutes while talking naturally? If not, the generic expert version still works, with the fade-out feature as the main human story.
