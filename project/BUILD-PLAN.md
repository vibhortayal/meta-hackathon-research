# Grocery Navigator — HACKATHON BUILD (decided by Vibhor, 2026-10-27)
Working title: Grocery Navigator. Team Nightshift, Indie track. Submission: Nov 4, 2026, 9:00 PM ET (he reviews the final package; no submission without his go-ahead).

## The product (v3, his full vision)
Camera-overlay grocery guide for stores with NO published layout data (Trader Joe's, Costco, independents). A store walkthrough video (phone or Ray-Ban Meta glasses) is indexed by Spark into zones/landmarks/items; shoppers get guided item-to-item with an overlay on the live camera view (landmark hops + camera relocalization + SAM item highlight on the shelf). Community platform: shared walkthroughs graded by recency/quality/completeness — Waze for store aisles; supply strategy = incentivized mapper-shoppers (Instacart-shopper-style partners, paid per accepted walkthrough). Personal layer: list + receipt -> what you actually bought, consumption frequency -> smart next lists -> recipe/meal-planner feed (ties to his recipe world).

## SCOPE DECISION (2026-10-27, his pick): golden thread end-to-end — one journey, depth over breadth; extra loops appear as scenes inside the thread, not separate products. Detail: SCOPE.md.

## What gets BUILT by Nov 4 (vs pitched)
BUILD: one demo store end-to-end — walkthrough ingest -> store index; list in (voice + text); guided mode (overlay, landmark hops, camera checkpoints, SAM finds the item); receipt capture -> bought-vs-list reconciliation + consumption model -> smart next list + one meal-plan suggestion; platform PROOF: two walkthroughs of the same store, system grades + picks the better map.
PITCH ONLY (demo video + roadmap): partner/incentive mapper network, multi-city platform, glasses live guidance (glasses record; phone guides — no display/API).

## Day-1 spike (the gate)
One TJ's walkthrough -> index; 10 fresh in-store photos -> Spark relocalizes department/zone. GATE: >=8/10. Pass = full build. Fail = degraded scope (zone guide + item spotting), decided same day.

## Phases (RESEQUENCED 2026-10-27, his question + Spark's recommendation: receipts first)
- D0-1: RECEIPT SPIKE on his real data — he uploads 5-6 Costco online receipts (last 2-3 months); decode every line (Costco item numbers/descriptions are cryptic: decode with confidence labels + ask-when-unsure), build consumption timeline (what / how often / how much), meal suggestions from the pattern. Prototyped by Spark-the-agent immediately; re-run on muse-spark-1.3 when the key lands (same prompts, re-measured). In parallel: his console unblock (payment method + API key -> Secure Vault).
- D1-2: personal layer productized (receipt intake, item dictionary = the item vocabulary the store index will reuse, patterns, smart list, meals).
- Store spike runs in parallel whenever he next shops a TJ's (no special trip): walkthrough + 10 photos, gate >=8/10 relocalization.
- D3-5: navigation layer on top (walkthrough ingest -> index; guided mode input = the smart list from the personal layer) + platform proof (two walkthroughs graded).
- D6-7: integration, in-store rehearsal, fixes.
- D8 (Nov 4): demo video, submission package, submit before 9pm ET on his go.

## Universal receipt intake (v7, 2026-10-27)
The intake pipeline is receipt-agnostic from day one (photo/PDF -> decode -> ledger): groceries, restaurant bills, delivery orders — one ledger with a source type. HACKATHON: the judged thread stays grocery; ONE restaurant/delivery receipt appears as a demo scene landing in the same ledger with a budget rollup line. ROADMAP (pitch): budget planning across food spend; the make-at-home bridge (often-ordered dishes -> grocery items on the next list + recipes — Our Kitchen tie-in); the trajectory grocery -> food spend -> household spend -> daily-life agent. Nutrition is OUT (owner + avoid list).

## Map data model (v4, 2026-10-27)
Store index is INCREMENTAL and personal-first: zones + item sightings with confidence, timestamps, and a coverage % per store — built from any mix of full walkthroughs, aisle photos, cart/receipt evidence, and user-taught captures of unmapped aisles. Route planning works against partial maps and lists unknowns explicitly. Community sharing = opt-in aggregation of personal maps, ranked by recency/quality/completeness (platform proof unchanged).

## Stack
muse-spark-1.3 (video indexing, relocalization, receipt reasoning — Model API, $150 credit), SAM 3.1 (shelf item grounding), Muse Voice Transcribe (hands-free list), Muse Image (not core; only if a visual asset needs it). Frontend: phone PWA. Meta models are load-bearing: no Spark video index = no map; no SAM = no shelf find.

## Reconciliation protocol (owner's design, confirmed 2026-10-27)
Three evidence streams, joined: (1) the LIST (intent), (2) the RECEIPT photo (cryptic lines + prices + quantities), (3) the CART photo (visual identity — packaging is distinctive). Price and quantity are the join keys; the cart photo disambiguates the cryptic codes, the receipt prices the cart. Design rules: confident matches post automatically; unseen/ambiguous items go to an explicit UNVERIFIED list for one-tap confirm/correct — never silently guessed; every correction feeds the personal item dictionary. Photo protocol: receipt flat + cart top-down (+ optional short pan for stacked items). Same list<->world<->record loop powers in-store verification — the receipt spike tests the product's core engine, not a side feature.

## Correction protocol (owner's design, 2026-10-27)
The map heals from being wrong — drift and AI mistakes are handled identically (to the user they're the same event):
- IN THE MOMENT (primary): at every guided stop, one-tap "Not here" (no typing, cart in hand). The disputed sighting is demoted immediately — the map stops asserting it.
- The app answers with the repair: most likely alternate zone ("also seen near frozen — check there?") + the exact fix action ("Find it? Tap Found it there, or photograph the shelf and I'll re-learn it"). The app always tells the user what to do to fix it.
- Confidence mechanics: every sighting carries confidence; it decays with age and failed checks; "Found it" refreshes it; repeat "Not here" retires it. Personal map = owner's corrections are authoritative. (Community maps later: multi-user consensus.)
- END OF TRIP (safety net): one recap screen — found / not found / taught — pre-filled from the trip; only exceptions need taps.
- Epistemics rule: every claim the map makes has a confidence and a repair path. Same DNA as receipt reconciliation: confident -> assert; contradicted -> demote + ask.

## Voice interaction (owner's design, 2026-10-27)
Voice is the PRIMARY in-store input (hands hold cart/bags/kids); taps are fallback. Meta Voice Transcribe = ears (realtime, endpointing); voice OUT = device TTS, minimal, earbud-first. Push-to-talk on the overlay (store noise + etiquette), short command grammar while walking, free-form at home.
Command set maps 1:1 onto the loops: TEACH — "the tahini is here" (voice label + camera evidence = a sighting in one gesture); CORRECT — "not here" / "it moved to the frozen aisle"; ASK — "where are the eggs in my map?"; LIST — "add oat milk"; CHECK — "got it."
Keyword biasing is loaded with the user's personal item dictionary (receipt-built), so the recognizer hears HIS vocabulary (tahini, gochujang) correctly. Restraint rule (Quiet Coach lesson): the app confirms consequential actions, stays silent otherwise.

## Build staging (owner, 2026-10-27)
Staged build after spec, API FIRST: (0) spec + API contracts; (1) API core — receipt decode, item dictionary/ledger, patterns (proven via harness on his receipts, no UI); (2) store map API — ingest, sightings, route, relocalization; (3) reconciliation API; (4) PWA client (installable, phone-first, camera overlay, voice; degrades on bad in-store connectivity); (5) UX joy pass (impeccable skill) + rehearsal. UI/UX is a PRIMARY focus per owner: "a joy, easy, intuitive" — glanceable, one-tap, voice-first, zero typing in store.

## Build methodology (owner, 2026-10-27): agent loops + token maxing
Build runs as loops, not one-shot passes: builder<->verifier loops per stage (independent verifier runs acceptance checks; failures loop back); eval loops iterate prompts against golden sets until stage gates pass (score trajectory reported); parallel candidate variants where quality is measurable; dual-judge on the riskiest calls. Every loop has a stop condition (max iterations / convergence / escalate to owner). Budget split: agent-labor tokens are abundant (500M/wk pool — spend freely per owner's standing rule); Meta API dollars are the metered $150 (Contributor mode for dev loops, Standard for final reads).

## Hosting split (DECIDED + agreed 2026-10-27)
Code + agent loops + Meta API dev calls: Hatch workspace (vault credential works only here; git/GitHub = source of truth). Runtime (API + PWA, phone-facing dev + demo): Oracle VM, pulls from GitHub; owner provisions the Model API key into Oracle's env himself once (agent cannot read back the vault key). Fallback: services run from Hatch for desk testing.

## Infrastructure (2026-10-27)
Hackathon: all on Oracle VM, $0 new infra. Caddy (auto-HTTPS, PWA statics, API proxy, single origin) -> FastAPI (Python: ffmpeg + meta-sam-parser native; DB-backed job queue, no Redis) -> Postgres (Docker) for map/ledger data; media on VM disk. Vercel + Supabase deliberately NOT in the hackathon build (split origin, function timeouts, single-user demo) — they are the platform-stage path (PWA scale-out; auth/storage/multi-user). Deploy: git pull + compose up; nightly media+DB sync to Hatch as insurance. Open owner choice: public hostname (his subdomain vs Cloudflare Tunnel) before the PWA stage.

## Returns (v8, owner 2026-10-27)
Intake must detect returns/refunds and net them against purchases before patterns compute — bought != kept. Returned items are excluded from consumption cycles and flagged do-not-suggest. Ledger shows returns as their own event type with refund amounts reconciled into spend.

## Core/enhancement split (v9, owner 2026-10-27)
CORE (critical path): Stage 1 receipt decode -> Stage 2 patterns/smart list + receipt<->cart
reconciliation (the double-check that keeps patterns verified). ENHANCEMENT (parallel-value,
not gating): Stage 3 store map/Spike 2 -> Stage 4 guided mode. Pitch leads with the
self-writing list; guidance is the "and at stores it knows, it walks with you" beat.

## PWA split (owner 2026-10-27)
PWA-core (scan, review queue, running-low home, dashboard, item/category patterns,
smart list) ships right after Stage 2 APIs — it is the product's face. Guidance UI
(camera overlay) stays with the enhancement track. Detail: PWA-CORE.md.
