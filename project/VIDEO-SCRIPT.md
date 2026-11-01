# Hackathon demo video — script working doc

Status: FRESH START, 2026-11-01 (owner direction). Supersedes the
HeyGen 12-scene plan as the script basis; that package stays in
~/workspace/arya-qa/demo-video/ as raw material (recordings, clips,
stills are reusable).

## Hard rules (owner, 2026-11-01)

- Total runtime 3:00 MAX. Speed up long runs; judges cut at 3:00.
- Show ONLY features, code and functionality built during the event.
  No slides, no unbuilt ideas.
- A person presents it. Voiceover/subtitles included. AI elements
  and editing help are fine.
- WHY first (10-15 seconds only), then WHAT.

## WHY — owner's draft, claim-checked 2026-11-01

Owner's two strands: (1) grocery shopping is fragmented across apps
and stores are not designed to help you; (2) groceries matter —
food is core, it's a chore, it's personal, and your own purchase
data is an untapped mirror of your habits.

Verdicts:
- Fragmentation (Notes / WhatsApp / list apps / receipt apps /
  budget apps / per-retailer apps): TRUE, keep. Add: per-store apps
  only work for that one chain; independent and local stores have
  nothing.
- "Stores don't want you on an optimized route": DIRECTIONALLY TRUE
  but soften the intent. Documented version: layouts are designed
  to maximize exposure and basket size — retail trade guides
  literally advise putting essentials at the back so shoppers walk
  past everything else. Say "the store is designed for the store's
  basket, not your time." Don't say stores hide items.
- Impulse/unplanned share: CONTESTED — do NOT cite a number.
  Underhill/industry studies say 60-70% unplanned; Inman & Winer
  (30k purchases) found 68% on major trips; Bell et al. (Wharton)
  argue ~20% and call the big figure an urban legend.
- Time cost: SAFE. ~41-47 min per trip, ~1.6 trips/week,
  roughly 55-60 hours a year (Time Use Institute figures).
- Choice overload: SAFE. Average US supermarket carries ~30,000+
  products (industry counts ~31,800 SKUs).
- Why groceries: personal need + "groceries decide what we eat"
  is first-person framing — unimpeachable, keep as the emotional
  core. "For most people it's a chore" is fine as opinion in the
  presenter's voice, not as a stat.

## WHY angles the draft is MISSING

1. The forgotten item: the return trip for the one thing you went
   for. Lists are written from memory, in the kitchen, by guessing.
2. Duplicates: buying what is already in the fridge -> food waste.
   No shared picture of what the home already has.
3. Stockouts found too late: you learn the item is gone standing
   in front of the empty shelf, mid-trip.
4. Two shoppers, no sync: both buy milk, nobody buys eggs. The
   list lives in one person's head or one app.
5. No price memory: nobody remembers what they paid last time or
   which store is cheaper for what — receipts could say, and are
   thrown away.
6. THE BRIDGE (strongest): the one document that already records
   what your household actually buys and eats is the receipt —
   and we throw it away. Every other WHY above is a data problem
   whose data already exists on paper.

## Opening hook candidates

A. THE RECEIPT (recommended): presenter holds a receipt.
   "This knows what my household actually buys and eats. We
   throw it away." Unique to Arya — no competitor can open here.
B. TIME: "About 60 hours a year pushing a cart, for an errand
   that decides what we eat." Strong stat, generic.
C. FRAGMENTATION MONTAGE: fast cuts — Notes, WhatsApp, list app,
   budget app, store app. "Five apps, and the list still isn't
   right." Visual, energetic.
D. THE FORGOTTEN ITEM: "Drove home. Forgot the one thing I went
   for." Micro-pain, very relatable, small stakes.
E. STORE DESIGN: "The store knows where everything is. It's
   designed so you take the long way." Punchy; keep the softened
   framing.
F. WASTE: fridge cleanout. "Threw away food this morning. Bought
   two of them again yesterday." Ties to expiry; mid-film beat
   more than an opener.

## Proposed WHY lock (~15s, ~40 words)

"Groceries run on scraps of paper and five different apps — and
the store is designed for its basket, not your time. This receipt
knows what my household actually buys and eats. We throw it away.
I built the thing that reads it."

## Next rounds (not yet locked)

- WHAT: feature selection for the remaining ~2:45. Candidates
  from last night's catches: list intelligence, stock warnings,
  Quest hunt, shelf report, receipt finish/score, price comparison,
  expiry/use-soon, share cards, Meta stack card. Not all fit —
  cutting is the work.
- Presenter: owner live on camera vs his digital twin.
- Tone: Quest-playful vs earnest; the WHY above leans earnest,
  the WHAT can carry the play.

## Owner's real data — the origin story (verified 2026-11-01)

Owner's point: he did NOT have his receipts; he had thrown them
away. He downloaded real receipts from the Costco app and tested
Arya on those. Spark verified the numbers against the preserved
snapshot of that corpus (114 receipts, 2023-10-25 to 2026-10-26,
$13,486.72 total, 11 different Costcos — Fremont 36, Sunnyvale 34,
Newark 23, others 21).

Top staples by trips: Kirkland egg whites in 35 of 114 receipts
($452), organic spinach 30, pasture eggs 25, Greek yogurt 18,
berries 16-18. The app surfaced his habits back to him.

ALMOND FLOUR — same SKU (1178969), same 3 lb bag, 7 purchases:
$9.99 Cypress (2023-12) / $11.89 Fremont + Newark (2025) /
$13.59 NE San Jose + Newark (2026-07, 2026-09) /
$16.49 Newark (2026-10-22) / $16.99 Pentagon City (2026-10-26).
A $9.99-$16.99 spread on an identical bag. Honesty nuance: the
spread is part time (prices rose over 3 years), part place
(same-month store variance is real: $16.49 vs $16.99 in one week).
Script line should say "at one Costco... at another," not claim
same-day arbitrage.

Placement: this is the BRIDGE, right after the WHY (~0:15-0:40).
It proves the receipt premise on real data before the WHAT starts.

Proposed beat (~24s, 59 words):
"I didn't have my receipts — I'd thrown them away, like everyone.
So I downloaded 114 from the Costco app and fed them to Arya. It
knew my habits cold: egg whites in 35 of 114 trips. And the same
bag of almond flour — $13.59 at one Costco, $16.99 at another.
I'd paid both, happily, for years."

Naming Costco: recommend YES in narration — it is factual personal
backstory (nominative use), and specificity is what makes it
believable. The standing no-Costco rule governs the in-app DEMO
data (fictional stores), not the owner's true story. Owner's call.

## WHY script — draft v1 (owner review, 2026-11-01)

Target: 30 seconds, plain spoken language, no polish/drama.
78 words ≈ 31s at a normal speaking pace.

"Grocery shopping takes up more of my week than it should. My
list is in one app, my wife's is in another, and the receipts
end up in the trash. The store doesn't help — it's laid out to
sell, not to save me time. And I had no idea what we actually
buy, or what we pay for it. I didn't even keep my receipts. I
had to download them from the Costco app just to find out."

Hands off to the bridge beat: "So I fed them to Arya..." —
almond flour + top staples live there.
