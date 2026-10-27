# Grocery Navigator — pitch (working title; decided 2026-10-27)

**One-liner:** Arya keeps a living model of your grocery world: every receipt read and verified, every return netted, every pattern learned — so the list writes itself. And in the store, she guides you shelf to shelf until the list is done. (Store layer origin line, still true as the add-on hook: Google Maps never made it inside the grocery store — we build the map from shoppers' own videos.)

**Problem.** Target and Walmart shoppers get aisle directions because those retailers publish their data. Everyone else wanders: Trader Joe's, Costco, and independent stores publish nothing — Costco's sign-free maze is deliberate — so no app can guide you there. And the one record of what you actually buy, the receipt, gets thrown away, so every shopping list starts from zero.

**What it does — one product, one loop:**
1. **LEARN your store, trip by trip.** Like a robot vacuum learning your house, the app builds your personal map of the store from whatever you give it — a full walkthrough (phone or Ray-Ban Meta glasses) if you have one, a few aisle photos if you don't. Coverage grows every trip, and the map is honest about its gaps: ask it where something is and it answers from what it knows, plans your route zone by zone, and when you find something it hasn't mapped, it asks you to show it that aisle — so next time, it knows. Maps can be shared and ranked (newest, clearest, most complete wins), but yours is yours first.
2. **GUIDE every trip.** Your list becomes a route. A camera overlay walks you aisle to aisle; the app sees what you see, spots each item on the shelf (SAM 3.1), and checks it off as you grab it.
3. **RECONCILE at checkout.** Photo of the receipt + photo of the cart. Cryptic receipt codes are matched against what's visibly in the cart — what you paid for is verified against evidence, never guessed; the unsure few ask you.
4. **LEARN always.** Receipts become your consumption pattern — what you buy, how fast you use it — so the next list writes itself, and tonight's dinner suggests itself from what's actually in your kitchen.

**Why Meta, why now.** Spark's native video understanding turns a raw walkthrough into a map — that was impossible before it, which is why this product doesn't exist. SAM grounds items on real shelves; Voice Transcribe takes the list hands-free. No retailer partnership, no beacons, no planogram feed.

**Who first.** Shoppers at no-data stores — and travelers walking into an unfamiliar store that someone else has already mapped for them.

**The platform.** Every guided trip can refresh the map; mappers (Instacart-style shoppers) get paid per accepted walkthrough. Waze for store aisles.

**Hackathon build (by Nov 4):** one Trader Joe's mapped and guided end-to-end + the full receipt/cart/pattern loop running on real Costco history. Community ranking and glasses capture shown as working proofs; the mapper network is the roadmap.
