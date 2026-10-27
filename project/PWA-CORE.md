# PWA — core product surface (owner direction, 2026-10-27 13:53 EDT)

The PWA is the face of the CORE (receipts + double-check + patterns -> self-writing
list). It splits from the guidance PWA: core PWA ships right after the Stage 1-2 APIs;
the camera-overlay guidance UI stays with the enhancement track.

## Screens
1. **Home — Running low first.** Items predicted to run out soon (last purchase +
   typical interval + pack-size burn), each with an "around <date>" range, never fake
   precision. Below it: the current smart-list draft, one-tap confirm/edit/add.
2. **Scan.** Camera-first intake: receipt photo/PDF, cart photo (the double-check).
   Lands in the Review queue: unverified lines and receipt-vs-cart mismatches,
   one tap to confirm or fix — the trust moment, kept under 30 seconds per trip.
3. **Dashboard.** Spend by category over time (categories emerge from the data —
   produce, dairy & eggs, protein, pantry, household, non-food/gift cards kept honest:
   Uber Eats cards are not groceries), trip history, top items, returns total.
4. **Item / category detail.** Tap milk, eggs, any item, or a category chip:
   purchase timeline, cadence ("about every 9 days"), pack sizes, average price and
   price trend by store, predicted run-out, bought/returned history, controls:
   add to list now, snooze suggestion, never suggest.

## Honesty rules (product-wide doctrine, applied to UI)
- A pattern needs >=2 purchases before any cadence is claimed; otherwise the item
  shows "not enough history yet" — no invented predictions.
- Run-out dates are ranges with the reasoning visible ("last bought Oct 18, usually
  lasts ~10 days").
- Confidence is shown, not hidden: unverified items look unverified until confirmed.
- Returns appear in the ledger and in item history; a returned item leaves the
  suggestion pool unless the user re-adds it.

## Build mapping
APIs: Stage 1 decode (incl. returns + savings-folding) -> Stage 2 patterns,
reconciliation, smart list -> PWA-core (this doc) built with the impeccable
playbook, UX joy pass included -> enhancement: guidance UI after Spike 2.
