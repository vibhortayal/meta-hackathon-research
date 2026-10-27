# Vision — a grocery assistant, not a list manager (owner, 2026-10-27)

## The product in one sentence
An assistant that keeps a living model of your grocery world — what you have, where
it is, what state it's in, what's coming, what's wasting, what it costs — by blending
the physical world (fridge, pantry, cart, store) with software (purchases, patterns,
plans), so you always have holistic visibility into your groceries.

## Scope of the model: the WHOLE receipt (v12)
Every purchase counts — food, household consumables, clothing, electronics, gift
cards. Categories are peers; patterns apply to anything bought more than once
(batteries every ~2 months is a pattern, like milk every ~9 days). Food is the
deep-focus domain (perishable, visible in the fridge, guided in the store); other
categories get their own lifecycle behaviors (return/warranty windows for
electronics, sizes for clothing, restock cadence for consumables).

## The model: every item has a lifecycle, the app can see all of it
planned -> bought -> verified (cart) -> stored (fridge/pantry/freezer) -> seen (Eyes)
-> used / expired / returned. The LIST is one view of this model. Patterns, budgets,
expiry, and guidance are other views of the same truth.

## Sensors and actuators
Sensors: receipts (bought), cart photo (verified), Eyes photos (have), date snaps
(expiry), walkthroughs (the store), the user's one-tap corrections (ground truth).
Actuators: the self-writing list, running-low and expiry reminders, in-store
guidance, spend visibility, waste feedback that changes future suggestions.

## Questions the assistant answers at maturity
- "Do we have eggs?" — from the model, with evidence ("seen in fridge photo Tue,
  6 left of 12 bought Oct 22").
- "What's about to die?" — expiry view across fridge and pantry.
- "What did groceries really cost this month?" — net of returns, gift cards and
  non-food kept honest.
- "What do we actually eat, and what do we waste?" — consumption truth, not
  purchase truth.
- "What should dinner be?" — inventory-aware, from what needs using first
  (the bridge to his recipe world).

## Why groceries are the starting point
Food is the most frequent, most physical, most recurring flow in a household —
the natural first domain for an assistant that manages the physical world with
software. Grocery visibility -> household visibility -> daily-life assistance.
That trajectory is the pitch. The BUILD stays groceries, done deeply.

## Architectural consequence
Inventory-first data model: items and their lifecycle states are the core objects;
list, dashboard, patterns, and reminders are derived views. Never-guess applies at
every state transition — a state the sensors haven't established is "unknown,"
shown as unknown, and the app asks rather than assumes.
