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

## Beat 1 gap audit vs live features (2026-11-01)

Checked against the LIVE app copy (landing cards + in-app
Guide cards, assistant/web/src/i18n/en.json @ 016da64).
Landing/guide feature set: per-store learning lists, household
sync, store maps (by shoppers), store news, receipts/spend,
cheaper-elsewhere, use-soon, Ask Arya, running-low prediction,
Quest, hauls/friends.

Covered in Beat 1/2: stakes, fragmentation, waste/expiry,
spend blindness, app silos, no-data small stores, store
design, community help, stock/price knowledge (Beat 2).

MISSING pains (feature exists, its pain is unnamed):
1. RUNNING OUT / LIST FROM MEMORY — guide "Never run out",
   landing "milk is on the list before you run out". Arya's
   CORE pain, currently unsold. Proposed line (merge into the
   consequences sentence): "So food goes bad in the fridge,
   things run out before you notice, and money goes out and
   nobody knows on what."
2. FINDING THINGS IN-STORE — guide maps card: "No more
   doubling back for the eggs". Beat 1 has store design but
   not the hunt. Proposed line after store design: "You walk
   up and down, and you still miss things."
3. HOUSEHOLD DUPLICATION — guide share card (sync, split up).
   v7 generalized this away. Proposed: fold into the
   fragmentation line — "...and none of it connects. Two
   people buy the same milk, and nobody buys the eggs."
4. (Small, bridge not Beat 1) RETURNS/RECALLS — receipts card:
   "kept for returns and recall refunds". Optional half-line
   in the bridge: "...not one receipt saved — nothing to
   return with either."

v10 Beat 1 with 1-3 lands ~47s. Pending owner's pick.

## Beat 1 v10 — owner's line rewrites (2026-11-01)

Owner killed two lines and rewrote them from real life:
- "Two people buy the same milk..." -> OUT. Instead: list
  building as it really happens — from memory, or scouting
  the house and fridge before you go.
- "we spend a lot" -> money AND time.
- "We already help each other — someone asks, someone
  answers" -> OUT. Real texture: you run into friends and
  neighbors in the store and compare notes — hauls, what you
  didn't find, what's good, which store for what. (This also
  foreshadows Arya's actual community features: haul shares,
  stock reports, price comparisons, store preferences.)

BEAT 1 v10 (~1:05-1:10 as written; trims noted in chat)
"Groceries are a big part of life. It's the food we eat at
home, what we feed our family, and we spend a lot of money
and a lot of time on it, every week. We all manage it in our
own way — notes, texts, apps — and none of it connects. We
make our lists from memory, or by walking around the house
and checking the fridge. So food goes bad in the fridge,
things run out before you notice, and money goes out and
nobody knows on what. Every big store has its own app, only
for that store. The small store near my house has nothing —
no prices, no stock. And the store is made to sell you more,
not to get you out faster. You walk up and down, and you
still miss things. And we run into friends and neighbors in
the store. We talk about our hauls, what we didn't find,
what's good, which store is better for what. That talk just
stays in the store."

## Beat 1 closing line — replacements (owner: "stays in the store" doesn't land)

1. (recommended) "And then we go home, and it's gone."
2. "That talk goes nowhere."
3. "Nobody writes it down, so it only helps the two people
   standing there."
Pending owner pick.

## Beat 2 rework (owner clarification, 2026-11-01)

Owner: "why community" was his direction TO Spark about what
the script must cover — NOT a line to say out loud. Beat labels
are internal scaffolding, never narration. Beat 2 now opens
with its thesis as a plain statement.

BEAT 2 (current, ~20s): "The only people who know a store are
the people who shop in it. A store won't tell you another
store's price. Things change every day — items finish, items
move — and only shoppers see it. If we shared what we see,
every trip gets easier."

## Advisor check (2026-11-01): have we answered "why built / trying to solve"?

Problem: YES (Beat 1). Stakes: YES (food, family, money,
time). Why community as the approach: YES (Beat 2 logic).
MISSING: the capstone sentence — nowhere does the script say
what he built and what it is for. The bridge ends on the
Costco anecdote and the film would jump to footage; judges
must assemble the intent themselves.

CAPSTONE (proposed, after the bridge, ~12s): "So that's what
I built. Arya learns from your receipts, and it holds what
shoppers share, so you don't start from zero every week."
Then the WHAT proves it, beat by beat.

## Bridge rework (owner, 2026-11-01)

Owner: remove "Not one receipt saved". The bridge's job is
to prove Arya was built during the hackathon: he needed data
to test, didn't have enough receipts saved, so he downloaded
them from his Costco app.

BRIDGE v2 (~12s): "I built Arya during this hackathon. I
needed data to test it, and I didn't have enough receipts
saved. So I downloaded my receipts from the Costco app —
114 of them, three years of my own shopping."

Capstone trimmed to match (bridge now carries "I built", so
the capstone no longer repeats it): "Arya learns from your
receipts, and it holds what shoppers share, so you don't
start from zero every week."

## Beat 2 opener rework (owner, 2026-11-01)

Owner killed "The only people who know a store are the people
who shop in it." His version of the idea: you learn a store
slowly, over time, by shopping there — and when you move
cities or change stores, you relearn from zero.

BEAT 2 (current, ~26s): "You learn a store over time. Month
after month of shopping there — where things are, what's
good, what it costs. Then you move to a new city, or you
change stores, and you start from zero again. A store won't
tell you another store's price. Things change every day —
items finish, items move — and only the people shopping
there see it. If we shared what we see, every trip gets
easier."

## Beat 2 tightened hard (owner, 2026-11-01)

Owner: Beat 2 too long; he likes the "if we could share what
we see" ending. Cut the middle (store price silence + daily
change now implied by the closing trio). ~17s, was ~26s.

BEAT 2 (current): "You learn a store over months of shopping
there. Move to a new city, or change stores, and you start
from zero. If we could share what we see — where things are,
what's good, what's cheaper — nobody starts from zero."

WHY running total back to ~1:50.

## ===== CURRENT FULL SCRIPT (assembled 2026-11-01, owner-reviewed) =====

BEAT 1 (~1:10)
"Groceries are a big part of life. It's the food we eat at
home, what we feed our family, and we spend a lot of money
and a lot of time on it, every week. We all manage it in our
own way — notes, texts, apps — and none of it connects. We
make our lists from memory, or by walking around the house
and checking the fridge. So food goes bad in the fridge,
things run out before you notice, and money goes out and
nobody knows on what. Every big store has its own app, only
for that store. The small store near my house has nothing —
no prices, no stock. And the store is made to sell you more,
not to get you out faster. You walk up and down, and you
still miss things. And we run into friends and neighbors in
the store. We talk about our hauls, what we didn't find,
what's good, which store is better for what. And then we go
home, and it's gone."

BEAT 2 (~0:17)
"You learn a store over months of shopping there. Move to a
new city, or change stores, and you start from zero. If we
could share what we see — where things are, what's good,
what's cheaper — nobody starts from zero."

BRIDGE (~0:15)
"I built Arya during this hackathon. I needed data to test
it, and I didn't have enough receipts saved. So I downloaded
my receipts from the Costco app — 114 of them, three years
of my own shopping."

CAPSTONE (~0:08)
"Arya learns from your receipts, and it holds what shoppers
share, so you don't start from zero every week."

THE WHAT — outline only, ~1:10 available, NOT yet scripted:
proof from the 114 receipts (egg whites 35/114; almond flour
$13.59 vs $16.99) ~12s; one trip sped up (list ready, stock
warning, hunt, empty-shelf report, receipt finish) ~40s;
Meta stack card 3s; close + end card ~8s.

Open micro-items: Beat 1 closing line shows option 1 ("and
it's gone") — owner never explicitly confirmed vs options
2/3. WHY total ~1:50 at ~150wpm (estimate; timed read still
pending). Lock-vs-further-trim: owner's call.

## ===== CURRENT FULL SCRIPT v2 (2026-11-01, gap-fix + tighten pass) =====

Supersedes the assembly above. Changes: WHAT written (was
outline — the biggest gap); bridge tightened; small trims in
Beat 1; "Move cities" tightened in Beat 2. Plain spoken
throughout. Total ~2:55 at ~150wpm.

BEAT 1 (~1:06)
"Groceries are a big part of life. It's the food we eat at
home, what we feed our family, and we spend a lot of money
and a lot of time on it, every week. We all manage it in our
own way — notes, texts, apps — and none of it connects. We
make our lists from memory, or by walking around the house
and checking the fridge. So food goes bad in the fridge,
things run out before you notice, and money goes out and
nobody knows on what. The big stores have their own apps,
one for each store. The small store near my house has
nothing — no prices, no stock. And the store is made to sell
you more, not to get you out faster. You walk up and down,
and you still miss things. In the store, we run into friends
and neighbors, and we compare notes — our hauls, what we
didn't find, what's good, which store is better for what.
And then we go home, and it's gone."

BEAT 2 (~0:16)
"You learn a store over months of shopping there. Move
cities, or change stores, and you start from zero. If we
could share what we see — where things are, what's good,
what's cheaper — nobody starts from zero."

BRIDGE (~0:13)
"I built Arya during this hackathon. To test it I needed
receipts, and I didn't have enough saved. So I downloaded
my receipts from the Costco app — 114 of them, three years
of my own shopping."

CAPSTONE (~0:08)
"Arya learns from your receipts, and it holds what shoppers
share, so you don't start from zero every week."

THE WHAT — proof (~0:16)
"I fed it the 114 receipts. It read every line. Egg whites,
in 35 of those 114 trips — I had no idea. And the same
almond flour was $13.59 at one Costco and $16.99 at another.
I had paid both."

THE WHAT — one trip (~0:32, over sped-up footage)
"Now this is a normal trip. Before I go, Arya tells me the
hummus is out at my store — three neighbors reported it. The
list is already made, from what we buy. In the store, it
walks me from item to item. This one is not here, so I
report the empty shelf. That helps the next shopper. At the
end, I take a photo of the receipt. The trip is done — and
next week's list is already learning."

THE WHAT — at home (~0:12, over Today footage)
"At home, it keeps watching. The eggs are cheaper at the
other store, and it tells me. The spinach will go bad soon,
and it tells me to use it first."

CLOSE (~0:12, Meta stack card on screen 3s)
"All of this runs on Meta's models. The AI does the
remembering. We do the shopping, and we help each other.
This is Arya."
End card: "Arya — the list that writes itself · Team
Nightshift · Built on Meta Muse models"

## Script v3 — Meta models shown IN the walkthrough (owner, 2026-11-01)

Owner direction: as we walk through the app, show where each
Meta model is used, explain the model choices, and cover the
other Meta products. Method: on-screen TAGS at each moment do
most of the work; narration carries only the three choices
worth saying out loud (Wonder for receipts, SAM+Spark double
check, math in code). Full stack card stays at the close.

MODEL MAP (moment -> product -> why chosen):
- Receipt photo decode -> Muse Wonder (primary). Tested on
  real receipts: 97/98 lines, 0 price errors vs Spark 92/98
  with 4. A wrong price is worse than a slow answer. Spark is
  the automatic fallback; low-confidence lines go to review.
- Paper-list photos, order text, receipt PDFs, Ask Arya,
  staple judge, shelf labels -> Muse Spark 1.3 Standard.
  The workhorse: cheap and fast at volume.
- Voice (list mic, Ask mic) -> Muse Voice Transcribe.
- Shelf camera (Find it for me, Shelf Scan) -> SAM 3.1 boxes
  candidates, Muse Spark verifies each crop. Two models, so
  a highlight is never a guess.
- Store mapping -> SAM 3.1 segments shelves + finds people to
  blur; Spark labels; VGGT (Meta AI research, not on the
  event list) builds geometry — supporting, not leading.
- "Where am I?" localizer -> authored by Muse Wonder, runs
  locally, no API call.
- Celebration characters -> Muse Image (generated once,
  shipped as assets).
- All server calls -> Meta Model API (one client, daily
  spend ceiling). Math (money, dates, patterns) = plain code.
- NOT claimed: Muse Spark Open, Muse Glimmer (not run),
  Muse Code (not used).

PROOF v3 (~0:22): "I fed it the 114 receipts. Muse Wonder
reads the receipt photos. We tested the models on real
receipts first — Wonder read them best, no price errors, and
a wrong price is worse than a slow answer. It found egg
whites in 35 of those 114 trips. And the same almond flour,
$13.59 at one Costco, $16.99 at another."

ONE TRIP v3 (~0:40): "Now a normal trip. The list is already
made, from what we buy. I add to it by typing, by voice —
Muse Voice Transcribe — or a photo of the list. Before I go,
Arya warns me the hummus is out — three neighbors reported
it. In the store, it walks me item to item. I point the
camera at a shelf, SAM 3.1 finds the item, Spark checks it —
two models, never a guess. This shelf is empty, so I report
it for the next shopper. A photo of the receipt ends the
trip, and next week's list is already learning."

CLOSE v3 (~0:12): "The math is plain code — no model touches
your money. The AI does the remembering. We do the shopping,
and we help each other. This is Arya." (Stack card on screen:
Spark / Wonder / SAM 3.1 / Voice Transcribe / Muse Image /
Meta Model API.)

TIMING: v3 totals ~3:05 — ~5s over. Trim candidates if he
wants it under: Beat 1 "You walk up and down, and you still
miss things" (-4s).

## ===== CURRENT FULL SCRIPT v3 (assembled 2026-11-01) =====

WHY and WHAT together. On-screen model tags ride the footage
(receipt photo -> Wonder; list/Ask -> Spark; voice -> Voice
Transcribe; shelf camera -> SAM 3.1 + Spark; characters ->
Muse Image; all via Meta Model API). Runtime estimate ~3:04
at ~150wpm (Beat 2 cut 2026-11-01) — under the cap.

BEAT 1 (~1:06)
"Groceries are a big part of life. It's the food we eat at
home, what we feed our family, and we spend a lot of money
and a lot of time on it, every week. We all manage it in our
own way — notes, texts, apps — and none of it connects. We
make our lists from memory, or by walking around the house
and checking the fridge. So food goes bad in the fridge,
things run out before you notice, and money goes out and
nobody knows on what. The big stores have their own apps,
one for each store. The small store near my house has
nothing — no prices, no stock. And the store is made to sell
you more, not to get you out faster. You walk up and down,
and you still miss things. We discuss stores, products and prices with our
friends. If we could all
share what we see — where things are, what's good, what's
cheaper — nobody starts from zero."

BRIDGE (~0:13)
"I built Arya during this hackathon. To test it I needed
receipts, and I didn't have enough saved. So I downloaded
my receipts from the Costco app — 114 of them, three years
of my own shopping."

CAPSTONE (~0:08)
"Arya learns from my receipts, and it holds what I share,
so I don't start from zero every week."

PROOF (~0:22)
"I fed it the 114 receipts. Muse Wonder reads the receipt
photos. We tested the models on real receipts first — Wonder
read them best, no price errors, and a wrong price is worse
than a slow answer. It found egg whites in 35 of those 114
trips. And the same almond flour, $13.59 at one Costco,
$16.99 at another."

ONE TRIP (~0:40)
"Now a normal trip. The list is already made, from what we
buy. I add to it by typing, by voice — Muse Voice Transcribe
— or a photo of the list. In the store,
it walks me item to item. I point the camera at a shelf, SAM
3.1 finds the item, Spark checks it — two models, never a
guess. This shelf is empty, so I report it for the next
shopper. A photo of the receipt ends the trip, and next
week's list is already learning."

AT HOME (~0:11)
"At home, it keeps watching. The spinach will go bad soon,
and it tells me to use it first. I finish the yogurt, I tell
Arya we're out, and it's on the list."

LIMITS (~0:29)
"Honest limits: eight days is not enough for Arya to learn
every store — the data just isn't there yet. And Arya
depends on its community: a store nobody shops stays
unknown. This is an incredibly hard problem. Every store is
different, and everything in it moves. So I built feedback
in everywhere. As I use it, as my friends use it, as you use
it, it gets better — and I will keep fixing and adding,
based on that feedback."

CLOSE (~0:12; Meta stack card on screen 3s)
"The math is plain code — no model touches your money. The
AI does the remembering. We do the shopping, and we help
each other. This is Arya."
End card: "Arya — learns how we shop, helps us help each
other · Team Nightshift · Built on Meta Muse models"

## Yogurt beat (owner, 2026-11-01)

Owner wants a yogurt reference: running out of yogurt and it
going on the list. Grounded in his real data — Greek yogurt
is in 18 of his 114 receipts — and a real feature (Guide,
Running low card: say "we finished the yogurt" and Arya adds
it to the right store's list). Goes in AT HOME:

AT HOME v3 (~0:16): "At home, it keeps watching. The eggs
are cheaper at the other store, and it tells me. The spinach
will go bad soon, and it tells me to use it first. I finish
the yogurt, I tell Arya we're out, and it's on the list."

Adds ~4s; the pending Beat 1 trim ("You walk up and down...")
covers it. NOTE: owner called this a subtle hint to "the
Alexander Wang yogurt" — Spark could not pin that reference
(only the 2014 Wang fro-yo truck, black-and-white, "Eat Me").
Kept as a plain yogurt moment pending his steer.

## Beat 1 amendment v3.1 (owner, 2026-11-01)

Owner cut the in-store friends passage. OLD: "In the store,
we run into friends and neighbors, and we compare notes —
our hauls, what we didn't find, what's good, which store is
better for what. And then we go home, and it's gone."
NEW: "We discuss stores, products and prices with our
friends — what's good, what's cheaper, which store is better
for what. And then we go home, and it's gone."
Slightly shorter (~-3s): total now ~3:02. The remaining
overage trim is now optional — the "You walk up and down"
line, or leave for the timed read to judge.

## Beat 2 CUT (owner, 2026-11-01)

Owner: Beat 2 ("You learn a store over months...") is not
needed — removed from the assembled script. Its two ideas
survive elsewhere: sharing lives in Beat 1's friends line +
the capstone ("it holds what shoppers share"); starting from
zero lives in the capstone ("so you don't start from zero
every week"). Runtime now ~2:46 — under the 3:00 cap with
~14s headroom; the Beat 1 trim is no longer needed.

## Beat 1 ending (owner, 2026-11-01)

Owner moved Beat 2's closing line to end Beat 1 (with "all"
added): "If we could all share what we see — where things
are, what's good, what's cheaper — nobody starts from zero."
To avoid repeating "what's good, what's cheaper" twice, the
friends line lost its tail: "We discuss stores, products and
prices with our friends. And then we go home, and it's gone."
The capstone's "so you don't start from zero every week" now
answers Beat 1's wish directly. Runtime ~2:48.

## PROOF variant — Spark first pass (owner testing, 2026-11-01)

Owner is testing a decode flip: Spark first pass, Wonder as
backup (the reverse of the current live setup). NOT yet
adopted. Spark's advisor position: for the flip IF Wonder is
a confidence-gated second look on hard lines (design already
exists: low-confidence -> review queue), because the bake-off
failure mode was confident-but-wrong prices (Spark 92/98, 4
price errors), which a failure-only fallback never catches.
The flip also matches MODEL-POLICY (cheapest model per job;
Wonder-primary was the exception) and the new spend caps
($10/hr freeze, $20/mo ceiling). If adopted, PROOF becomes:

"I fed it the 114 receipts. Muse Spark reads them first —
it reads most receipts fine. When a line is hard to read,
Muse Wonder takes a second look. We tested both models on
real receipts — Wonder is the better reader, so it gets the
hard ones. It found egg whites in 35 of those 114 trips.
And the same almond flour, $13.59 at one Costco, $16.99 at
another."

If adopted, also update: META-PRODUCTS.md, SUBMISSION-DRAFT,
the Nov 4 amendment note — script, app and docs must agree.

## Owner edits batch (2026-11-01 ~09:30)

1. Beat 1: "And then we go home, and it's gone." CUT.
2. Capstone -> first person: "Arya learns from my receipts,
   and it holds what I share, so I don't start from zero
   every week."
3. Trip: hummus neighbor-warning CUT — owner cannot show it
   in the demo (his account has no other users reporting).
   Demo town can show it; his footage cannot.
4. At home: eggs-cheaper line CUT — same showability problem,
   and the price insight is already proven by almond flour.
5. Tagline: "the list that writes itself" does not land.
   Owner wants learns / helps / help others. End card now:
   "Arya — learns how we shop, helps us help each other."
Runtime ~2:35.

## Honest limitations beat (owner, 2026-11-01)

Owner ordered a limitations section: not enough data to
train Arya in 8 days; Arya is community dependent; he built
many ways to give feedback; as he, his friends, and the
viewer use it, it gets better and he will fix/add from
feedback; admit the problem is incredibly hard. Placed
between AT HOME and CLOSE so the film still ends on the
close. "Train" rendered as "learn" (Arya learns patterns in
code; it does not train models). Runtime now ~3:04 — the
Beat 1 "You walk up and down" line (-4s) brings it to ~3:00
if he wants it inside the cap before the timed read.
