# Paper Games: teach it any game by talking

2026-10-26. Scores are my judgement. Prior art was searched once, shallowly (below). Everything about Meta-model accuracy on paper is **untested**.

## Concept
Draw a grid or board on paper, prop up the phone, and explain a game out loud ("three in a row wins; you can't take the middle on the first move"). The agent plays you on the paper: it reads the board with the camera, says its move aloud, tells you where to draw it, keeps score, refuses illegal moves (its own and yours), and says "I can't tell if that mark is an X, is it?" when unsure. Teach it a new game tomorrow by talking again.

## How it works
1. **Teach:** Muse Voice Transcribe (realtime) turns the spoken rules into text. Spark writes the rules as a small structured spec (board shape, legal moves, win and end conditions) **plus test cases**, then reads a plain-language summary back for you to confirm. Code runs the spec in a rules engine, and the model's own proposed moves are checked against it.
2. **See:** the phone camera frame goes through grid detection and per-cell reading. SAM 3.1 can find the sheet and marks; Spark vision classifies cells. Low-confidence cells trigger a question, never a guess.
3. **Play:** Spark proposes a move; the **rules engine verifies** it is legal; the browser's speech synthesis speaks it (Meta has no text-to-speech).
4. **Verify:** after your move the agent compares the new frame to the previous state and checks that exactly one legal change happened.

Why this design: language models make illegal moves in games, so legality must be checked in code. A February 2026 study of LLMs on general-game-playing rule descriptions catalogues such mistakes ([arXiv 2602.19160](https://arxiv.org/html/2602.19160v1)), and LLM game platforms track illegal moves as a standard measure ([LLM GameLab](https://pure.ups.edu.ec/en/publications/llm-gamelab-an-interactive-platform-fortesting-large-language-mod/)). Reading boards from images is also a known weak point: one benchmark found models do much worse on game state as an image than as text ([MET-Bench](https://arxiv.org/pdf/2502.10886)), and another notes board-to-matrix perception needs high local precision ([LVLM-Playground](https://arxiv.org/pdf/2503.02358)). So: detect the grid with classical vision first, classify cell by cell, confirm doubtful cells. **Whether Spark 1.3 reads hand-drawn marks reliably is the key unknown.**

## Prior art (shallow, one pass)
- Camera-plus-robot-arm tic-tac-toe is a long-standing hobby and student project, with classical vision and minimax ([Hackster](https://www.hackster.io/Elephant-Robotics-Official/tic-aruco-toe-teaching-a-robot-arm-to-play-and-win-49fef8), [Niryo](https://niryo.com/docs/niryo_one/niryo-one-demonstrators/vision-tic-tac-toe/)); one HKU project has an LLM choose moves ([HKU AI Hub](https://aihub.hkuspace.hku.hk/?p=5141)). The builders note colour detection is unreliable under shadows.
- I found **no** project that takes spoken rules for an unseen game and plays on real paper. That is a search-result absence, not proof.
- **Not checked:** commercial AI game companions, Google or Meta live-camera game demos, Meta AI glasses games, and whether a judge has seen similar at earlier hackathons.

## Rubric (my scores)
| Criterion | Score | Reason | What would raise it |
| --- | --- | --- | --- |
| Stage 1 | Pass | Fits "Build for Your World"; real use of Voice, Spark vision, tools, SAM | n/a |
| Impact (30%) | 5 | Joy and screen-free play are real but the problem is small, and I have no sourced number for it yet | A framing with evidence (family time, kids' screen time) and real use by children |
| Meta tooling (25%) | 8 | Voice realtime, vision, SAM 3.1, tool calls, structured output, hosted Glimmer as the engine | Show Glimmer as the move engine and Spark only for rule compilation |
| Demo (25%) | 9 | Visible, funny, instantly understood; a kid teaching it a made-up game is the peak | Real footage of a family; clean camera setup |
| Depth (20%) | 7 | Rules compiled to a checked spec, state rebuilt from frames, legality verified, abstain-and-ask. Drops to 6 if rules are hard-coded | Tests showing rule-compile success rate on N games |
| **Weighted** | **7.2** | Earlier 6.9 assumed thinner depth | |

Assumption-based scores: Demo (depends on cell-reading accuracy), Depth (depends on Spark turning spoken rules into a correct spec), and Impact (no evidence yet).

## Rule risk
Safe on the discouraged list if it plays and verifies: it is not an image analyzer, a tutor or an education chatbot. Do not add a "learn chess" lesson mode (education chatbot) or real sports analysis (sports analyzer). The caveat is "simple": the judges will see tic-tac-toe, so the depth must show in the teach-by-talking, the verification, and the failure handling.

## Demo moment (3 minutes)
A four-year-old (or Vibhor's wife) invents a game on the spot, "you jump over my dots and keep them," and explains it in two sentences. The agent reads it back ("so a jump removes the dot, right?"), the kid says "no, you get two points," it corrects the rule, and then it plays, refuses its own illegal move, and says "I can't tell if that's a dot or a smudge." Final beat: one rules spec shared as a card.

## Tiers to Oct 31
- **Tier 0 (by Oct 29):** tic-tac-toe and dots-and-boxes on paper via the phone browser, grid detection plus per-cell reading, hard-coded rules engine, spoken moves, public repo, hosted demo.
- **Tier 1 (by Oct 31):** teach-by-voice: spoken rules to checked spec with generated tests, read-back confirmation, abstain-and-ask on unsure marks, Glimmer hosted as the move engine, a visible log of what each model did.
- **Tier 2 (only if solid):** custom kid-drawn boards, two-player referee mode, shareable game card.
- Feature freeze Oct 31.

## Spike today (before product code on Oct 27)
Photograph 20 hand-drawn grids (tic-tac-toe, dots-and-boxes, a made-up game) in normal kitchen light. Per-cell accuracy on Spark 1.3 and on hosted Glimmer. **Pass: at least 95% of cells correct on clean grids, or doubtful cells flagged.** Then read three made-up rule descriptions aloud and check whether Spark produces a correct, runnable spec for at least 2 of 3.

## Passion project beyond the hackathon
- Family evenings and a reason to put screens down, with a kid or a partner.
- **A bridge to his tournament app (hypothesis):** the same rule-compiler could turn a spoken tournament format ("round robin, doubles partners rotate, first to 11") into a checked schedule spec. I do not know what his app does yet, so ask.
- Each new game taught is saved, so the library grows with use, which gives a reason to return.

## Honest weaknesses
Lowest Impact of the top candidates; likely to read as a toy unless the verification and teach-by-talking are shown clearly; latency of 2 to 5 seconds per move is unmeasured; paper, lighting and phone-propping add setup friction, the same "ramp-up" problem Vibhor dislikes; no Hindi test yet.
