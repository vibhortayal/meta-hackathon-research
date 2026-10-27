# REVISED Idea Research — The Mass-Problem Lens

*Generated 2026-10-27 under a new mandate from the owner: the previous pool's center of gravity (niche / emotional / frontier) was rejected. This pass hunts problems that MOST people face, quantified with prevalence evidence, that a Meta-model agent can genuinely solve end-to-end. Judging reminder: Impact 30%, Use of Meta AI Tooling 25%, Demo 25%, Technical Depth 20%. Deadline Nov 4, 2026, 9:00 PM ET. One developer + AI agents, phone-first demo, no GPU, no TTS in Meta's stack (voice-out = device/third-party or text).*

*The winning shape, kept from prior rounds: agents that **verify with evidence and act** — recompute, compare, draft, file, track to closure — not chatbots that answer.*

---

## Part 1 — The territory map (prevalence first)

| Territory | The numbers | Source |
|---|---|---|
| **Wrong medical bills & denied claims** | Insurers denied **19% of in-network claims** on HealthCare.gov plans in 2024 — ~85M of 451M claims; 37% of out-of-network. **Fewer than 1% are ever appealed**, yet ~34% of internal appeals are overturned and external review flips roughly half. **45% of insured working-age adults** received a bill in the past year for something they thought should be covered; 17% were denied doctor-recommended care. Of people who challenged a bill, **74% with billing errors got them corrected** (JAMA Health Forum survey). **100M+ adults (41%) carry medical debt; ~$220B owed.** | KFF 2024 claims analysis; Commonwealth Fund 2024; USC Schaeffer / JAMA Health Forum 2024; KFF Health News |
| **Money owed to you, never collected** | States hold **$70B+ in unclaimed property belonging to ~1 in 7 Americans (~33M people)**; only ~$4.49B (about 6%) was returned in FY2024; average claim ≈ $2,080. Class actions settled **$42B in 2024**, but claim participation routinely runs **below 10%, often below 1%**. The IRS estimates **1 in 5 eligible taxpayers never claim the EITC** — average credit ≈ $2,916, billions left annually. | NAUPA (via Motley Fool / state treasurers); NERA via Talli; IRS / Taxpayer Advocate |
| **Scams & fraud** | Consumers reported **$12.5B lost to fraud in 2024, up 25% YoY** (FTC). Imposter scams are the #1 category (~$2.95B). Older adults reported $2.3–2.4B, but the FTC estimates the true senior toll at **$10.1B–$81.5B** after underreporting. Gallup/Stop Scams: roughly **1 in 10 households** experienced scam losses in 2025. | FTC Consumer Sentinel 2024; FTC Protecting Older Consumers 2024–25; Gallup |
| **The annoyance economy (holds, disputes, broken promises)** | Consumers average **~13 hours/year on hold**. Groundwork Collaborative estimates the "annoyance economy" — holds, billing disputes, paperwork, junk-fee fights — costs US families **~$165B/year** in time and money, including ~$21.6B of healthcare-admin hassle. Making cancellation hard can raise a seller's revenue >200% — friction is a business model, and firms know most people give up. | TalkTo survey; Groundwork Collaborative |
| **Subscription creep** | Households spend ~**$1,100/year on subscriptions (~$90/mo)**, ~$200/yr of it rarely or never used; consumers underestimate their subscription spend by ~$133/mo on average (estimated $86 vs actual $219). The FTC click-to-cancel rule was vacated in July 2025 — cancellation stays hard by design. | CNET/YouGov 2025; C+R Research |
| **Food waste at home** | EPA (2025): food waste costs **$728 per person per year — $2,913 for a household of four, $56/week**. Households are the largest single waste segment (~35–37% of all food waste happens in homes). | US EPA 2025; ReFED |
| **Home repairs & contractor quotes** | ~86M US homeowner households. Angi: the typical household spends ~**$2,041/yr on maintenance + $1,143 on emergency repairs**; Thumbtack's Home Care Price Index puts full annual upkeep of a single-family home at **~$11,196/yr**. Prices for identical jobs vary widely by region and contractor (regional cost swings of 40–80%), and marketplaces are paid by the contractors they recommend. | Angi State of Home Spending; Thumbtack (2026 roundups) |
| **Caregiver admin** | **63M Americans — nearly 1 in 4 adults — provided unpaid care in the past year** (AARP/NAC 2025, up 46% in a decade), worth ~$600B/yr; ~1 in 4 caregivers provide 40+ hrs/week; caregivers spend ~$7,200/yr out of pocket. Their load is heavily paperwork: bills, benefits, discharge docs, deadlines for a *second* person. | AARP / NAC, Caregiving in the U.S. 2025 |

---

## Part 2 — Territories killed, and why

- **Appeal-letter generation, standalone — SATURATED.** Counterforce Health (free, NIH/UPenn-funded, 10,000+ appeals, ~70% reported reversal), Claimable ($39.95/appeal, claims >80% success), Fight Health Insurance (free, 10,000+ appeals), plus AppealGen, ClaimPilot, Apellica, and human-advocate Sheer Health. The letter is now a commodity feature. What survives: everything *around* the letter (audit before, deadlines during, verification after) — see BillVerdict.
- **Subscription tracking/cancellation, standalone — SATURATED.** Rocket Money has 10M+ members, a cancellation concierge, and bill negotiation (for a 35–60% cut), plus a dozen clones. Survives only as one feature inside a broader verify-and-recover agent.
- **Settlement *finders*, standalone — COMMODITIZED.** Claim Depot newsletters, Class Action Buddy (auto-fill apps), Owed/MoneyPilot settlement tabs. Finding is a list; the unclaimed 90% is lost in *eligibility proof and claim assembly*, which is where Owed (below) aims.
- **Scam-screenshot checkers — OWNED BY A GIANT.** Norton Genie does free screenshot/text verdicts with Norton's threat data. Survives only as live, claim-by-claim verification during the call itself — see CallCheck.
- **Manual-entry fridge/pantry trackers — GRAVEYARD CATEGORY.** NoWaste, Fridgely and kin all die on data entry. Survives only in zero-entry form (receipt + photo), see UseFirst.
- **Bill-negotiation services — TAKEN, AND THE MODEL IS RENT-SEEKING.** Rocket Money's 35–60%-of-savings cut is the incumbent shape; a hackathon entry can't out-distribute it in 8 days.
- **Benefits screening, standalone — QUIETLY OCCUPIED.** NCOA BenefitsCheckUp and state tools exist; the gap is execution (assembled applications), so benefits fold into Owed/CareDesk rather than standing alone.
- **Tax prep — FORTIFIED.** TurboTax/H&R Block/IRS Direct File. The EITC gap is a *discovery* problem, folded into Owed.
- **Avoid-list kills (unchanged):** medical/mental-health *advice* (billing arithmetic is explicitly not advice), job screeners, nutrition coaches, personality analyzers, sports analyzers, simple education chatbots, basic RAG, simple image analyzers, politics/war.
- **Contractor lead-gen — WRONG SIDE OF THE MONEY.** Angi/Thumbtack own distribution and are paid by contractors; the open seat is the homeowner's independent auditor (QuoteCheck).

---

## Part 3 — The new candidates

### 1. BillVerdict — the medical-bill case agent: audit → dispute → verified closure

**One-liner:** Photograph any medical bill, EOB, or denial letter; BillVerdict recomputes what you actually owe line by line, builds the dispute or appeal packet, tracks the deadline, and then verifies the corrected bill really posts the promised adjustment.

**The problem.** 45% of insured working-age adults got a bill in the last year for something they believed was covered (Commonwealth Fund); marketplace insurers denied 19% of in-network claims — ~85M claims in 2024 (KFF); fewer than 1% of denials are appealed (KFF), and 86% of people who don't challenge a bad bill say it's because they think it won't matter (JAMA Health Forum) — while 74% of those who did report a billing error got it corrected, and about a third to a half of appeals are overturned. 100M+ adults carry medical debt totaling ~$220B (KFF). Who: essentially every insured adult, several times a year; hardest on the 63M caregivers managing a parent's bills too.

**The loop (end-to-end).**
1. **Ingest:** photos/PDFs of itemized bill + EOB + denial letter + plan summary. Spark 1.3 reads all of it in one long-context pass (native PDF + image input) into a structured case file.
2. **Recompute (the core):** a deterministic engine (Spark tool-calling code execution) re-derives every line — deductible already met?, coinsurance math, duplicate charges, unbundled codes, in-network rate applied?, contractual adjustment present? Each discrepancy is pinned to the exact bill line and the exact plan clause. Output: "You were billed $4,812. You owe $617. Here's the evidence, line by line."
3. **Act:** generates the right instrument per discrepancy — billing-office correction request, internal appeal citing plan language, or external-review request — as a ready-to-send packet with exhibits numbered to the evidence.
4. **Track:** appeal deadlines extracted and calendared; status check-ins.
5. **Verify closure (the part nobody builds):** when the corrected EOB / new bill arrives, the agent re-audits it against the promised adjustment and stamps the case CLOSED-VERIFIED or reopens it with the delta. Family mode: one person runs cases for parents/spouse.

**Meta mapping.** Muse Spark 1.3 — multimodal document understanding + plan-clause reasoning + tool-called computation for the arithmetic (numbers come from code, not vibes). Muse Voice Transcribe — billing-office calls on speakerphone become searchable case notes; promised adjustments are extracted as trackable commitments. Muse Glimmer (open weights, local-feasible) — on-device redaction pass that masks SSNs/member IDs before anything leaves the phone: a real privacy architecture, not a promise. (SAM/Image deliberately unused — tooling honesty beats box-ticking.)

**Why it scores.** *Impact:* the largest sourced dollar pool in this entire research program, hitting ~half of insured adults yearly. *Tooling:* three Meta products in load-bearing, non-interchangeable roles. *Demo:* a dollar figure collapsing on screen, with receipts (below). *Depth:* deterministic recompute + evidence graph + closure verification is a system, not a prompt.

**Demo moment (20s).** A $4,812 hospital bill goes in. Lines light up: duplicate charge, deductible double-counted, out-of-network rate on an in-network facility. The verdict flips to **"You owe $617"** — then a "corrected bill" arrives and BillVerdict stamps it: *Adjustment verified. Case closed.* 

**Incumbents & the new lens.** Counterforce Health / Claimable / Fight Health Insurance write appeal letters for *denials of care*, starting from a denial letter. BillVerdict starts earlier (audits the *bill math* before you pay a wrong number) and ends later (verifies the fix actually posted). Nobody in the cluster owns audit + closure, and none does family mode. This is billing administration and arithmetic — explicitly not medical advice.

**Build sketch (8 days).** Days 1–2: document intake + structured extraction on realistic synthetic bills/EOBs (no real PHI in the demo, ever). Days 3–4: recompute engine for the top discrepancy classes (duplicates, deductible/coinsurance math, network-rate mismatch, missing contractual adjustment). Day 5: packet generation. Day 6: closure re-audit. Day 7: family mode + polish. Day 8: demo video. **Biggest risk:** scope creep in discrepancy classes — cap at 4–5 provable classes and let the agent say "outside what I can verify" on the rest (abstention is on-brand for the evidence story).

---

### 2. Owed — the money-you're-owed agent: property, settlements, credits

**One-liner:** One profile in, Owed hunts everything you're owed — state unclaimed property, class-action settlements you qualify for, tax credits you never claimed — then assembles the actual claim packets and tracks them to payout.

**The problem.** $70B+ sits in state unclaimed-property vaults belonging to ~1 in 7 Americans; only ~6% comes back each year (NAUPA). $42B in class-action settlements in 2024 with participation often under 1–10% — the money reverts to defendants or sits idle. 1 in 5 eligible workers skip the EITC (~$2,916 average). The common cause isn't ignorance of one program; it's that every silo has its own search, its own form, its own proof, its own deadline — and life (12% of Americans move each year) breaks the paper trail.

**The loop.**
1. **Profile:** name variants, address history, past employers — the keys every database actually matches on.
2. **Hunt:** assisted search across state unclaimed-property databases (scope: top states + MissingMoney-participating states), a curated live-settlements feed, and a credits screener (EITC/CTC/state analogs) run against the user's own numbers.
3. **Match with evidence:** Spark 1.3 reads the user's own documents (old pay stubs, receipts, policy mail — photos) to establish eligibility and proof *before* suggesting a claim — no spray-and-pray filings.
4. **Assemble:** generates each claim packet: form filled, proof checklist with the exact documents, notarization flagged where states require it, heir documentation path when the owner is a deceased parent.
5. **Track & verify:** deadlines calendared; payout confirmations logged; a running "recovered" ledger.

**Meta mapping.** Spark 1.3 — document understanding over messy personal paperwork + eligibility reasoning against settlement class definitions (long legal PDFs in context). Voice Transcribe — the profile itself can be *dictated* ("I lived in Ohio from 2009 to 2014, worked at…"), which is how real users will actually give address history. Muse Image — not core; skip. Glimmer — cheap first-pass classifier over large settlement lists ("could this class definition ever match this profile?") — the open-weights cost story.

**Why it scores.** *Impact:* three giant sourced pools, one universal audience (everyone is owed something with probability ~1-in-7 before settlements/credits). *Demo:* real money found live is the strongest 20 seconds in this document (below). *Tooling:* document-evidence matching is beyond-basic. *Depth:* identity-resolution + evidence assembly is genuinely hard, honest engineering.

**Demo moment.** The developer runs his *own real profile* live: two states searched, a forgotten utility deposit and a settlement match surface, claim packet assembled on camera. Counter on screen: **"$386 found. Packet ready."** (Pre-run the search before filming so the live run reproduces it — standard demo hygiene, disclosed in the video as a re-run.)

**Incumbents & the new lens.** MissingMoney/unclaimed.org search one silo and stop at a link. Class Action Buddy/Owed-app/MoneyPilot file *no-proof* settlement claims only. Finders charge 10–15% to do the state paperwork. Nobody unifies property + settlements + credits, matches against your documents, and assembles state-grade packets including the heir path. **New lens: recovery is a paperwork-assembly problem, not a search problem.**

**Build sketch.** Days 1–2: profile + state-search assistance for ~8–10 states (guided deep-links + result capture; full scraping of 50 CAPTCHA'd state sites is NOT the 8-day play). Day 3: settlements feed (curate ~100 live settlements with class definitions). Day 4: document-evidence matcher. Days 5–6: packet assembly (2–3 state form templates + generic settlement claims). Day 7: tracker + ledger. Day 8: video. **Biggest risk:** state-site heterogeneity — mitigated by the assisted-search scope and by making packet assembly (which is fully in our control) the hero.

---

### 3. PromiseKeeper — win the customer-service fight, then verify they kept the promise

**One-liner:** Tell PromiseKeeper the problem; it computes what the company owes you, scripts the call, records every promise the rep makes — then checks your next bill and escalates with the rep's own words if the promise never landed.

**The problem.** The average consumer spends ~13 hours/year on hold; the "annoyance economy" burns ~$165B/yr of American time and money (Groundwork), and the system's open secret is that promised credits, refunds, and corrections quietly fail to post — because nobody checks. Friction is deliberate: hard cancellation alone can more than triple a seller's take from a customer who meant to leave.

**The loop.**
1. **Case math first:** upload the bill/contract; Spark 1.3 recomputes the correct amount (wrong rate, fee that violates the plan, price-protection window) and states the exact remedy to demand.
2. **Playbook:** a one-screen call script — opening line, the specific ask, escalation triggers, the phrases that create a record ("please confirm the credit amount and date").
3. **Capture:** user calls on speakerphone; Voice Transcribe (diarized: you vs. rep) streams the call; the agent extracts every commitment into a **Promise Ledger** — amount, action, date promised, confirmation number.
4. **Verify:** when the next bill/statement arrives (photo), the agent checks each promise against it. Kept → closed with evidence. Broken → 
5. **Escalate:** an escalation packet quoting the rep's own transcribed words + the ledger + a regulator complaint draft (CFPB/FCC/state AG as appropriate).

**Meta mapping.** Spark 1.3 — case math + playbook + promise extraction + escalation drafting. Voice Transcribe — the load-bearing ear: diarized call capture is what turns "they promised me" into evidence. Glimmer — on-device pre-screen of statements for the promised line item (cheap, private).

**Why it scores.** *Impact:* universal — everyone fights at least one company a year; the $165B annoyance economy is the frame. *Demo:* the broken-promise catch is a perfect story beat (below). *Tooling:* diarization-as-evidence is a genuinely novel use of Voice Transcribe. *Depth:* commitment extraction + cross-document verification over time.

**Demo moment.** Rep (transcribed live): *"A $200 credit will post within 5–7 days."* Cut to the next bill. PromiseKeeper stamps it: **PROMISE BROKEN — $0 posted.** Then the escalation letter appears, quoting the rep verbatim. 

**Incumbents & the new lens.** DoNotPay (generic letters; FTC-scarred), Rocket Money (negotiates a few bill types for a 35–60% cut, bank-link required), Pixel Hold For Me (holds your place, then leaves). **Nobody verifies the promise.** The lens: customer service isn't a conversation problem, it's a *commitments-tracking* problem.

**Build sketch.** Days 1–2: case-math for 2–3 case types (telecom bill, subscription refund, airline/hotel fee). Day 3: playbook gen. Days 4–5: diarized capture + promise extraction against a recorded mock call corpus. Day 6: next-bill verification. Day 7: escalation packet. Day 8: video. **Biggest risk:** call-recording consent varies by state — product posture is user-side capture with an on-screen disclosure prompt and a notes mode; demo uses a consented mock call center (a second phone + scripted "rep"). Time-compression in the demo ("8 days later") must be labeled, not faked.

---

### 4. CallCheck — the live scam-call lie detector for your family

**One-liner:** Put the suspicious call on speaker (or forward the text/photo of the letter); CallCheck transcribes it live, extracts every factual claim the caller makes, verifies each one against official sources in real time, and tells you — claim by claim — what's false, while auto-alerting your family.

**The problem.** $12.5B reported fraud losses in 2024 (+25%, FTC) with imposter scams #1; seniors' true losses estimated up to $81.5B with underreporting (FTC); ~1 in 10 households hit in 2025 (Gallup). The attack is always the same shape: an authority claim ("I'm from Social Security"), a crisis claim ("your grandson is in jail"), and a secrecy/urgency claim ("don't tell anyone, pay in gift cards"). Victims don't need a vibe check — they need the *claims checked*, in the moment, by someone calm.

**The loop.**
1. **Capture:** live speakerphone audio → Voice Transcribe realtime stream (diarized), or screenshot/photo/text paste for messages and mail.
2. **Claim extraction:** Spark 1.3 pulls discrete checkable claims from the transcript as the call proceeds.
3. **Verification:** each claim is checked against official-source ground truth via web-search grounding (SSA's published procedures, court bail reality, the real agency phone numbers, "the IRS never demands gift cards") and against a scam-script pattern library (the scripts are standardized — that's the exploitable weakness).
4. **Verdict & action:** a big, calm red/green board: FALSE — "Social Security never threatens arrest by phone." Plus the one action that ends it safely (hang up; call the family code-word protocol; call the number on the real card).
5. **Aftermath:** family alert sent with the claim-by-claim report; if money moved, a recovery packet (bank dispute + FTC report drafts) with the transcript as evidence.

**Meta mapping.** Voice Transcribe — realtime diarized stream is the product's spine (and its 20+ speaker headroom is irrelevant-but-free). Spark 1.3 — claim extraction + grounded verification reasoning over a live transcript. Spark (native audio in) — second-pass tone/pressure analysis on flagged segments. Device TTS or pure visual verdicts for output (no Meta TTS exists — the UI is designed around that, big-text verdicts readable by a stressed senior).

**Why it scores.** *Impact:* the fastest-growing mass harm on the list, concentrated on the most vulnerable. *Demo:* a live staged call getting dismantled claim by claim is riveting television. *Tooling:* realtime ASR + extraction + grounded verification is a three-stage Meta pipeline nobody demos by accident. *Depth:* latency budget + claim-schema + source grounding is real systems work.

**Demo moment.** "Officer Daniels" on speaker: *"Your Social Security number is suspended due to drug trafficking in Texas."* The board stamps claims as he speaks: **FALSE** (numbers aren't "suspended") · **FALSE** (SSA doesn't call like this) · **SCRIPT MATCH: SSA imposter, variant 4.** Final card: *Hang up. Nothing is wrong with your number.* 

**Incumbents & the new lens.** Norton Genie judges a screenshot's *vibe* after the fact. Truecaller flags numbers. Banks warn in brochures. **CallCheck verifies the caller's factual claims against the world, live, during the pressure moment** — and closes the family loop. (The old pool's "scam second opinion" scored 6.1 as a static analyzer; the live claim-verification loop is a different product.)

**Build sketch.** Days 1–2: claim schema + pattern library for the top 5 scripts (SSA, IRS, grandparent, bank-fraud dept, tech support). Day 3: grounded verification sources per script (curated official pages). Days 4–5: realtime pipeline (speakerphone → stream → claims board). Day 6: family alert + aftermath packet. Day 7: rehearsed-call hardening. Day 8: video. **Biggest risk:** live latency/accuracy on speakerphone audio — mitigate with the pattern library doing early warning while grounded checks land seconds later (matches reality: scripts self-identify fast).

---

### 5. QuoteCheck — the homeowner's independent quote auditor

**One-liner:** Photograph the problem, upload the contractor's quote; QuoteCheck measures the job itself, builds an independent line-item estimate, flags the padding — and after the work, verifies from photos that everything you paid for was actually done.

**The problem.** ~86M US homeowner households spend ~$3,200/yr on maintenance and emergency repairs (Angi) — ~$11,196/yr for full upkeep of a single-family home (Thumbtack) — in a market where prices for the same job swing wildly, homeowners can't judge a line item, and the big platforms (Angi, Thumbtack) are paid by the contractors they steer you to. The information asymmetry is the product's target.

**The loop.**
1. **Scope from evidence:** user walks the problem with the camera; SAM 3.1 segments/measures (roof planes, damaged siding area, cabinet run), Spark 1.3 builds the job scope in plain language.
2. **Independent estimate:** line-item estimate grounded in published cost data (web-search grounding over cost references), localized, presented as ranges with stated uncertainty.
3. **Quote audit:** contractor PDFs/photos are parsed and diffed against scope + estimate: items not in scope, duplicated labor, quantities above measurement, permit missing, allowance traps. Output: the 3 questions to ask and the fair-range verdict per line.
4. **Negotiation brief:** a polite, specific counter script ("your tear-off line is billed at 26 squares; the roof measures ~19").
5. **Completion verification:** before/after photo sets are compared against contracted line items before final payment — "shingle course replaced: visible ✓; underlayment: not verifiable from photos — ask for the in-progress shot."

**Meta mapping.** SAM 3.1 — measurement/segmentation is the differentiator (counting and areas, its home turf). Spark 1.3 — scope reasoning + quote diffing + drafting. Voice Transcribe — the walkthrough narration ("this stain appeared after the March storm") becomes structured job context.

**Why it scores.** *Impact:* nearly every homeowner, thousands per household per year. *Tooling:* SAM in a measurement role (not another image analyzer) + Spark diffing. *Demo:* a $14,800 quote getting red-lined is deeply satisfying. *Depth:* estimate grounding + quantity verification is honest, hard estimation work.

**Demo moment.** Roof quote: **$14,800**. QuoteCheck overlays its own measurement on the roof photo — *"billed 26 squares; measured ≈19"* — two duplicated line items flagged; verdict: **fair range $9,600–$11,200.** 

**Incumbents & the new lens.** Angi/Thumbtack sell your job to contractors; Xactimate serves insurance adjusters. QuoteCheck is the first agent on the *homeowner's* side of the table, and the only one that verifies completion against the quote before the final check.

**Build sketch.** Days 1–2: scope+measure for 2 job types (roofing, water-heater/plumbing). Day 3: cost-grounding data pack. Days 4–5: quote parser + diff report. Day 6: completion check. Days 7–8: polish + video. **Biggest risk:** photo-based measurement accuracy — present estimates as ranges with method shown ("measured from your photos ±15%") rather than false precision; the audit still works because padding is usually way outside the error bars.

---

### 6. CareDesk — the paperwork department for the 63 million

**One-liner:** Caring for a parent? Photograph every letter, bill, discharge paper, and benefits notice that lands; CareDesk turns the pile into one family dashboard: what's due, what's wrong, what's owed to them, and what's already handled.

**The problem.** 63M Americans (nearly 1 in 4 adults) provide unpaid care (AARP/NAC 2025); the care is medical, but the *second job* is administrative — a parent's EOBs, benefits letters with deadlines, discharge instructions, bills in two households — carried by someone already at 40+ care hours a week, spending ~$7,200/yr out of pocket. The failure mode is never knowledge; it's a missed deadline in a shoebox.

**The loop.** Same verify-and-act engine, pointed at a second person: (1) any document photo → extracted obligation/entitlement/deadline; (2) bills route into the BillVerdict audit; (3) benefits notices are screened against unclaimed-entitlement patterns (veterans' Aid & Attendance and state caregiver programs are chronically under-claimed — screening here is *discovery*, with assembly handed to the Owed packet machinery); (4) a weekly one-page family brief: due this week / waiting on them / money recovered so far. Multi-sibling sharing: everyone sees the same truth.

**Meta mapping.** Spark 1.3 (document chaos → structured obligations), Voice Transcribe (dictated updates from the road — "Mom's pharmacy bill was $212, due Friday"), Glimmer (private on-device triage of sensitive family documents).

**Why it scores / where it's honest.** *Impact:* the largest single population number in this document. *Demo:* the shoebox-to-dashboard transformation is instantly legible to any judge who has a parent. *Risk to its rank:* as a standalone it's a bundle of BillVerdict + Owed with a caregiver frame — the honest read is that CareDesk is the **distribution wedge** (the person who'll install an agent for Mom before they install one for themselves), not a separate engine. Ranked accordingly in the union table.

**Demo moment.** A literal shoebox of a parent's mail emptied onto a table → 14 photographs → one dashboard: *2 bills wrong ($311 back), 1 benefits deadline in 9 days, 1 unclaimed state refund: $148.* 

**Build sketch.** Reuse BillVerdict/Owed components; new work is intake triage + the family brief + multi-person case model (3–4 days on top of a sibling build; as a *standalone* 8-day build it means thinner audit depth). **Biggest risk:** exactly that trade — breadth over depth, live on stage.

---

### 7. UseFirst — the zero-typing fridge agent that pays you back in groceries

**One-liner:** Photograph the grocery receipt and, later, the fridge; UseFirst keeps the inventory you never typed, tells you what to cook *tonight* before it dies, and proves at week's end — in dollars — what you saved and what still hit the bin.

**The problem.** EPA 2025: **$728 per person per year** of food wasted — **$2,913 per household of four, $56 every week** — with households the largest waste segment. The cause is mundane: food bought without a plan meets a fridge nobody inventories. Every prior app died on manual entry.

**The loop.**
1. **Receipt in:** photo → Spark 1.3 builds the inventory with realistic shelf-life windows per item (no typing, ever).
2. **Fridge check-ins:** a 3-second photo sweep; SAM 3.1 + Spark reconcile what's actually still there vs the list.
3. **Rescue order:** each evening, a cook-first ranking by expiry risk × dollar value — with Muse Image rendering the rescue dish *from your actual ingredients* so it looks like dinner, not homework.
4. **Waste audit (verified):** items that died get photographed at the bin; the weekly report prices them from the receipt and generates next week's **buy-less list** — the rare app whose success metric is you buying less.

**Meta mapping.** Spark 1.3 (receipt OCR/reasoning + reconciliation + planning), SAM 3.1 (fridge item segmentation), Muse Image (the rescue-dish render — the one decorative-but-motivating use, $0.01 a pop), Voice Transcribe (hands-free "we're out of eggs" capture mid-cooking).

**Why it scores / honest limits.** *Impact:* universal and EPA-priced. *Demo:* warm, visual, the dish render is a delight beat. *Limits:* savings are behavior-mediated (the agent can't eat the spinach for you), the category has a graveyard of failed trackers, and recovery-per-demo is tens of dollars, not hundreds — under a *mass-money* lens it lands mid-table despite perfect prevalence. Framed strictly as money/waste logistics, never nutrition coaching (avoid list).

**Demo moment.** Fridge photo in → *"Spinach dies tomorrow ($4.20), chicken by Friday ($11.60). Cook this tonight:"* — a rendered plate built from exactly those items — then the week-end report: **"Wasted this week: $6.10. Last month's average: $38."**

**Build sketch.** Days 1–2: receipt→inventory + shelf-life table. Days 3–4: fridge reconciliation. Day 5: rescue ranking + dish render. Days 6–7: waste audit + buy-less list. Day 8: video. **Biggest risk:** fridge-photo recognition in cluttered real fridges — mitigate by making the *receipt* the source of truth and photos a spot-check, never the foundation.

---

## Part 4 — The union, re-ranked under the mass-problem lens

All 15: the 7 new candidates + the previous pool's 8 (Heirloom, Paperwork Pilot, Follow-Along, Paper Replicator, Second Listen, Bill Auditor, Household brain, Quiet Coach). Ranking rule for this table: prevalence × dollars-at-stake-per-person × frequency, then Tooling/Demo/Depth, then 8-day feasibility.

| # | Idea | Origin | Under the mass lens |
|---|---|---|---|
| **1** | **BillVerdict** | new | Largest sourced dollar pool ($220B debt; 85M denials/yr; 45% of insured adults hit yearly), full audit→act→verify loop, the appeal-letter cluster proves demand while leaving the audit/closure seat empty |
| **2** | **Owed** | new | $70B + $42B/yr settlements + EITC billions; 1-in-7 base rate; the only candidate whose demo can find *real money for a real person live* |
| **3** | **PromiseKeeper** | new | Everyone fights a company yearly (13 hrs on hold; $165B annoyance economy); purest verify-with-evidence loop; absorbs Bill Auditor as its case-math front end |
| 4 | CallCheck | new | $12.5B+ and rising, the most vulnerable victims, arguably the best live demo of the 15 — held at #4 only by realtime-audio build risk |
| 5 | QuoteCheck | new | ~86M homeowner households, thousands/yr each; strong red-line demo; estimate-grounding risk keeps it out of the top 3 |
| 6 | Bill Auditor | old pool #6 | Still the safest build in the union — but under this lens it's visibly a *subset* (utility/telecom case math) of #1/#3's pattern, with smaller dollars per person |
| 7 | CareDesk | new | 63M people — but it's #1+#2 re-framed for a parent; best as a wedge/frame on a sibling build, not a standalone engine |
| 8 | UseFirst | new | Perfect prevalence ($2,913/household, EPA) but behavior-mediated savings and a graveyard category cap it |
| 9 | Paperwork Pilot | old pool #2 | **Drops hard under this lens.** Forms are universal but episodic and low-dollar per event; computer-use demo risk stays; its best move (file the thing) is now an act inside #1 and #2 |
| 10 | Heirloom | old pool #1 | **The honest big drop.** It remains the most moving demo in the union — but the addressable moment (a living demonstrator + a skill worth inheriting + filming it) happens rarely per person, with no quantifiable dollars. Under a mass lens it cannot hold #1; under an emotion lens it still can |
| 11 | Follow-Along | old pool #3 | DIY/cooking learners are numerous, but value is convenience, not money or harm; unverified-coach behavior change is unproven |
| 12 | Household brain | old pool #7 | Scheduling pain is universal but diffuse and dollar-free; the demo payoff problem identified last round survives this lens too |
| 13 | Second Listen | old pool #5 | Appliance owners are mass; "machine sounds wrong" is a rare event per household — frequency kills it here |
| 14 | Quiet Coach | old pool #8 | Prevention is a beautiful frame in search of a mass, frequent, costly mistake class it can own by Nov 4; staging risk unchanged |
| 15 | Paper Replicator | old pool #4 | **Last under this lens, by design of the lens.** Its audience (researchers with a paper to check) is the smallest population in the union; frontier points don't compensate when the mandate is mass problems |

### Top 3 flagged

1. **BillVerdict** — the biggest verified money pool in American household life, with a full loop (audit → dispute → verified closure) that the existing appeal-letter cluster demonstrably does not cover.
2. **Owed** — three giant "your money, uncollected" pools unified by the insight that recovery is paperwork assembly, not search — and a demo that can find real dollars live.
3. **PromiseKeeper** — the universal fight (holds, promised credits that never post) solved at its unowned step: verifying the promise actually landed, with the rep's own words as evidence.

*Strategic note for the parent agent: #1, #2, #3 and #7 are one platform wearing four hats (document intake → recompute/match → packet → tracked closure). Picking any one of them keeps the others alive as roadmap. CallCheck (#4) is the only top entry on a different technical spine (realtime audio) — it's the high-variance pick: best demo, riskiest build.*

---

## Sources

- KFF, Claims Denials and Appeals in ACA Marketplace Plans in 2024 — https://www.kff.org/patient-consumer-protections/claims-denials-and-appeals-in-aca-marketplace-plans-in-2024/
- KFF Health News, Diagnosis: Debt takeaways (100M adults / $220B) — https://kffhealthnews.org/health-care-costs/diagnosis-debt-investigation-key-takeaways/
- Commonwealth Fund, Unforeseen Health Care Bills and Coverage Denials (2024) — https://Www.Commonwealthfund.Org/press-release/2024/new-research-insured-working-age-americans-face-widespread-medical-billing
- USC Schaeffer Center / JAMA Health Forum (challenging bills works; 74% of billing errors corrected) — https://mann.usc.edu/news/its-worth-challenging-that-troubling-medical-bill-study-finds/
- Counterforce Health (incumbent landscape; NIH/UPenn, ~70% reversal) — https://en.wikipedia.org/wiki/Counterforce_Health ; MarketWatch coverage — https://www.itiger.com/news/2577087621
- NAUPA unclaimed property ($70B, 1 in 7, $4.49B returned FY2024) — https://www.fool.com/money/banks/articles/heres-what-happens-to-70-billion-of-unclaimed-money-in-the-us/
- Class-action claim rates (<10%, often <1%; $42B in 2024) — https://www.talli.ai/blog/why-90-of-settlement-money-never-arrives---and-how-digital-payouts-fix-it ; https://theconsumersbrief.com/billion-dollar-investigation/
- IRS / Taxpayer Advocate, EITC (1 in 5 eligible don't claim; avg ≈ $2,916) — https://www.irs.gov/tax-professionals/eitc-central/eitc-facts-to-share ; https://www.taxpayeradvocate.irs.gov/news/nta-blog/eitc-awareness-day-is-january-23/2026/01/
- FTC fraud losses ($12.5B in 2024; older adults $2.3B reported) — https://www.aarp.org/money/scams-fraud/older-adults-ftc-fraud-report.html ; FTC older-consumer estimates via SF Treasurer — https://sftreasurer.org/san-francisco-becomes-first-city-country-build-unified-response-scams
- Norton Genie (incumbent scam checker) — https://www.zdnet.com/article/how-to-use-nortons-free-ai-powered-scam-detector/
- Groundwork Collaborative "annoyance economy" (~$165B) — https://moneywise.com/news/economy/the-annoyance-economy-is-costing-americans-billions-here-are-the-3-biggest-culprits-stealing-your-time-and-money
- Time on hold (~13 hrs/yr) — https://www.edwardsansweringservice.com/study-americans-spent-13-hours-on-hold-last-year/amp/
- Subscriptions (~$1,100/yr; ~$200 unused; $133/mo underestimate) — https://globalwarming.einnews.com/pr_news/949563719/americans-spend-nearly-1-100-a-year-on-subscriptions-with-about-200-going-unused-cnet-survey-finds
- Rocket Money (10M+ members; negotiation 35–60% of savings) — https://fortunly.com/reviews/rocket-money-review/
- US EPA, Estimating the Cost of Food Waste to American Consumers (2025) — https://www.epa.gov/land-research/estimating-cost-food-waste-american-consumers
- AARP / NAC, Caregiving in the U.S. 2025 (63M caregivers) — https://www.aarp.org/states/maryland/caregiving-report/
- Home spending (Angi: $2,041 maintenance + $1,143 emergency repairs) — https://myhomepros.com/home/how-to-budget-for-annual-home-services-and-repairs/
