# Capability-to-idea map: building the idea around what Meta's products do best

2026-10-27. Method: list each Meta capability with its real strengths and limits (from `/mnt/project-files/meta-hackathon-docs/`, fetched from dev.meta.ai on Oct 26), then see which ideas lean hardest on the most distinctive ones. **All scores are my judgement, not data.** Anything about live latency or vision accuracy is **untested**. Context: Indie track, solo, guaranteed entry first, feature freeze Oct 31, submit by Nov 4 9 PM ET. Vibhor's lens: intuitive, AI with agency, away from screens, live feed (no recorded-only products).

## 1. Capabilities, strengths, limits

| Capability | Distinctive strength | Limit that shapes design |
| --- | --- | --- |
| **Spark 1.3 multimodal input** (text, image, video, audio, PDF in one 1M-token context) | One model reads a manual PDF, a photo, a video with its soundtrack and a spoken question together. PDFs: text of 100 pages, 50 as images. | Text out only. No streaming video session, so "live" means sampled frames. 1.3 audio is degraded; use 1.2 for audio. |
| **SAM 3.1** (text prompt to boxes and pixel masks, images and video) | Where Spark says *what*, SAM says *exactly where*, with countable, overlayable masks. Few entries will use it well. Cookbook has a "perception grounding" recipe. | One noun phrase per object type per call. Output is a custom base85 stream that needs the parser library. Segments, does not reason. |
| **Voice Transcribe** (realtime WebSocket, diarization, 25 language bias, keywords) | Real streaming speech in, with **who said what**. | Transcript only: no TTS, no word timestamps. Spoken replies need browser speech synthesis. |
| **Muse Image** (generate, multi-turn edit, compose up to 10 images, web-grounded, $0.01 each) | Edit-in-place and consistent series; cheap. Strong for "redraw this" outputs. | No mask, no other tools in the same call, handwriting legibility untested. Still images only: no video output. |
| **Tool calling, structured output, tool search, reasoning effort, background runs** | Reliable agent plumbing: state machines, JSON schemas, verifiable steps (the Oct 28 "verifiable agents" session). | `tool_choice` is `auto` only; no recursive schemas. |
| **Computer use** (Wonder or Spark 1.3, you supply the browser) | An agent that does screen chores *for* a person. | Preview model, 3 to 5 times Spark cost, slower, risky to demo on real sites. |
| **Web search grounding** | Fresh facts with citations, $2.50 per 1K. | Not a differentiator alone (basic RAG is discouraged). |
| **Open weights: Glimmer 30B** (Apache 2.0, vision in, 100+ languages), Spark Open 816B | Cheap first-pass model, portable, the $10K open-weights bonus; cookbook has "Glimmer local, escalates to Spark after approval". | No GPU here: Glimmer runs hosted for the hackathon. Say "designed for local", not "tested on". |
| **Muse Code / SDK, post-training** | Fast build; SFT and GRPO exist. | Fine-tuning is too heavy for a solo week. Not recommended. |
| **Platform limits** | 3,000 RPM and 4M TPM leave plenty of room for a frame loop; $150 credit is ample. | No voice or video output; 2 to 5 s per live reply is an estimate. |

Most distinctive combination versus Gemini and OpenAI assistants (which already ship live camera chat): **document-grounded state + pixel-precise evidence (SAM) + diarized live speech + image edit output + open-weights tier**. Live camera chat alone is not a differentiator.

## 2. Ideas against capabilities

● = central, ○ = supporting, blank = unused.

| Capability | Live guide (manual first, cooking as second pack) | Family Sync (new) | Household board | Paper Games | Computer-use errands (new) | Scam shield | Play to Comic |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Spark vision on live frames | ● | | ○ | ● | | ○ | ○ |
| Spark PDF or video as knowledge | ● | | ○ | | | | ● |
| SAM 3.1 | ● | | | ○ | | | ○ |
| Voice realtime | ● | ● (diarized) | ○ | ● | ○ | | |
| Tool calls and state machine | ● | ● | ● | ● | ● | ○ | |
| Muse Image output | | ○ | ● (redraw board) | | | | ● |
| Computer use | | | ○ stretch | | ● | | |
| Glimmer tier | ● (cheap frame triage, escalate) | ● (extraction) | ● | | | ○ | |
| **Capabilities used centrally** | 6 | 3 | 3 | 3 | 2 | 1 | 2 |
| Live feed is the product | Yes | Yes (spoken sync) | Partly | Yes | No | No | No |
| Screen-away | Strong | Strong | Partial | Strong | Weak (it uses screens for you) | Weak | Weak |

**New ideas the mapping suggests**
- **Family Sync (kitchen-table standup).** Five spoken minutes once a week, diarized by Voice Transcribe. The agent extracts commitments per person ("I'll get the kids Tuesday"), spots conflicts with flights and calendars, asks at most three questions, and redraws the whiteboard with Muse Image. It answers Vibhor's own pain (info scattered, dinner scrambles, a neutral third party) with capture by *talking*, not photographing. Glimmer does the text extraction. Risks: diarization on a real two-person Hindi-English kitchen is **untested**; a voice-only product is hard to film, so the redrawn board is the visual payoff; family speech is sensitive, so staged or consenting demo only.
- **Errand agent via computer use.** The screen chores done *for* you, with approval gates. Fits Best Agentic, but it is the weakest on "live feed" and risky to demo on real sites. Keep as a Tier 2 stretch on the household product, not a core idea.

## 3. Rubric scoring (judgement)

Stage 1 (theme fit, real Meta use) passes for all. Stage 2 weights: Impact 30, Meta tooling 25, Demo 25, Depth 20.

| Idea | Impact | Meta tooling | Demo | Depth | Weighted | Main untested risk |
| --- | --- | --- | --- | --- | --- | --- |
| **Live guide, manual first** | 6 | 9 | 8 | 7 | **7.4** | Live latency; small-part vision; Gemini Live is the nearest competitor |
| Family Sync + board | 7 | 7 | 6 | 7 | **6.8** | Diarization in real kitchen audio; weak filmability |
| Household board (photo capture) | 6 | 8 | 7 | 8 | 7.2 (from `ranked-candidates.md`) | Whiteboard read accuracy; capture habit |
| Paper Games | 5 | 7 | 8 | 6 | 6.4 | Hand-drawn mark reading; lowest Impact |
| Errand agent (computer use) | 6 | 6 | 6 | 6 | 6.0 | Demo reliability; cost |
| Scam shield | 6 | 5 | 6 | 5 | 5.6 | "Simple analyzer" label; crowded |
| Play to Comic | 5 | 7 | 8 | 5 | 6.2 | Lowest Impact; no video output |

Weighted = 0.3 Impact + 0.25 Meta + 0.25 Demo + 0.2 Depth. The live guide is the same engine as the earlier cooking plan, so its tooling and demo scores follow `ranked-candidates.md`. Cooking scored 7.7 there on stronger Impact and Demo, which I trimmed for the manual-first variant because the real-expert-voice story is lost; treat 7.4 to 7.7 as one range.

## 4. Recommendation

**Primary: the live guide, with the knowledge source as a plug-in.** Ship the engine once, with two "packs": a **manual PDF pack** (Tier 0, no expert to film, no food-health risk) and the **expert video pack** (cooking, Tier 1 if time). It leans on six Meta capabilities at once, which no other candidate does:
- Spark reads the PDF or video into numbered steps with checks (structured output).
- Frames every 1 to 2 s go to **Glimmer first** (cheap triage) and **escalate to Spark** on ambiguity, which gives the open-weights bonus a real role and mirrors the cookbook recipe.
- **SAM 3.1 puts a mask on the exact part or tool** and the evidence frame shows it, which is the "verifiable agent" story for Oct 28.
- Voice Transcribe realtime for "next", "repeat" and questions; browser speech synthesis speaks.
- Fade-out: fewer prompts as the user gets faster, the human story and the screen-away one.

Why it fits the lens: live feed is the product, hands and eyes stay on the task, it builds a skill instead of replacing one, and it is a "step-by-step agent", not an analyzer or coach, as long as the demo shows actions (state machine, evidence frame, ask-when-unsure).

**Runner-up and passion project: Family Sync + redrawn board.** It uses fewer Meta capabilities and is harder to film, but it solves the problem Vibhor lives and keeps him building after Nov 4. Choose it if the live-loop spike fails or if he would rather ship the thing he will use in December. It also reuses the same plumbing (Voice, tools, Glimmer), so little work is wasted.

**Floor:** Paper Games as the small finishable fallback, unchanged.

## 5. Spikes today (decide before product code)

1. **Live loop latency:** 3 frames plus current step to Glimmer and to Spark 1.3, median under 5 s, p90 under 8 s (`spike-plan.md` test 9).
2. **Manual to steps:** a 20-page flat-pack PDF to structured steps; no missing or invented steps.
3. **SAM part finding:** "screw", "wooden panel" on one phone photo; are the masks usable?
4. **Wrong-orientation catch:** 5 deliberate mistakes and 5 correct runs; pass is 4 of 5 caught, at most 1 false alarm.
5. **Voice diarization** (only for Family Sync): 2 speakers, a kitchen recording, one Hindi-English mix.

If 1 and 4 fail, the guide narrows to coarse visible claims plus ask-when-unsure, or switches to Family Sync. Office-hours question for Discord: is a planner or guide acceptable under the "coach" caution, and does a live-feed-with-sampled-frames product count as live?

## 6. Open items for Vibhor
- Manual-first or cooking-first for Tier 0? I lean manual-first (nothing to film, safer), with cooking as pack two.
- Is the household product more important to him than the highest rubric score?
