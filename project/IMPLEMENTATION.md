# Grocery Navigator — Implementation Plan

*How SPEC.md gets built with Muse Code, starting today (Oct 27). Deadline: **Nov 4, 2026, 9:00 PM ET**. Read SPEC.md first — every stage below is gated against its acceptance criteria (§9 there).*

**Three structural decisions (owner steers, 2026-10-27):**
1. **Staged build with explicit gates.** Nothing advances on vibes; each stage has measurable gate criteria and a verifier who didn't build it.
2. **API first.** Backend services are built and *proven as APIs through a test harness* before any frontend exists. The receipt spike exercises the decode API from a CLI, not a UI.
3. **Agent loops + token maxing.** The build runs as loops (builder ↔ verifier, eval loops on golden sets, parallel candidates), spending the abundant agent-labor token pool aggressively toward measured gates — never open-ended burn. Every loop has a written STOP condition.

---

## 1. Build methodology — loops, not passes

### 1.1 The three loop types

**A. Builder ↔ verifier loop (every stage).** A builder agent (Muse Code session) implements the stage's services against the contracts in §3. An *independent* verifier agent then runs the stage's acceptance checks (SPEC §9) against the harness — it does not read the builder's reasoning, only the API behavior and the evidence. Failures return to the builder as a defect list (failing check, input, expected vs actual). Loop until the gate passes or the STOP condition fires. This is the Nightshift factory pattern: nobody grades their own work.

**B. Eval loop (prompt/model behavior).** Where a stage's quality lives in a prompt (receipt decode, relocalization, indexing, command parsing), the loop is automatic: run the current prompt against the golden set → score with the stage's scorer → revise prompt (one variable at a time) → re-run. Every attempt is logged (prompt hash, set version, score) so the report shows **attempts + score trajectory**, not just the final number. The gate metric is computed on Standard mode only (see §1.3).

**C. Parallel candidate generation (where quality is measurable).** For the two riskiest prompts (decode, relocalization) and the walkthrough-indexing approach, generate 3 candidate variants up front (e.g. indexing: whole-video single pass vs zone-chunked passes vs frame-sample + stills), score all on the golden set, build on the winner. Candidates that lose are kept in the repo with their scores — the trajectory is demo-day evidence of Technical Depth.

**D. Dual-judge redundancy (riskiest calls only).** Two independent Spark calls (different prompt framings, no shared context) must agree for: (i) a receipt line auto-posting when its decode is dictionary-novel, (ii) a sighting being marked verified from a single photo. Disagreement → the item drops to the unverified/ask path. This is the epistemics rule implemented as architecture, and it directly defends the ≤2% silently-wrong gate metric.

### 1.2 STOP conditions (every loop, no exceptions)

| Trigger | Action |
|---|---|
| Gate passes | Stop immediately. Bank the win; extra polish is a new decision, not loop momentum. |
| Max iterations reached (per-loop caps in §4; default 12 prompt iterations, 3 candidate rounds, 4 builder↔verifier rounds) | Stop; escalate to owner with the trajectory + best-so-far + the blocking evidence. |
| Convergence: <1 point improvement on the gate metric across 3 consecutive iterations | Stop; the approach, not the effort, is the problem → escalate with a proposed approach change. |
| API-dollar spend for the stage exceeds its §8 allocation by >50% | Stop; escalate before spending more. |
| A loop discovers the spec is wrong (not just the code) | Stop; flag to owner; spec changes are his call. |

Token maxing means: within those rails, spend freely — parallel candidates, full golden-set runs on every iteration, verifier re-runs from scratch. The weekly agent pool (500M + 5B reserve) is the labor budget and is not the constraint; **iterations and the $150 are.**

### 1.3 The two budgets (never confuse them)

| Budget | Size | Spent on | Rule |
|---|---|---|---|
| Agent labor tokens (Muse Code / agent loops) | 500M/week + 5B reserve — abundant | Building, verifying, eval-loop reasoning | Spend freely toward gates; capped by STOP conditions, not tokens |
| Meta API dollars | **$150 credit** (10-day window) + $25 Fireworks (if granted) | The *product's own* model calls | Metered from the first call (§2.4); mode discipline below |

**Mode discipline (pricing from PRODUCTS.md):**
- **Contributor** (`muse-spark-1.3-contributor`, $0.10 in / $0.002 cached / $0.20 out) — dev-loop iterations, prompt exploration, candidate generation. **Synthetic and anonymized data only** (flag F1: Contributor may be trained on, and Meta's terms bar sending it personal data — the owner's real receipts never touch it).
- **Standard** (`muse-spark-1.3`, $1.25 / $0.15 cached / $4.25) — gate measurements, rehearsals, demo, and *all* real user data. A score only counts if it was measured on Standard.
- **Muse Code itself:** subscription seats default to Contributor mode — **turn Contributor OFF in `/settings` before any code is written** (PRODUCTS.md §9: defaults let Meta train on prompts/code/outputs, and v1.4.6+ routes by model family, so picking a Standard model name is not enough).

## 2. Foundations (Stage 0, today)

### 2.1 Repo layout

```
grocery-navigator/
  api/            # services (API-first) — one module per SPEC component
    decode/  dictionary/  ledger/  storemap/  relocalize/
    route/   guided/      reconcile/ patterns/ grading/  voice/
    meta_client.py        # the ONLY module that calls api.meta.ai / Fireworks
    cost_ledger.py        # every call logged: model, mode, tokens, $
  harness/        # CLI test harness — spikes + eval loops run here, no UI
    spike_receipts.py  spike_relocalize.py  eval_runner.py  scorers/
  prompts/        # versioned prompt files (hash-named copies per eval attempt)
  golden/         # golden sets (see §6) — data + expected outputs + scorers
  pwa/            # Stage 6 — does not exist until the APIs pass their gates
  deploy/         # Oracle VM deployment: service unit, env template, pull-from-git script
  docs/           # SPEC.md, IMPLEMENTATION.md copies + loop reports
  loops/          # per-stage loop logs: attempts, trajectories, gate verdicts
```

Git/GitHub is the source of truth for everything above. Where code *runs* is split (§2.5).

### 2.2 The meta_client contract

All Meta calls go through one module (this is what makes cost metering and mode discipline enforceable): base URL `https://api.meta.ai/v1`, `Authorization: Bearer $MODEL_API_KEY` (env var, never in code; the key lives in the Secure Vault and is injected at runtime). Endpoints wrapped:

| Job | Model ID | Endpoint | Mode |
|---|---|---|---|
| Reasoning / video / decode / relocalize / parse | `muse-spark-1.3` / `-contributor` | `POST /v1/responses` | per §1.3 |
| File upload (videos, receipt PDFs) | — | `POST /v1/files` | — |
| Shelf grounding | `sam-3.1` | `POST /v1/responses` (model=`sam-3.1`; masks decoded via `meta-sam-parser`) | n/a |
| Voice (live) | `muse-voice-transcribe-1.0` | `wss://api.meta.ai/v1/asr/realtime` | n/a |
| Voice (batch/file) | `muse-voice-transcribe-1.0` | `POST /v1/asr/transcribe` | n/a |
| Dinner render | `muse-image-1.0` | `POST /v1/images/generations` | n/a |
| Pre-filter | Glimmer (`meta-ai/muse-glimmer-30b` via Fireworks) | Fireworks chat endpoint | n/a (separate credit) |

Watch-outs baked into the client: Spark emits a non-standard SSE event that trips some OpenAI-compatible streaming clients (PRODUCTS.md §1) — parse defensively, prefer non-streaming for harness calls. SAM accepts **text prompts only, one concept per request**, ≤16 tracked objects/frame, ≤15,000 frames/request, MP4/MOV only (no WebM — phone recordings must be transcoded if captured as WebM). Rate ceilings are per-team (3,000 RPM Standard / 150 RPM Contributor) — eval loops throttle to the Contributor ceiling when in Contributor mode.

### 2.3 Prompt caching discipline

System prompts, the item dictionary, and the store index are large, stable prefixes — structure every call as [stable prefix][variable tail] so cached-input pricing ($0.15/M Standard) hits. The store index is passed as cached context for relocalization/route calls, never re-serialized differently between calls (cache keys are exact-prefix).

### 2.4 Cost ledger

`cost_ledger.py` appends one row per API call {ts, service, model, mode, in_tokens, cached_tokens, out_tokens, est_$} and renders a running total vs the §8 allocations. Stage gates include "spend within allocation." Demo day has its own line (§7).

### 2.5 Hosting split (DECIDED with owner, 2026-10-27)

| | Hatch workspace (Spark's) | Oracle VM (owner's) |
|---|---|---|
| What runs there | All code authoring, agent loops (§1), the harness, spikes, evals — **all development Meta API calls** | The deployed runtime: `api/` service + PWA, for phone testing and demo day |
| Source of truth | git working copy | `git pull` from GitHub (via `deploy/`) — never hand-edited |
| Meta API key | The Secure Vault credential — **usable only from Hatch** (surrogate exchange). Harnesses therefore call the Meta API from Hatch, by design. | **Owner provisions the Model API key into the Oracle environment himself, once** (see runbook §7 — the agent cannot read back or move the vault key; this step cannot be delegated) |
| Why | Loops need the vault key + fast iteration; the key's constraint makes Hatch the only possible dev-call site | Durable, publicly reachable, HTTPS — which `getUserMedia` camera access requires |

**Fallback:** the same `api/` service also runs from the Hatch workspace for desk testing if Oracle hiccups (§7). The harness never depends on Oracle; the phone never depends on Hatch.

### 2.6 Runtime stack — deliberately minimal, all on the Oracle VM, $0 new infra

Owner's Always-Free constraint: no new cloud resources, nothing that can incur charges.

| Layer | Choice | Why |
|---|---|---|
| Edge / TLS | **Caddy** on the VM | Automatic HTTPS; serves PWA statics and reverse-proxies the API under **one origin** — camera APIs (`getUserMedia`) require a secure context, and single-origin kills CORS friction |
| API | **Python FastAPI** | The media pipeline is Python-native: Meta's `meta-sam-parser`, ffmpeg frame work, the harness language. One language end to end |
| Background jobs | **DB-backed job queue** (a Postgres table + worker loop) | Walkthrough indexing is a long job; no Redis, no extra moving parts |
| Data | **Postgres in Docker** on the VM | Sightings/index are relational + JSONB (schemas in §3 map directly); Docker keeps the VM clean and the deploy reproducible |
| Media | **VM disk** | Walkthrough videos/photos are far too big for hosted free tiers; derived frames and indexes live in the DB, originals on disk |
| Deploy | `git pull` + `docker compose up` on the VM | Matches §2.5: GitHub is the source of truth; the VM never hand-edits |
| Insurance | **Nightly sync of media + DB dump back to Hatch** | If the VM dies demo week, the data and a Hatch-run service (§7 fallback) survive |

**Explicitly NOT used for the hackathon:** Vercel (split origin/CORS friction; functions can't run long indexing jobs — it is the scale-out path for the PWA later) and Supabase (single-user demo; VM Postgres replaces it — it becomes the platform-stage answer for auth/storage/multi-user, and it's the owner's known stack). Naming them here is deliberate: choosing *against* familiar tools for stated reasons is part of the engineering story.

**Open owner choice — public hostname:** a subdomain of a domain the owner controls pointed at the VM, *or* a Cloudflare Tunnel hostname. Needed before the PWA stage (Stage 6); flagged again in the runbook (§7). Caddy works with either; the tunnel avoids opening inbound ports.

## 3. Contracts (JSON schemas — the API-first backbone)

These are the interfaces every stage builds against; the harness tests them before any UI exists. (Abbreviated field lists; the repo carries full JSON Schema files.)

```jsonc
// DecodedReceipt — output of decode service (SPEC FR-1.2)
{ "receipt_id": "uuid", "source_type": "grocery|restaurant|delivery",
  "merchant": "Costco", "purchased_at": "ISO-8601",
  "lines": [ { "raw": "KS ORG MLK 1GAL", "sku": "100123",
               "item_id": "dict:milk-whole-1gal|null",
               "decoded_name": "Kirkland Signature Organic Whole Milk 1gal",
               "qty": 1, "unit_price": 4.29, "line_total": 4.29,
               "confidence": 0.93, "status": "auto|unverified",
               "judge_agree": true } ],
  "subtotal": 0.0, "tax": 0.0, "total": 0.0,
  "totals_reconcile": true, "image_ref": "file_id" }

// DictionaryEntry (SPEC FR-2.1)
{ "item_id": "dict:milk-whole-1gal", "canonical_name": "Whole milk, 1 gal",
  "category": "dairy", "aliases": ["KS ORG MLK", "organic milk"],
  "spoken_names": ["milk"], "sam_concept": "milk gallon jug",
  "typical_unit": "1 gal" }

// Sighting & StoreIndex (SPEC FR-3.x)
{ "sighting_id": "uuid", "store_id": "...", "zone_id": "frozen-back-wall",
  "item_id": "dict:...", "evidence": "walkthrough_frame|aisle_photo|cart_photo|user_taught|receipt_only",
  "captured_at": "ISO-8601", "base_confidence": 0.9,
  "status": "live|disputed|retired", "source_ref": "file_id|trip_id" }
// effective_confidence computed at read time: base * 0.5^(age_days/21), per FR-3.2
{ "store_index": { "store_id": "...", "version": 7,
    "zones": [ {"zone_id": "...", "label": "Frozen — back wall",
                "landmarks": ["glass freezer doors", "red signage"], "order": 40} ],
    "sightings": ["<Sighting>"], "coverage_pct": 62, "item_coverage_pct": 71 } }

// RoutePlan (SPEC FR-4.1)
{ "route_id": "uuid", "store_id": "...", "index_version": 7,
  "stops": [ {"item_id": "dict:...", "zone_id": "...",
              "confidence": 0.81, "evidence_age_days": 3} ],
  "unknowns": [ {"item_id": "dict:tahini", "ask": "If you find it, show me the aisle"} ] }

// RelocalizationResult (SPEC FR-5.1)
{ "zone_id": "frozen-back-wall|null", "confidence": 0.0,
  "landmarks_seen": ["..."], "needs": "none|another_pan|landmark_photo" }

// ReconciliationResult (SPEC FR-1/6.5 — list <-> receipt <-> cart)
{ "trip_id": "uuid",
  "matched":   [ {"item_id": "...", "evidence": ["list","receipt","cart"], "price": 0.0} ],
  "unverified":[ {"item_id": "...", "seen_in": ["receipt"], "reason": "not visible in cart photo"} ],
  "surprises": [ {"raw": "...", "reason": "on receipt, not on list, not in cart"} ] }

// PatternSummary & SmartList (SPEC FR-9/10) — computed, not generated
{ "item_id": "dict:...", "count": 6, "median_interval_days": 9,
  "last_bought": "ISO", "typical_qty": 2, "due": true }

// WalkthroughGrade (SPEC FR-12.1)
{ "walkthrough_id": "...", "recency_days": 2, "clarity": 0.0,
  "completeness_zones": 0.0, "completeness_items": 0.0, "overall": 0.0,
  "wins_over_index_version": 6 }
```

---

## 4. Stages (each: build → loop → gate; no stage starts before the prior gate, except where noted)

### Stage 0 — Foundations (D0, today)
- **Build:** repo + layout (§2.1); `meta_client` with cost ledger; one smoke call per service (Spark text, SAM on a sample photo, ASR batch on a 10-second clip, Muse Image one render, Glimmer ping if the Fireworks credit exists); Muse Code Contributor mode **OFF** in `/settings` (§1.3); Oracle skeleton: Caddy + FastAPI + Postgres via docker compose, `/health` green over HTTPS.
- **Owner steps (cannot be delegated):** (a) decide the public hostname (§2.6) — needed by Stage 6, earlier is better; (b) provision the Model API key into the Oracle env — needed by Stage 6 rehearsal (the vault key works only from Hatch; the agent cannot move it).
- **Loops:** builder ↔ verifier, expect 1–2 rounds. No eval loop (nothing to score yet).
- **Gate:** smoke calls green from the Hatch harness *and* from the Oracle service; cost ledger renders a total; `docker compose up` from a clean pull reproduces the stack.
- **Est. API $:** ~1.

### Stage 1 — Receipt decode API + SPIKE 1 (D0–1) — *the first spike, harness only, no UI*
- **Build:** `decode/` (photo/PDF → `DecodedReceipt`), arithmetic self-check (FR-1.4), `dictionary/` v1 seeded from decodes + corrections, `ledger/` append-only posting with unverified queue; `harness/spike_receipts.py` drives everything from the CLI.
- **Data:** the owner's 5–6 real Costco receipts (Standard mode only — F1) become the *gate set*; 12 synthetic Costco-format receipts (fabricated, incl. edge cases: refund lines, duplicates, blurry photo) are the *iteration set* for Contributor-mode loops.
- **Loops:** (C) 3 decode-prompt candidates scored on the synthetic set → winner; (B) eval loop on the winner, ≤12 iterations, one variable at a time; (D) dual-judge on dictionary-novel auto-posts. Score trajectory logged per attempt.
- **Gate (SPEC §9, Spike 1, measured on Standard against the real set):** ≥95% lines captured; ≥85% auto-posted and correct; ≤2% silently wrong; totals reconcile ≤$0.05 on ≥5/6 receipts; after a corrections pass, re-decode asks about 0 previously-corrected codes.
- **Est. API $:** ~5 (≈2 Contributor iterations + ≈3 Standard gate runs).

### Stage 2 — Patterns, smart list, meal hook APIs (D1–2)
- **Build:** `patterns/` — deterministic aggregations over the ledger (FR-9.1; SQL, not an LLM); `smart list` due-rule (FR-10.1) + Spark narration constrained to the computed due-set; `meal hook` suggestion from ledger-supported ingredients only (FR-11.1) + missing-items → list (FR-11.2); budget rollup endpoint (FR-2.4).
- **Loops:** builder ↔ verifier (arithmetic checked 100% against hand-computed values on the golden ledger); small eval loop (≤6 iterations) on the meal prompt with the single metric *invented ingredients = 0*.
- **Gate:** SPEC §9 rows for Patterns / Smart list / Meal hook.
- **Est. API $:** ~2.

### Stage 3 — Store map, walkthrough indexing + SPIKE 2 (D2–4; starts the day TJ's footage lands)
- **Build:** ingest pipeline — video upload (`POST /v1/files`), DB-backed indexing job (§2.6), Spark video → zone skeleton + sightings (FR-3.4); `storemap/` versioned StoreIndex + coverage computation (FR-3.2/3.3); aisle-photo ingest (FR-3.5); `relocalize/` service (photo/pan frames + cached index prefix → `RelocalizationResult`).
- **First action is a probe, not a build (F5):** index a 2-minute clip three ways and measure tokens/latency/$ per approach before committing — video tokenization is unpublished in our sources and is the budget's swing factor.
- **Loops:** (C) 3 indexing candidates from the probe, scored on walkthrough #1 (zones found, sightings for the owner's regular TJ's items, $/video); (B) relocalization eval loop ≤10 iterations against the golden photo set (10 fresh in-store photos + 5 negatives that must *not* produce a confident zone).
- **Gate (SPEC §9, Spike 2):** ≥8/10 fresh photos relocalized to the correct zone, ≤6 s p95, negatives handled honestly. **Fail → degraded scope (zone guide + item spotting), decided the same day** — Stages 4–7 proceed against the degraded contract, and the demo script is rewritten that evening, not on Nov 4.
- **Est. API $:** ~20 (the swing stage; STOP rule at +50% per §1.2).

### Stage 4 — Route, guided session, reconciliation APIs (D3–5)
- **Build:** `route/` planner (computed ordering over the zone skeleton; Spark narrates exceptions only; unknowns explicit per FR-4.1); `guided/` session state machine (SPEC §6.5 states) as a service the PWA drives; correction endpoints implementing FR-3.2/8.x semantics; `reconcile/` — the three-way join (list ↔ receipt ↔ cart photo) reusing `decode/` for both photos, price + quantity as join keys, output `ReconciliationResult`.
- **Loops:** builder ↔ verifier against **simulated trips** in the harness (scripted checkpoint/correction sequences — no store visit needed); reconciliation eval loop on 3 synthetic trips + the Stage 1 golden receipts paired with cart photos.
- **Gate:** SPEC §9 rows for Route / Guided / Correction / Reconciliation; a simulated trip containing a "not here" and a teach event completes with zero dead ends and a correct recap.
- **Est. API $:** ~3.

### Stage 5 — Voice APIs (D4–5; may run parallel to Stage 4)
- **Build:** ASR realtime WebSocket proxy in the API service (`muse-voice-transcribe-1.0`), dictionary loaded as keyword biasing; `voice/` command parser — Spark turns transcript → {intent, slots, interpretation confidence} (FR-7.2; ASR itself returns no confidence — F4); confirm-prompt policy (consequential or low-confidence only).
- **Loops:** eval loop ≤8 iterations on the recorded command set (~40 commands in the owner's voice, clean + store-noise mixes); metric = intent accuracy + zero unconfirmed consequential actions.
- **Gate:** ≥90% intent accuracy; 0 consequential actions on low-confidence parses without confirmation (SPEC §9).
- **Est. API $:** ~1 (ASR is $0.18/audio-hour; the whole test set is minutes of audio — parse calls dominate).

### Stage 6 — PWA + UX (D5–7) — *starts only when Stages 1–5 APIs have passed their gates*
- **Build:** the PWA (SPEC §8): installable, single-origin behind Caddy on Oracle, `getUserMedia` camera, Wake Lock in guided mode, offline cache of shell + active StoreIndex + list + RoutePlan, local queue for sightings/corrections/check-offs with sync (§7.4 of SPEC — corrections apply locally *immediately*). **The UI pass follows the impeccable skill playbook**, worked against SPEC §3's UX principles as a checklist, not a vibe: every principle becomes checkable items (e.g. "every in-store action = 1 tap on a ≥64px target," "zero text inputs anywhere in the trip flow," "coverage % visible on the store home," "current target readable at arm's length").
- **Owner step (blocking):** Model API key provisioned into the Oracle env (§2.5) + hostname live (§2.6) — rehearsal #1 runs on the real deployment or it doesn't count.
- **Loops:** builder ↔ verifier against the UX checklist (100% or it doesn't pass); then **in-store rehearsal #1** at the TJ's — full golden thread on the owner's phone over the Oracle deployment — whose defects feed one fix loop (≤4 rounds, then escalate).
- **Gate:** UX checklist 100%; rehearsal trip completes end to end (route → guided → a correction → reconcile) on the deployed stack.
- **Est. API $:** ~4 (rehearsal trips at ≈$0.25 each + defect-loop re-runs).

### Stage 7 — Platform proof, hardening, demo (D6 – Nov 4)
- **Build:** `grading/` (second walkthrough ingested + graded vs the first, FR-12.1 — the platform proof scene); dinner-render scene (Muse Image, FR-11.3); delivery-receipt scene (one real delivery receipt through the same intake → ledger + rollup, FR-2.4); Glimmer pre-filter behind its flag (FR-13.1) — **first thing cut if the schedule squeezes**; demo script + shot list keyed to the golden thread.
- **Loops:** full-thread dry runs ×3 (one against Hatch-run services as a desk test of the §7 fallback, two against Oracle); each dry run is a verifier pass against the demo script, defects loop back (≤3 rounds).
- **Gate:** two consecutive green dry runs on the Oracle deployment; runbook (§7) rehearsed; submission package assembled for the owner's review.
- **Est. API $:** ~8 (dry runs, video takes, re-takes).

**Build order in one line:** Stage 0 foundations → **Stage 1 receipt spike** → Stage 2 patterns/list/meal → Stage 3 store map + relocalization spike → Stage 4 route/guided/reconcile → Stage 5 voice → Stage 6 PWA/UX + rehearsal → Stage 7 grading proof + hardening + demo.

## 5. Dev-loop workflow (how a single day actually runs)

1. Pick the stage's next unpassed gate check. The builder agent gets: the SPEC section, the §3 contract, the failing checks (or the golden set), and the STOP conditions — nothing else it doesn't need.
2. Builder implements in a worktree/branch; commits are small and gate-scoped.
3. Verifier agent (fresh context) runs the harness checks from a clean checkout and files defects as {check, input, expected, actual, evidence}. It never edits code.
4. Prompt work runs through `eval_runner`: every attempt writes `loops/<stage>/<loop>-<n>.md` — prompt hash, set version, per-item scores, gate metric, $ spent, and the one variable changed. Trajectories are reported to the owner at stage gates, not narrated mid-loop.
5. Merges happen only on verifier pass. The cost ledger is checked at every gate; a stage over its §8 allocation by >50% stops and escalates (§1.2).
6. Nightly: Oracle media + DB sync back to Hatch (§2.6 insurance) — scripted from Stage 0, not remembered.

## 6. Test strategy & golden sets

Golden sets are versioned, scored by code (not by an agent's impression), and re-run in full after *any* prompt or contract change (regression rule).

| Set | Contents | Used by |
|---|---|---|
| `golden/receipts-real` | Owner's 5–6 real Costco receipts + hand-verified decodes. **Standard mode only; access-controlled** (F1) | Stage 1 gate |
| `golden/receipts-synthetic` | 12 fabricated Costco-format receipts + expected decodes; edge cases: refund/negative lines, duplicate receipt, tax-exempt items, blurry-photo variant, a TJ's receipt for format range | Stage 1 iteration loops (Contributor-safe) |
| `golden/relocalize` | 10 fresh TJ's photos (never in any walkthrough) with zone labels + 5 negatives (wrong store, parking lot, home kitchen) that must return low confidence / `needs`, never a guessed zone | Stage 3 gate |
| `golden/shelf` | 10 shelf photos with hand-labeled target boxes | Stage 4/6 SAM IoU checks |
| `golden/voice` | ~40 recorded commands (owner's voice), clean + store-noise mixes, with expected {intent, slots} | Stage 5 gate |
| `golden/trips` | Scripted simulated trips (checkpoint sequences, a "not here," a teach, a skip) with expected state transitions + recap | Stage 4 gate |
| `golden/ledger` | The Stage 1 output frozen as data; hand-computed pattern values | Stage 2 gate |

**In-store rehearsal checklist** (Stages 6–7, run at the actual TJ's): airplane-mode mid-trip (offline queue + local correction must hold); hotspot-only connectivity; bright-aisle glare readability; one-hand operation with a cart; teach-a-sighting in <10 s; "not here" → repair prompt flow; end-to-end trip timing; battery drain over a full trip; PWA install + Wake Lock behavior on the owner's actual phone.

## 7. Demo-day runbook (Nov 4) — outline

**T-1 (Nov 3):** prompt/index freeze (only defect fixes after this); final dry run on Oracle; nightly sync to Hatch verified restorable; devices charged; demo video shot list printed; submission form fields pre-checked in the portal (Representative = owner; Indie track; team members named).

**Owner-only steps (cannot be delegated — the agent cannot read back or move the vault key):**
1. Model API key provisioned into the Oracle environment (once; ideally Stage 6, verified by the Oracle `/health` + one authenticated smoke call).
2. Public hostname confirmed live (his §2.6 pick).
3. Final submission: he reviews the complete package and gives the explicit go before anything is submitted (standing rule).

**Live vs pre-computed:**

| Live in the demo | Pre-computed (real data, computed earlier — the honest kind) |
|---|---|
| Guided trip: route, checkpoints, SAM finds, voice teach/correct | Store index — from walkthroughs filmed during the week (indexing is a background job by design, FR-3.4) |
| That trip's real receipt + cart reconciliation | Pattern history — from the owner's real 5–6 receipts, decoded in Stage 1 (re-decodable live if the segment runs long) |
| Smart list regeneration, meal suggestion, grading of walkthrough #2 | Dinner render may be pre-rendered if network is poor (it's $0.01 and 1 call — try live first) |

**Fallbacks, in order:** (1) in-store network dies → SPEC §7.4 degradation (cached route, local corrections, manual check-off) — rehearsed, not improvised; (2) Oracle hiccups → the same `api/` service runs from the Hatch workspace for desk-side segments while the VM is restored from the nightly sync; (3) live guidance wobbles → the pre-shot demo video + stage artifacts (map, routed list, reconciliation table) carry the segment, per the SCOPE risk plan. **Submit before 9:00 PM ET** — target 6:00 PM, buffer is for the portal, not for building.

## 8. Cost rollup — Meta API dollars (the metered budget)

Per-stage allocations (§4) against the **$150 credit**:

| Stage | Est. $ | Main driver |
|---|---|---|
| 0 Foundations | 1 | Smoke calls |
| 1 Receipt spike | 5 | Contributor iterations + Standard gate runs |
| 2 Patterns/list/meal | 2 | Small text calls; meal-prompt loop |
| 3 Store map + relocalization | 20 | Walkthrough indexing experiments (F5 swing factor) |
| 4 Route/guided/reconcile | 3 | Simulated trips |
| 5 Voice | 1 | Parse calls (ASR ≈ free at this scale) |
| 6 PWA + rehearsals | 4 | ≈$0.25 per rehearsal trip + fix loops |
| 7 Proof + demo | 8 | Dry runs, video takes |
| **Subtotal** | **44** | |
| Contingency (~30%) | ~13 | Re-indexing, extra takes |
| **Expected total** | **≈ $57** | **Ceiling $150**, enforced by the §1.2 STOP rule |

Per-trip run cost on Standard ≈ **$0.25** (SPEC §7.2 target ≤$0.35): ~6 relocalization checkpoints, ~10 SAM stills ($0.0025 each), ~5 min PTT audio ($0.015), one receipt decode (~$0.01–0.02), pattern/list calls (~$0.02) — indexing amortized separately. Glimmer spend, if any, rides the separate $25 Fireworks credit and is **not** counted against the $150 (F7). Agent-labor tokens are not in this table: they're the abundant pool (§1.3), spent per the loop caps in §4, reported as attempt counts + trajectories in `loops/`.

## 9. Design flags — what doesn't build as naively designed, and the smallest fix

- **F1 — Contributor mode × personal data.** Contributor models may be trained on by Meta, and Meta's terms bar sending them confidential/personal data. The owner's real receipts are personal data. **Fix (already reflected above):** Contributor loops run *only* on synthetic/anonymized sets; real receipts are Standard-only, in dev, rehearsal, and demo. Same rule for Muse Code itself: Contributor OFF in `/settings` before coding (subscription default trains on code).
- **F2 — SAM over full walkthrough video.** Hosted SAM caps at 15,000 frames/request and charges $0.20/1K frames *per concept, one concept per request*: a 10-min 30 fps walkthrough is 18,000 frames (over cap) and a single concept pass ≈ $3.60 — dozens of items would eat the credit and still not finish. **Fix (in SPEC FR-3.4):** Spark indexes the video; SAM runs only on stills and short clips where shelf grounding is needed ($0.0025/image).
- **F3 — Spark latency in the aisle.** Spark is a reasoning model; a third-party measurement showed ~9 s for a trivial reply at default effort. The 6 s relocalization budget fails at default settings. **Fix:** in-store calls use low `reasoning_effort`, minimal prompts, cached index/dictionary prefixes; checkpoints are async and non-blocking (FR-5.3); degraded mode (zone guide + item spotting) is pre-decided if Spike 2 fails on latency.
- **F4 — Voice Transcribe returns no confidence scores** (and turn-level timestamps only). Voice "ask when unsure" cannot key off the ASR. **Fix (in FR-7.2):** confidence lives in Spark's parse layer (intent + slots + interpretation confidence); no word-level highlighting is promised anywhere.
- **F5 — Spark video tokenization is unpublished** in our sources, so walkthrough-indexing cost/latency is the budget's swing factor. **Fix:** Stage 3 opens with a 2-minute-clip probe across 3 indexing approaches, measured before committing; indexing chunks by zone; Stage 3 carries the largest allocation + the +50% STOP rule.
- **F6 — PWA platform limits.** iOS requires HTTPS + a user-gesture context for camera, offers no background camera, and Wake Lock support varies. **Fix:** single-origin HTTPS via Caddy on Oracle (§2.6); guided mode is a foreground camera UI by design (nothing needs background capture); Wake Lock requested on trip start with the camera screen itself as the stay-awake fallback.
- **F7 — Glimmer's Fireworks price and credit are unverified.** PRODUCTS.md confirms Glimmer is hosted on Fireworks but publishes no per-token price; the $25 Fireworks credit is select-participants-only and may not be granted. **Fix:** Glimmer is flag-isolated and every gate must pass with it off (FR-13.1); verify price at the console before enabling; dropping it costs an optimization and a showcase beat, never a gate.
- **F8 — Two smaller unknowns, designed around:** Spark *audio* input is listed by one catalog and not others — the design never routes audio to Spark (ASR is the only audio path). Contributor rate limit is quoted as 150 RPM by one source, 100 by another — eval loops throttle to 100 RPM in Contributor mode to be safe.
