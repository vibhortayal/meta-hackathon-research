# Meta Hackathon Product Reference — PRODUCTS.md

*Compiled 2026-10-27 for the Meta Global AI Developer Hackathon (hacking Oct 26 – Nov 4, 2026). Project context: an AI agent built on Meta's open-weight models that helps people learn and do hands-on tasks.*

> **Access caveat (read first):** The nine canonical product pages on dev.meta.ai could **not be fetched directly** — the domain is blocked by fetch policy in this environment, so every dev.meta.ai URL below is listed as the canonical product page but was **not read first-hand**. All facts were reconstructed from indexed secondary sources (tech press, API catalogs, and developer guides) that quote or mirror Meta's published pages, docs, and pricing. Where a fact comes from a secondary source, that source's URL is cited. Figures should be re-verified against dev.meta.ai before locking a budget or architecture. Anything not found in any source is stated as "not published / not found" — nothing here is invented.

---

## 1. Muse Spark series (closed models, hosted)

Canonical page: https://dev.meta.ai/models/muse-spark *(not directly readable — see caveat)*

**What it is.** Meta Superintelligence Labs' multimodal reasoning model family, "built for agentic tasks" — tool use, computer use, coding, and multimodal understanding. The original Muse Spark launched April 2026 with no public developer API; Muse Spark 1.1 (released July 9, 2026) was the first version opened to outside developers, alongside the public preview of the Meta Model API (https://pondero.ai/news/2026-07-12-meta-muse-spark-1-1-launch-model-api/). Muse Spark 1.3 is the current version and the one Meta marks "Recommended for new work" (https://www.orcarouter.ai/blog/muse-api). The models are closed/hosted — no downloadable weights (the open-weights sibling is Muse Spark Open, §8).

**Model IDs (exact, as published).**
- `muse-spark-1.3`, `muse-spark-1.2`, `muse-spark-1.1` — Standard mode (https://shipwithmuse.live/blog/muse-developer-platform)
- `muse-spark-1.3-contributor`, `muse-spark-1.2-contributor` — Contributor mode. There is **no** Contributor variant of 1.1 (https://www.orcarouter.ai/blog/muse-api)

**Capabilities and modalities.**
- Inputs: text, images, video, and documents/PDF; output: text (https://www.marktechpost.com/2026/07/09/meta-superintelligence-labs-releases-muse-spark-1-1/; https://shipwithmuse.live/blog/muse-for-developers). One API catalog also lists audio among Spark inputs (https://www.orcarouter.ai/blog/muse-api, model-page screenshot description).
- It is a reasoning model: it thinks before answering, and reasoning effort is adjustable per request via `reasoning_effort` (reported range `minimal` to `xhigh`; there is no "off"). Reasoning tokens are billed as output tokens (https://pondero.ai/news/2026-07-12-meta-muse-spark-1-1-launch-model-api/; https://big-agi.com/docs/connect-meta).
- Parallel tool calling with streamed arguments, structured output, prompt caching, a Files API, and tool search with deferred loading (https://shipwithmuse.live/blog/muse-developer-platform).
- Built-in `web_search` tool on Responses API calls returns cited answers; billed separately (see pricing) (https://www.marktechpost.com/2026/07/09/meta-superintelligence-labs-releases-muse-spark-1-1/).
- Computer use (write scripts, navigate UIs, orchestrate across apps), multi-agent orchestration (as main agent or subagent), repository-level code edits, and "active context management" — the model can compact context during long tasks (https://www.developersdigest.tech/blog/meta-muse-spark-1-1-developer-guide-2026; https://pondero.ai/news/2026-07-12-meta-muse-spark-1-1-launch-model-api/).

**Key specs.**
- Context window: **1,048,576 tokens**, one figure for the whole 1.1/1.2/1.3 line (https://www.orcarouter.ai/blog/muse-api).
- No long-context premium: the per-token rate is the same whether the window is nearly empty or full (https://www.orcarouter.ai/blog/muse-api).

**Access route.** Meta Model API only (§6), at `https://api.meta.ai/v1`, in Responses, Chat Completions, and Messages formats. Also reachable via Vercel AI Gateway, OpenRouter, Cursor, and OpenCode (https://shipwithmuse.live/blog/muse-developer-platform). Consumers get it free in "Thinking" mode in the Meta AI app and on meta.ai (https://www.marktechpost.com/2026/07/09/meta-superintelligence-labs-releases-muse-spark-1-1/).

**Pricing (Meta Model API, per 1M tokens).**
- Standard: **$1.25 input / $0.15 cached input / $4.25 output** — prompts/completions **not** used for training.
- Contributor: **$0.10 input / $0.002 cached input / $0.20 output** — Meta **may** train on your prompts and completions.
- Web search grounding: **$2.50 per 1,000 queries**.
(https://shipwithmuse.live/blog/muse-developer-platform; https://aiusagelimits.com/api-rate-limits-pricing/)
- Multiple launch reports cite a one-time **$20 credit for new accounts** in the public preview (https://pondero.ai/news/2026-07-12-meta-muse-spark-1-1-launch-model-api/); one docs-based reference says Meta's docs do **not** confirm any free tier or trial credit (https://www.orcarouter.ai/blog/muse-api). Treat the $20 as an unverified launch offer — check the dashboard.

**Rate limits (per team, shared across all keys on the team).**
- Standard: **3,000 RPM / 4,000,000 TPM**.
- Contributor: **150 RPM / 3,000,000 TPM** per Meta's pricing page as quoted by two sources (https://aiusagelimits.com/api-rate-limits-pricing/; https://www.orcarouter.ai/blog/muse-api); one secondary source says 100 RPM for Contributor (https://shipwithmuse.live/blog/muse-for-developers) — verify on the pricing page.

**Limitations / requirements.**
- The 1.1 public preview was described as **US-only, with no EU access yet** (https://www.marktechpost.com/2026/07/09/meta-superintelligence-labs-releases-muse-spark-1-1/).
- Billing must be configured on the account before API-key creation is enabled (https://www.marktechpost.com/2026/10/13/meta-muse-wonder-muse-wonder-full-release/).
- Quirk: Spark emits a non-standard SSE event that trips some OpenAI-compatible streaming clients (https://shipwithmuse.live/blog/muse-for-developers).
- Reasoning latency: every reply reasons first; a two-word reply was measured at ~340 reasoning tokens and ~9 s at default effort by one third-party integration (https://big-agi.com/docs/connect-meta).

---

## 2. Muse Wonder

Canonical page: https://dev.meta.ai/models/muse-wonder *(not directly readable — see caveat)*

**What it is.** Meta's frontier model family, released **October 12, 2026**: **Muse Wonder** ("fast frontier performance") and **Muse Wonder Full** ("the full version of the model"), built for "personal and professional agentic work" (https://www.marktechpost.com/2026/10/13/meta-muse-wonder-muse-wonder-full-release/; https://www.linkedin.com/news/story/meta-rolls-out-paid-muse-wonder-ai-for-agent-apps-7677812/). Meta pitches both at "frontier coding, long-running agents and advanced computer use" (https://www.curatedai.net/guides/meta-muse-wonder-explained.html).

**Model IDs (exact, as published).**
- `muse-wonder-1.0` — the only Wonder callable on the Meta Model API (https://apidog.com/blog/what-is-muse-wonder/).
- `muse-wonder-full-1.0` — exists as an ID in Muse Code plan contexts, but has **no API SKU and no per-token price** (https://techpilot.ai/tools/muse-wonder/).

**Capabilities and modalities.**
- Inputs: text, images, video, screenshots, charts, and documents/PDF; output: text. Both models have a **1M-token context window** (https://www.curatedai.net/guides/meta-muse-wonder-explained.html; https://techpilot.ai/tools/muse-wonder/). One API catalog also lists **audio** as a Wonder input (https://www.aicompare.ninja/en/tool/meta-model-api); another source says audio support "still has to be confirmed on each product" (https://www.curatedai.net/guides/meta-muse-wonder-explained.html) — do not assume audio input.
- Two named agent capabilities: **Active Memory** (carries context across conversations and retrieves what's relevant) and **Active Focus** (sustains effort on a hard goal, works through blockers, checks in before important actions) (https://www.linkedin.com/news/story/meta-rolls-out-paid-muse-wonder-ai-for-agent-apps-7677812/).
- Deeper domain expertise in law, finance, and health; handles long-running software projects end to end; described by Meta as its most aligned model to date (same source).
- Adjustable reasoning effort (`minimal` to `max`); `max` does not select Wonder Full (https://www.aicompare.ninja/en/tool/meta-model-api).

**Access route.**
- `muse-wonder-1.0`: Meta Model API (§6); also OpenRouter (`meta/muse-wonder`), Vercel AI Gateway, and Cloudflare Workers AI at the same token prices (https://apidog.com/blog/what-is-muse-wonder/).
- **Muse Wonder Full: not on any API.** It is available only inside **Muse Code** subscriptions on the Power ($50/mo) or Maximum ($200/mo) plans (https://techpilot.ai/tools/muse-wonder/; https://letsdatascience.com/blog/metas-best-model-skips-api-coding-plan-trains-on-your-code).
- Muse (consumer app): Wonder is rolling out to $20/$100 subscribers first (https://apidog.com/blog/what-is-muse-wonder/).

**Pricing (Meta Model API, per 1M tokens).** **$4.00 input / $0.20 cached input / $20.00 output**, Standard mode only — Meta states "Contributor mode isn't available for Muse Wonder on Model API," so there is no discounted tier (https://www.orcarouter.ai/blog/muse-api). Web search adds $2.50 per 1,000 queries (https://saascity.io/blog/meta-muse-wonder-frontier-model-pricing-2026).

**Rate limits.** 3,000 RPM / 4,000,000 TPM per team (https://apidog.com/blog/what-is-muse-wonder/).

**Limitations / cautions.**
- The strongest model in the family cannot be built against programmatically — anything that depends on Wonder Full depends on a Muse Code seat, not an endpoint (https://letsdatascience.com/blog/metas-best-model-skips-api-coding-plan-trains-on-your-code).
- Token hunger: independent measurement put Wonder at ~$4.52 per Intelligence Index task, consuming 2–7× more input tokens than rival models, mostly cache writes/reads — list price understates task cost for verbose agent loops (https://apidog.com/blog/what-is-muse-wonder/).

---

## 3. Muse Image

Canonical page: https://dev.meta.ai/models/muse-image *(not directly readable — see caveat)*

**What it is.** Meta Superintelligence Labs' first image generation model — generation and precise editing in one model. Announced July 7, 2026 inside Meta AI, Instagram, and WhatsApp; it joined the Meta Model API on **August 26, 2026** as `muse-image-1.0` (https://fal.ai/muse-image; https://mungomash.com/ai/llama/versions/). It is served on the same API, base URL, and key as Muse Spark — not a separate image credential (https://www.orcarouter.ai/blog/muse-image).

**Model ID.** `muse-image-1.0` (also routed by OpenRouter as `meta/muse-image`) (https://www.orcarouter.ai/blog/muse-image; https://mungomash.com/ai/llama/versions/).

**Capabilities and modalities.**
- Input: text prompt, plus reference images for editing/composition. Output: images.
- **Generate** — `POST /v1/images/generations`, text prompt in, image out.
- **Edit** — `POST /v1/images/edits`, prompt plus input images; instruction-based edits preserve the rest of the frame with **no mask and no separate inpainting model** ("name the element to change and the remaining pixels are preserved").
- **Multi-turn refine** — `POST /v1/responses` (the Responses API) for conversational, multi-turn refinement without visible quality degradation across turns.
(All three endpoints: https://www.orcarouter.ai/blog/muse-image; edit-preservation behavior: https://fal.ai/muse-image.)
- **Multi-image composition:** up to 10 reference images, each taggable with a role (subject, product, environment, palette); untagged references "tend to produce an average of themselves" (https://muapi.ai/muse-image; https://fal.ai/muse-image).
- **Agentic behavior:** during generation it can use tools — it writes and runs code when an element must be exact (a scannable QR code, a chart with real numbers), and can search the web / image-search to ground knowledge-heavy prompts — and it self-reviews drafts, fixing small errors by editing, large ones by regenerating (https://marcbazemore.medium.com/metas-muse-image-thinks-before-it-draws-04c10bf9ad39; https://www.orcarouter.ai/blog/muse-image). On the images endpoints this is controlled by a `tool_enablement` extension (`enable_image_search`, `enable_web_search`, `enable_shell`) and a `reasoning_strength` of `high` (default) or `low` (https://www.orcarouter.ai/blog/muse-image).

**Parameters (as documented).** `n` 1–10, default 1; `size` is a "WxH" string that **sets aspect ratio only, not exact pixels**; `response_format` `b64_json` (default) or `url`; `output_format` `webp` (default), `png`, or `jpeg` (https://www.orcarouter.ai/blog/muse-image). One integration reports one WebP image returned per request and no streaming (https://hermes-agent.nousresearch.com/docs/user-guide/features/image-generation; https://big-agi.com/docs/connect-meta).

**Access route.** Meta Model API (§6), plus third-party routers (fal, OpenRouter). A Medium analysis written from the consumer launch claimed "no public API," but that predates/conflicts with the documented API launch on Aug 26, 2026 — the API endpoints above are documented in Meta's developer docs per OrcaRouter (https://www.orcarouter.ai/blog/muse-image).

**Pricing.** **$0.01 per image** on the Meta Model API (https://www.orcarouter.ai/blog/muse-api). Third-party resellers charge differently (e.g., $0.02/image at Muapi) (https://muapi.ai/muse-image).

**Rate limits.** 150 RPM, no token cap (https://www.orcarouter.ai/blog/muse-api).

**Limitations.** `size` does not guarantee exact output resolution (aspect ratio only); text-to-image only via the Hermes integration (that limit is the integration's, not the model's) (https://www.orcarouter.ai/blog/muse-image; https://hermes-agent.nousresearch.com/docs/user-guide/features/image-generation).

---

## 4. Muse Voice Transcribe

Canonical page: https://dev.meta.ai/models/muse-voice-transcribe *(not directly readable — see caveat)*

**What it is.** Meta Superintelligence Labs' first real-time audio perception model, launched **September 1, 2026**. It combines streaming automatic speech recognition (ASR), speaker diarization, and endpointing (detecting when a speaker has finished a turn) in a single model, with no separate post-processing step. Meta describes it as "an autoregressive multimodal model from the Muse Spark family" (https://hiindia.com/meta-launches-muse-voice-transcribe-with-native-support-for-five-indian-languages/; https://slator.com/meta-launches-muse-voice-transcribe/). It also powers dictation in Meta AI for Mac and in Muse Code (https://9to5mac.com/2026/09/01/meta-launches-muse-voice-transcribe-for-real-time-voice-dictation-on-mac/).

**Model ID.** `muse-voice-transcribe-1.0` (https://mungomash.com/ai/llama/versions/).

**Capabilities and modalities.**
- Input: live audio streams or prerecorded audio. Output: transcript text with speaker attribution and speaker-turn timestamps.
- **Streaming ASR:** audio is processed in **80 ms chunks** (12.5 Hz), each becoming a soft token; the model decides per chunk whether to keep listening or emit a token. Meta calls this RL-trained behavior **"adaptive delay"** — easy words commit fast, hard words get more context (https://www.techrepublic.com/article/news-meta-muse-voice-transcribe-real-time-speech/; https://hiindia.com/meta-launches-muse-voice-transcribe-with-native-support-for-five-indian-languages/).
- **Diarization:** identifies **more than 20 speakers** and assigns speech to each (https://slator.com/meta-launches-muse-voice-transcribe/).
- **Languages:** trained on **70+ languages**, of which **25 were extensively validated** for the initial release (including Hindi, Tamil, Telugu, Kannada, Malayalam); Meta recommends the validated 25 for the initial release. Native **code-switching** recognition within and between sentences (https://slator.com/meta-launches-muse-voice-transcribe/; https://www.techrepublic.com/article/news-meta-muse-voice-transcribe-real-time-speech/).
- **Biasing:** developers can supply a language bias and keywords (names, specialist terminology, places, product names). Per Meta these inputs **guide rather than constrain** the model and do not guarantee a particular spelling (https://slator.com/meta-launches-muse-voice-transcribe/).
- **Long audio:** processes recordings exceeding one hour without separate post-processing (https://slator.com/meta-launches-muse-voice-transcribe/).
- Meta claims it ranked first on Artificial Analysis' streaming speech-to-text leaderboard and public diarization benchmarks as of Sept 1, 2026 (https://www.techrepublic.com/article/news-meta-muse-voice-transcribe-real-time-speech/).

**Access route — two endpoints on the Meta Model API (§6).**
- Live: WebSocket at `wss://api.meta.ai/v1/asr/realtime`.
- Recordings: `POST /v1/asr/transcribe`.
(https://mungomash.com/ai/llama/versions/; https://www.orcarouter.ai/blog/muse-api)

**Pricing.** **$0.18 per audio hour** (= $3 per 1,000 audio-minutes), billed per hour of audio, not per token (https://9to5mac.com/2026/09/01/meta-launches-muse-voice-transcribe-for-real-time-voice-dictation-on-mac/; https://www.orcarouter.ai/blog/muse-api).

**Limitations (stated).** The API returns **timestamps for speaker turns, not individual words**; it provides **no confidence scores**, no sound-event or emotion detection, and no transcript reformatting (https://slator.com/meta-launches-muse-voice-transcribe/).

---

## 5. SAM 3.1

Canonical page: https://dev.meta.ai/models/sam-3-1 *(not directly readable — see caveat)*

**What it is.** Meta's segmentation model — from the FAIR "Segment Anything" line, **not** a Muse-family model (https://mungomash.com/ai/llama/versions/). SAM 3 (November 2025) replaced point/box prompting with **Promptable Concept Segmentation (PCS)**: give it a short text concept (e.g. "red bicycle") or a visual exemplar and it detects, segments, and tracks **all matching instances**. SAM 3.1 (released March 27, 2026) adds **Object Multiplex** — objects are processed jointly in fixed 16-object buckets with shared temporal memory — plus new checkpoints and inference optimizations; Meta reports roughly **7× faster inference at 128 objects on one H100** vs. the original SAM 3 release (a controlled comparison in the paper reports 5.2×). Accuracy changes are benchmark-dependent, not uniformly better (https://learnopencv.com/sam-3-whats-new/). SAM 3.1 was added to the Meta Model API on **September 18, 2026** (https://mungomash.com/ai/llama/versions/; https://learnopencv.com/sam-3-whats-new/).

**Model ID.** `sam-3.1` on the Meta Model API (https://learnopencv.com/sam-3-whats-new/). Self-hosted checkpoint: `facebook/sam3.1` on Hugging Face, file `sam3.1_multiplex.pt` (gated) (https://learnopencv.com/sam-3-whats-new/).

**Capabilities and modalities.**
- Input: an image or a video plus **one short text concept phrase**. Output: bounding boxes and **pixel-level masks** for every matching instance, with persistent object IDs and tracking across video frames (https://www.kucoin.com/news/flash/meta-launches-sam-3-1-api-for-image-and-video-segmentation; https://learnopencv.com/sam-3-whats-new/).
- The underlying SAM 3 model is an 848M-parameter unified model: a shared Perception Encoder feeding a concept-conditioned detector (with a Presence Head that scores whether the concept is present at all) and a memory-based tracker that maintains identities ("masklets") and discovers new instances as they enter (https://learnopencv.com/sam-3-whats-new/).
- **Prompt types differ by route:** the hosted API **currently accepts text prompts only**; the native/open-weight implementation also supports visual prompts — points, boxes, image exemplars, and click/box refinement (https://learnopencv.com/sam-3-whats-new/).

**Access routes (three).**
1. **Meta Model API** — `POST /v1/responses` with `model="sam-3.1"` via the OpenAI-compatible client; output is structured text containing boxes and encoded masks, decoded with Meta's published Python package **`meta-sam-parser`** (https://learnopencv.com/sam-3-whats-new/).
2. **Downloadable open weights** — gated Hugging Face repo under **Meta's SAM License** (not Apache 2.0); self-hosting requires Python 3.12+, PyTorch 2.7+, and an NVIDIA CUDA GPU (CUDA 12.6+) (https://learnopencv.com/sam-3-whats-new/). SAM 3.1 is the one Meta Model API model whose weights you can also download (https://mungomash.com/ai/llama/versions/).
3. **Third-party hosted** — e.g. fal (`fal-ai/sam-3-1/video`) (https://learnopencv.com/sam-3-whats-new/).

**Hosted API limits (as documented).**
- Video: at most **15,000 input frames** per request (≈ 8 min 20 s at 30 FPS) and at most **16 tracked objects per frame** (https://learnopencv.com/sam-3-whats-new/).
- Containers: MP4 and MOV with H.264, H.265, or MPEG-4 video; **WebM/VP9 is not supported** (https://learnopencv.com/sam-3-whats-new/).
- **One concept per request.** Commas are *not* a documented multi-label separator in Meta's native predictor or the Model API — different concepts require separate requests. (Object Multiplex's "16" is a bucket width for object *instances*, not labels.) (https://learnopencv.com/sam-3-whats-new/)
- The hosted 16-object cap differs from self-hosting, where multiple 16-object buckets scale to 128+ objects (https://learnopencv.com/sam-3-whats-new/).

**Pricing (Meta Model API).** **$2.50 per 1,000 images** and **$0.20 per 1,000 video frames** — billed per image/frame, not per token. Worked example: a 1-minute 30 FPS clip = 1,800 frames = $0.36 per concept request (https://learnopencv.com/sam-3-whats-new/; https://www.orcarouter.ai/blog/muse-api).

**Limitations (stated).**
- Tracking can still drift: detector refresh mitigates identity loss but cannot guarantee recovery after long occlusion, severe motion blur, or interactions between similar instances; track IDs should not be treated as guaranteed identities across full occlusion or exit/re-entry (https://learnopencv.com/sam-3-whats-new/).
- Presence/confidence scores need calibration on representative data for the target camera/domain before being used as thresholds (https://learnopencv.com/sam-3-whats-new/).
- PCS prompts are intentionally short, visually groundable noun phrases; long referring expressions or requests that need reasoning belong on a multimodal-language-model path (https://learnopencv.com/sam-3-whats-new/).
- Fine-grained domain transfer can be weak (niche aircraft types, medical terms, thermal imagery) (https://learnopencv.com/sam-3-whats-new/).
- Known upstream bug at the time of the LearnOpenCV write-up: the multiplex predictor's session start had a signature mismatch (`offload_state_to_cpu`) with an unmerged fix — pin a reviewed source commit if self-hosting (https://learnopencv.com/sam-3-whats-new/).

---

## 6. Meta Model API (the platform)

Canonical page: https://dev.meta.ai/products/meta-model-api *(not directly readable — see caveat)*

**What it is.** Meta's hosted inference platform — in Meta's own one-sentence definition, "the inference platform for the latest models from Meta including Muse Wonder and Muse Spark" (https://www.orcarouter.ai/blog/muse-api). Base URL **`https://api.meta.ai/v1`**; auth is a Bearer <redacted> sent in the `Authorization` header, stored in the **`MODEL_API_KEY`** environment variable (https://shipwithmuse.live/blog/muse-for-developers; https://www.orcarouter.ai/blog/muse-api).

**Compatibility.** Three documented request surfaces — **Responses API, Chat Completions API, Messages API** — and Meta's headline claim is drop-in compatibility with the OpenAI SDK, the Anthropic SDK, and OpenAI-compatible agent CLIs: "no custom client to learn." **Meta publishes no first-party SDK** (https://www.orcarouter.ai/blog/muse-api). Note the OpenAI SDK does not auto-read `MODEL_API_KEY` — pass `api_key` explicitly or export the key as `OPENAI_API_KEY` (https://www.orcarouter.ai/blog/muse-api).

**Endpoints named in Meta's reference.** `POST /v1/responses`, `POST /v1/chat/completions` (text); `POST /v1/images/generations`, `POST /v1/images/edits` (Muse Image); `POST /v1/asr/transcribe` and WebSocket `wss://api.meta.ai/v1/asr/realtime` (transcription); `POST /v1/files` (uploads) (https://www.orcarouter.ai/blog/muse-api). SAM 3.1 is called through `POST /v1/responses` with `model="sam-3.1"` (https://learnopencv.com/sam-3-whats-new/).

**Models served (exact IDs).** `muse-spark-1.3`, `muse-spark-1.2`, `muse-spark-1.1`, `muse-spark-1.3-contributor`, `muse-spark-1.2-contributor`, `muse-wonder-1.0`, `muse-image-1.0`, `muse-voice-transcribe-1.0`, `sam-3.1` (https://shipwithmuse.live/blog/muse-developer-platform).
**Not served:** Muse Glimmer (weights-only; Meta excludes it from the models list endpoint), Muse Spark Open (served by third-party hosts instead), Muse Wonder Full (Muse Code subscriptions only) (https://www.orcarouter.ai/blog/muse-api; https://anchorterminal.com/tools/muse-spark-open; https://techpilot.ai/tools/muse-wonder/).

**Full price list (Meta's published rates).**
| Item | Price |
| --- | --- |
| Muse Spark Standard | $1.25 in / $0.15 cached / $4.25 out per 1M tokens |
| Muse Spark Contributor | $0.10 in / $0.002 cached / $0.20 out per 1M tokens |
| Muse Wonder (`muse-wonder-1.0`) | $4.00 in / $0.20 cached / $20.00 out per 1M tokens |
| Web search grounding | $2.50 per 1,000 queries |
| Muse Image | $0.01 per image |
| Muse Voice Transcribe | $0.18 per audio hour |
| SAM 3.1 | $2.50 per 1,000 images / $0.20 per 1,000 video frames |
(https://www.orcarouter.ai/blog/muse-api; https://shipwithmuse.live/blog/muse-developer-platform)

**Rate limits (per team — all keys on a team share one ceiling).**
- `muse-spark-1.3/1.2/1.1` and `muse-wonder-1.0`: **3,000 RPM / 4,000,000 TPM**.
- Contributor variants: **150 RPM / 3,000,000 TPM** (one secondary source says 100 RPM — verify).
- `muse-image-1.0`: 150 RPM, no token cap.
- Background responses: separate ceiling of 600 submissions/minute/team.
- On breach: HTTP 429 with `Retry-After`, plus `x-ratelimit-*` headers.
(https://www.orcarouter.ai/blog/muse-api; https://aiusagelimits.com/api-rate-limits-pricing/)

**Accounts, keys, billing.**
- Access = a Model API account + key from the dashboard (API keys → Create API key). **Copy the key right away — you only see it once.** Revoking one key leaves other team keys untouched; Meta's own advice is one key per application (https://www.orcarouter.ai/blog/muse-api).
- A payment method must be added under Billing before **Create API key** becomes enabled (https://www.marktechpost.com/2026/10/13/meta-muse-wonder-muse-wonder-full-release/).
- Billing is usage-based: input and output counted separately; charges land when the balance reaches the payment threshold, with any remainder charged on the 1st of the month; "no minimums or upfront commitment" (https://www.orcarouter.ai/blog/muse-api).
- An API key does not guarantee access to every model: Meta documents `404 model_not_found` for teams that can't access a requested model (https://learnopencv.com/sam-3-whats-new/).
- **Not published:** no org/project hierarchy (team is the only grouping), no key scopes or read-only keys, no key expiry/rotation procedure, no documented free tier/trial credit (https://www.orcarouter.ai/blog/muse-api).
- A Muse Code subscription does **not** state any entitlement to Model API tokens — the two billing systems are separate (https://www.orcarouter.ai/blog/muse-api).
- The API launched as a US-only public preview (July 2026); EU access was not available at launch (https://www.marktechpost.com/2026/07/09/meta-superintelligence-labs-releases-muse-spark-1-1/).

---

## 7. Muse Glimmer (open weights)

Canonical page: https://dev.meta.ai/models/muse-glimmer *(not directly readable — see caveat)*

**What it is.** A 30B-parameter dense multimodal model **distilled from Muse Spark**, released **August 10, 2026** by Meta Superintelligence Labs under **Apache 2.0**, designed for "always-on local agents" on consumer hardware (https://www.datacamp.com/blog/muse-glimmer; https://www.marktechpost.com/2026/08/10/meta-ai-releases-muse-glimmer/). Meta's own framing: "small enough to run on a Mac or PC with a single consumer GPU, enabling use cases that range from local agents and function calling, to local coding, and LLM-as-a-judge evaluation" (https://tech-insider.org/meta-muse-glimmer-open-weight-ai-model-2026/).

**Model ID / distribution.** Hugging Face download shown as `meta-ai/muse-glimmer-30b` (https://tech-insider.org/meta-muse-glimmer-open-weight-ai-model-2026/). The Hugging Face collection carries BF16 weights, GGUF k-quants, ExecuTorch builds, and the DFlash speculative-decoding drafter (https://www.marktechpost.com/2026/08/10/meta-ai-releases-muse-glimmer/). There is **no Meta-hosted API and no API model ID** — Meta excludes Glimmer from the Model API models endpoint; you download it (https://www.orcarouter.ai/blog/muse-api). Third-party hosted serving exists (Together AI, Fireworks AI) (https://www.datacamp.com/blog/muse-glimmer).

**Capabilities and modalities.**
- Input: **text and images**; output: **text only**. No audio; video is handled as individual frames (https://www.datacamp.com/blog/muse-glimmer; https://madrobot.blog/2026/10/10/meta-muse-glimmer-how-to-run-locally-ollama-lm-studio-vs-qwen-gemma/).
- Tuned for reliable tool/function calling, planning, self-checking and failure recovery over long tasks, local coding, and grading other models' outputs. Meta-reported results include MCP-Atlas 75.5 and SWE-Bench Pro 51.2 in its size class (https://www.datacamp.com/blog/muse-glimmer; https://thestackobserver.com/the-open-source-agent-stack-what-meta-nvidia-and-vllm-shipped-this-week-for-local-ai-agents/).

**Key specs (from the model card, via secondary sources).**
- ~29.6B parameters total, including a ~1.8B-parameter vision encoder (frozen ViT-style) plus a ~28B text decoder (https://dev.to/roberts_jakuko_fbc04cb38/qwen38-27b-vs-muse-glimmer-30b-which-permissive-open-weight-model-fits-your-local-gpu-36h1; https://thestackobserver.com/the-open-source-agent-stack-what-meta-nvidia-and-vllm-shipped-this-week-for-local-ai-agents/).
- Context window: **131,072 tokens** (https://dev.to/roberts_jakuko_fbc04cb38/qwen38-27b-vs-muse-glimmer-30b-which-permissive-open-weight-model-fits-your-local-gpu-36h1).
- Languages: trained on data from **100+ languages** (not all evaluated) (https://madrobot.blog/2026/10/10/meta-muse-glimmer-how-to-run-locally-ollama-lm-studio-vs-qwen-gemma/).
- Knowledge cutoff: **January 4, 2026** (https://madrobot.blog/2026/10/10/meta-muse-glimmer-how-to-run-locally-ollama-lm-studio-vs-qwen-gemma/).
- Footprint: ~60 GB at full precision; **under 20 GB at ~4-bit quantization** — runs on a single 24 GB consumer GPU or a Mac with unified memory (https://tech-insider.org/meta-muse-glimmer-open-weight-ai-model-2026/; https://www.datacamp.com/blog/muse-glimmer).
- Architecture notes reported by practitioners: Gemma-like with SwiGLU and gated attention, only 2 KV heads with a local/local/local/global attention pattern and a 2,048-token sliding window on local layers (KV cache barely grows with context), plus an optional DFlash block-diffusion drafter for faster structured generation (https://stonepath.tech/blog/2026-09-11-muse-glimmer-30b-local.html; https://thestackobserver.com/the-open-source-agent-stack-what-meta-nvidia-and-vllm-shipped-this-week-for-local-ai-agents/).

**Runtimes.** Day-one support in vLLM, SGLang, llama.cpp, Ollama (`ollama run muse-glimmer`), LM Studio, MLX, and Transformers (https://shipwithmuse.live/blog/muse-for-developers; https://www.marktechpost.com/2026/08/10/meta-ai-releases-muse-glimmer/).

**Pricing.** None — free weights under Apache 2.0, no per-token billing, no revenue gate (https://tech-insider.org/meta-muse-glimmer-open-weight-ai-model-2026/; https://dev.to/roberts_jakuko_fbc04cb38/qwen38-27b-vs-muse-glimmer-30b-which-permissive-open-weight-model-fits-your-local-gpu-36h1).

**Limitations / requirements (from the model card).** Meta recommends adding system-level guardrails rather than serving it as a bare endpoint, including **human confirmation before any irreversible action**; the model is not meant for under-18s (https://madrobot.blog/2026/10/10/meta-muse-glimmer-how-to-run-locally-ollama-lm-studio-vs-qwen-gemma/; https://www.marktechpost.com/2026/08/10/meta-ai-releases-muse-glimmer/). Independent local results vary — one catalog notes a Dell GB10 negative result and a 24/30 vs 30/30 comparison against Qwen 3.8 (https://shipwithmuse.live/blog/muse-for-developers).

---

## 8. Muse Spark Open (open weights)

Canonical page: https://dev.meta.ai/models/muse-spark-open *(not directly readable — see caveat)*

**What it is.** The open-weights release of the Muse Spark line, launched **October 15, 2026** — a sparse mixture-of-experts model Meta calls "the most capable US-developed open-weight model to date," trained for agentic coding and long-horizon software tasks (https://deccanfounders.com/2026/16/news/meta-muse-spark-open-816b-parameters-desktop-ai/; https://miraflow.ai/blog/meta-muse-spark-open-explained-benchmarks-hardware-license-2026). It is the full-size sibling of Muse Glimmer and shares its tokenizer; it is a **different model** from the closed Muse Wonder (https://cellcog.ai/blog/muse-spark-open/).

**Model IDs.** Hugging Face / provider ID: **`meta/muse-spark-open`** (OpenRouter lists it under the same ID) (https://modelindex.ai/models/meta/muse-spark-open; https://openrouter.ai/meta/muse-spark-open).

**Capabilities and modalities.**
- Inputs: **text, images, video, files such as PDFs, and audio**; output: **text**. Notably, it is the only model in its comparison class that accepts audio input (https://openrouter.ai/meta/muse-spark-open; https://zyvop.com/introducing-muse-spark-open-the-most-capable-us-open-weight-model-to-date-d4u3z).
- Tool calling (`tools` / `tool_choice`) and structured outputs (JSON schema via `response_format`) supported (https://openrouter.ai/meta/muse-spark-open).
- Meta-reported strengths: MCP-Atlas 89.2 and JobBench 61.8 lead its listed open-model table; it trails GLM 5.3 and Kimi K3 on Terminal-Bench 2.1 and DeepSWE 1.1 (https://miraflow.ai/blog/meta-muse-spark-open-explained-benchmarks-hardware-license-2026).

**Key specs.**
- **816B total parameters, ~42B active per token**; 62 layers; 256 experts per MoE layer, 8 routed per token (https://cellcog.ai/blog/muse-spark-open/; https://miraflow.ai/blog/meta-muse-spark-open-explained-benchmarks-hardware-license-2026).
- Context window: **1,048,576 tokens**, shared across modalities; max completion **131,072 tokens** (https://openrouter.ai/meta/muse-spark-open).
- Checkpoints: **BF16 (~1.5–1.65 TB)** and **NVFP4 (~530 GB)** (https://miraflow.ai/blog/meta-muse-spark-open-explained-benchmarks-hardware-license-2026).

**License — read carefully.** Distributed under the **Muse Model License** — *not* Apache 2.0. It allows commercial use and fine-tuning, but adds: an **attribution rule**; a **$20M revenue trigger** (a licensee whose group has >$20M gross revenue in any 12 months must notify Meta and sign a separate agreement **before offering it as Model-as-a-Service**); and **bans on military and critical-infrastructure use**. Large inference providers must contact Meta separately for a serving license, which is the likely reason hosted prices are uniform (https://miraflow.ai/blog/meta-muse-spark-open-explained-benchmarks-hardware-license-2026; https://www.eesel.ai/blog/meta-muse-spark-open-review; https://anchorterminal.com/tools/muse-spark-open). Hugging Face access is gated behind a short access form (https://thethreshold.media/blog/muse-spark-open-meta-open-weights-mac-studio-2026).

**Access routes.**
- **Download:** Hugging Face, Amazon SageMaker AI, Google Cloud Model Garden, Microsoft Foundry Models (https://deccanfounders.com/2026/16/news/meta-muse-spark-open-816b-parameters-desktop-ai/).
- **Hosted APIs:** Baseten, Fireworks AI, Groq, Modal, Nebius, OpenRouter, Together AI (https://cellcog.ai/blog/muse-spark-open/). **Not served on the Meta Model API** (https://anchorterminal.com/tools/muse-spark-open).
- **Self-host hardware reality:** BF16 serves on ~8 GPUs (e.g. 8×B300; Meta's card recommends ~2 TB VRAM); NVFP4 needs ~700 GB VRAM (4 Blackwell Ultra GPUs or 8×H200). The Apple route needs ~1 TB of unified memory — two linked 512 GB M5 Ultra Mac Studios (or four 256 GB machines) over Thunderbolt 5/RDMA with MLX; the 4-bit build alone is ~493 GB, so it cannot fit on one Mac (https://zyvop.com/introducing-muse-spark-open-the-most-capable-us-open-weight-model-to-date-d4u3z; https://thethreshold.media/blog/muse-spark-open-meta-open-weights-mac-studio-2026).
- **Inference frameworks:** vLLM, SGLang, TensorRT-LLM, Apple MLX, llama.cpp (https://deccanfounders.com/2026/16/news/meta-muse-spark-open-816b-parameters-desktop-ai/).

**Hosted pricing.** Uniform at launch across hosts: **$1.25 input / $0.15 cached input / $4.25 output per 1M tokens** on Baseten, Fireworks, Modal, Together, Nebius, and OpenRouter (https://modelindex.ai/models/meta/muse-spark-open; https://www.eesel.ai/blog/meta-muse-spark-open-review). Groq is a limited preview with a **131K** context at ~350+ tok/s (https://www.eesel.ai/blog/meta-muse-spark-open-review). Independent note: Artificial Analysis flags this as expensive for an open-weight model of its size (open-weight median ≈ $0.43 in / $1.68 out) (https://www.eesel.ai/blog/meta-muse-spark-open-review).

---

## 9. Muse Code (coding agent)

Canonical page: https://dev.meta.ai/lp/muse-code *(not directly readable — see caveat)*

**What it is.** Meta Superintelligence Labs' terminal coding agent — not a model and not an API. It takes on complete software-engineering tasks across large repositories: planning changes, writing code, running commands, and validating results (https://musecodes.io/; https://www.orcarouter.ai/blog/muse-api). Launched in beta August 2026 (Aug 5 per OrcaRouter), out of beta **August 31, 2026**, adding monthly plans, inter-session messaging, multi-agent Workflows, and an SDK in developer preview (https://musecodes.io/).

**Install & run.**
- macOS/Linux: `curl -fsSL https://dev.meta.ai/install.sh | bash` (a `| sh` variant is also published).
- Windows (native installer, PowerShell): `irm https://dev.meta.ai/install.ps1 | iex`.
- Run `muse` in your project folder; sign in via browser or paste an API key.
(https://apidog.com/blog/what-is-muse-wonder/; https://musecodes.io/)
- Platforms: macOS, Linux, and native Windows. On Windows the agent runs commands in PowerShell and **voice input and inter-session messaging are unavailable**; WSL2 also works. There is **no desktop app, IDE, or official VS Code extension** — terminal only (VS Code's integrated terminal works) (https://musecodes.io/).

**Models inside it.** Defaults to **`muse-spark-1.3`** (it launched on Spark 1.2); switch with `/models` or `muse --model muse-wonder-1.0`. Muse Wonder and **Muse Wonder Full** have been available in it since October 12, 2026 — Wonder Full only on the higher plans (see below) (https://musecodes.io/; https://apidog.com/blog/what-is-muse-wonder/).

**Features.** Subagents in isolated git worktrees; persistent background agents; auditable, replayable event logs; inter-session messaging; multi-agent Workflows; built-in skills such as `/plan`, `/grilling`, `/taste`; voice mode (dictation is powered by Muse Voice Transcribe); OS sandbox and approval prompts on by default (https://shipwithmuse.live/blog/muse-spark-for-developers; https://aiwiz.uk/blog/muse-code/; https://9to5mac.com/2026/09/01/meta-launches-muse-voice-transcribe-for-real-time-voice-dictation-on-mac/). Credential lookup order when using an API key: `META_API_KEY`, then a stored key, then a stored browser session (https://www.orcarouter.ai/blog/muse-api).

**Plans (subscription).**
| Plan | Price | Usage | Notes |
| --- | --- | --- | --- |
| Everyday | $5/mo | 10–50 prompts every 5 hours | Muse model family incl. Wonder |
| High | $15/mo | 5× Everyday | |
| Power | $50/mo | 20× Everyday | Adds Muse Wonder Full, early features |
| Maximum | $200/mo | 80× Everyday | Adds Muse Wonder Full |
(https://techpilot.ai/tools/muse-wonder/; https://musecodes.io/)
Alternatively, pay per token through the Meta Model API with your own key (§6). Installing is free; **there is no free tier** (https://musecodes.io/).

**⚠️ Data-use gotcha (important).** Muse Code **subscriptions default to Contributor mode** — and since v1.4.6, Contributor mode routes each model family to its Contributor model, so picking `muse-spark-1.3` in the model menu is **not** enough: Meta may train on your prompts, code, and outputs until you turn Contributor mode **off in `/settings`** (subscriptions only). Meta's API terms also forbid sending Contributor models confidential code or personal data (https://aiwiz.uk/blog/muse-code/; https://www.orcarouter.ai/blog/muse-api). On the API itself the default is the opposite — Standard unless you deliberately address a `-contributor` ID (https://www.orcarouter.ai/blog/muse-api).

---

## 10. Fit for our build

*Project: an AI agent on Meta's open-weight models that helps people learn and do hands-on tasks (camera + voice + step-by-step guidance). Everything below is a **recommendation** unless it says "fact:" with a citation.*

### Recommended architecture (recommendation)

| Job in the product | Recommended product | Why |
| --- | --- | --- |
| **Main reasoning / task-planning brain** | **Muse Spark Open**, hosted (Baseten / Modal / Fireworks) | Fact: it's the open-weight model the project is chartered on; 1M-token context shared across text/image/video/audio; strong Meta-reported tool-use scores (MCP-Atlas 89.2); uniform $1.25/$4.25 hosting price on exactly the three providers the user applied for credits with (§8). Self-hosting is unrealistic in a hackathon (needs ~700 GB–2 TB VRAM) — hosted is the only sane route. |
| **Hands-free voice input** | **Muse Voice Transcribe** (Meta Model API) | Fact: realtime WebSocket endpoint built for live speech; endpointing tells the agent when the user has finished a turn; diarization separates the learner from a helper/instructor; keyword biasing accepts task vocabulary (tool and part names) (§4). At $0.18/audio-hour it is effectively free at hackathon scale. |
| **"Which thing am I looking at?" grounding** | **SAM 3.1** (Meta Model API) | Fact: one text phrase ("the red wire", "the drain valve") returns boxes + pixel masks and tracks the object through video — exactly what an overlay/highlight UI needs while hands move (§5). Pair it with the reasoning model: the LLM *understands* the scene in words; SAM *localizes* the object precisely. |
| **Generated teaching visuals** | **Muse Image** (Meta Model API) | Fact: $0.01/image; edits preserve the untouched parts of a photo (ideal for annotating the *user's own* photo of their setup step-by-step), and its code tool renders exact charts/labels/diagrams (§3). Recommendation: generate a diagram per task step, or edit the user's photo to highlight the next action (after SAM finds the region). |
| **Offline / no-network fallback + cheap eval** | **Muse Glimmer**, self-hosted on a laptop | Fact: Apache 2.0, <20 GB at 4-bit, runs on one 24 GB consumer GPU or a Mac, tuned for function calling and LLM-as-a-judge (§7). Recommendation: ship it as the offline mode for workshops/field settings, and use it locally as the judge that grades the main agent's step instructions during development. |
| **Premium reasoning for the hardest sessions** | **Muse Spark 1.3** (Meta Model API, Standard) | Recommendation: if the hackathon rules allow adjunct closed models, use Spark 1.3 as an escalation tier (same $1.25/$4.25 price as hosted Spark Open, zero integration cost — same SDK shape). Fact to check first: the project brief says the project "must incorporate Meta's models" and is built on open weights — confirm whether closed API models are permitted as adjuncts before depending on this. |
| **Long-horizon tutoring memory** | **Muse Wonder** (`muse-wonder-1.0`, API) — optional | Fact: Active Memory/Active Focus are designed for agents that work over time and across conversations (§2). Recommendation: evaluate only if a session genuinely spans days; its $4/$20 price and measured token hunger make it a poor default loop model, and **Wonder Full cannot be called from code at all** (§2). |
| **Building the project itself** | **Muse Code** | Recommendation: use it as the dev-time coding agent (it defaults to Spark 1.3 and can run Wonder). Fact-based warning: **turn Contributor mode off in `/settings` first** — subscription defaults let Meta train on your code, and v1.4.6+ routes by family to Contributor models even after you pick a Standard model name (§9). |

### Architecture-shaping constraints (all facts, from the sections above)

1. **Two platforms, two keys.** Open weights (Spark Open) live on Baseten/Modal/Fireworks/OpenRouter; the perception models (Voice Transcribe, SAM 3.1, Muse Image) live on the Meta Model API. The stack needs both credentials from day one (§6, §8).
2. **Voice output is not in this lineup.** Voice Transcribe is speech-to-text only, and Meta's realtime voice/avatar models are consumer-app-only — not on the API, not downloadable (https://mungomash.com/ai/llama/versions/). Budget a third-party TTS (or on-device TTS) if the agent must speak.
3. **SAM 3.1 hosted caps shape the camera design:** ≤16 tracked objects per frame, ≤15,000 frames (~8 min @30 fps) per request, MP4/MOV only, one concept per request, and masks arrive as encoded text that needs `meta-sam-parser` to decode (§5). Design for short clips and one queried object at a time.
4. **No word-level timestamps or confidence scores from Voice Transcribe** — the UI can highlight by speaker turn, not by word, and can't grey out low-confidence words (§4).
5. **Rate limits are per team, not per key** — 3,000 RPM / 4M TPM shared across every key the team mints; minting more keys for parallel demo machines does not raise the ceiling (§6).
6. **Cost profile is dominated by the reasoning model.** Perception is nearly free ($0.18/audio-hr, $0.0025/image, $0.01/generated image). The $100 credit packs (≈$300 total across the three hosts if all are granted) go almost entirely to Spark Open tokens — cache aggressively (cached input is $0.15/M, ~8× cheaper) and keep system prompts stable so prompt caching hits (§8, §6).
7. **License posture differs per model:** Glimmer is Apache 2.0 (no strings); Spark Open is a custom license with a $20M-revenue MaaS trigger (irrelevant at hackathon scale, but the attribution rule applies); SAM 3.1 weights are under the SAM License and gated (§7, §8, §5).
