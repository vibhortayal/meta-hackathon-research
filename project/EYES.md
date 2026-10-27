# Eyes of the app — visual inventory + expiry (owner, 2026-10-27)

## The three sensors
1. Receipts — what you bought (verified by arithmetic).
2. Cart photo — what actually left the store with you (double-check).
3. Fridge/pantry/freezer/fruit photos — what you still HAVE. Ground truth for the
   consumption model; corrects "running low" the way "Not here" corrects the store map.

Inventory = bought - returned - consumed - expired. Photos correct the estimate;
corrections are one-tap, and unseen items stay "unknown," never assumed.

## Expiry engine
- Priors: average shelf life per category (leafy greens days, milk ~a week, eggs weeks).
- Printed dates: at put-away, the app prompts for a close-up of the best-before date on
  the few high-risk items in this trip ("before it goes in the fridge — snap the date").
- Learning: every "this expired" report retunes that item's model for THIS household;
  repeated waste changes the suggestion (smaller pack, lower quantity, buy later).
- Reminders fire before predicted expiry, phrased as a check, not a fact:
  "Spinach from Oct 24 usually turns about now — still good?"

## Hackathon scope
IN: single-photo inventory check (fridge or pantry) with confirm/correct checklist;
put-away date capture for top perishables; expiry nudges from priors + sightings.
The demo beat: the app sees the spinach bag in the fridge photo and takes spinach
OFF the list it just wrote.
LATER: video walkthrough inventory, automatic multi-photo stitching, quantity
estimation beyond rough levels (full / some / low / out as seen).
