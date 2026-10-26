# Magical ideas: from tic-tac-toe to a time machine

2026-10-26. Vibhor's brief: build something magical, anywhere from "tic-tac-toe" to "time machine," grounded in a real human need or joy, visible to judges in three minutes. Scores are my judgement, not data. **Prior art was not checked for most of these** (marked "not checked"); I only know what the project notes and the Meta docs already say. The literature and human-voices passes are still running and will refine the ranking.

## How to read this

- **Rubric:** Impact 30, Meta tooling 25, Demo 25, Depth 20. Simple ideas lose most on Impact and Depth, so each small idea below says how it earns depth honestly.
- **Feasibility** is a guess at the chance a solid version works by the Oct 31 freeze, solo. Tier 0 is the version I would submit first.
- **Rules (discouraged):** medical or mental-health advice, basic RAG, simple image analyzers, education chatbots, job screeners, nutrition coaches, personality analyzers, sports analyzers, politics or war. A game that watches paper is not an analyzer if the agent plays, decides, and verifies. A tool that only labels a photo would be.
- **Bonus prizes:** Best Agentic ($5K), Best Creative Build ($5K, Muse Image or Wonder), Open Weights ($10K, Glimmer or Spark Open), Most Viral ($20K, X engagement), Community Vote ($10K).
- **Tie to the interview:** each idea names the human need it serves (the dinner scramble, the stale shared calendar, the wish to generate time, the wish for protection from AI, joy with his wife, his tournament app).

## The small end: finishable in a day or two

### S1. Paper Games: teach it any game by talking
- **Need:** screen-free play with a partner or kids; joy; an excuse to be together in the evening.
- **Magic:** draw a grid on paper, explain a game out loud ("three in a row wins, but you can't play in the middle first"), and it plays you on the paper, says its move, and catches illegal moves. Teach it a new game tomorrow by talking.
- **Meta tooling:** Voice Transcribe realtime for the rules, Spark vision to read the sheet, SAM 3.1 to find the grid and marks, tool calls to hold game state and rules, Spark reasoning to induce rules and pick moves.
- **Depth, honestly:** rule induction from speech into a checkable rule set, a game-state machine rebuilt from camera frames, move-legality verification, and a visible "I am not sure what that mark is, is it an X?" abstain step. That fits the "verifiable agents" session on Oct 28.
- **Rules:** safe. Not an analyzer (it plays and verifies). Not an education chatbot.
- **Prizes:** Viral (a clip of a toddler teaching it a made-up game), Creative, Agentic.
- **Weakness:** Impact is the lowest of the lot unless framed around connection and play. Whether play and shared screen-free time have research support is **unverified**; wait for the literature pass.
- **Feasibility:** high (about 75%). Tier 0: tic-tac-toe plus dots-and-boxes by camera. Tier 1: spoken rules for new games. Prior art: not checked.

### S2. The board that answers back
- **Need:** the weekly whiteboard dies when the week changes (interview).
- **Magic:** photograph the whiteboard; the agent reads it, fixes conflicts with flights, and returns a **redrawn board image in handwriting style** that you can show on a cheap kitchen tablet or print. The physical board stays home base, as Vibhor wanted.
- **Meta tooling:** Spark vision for reading, structured output, tool calls, `muse-image-1.0` image edits for the redraw, Voice Transcribe for edits by voice.
- **Weakness:** whether Muse Image keeps handwriting legible is **untested**. If not, fall back to a clean typed board.
- **Prizes:** Creative Build plausible. Open Weights if reading runs on Glimmer.
- **Feasibility:** medium to high (about 65%). Folds into the household agent as its magic moment.

### S3. Charades and Pictionary with a referee that talks back
- **Need:** party play. **Magic:** you draw or act, it guesses live and speaks. **Risk:** latency of 2 to 5 seconds, a "simple image analyzer" reading if it only guesses. **Fix:** it also keeps score, teaches itself house rules, and trash-talks in Hindi or English. **Feasibility:** high, but low Depth. Prior art: not checked.

### S4. Your day as a comic
- **Need:** joy and reflection. **Magic:** at day's end, 6 photos plus a voice memo become a short comic of the day, locally. **Meta tooling:** Spark, Muse Image, Voice Transcribe. **Risk:** low Impact, mostly a feature, not a product. Fits as the weekly recap of the household agent. **Prizes:** Creative, Viral.

### S5. Hinglish brain-dump to plan
- **Need:** he and his wife think and talk in mixed Hindi and English; commitments get lost. **Magic:** talk for two minutes after dinner, in any mix of languages, and it returns the commitments, dates and groceries. **Meta tooling:** Voice Transcribe with language bias (25 languages; Hindi coverage **unverified**), Spark for extraction. **Risk:** can read as basic summarization unless it acts (schedules, confirms). A good input mode for the household agent.

## The middle: delightful and real

### M1. The dinner diplomat (two private conversations, one proposal)
- **Need:** the evening dinner fight in the interview; Vibhor's wish for a neutral third party that helps both converge.
- **Magic:** it asks each of you privately and briefly ("what would feel easy tonight?"), then proposes one plan that respects both limits, e.g. "she is working after dinner, you are free, so order for you and she cooks hers."
- **Guardrails:** stays on meals and timing. No relationship advice, no emotion analysis, no personality model of either person (all discouraged). Each person's private answers are never shown to the other, only the proposal.
- **Meta tooling:** Voice Transcribe, tool calls with two memory spaces, Spark for negotiation, optional Glimmer local.
- **Prizes:** Agentic. Community Vote if the story lands.
- **Feasibility:** medium (about 50%). Needs his wife's consent and a second device. Demo with a staged pair. Prior art: not checked; Instinct's trusted-person coordination is related ([eesel review](https://www.eesel.ai/blog/instinct-ai-review)).

### M2. Fridge to tonight
- **Need:** the 5 PM what's-for-dinner scramble. **Magic:** a 10-second fridge video labels what is there (the cookbook's perception-grounding recipe puts dots on items), then it settles tonight's meal given who is home and who is tired, and writes the missing items to the list. **Meta tooling:** Spark video or frames, SAM 3.1, tool calls. **Rule risk:** nutrition coach if it comments on health, so it must not; it only plans logistics. **Feasibility:** high for the vision, medium for a dinner decision you trust.

### M3. Court director for your tournament app
- **Need:** Vibhor is already building an app for players and tournament organizers (details unknown to me), so he would keep building. **Magic:** a voice-and-camera agent that runs a live pickleball or tennis round-robin: players text it late arrivals, it re-balances rotations on the fly, announces matches, counts occupied courts from a phone camera. **Meta tooling:** tool calls, Voice Transcribe, SAM 3.1 counting people. **Rules:** scheduling is not sports analysis, but any line-call or stroke analysis would be. **Prior art exists** for scheduling ([PlayMore](https://www.playpickleball.com/playmore-app-pickleball-scheduling-round-robin/), PickleCourt, Round Robin Assistant); most are deterministic algorithms, and whether any use an LLM live is **unverified**. **Feasibility:** medium. Ask Vibhor what his app already does before building more.

### M4. Scam gym for your parents
- **Need:** the wish to be protected from AI; voice-clone and grandparent scams are well described in press, with scale figures that need checking ([FBI figure via a Yahoo News article](https://www.yahoo.com/news/articles/ai-grandkid-voice-clone-scam-171510668.html) is secondary). **Magic:** with consent, a family member practices on a simulated scammer call, learns the tells, and the family sets a safe word ritual. **Meta tooling:** Voice Transcribe, Spark, optional Glimmer. **Rule risk:** an education chatbot and a possible "simple analyzer" reading. **Crowded neighbour:** [Norton Genie](https://us.norton.com/products/genie-scam-detector) checks suspicious messages. **Feasibility:** medium; Impact depends on evidence. Meta has no audio-deepfake detector in the docs I read, so do not promise detection.

## The moonshot end, with the version that could actually ship

| Moonshot | Why it is magical | Honest Oct 31 version |
| --- | --- | --- |
| **Time machine: "Rewind my day/week"** | Walk back through a day, with a narrator and the right photos | The day-as-comic (S4) plus a spoken recap. Grief and memorial uses are off limits. No real time travel, obviously. |
| **Generate time** (Vibhor's wish) | Hours returned to your week | Not generated, reclaimed and made visible: a **Time Saved ledger** inside the household agent that counts minutes of admin the agent absorbed (parsing, reminding, re-planning). Needs honest measurement or it is fake. |
| **A home that notices** | Ambient, no input | A consented kitchen camera is a privacy hazard and conflicts with local-first. Ship: opt-in photo moments only. |
| **Two agents negotiate for you, in public** | Spectacle: watch your agent and hers bargain | Split-screen demo of M1 with a mediator and visible tool calls. Do not make claims about general agent-to-agent protocols. |
| **Agent that acts in the real world** | Orders the groceries itself | Computer use (`muse-wonder-1.0` or Spark) on a test store with a spend cap, behind explicit approval. Instinct's reviews describe brittle browser flows, CAPTCHAs and 2FA ([Carly summary](https://www.usecarly.com/blog/what-is-instinct-ai/)); treat as Tier 2 at best. |
| **Self-driving mini-lab / robot planner** | Frontier science feel | Already in the notes (sim mode). Heaviest build, weakest tie to Vibhor's life. Skip unless he wants "Push the Frontier." |
| **Live Hindi-English bridge for family calls** | Grandparents and kids understand each other | Voice Transcribe plus translation captions. Crowded: large vendors ship live translation (not checked). Weak differentiation. |

## Moonshot added by Vibhor: the upgradable home robot ("grow-a-robot")

**His idea:** a small wheeled, pet-like home robot that is modular and Lego-style, so people build comfort with robots and AI at home over time, the way they came around to Alexa and Google Home. Parts can be added, swapped or serviced (no landfill of plastic and electronics). The device keeps context about the home (layout, people, language, routines) so every upgrade feels continuous with what it already knows.

**What the evidence says (honest, partly unchecked)**
- *Cloud-dependent home robots can die and take the relationship with them.* Embodied shut down in December 2024 after an investor withdrew, and its $800 Moxie companion robot for children stopped working because it relied on cloud servers; commentators argue for local operation, modular and open design, and "ethical sunsetting." Sources: [The Register](https://www.theregister.com/2024/12/16/moxie_cloud_services_lessons/), [ACM paper on Moxie end-of-life](https://dl.acm.org/doi/10.1145/3772318.3790895), [OECD.AI incident](https://oecd.ai/en/incidents/2024-12-09-ab89). This strongly supports Vibhor's "no junk, own your context" principle. It is a real, documented failure, not a guess.
- *Trust and privacy gate home-robot adoption, and familiarity helps.* A qualitative study of 24 adults aged 65+ in Slovenia ([PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10850379/)) and a survey of nearly 5,000 people reported by [UCD](https://www.ucd.ie/newsandopinion/news/2025/november/05/mostwillingtoacceptcaregivingrobotsassolutiontolong-termcarechallenge) tie willingness to familiarity, with trust, safety and privacy central, and most people comfortable sharing health data with clinicians but under half with robotics companies. Neither tests a staged "earn trust gradually" design, so the specific claim that a ladder works is **unproven**.
- *The Alexa analogy is only half supported.* Studies from 2018 to 2022 show people adopted smart speakers while privacy concern persisted, often resigned to it ([UMich summary](https://record.umich.edu/?p=46272)). That suggests people came around through convenience, not because concern faded. I found no 2025 adoption or trend data.
- *Prior art not checked:* Matic, Misty, Vector/Anki, Enabot and robot-vacuum arms. I only searched the Moxie shutdown. Do not claim novelty until those are checked.

**The insight worth keeping.** The product is not the plastic, it is the **home context that survives every body**. A local, portable "home brain" (layout, people, languages, routines, permissions) that today lives behind a phone, next year drives a cheap wheeled base, later an arm, and can be moved to a new body if one maker dies. That also answers the Moxie lesson. The hardware is a roadmap, the brain is the product.

**Ship-by-Oct-31 version with phone and headphones only (no robot hardware)**
| Stage | What it is | Buildable now? |
| --- | --- | --- |
| 0. Phone as the body | Walk the house with the phone camera and talk. Spark vision plus SAM 3.1 build a local room-and-object map; Voice Transcribe learns names, languages and routines; everything stays in a local store. This is the household agent's memory. | Yes, about 60% |
| 1. Adds voice and nudges | The household agent: board photo, groceries, nudge budget, bad-day exit | Yes, same build |
| 2. Adds wheels (simulated) | The same home map loaded into a 2D or physics sim; a virtual base navigates to "the kitchen" and "the pantry" from spoken commands. Clearly labelled simulation. | Maybe, about 30%, and it risks looking like vapor |
| 3. Adds an arm or a camera mast (roadmap) | Shown as a slide: what the agent already knows tells you which upgrade is useful next | Yes as a slide |
| Trust ladder | Each stage unlocks only with explicit consent, and the screen shows exactly what the new part can see and store | Yes, and it is the most original UI idea here |

**Meta models:** Spark vision and video for the home map, SAM 3.1 for objects and rooms, Voice Transcribe for language and routine learning, Glimmer locally as the brain so the context stays home, Muse Image for the "your next upgrade" visual.

**Rules:** robotics fits "Push the Frontier." No hardware is needed if the demo is honest about being a simulation for stage 2. Avoid claims of a working robot. A camera that maps the home is a privacy hazard, so it must be opt-in, local, and deletable.

**Score (my judgement):** Impact 7, Meta 8, Demo 6, Depth 7, weighted about 7.0. Feasibility of the full vision: low (about 25%). Feasibility of stages 0 and 1 with a roadmap slide: medium to high.

**Recommendation.** Do not pitch a robot you cannot show. Pitch **stage 0 as a real, working "home brain,"** with the household agent as its first capability and a 20-second roadmap at the end ("this is how it grows, and your home's memory moves with it"). That keeps the moonshot as the vision and the household agent as the guaranteed entry, and it turns "local-first" into a design principle backed by a real shutdown story instead of a slogan.

## Scorecard (my judgement)

| Idea | Impact | Meta | Demo | Depth | Weighted | Feasibility | Bonus fit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 Paper Games | 5 | 8 | 9 | 6 | 6.9 | high | Viral, Creative, Agentic |
| S2 Board answers back | 6 | 8 | 8 | 6 | 7.0 | medium-high | Creative, Open Weights |
| M1 Dinner diplomat | 6 | 7 | 7 | 7 | 6.7 | medium | Agentic, Community |
| M2 Fridge to tonight | 5 | 8 | 8 | 6 | 6.7 | high | Open Weights (Glimmer sees images) |
| M3 Court director | 6 | 7 | 7 | 7 | 6.7 | medium | Agentic |
| M4 Scam gym | 6 | 7 | 6 | 5 | 6.1 | medium | Open Weights |
| Grow-a-robot (software stage 0 plus roadmap) | 7 | 8 | 6 | 7 | 7.0 | stage 0 medium-high, full vision low | Open Weights, Agentic |
| Household agent (S2 + M1 + M2 combined) | 6 | 8 | 7 | 8 | 7.1 | medium | Agentic, Open Weights, Creative |
| Cooking guide (earlier work) | 6 to 8 | 9 | 9 | 7 | 7.4 to 8.3 | medium, untested | Agentic |

## Top picks

1. **The household chief of staff, built around "the board that answers back."** Pitch: Every Sunday night you photograph the family whiteboard. In seconds it becomes the real week: flights, workouts, meals, groceries, the pickleball Saturday you forgot to mention. The board comes back redrawn in handwriting, the phone stays quiet except for the one nudge that matters, and on a bad day you say so and it simply lets the plan go, without guilt. Everything stays on your own machine unless you approve the exact message that leaves. This is the only candidate that solves a problem Vibhor lives, combines three magic moments (redrawn board, dinner diplomat, bad-day exit) into one story, and has the strongest open-weights claim. Cost: the weakest demo payoff of the group, and a hard capture problem (see pass 2 of `household-agent-candidate.md`).
2. **Paper Games: teach it any game by talking.** Pitch: Draw a grid, say the rules out loud, and it plays you on paper. It keeps score, refuses illegal moves, and says "I can't tell if that mark is an X" when it can't. The following night a four-year-old teaches it a game she invented. Small, finishable, and delightful, with the most shareable demo moment of any idea here. Cost: the lowest Impact, so it only wins if the judges value joy and craft over problem size. Best used as the safe floor if bigger bets slip.
3. **Court director (conditional).** Pitch: A voice-and-camera agent that runs a pickleball or tennis round-robin so the organizer can play too. Only worth it if Vibhor's tournament app is already close to this and he would ship it beyond the hackathon; ask him.

**Suggested combination.** Do not submit two things. A sound shape is the household agent as the product, Paper Games as the evening-ritual feature inside it only if time remains (the dinner-table game that gets the phone out of both hands), and everything else cut.

## Open questions
- What does his tournament app do today, and who uses it? That decides whether M3 is a real product or a tangent.
- Does he have a 24 GB GPU, a kitchen tablet, a printer? That decides S2 and Glimmer.
- Will his wife consent to being in a demo, even as a staged scene? That decides M1.
