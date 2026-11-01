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

## WHY timing decision + draft v2 (2026-11-01)

Owner verdict on v1: doesn't land. Missing: the full fragmented
experience, the store-data gap (per-chain apps; most stores show
nothing), and humans-helping-humans (community).

Spark recommendation, owner to confirm: WHY gets 45 seconds, in
two beats — problem ~30s, turn ~15s (receipt + community). WHAT
then runs ~0:45-2:40, close ~20s. Past 45s of WHY, the Demo
score (25%) starves; under 30s, the Impact story (30%) has no
room to land.

WHY draft v2 (~45s, plain spoken):

"Grocery shopping is scattered. My list is in my notes, my
wife's list comes over text, the receipts go in the trash, and
the budget lives in another app. Every big store has its own
app, and it only covers that store. The store down the street
shows nothing — no prices, no stock, no way to find anything.
And the store is laid out to sell, not to save me time. The
people around me know that store — what's out, what moved,
what it costs. That knowledge walks out the door with them.
I lived all of this. I didn't even keep my receipts — I had
to download them from the Costco app to see what I was
actually buying."

## WHY draft v3 (2026-11-01) — simple spoken, no polish

Owner: v2 still sounded written ("I lived all of this"). v3 is
plain talk, short sentences, no crafted lines. 122 words,
~50s spoken; to hit 45s cut the budget line and the last
community clause.

"Grocery shopping is all over the place. My list is in my
notes. My wife sends hers on WhatsApp. I throw the receipts
away. The budget is in another app. Every big store has its
own app, and it only works for that store. The small store
near my house has nothing — you can't check a price, you
can't check stock. And the store is made to sell you more,
not to get you out faster. The people shopping there know
the store — what's finished, what moved, what's cheaper
somewhere else. But that stays with them. I had the same
problem. I didn't have one receipt saved. I had to download
them from the Costco app to see what I actually buy."

## WHY draft v4 (2026-11-01) — adds "why grocery" (Bring Your World)

Owner: judges must understand the problem; the "Bring Your
World" track means the domain stakes must be explicit — grocery
is your world: home, family food, weekly money, your store,
your neighbors. v3 never said why grocery matters. Insert at
the top, plain spoken. Full script now ~170 words, ~1:05-1:10;
trade: WHAT gets ~1:55, fine if the journey is sped up.

"Groceries are a big part of life. It is the food we eat at
home, what we feed our family. We spend a lot of money on it,
every week. And one store has thousands of things in it —
nobody can keep track of all that in their head. But the way
we manage it is all over the place. My list is in my notes.
My wife sends hers on WhatsApp. I throw the receipts away.
Every big store has its own app, and it only works for that
store. The small store near my house has nothing — you can't
check a price, you can't check stock. And the store is made
to sell you more, not to get you out faster. The people
shopping there know the store — what's finished, what moved,
what's cheaper somewhere else. But that stays with them. I
had the same problem. I didn't have one receipt saved. I had
to download them from the Costco app to see what I actually
buy."

## WHY v5 — beat structure (owner direction, 2026-11-01)

Owner restructured the WHY into named beats. Two beats, then
the personal bridge into the WHAT.

BEAT 1 — WHY GROCERY MANAGEMENT (~40s)
"Groceries are a big part of life. It is the food we eat at
home, what we feed our family. We spend a lot of money on it,
every week. But the way we manage it is all over the place.
My list is in my notes. My wife sends hers on WhatsApp. I
throw the receipts away. Every big store has its own app,
and it only works for that store. The small store near my
house has nothing — you can't check a price, you can't check
stock. And the store is made to sell you more, not to get
you out faster."

BEAT 2 — WHY COMMUNITY (~30s)
"So why community? Because no store is going to fix this.
One store will never tell you the price in another store.
And stock changes every day — something is finished,
something moved. The only people who know are the people
who shop there. We already help each other in the store.
Somebody asks, where is this, and somebody answers. That
help just goes nowhere today. If shoppers share what they
see, everybody's trip gets easier."

BRIDGE (personal, ~10s, into the WHAT)
"I had the same problem. I didn't have one receipt saved.
I had to download them from the Costco app to see what I
actually buy."

Running total: WHY ~1:10 + bridge ~0:10. WHAT gets ~1:40.

## WHY v6 — tightened (owner ask, 2026-11-01)

Same beats, ~164 words total (~1:05 with bridge). Cuts: merged
the stakes lines, dropped "all over the place" (the next three
lines show it), shortened community logic. No point removed.

BEAT 1 — WHY GROCERY MANAGEMENT (~33s)
"Groceries are a big part of life. It's the food we eat at
home, what we feed our family, and we spend a lot on it every
week. My list is in my notes. My wife sends hers on WhatsApp.
I throw the receipts away. Every big store has its own app,
only for that store. The small store near my house has
nothing — no prices, no stock. And the store is made to sell
you more, not to get you out faster."

BEAT 2 — WHY COMMUNITY (~24s)
"Why community? Because no store will fix this. A store will
never tell you another store's price. Stock changes every
day — things finish, things move. Only the people shopping
there know. And we already help each other. Somebody asks
where something is, somebody answers. Today that help goes
nowhere. If shoppers shared what they see, every trip gets
easier."

BRIDGE (~9s)
"I had the same problem. Not one receipt saved. I had to
download them from the Costco app to see what I actually buy."

## WHY v7 — fragmentation collapsed to one line (owner, 2026-11-01)

The three example lines (my notes / wife's WhatsApp / receipts
in the trash) become ONE universal line — judges see themselves,
not just his household. Receipts now live only in the bridge.

Beat 1 line: "We all manage it in our own way — notes, texts,
apps — and none of it connects."
Alt phrasing: "We all do it differently, and none of it talks
to each other."

BEAT 1 v7 (~31s): "Groceries are a big part of life. It's the
food we eat at home, what we feed our family, and we spend a
lot on it every week. We all manage it in our own way — notes,
texts, apps — and none of it connects. Every big store has its
own app, only for that store. The small store near my house has
nothing — no prices, no stock. And the store is made to sell
you more, not to get you out faster."

## Status 2026-11-01: Beat 1 LOCKED (v7). Beat 2 tightened (v8)

BEAT 2 v8 (~22s, 55 words): "Why community? Because no store
will fix this. A store won't tell you another store's price.
Things change every day — items finish, items move. Only the
people in the store know. And we already help each other —
someone asks, someone answers. That help goes nowhere. If we
shared what we see, every trip gets easier."

Only remaining cut available: the "someone asks, someone
answers" texture line (~2s) — kept for spoken life.

## Segue fix (owner catch, 2026-11-01): Beat 1 never mentions people

Beat 2's "Why community?" came from nowhere — Beat 1 ends on
stores, Beat 2 opens on community. Two options, pending pick:

OPTION A (one line appended to Beat 1, nothing else moves):
Beat 1 ends "...not to get you out faster. Most days, the only
help you get in a store is another shopper." Beat 2 unchanged.

OPTION B (recommended — move the texture to Beat 1's end):
Beat 1 ends: "...not to get you out faster. And we already
help each other there — someone asks, someone answers. That
help just goes nowhere."
Beat 2 becomes pure logic (~18s): "Why community? Because no
store will fix this. A store won't tell you another store's
price. Things change every day — items finish, items move.
Only the people in the store know. If we shared what we see,
every trip gets easier."

## WHY — CURRENT LOCKED TEXT (v9, 2026-11-01)

Owner picked segue Option B. Also added (owner catch): food
waste and spend blindness — the personal cost of no memory.
Both sit in Beat 1, right after "none of it connects."

BEAT 1 — WHY GROCERY MANAGEMENT (~41s)
"Groceries are a big part of life. It's the food we eat at
home, what we feed our family, and we spend a lot on it every
week. We all manage it in our own way — notes, texts, apps —
and none of it connects. So food expires in the fridge, and
money goes out every week and nobody knows on what. Every
big store has its own app, only for that store. The small
store near my house has nothing — no prices, no stock. And
the store is made to sell you more, not to get you out
faster. And we already help each other there — someone asks,
someone answers. That help just goes nowhere."

BEAT 2 — WHY COMMUNITY (~18s)
"Why community? Because no store will fix this. A store
won't tell you another store's price. Things change every
day — items finish, items move. Only the people in the store
know. If we shared what we see, every trip gets easier."

BRIDGE (~9s)
"I had the same problem. Not one receipt saved. I had to
download them from the Costco app to see what I actually
buy."

WHY total ~1:08. WHAT gets ~1:50, close ~0:15-0:20.

## Price-comparison provenance (owner question, verified 2026-11-01)

Owner asked: did the app point out cheaper items from his OWN
data alone? Answer: the almond flour case — yes, 100% his own
receipts (same SKU, his purchases only; no other household's
data was ever in his account). Own-receipt comparison catches
any item he bought at 2+ stores.
The "cheaper elsewhere / 30 neighbors bought it" cards are the
DEMO TOWN's community layer — the same trick widened with all
shoppers' receipts (stores/items he never bought). Script rule:
personal beat says "my receipts showed me" (true); community
beat promises the wider version (true to design + demo).
