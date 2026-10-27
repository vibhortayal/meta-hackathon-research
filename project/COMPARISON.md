# Head-to-head: his research vs independent research — combined ranking
Compiled 2026-10-27 by Spark. Sources: fresh-eyes-ideas_md.md (10 ideas), vibhortayal/meta-hackathon-research (ranked-candidates.md et al.), IDEAS-independent.md (8 ideas generated without reading his material).

## Limits on product choice (verified across the docs)
1. Guide avoid list: medical/mental-health advice, basic RAG, simple image analyzers, simple education chatbots, job screeners, nutrition coaches, personality analyzers, SPORTS analyzers, politics/war. → kills GhostRep as framed; Manual Whisperer only survives as a verified-coach variant; SkillReceipt must avoid medical-skills framing; caregiver sits on the medical boundary.
2. No TTS anywhere in Meta's stack (Voice Transcribe is STT only; Spark Open outputs text). Speaking coaches need device/third-party TTS; Meta models listen, see, reason.
3. His hardware: no GPU, phone-only demo, 2015 MacBook. Glimmer local cannot be demonstrated — hosted only; honesty rule on the privacy story ("open weights, portable; hosted for the hackathon").
4. Platform split: VERIFIED FIRST-HAND 2026-10-27 (dev.meta.ai docs, signed-out): muse-spark-1.3 IS on the Meta Model API at the same $1.25/$4.25 card and takes audio+video+PDF — so the reasoning brain for every top idea is payable from the confirmed $150 Meta credit, no partner credit needed. Partner credits (all 3 applied, select-only) now matter only for the open-weights angle (Spark Open weights / Glimmer hosting) and Modal sandboxes/GPUs. Docs deltas vs secondary sources: Voice Transcribe turn-level timestamps only, batch cap 32MB/10min, realtime sessions cap 60 min; web-search grounding $2.50/1k queries. Rankings unchanged; feasibility of the coach family improves. Meta Model API key creation needs a payment method on file first; rate limits are per-team (3,000 RPM / 4M TPM shared). SAM 3.1 hosted: text concepts only, 1 concept/request, max 16 tracked objects/frame.
5. Clock: submissions Nov 4, 9:00 PM ET. Unspiked capabilities are the real risk budget: computer-use reliability (Paperwork Pilot), live mistake detection (all coaches), whiteboard read (Household). Specialist Distill's training run does not fit the window.

## Convergence (both researches, independently)
The "watch -> verify -> coach" engine is the shared #1 family: his live expert guide / skill-transfer coach (7.4-8.3) == independent Follow-Along (#2) and Heirloom (#1, = the coach + personal-demonstrator lens his own notes suggested to raise Impact). One runtime serves all three; only the knowledge source differs (expert film / any tutorial / a loved one's demonstration).

## Combined ranking
| # | Idea | Origin | Why here |
|---|---|---|---|
| 1 | Heirloom | independent #1 + his coach family | Personal-demonstrator lens fixes the coach's generic weakness; authentic material (his family-recipe world); batch pipeline, feasible; 4 Meta products load-bearing; most emotional demo |
| 2 | Paperwork Pilot | fresh-eyes #1 (8.3) | Hardest Meta-tooling use (computer tool + sandbox + receipts); verifiable demo; risk = computer-use reliability on camera; weaker personal pull |
| 3 | Follow-Along | independent #2 | Heirloom's engine on any tutorial; biggest everyday pain; ingestion friction (uploads, not URL scraping) |
| 4 | Paper Replicator | fresh-eyes #2 (8.2) | Frontier pick, deepest tech; demo needs a real discrepancy (luck) or a disclosed seeded error |
| 5 | Second Listen | independent #3 | Freshest lens (native audio diagnosis + re-listen verification); scope to 4-6 fault sounds |
| 6 | Bill Auditor | fresh-eyes #3 (7.6) | Safest build in the field; natural act 2 = Paperwork Pilot files the dispute |
| 7 | Household brain | repo #1 (7.1-7.2) | Best personal fit + open-weights story; weak demo payoff, whiteboard read unspiked; better December product than Nov 4 winner |
| 8 | Quiet Coach | independent #4 | Meta's own Prevention framing; highest staging/latency risk |

Parked by limits: GhostRep (avoid list), Specialist Distill (clock), DoWith (no blind testers), Table Captions (thin), Drawing Studio (low impact), Khata (mundane demo), SkillReceipt (medical framing risk), StateCheck (SAM counting risk on identical parts), Workshop QC (analyzer-label risk), Flight Recorder (dry demo).

## Recommendation
Build Heirloom. Day-1 spike: film one real family-recipe demonstration; run the step-graph extraction + one coached attempt. If attempt-vs-demo verification fails the spike, fall back to Follow-Along (same runtime, tutorial source) — no rebuild, just a different index.
