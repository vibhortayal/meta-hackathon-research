# Screen-light ideas: AI that works through the physical world, voice and agency

2026-10-26. Lens from Vibhor: ideas that feel intuitive, use AI, give people more agency, and take humans away from screens. Scores are my judgement. Constraints I keep in mind: **no Meta model outputs video or audio** (voice out is the browser's speech synthesis), phone camera and headphones only, no GPU, hosted open weights, building starts Oct 27.

## What counts as "screen-light" here
Input comes from paper, objects, rooms or speech. The phone stays in a pocket or propped up. The human does the hands-on thing, and the AI helps, asks before acting, and ideally fades out. Output is spoken, printed or physical, with a screen as the exception.

## Which existing ideas already fit
| Idea | Fit | Why |
| --- | --- | --- |
| Cooking guide (`build-plan.md`) | Strong | Hands busy, headphones, fade-out measure, user stays the actor |
| Paper Games | Strong | Play happens on paper; the phone only watches and speaks |
| Household "Homebase" | Partial | The whiteboard is physical, but nudges and confirmations are on the phone. A voice-first variant is below. |
| Play to Comic | Partial | Input is real play outside; output is a screen artifact |
| Faceless Studio | Weak | Screen-heavy creation tool |
| Khelo / sports organizer | Weak | App-centric |

## New ideas and variants

### A. Manual Whisperer (assembly and repair guide from the manual) — **new, and the strongest**
- **Pain:** flat-pack assembly. In a Galaxus/YouGov survey of 5,226 people in five countries, about half said they had assembled flat-pack furniture wrongly at least once and just over 20% had argued with a partner while doing it ([Galaxus](https://www.galaxus.de/en/page/build-it-yourself-furniture-italys-couples-argue-over-flatpacks-germanys-cant-be-bothered-with-them-43028), consumer survey); a Canstar Blue poll of 2,500 New Zealanders found 36% had trouble ([ODT](https://www.odt.co.nz/node/219158)). Moderate evidence for a mundane, universal pain, and a couples-conflict angle that matches Vibhor's dinner-fight theme.
- **What it does:** you hand it the manual PDF, lay out the parts, and prop up the phone. It sorts the parts by sight, speaks one step at a time, and checks each step against the camera. It says "that screw is in the wrong hole, here is the one" and asks when unsure. It speaks less as you get faster.
- **Meta models:** Spark reads the manual PDF (first 50 pages as images are supported per the docs), Spark vision plus SAM 3.1 find parts, Voice Transcribe takes your questions, tool calls hold a step state machine, browser speech synthesis speaks.
- **Same engine as the cooking guide.** The knowledge source is a manual PDF instead of an expert video. It removes the dependency on filming a family expert, and removes food-health claims.
- **Prior art (real, not empty):** Gemini Live reportedly helped a reviewer sort parts and build a drawer chest, but without per-step verification ([Android Authority](https://www.androidauthority.com/gemini-live-ikea-assembly-3614666), anecdotal review); academic prototypes verify steps by image comparison ([CNN-based app](https://repository.adu.ac.ae/items/122e062a-d6e3-45f7-ae85-2945a120541f)); FixMode is a general repair app with live camera guidance. I found no public app that verifies each step against the official manual with shown evidence. That is a search absence only. **Big-tech assistants are the real competitor.**
- **Rules:** not a simple image analyzer (it plays a step-by-step agent role); not RAG (it acts on live frames). Avoid safety claims on load-bearing items; keep demo furniture low-risk.
- **Demo moment:** a cheap shelf kit on the floor; the agent catches the wrongly oriented panel before the screws go in, shows the frame that proves it, and goes quiet on the second shelf.
- **Risks:** small-part vision accuracy and live lag are untested; Gemini Live comparison; needs a flat-pack kit (cheap).
- **Tiers:** Tier 0 by Oct 29: manual to steps, voice step-by-step, user says "next" (no vision). Tier 1 by Oct 31: camera verification with abstain-and-ask, fade-out, evidence frames. Tier 2: part sorting with SAM, repair mode.

### B. Walk-and-Talk Homebase (voice-first household variant)
Phone in the pocket and earbuds in. A two-minute spoken check-in at set moments ("what changed today?"), at most three questions, the board photo as the only screen moment. Same engine as `household-agent-candidate.md`. Caveat: a screenless product is hard to show in a video, so the demo needs the board, the kitchen, and the audio on screen. Meta: Voice Transcribe, Spark, tools, hosted Glimmer.

### C. Yard Rules (Paper Games outdoors)
A rule-keeper for kids' made-up outdoor games, or house rules for cards and board games: it listens to the agreed rules, keeps score by voice, and settles disputes by quoting the rules the group agreed to, never by inventing new ones. Takes the phone away from play. Same rule-compiler as Paper Games. Voice-only input outdoors is noisy and untested.

### D. Storybook from a kid's drawing
A child draws and tells a story; the agent turns it into a short illustrated book with Muse Image that the parent prints and reads aloud. Screen-away, creative, strong for Best Creative Build. Caveats: I do not know whether Vibhor has children; photos of minors need care and consent; an "education chatbot" reading is a risk.

### E. Neighborhood Quest
A family walk where the phone stays in a pocket and occasionally sees something you point at, turning the walk into a quest narrated through headphones. Risks: "simple image analyzer" and "education chatbot" labels, and outdoor lag. Weak.

### F. Analog inbox (mail and sticky notes)
Photograph the mail pile and handwritten notes; the agent files, reminds and drafts. Best as a feature of Homebase, not a product; basic OCR plus reminders reads as an analyzer.

### G. Pocket scorekeeper (voice-only racquet scoring) — **dropped**
Hands-free pickleball scoring is already crowded: apps such as Pickleball Voice Score (on-device), PCKLSCORE, PickleMate and DinkTally announce scores and handle server numbers ([Pickleball Voice Score](https://mwm.ai/apps/pickleball-voice-score/6760217378), [DinkTally](https://mwm.ai/apps/dinktally-pickleball-score/6790180166); store listings, so marketing claims). Not worth building for the hackathon.

### H. Session DJ (voice-guided yoga or workout from your own sequences)
Takes screens away but is health-adjacent (fitness advice is on the discouraged side) and shallow. Weak.

## Rubric (my scores)
| Idea | Impact | Meta | Demo | Depth | Weighted | Screen-light | Rule risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A. Manual Whisperer | 6 | 9 | 8 | 7 | **7.4** | high | low |
| B. Walk-and-Talk Homebase | 6 | 8 | 6 | 8 | 6.9 | high | medium |
| C. Yard Rules | 5 | 7 | 8 | 6 | 6.5 | high | low |
| D. Storybook from a drawing | 5 | 7 | 8 | 5 | 6.3 | medium | medium |
| E. Neighborhood Quest | 5 | 6 | 7 | 5 | 5.7 | high | high |
| F. Analog inbox | 5 | 7 | 6 | 5 | 5.8 | low | medium |
| H. Session DJ | 4 | 6 | 5 | 4 | 4.8 | high | high |

Assumption-based: every vision accuracy and latency figure; Impact for D and E rests on no evidence.

## What this changes in the ranking
- **Manual Whisperer is a strong variant of the cooking guide**, not a competitor. Same engine, same fade-out, but the knowledge source is a manual PDF, so there is no expert to film, no food-health risk, an easier-to-film demo, and a broader audience. It loses the "real expert voice" human story. Recommendation: **build one live-guide engine and pick the demo task after the day-1 test**, cooking if the expert footage is good, assembly if not. This also keeps the 7.4 to 7.7 slot.
- Paper Games stays the strongest small, screen-away idea.
- Homebase gets a voice-first variant but stays a demo-light idea.
- The comic ideas keep their score but do not fit this lens.
