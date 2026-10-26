# Prior art: live camera-and-voice assistants for hands-on tasks

2026-10-26. Do AI agents that give live assistance already exist? Yes, in general form from big companies, in research, and as a few niche products. What I could not find is a public product that follows a specific manual or expert video step by step, shows its evidence, asks when unsure, fades out, and runs on open weights. That is a search absence, not proof. Most entries below come from search summaries and secondary sources; confidence is stated.

## 1. General assistants with live video modes
| Product | What it does | Verifies or just chats | Authoritative source? | Source, date, confidence |
| --- | --- | --- | --- | --- |
| **Gemini Live** (Google) | Camera and screen sharing; answers about what the camera sees; **Guided Vision** asks you to pan, tilt or step back for a better view, built for accessibility | Conversational help; I found no step state or per-step verification | No, general knowledge | [Google blog](https://blog.google/innovation-and-ai/products/gemini-app/guided-vision-gemini-live/) and [Android Authority](https://www.androidauthority.com/gemini-live-guided-vision-launch-3718122/) via search summaries, 2026, moderate. A reviewer reportedly used Gemini Live to sort parts and build furniture ([Android Authority](https://www.androidauthority.com/gemini-live-ikea-assembly-3614666), the page returned 403 so I only saw the search summary, anecdotal) |
| **ChatGPT Advanced Voice with video** (OpenAI) | Live camera and screen sharing in voice mode; launch demo walked a person through pour-over coffee and commented on technique | Conversational feedback; no step state found | No | Launched Dec 2024 ([Android Authority via search](https://androidauthority.com/chatgpt-advanced-voice-mode-live-video-feature-beta-rollout-3500414/)); I found **no 2026 status**, low confidence for today |
| **Meta AI Live AI on Ray-Ban Meta** | Say "start live AI"; camera and microphone stay on; answers about what you see; also timers and substitutions | Conversational; reportedly does not know which recipe or step you are on | No, general knowledge | Secondary and promotional sources (Glutt blog), moderate-low; English only, US and Canada per those sources |
| **NYT Cooking on Meta glasses** | Hands-free mode with short audio steps; swipeable cards on Ray-Ban Display | **Not stated** whether it uses the camera or checks what you do | Yes, the NYT recipe | [Engadget](https://www.engadget.com/2268183/new-york-times-cooking-is-coming-to-metas-ai-and-display-glasses/), Sept 24, 2026; announced, **not yet available** ("later this fall"), moderate-high |
| **FixMode** (consumer repair app) | Live camera guidance with voice instructions for repairs | Unknown | Unknown | App Store listing only, low |

## 2. Research and prototypes (steps, errors, assembly, cooking)
| Work | What it shows | Notes |
| --- | --- | --- |
| **Pro²Assist** ([arXiv 2605.04227](https://arxiv.org/abs/2605.04227), May 2026, IMWUT'26) | Step-aware, proactive assistance from AR-glasses sensors for long procedural tasks; 90% of 20 participants found it useful; beats baselines by over 21% on action understanding | The closest academic system to our idea. Baselines not named, latency not reported in the abstract. Uses AR glasses, not a phone. |
| **EgoErrorVQA** ([arXiv 2608.24134](https://arxiv.org/abs/2608.24134), Aug 2026) | Benchmark of whether vision-language models can detect procedural errors in first-person video; reports "persistent weaknesses" in handling errors and telling error types apart | Strong warning for our mistake-catch test; model names and scores not in the abstract |
| **PREGO**, **EgoPER**, **CaptainCook4D**, **HoloAssist** | Online mistake detection, error taxonomies, cooking videos with induced errors, a 166-hour remote-instructor error dataset | From a survey summary in search, not opened; moderate-low |
| **Vinci** (IMWUT, Sept 2025) | Real-time smart assistant on portable devices with a memory module | From search summary only |
| **CNN-based furniture app** ([ADU repository](https://repository.adu.ac.ae/items/122e062a-d6e3-45f7-ae85-2945a120541f)) | Guides assembly and verifies each step by image comparison on an IKEA table and chair | Small prototype; image similarity, not a language model |
| **UW AR cooking assistant** and a **Raspberry Pi YOLO cooking-state build** | Track the recipe step from an overhead camera; the YOLO build reported 99% recall on six states in its own tests | Student reports; trained on a few dishes; not general |

## 3. Cooking appliances with cameras
**wan AIChef ultra** (Indiegogo, Sept 2026) and **Nosh** (CES 2026) use built-in cameras to identify ingredients or when food is cooked; press-release claims, not independently verified. They need the vendor's hardware and are not general guides.

## 4. What this means for the live guide / Manual Whisperer
**What already exists:** big assistants will watch through your camera and chat about it, with Google, OpenAI and Meta all shipping versions. Research systems do step-aware, proactive assistance and prototype step verification on specific tasks. A recipe publisher (NYT) is about to ship step-by-step audio on Meta glasses.

**What I could not find, and what is open for us:**
| Capability | Found in a product? | Our angle |
| --- | --- | --- |
| Follows a specific manual or expert video as the authority | Only NYT recipes (announced) and research prototypes | Manual PDF or expert video to a numbered step list with checks |
| Persistent step state ("you are on step 7") | Research (Pro²Assist); not found in the general assistants | A visible step state machine |
| **Shown evidence** (the frame behind each verdict) | Not found | Evidence frame per pass or fail |
| **Asks or waits when unsure** | Gemini's "pan or tilt" is a partial version | Explicit abstain-and-ask, with a measured abstain rate |
| **Fade-out** (fewer hints as you succeed, with a measure) | Not found anywhere | Independence measure over attempts |
| **Hindi-English** | Meta Live AI is reportedly English only (secondary source) | Hindi, English and mixed, if the day-1 test passes |
| **Open weights / user-owned data** | All the products above are cloud services | Glimmer hosted today, local path documented, user-owned logs |
| Phone only | Gemini and ChatGPT yes; Meta's needs glasses | Phone and earbuds |

**Honest differentiation:** do not sell "live camera assistance," which Google, OpenAI and Meta already offer. Sell the verifiable layer: grounded in the manual or expert, step state, shown evidence, asking when unsure, and an agent that gets out of the way as you improve. That is a thin but real gap, and a platform could ship it. NYT on Meta glasses shows publishers moving toward step-by-step grounding.

**Technical warning:** the research says models are weak at detecting procedural errors (EgoErrorVQA, Aug 2026). That makes test 2 in `spike-plan.md` (catch at least 4 of 5 mistakes, at most 1 false alarm in 5) the most likely failure. The fallback in `build-plan.md` is the right one: claim only coarse, visible things and ask when unsure.

## 5. Effect on the ranking
No score changes. Impact stays at 6 because the problem is real but the category is crowded. Demo stays high only if the evidence-and-abstain behavior is visible. The mistake-catch risk is raised, and `ranked-candidates.md` already puts the spike first.

## 6. Could not verify
- Whether Gemini Live or ChatGPT currently offer any step tracking or manual grounding: I found none, but I did not read their help pages directly.
- The Android Authority IKEA review (403): seen only through a search summary.
- Whether NYT Cooking's glasses mode uses the camera.
- Current status of ChatGPT live video in 2026, and Gemini Live tier limits.
- Model names and scores in EgoErrorVQA, and the baselines in Pro²Assist.
- arXiv IDs in the 2605 to 2609 range: they open, but I read only the abstracts.
