# VET: Grocery Navigator — owner-originated candidate

*Vetted 2026-10-27. Lens: prior art, phone-only positioning physics, layout drift, judge scoring (Impact 30 / Tooling 25 / Demo 25 / Depth 20). Verdict at the end.*

**The idea.** Pick a store + a list. The app walks you item to item, turn by turn, because it knows this store's layout. The layout knowledge comes from a video walkthrough, indexed into a shelf/landmark graph. Target chains: the ones that publish *nothing* — Trader Joe's (no app, no e-commerce, no customer data, by stated philosophy) and Costco (no aisle signs, no maps, deliberate "treasure hunt" rotation). Layer 2 (parked): receipts → purchase patterns → smart lists.

---

## 1. Prior art — what's actually new, and what the graveyard says

**Retailer first-party item location (mature, solved where data exists).**
- **Walmart app:** aisle + 4-foot *section* for items, plus in-store maps and Wi-Fi-based blue-dot positioning. The data comes from Walmart's own "Item File" — every product's modular (planogram bay), updated when associates scan items during modular resets. It is an operations database, not a map someone made.
- **Target app:** same shape — aisle + stock status from planogram and inventory systems.
- **Instacart Shopper app:** interactive store map with "precise item locations" — but for gig shoppers, at retailer-partner stores (pilot at 80+ stores), fed by retailer data. And in Sept 2026 Instacart went further: shelf-scan data from its ~600k shoppers (~15 visits/store/day) + Caper Carts computer vision to build a *real-time* shelf map for retailers. The data flywheel belongs to whoever has an army in the aisles daily.
- **Sainsbury's SmartLists (Oct 2026):** AI list-building (type/speak/photo) with an in-store product finder — first-party again.

**Indoor-mapping startups (the cautionary tale).**
- **Aisle411 (founded 2008):** the direct ancestor of this idea — search a store, get a map pinning the aisle. It survived only by licensing to retailers (Walgreens' 7,800 stores, Hy-Vee, WinCo) and bolting on indoor positioning (WiLocate acquisition, 2012). As an independent consumer product it faded; its trademarks lapsed (cancelled 2023). Lesson: the technology worked; the *data supply chain* was the business, and retailers owned it.
- **Point Inside:** built indoor maps for 1,800+ US malls and 200+ airports; its assets were acquired by MapsPeople in 2023 and folded into B2B venue wayfinding. Again: B2B, partner-supplied floor plans.
- **Google Indoor Maps:** 10,000+ venues since 2011, floor plans *submitted by venue partners only* — Google explicitly disables crowdsourced edits on indoor layers. Blue dot indoors is Wi-Fi-based, "accurate within several meters." Even Google will not build indoor maps without the venue handing over plans.
- **Accessibility research** (GuidedGrocer and similar): voice-guided grocery help for visually impaired shoppers exists as prototypes — all assuming a store-managed inventory backend.

**What failed and why.** Every durable deployment sits on one of two foundations: (1) retailer-owned operational data (planograms, mod-set scans, POS inventory), or (2) venue-submitted floor plans plus installed infrastructure (Wi-Fi fingerprinting, beacons). Every attempt to be a third-party layer without the retailer's data either became a B2B vendor to retailers or died. Nobody — not Google — maintains consumer indoor item maps from independent observation, because keeping them true costs more than making them once.

**Genuinely new in this candidate.** Two things have never shipped consumer-side:
1. **The map source.** A map built from a *video walkthrough* by a vision model — no planogram feed, no venue partnership, no survey hardware. In 2012 this was impossible; with Spark's native video understanding it is at least plausible. This is the idea's real invention.
2. **The target.** Deliberately aiming at the two chains whose *business model is withholding this data* (Costco's treasure hunt, TJ's analog philosophy). No incumbent will ever serve these stores. The moat-gap is real.

Honest counterweight: "new because nobody could" and "new because nobody can keep it true" are the same sentence until the drift question (§3) is answered.

## 2. Indoor positioning — the physics problem, answered honestly

GPS indoors: dead (multipath/attenuation; several-meter error even in Walmart's Wi-Fi-assisted best case). A phone-only build has two honest shapes:

**(a) True continuous positioning (blue-dot turn-by-turn).** Requires one of: BLE beacons installed by the venue (Costco/TJ's will not install them for a third-party app, and the user can't); Wi-Fi RTT (802.11mc — Android-only in practice, needs RTT-capable APs, iOS exposes nothing equivalent); geomagnetic fingerprinting (needs a prior per-store survey pass — Oriient's model, sold B2B); or full VPS against a pre-built 3D visual map (needs multi-pass SfM capture per store, heavy offline pipeline, and commercial VPS SDKs are B2B per-venue contracts). ARKit/ARCore VIO alone gives *relative* motion that drifts and resets every session — it cannot know "you are at dairy" without relocalization. And even if position were free, the guidance loop can't run at navigation frame rates through the Meta API: Spark reasons before answering (third-party measurements in PRODUCTS.md put even short replies at ~seconds of latency), and SAM video is billed per frame. **A live blue-dot with cloud-VLM guidance is not buildable honestly by Nov 4. Faking it (scripted route, hidden wizard) is exactly what live judging exposes.**

**(b) Landmark-guided hops with camera relocalization — the demo-honest shape.** No continuous position is ever claimed. The route is a sequence of legs between *stable, human-visible landmarks* (entrance → produce wall → back-wall coolers → freezer row → checkout). Guidance is spatial language a human can follow unaided ("walk to the back wall; dairy runs along it; eggs at the far end"). At each hop, or whenever the user is unsure, they pan the camera: Spark identifies the landmark/department from the live scene (matched against walkthrough exemplars), SAM grounds the target category/product on the shelf ("coffee" concept → mask + highlight), and the app confirms arrival and checks the item off. Failure degrades gracefully — worst case it is a zone guide with a camera that can spot your item, which is still better than anything TJ's shoppers have today (nothing). Per-hop latency of 2–5 s is acceptable because it happens at checkpoints, not mid-stride.

**Verdict on approach: (b), unambiguously.** It also happens to be the only shape whose demo can't be accused of being staged — there is no continuous tracking on screen to fake.

## 3. Layout drift — how fast the index decays, and what can repair it

Drift is *layered*, and the layers decay at very different rates:

| Layer | Costco | Trader Joe's | Conventional grocer | Half-life |
|---|---|---|---|---|
| Macro zones (departments, back wall, freezer row) | Stable — fresh/frozen anchored at rear by design | Stable | Stable | Months–years |
| Category placement (which aisle/run holds coffee) | Moves, but within a zone | Mostly stable | Planogram resets a few times/yr per category | Weeks–months |
| Exact product bay / pallet position | **Deliberately rotated** — the "treasure hunt"; staples get moved once regulars learn them | Product churn is high (items discontinued/rotated) but placement steadier | Endcaps/promos weekly; bay placement steadier | Days–weeks |

Design consequence: **the index must be hierarchical and the guidance must target the stable layers.** Navigate to zone → category; let the *camera* do the last ten feet live (SAM spots the item wherever it is today). An index that promises "aisle 12, bay 3" at Costco is lying within a fortnight; an index that promises "coffee lives in the center-store dry-goods run, roughly here" is still true next month, and the live camera closes the gap.

**Cheap correction loops, ranked by cost per fix:**
1. **Found-it confirmation (free, in-flow).** Every successful camera spot during a shop *is* a relabeling event: the system learns the item's current landmark context from the shopper's own session. The map heals as a byproduct of use.
2. **One-tap "it moved" report.** User taps when the index is wrong; the item is re-anchored at the user's next camera confirmation. Cheap, but sparse.
3. **Targeted re-walks (minutes, not hours).** Only volatile zones need re-indexing — a 2-minute walkthrough of center-store, not the whole warehouse.
4. **Receipts (weak for location, strong for stock).** A receipt proves an item was *in the store that day* but carries zero location signal. Receipts feed layer 2 (patterns, smart lists) and a "probably still stocked" prior — they do **not** repair the map. Don't oversell them as a drift fix.

## 4. Judge scoring

**Impact — strong prevalence, moderate depth per use.** Grocery shopping is one of the most frequent errands in life: industry figures put the average US household at roughly 1.5–2+ store trips a week and ~40–47 minutes per trip; Oracle's shopper survey found 38% cite lack of/limited inventory as their *biggest* grocery frustration, 36% prize easy-to-navigate floor plans, and separate UK research found 1 in 5 trips involves missing items. The pain concentrates exactly where this app aims: an unfamiliar store, a moved staple, a 146,000 sq ft warehouse with no signs. Realistic value per trip is 5–10 minutes and one avoided backtrack-across-the-warehouse — meaningful at weekly cadence, but it is minutes, not money, health, or safety. **8/10 on breadth, capped by shallowness per use.**

**Tooling — genuinely load-bearing, three models deep.** Spark's native video input is the *indexing engine* (walkthrough → landmark graph) *and* the relocalizer — the single most "only this model family" use in the whole candidate pool. SAM 3.1 grounds the target on the shelf — perception with a job nothing else does. Voice Transcribe is the hands-free interface (cart in one hand, list dictated, "where are the eggs?" mid-aisle) — STT-only is fine because the output channel is visual. Muse Image is *not* needed; forcing it would weaken the story. This is a real three-model architecture, not a wrapper. **9/10.**

**Demo — highest ceiling, highest variance in the pool.** In a real store, on a real list, with the camera spotting the item on the shelf: unforgettable, and it demos a *capability*, not a UI. But the failure modes are all live and physical: Costco prohibits photography in its warehouses (membership terms) and TJ's is famously camera-unfriendly — the demo store must be chosen for permission, not just pain; warehouse connectivity is poor (steel roof, deep interior); and **visual aliasing is severe in Costco** — endless identical orange racking and pallets means Spark's relocalization has far fewer distinctive landmarks than in a TJ's, whose hand-lettered signs and colorful displays are a landmark-rich environment. The pain is worst at Costco; the technology works best at TJ's. Choose TJ's (or a characterful independent grocer) for the demo and let Costco be the roadmap slide. **9/10 if it lands, 4/10 if the store fights back — call it 7 risk-adjusted.**

**Depth — real systems problems, honestly framed.** Landmark-graph construction from raw video (no SfM, no planogram), VLM relocalization under aliasing with confidence-gated fallback, list→route optimization over zones, and a decay-weighted index that knows what it no longer knows. That is a legitimate 20%. It reads thin only if presented as "prompt a model with frames" — the depth is in the hierarchy and the honesty machinery. **8/10.**

**Weighted ≈ 0.3(8) + 0.25(9) + 0.25(7) + 0.2(8) = 8.0** — competitive with anything in the pool on paper; the Demo term carries all the variance.

**Shape vs. the watch→verify→coach engine family.** This is the same skeleton wearing different clothes: the coach family runs *perceive state → compare to target → guide next action → verify completion* over a **task**; Grocery Navigator runs *perceive location → compare to route → guide next leg → verify item found* over a **space**. Step graph ↔ landmark graph; step-completion check ↔ relocalization; "you did it wrong" ↔ "you're in the wrong aisle." A team that builds one has built ~60% of the other. Grocery Navigator is the family member whose "task" is the store itself.

## 5. One-store demo build sketch (~8 days)

**Store: one Trader Joe's** (landmark-rich, small footprint ~13k sq ft, no incumbent app, cult following = recognizable in a demo video). Get filming comfort first — shoot the walkthrough at a quiet hour; if TJ's pushes back, fall back to an independent grocer who says yes.

- **Day 1:** Walkthrough capture (2–3 slow passes, narrated). Spark video pass → zone/landmark graph JSON: departments, landmark exemplars (frames), adjacency, category→zone map. *Spike gate: can Spark relocalize from 10 test photos taken fresh in the store? If <8/10 correct department, stop and re-rank — this is the whole bet.*
- **Day 2:** Landmark graph editor (hand-fix the JSON; cheap and honest), route planner (list → zone-ordered legs, simple TSP over zones).
- **Day 3:** List ingestion — voice dictation via Voice Transcribe, photo of a handwritten list via Spark vision; item→category resolution.
- **Day 4–5:** Shopper PWA (no app-store review): leg cards ("Head to the back wall — frozen"), "Where am I?" camera check (Spark relocalization, confidence-gated), "Find it" mode (SAM concept mask on the live shelf view), found-it check-off feeding the correction loop.
- **Day 6:** Full in-store field test with a real list; fix the top failure class only.
- **Day 7:** Drift machinery: confidence decay, one-tap "it moved," receipt-photo stub for the layer-2 story.
- **Day 8:** Demo video shot in the store (real list, real backtrack avoided), submission buffer.

## 6. Top 3 risks and mitigations

1. **Filming permission / store hostility (esp. Costco's no-photography rule).** *Mitigation:* demo at TJ's or an independent with permission; walkthrough shot discreetly at off-peak; if live judging needs a store run, the pre-shot in-store video + a live relocalization on judge-supplied photos covers it.
2. **Relocalization failure under visual aliasing** (Costco worst, any big-box bad: identical shelving runs). *Mitigation:* landmark set chosen for distinctiveness (endcaps, freezer doors, signage, department color blocks); hierarchical fallbacks (zone-level directions when confidence is low); the app says "I think you're in beverages — pan left" instead of asserting. Gate the whole project on the Day-1 spike.
3. **Drift between indexing day and judging day** (index built Oct 28, demo Nov 4 — a Costco rotation cycle fits inside that gap). *Mitigation:* navigate to category, never to bay; live SAM search absorbs product-level drift; re-walk volatile zones the morning of the demo (2 minutes once the pipeline exists).

## 7. Verdict

**Mid — upper-mid (the #4–#5 slot in a mass-problems ranking), with a promotion clause.**

One-line reason: the pain is weekly and universal and the walkthrough-index mechanism is genuinely new, but the value per trip is minutes, incumbents prove the data moat belongs to retailers, and the demo must survive a real store that is designed — and in Costco's case, contractually enforced — to defeat it.

**Promotion clause:** if the Day-1 relocalization spike hits ≥8/10 at a Trader Joe's, this jumps to top 3 — the demo ceiling is the highest in the pool and Tooling is a clean 9. If the spike fails, park it without regret: every alternative positioning approach is a research project, not an 8-day build.
