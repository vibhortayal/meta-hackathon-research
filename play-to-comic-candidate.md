# Play to Comic: turn a live game clip into a comic or animated short

2026-10-26. Idea from Vibhor, an extension of the community-sports idea: record clips of live games (pickleball, tennis, friends' matches), the AI finds the key play and turns it into a comic, anime or animated-film style short. Scores are my judgement. **Muse Image and Spark behavior on real sports footage is untested.**

## What the Meta models actually output (read from the docs today)
- **No Meta model outputs video or audio.** Spark and Wonder take text, image, video, audio and PDF in and give text out. Muse Image takes text and images in and gives still images out ([models page](https://dev.meta.ai/docs/models)).
- **Muse Image:** stills only, $0.01 per generated image, 1 to 10 input images per edit, multi-turn edits via `previous_response_id`, no mask. Docs give **no latency figures** and do not address character consistency or real-person likeness ([image generation docs](https://dev.meta.ai/docs/image-generation)). Safety blocks return a 400 `content_policy_violation` and are not billed.
- **Consequence:** a true stylized video cannot come from Meta models. "Animated" means an assembled sequence of stills: panel-to-panel motion, or a short frame sequence, built with ffmpeg or the browser. A third-party video model would weaken the "really uses Meta models" test and is not recommended.

## Pipeline
1. **Find the play:** Spark 1.3 watches the clip (video input) and returns the key rally as structured JSON: start and end timestamps, what happened in plain words, 4 to 6 beats. Banter from the audio goes through Voice Transcribe (Spark 1.3 audio is degraded per the docs, so do not rely on it for speech).
2. **Cut keyframes:** ffmpeg pulls frames at the beat timestamps. SAM 3.1 video tracking could mark players and the ball for speed lines and trails; **ball tracking on a small fast ball is untested**, so treat it as stretch.
3. **Stylize:** Muse Image edit takes each keyframe plus the same reference frames of the players and a style prompt, one call per panel.
4. **Compose:** HTML or canvas lays out panels, speech bubbles from the transcribed banter, caption boxes written by Spark, and a splash panel for the winning shot. Export as a PNG page and, for the animated version, an MP4 with simple motion (zooms, panel wipes).
5. **Voice:** Meta has no text-to-speech, so narration uses the browser's speech synthesis or is skipped; bubbles carry the voice.

## Prior art (shallow, one pass)
- **True video restyle:** Magic Hour offers video-to-video anime and cartoon templates for NFL, basketball and football clips ([example](https://magichour.ai/templates/details/cm47rse6a0cyv1u10xzk7tnoh-nfl-retro-anime-winter)). Pickleball is not covered in what I saw. These make real moving stylized video, which Meta models cannot, so a judge who has seen them will compare.
- **Highlight finding is a commodity:** PlaySight already auto-cuts rallies and highlights on padel, pickleball and tennis courts and sells clips for under about €5 ([PlaySight Weekly](https://thepadelweekly.com/playsight-redefines-racquet-sports-with-new-ai-driven-highlight-feature/)); SwingVision generates highlights for tennis and pickleball ([roundup](https://imagen-ai.com/post/best-ai-video-highlights-generator-sports-2026/)). Both are claims from vendor or trade pages.
- **Not checked:** phone apps that make comic strips from video, and whether any combine highlight picking, comic storytelling and real banter.
- **Our honest angle:** not "restyle pixels" but "tell the story of the point" with panels, captions and your friends' real words. A comic page is something a still-image model can do well and a video-restyler cannot.

## Rules, consent and rights
- **Sports-analyzer rule:** this is creative generation, not play analysis. To stay on the right side, output no stats, no coaching, no line calls, no "you should have." The key-play selection is for storytelling. Say that explicitly in the README and demo.
- **Rights:** use only footage Vibhor shot himself of consenting friends. No downloaded match clips (the same rule as the cooking plan). No minors in the demo.
- **Likeness:** stylizing real people's faces may hit Muse Image's content policy or may be fine; the docs do not say. Test early. Get written consent from everyone who appears.
- **Style naming:** avoid naming a studio's trademarked style ("Pixar") in prompts, marketing or the repo; say "3D animated-film style." Whether Muse Image refuses such prompts is unknown.
- **Privacy:** clips go to Meta's API (standard mode keeps prompts out of training per the docs). This idea has no local-first story, unlike the household agent.

## Cost
Estimate, not measured: images are $0.01 each, so a 6-panel comic is about $0.06 per pass; allowing 3 retries per panel is about $0.20. A 5-second frame-sequence animation at 8 fps is 40 images, about $0.40 per pass. Spark video-input token cost per clip is **unknown** and may dominate; measure it. The $150 Meta credit covers hundreds of clips at these rates, but a spend cap in code is still required.

## Bonus prizes
Best Creative Build ($5K, Muse Image): strong fit. Most Viral ($20K): the best viral shape of any candidate, because a comic of your own match is something people want to post on X. Community Vote ($10K): plausible. Best Agentic: weak unless it plans the shots and retries autonomously. Open Weights: none (Muse Image is hosted only).

## Rubric (my scores)
| Criterion | Score | Reason | What would raise it |
| --- | --- | --- | --- |
| Stage 1 | Pass | Fits "Build for Your World"; real use of Spark video, Muse Image, Voice Transcribe, optional SAM | n/a |
| Impact (30%) | 4 | Joy and community engagement, but no problem with sourced evidence of need | Tie to Khelo's goal of fun score entry and banter with real pilot users; a measure of replays and shares |
| Meta tooling (25%) | 8 | Spark video, Muse Image, Voice Transcribe, SAM 3.1 | Use SAM tracking visibly |
| Demo (25%) | 9 | A shaky rally becomes a manga page with friends' real words; instantly understood | Strong source clip |
| Depth (20%) | 6 | Highlight selection, keyframe pipeline, consistency across panels, retries. Could be called a wrapper if consistency and selection are weak | Measured consistency, abstain when no clear play, cost cap |
| **Weighted** | **6.7** | | |

Assumption-based: Demo (needs clean consistency and a policy-clean likeness), Depth (selection quality), and every latency figure.

## Separate from Khelo?
**Yes, a new repo built from Oct 27.** Khelo predates the hackathon (see `khelo-and-sports-organizer.md`), and the guide says the demo may show only what was built during it. The standalone web app takes an uploaded clip and returns a comic. An optional "post to a Khelo community" export can be built after Nov 4. Whether showing Khelo as a disclosed integration is acceptable needs the organizers' answer.

## Tiers to Oct 31
- **Tier 0 (by Oct 29):** upload a clip, Spark picks the key rally and writes the 4 to 6 beat script, ffmpeg cuts keyframes, Muse Image restyles each into a comic panel, an HTML page with captions exports a PNG. Public repo and hosted demo.
- **Tier 1 (by Oct 31):** friends' banter into speech bubbles via Voice Transcribe, style picker (comic, anime, 3D animated-film), the same reference frames across panels for consistency, MP4 export with panel motion, spend cap and a visible "no clear play" refusal.
- **Tier 2 (only if solid):** frame-sequence animation, SAM 3.1 trails and speed lines, share card for X, Khelo export.

## Spike today (before product code on Oct 27)
Film three 10 to 20 second rallies with consenting friends. Check: (1) Spark picks the key moment in 2 of 3 clips (human judge); (2) Muse Image keeps players recognizable and outfits consistent across 4 panels in at least 2 of 3; (3) real-person photos pass the content policy; (4) per-panel time and Spark video cost per clip. Pass: all four.

## Demo moment
Split screen. On the left, a shaky phone clip of an absurd 14-shot rally. Twenty seconds later, on the right, the same rally as a manga page: panel by panel, a splash panel for the winner, and speech bubbles carrying the friends' real shouted words ("Not today, Raj!"). The friends watch it and laugh.

## Honest read
Highest viral and demo shape, lowest Impact and weakest local-first story. Feasible, but its depth is thin unless selection and consistency are measured, and a judge who has seen true video restyling may find a comic page small. Best as a delight feature for Khelo, or as a floor-level entry if Paper Games is not chosen.
