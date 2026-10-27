# Independent Hackathon Idea Research — Meta Global AI Developer Hackathon

*Generated independently on 2026-10-27, without reading the user's existing idea document or research repo. Landscape research via web search; product capabilities from `PRODUCTS.md` (itself sourced from secondary sources — see its caveat) and the event knowledgebase (themes: "Build for Your World" / "Push the Frontier"; judging: Impact 30%, Use of Meta AI Tooling 25%, Demo 25% incl. video quality and holding up live, Technical Depth 20%). Build window: ~9 days to Nov 4, 2026, 9:00 PM ET. Team: one developer (Vibhor) + AI agents.*

---

## Part 1 — The landscape: what to avoid, and where the gaps are

### Saturated categories (enter only with a genuinely new lens)

1. **Generic AI tutors / homework helpers.** Khanmigo, Photomath (220M downloads, Google-owned), ChatGPT Study Mode, Google Lens/Socratic, CK-12 Flexi, Synthesis, Quizlet, NotebookLM. Explicitly named on "do not build" lists for hackathons ("generic AI tutor… too crowded and too easy to fake").
2. **Photo-diagnosis repair apps.** Repair Coach AI (1.4M installs), AI Repair, Reparo, Fixi — snap a photo, get step-by-step fix instructions is a commodity. Voice-first repair also exists (TalkFixAI, launched Oct 2026), as does a Ray-Ban-glasses fix-it agent with live bounding boxes (Clutch, a DEV hackathon build).
3. **AI cooking coaches that watch you.** SuChef (camera checks, "90 more seconds"), SousChef Live (real-time Gemini sous-chef), UnBurnt (watches for overheating/missed steps), Miso (passive vision monitoring design). "Camera watches the pan" is no longer novel.
4. **Music-practice apps with feedback.** Simply Piano, Yousician, flowkey, Skoove — mature subscription products with mic-based note/timing feedback. Their known gap is physical technique/form, which none assess well — but that's a gap in a mature market, not an empty one.
5. **Sign-language apps with camera feedback.** Lingvano's Sign Mirror and Ace ASL already do real-time sign recognition and correction.
6. **Scene description for blind users.** Be My AI (single-photo descriptions, known to make placement errors), Microsoft Seeing AI, Meta AI on Ray-Ban glasses. Description is solved-ish; *guided task completion* is not (see idea 6).
7. **Enterprise expert-capture / SOP platforms.** DeepHow (expert video → step-by-step "Smart Instructions" + AI skill verification, customers like Unilever and Stanley Black & Decker) and Xapify own the B2B version of "record an expert, verify the worker."
8. **Video → text protocol extractors.** Distill, StepTube, PlanYogi, ScreenApp turn tutorials into step lists. All passive — none watches you do it (one research system does: Vid2Coach, an academic prototype for blind/low-vision users built on Gemini).
9. **Car-sound diagnosis.** Carithm, MyAutoSound, Check Engine Chat (29 sounds, abstains when unsure), AutoSonic. Cars are covered; appliances are not, and none closes the loop with a guided fix + verification.
10. **Hackathon sludge generally:** PDF chatbots, research summarizers, mental-health chatbots, "AI doctor," meeting assistants, personal-finance agents, DevOps autopilots, resume builders, habit trackers. Judges have seen hundreds of each.

### Signals worth exploiting

- **Meta itself is benchmarking this exact space.** Meta's InteractiveWorld tests glasses assistants across 120 tasks in six categories — Guidance, Planning, Accessibility, Decision, **Prevention** ("warn before a mistake, scored on restraint — over-talking is a failure mode"), and Finding. A submission that speaks Meta's own research language (especially Prevention) is legible to Meta judges in a way a generic tutor never will be.
- **Spark Open takes native audio input** — almost nothing consumer-facing diagnoses problems *by sound*, and no repair product verifies a fix by re-listening.
- **SAM 3.1's text-concept masks + video tracking** make "watch the *thing*, not the scene" cheap ($0.20/1,000 video frames) — object-level verification loops are newly practical.
- **Muse Image edits preserve the rest of the frame** — annotating the user's *own* photo ("your setup, with the next action marked") and generating corrected versions of the user's own frames is a capability no incumbent learning product uses.
- **Voice Transcribe diarizes 20+ speakers in real time** — two-person scenes (demonstrator + learner, teacher + student) can be separated and structured automatically.
- The market's own analysts flag the shift **from course completion to skill verification** as the big structural opening in learning/workforce — proof-of-skill with evidence is under-built for individuals.

---

## Part 2 — The candidates

### 1. Heirloom — learn it from the one person who does it right

**One-liner:** Record anyone doing a hands-on task once — a grandmother's recipe, a father's knot, a coach's drill — and Heirloom turns that single demonstration into a coach who later watches *you* do it and teaches you in their steps and their words.

**Problem & who it's for.** The world's real skills live in people's hands, not in content libraries: family recipes, crafts, trades tricks, cultural techniques. When that person is far away — or gone — the knowledge dies or degrades into a shaky phone video nobody can learn from. Existing options are generic guides (DeepHow is enterprise SOP software; YouTube is one-way). Nobody turns a *personal* demonstration into an interactive, verifying coach. For: adult children of immigrants, craft learners, families, anyone with a "show me how you make that" person.

**How it works.**
- **Capture:** the demonstrator does the task once on a phone camera, narrating naturally. Voice Transcribe diarizes and transcribes the narration; Spark Open watches the full video and extracts a step graph — each step gets the demonstrator's own words, the objects involved, and a completion criterion ("fold until the edges seal").
- **Index:** SAM 3.1 segments the key objects per step (the dough, the corner fold, the wrench) so the system knows what "right" looks like *in this person's version*.
- **Coach mode (days or years later):** the learner props up a phone and attempts the task. The agent watches in clips, matches progress against the demonstration's step graph, and coaches with the demonstrator's phrases — "She pinches the corner twice; you did it once" — replaying the exact seconds of the original demonstration at the moment they're needed.
- **Annotate:** when words aren't enough, Muse Image edits a frame of the *learner's* attempt to mark the next action, preserving their actual setup.
- **Keepsake:** the session produces a side-by-side "you learned her way" recap — demo moment vs. your matching moment.

**Meta models used.** Muse Spark Open (video understanding of both demonstration and attempt; step-graph extraction; attempt-vs-demo comparison — its 1M context holds both), Muse Voice Transcribe (diarized demonstrator narration → transcript + step timing), SAM 3.1 (object masks/tracking in both videos; visual alignment of attempt vs. demo), Muse Image (preservation-first annotation of the learner's frames). Optional: Muse Glimmer locally as a step-completion judge.

**Why judges care.** *Impact (30%):* knowledge inheritance is a universal, emotional, firsthand problem — peak "Build for Your World." *Tooling (25%):* four Meta products, each doing the job only it can do — this is beyond-basic integration by construction. *Demo (25%):* the story tells itself in video (see below) and the live demo is a person actually learning a fold/stitch/knot on stage. *Technical (20%):* cross-video step alignment and state tracking is real engineering, not a prompt wrapper.

**The demo moment.** Split screen: 1998-style kitchen video of a grandmother folding a samosa — "pinch, pinch, like this" — beside a grandchild attempting it today. The coach pauses them: "She pinches the corner *twice*. You did it once — that's why it opened." They pinch again; SAM's mask seals the edge on screen; the coach, in her words: "There. Like this." Twenty seconds, judges feel it.

**Build risk & Nov 4 feasibility.** Medium-low. No true realtime needed — clip-based loops (5–10 s) are fine for coaching. Pre-record one polished demonstration (a family recipe is ideal and authentic to Vibhor's own recipe-app history); the step-graph pipeline is batch processing. The risky part is attempt-vs-demo comparison quality; mitigate by scoping to tasks with visible state changes and letting Spark Open judge semantically with SAM masks as grounding. Very buildable in 9 days.

**Nearest competitors & difference.** DeepHow (enterprise, employees' SOPs, no personal/emotional frame, no attempt-vs-*that specific person* comparison coaching); YouTube (one-way); Clutch (generates generic guides from scratch — the opposite: Heirloom's authority is a real person's real demonstration). **Type: common category (how-to guidance) through a genuinely new lens — the source is a person, not a library, and the coach verifies against their demonstration.**

---

### 2. Follow-Along — the tutorial that watches you back

**One-liner:** Paste any how-to video and Follow-Along becomes a coach who watches you do the task, knows which step you're on, verifies each step is actually done, and replays the exact 5 seconds of the tutorial when you're stuck.

**Problem & who it's for.** Everyone learns hands-on skills from video, and video is terrible at it: greasy hands can't scrub timelines, the 14-minute video has 3 useful minutes, and nothing notices when you did step 4 wrong. Distill/StepTube fix the *reading* problem (text protocols) but still leave you alone with the doing. For: DIYers, cooks, cyclists, crafters, new hires learning from internal recordings — anyone mid-task with dirty hands.

**How it works.**
- **Ingest:** user pastes a tutorial (or picks from bundled openly-licensed ones). Spark Open consumes the video natively and builds a step graph: steps, tools, timestamps, and a *visual completion test* per step.
- **Do mode:** phone propped up, hands-free. Voice Transcribe handles the conversation (its endpointing knows when you've finished speaking; keyword biasing loads the task's vocabulary). The agent tracks your step from periodic video clips.
- **Verify, don't assume:** step completion is checked — SAM 3.1 tracks the step's target object/state ("tire bead seated", "valve closed") plus Spark Open's semantic read — before advancing. No check-off theater.
- **Stuck loop:** say "I'm stuck" (or the agent sees no progress) and it plays the tutorial's exact clip for your current step, then watches you retry.
- **Finish:** a completion recap — the tutorial's steps with your verified evidence frame for each.

**Meta models used.** Muse Spark Open (tutorial understanding + live attempt tracking in one 1M-context session), SAM 3.1 (per-step object/state verification + overlays), Muse Voice Transcribe (hands-free realtime dialogue, diarization if a helper is present), Muse Image (optional: annotate your frame with "this bolt, this direction" when a step needs a pointer).

**Why judges care.** *Impact:* attacks the single most common way humanity learns physical skills, with a retention argument (active + verified ≫ passive watching). *Tooling:* the whole multimodal stack in one loop. *Demo:* inherently visual — judges watch someone get unstuck in real time. *Technical:* step-state machine grounded by two independent perception paths (LLM semantics + SAM masks) is a defensible architecture.

**The demo moment.** A cyclist mid-tire-change, hands covered in grime: "I'm stuck." The agent instantly replays the creator seating the bead at 04:12–04:17, then watches: "That's it — thumb pressure, walk it around. Bead's seated. Step done." The step checks itself off with the evidence frame.

**Build risk & Nov 4 feasibility.** Medium. Ingestion is batch and cacheable (pre-process 2–3 demo tutorials); live mode is clip-loop, not streaming. Watch-outs: arbitrary YouTube ingestion has ToS/Download friction — ship with user-uploaded or openly licensed videos (upload path is also the honest product framing) and treat URL-fetch as stretch. SAM concept prompts must be generated per step by Spark Open — prompt quality is the main tuning task.

**Nearest competitors & difference.** Distill / StepTube / PlanYogi (text extraction only — no watching, no verification); Vid2Coach (academic research prototype for blind/low-vision users on Gemini — validates the concept, proves the consumer sighted market is unbuilt); Clutch (generates its own guides; Follow-Along activates the video the user already trusts). **Type: common category (tutorial tools) through a new lens — the video stays the teacher; the AI becomes the proctor.**

---

### 3. Second Listen — it hears what's broken, and proves you fixed it

**One-liner:** Hold your phone near the machine that sounds wrong. Second Listen diagnoses it by ear, guides the fix hands-free, then listens again to verify — fixed means fixed.

**Problem & who it's for.** Strange noises are how machines announce failure, and homeowners can't interpret them: is that washer grind a $40 pump or a $400 bearing? Is it safe to run? Photo-diagnosis apps can't hear anything; car-sound apps stop at cars and at diagnosis. For: homeowners, renters, DIYers facing a misbehaving washer, dryer, dishwasher, fridge, or HVAC unit.

**How it works.**
- **Listen:** 10-second recording (or live clip) of the appliance. Spark Open — one of the only models in its class with **native audio input** — characterizes the sound (periodic grind vs. rattle vs. hum), combines it with what the camera sees, and produces a ranked diagnosis with an explicit confidence and an honesty rule: unsure means it says so and asks for a closer recording or one more symptom.
- **Interrogate:** like a good mechanic, it asks 2–3 discriminating questions by voice ("does it change on the spin cycle?") via Voice Transcribe, narrowing the diagnosis before any tools come out.
- **Guide:** step-by-step fix coaching with the camera watching — SAM 3.1 tracks the part (pump, belt, filter) and Muse Image annotates the user's own unit photo ("this hose clamp, quarter-turn").
- **Verify (the signature move):** after the fix, it re-listens and runs the functional check with you. Diagnosis isn't closed until the sound is gone or the agent explains what remains.
- **Baseline:** optionally record your machine healthy; future checks compare against *your* machine's own normal.

**Meta models used.** Muse Spark Open (native audio diagnosis + video + reasoning in one context — the architectural centerpiece), Muse Voice Transcribe (hands-free mechanic's interview), SAM 3.1 (part localization during the fix), Muse Image (annotated diagrams on the user's actual appliance).

**Why judges care.** *Tooling (25%):* this is the idea that most needs *this* model — native audio understanding in the open-weight flagship is a capability judges are being asked to reward, and almost no team will build on it. *Impact:* misdiagnosis costs real money and the "call a pro blind" tax falls hardest on people with least to spare. *Demo:* sound is theater (below). *Technical:* multimodal differential diagnosis + a verification loop is a real system.

**The demo moment.** A washing machine grinding horribly. The agent listens five seconds: "That's a worn drain pump — not the bearing. Bearing would keep grinding through the spin; yours stops." Twenty minutes of guided fix later, the machine runs quiet, the agent listens again: "That's the sound of fixed." The before/after audio pair is unforgettable in a video.

**Build risk & Nov 4 feasibility.** Medium. Honest scoping: launch with 4–6 well-chosen appliance fault sounds (drain pump, unbalanced load, worn belt, fridge compressor rattle, dishwasher spray-arm blockage) with recorded exemplars, and let Spark Open reason openly rather than pretending to a trained classifier. Risk: audio quality variance; mitigate with guided recording placement and the abstain-and-ask behavior. The verification loop means even a partial diagnosis demos well.

**Nearest competitors & difference.** Carithm / MyAutoSound / Check Engine Chat (cars only, diagnosis only, no fix guidance, no verification); Repair Coach AI / Reparo (photo + text, deaf to the actual symptom); Fixi (diagnosis → books a pro). **Type: saturated category (repair help) through a genuinely new lens — ears first, and the loop isn't closed until the machine sounds right.**

---

### 4. Quiet Coach — the assistant that only speaks before you mess up

**One-liner:** A watching coach that stays silent while you work — and interrupts only in the seconds before a mistake becomes expensive, painful, or irreversible.

**Problem & who it's for.** Step-by-step guidance has a fatal flaw: it's noise. Real people mute chatty assistants, and chattiness is worst exactly when hands and attention are busy. But the highest-value moment in any hands-on task is the second *before* the error — the wrong wire, the upside-down panel, the hand reaching for the hot handle. Meta's own InteractiveWorld benchmark names this category (Prevention) and scores it on restraint. For: cooks, DIYers, assemblers, anyone who wants a spotter, not a narrator.

**How it works.**
- User states the task ("I'm replacing this faucet", "assembling this shelf"); Spark Open builds the task's known error points from the video context/manual (PDF fits the 1M window).
- During work, a clip-loop watcher (Spark Open + SAM 3.1 tracking hands, tools, and hazard objects) evaluates one question only: *is an error or hazard imminent?*
- If not: silence — visibly. The UI shows a calm "watching" state and a running restraint stat.
- If yes: one short spoken interruption, specific and early — "Wait — that panel's upside down; the cam holes should face up." Voice Transcribe's endpointing keeps it from talking over the user.
- Session ends with a receipt: interruptions made, estimated saves, and — just as important — the long stretches where it correctly said nothing.

**Meta models used.** Muse Spark Open (task model + imminent-error judgment over video), SAM 3.1 (continuous tracking of the few objects that matter — hands, blade, hot pan, wire), Muse Voice Transcribe (voice channel discipline + user barge-in). Optional Glimmer on-device as a low-latency first-pass filter so the big model only judges candidate moments.

**Why judges care.** *Tooling:* uses Meta's stack to implement *Meta's own published research framing* — the Prevention category with restraint as a scored virtue; no other team will read the benchmark tea leaves this directly. *Demo:* the silence is the demo — tension and release, live. *Impact:* injuries and ruined work concentrate in preventable seconds. *Technical:* a two-stage watch/judge pipeline with false-positive discipline is a real systems problem.

**The demo moment.** Live on stage: a cook reaches bare-handed for a cast-iron handle — "Wait. Mitt first." — then ten correct steps pass in total silence, the restraint counter ticking up, until a knife starts sliding toward the counter edge: "Knife." Two words. The room gets it instantly.

**Build risk & Nov 4 feasibility.** Medium-high — the riskiest of the top four. Latency is the enemy: mitigate with short clip loops, a small set of rehearsed task scenarios with strong visual precursors, and Glimmer/SAM pre-filtering so Spark Open judges 1 frame in 30. Demo must be rehearsed with real near-mistakes, not simulated UI. Ship 2–3 task domains done well (kitchen safety, flat-pack assembly, basic electrical-off tasks) rather than "any task."

**Nearest competitors & difference.** UnBurnt/SuChef (chatty cooking-specific guidance — the opposite philosophy, and cooking-only); Clutch (narrates steps). Nobody sells restraint as the feature. **Type: uncommon — guidance products compete on how much they say; this one competes on how little.**

---

### 5. StateCheck — never build it backwards again

**One-liner:** Point your phone at a flat-pack/kit build and StateCheck maintains a verified live model of your build — parts used, parts remaining, orientations right — catching the error at step 3 that would have ruined step 12.

**Problem & who it's for.** Assembly instructions describe the *intended* build; nothing tracks *your* build. The classic failure — a panel reversed, a screw in the wrong hole — is invisible until it isn't, and disassembly at step 12 is where furniture (and weekends) go to die. For: flat-pack furniture buyers, model/LEGO-style kit builders, PC builders, anyone assembling anything with 40 similar screws.

**How it works.**
- **Load the target state:** user photographs the manual (or uploads the PDF); Spark Open parses steps, parts list, and per-step end-states into a build graph.
- **Inventory:** camera sweep of the parts pile — SAM 3.1 segments and counts parts by concept ("cam lock screw", "side panel"); the agent confirms the kit is complete *before* starting and flags the missing dowel while returns are still possible.
- **Track:** as you build, periodic photos/clips update the state model: which parts are consumed, what the current assembly should look like vs. what yours looks like.
- **Guard the irreversible steps:** before screws tighten and glue sets, it checks orientation and fit against the step's end-state and speaks up only on mismatch (borrowing Quiet Coach's restraint).
- **Finish check:** final comparison against the manual's completed image; a parts-remaining report ("two screws left over — that's expected; three would mean step 7 was skipped").

**Meta models used.** Muse Spark Open (manual/PDF understanding, build-graph reasoning, state comparison), SAM 3.1 (parts counting, per-part segmentation, assembly tracking), Muse Voice Transcribe (hands-free "does this look right?" checks), Muse Image (generates "your build should now look like this" reference images matched to your model's finish/colorway).

**Why judges care.** *Demo:* the step-3 catch is instantly legible and deeply relatable — everyone in the room has lost that Sunday. *Technical:* persistent physical state estimation from images is a meaty, honest problem. *Impact:* billions of flat-pack hours; returns and landfill from failed builds. *Tooling:* SAM counting + PDF-to-build-graph is a fresh combination.

**The demo moment.** The builder lifts the back panel into place. StateCheck: "Stop — your left side panel is flipped. The cam holes face down; on the diagram they face up. Flip it now, or the top can't attach at step 12." Disaster averted on camera, 40 minutes of future rage deleted.

**Build risk & Nov 4 feasibility.** Medium. Scope to one demo build done deeply (a small shelf) plus a generic manual-ingestion path; parts counting on near-identical screws is genuinely hard for segmentation — mitigate by counting *distinct* parts and treating screw-count as estimate-with-confirmation. State model can be photo-checkpoint-based (after each step) rather than continuous video — much more reliable, still demos great.

**Nearest competitors & difference.** IKEA's app ecosystem and AR room planners (visualization, not build-state verification); manual apps (static PDFs); BILT (3D animated instructions for brands — excellent instructions, but it never looks at *your* build). **Type: common category (assembly instructions) through a new lens — verification of physical state, not presentation of steps.**

---

### 6. DoWith — a coach that helps blind users *finish* the task

**One-liner:** For blind and low-vision users, DoWith goes beyond describing the scene: it guides a real task to completion — finding each component, directing your hands, and verifying every step — entirely by voice.

**Problem & who it's for.** Be My AI and Seeing AI answer "what is this?" with a single photo (and documented placement errors). But independence is not descriptions; it's *doing* — assembling the shelf, wiring the thermostat, organizing the medication, cooking the recipe — in an unfamiliar space, without a sighted volunteer. Meta's InteractiveWorld explicitly includes Accessibility tasks where "the human gets no images; the assistant has to do the seeing." For: blind and low-vision people doing hands-on tasks at home.

**How it works.**
- **Voice-first, screen-reader-native:** the whole product is a conversation (Voice Transcribe for input and turn-taking; no visual UI dependency, no word-level timing needed).
- **Find:** SAM 3.1 locates task components in the camera view; the agent gives clock-face/spatial directions and confirms grasp ("that's the blue cable — wrong one is ribbed; yours is smooth: correct").
- **Guide & verify:** step-by-step task guidance where each step ends in a verification — a photo the agent reads to confirm state (connector seated, lid aligned) before proceeding. No step is assumed done.
- **Remember:** using Spark Open's long context, it builds a spatial memory of the workspace during the session ("the screws are in a bowl at your 2 o'clock") so later steps can reference where things were put down — the InteractiveWorld "Finding" skill, in service of doing.
- **Escalation honesty:** when perception is uncertain, it says so and suggests a tactile check rather than guessing — a stated design rule, learned from Be My AI's documented error modes.

**Meta models used.** Muse Voice Transcribe (the entire interaction surface — realtime ASR with endpointing), SAM 3.1 (object finding + grasp verification), Muse Spark Open (task planning, scene reasoning, session spatial memory), Muse Image not required — deliberately: every Meta perception product is load-bearing, none decorative.

**Why judges care.** *Impact (30%):* this is the highest-ceiling impact idea in the set — the difference between information access and actual independence. *Tooling:* Meta's models doing exactly what Meta's own benchmark asks for. *Demo:* a completed task (assembled kit, made drink, sorted cables) accomplished eyes-free is a powerful, honest demo. *Technical:* spatial memory + verification discipline under perception uncertainty.

**The demo moment.** Eyes-free, a user sorts and connects a small electronics kit: "Move your right hand forward… stop. That's the housing. Now the cable at your 1 o'clock — yes, that click means it's seated." Task: done, verified, unassisted.

**Build risk & Nov 4 feasibility.** High — stated honestly. The technology is buildable (all pieces above exist), but designing *for* blind users without blind testers in a 9-day sprint risks a well-meant demo rather than a validated product, and a blindfolded-sighted-person demo would be the wrong look. The responsible version: narrow scope (one guided kit task + find-my-object mode), VoiceOver-tested flows, explicit "designed with the community next" framing, and — if any blind tester can be recruited even for one session — that session becomes the demo. Rank reflects risk, not value.

**Nearest competitors & difference.** Be My AI (describes photos; no task state, no verification, no spatial memory); Seeing AI (identification utilities); Ray-Ban Meta + Be My Eyes volunteers (human help — the thing users want independence *from*); Vid2Coach (research prototype — BLV how-to-video assistance; DoWith differs by sourcing tasks from manuals/goals, not only videos, and by its find-and-verify loop). **Type: common category (accessibility AI) through a new lens — completion, not description.**

---

### 7. GhostRep — your last rep, corrected, laid over your next one

**One-liner:** Film one attempt at a physical skill — a tennis serve, a golf swing, a squat — and GhostRep picks the *one* thing to fix, generates a corrected "ghost" of your own body doing it right, then watches your next attempt and grades only that.

**Problem & who it's for.** Skill apps drown learners in metrics (SwingVision's shot charts, OnForm's angles) or judge the wrong channel (music apps hear notes but can't see the collapsed wrist). Human coaches do the opposite: one cue at a time, shown on *your* body. For: self-coached athletes and movers — tennis players, golfers, lifters, dancers — practicing alone. (Vibhor plays competitive tennis and has built tennis software — an authentic Build-for-Your-World story.)

**How it works.**
- **Attempt:** user records a short clip. Spark Open — native video input — reads the whole movement holistically (not pose-keypoint arithmetic) and selects the single highest-leverage fault, explained in plain language.
- **Ghost:** SAM 3.1 isolates the athlete and the implement (racket, club, bar); Muse Image generates the corrected keyframe — *your* frame, *your* clothes, *your* court — with the one change made (toss arm higher, hips turned), using its edit-preserving behavior so it reads as you, fixed.
- **Next rep:** film again; the agent grades only the chosen cue ("toss is 20 cm further left — better; cup the wrist less") and either graduates the cue or repeats it with a drill.
- **Session log:** a rep-by-rep trail of single cues — the anti-dashboard: one thing at a time, each verified.

**Meta models used.** Muse Spark Open (full-motion video critique + cue selection + rep grading), SAM 3.1 (athlete/implement segmentation and ball tracking across reps), Muse Image (generative ghost frames from the user's own footage — the signature capability), Muse Voice Transcribe (hands-free "again" / "why?" between reps, on-court).

**Why judges care.** *Demo:* the ghost overlay is a visual nobody forgets — "me, but correct" is instantly understood. *Tooling:* Muse Image's edit mode used as a coaching instrument is a genuinely unexpected application. *Impact:* private coaching costs $50–150/hr; a one-cue-at-a-time loop is how learning actually happens. *Technical:* video-native critique without a pose pipeline is a bet on exactly what these models newly make possible.

**The demo moment.** A serve toss drifts left; the screen splits — real frame vs. ghost frame, same player, toss arm corrected. Next serve: ball tracked, toss lands in the ghost's zone. "That's the toss. Keep it. New cue —" and the video ends with the audience wanting the next rep.

**Build risk & Nov 4 feasibility.** Medium-high. Form judgment quality from a general video model is the open question — mitigate by choosing skills with gross, visible faults (toss placement, obvious squat depth) rather than subtle ones, and leaning on SAM ball/implement tracking for the objective part of grading. Ghost generation on video frames can look uncanny; mitigate with stylization (the ghost is *meant* to look like an overlay, not a deepfake). Feasible as clip-loop; not a realtime product.

**Nearest competitors & difference.** SwingVision (tennis stats/line calls — measurement, not coaching), OnForm & GolfFix (pose/AI swing analysis with generic avatars), Sportsbox 3D (mocap-grade, hardware). None generates the correction on your own body or runs a verified one-cue loop. **Type: common category (sports coaching) through a new lens — generative self-overlay + single-cue verification.**

---

### 8. SkillReceipt — practice the procedure, get graded with evidence

**One-liner:** Perform a hands-on procedure on camera — a nursing skills check, a knife-skills test, a bench task — and SkillReceipt grades you against the rubric, with a timestamped video clip as evidence for every point won or lost.

**Problem & who it's for.** Hands-on learners practice blind: nursing and EMT students before OSCE-style checks, culinary students, trade apprentices, driving-test candidates. Instructors can't watch every practice rep, and self-assessment is unreliable. Enterprise verification exists (DeepHow for employers) but nothing serves the individual learner preparing to be judged. Ed-tech analysts call the completion→verification shift the sector's biggest opening.

**How it works.**
- **Rubric in:** user picks or pastes a rubric/checklist (instructor's PDF, exam criteria, or one the agent drafts from the procedure name for approval).
- **Perform:** one continuous attempt on camera, narrating as rubrics require ("I'm checking the patient's wristband") — Voice Transcribe diarizes and timestamps the narration.
- **Grade:** Spark Open reviews the full attempt against the rubric; SAM 3.1 supplies object-level evidence (was the tourniquet actually placed? was the guard on?). Every criterion gets pass/miss + the evidence clip + a one-line reason.
- **Audit:** Muse Glimmer, running locally, re-grades independently; where the two judges disagree, the criterion is flagged "borderline — human review" instead of silently averaged. Honest grading is the brand.
- **Drill down:** missed criteria become a practice plan; re-attempts track the delta, and the final receipt is shareable with an instructor.

**Meta models used.** Muse Spark Open (rubric reasoning over the full attempt video), SAM 3.1 (object/step evidence), Muse Voice Transcribe (narration capture + diarization), Muse Glimmer (independent local second judge — a real architectural role for the small open model, and a nice open-weights story).

**Why judges care.** *Impact:* credential anxiety is real and the users are strivers — students and apprentices. *Technical:* dual-judge grading with evidence-linked criteria is the most "systems" idea here. *Demo:* a grade appearing criterion-by-criterion, each with its video proof, is satisfying and legible. *Tooling:* four products, including a principled use of Glimmer most teams will ignore.

**The demo moment.** A student performs a timed skills check. The receipt builds live: "Hand hygiene before contact — ✓ (00:12 clip). Tourniquet released before draw — ✗ (01:47: still on). Borderline call flagged for instructor." Then the re-attempt fixes exactly that line.

**Build risk & Nov 4 feasibility.** Medium. Rubric quality drives everything — ship 2–3 built-in rubrics (e.g., a cooking knife-skills check, a first-aid sequence, a soldering bench task) plus paste-your-own. Grading consistency is the risk; the dual-judge + borderline mechanism turns that risk into a feature. All batch processing, no realtime — very buildable.

**Nearest competitors & difference.** DeepHow/Xapify (employer-side verification of employees; SkillReceipt is learner-side, for passing *someone else's* test); generic AI graders (text-based). **Type: uncommon in consumer form — verification exists in enterprise; nobody hands the receipt to the learner.**

---

## Part 3 — Ranking

| Rank | Idea | One-line reason |
|---|---|---|
| **1** | **Heirloom** | The only idea judges will *feel* — personal knowledge inheritance, four Meta products each load-bearing, batch pipeline = safest build, and an authentic firsthand story. |
| **2** | **Follow-Along** | The biggest everyday pain (learning from video) with a verification loop nobody ships; strong demo, medium build risk. |
| **3** | **Second Listen** | The freshest lens in a saturated category and the strongest single-model story (Spark Open's native audio) — memorable before/after audio demo. |
| 4 | Quiet Coach | Directly implements Meta's own Prevention benchmark framing; ranked below the top 3 only on staging/latency risk. |
| 5 | StateCheck | The step-3 catch is the most relatable demo in the set; narrower emotional range and parts-counting risk keep it mid-table. |
| 6 | SkillReceipt | Solid, defensible, very buildable — but reads "worthy" more than "wow," and rubric dependence caps the sparkle. |
| 7 | DoWith | Highest impact ceiling of all eight; ranked here purely on the ethics/testing risk of building for blind users in 9 days without blind testers. With one blind collaborator, it jumps to #2. |
| 8 | GhostRep | The ghost overlay is a great visual, but incumbents are strong and video-model form judgment is the least proven capability in the set. |

**Top 3 flagged: Heirloom, Follow-Along, Second Listen.**

A note for the comparison stage: the top three are complementary, not mutually exclusive — Heirloom's demonstration-indexing, Follow-Along's tutorial-indexing, and a shared "watch → verify → coach" runtime are the same engine with different sources. If the user's existing research converges on any of them, the build plan barely changes.
