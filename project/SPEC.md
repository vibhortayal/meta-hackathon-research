# Grocery Navigator — Product Spec

*Working title. Team Nightshift (Vibhor, solo dev + AI agents), Indie track, Meta Global AI Developer Hackathon. Submission deadline: **Nov 4, 2026, 9:00 PM ET**. This spec is the contract the build stages in IMPLEMENTATION.md are gated against.*

---

## 1. Vision

Google Maps never made it inside the grocery store. Target and Walmart shoppers get aisle directions because those retailers publish planogram data; Trader Joe's, Costco, and independent stores publish nothing — Costco's sign-free maze is a deliberate business choice — so no app can guide you there. Separately, the one perfect record of what a household actually buys — the receipt — is thrown away, so every shopping list starts from zero and nobody knows their own consumption pattern.

Grocery Navigator builds the store map from shoppers' own captures and closes the loop between the map and the receipt:

1. **LEARN your store, trip by trip** — a personal, incremental map (robovac-style), built from walkthrough video, aisle photos, cart/receipt evidence, and user-taught captures.
2. **GUIDE every trip** — the list becomes a route; a camera overlay walks the shopper zone to zone, relocalizes from what the camera sees, and spots each item on the shelf.
3. **RECONCILE at checkout** — receipt photo + cart photo + list are joined; what was paid for is verified against evidence, never guessed.
4. **LEARN always** — receipts become a consumption model; the next list writes itself and tonight's dinner suggests itself from what's actually in the kitchen.

**Epistemics rule (applies to every component):** every claim the system makes carries a confidence and a repair path. Confident → assert. Unsure → ask. Contradicted → demote and ask. Nothing is silently guessed, and nothing wrong stays asserted.

**Why Meta, why now:** Muse Spark 1.3's native video understanding turns a raw walkthrough into a store index (impossible before it — this is why the product doesn't exist); SAM 3.1 grounds items on real shelves; Muse Voice Transcribe takes lists and corrections hands-free, biased by the user's own item vocabulary. No retailer partnership, no beacons, no planogram feed.

## 2. The golden thread (what the demo must prove, end to end)

One continuous journey on the owner's real data and one real store:

> Costco receipts (5–6, last 2–3 months) decode into a ledger → patterns produce a smart list → at Trader Joe's, the personal map (built from his captures) routes that list → guided trip with overlay, relocalization, SAM finds, and a voice "not here" correction that heals the map → checkout reconciliation (list ↔ receipt ↔ cart) → the trip's receipt updates the patterns → one meal suggestion feeds the next list. Inside the thread, three thin proof scenes: a second walkthrough is graded against the first (platform proof), a dinner render from actual ingredients (Muse Image), and a delivery receipt landing in the same ledger (universal intake).

Every stage of the thread emits a visible artifact (map + coverage %, routed list, overlay find, reconciliation table, pattern page) so the demo survives a wobbly live moment.

## 3. UX principles — "a joy: easy, intuitive" (owner's words; these are requirements, not aspirations)

The UI/UX is a primary focus of this product, equal to the AI pipeline.

1. **Glanceable in-store.** Every in-store screen is readable in ≤2 seconds at arm's length, in store lighting, while moving: one message per screen, huge type for the current target, no paragraphs.
2. **One-tap everything.** Any in-store action (found it, not here, got it, skip) is a single tap on a target ≥64px. The user's other hand holds a cart, a bag, or a child.
3. **Voice-first in the store.** Teaching, correcting, asking, adding, and checking off are all voice commands (§6.7). Taps are the fallback, never the requirement.
4. **Zero typing in the store.** No text field is ever required between the entrance and checkout. Lists are built by voice, by patterns, or at home.
5. **The map's learning is visible and delightful.** Coverage % per store, "new zone learned," "you taught me 12 things at this store" — the robovac moment. The user should *feel* the map getting smarter and enjoy teaching it.
6. **Restraint.** The app confirms consequential actions and stays silent otherwise (the Quiet Coach lesson). No nagging, no notification spam, no prompts that don't change a decision. In guided mode it speaks only at checkpoints, finds, and contradictions.
7. **Honesty as UI.** Unknowns are shown as unknowns ("not in my map yet — if you find it, show me"), low-confidence sightings are labeled "last seen," never dressed up as facts.
8. **At-home depth, in-store shallowness.** Home screens (patterns, ledger, meals) can be rich and browsable. In-store screens are stripped to the current mission.

## 4. Users and user stories

**Primary user:** the owner himself (authentic first-person data: his Costco history, his Trader Joe's). **Wedge users:** shoppers at no-data stores; travelers in an unfamiliar store someone else mapped.

| # | Story |
|---|---|
| US-1 | As a shopper, I upload past receipts (photo/PDF) and get a decoded ledger where I'm only asked about lines the system can't resolve, so my purchase history builds itself without data entry. |
| US-2 | As a shopper, I see what I buy, how often, and in what quantity, so I understand my own patterns. |
| US-3 | As a shopper, the app drafts my next list from my patterns (what's due), and I adjust it by voice or tap — never by typing in the store. |
| US-4 | As a shopper arriving at my store, I get a route through my personal map that groups my list by zone and honestly lists what the map doesn't know yet. |
| US-5 | As a shopper mid-trip, the overlay shows me the current zone target; when I pan my camera, the app confirms where I am (relocalization checkpoint) and points me onward. |
| US-6 | As a shopper at the shelf, the app highlights my item in my camera view (SAM) so I grab the right thing the first time. |
| US-7 | As a shopper, when the app is wrong ("not here"), I correct it in one tap or one sentence, it stops asserting the wrong location immediately, and it tells me exactly what to do so it's right next time. |
| US-8 | As a shopper who found an unmapped item, the app asks me to show it the aisle (photo or short clip), learns the sighting, and thanks me — teaching takes under 10 seconds. |
| US-9 | As a shopper at checkout, I photograph the receipt and the cart; the app reconciles them against my list and only bothers me about the handful it can't verify. |
| US-10 | As a home cook, I get one dinner suggestion built from ingredients my receipts prove I have, and its missing items can join the next list in one tap. |
| US-11 | As a food spender, I can drop a restaurant/delivery receipt into the same intake and see it in the same ledger with a budget rollup (demo scene; depth is roadmap). |
| US-12 | As a mapper, I can submit a second walkthrough of a store and see it graded against the existing map source (recency, clarity, completeness), and the better one wins. |

## 5. System overview

**Clients:** phone PWA (installable; §8). **Services (API-first, built and proven before the client):** Receipt Decode, Item Dictionary & Ledger, Store Map & Sightings, Relocalization, Route Planning, Guided Session, Reconciliation, Patterns, Walkthrough Grading. **Models:** `muse-spark-1.3` (Meta Model API) as the reasoning/video core; `sam-3.1` for shelf grounding; `muse-voice-transcribe-1.0` for voice in; `muse-image-1.0` for the dinner render; Muse Glimmer (hosted on Fireworks) as a cheap sighting pre-filter and open-weights showcase — isolated behind a flag, never load-bearing. **Voice out:** device TTS only (no TTS exists in Meta's stack), minimal and earbud-first.

## 6. Functional requirements

### 6.1 Receipt intake & decoding (C1)

- FR-1.1 Accept receipt input as photo (camera/upload), PDF, or screenshot; sources: grocery, restaurant, delivery (source type tagged at intake; grocery is the judged thread).
- FR-1.2 Decode each receipt into a `DecodedReceipt` (schema in IMPLEMENTATION.md §3): merchant, date/time, line items {raw text, SKU/item number when present, decoded product, quantity, unit price, line total, line confidence}, subtotal, tax, total, totals confidence.
- FR-1.3 Cryptic lines (Costco item numbers, abbreviations like "KS ORG MLK") are decoded against (a) the personal item dictionary first, (b) model knowledge + optional web-search grounding second. Every line gets a confidence; lines below the auto-post threshold (0.85) go to the **unverified queue** — the user confirms or corrects in one tap per line. Nothing below threshold is ever silently posted to the ledger.
- FR-1.4 Arithmetic self-check: sum of line totals must reconcile to the receipt total within $0.05 after tax handling. Failure raises decode confidence penalty and flags the receipt for review — a decoded receipt that doesn't add up is never presented as fact.
- FR-1.5 Corrections feed the item dictionary immediately (FR-2.3): the same code/abbreviation never asks twice.
- FR-1.6 Duplicate detection: same merchant + date + total → warn, don't double-post.

### 6.2 Item dictionary & ledger (C2)

- FR-2.1 The dictionary maps every surface form of a product (receipt code, abbreviation, brand name, user's spoken name) to one canonical item {canonical name, category, typical unit/size, aliases[]}. The dictionary is the shared vocabulary for decoding, voice biasing, and the store index — all three read the same table.
- FR-2.2 The ledger is append-only: every posted line from every receipt, with source receipt, timestamp, price, and store. Corrections amend via superseding entries, never silent edits.
- FR-2.3 User corrections (decode confirmations, reconciliation fixes, voice teaching) write dictionary aliases and preferred names.
- FR-2.4 The ledger is receipt-agnostic: grocery, restaurant, and delivery entries coexist with a `source_type`; a budget rollup (per period: grocery / dining / delivery totals) is computable from the ledger alone.

### 6.3 Store map (C3)

Data model (full JSON schemas in IMPLEMENTATION.md §3):

- **Store** {id, name, chain, address, created from}. One store is fully built for the demo (Trader Joe's); the model supports many.
- **Zone** {id, store_id, label ("produce", "frozen, back wall"), description, landmarks[], skeleton order}. Zones are the routing unit — never aisles-with-numbers (no-data stores don't have reliable ones).
- **Sighting** {id, item_id (dictionary), zone_id, store_id, evidence {type: walkthrough_frame | aisle_photo | cart_photo | user_taught | receipt_only}, captured_at, confidence, status: live | disputed | retired, source_ref}.
- **StoreIndex** = the store's zones + live sightings + coverage, versioned; every ingest produces a new version.

Requirements:
- FR-3.1 The map is **incremental and partial by design**: it is built from any mix of full walkthroughs, aisle photos, cart photos, taught captures, and receipt-only evidence (receipt proves the store sells it, not where). There is no "complete index" state — only coverage.
- FR-3.2 **Confidence & decay.** Each sighting's effective confidence = base confidence × 0.5^(age_days / 21) (21-day half-life). "Found it" → confidence refreshed to 0.95, timestamp reset. "Not here" → confidence × 0.3 and status disputed. Two independent "not here" reports within 14 days → status retired. Guidance asserts sightings at effective confidence ≥0.60; 0.35–0.60 is shown as "last seen (unconfirmed)"; <0.35 is excluded from routing but retained for history/grading.
- FR-3.3 **Coverage.** coverage % per store = zones with ≥1 live sighting ÷ zones in the store skeleton, shown alongside item coverage (user's regular items with a live sighting ÷ regular items bought at this store). Coverage is a first-class UI element (§3.5).
- FR-3.4 Walkthrough ingest: a video (phone or Ray-Ban glasses recording, uploaded as a file) is indexed by Muse Spark 1.3 into zone skeleton + item sightings with timestamps. Ingest is an offline/background job, never in the shopping path. SAM is **not** run over full walkthrough video (see IMPLEMENTATION flag F2) — Spark produces the index; SAM grounds stills.
- FR-3.5 Aisle-photo ingest: one photo → Spark proposes zone + sightings; items needing shelf grounding can be SAM-verified on the still.
- FR-3.6 The map is **personal-first**: one user's map is authoritative for that user; the owner's corrections are final (no consensus needed). Sharing/aggregation is roadmap; the grading proof (§6.12) is the only multi-source element in scope.

### 6.4 Route planning (C4)

- FR-4.1 Input: a list (from smart list, voice, or manual at home) + a StoreIndex. Output: a `RoutePlan` — stops grouped and ordered by zone skeleton order; each stop {item, zone, sighting confidence, evidence age}; an explicit **unknowns** list (items with no live sighting) with the teaching ask attached ("if you find it, show me the aisle").
- FR-4.2 Planning works against partial maps at any coverage, degrading honestly: low coverage → shorter known route + longer unknowns list, never fabricated locations.
- FR-4.3 Replanning is live: a correction, a taught sighting, or a checked-off item re-plans the remaining stops without restarting the trip.

### 6.5 Guided mode (C5)

Overlay states (the full state machine is a PWA concern; the semantics are specified here):

| State | Meaning | Screen shows |
|---|---|---|
| `TO_ZONE` | Walking to next zone | Zone name + landmark cue ("back wall, past produce"), current item |
| `CHECKPOINT` | Relocalization requested | "Show me the aisle" — camera pan prompt |
| `RELOCALIZED` | Position confirmed | Confirmation + next cue |
| `AT_SHELF` | In the item's zone | "Find: oat milk" + SAM find button/auto |
| `FOUND` | SAM/user confirmed the item | Highlight + Got it |
| `NOT_HERE` | User disputes the sighting | Repair flow (§6.8) |
| `TEACH` | Unknown item found by user | "Show me where" capture prompt |
| `DONE` | All stops resolved | Trip recap (found / not found / taught) |

- FR-5.1 **Relocalization checkpoints** occur at zone transitions and on demand ("where am I?"). The user pans the camera across the aisle (or snaps one photo); Spark compares against walkthrough exemplars/index descriptions and returns the zone + confidence. Low confidence → the app asks for one more pan or a landmark, it does not guess a zone.
- FR-5.2 Guidance is landmark-based spatial language ("back wall," "on your left after frozen"), never turn-by-turn GPS and never invented aisle numbers.
- FR-5.3 Checkpoints are asynchronous and non-blocking: the user keeps walking; the answer lands when it lands (latency budget §7). The UI never freezes the trip on a model call.

### 6.6 SAM item find (C6)

- FR-6.1 At the shelf, SAM 3.1 is queried with one short concept phrase per request (hosted API limit: text prompts only, one concept per request) against the current camera frame/photo; returned masks/boxes are drawn as the overlay highlight.
- FR-6.2 The concept phrase comes from the dictionary (the visually groundable noun phrase for the canonical item, e.g. "oat milk carton").
- FR-6.3 SAM absence is not failure: no mask → "not spotted — scan slowly" + manual Got it remains available. Presence score below the calibrated threshold → shown as a tentative highlight, labeled as such.

### 6.7 Voice interaction (C7)

- FR-7.1 Voice is the primary in-store input: push-to-talk button on the overlay (large, thumb-reachable). Always-listening is out of scope (noise, etiquette, battery).
- FR-7.2 Transport: Muse Voice Transcribe realtime WebSocket (`wss://api.meta.ai/v1/asr/realtime`) with the user's dictionary loaded as keyword biasing (the recognizer hears *his* vocabulary: tahini, gochujang). Biasing guides, doesn't guarantee — so every transcript is parsed by Spark into {intent, slots, interpretation confidence}; low interpretation confidence → a single confirm prompt ("Oat milk — add it?"), restraint rule applies (confirm only consequential or low-confidence parses).
- FR-7.3 Command grammar (in-store set is deliberately small):

| Intent | Example | Effect |
|---|---|---|
| `teach` | "The tahini is here" | Create sighting at current zone (asks camera capture if none) |
| `correct` | "Not here" / "It moved to the frozen aisle" | Correction protocol (§6.8) |
| `ask` | "Where are the eggs in my map?" | Answer from StoreIndex (with confidence label) |
| `list_add` | "Add oat milk" | Append to active list; replan if in a trip |
| `check` | "Got it" | Check off current target |
| `where_am_i` | "Where am I?" | Trigger relocalization checkpoint |
| `skip` | "Skip it" | Defer current stop |

- FR-7.4 Free-form speech is allowed at home (list building, questions about patterns); in-store, out-of-grammar speech falls back to `list_add` interpretation or a brief "didn't catch that" — never a dead end.
- FR-7.5 Voice out is device TTS, short phrases only, and suppressible; visual + haptic confirmations are the default.

### 6.8 Correction protocol (C8)

- FR-8.1 At every guided stop, a one-tap **Not here** (and the voice `correct` intent) is available. The disputed sighting is demoted **immediately** (FR-3.2) — the app stops asserting it in the same session.
- FR-8.2 The app responds with the repair, in this order: most likely alternate zone if another sighting exists ("also seen near frozen — check there?"), then the exact fix action ("Find it? Tap Found it there, or photograph the shelf and I'll re-learn it"). A correction is never a dead end or a bare apology.
- FR-8.3 "Found it" at a different zone creates a new sighting there and refreshes confidence (FR-3.2).
- FR-8.4 End-of-trip recap (safety net): one screen — found / not found / taught — pre-filled from the trip; only exceptions need taps.

### 6.9 Patterns & consumption model (C9)

- FR-9.1 From the ledger, per canonical item: purchase count, dates, quantities, median interval (days), last bought, spend. Computed deterministically from ledger data (SQL/aggregations), **not** by an LLM — the model narrates, it doesn't do the arithmetic.
- FR-9.2 Pattern page shows: staples & their cycles, one-offs, lapsed items (bought before, stopped), and spend by source type (budget rollup, FR-2.4).

### 6.10 Smart list (C10)

- FR-10.1 The smart list drafts from patterns: items whose elapsed time since last purchase ≥ their median interval are "due"; quantity suggested from typical quantity. Spark ranks/narrates the draft ("due this week") but the due-set itself is computed (FR-9.1).
- FR-10.2 The user edits by tap/voice at home; the list binds to a store for routing (FR-4.1). Meal-hook missing ingredients join here (FR-11.2).

### 6.11 Meal hook (C11)

- FR-11.1 One dinner suggestion per day built **only** from ingredients the ledger proves are in the kitchen (recent purchases minus typical consumption), with the reasoning shown ("you have chicken, rice, and frozen peas as of Sunday").
- FR-11.2 Missing ingredients for the suggestion can be added to the smart list in one tap — this is the visible loop-closure into the next trip.
- FR-11.3 Optional scene: Muse Image renders the suggested dish from the actual ingredient set ($0.01/image; the delight beat). No nutrition claims anywhere — money and habits only (owner rule + avoid list).

### 6.12 Platform grading proof (C12)

- FR-12.1 Two walkthroughs of the same store can be ingested; the system grades each on **recency, clarity** (frame sharpness/coverage of zones), and **completeness** (zones/items indexed) and selects the map source, showing the grade table. This is the working proof of the Waze-for-aisles mechanism; the multi-user platform itself is roadmap.
- FR-12.2 Glasses-captured walkthroughs are accepted as ordinary video uploads (glasses record; phone guides — Ray-Ban glasses have no display and no live third-party camera API).

### 6.13 Glimmer pre-filter (C13)

- FR-13.1 Behind a feature flag, Glimmer (Fireworks-hosted) does a cheap first pass on aisle photos ("does this frame likely contain the target / which zone family?") before Spark is called. It is an optimization and the open-weights showcase — the pipeline must pass all gates with the flag **off**.

## 7. Non-functional requirements

### 7.1 Latency budgets (Standard mode, in-store network)

| Interaction | Budget | Notes |
|---|---|---|
| Voice command (PTT release → action) | ≤ 2.5 s | ASR streams during speech; parse is the tail |
| SAM find (frame → highlight) | ≤ 3 s | One concept, one still |
| Relocalization checkpoint | ≤ 6 s p95, non-blocking | Async by design (FR-5.3); Spark at low reasoning effort |
| Route plan / replan | ≤ 5 s | Mostly computed; Spark only narrates exceptions |
| Receipt decode (photo → draft ledger) | ≤ 20 s | At-home context; progress shown |
| Walkthrough indexing | ≤ 10 min per 10 min of video | Background job (FR-3.4) |

Spark is a reasoning model (reasoning tokens bill as output; third-party measurement showed ~9 s for a trivial reply at default effort). In-store calls therefore use low `reasoning_effort`, tight prompts, and cached dictionary/index context (cached input $0.15/M vs $1.25/M). If the relocalization gate (§9) fails on latency or accuracy, the degraded mode is zone guide + item spotting (pre-decided in BUILD-PLAN).

### 7.2 Cost budget (from PRODUCTS.md pricing)

- **Ceiling: the $150 Meta Model API credit.** Fireworks Glimmer spend rides the separate $25 Fireworks credit (select-participant; flag F7).
- **Per guided trip target: ≤ $0.35** on Standard rates (relocalization checkpoints × ~6, SAM finds × ~10 stills at $0.0025, voice ≈ 5 min PTT audio at $0.18/hr ≈ $0.015, decode of one receipt ≈ $0.01–0.02, pattern/list calls ≈ $0.02; store indexing amortized separately at ≤ $0.10/trip over ≥20 trips).
- Every API call is logged (model, mode, tokens, $) to a running cost ledger from Stage 0 — no unmetered calls exist.

### 7.3 Privacy — personal-first

- The map, ledger, and dictionary are one user's data, stored under that user's identity; personal maps are never shared by default (sharing is opt-in roadmap).
- Receipts are intimate data: **real user receipts are only ever sent to Standard-mode models.** Contributor-mode models may be trained on by Meta and Meta's terms bar sending them personal data — Contributor is used in dev loops only with synthetic/anonymized data (IMPLEMENTATION flag F1).
- Demo data is the owner's own, used with his consent; no third party's data appears in the demo.

### 7.4 Connectivity & degradation (in-store reality)

In-store connectivity is poor (warehouse construction). The PWA must:

- Cache the app shell, the active StoreIndex, the active list, and the current RoutePlan for offline use after trip start.
- Queue sightings, corrections, and check-offs locally when offline and sync on reconnect (corrections apply locally immediately — FR-8.1's "stops asserting" must not wait for a network).
- Degrade in order: live relocalization → last-known zone + landmark cues → static route list with manual check-off. SAM find offline → unavailable, manual Got it always works.
- Precompute/prefetch the route plan before entering the store when a trip is started at home.

## 8. Client requirements (PWA)

- Installable PWA, phone-first, single-hand use; camera via `getUserMedia`; screen kept awake during guided mode (Wake Lock API where available).
- List and map views fully usable on cached data with no connectivity (§7.4).
- The UI build stage follows the **impeccable skill playbook** (UX is a primary focus, §3); the design bar is "a joy — easy, intuitive," reviewed against §3's principles as an explicit gate (IMPLEMENTATION Stage 6).

## 9. Acceptance criteria & spike gates

**Spike gate 1 — receipt decode (Stage 1, on the golden receipt set, Standard mode):**
- ≥95% of receipt lines captured (none dropped silently).
- ≥85% of lines auto-posted (confidence ≥0.85) **and** correctly identified.
- Silently-wrong auto-posts ≤2% of lines (the trust metric — this is the one that matters).
- Totals reconcile within $0.05 (FR-1.4) on ≥5 of 6 golden receipts.
- The remainder land in the unverified queue (never dropped, never guessed).

**Spike gate 2 — TJ's relocalization (Stage 3):**
- ≥8/10 fresh in-store photos correctly relocalized to department/zone from the walkthrough index, at ≤6 s p95. Fail → degraded scope (zone guide + item spotting), decided the same day.

**Per-component acceptance (all Standard mode, gates run by the verifier loop):**

| Component | Criterion |
|---|---|
| Dictionary (C2) | After the golden set + corrections pass, re-decoding the same receipts asks about 0 previously-corrected codes |
| Store map (C3) | Ingest of walkthrough #1 yields a zone skeleton + sightings for ≥70% of the items on the owner's TJ's regular list; coverage % computed and displayed |
| Route (C4) | Every list item appears exactly once: in stops or in unknowns; no invented locations (0 stops without a live sighting) |
| Guided (C5) | Simulated trip (scripted checkpoints) completes all states incl. NOT_HERE and TEACH without a dead end |
| SAM find (C6) | On the rehearsal shelf set, target highlighted (IoU ≥0.3 vs hand-labeled box) on ≥7/10 items; absence handled per FR-6.3 |
| Voice (C7) | ≥90% intent accuracy on the recorded command test set (owner's voice, store-noise background); 0 consequential actions taken on low-confidence parses without confirmation |
| Correction (C8) | After "not here," the same trip's replan never re-asserts the disputed sighting; recap matches trip events exactly |
| Patterns (C9) | Intervals/counts match a hand-computed check on the golden ledger for 100% of items (it's arithmetic — no partial credit) |
| Smart list (C10) | Due-set equals the deterministic rule output; Spark's narration adds no items not in the due-set or user-added |
| Meal hook (C11) | Suggestion uses only ledger-supported ingredients (0 invented ingredients) |
| Grading (C12) | Two-walkthrough grade table produced; the objectively more complete walkthrough wins on the completeness sub-score |
| Glimmer (C13) | All gates pass with the flag off; with it on, Spark calls per aisle photo drop vs baseline (that's its only job) |

## 10. Out of scope (roadmap — pitch only, do not build)

- Mapper incentive network / Instacart-style paid walkthrough partnerships; multi-store/city platform; consensus (multi-user) maps; public map sharing.
- Live guidance *on* glasses; any glasses API integration (glasses are a recording source only).
- Retailer-data hybrid (Target/Walmart planogram APIs); barcode scanning as a primary input.
- Price intelligence across stores/receipts; budget-planning depth beyond the ledger rollup (FR-2.4); make-at-home bridge (delivery-pattern → grocery suggestions).
- Nutrition, health, or dietary advice — permanently out (owner rule).
- Shared family lists/accounts; multi-user anything.
- Native apps (PWA only); always-listening voice; turn-by-turn indoor positioning of any kind.
- Muse Wonder / Wonder Full anywhere in the pipeline (Wonder Full has no API SKU; Wonder's $4/$20 token hunger buys nothing this product needs).

*Design flags discovered while specifying (with smallest fixes) live in IMPLEMENTATION.md §9 — F1 (Contributor × personal data), F2 (SAM over full video), F3 (Spark latency), F4 (ASR has no confidence scores), F5 (video tokenization unknown), F6 (PWA camera/wake limits), F7 (Glimmer price/credit unverified).*
