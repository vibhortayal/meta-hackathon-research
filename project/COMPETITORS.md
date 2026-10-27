# Competitive Research — Personal Purchase Assistant (Team Nightshift)

Research date: 2026-10-27. Method: vendor App Store / Google Play listings, vendor sites, and dated third-party coverage. Vendor claims are marked as claims. Search snippets are not product tests.

Capability key:
- (a) Receipt/purchase ingestion beyond its own store
- (b) Cross-store purchase history in one user-facing model
- (c) Consumption patterns / run-out prediction
- (d) Home inventory or fridge/pantry photos
- (e) Returns tracking
- (f) Self-writing lists (system composes the list, not the user)

## Matrix

| Product | (a) | (b) | (c) | (d) | (e) | (f) |
|---|---|---|---|---|---|---|
| Instacart | No | Partial | Partial | No | No | Partial |
| Walmart app / Walmart+ | No | No | Partial | No | Partial* | Partial |
| Amazon (Fresh / Alexa / Subscribe & Save) | No | No | Partial | No | Partial* | Partial |
| AnyList | No | No | No | No | No | No |
| OurGroceries | No | No | No | No | No | No |
| Samsung Food | No | No | Partial | Yes | No | No |
| Fetch Rewards | Yes | No | No | No | No | No |
| CoinOut | Yes | No | No | No | No | No |
| Receipt Hog | Yes | No | No | No | No | No |
| Pantry Check | No | No | Partial | Yes | No | Partial |
| NoWaste | Partial | No | Partial | Yes | No | No |
| BEEP | No | No | No | Yes | No | No |
| KitchenPal | No | No | Partial | Yes | No | Partial |
| FridgeBuddy | Yes | Partial | Partial | Yes | No | Partial |
| Pastro | Yes | No | Partial | Partial | No | Partial |
| Duneed | Yes | Partial | No | Partial | No | No |

\* Partial (e) for Walmart and Amazon means return/refund status inside their own order history only. No product in the set nets returns against a purchase or consumption ledger. Column (e) is empty as a user feature across the whole set.

## Per-product evidence

### Instacart
- (a) No. No import of paper receipts or other stores' in-store purchases. History comes from orders placed through Instacart. Loyalty-card linking gives member pricing, not history ingestion — "you can link it to your Instacart account" for savings (https://www.dealnews.com/s57521/Instacart-Inc/).
- (b) Partial. Order history spans many retailers, but only for purchases made on Instacart. Buy It Again "surfaces previously purchased items to help build baskets" across those retailers (https://www.groceryretailonline.com/doc/instacart-caper-carts-roll-out-new-omnichannel-capabilities-for-more-savings-in-every-aisle-0001).
- (c) Partial. Frequency-based surfacing and sale alerts for regular items; no run-out date or cadence model is claimed.
- (f) Partial. Buy It Again helps build a basket faster; the user still picks each item (https://theshelbyreport.com/2025/10/02/instacart-rolls-out-additional-savings-features-on-caper-carts/).
- (d), (e): No evidence in sources reviewed.

### Walmart app / Walmart+
- (a) No. No outside-receipt ingestion found; history is Walmart orders.
- (c) Partial. "The new Walmart app uses purchase history to suggest frequently bought items, helping users reorder faster" (https://www.appsrhino.com/blogs/things-you-should-know-before-using-walmarts-grocery-app).
- (f) Partial. "Take advantage of the 'Reorder' section to quickly add frequently purchased items to your cart" — user-driven reorder, not a composed list (https://www.applibrary.reviews/en-US/app/walmart).
- (b) No; (d) No; (e) Partial* — "The account area keeps purchase history, subscriptions, plans, and order-related information in one place," Walmart orders only (https://apkpure.net/walmart-shopping-savings/com.walmart.android).

### Amazon (Fresh, Whole Foods, Alexa lists, Subscribe & Save)
- (a) No. No receipt ingestion from other retailers. (Amazon Shopper Panel pays users for outside receipts, but it is a market-research panel, not a user-facing assistant feature.)
- (c) Partial. Subscribe & Save gives "automatic recurring delivery of items you regularly use" on user-set intervals; Dash Replenishment lets devices "auto-order supplies when running low." Neither learns cadence from a unified purchase history (https://okut.online/voice-shopping-and-smart-home-commerce-guide/).
- (f) Partial. Alexa Scheduled Actions can add "restocking regular household items like pet food, paper towels, and detergent" to the cart on a schedule — rule-based, not learned from cross-store data (https://www.zonguru.com/blog/alexa-for-shopping-amazon-sellers).
- (b) No (Amazon-ecosystem orders only); (d) No; (e) Partial* (own-order returns only).

### AnyList
- List and recipe app. Lists are user-built with "smart autocomplete"; favorites and recent items are re-added by hand. No receipt ingestion, no purchase history model, no patterns, no inventory, no returns, no list composition (https://apps.apple.com/us/app/anylist-grocery-shopping-list/id522167641).

### OurGroceries
- Shared list app. "On-the-fly completion searches past shopping list items as you type" — that is list history, not purchase history. It keeps "a separate list of pantry staples so restocking the pantry takes just a few taps," which is manual. Its photo feature photographs an item to add it to a list; it is not receipt or inventory capture (https://apps.apple.com/us/app/our-groceries-shopping-list/id325851015; https://play.google.com/store/apps/details?id=com.headcode.ourgroceries&gl=DE).

### Samsung Food
- (d) Yes — the strongest platform version of photo inventory. Vision AI: "snap a picture of whatever is in your pantry or fridge, and the ingredients will be added to the list"; the app "can identify over 40,000 types of ingredients" (https://dlsserve.com/with-ai-food-recognition-samsung-food-could-be-the-ultimate-meal-planning-app/). Family Hub fridge cameras add items automatically.
- (c) Partial. Meal plans prioritize items "nearing use-by date," but the date "has to be set manually." Expiry-driven, not cadence learned from purchases (same source).
- (a) No receipt ingestion found. Lists are built from recipes and the Food List, then "send it straight to a retailer's e-commerce checkout" — recipe-driven, so (f) No (https://news.samsung.com/ca/samsung-announces-global-launch-of-samsung-food-an-ai-powered-personalized-food-and-recipe-service).
- (b), (e): No.

### Fetch Rewards
- (a) Yes. Takes any receipt: "Fetch | 25 points a receipt... | Any receipt" (https://www.mymillennialguide.com/money-for-receipts/). Receipts must be under 14 days old and are capped at 35 per rolling 7 days (https://www.claimowedmoney.com/blog/best-receipt-scanning-apps).
- (b)–(f) No. The decoded data serves points and brand offers. It is not returned to the user as a unified history, pattern view, inventory, or list. Fetch proves any-store receipt ingestion is a commodity; it does not compete on the assistant loop.

### CoinOut
- (a) Yes. "Snap a photo of any valid paper receipt... Receipts can be from any retailer or store in the US." It also connects email and retailer accounts so e-receipts earn automatically (https://play.google.com/store/apps/details?id=com.coinout.scan&hl=en_US&gl=US).
- (b)–(f) No. Same rewards-only pattern as Fetch.

### Receipt Hog
- (a) Yes. "Submit any purchase receipt. You earn 'coins' based on the total spent" (https://hertask.blogspot.com/2025/06/best-20-cashback-apps-for-grocery-receipt-savings.html). Note the coins scale with the total, not item lines — line-level decode for the user is not the product.
- (b)–(f) No.

### Pantry Check
- (d) Yes. Barcode-built inventory for pantry, fridge, and freezer, with expiration reminders and a "low stock" filter (https://www.agratefulkitchen.com/pantry-organization/best-pantry-inventory-apps).
- (c) Partial. It keeps a "current inventory & usage timeline" — usage recording, not forward run-out prediction (https://www.appbrain.com/app/pantry-check-grocery-list/com.pantrycheck.pantrycheck).
- (f) Partial (vendor claim). "Shopping lists built automatically from your usage and inventory" (same AppBrain listing). List generation is inventory-driven; the inventory itself is built by hand via barcode scans.
- (a) No receipt scanning found in listings reviewed. (b), (e): No.

### NoWaste
- (a) Partial (vendor claim). "Scan barcodes, receipts or photos to add food in seconds" (https://apps.apple.com/us/app/nowaste-food-inventory-list/id926211004). A 2026 comparison notes "receipt scanning unreliable in user reviews" and "receipt scanning only on iOS" (https://fango.fi/en/blog/best-food-waste-tracker-app/).
- (d) Yes. Inventory lists for freezer, fridge, and pantry with expiry reminders (App Store listing above).
- (c) Partial. "See what needs using first" is expiry-date ordering, not learned consumption cadence.
- (b), (e), (f): No. It has shopping lists, but they are user-built.

### BEEP
- (d) Yes, narrow. "Scan a barcode to add products and get reminders before they expire" for fridge, pantry, or storage (https://iphone.apkpure.com/app/beep-expiry-date-tracking/com.bgpworks.beep).
- (a) No — "No receipt scanning, no recipes — just expiry tracking" (https://fango.fi/en/blog/best-food-waste-tracker-app/).
- (c) No. Expiry dates are entered manually; there is no pattern model. (b), (e), (f): No.

### KitchenPal
- (d) Yes. Pantry/fridge/freezer manager with quantities and expiry dates, entered by barcode scan (4M+ product library) or by hand (https://play.google.com/store/apps/details?id=fr.icuisto.icuisto).
- (c) Partial. "Receive automated recommendations based on your pantry inventory tracker [recently finished, running low, frequently bought]" — inventory-state signals, not cadence learned from receipts (https://apps.apple.com/us/app/kitchenpal-shared-grocery-list/id1084982489).
- (f) Partial. "Create a new grocery list in seconds, based on an automated pantry check (never forget milk, eggs, etc)" (same listing). The list is composed from manually maintained inventory.
- (a) No receipt ingestion found. (b), (e): No.

### FridgeBuddy
- (a) Yes. "Import a grocery receipt from a photo or a PDF, then check the products before saving them" (https://AppAgg.com/ios/food-drink/pantry-inventory-fridgebuddy-34276298.html?hl=en). The check-before-saving step is a review-queue analog.
- (d) Yes. "On iOS 27, with a device that supports Apple Intelligence, photograph a fridge or pantry shelf to add several items at once." Pro also reads the printed expiration date with the camera (same source).
- (b) Partial. Receipts from any store can feed one inventory, but there is no cross-store purchase-history or spend model; it is an inventory, not a ledger.
- (c) Partial. Expiry reminders with suggested dates from USDA FoodKeeper storage times; no learned per-item consumption cadence or run-out prediction (https://apps.appfollow.io/ios/pantry-inventory-track-food/1500190823?country=us).
- (f) Partial. Items move from inventory to the shopping list and checked items move back into inventory in one step — a closed loop, but the user composes the list.
- (e) No. iOS-only. Food only.

### Pastro
- (a) Yes. "Photograph your receipt and every item lands in your pantry with its shelf life... AI reads every line item and adds price, category and shelf life" (https://pastro.app/).
- (d) Partial. The pantry is receipt-built; there is no fridge-scene photo correction.
- (c) Partial. Shelf-life estimates and expiry views; no learned cadence.
- (f) Partial (site claim). "Anything you run out of lands on the list your whole household shares" (same source).
- (b), (e): No.

### Duneed
- (a) Yes. "A pantry app that reads receipts instead of barcodes... Photograph the receipt and it becomes a list of what is in your kitchen, with what you paid for each thing" (https://duneed.app/).
- Review step present: "Nothing is filed behind your back. Rename an item, fix a price, drop a line you did not want — then save" (same source).
- (b) Partial. "A running total of what the month cost by category" across scanned receipts — spend aggregation, not a cadence model.
- (d) Partial (receipt-built pantry). (c) No — dates are user-set. (e) No. (f) No — the shared list is user-built and ticked off.

### Also found
- **The Pantry** (thepantry.app): receipt scans are a metered feature (3 trial scans free; 10/month on Plus) feeding a pantry inventory — the same receipt-to-pantry pattern as Pastro and Duneed (https://thepantry.app/).
- **Well Stockd**: a web app built on the same loop — pantry with amounts and estimated dates, reminder emails, and a shopping list minus what you have, sent to Walmart and Kroger carts after user check (vendor's own comparison page; treat as a vendor claim) (https://www.wellstockd.com/blog/samsung-food-alternative).

## Verdict

**The claimed edge is partially real. It is real as a combination. It is not real as any single feature.**

Taken feature by feature, everything is already shipped by someone:

- Any-store receipt ingestion is a commodity. Fetch, CoinOut, and Receipt Hog take any receipt today, and FridgeBuddy, Pastro, Duneed, and The Pantry turn receipt photos into pantry inventory. "Scan a receipt" is not a differentiator in 2026.
- The fridge-photo piece exists at two scales. Samsung Food's Vision AI identifies 40,000+ ingredients from a pantry or fridge photo, and its Family Hub fridges capture inventory with built-in cameras. FridgeBuddy adds several items from one shelf photo. "Eyes" is a real feature with real incumbents, not white space.
- Cross-retailer purchase history exists inside one wall. Instacart's Buy It Again spans hundreds of retailers, but only for orders placed through Instacart. Nobody imports a paper Costco receipt and a Walmart order into one model — that gap is real, but it is a gap of integration, not of technology.
- List help is everywhere; list *writing* is partial everywhere. KitchenPal composes a list from an automated pantry check, Pantry Check claims lists built from usage and inventory, and Pastro claims run-outs land on the list. All of them run on manually maintained (barcode) inventory or fixed rules, not on learned cadence from receipts.

Three parts of the claim survive contact with the market:

1. **Returns netting is unoccupied.** Column (e) is empty across all 16 products. Amazon and Walmart show return status for their own orders; no product subtracts a returned item from a purchase ledger, a consumption pattern, or a future list. This is the single cleanest white space in the set.
2. **Verified records are unoccupied as a user feature.** Arithmetic-checked decode with confidence and a review queue is not how any incumbent presents receipts. FridgeBuddy ("check the products before saving") and Duneed ("nothing is filed behind your back") have the review step, but neither claims total-arithmetic verification or per-line confidence. The rewards apps decode receipts opaquely and for advertisers, not for the user's ledger.
3. **Learned, all-category, cross-store cadence is unoccupied.** Pantry apps predict from expiry dates. Amazon predicts from user-set subscription intervals. Instacart predicts from its own order frequency. No product learns "you buy this every ~9 days at any store" across all categories — including non-food — and writes the next list from it. Caveat: our MVP is grocery-first, so the all-category part is currently a roadmap claim, not a shipped difference.

**Closest existing threat: FridgeBuddy.** It is the only product that already combines receipt import from photo or PDF, a check-before-saving review step, and fridge/pantry shelf-photo inventory in one app. **The feature that most overlaps is its receipt import: "Import a grocery receipt from a photo or a PDF, then check the products before saving them"** — that is our ingestion-plus-review-queue claim, shipped, on iOS. FridgeBuddy lacks cross-store history, cadence learning, returns, all-category coverage, and a self-writing list, and it is iOS-only — but it is one or two feature releases from overlapping most of the home-side story.

**Second threat: the receipt-to-pantry indie cluster (Pastro, Duneed, The Pantry, Well Stockd).** Four small products launched the same receipt → pantry → list loop. They validate the idea and crowd the exact demo narrative. None does returns, confidence scoring, arithmetic checks, or cadence-based list writing.

**Platform risk, stated plainly:** Samsung Food already owns photo inventory at platform scale, and Instacart already owns cross-retailer history inside its wall. Either could add receipt import or cadence in one release cycle. The defensible position for the hackathon is the *joint* claim — verified cross-store ledger + returns netting + learned cadence + photo-corrected inventory, in one loop — and the demo should show the two things nobody else shows: a return changing the ledger and the patterns, and a receipt whose totals are arithmetic-verified before a line is trusted.
