# Owner brainstorm candidates (from Vibhor, live)

## Grocery Navigator (2026-10-27, voice brainstorm)
- Core: pick your store + your list; the app guides you item to item, turn-by-turn (Maps-style overlay), because it knows THAT store's layout. Target already publishes aisle/stock data; Trader Joe's and Costco don't, and layouts differ per location — that's the gap.
- Knowledge source (his premise): stores get recorded — a video walkthrough of the layout/items. Per-store, crowdsourceable.
- Layer 2 (parked by him): receipt uploads -> learns purchase patterns/frequency, maintains smart lists, product research.
- Spark's scoping for feasibility: true indoor turn-by-turn needs positioning GPS can't do; the buildable version = walkthrough video -> Spark builds a shelf/landmark index; live mode guides by landmarks and VERIFIES via the shopper's camera (SAM finds the item on the shelf: "that's it") — the watch-verify-coach engine applied to navigation. Scope demo to ONE store (his Costco or TJ's).
- Status: sent to the mass-problems researcher for prior-art vetting (Instacart/Walmart in-store nav, indoor-positioning startups) + scoring in the revised union ranking, flagged owner-originated.

## Grocery Navigator v2 (owner refinement, 2026-10-27 11:37 EDT)
- Guidance was NEVER GPS: it's an overlay on the live camera image — arrows/highlights drawn on what the camera sees. (Matches the vetting's landmark-hop + relocalization model; the "map" routes offscreen, the user sees camera overlay + next landmark.)
- Capture device option: Ray-Ban Meta glasses. The wearer's brain doesn't register every product; the camera + recognition does. Two capture modes: phone camera held on while shopping, or glasses recording the walkthrough.
- PLATFORM layer (new): people share store walkthrough videos; the system picks the latest / most popular / best-graded (quality, lighting, completeness) as that store's map. Community-built — Waze for store aisles. Travelers/new-city shoppers inherit maps others made; drift heals via fresh uploads + quality grading.
- His words on value: "i don't know if this is a monetizable product but it's definitely something that is going to help a lot of people... a guided tour guide through our grocery store" (rushed/overwhelmed daily shoppers + travelers).
- Spark's honest hardware note: glasses have no display and no live third-party camera API — glasses RECORD (POV, hands-free, ideal walkthroughs; video lands on the phone), the phone shows the overlay. Capture on glasses, guidance on phone.

## Grocery Navigator v4 — personal incremental map (owner, 2026-10-27 11:46 EDT)
- PERSONAL map mode: no complete walkthrough required. User records a video OR clicks a few aisle photos per trip; like a robot vacuum learning a house, the AI builds THAT store's map incrementally for him alone.
- Map is browsable/searchable: "where might X be?" answered from the map; route planning from a list against the PARTIAL map — items grouped by known zones; honest gaps listed ("not in my map yet").
- Active-learning loop: when the user finds an unmapped item, the app asks him to photograph that aisle/record the area -> map updates. The app knows what it doesn't know and requests exactly that evidence.
- Architecture consequence: store index must be incremental/partial from day one (zones + item sightings w/ confidence + timestamps + coverage %), not a one-shot full index. Personal-first; community sharing is opt-in aggregation later.

## v5 — correction loop (owner, 2026-10-27 11:47 EDT)
- Solves drift at the point of failure: app says item is here, it isn't (layout changed OR AI erred — same handling). One-tap "Not here" in the moment + end-of-trip feedback recap option.
- On correction, the app must tell the user what to DO to fix it for the future (alternate zone hint + "photograph the shelf / tap Found it where it actually is").

## v6 — voice interaction (owner, 2026-10-27 11:53 EDT)
- Voice as a first-class interaction channel: users talk to the app — teaching ("this is here"), correcting, asking — because in a store, hands are busy and most people are fine talking to an app.

## v7 — beyond groceries (owner, 2026-10-27 13:26 EDT)
- Receipt intake generalizes: restaurant bills + delivery orders upload the same way. The ledger becomes a FOOD-SPEND ledger (groceries / dining out / delivery), feeding budget planning.
- Nutrition explicitly OUT (his words — hackathon avoid list); money + habits only.
- Make-at-home bridge (future): things ordered/eaten out often that are easily made at home -> suggest grocery items for the list + recipes. Spend visibly shifts delivery -> grocery.
- Trajectory: grocery + purchase habits are the seed of a general daily-life AI agent assistant.

## v8 — returns handling (owner, 2026-10-27 13:42 EDT)
- Returns are a first-class ledger event: intake detects refund lines/return receipts; returns reconcile against the original purchase; consumption patterns count KEPT items only (bought != kept); a returned item is a strong negative signal for future lists.
- Product surface: returns queue with the receipt proof ready + policy windows (e.g., Costco electronics 90 days); refunds flow back into the spend ledger.
- Hackathon scope: detection + pattern exclusion + honest ledger. Reminders/desk flow = roadmap.

## v9 — CORE vs ENHANCEMENT reframe (owner, 2026-10-27 13:52 EDT)
- CORE BUSINESS = receipts + cart double-check + patterns -> the list that writes itself.
  The loop closes with NO store map: list writes itself -> shop anywhere -> receipt+cart
  verified at checkout -> patterns sharpen. Works in any store, day one, on data in hand.
- The grocery video/store layer is an ADD-ON: a helper for days you want it. When a map
  exists, guidance turns on; when it doesn't, the core is untouched.
- Framing: the receipt is the SENSOR, the self-writing list is the SURFACE (the product).
- Consequence: Spike 2 (relocalization) leaves the critical path — it gates the
  enhancement only. Nov 4 risk drops materially.

## v10 — "Eyes of the app" (owner, 2026-10-27 13:56 EDT)
- Third sensor: fridge / pantry / freezer / fruit-table photos (or short video) = visual
  inventory. App identifies visible items -> list updates automatically (have it -> off
  the list; missing vs pattern -> on).
- Expiry awareness: category shelf-life priors + per-item printed dates. App ASKS the user
  to photograph best-before dates of specific high-risk items AT PUT-AWAY time (one item,
  close-up, good light — the winnable OCR moment).
- User corrections teach the household's real shelf life: "this expired" feedback adjusts
  that item's burn model; app reminds next cycle before it happens again; chronic waste
  -> suggest smaller pack / lower qty.
- Owner's own caveat (adopted as doctrine): not everything is visible — identify what's
  seen, ask for corrective action on the rest. Never guess inventory.
