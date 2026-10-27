# IDEAS — the joy lane

*Compiled 2026-10-27 for the Meta Global AI Developer Hackathon (Indie track, submission Nov 4, 2026, 9:00 PM ET). This file covers ONLY the joy / relaxation / human-connection lane — the mass-problem lane is researched separately. Scores are my judgement, calibrated against the prior pool (cooking coach 7.7–8.3, Paper Games 7.2, household agent 7.1–7.2, Faceless Studio 6.8, Play to Comic 6.7). Evidence strength is marked; vendor numbers are labelled as such.*

---

## What the evidence says people actually do for joy and connection

| Finding | Evidence | Strength |
| --- | --- | --- |
| Same-room party games with phones as controllers are a durable ritual, not a fad | Jackbox has shipped a new Party Pack **every year since 2014**; the phone-as-controller + room-code join (no installs) is credited by its own CEO for the breakthrough; pandemic and Twitch surges on top of a decade-long base | Strong (12 years of annual releases) |
| A tiny daily game is a *relationship* ritual with retention economics | NYT Games: **11.2B plays in 2025** (Wordle alone 5.3B in 2024); the Games app gets more daily time than the News app; LinkedIn Games reports **84% next-day return**; a 2026 lifestyle piece documents couples bonding over shared daily puzzles ("'I nudged you!' has become part of our vocabulary") | Strong (company-reported) |
| Async turns inside an existing chat beat new destinations | GamePigeon: 20M+ installs, millions of games/day, iMessage-native (figures from a secondary stats blog — directionally reliable, not audited). Marco Polo (async video "walkie-talkie" built for far-apart families): **29M installs**, +1,147% sign-ups in the pandemic, zero paid marketing — word of mouth only | Moderate–strong |
| The weekly-prompt keepsake ritual prints money and meaning | StoryWorth: **1M+ books published**, $99/yr, one question a week for a year → hardcover. Remento (voice-first variant, Shark Tank deal): grandparent just talks; the printed book carries QR codes that replay their actual voice | Strong (a decade in business) |
| Voice is the family's native input | WhatsApp users send **~7 billion voice messages a day** (Meta, 2022); voice notes are the default where typing in a local script is slow. Grandparents who "hate writing will happily talk your ear off" — Remento's entire business rests on this | Strong |
| Intergenerational play needs a shared activity, not a call | Caribu (acquired by Mattel): grandparent–grandchild video playdates with shared books/games/drawing, used in 200+ countries. Its limit: the content is a publisher's library — nothing in it is *the family's own* | Moderate |
| Group-celebration rituals are a real, recurring market | Kudoboard (group cards for birthdays/farewells): "millions of employees around the world actively using the platform every month"; Tribute does the video-montage version. The ritual recurs on a calendar, forever | Moderate (vendor claims, plausible) |
| Playful AI works when the human performs and AI assists | Infinite Craft (an LLM combination game, originally Llama 2): tens of millions of players; the "First Discovery" label made players share. Google's Quick Draw and Gartic Phone (millions of monthly players) show drawing-with-others is a proven pleasure | Moderate–strong |

### The three failure lessons (these shape every candidate below)

1. **AI must never take the human's turn.** Gartic Phone shipped an AI drawing mode in 2024 and **removed it within roughly a day** after community backlash — players and artists said AI drawing for you "removes most of the fun and chaos." In a joy product, the human is the performer; AI is the referee, stagehand, illustrator of *your* material, and memory — never the artist, author, or friend.
2. **The robot must not interview Grandma.** A mainstream review roundup of family-story services explicitly rejected AI-robocall interviewers: "Why would you ask a robot to call Grandma? … Wall-E levels of sad." A *family member* asks and performs; AI works invisibly behind them.
3. **AI companions for kids are legally and reputationally toxic.** PIRG's 2025 *Trouble in Toyland* testing found an AI teddy (Kumma) giving dangerous and sexual content; California's SB 867 (signed Sept 2026) **bans AI companion-chatbot toys for under-16s for four years** from Jan 2027; Embodied's $800 Moxie robots were bricked when the company died, orphaning attached children. This lane connects humans to humans — the exact opposite bet.

**Design rules that follow:** (1) human-seeded, human-performed content only; (2) every session must mint a *shareable artifact* a human sends to another human (the Wordle grid, the Kudoboard invite, the printed book are the growth loops); (3) design for a *cadence* — daily, weekly, or calendar rituals — not a feed; (4) voice-first input, because Meta has **no TTS** — output is the humans' own recorded voices, device speech synthesis, text, or print; (5) character consistency is managed the way the owner already works on @v_do_stuff: a locked character sheet, SAM cut-outs of real drawings composited into scenes (the pixels persist), multi-image reference edits, and a Spark vision drift-check with bounded regeneration.

**Why "fun" scores on Impact here (30%):** Impact = breadth of relationships touched × emotional payload per session × cadence × keepsake permanence. Every candidate below is multi-person by construction — one user recruits 1–30 others. The problem statement is distance and drift between people who love each other; the retention evidence above is the proof it matters.

---

## The candidates

### 1. StoryRelay — a story that travels between two people

- **One-liner:** Grandpa records a 60-second chapter by voice; his granddaughter answers with the next one; every installment comes back as an illustrated storybook page starring characters they locked together — and a "Your turn" message that keeps the story, and them, going.
- **The joy and the relationship:** grandparent ↔ grandchild across distance (also parent ↔ child, aunt ↔ nephew). StoryWorth proved families pay for a weekly story ritual; StoryRelay makes it *play* — bidirectional, fictional, co-authored — instead of one-way memoir homework. The cliffhanger is the appointment.
- **How it works end-to-end:**
  1. The pair locks their cast once: the child draws the heroes on paper (photographed, cut out by SAM) or they describe them; a character sheet is built and frozen — the @v_do_stuff lock discipline, productized.
  2. Player A records a voice-note chapter (any mix of languages — Voice Transcribe's validated 25 languages with native code-switching is the Hinglish edge). Diarization separates the storyteller from background family.
  3. Muse Spark keeps the *story bible* (cast, places, open threads), lightly cleans the transcript into chapter text **in the teller's own words**, verifies continuity against the bible, and drafts the next cliffhanger prompt — addressed to the other player by name.
  4. Muse Image illustrates the chapter from the locked sheet (multi-image references); Spark vision drift-checks the cast against the sheet and regenerates bounded times; the hand-drawn hero cut-outs can be composited in so the child's own drawing literally persists across pages.
  5. The page — illustration, chapter text, and the original voice recording one tap away — goes to Player B: "Your turn." Monthly, the chapters bind into a printable book (with audio links per page, Remento-style).
- **Meta mapping:** **Voice Transcribe** — the input surface (async voice chapters, diarization, code-switching). **Muse Spark 1.3** — story bible, continuity verification, cliffhanger prompts. **SAM 3.1** — cut-outs of hand-drawn heroes, panel element masks. **Muse Image** — chapter illustration with edit-preserving multi-turn refinement. **Glimmer** (optional) — local story-bible keeper for the open-weights story.
- **Share mechanic:** the product *is* a message to one specific person; every chapter is an invitation. Finished books get shown to the whole family — each reader is a candidate pair.
- **Demo moment (20 s):** Split screen. In Delhi, a grandfather records "…and then the little robot opened the door, and guess WHO was inside—" in Hindi-English. In Fremont, his granddaughter listens, gasps, records her answer; the page renders with *her* paper robot in the illustrated doorway; his phone buzzes: "Your turn, Dada."
- **Scores:** Impact 9, Meta 9, Demo 9, Depth 8 → **8.8**. Impact justification: every family with distance is the market; two generations per install; weekly cadence with StoryWorth-grade evidence behind the ritual.
- **Incumbents & what's new:** StoryWorth/Remento (one-way, memoir, no reply loop, no fiction, no play); Caribu (live calls around a publisher's library — none of the content is the family's own); prompt-to-storybook generators (slop, single-player, no relationship). **New:** a bidirectional fiction relay where both humans author, AI only illustrates, remembers, and referees continuity.
- **Build sketch (~8 days):** PWA; voice-note upload → ASR batch + story-state JSON → chapter render pipeline (Image ~$0.01–0.03/page) → share link; print CSS for the book. Async throughout, so latency is a non-issue. **Biggest risks:** character consistency across chapters (mitigations in the design rules above — composite the real cut-outs, drift-check, forgiving painterly style); Hinglish ASR quality (spike day 1 with a real family conversation).
- **Relation to prior pool:** extends Drawing Studio (one child, one static book) into a two-player living ritual; the pipeline pieces already exist in the pool's research.

### 2. The Toast — a celebration comic the whole group secretly co-authors

- **One-liner:** For someone's birthday or farewell, every friend contributes one 20-second voice memory; the app turns the group into co-authors of a comic starring that person as the hero of their own year — one page they will actually keep.
- **The joy and the relationship:** friends group chat, coworkers, family — the Kudoboard/Tribute ritual (group cards used by millions monthly) upgraded from a grid of typed platitudes to a *story with the recipient in it*. Voice beats the blank text box — "I don't know what to write" is why group cards die; everyone can *tell* one 20-second story.
- **How it works end-to-end:**
  1. An organizer picks the person and occasion, shares one link. No installs — contributors land on a web page (Jackbox's no-friction lesson).
  2. Each contributor records one voice memory/roast/wish and may add one photo of the hero. Deadline nudges are automatic.
  3. Voice Transcribe diarizes and transcribes all contributions; Spark selects the best beats, assigns each to a panel (every panel credited to its contributor), and writes captions around the contributors' **real words** in speech bubbles.
  4. Spark + SAM build the hero's character sheet from the contributed photos (or, if likeness proves policy-blocked, a stylized avatar from the group's description — see risk). Muse Image renders 6–8 panels with the drift-check/regenerate loop.
  5. Organizer previews, hits send: the birthday person gets the comic page/carousel (printable poster optional). Every contributor automatically receives the final comic — they share it onward.
- **Meta mapping:** **Voice Transcribe** — many async contributors, diarized. **Muse Spark** — beat selection, storyboard, captioning, panel-vs-sheet verification. **SAM 3.1** — hero cut-outs and anchors from real photos. **Muse Image** — panel rendering with multi-image consistency. **Wonder** (optional) — richer storyboarding for big groups.
- **Share mechanic:** contribution *requires* inviting humans (the invite is the product), and the deliverable is inherently forwarded by every contributor. Birthdays, farewells, retirements, new babies recur on a calendar — the loop re-fires forever without marketing.
- **Demo moment (20 s):** Three friends' voice notes play over their panels appearing one by one — "remember the kayak incident—" — the birthday guy as comic hero, same face, same hoodie, panel after panel; the final panel is the whole group; his phone buzzes and he laughs out loud.
- **Scores:** Impact 8, Meta 9, Demo 9, Depth 7 → **8.3**. Impact: the occasions are universal and year-round; the payload (a keepsake vs. a disposable card) is the upgrade.
- **Incumbents & what's new:** Kudoboard (text board — no narrative, no hero), Tribute (video montage — camera-shy contributors skip it; stitching clips isn't a story), JibJab (face-in-template gags, dated), AI card generators (single-author slop). **New:** the group's spoken memories become a narrative comic with the recipient as its consistent hero.
- **Build sketch:** link-based contributor pages; batch ASR endpoint; storyboard JSON; the same illustration pipeline as StoryRelay. All pieces exist in the pool's research; the new engineering is multi-contributor orchestration (invites, reminders, dedupe, consent). **Biggest risks:** real-person likeness on Muse Image is untested (the Play to Comic research flags this — spike on day 1; fallback is the description-built avatar, which keeps the product intact); contributor completion (mitigated by one-tap voice + organizer deadline).
- **Relation to prior pool:** extends Faceless Studio from a solo persona to a group-authored celebration of a real, loved person — with the anti-slop guardrails Faceless itself demanded (human-authored, labelled, no mass production).

### 3. Doodle Duel — the drawing game where AI is the art department, never the artist

- **One-liner:** Everyone at the party draws the same absurd prompt on their phone in 60 seconds; Muse Image re-renders every scribble in one gorgeous shared style, the AI referee crowns the winners, and the night exports as a comic strip of your group.
- **The joy and the relationship:** friends at a party, family after dinner, coworkers on a call — the Jackbox shape (annual packs since 2014; room code, phones as controllers, no installs), rebuilt around the one thing Jackbox can't do: making everyone's terrible drawing *beautiful in the same style*.
- **How it works end-to-end:**
  1. Host opens a room, players join by code in the browser. A round begins: Spark deals a prompt tuned to the group (inside-joke categories the host seeds).
  2. Everyone finger-draws for 60 seconds. The drawings are 100% human — Gartic's backlash is the design law here.
  3. Each drawing goes to Muse Image as an edit with the round's shared style card (e.g. the warm storybook style); composition is preserved, rendering is elevated.
  4. SAM segments the drawn subject; Spark vision referees with a comic rubric — funniest, most accurate, most cursed — with one-line roasts on screen (device TTS optional), then the room votes to settle it.
  5. The round's gallery auto-composes into a comic page (the Play to Comic layout engine); the host sends it to the group chat/Instagram. Losers demand a rematch.
- **Meta mapping:** **Muse Image** — style-transfer edits are the magic trick (human input in, beautiful panel out, $0.01 each). **SAM 3.1** — subject segmentation for judging and layout. **Muse Spark** — prompt dealing, vision judging, roast copy, comic scripting. **Voice Transcribe** — optional shout-your-guess mode.
- **Share mechanic:** the gallery comic is the artifact; it names names and begs to be posted. New groups form around a room link.
- **Demo moment (20 s):** Four phones, one prompt — "Fluffy the dog filing his taxes." Four dreadful scribbles. Swipe: four painterly panels in one style, Fluffy at a tiny desk. The referee crowns "Most Cursed"; the room erupts; the comic page lands in the chat.
- **Scores:** Impact 7, Meta 8, Demo 10, Depth 6 → **7.8**. The before/after swipe is the most visibly fun three seconds in the entire pool; Impact rests on party games' proven mass ritual rather than emotional depth.
- **Incumbents & what's new:** Drawful/Jackbox (the drawings stay ugly — a different pleasure), Gartic Phone (browser telephone game — and its AI-mode fiasco proves this positioning), skribbl.io (no elevation, no artifact). **New:** AI as beautifier + referee of human drawings, multiplayer, same-room, with a keepsake export.
- **Build sketch:** WebSocket rooms; canvas drawing; image-edit calls (150 RPM is ample at party scale); reveal sequence is choreographed to absorb edit latency. **Biggest risks:** Muse Image edit latency is unpublished (measure in the spike; if slow, shrink rounds/players); style drift between players' renders (one shared style reference image per round); judging quality (human vote is the tiebreak, referee is comedy, not law).
- **Owner asset:** the house style can be @v_do_stuff's warm painterly look — the demo literally plays inside his comic universe, and any group can lock its own style the same way.

### 4. Home Movie Premiere — your family's archive becomes an event

- **One-liner:** Point it at an old family video and it returns a movie poster, a trailer-style program, and a premiere night — so the camera roll stops being storage guilt and becomes the best seat in the house.
- **The joy and the relationship:** the whole family, especially the elders *in* the footage. Nostalgia is a proven spend (digitization services, Skylight frames) — but those deliver files; nobody delivers the *occasion*.
- **How it works end-to-end:** Upload a clip (≤2 min by design). Spark watches it (native video) and picks 5 beats; Voice Transcribe diarizes the audio — who's laughing, who's narrating, sometimes a voice the family hasn't heard in years. SAM cuts the cast out of frames as anchors; Muse Image renders the poster ("THE GREAT CAKE INCIDENT — starring Dadi") and title cards. Premiere mode plays the beats with cards between them. Afterwards Spark drafts the group-chat message with one question only an elder can answer ("Dad — where was this filmed?"), turning the premiere into a conversation, not a viewing.
- **Meta mapping:** **Spark** video understanding (beat selection, program notes), **Voice Transcribe** (family-audio diarization), **SAM 3.1** (cast cut-outs, person tracking across the clip), **Muse Image** (poster, title cards).
- **Share mechanic:** the poster goes to the family chat; the closing question pulls elders into replying — the artifact *starts* a conversation.
- **Demo moment (20 s):** Grainy 2009 birthday video → poster reveal with Dadi as the star → the actual cake moment plays → grandma's reply lands in the chat with the story behind it.
- **Scores:** Impact 7, Meta 8, Demo 8, Depth 7 → **7.5**.
- **Incumbents & what's new:** Google Photos Memories (automatic, generic, no event, no elder loop); CapCut templates (manual labor); digitizers (files, not experiences). Play to Comic pointed this engine at sports; this points it at the archive that actually matters to people. **New:** the premiere framing + the elder-question loop.
- **Build sketch & risks:** reuse the Play to Comic pipeline wholesale (beat JSON → keyframes → stylized artifacts). Risks: video token cost on longer clips (sampling + the 2-minute design cap), likeness policy (stylized poster, consenting family), monthly rather than weekly cadence.

### 5. Our Puzzle — a daily mini-game made from your own shared life, for exactly two people

- **One-liner:** Every morning, you and your person get the same two-minute puzzle built from things only you two share — your photos, your inside jokes, your streak — plus a spoiler-free results card to send each other.
- **The joy and the relationship:** couple, best friends, parent ↔ adult child. NYT proved the daily puzzle is a relationship ritual; NYT's puzzles are generic. A puzzle about *us* is un-copyable and stickier.
- **How it works end-to-end:** The pair opts in once and seeds a small shared "fact file" in a playful week-1 ritual (how we met, the dog's birthday, the infamous kebab place), plus chosen shared photos. Daily, one format rotates: Connections-style grouping of 16 shared things; "Who said it?" from their real diarized voice notes; spot-the-difference on a photo twin (SAM finds the elements, Muse Image's edit-preserving generation changes exactly three). **Spark must solve its own generated puzzle and prove the solution is unique before it ships** — a verifiable-generation loop; Glimmer does the cheap daily drafting on open weights, Spark spot-checks (a real cost story for a daily product). Both play the identical puzzle; the results card is one tap to send.
- **Meta mapping:** **Spark** (generation, grading, self-solve verification), **Glimmer** (daily drafting — open-weights angle), **SAM + Muse Image** (difference twins), **Voice Transcribe** (voice-note formats).
- **Share mechanic:** the Wordle-grid mechanic transplanted into a relationship; the streak lives in their chat.
- **Demo moment (20 s):** Both phones buzz at breakfast: "Our Puzzle #43 — group these 16 things from Goa." She solves in 4 groups, he needs 6 tries; card sent; streak flame: 43.
- **Scores:** Impact 7, Meta 8, Demo 7, Depth 7 → **7.3**. Honest Impact note: growth is pair-by-pair (slow), but habit depth is the strongest retention shape in consumer software.
- **Incumbents & what's new:** NYT Games (generic, human-made), Paired/couples-question apps (prompts, no game, no artifact), Wordle clones (slop). **New:** a personal corpus + verified generation + two-player symmetry.
- **Build sketch & risks:** three template formats only; the verifier (self-solve + uniqueness) is the core engineering. Risks: generation quality *is* the product (template constraints + verification mitigate); cold start (the seeding ritual must itself be fun).

### 6. Table Tales — the dinner-table story game that arrives as tomorrow's comic

- **One-liner:** One phone in the middle of the table deals three picture cards from your own family photos; the table invents a story out loud, taking turns; next morning the story arrives as a comic page starring the family.
- **The joy and the relationship:** the household at dinner — parents and kids, roommates, the owner's own table. Zero installs, zero setup: the anti-app.
- **How it works end-to-end:** Muse Image generates three story-dice cards remixed from family photos (SAM cut-outs of the family dog, the house, the car). The phone listens (Voice Transcribe diarization attributes each turn to its teller); Spark keeps the plot coherent, deals a twist card mid-story ("suddenly, the doorbell rings"), and afterwards assembles the tale. By morning: a comic page in the locked family style, delivered to the group chat — the artifact that makes last night's silliness permanent.
- **Meta mapping:** **Voice Transcribe** (multi-speaker dinner-table diarization is the technical centerpiece), **Spark** (plot-keeping, twist dealing, comic script), **SAM** (photo cut-outs for cards), **Muse Image** (cards + morning comic).
- **Share mechanic:** the morning comic lands in the family chat; grandparents get sent the best ones — and ask how to play at their table.
- **Demo moment (20 s):** The card shows Fluffy in a superhero cape; a kid shouts the opening line; Dad derails it; the twist card lands; cut to morning — the comic of *their* story, word for word, in the chat.
- **Scores:** Impact 6, Meta 8, Demo 8, Depth 7 → **7.2**.
- **Incumbents & what's new:** story-dice toys (physical, no memory, no artifact), "Your day as a comic" from the magical-ideas pass (passive recap — nobody performs). **New:** the table performs; the product remembers and illustrates. Honest overlap: it shares StoryRelay's engine — same pipeline, different room (one table vs. two time zones). Build one, and this is a mode, not a second product.

---

## Scorecard

| Rank | Candidate | Impact | Meta | Demo | Depth | Weighted | Cadence | Core relationship |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **StoryRelay** | 9 | 9 | 9 | 8 | **8.8** | Weekly | Grandparent ↔ grandchild |
| 2 | **The Toast** | 8 | 9 | 9 | 7 | **8.3** | Calendar (birthdays, farewells) | Friends / coworkers / family |
| 3 | **Doodle Duel** | 7 | 8 | 10 | 6 | **7.8** | Every game night | Friends / family, same room |
| 4 | Home Movie Premiere | 7 | 8 | 8 | 7 | 7.5 | Monthly | Whole family + elders |
| 5 | Our Puzzle | 7 | 8 | 7 | 7 | 7.3 | Daily | Couple / best friends |
| 6 | Table Tales | 6 | 8 | 8 | 7 | 7.2 | Weekly | Household at dinner |

Bonus-prize fit (the rules allow bonus categories such as most-viral and community vote): Doodle Duel and The Toast have the strongest viral shapes; StoryRelay is the community-vote and emotional-resonance play; all three are Muse Image-heavy, suiting a creative-build bonus.

## Top 3

1. **StoryRelay (8.8)** — the only candidate with a *proven paid ritual* behind it (StoryWorth's decade, 1M+ books) that nobody has made bidirectional and playful. Four Meta products are each load-bearing; the demo is two real people in two places making each other laugh; the owner's locked-character craft from @v_do_stuff is a genuine, visible asset. It beats Drawing Studio by adding the second human and the reply loop.
2. **The Toast (8.3)** — the strongest *growth* shape in the lane: the invite is the product, the calendar is the marketing department, and Kudoboard's millions prove the ritual. It beats Faceless Studio by making the persona a real loved person and the authors a group.
3. **Doodle Duel (7.8)** — the best 20 seconds of demo in the pool and a Jackbox-proven format with one capability Jackbox lacks. Its positioning is evidence-hardened: Gartic's AI-mode backlash is exactly the mistake this design refuses to make.

**Suggested combination, if the judges' appetite allows one product with modes:** StoryRelay as the product; Table Tales is a same-engine mode (one table instead of two time zones); Doodle Duel's style-card mechanic is the same illustration pipeline pointed at a party. Build the pipeline once — locked cast, drift-checked illustration, diarized voice in — and all three demos run on it.

## Killed territories

| Territory | Why killed |
| --- | --- |
| **AI companion / AI friend, incl. chatbot toys for kids** | PIRG 2025 findings (Kumma's dangerous and sexual answers); California SB 867 bans companion-chatbot toys for under-16s (2027–2030); Moxie's $800 bricking orphaned attached kids. Also the opposite of the brief: it replaces humans instead of connecting them |
| **AI that draws/writes *for* the player** | Gartic Phone's AI mode was pulled within ~a day in 2024 after artist/player backlash — "getting an AI to do the drawing for you removes most of the fun and chaos." The creative turn belongs to the human |
| **AI-interviews-grandma services** (robot as interviewer) | Rejected by the memoir market's own reviewers ("Why would you ask a robot to call Grandma?"). Humans ask; AI assists invisibly |
| **Prompt-to-storybook generators** ("type a name, get a book") | Dozens of startups, pure slop, no relationship, no ritual, no second human. Drawing Studio's human-drawn version already beats it inside our own pool |
| **Talking-avatar greetings / AI video messages** | HeyGen-class saturation, uncanny output, and real-person face/voice cloning is the misuse profile Meta itself avoids; the Faceless research already found this category funded and generic |
| **Watch-together clones** | Teleparty/SharePlay solved sync; zero Meta-model depth. The value lives in the artifact *around* watching — kept only as Home Movie Premiere's framing |
| **AI party DJ / shared-playlist generators** | Spotify and YouTube own the rails; this stack cannot generate music; the demo is invisible |
| **Affirmation / AI-listener journaling** | Therapy-adjacent (avoid list), Character.AI reputational blast radius, and structurally just the companion pattern with extra steps |
| **Generic AI meme generators** | A slop firehose with no retention evidence and no relationship; memes work when a human makes one about *their* group |

## Day-one spikes for this lane

1. **Consistency:** one hand-drawn character → character sheet → 6 Muse Image scenes. Pass: recognizably the same character in ≥5 of 6. (Decides StoryRelay, Toast, Table Tales — same spike the Faceless research demanded.)
2. **Latency:** time a Muse Image edit end-to-end. (Decides Doodle Duel's round design.)
3. **Likeness policy:** run a real, consented person's photo through Muse Image edits. Pass/fail decides Toast's hero: photo-anchored sheet vs. description-built avatar.
4. **Voice:** one real Hinglish family conversation through Voice Transcribe. Pass: diarization and transcript good enough that the story survives. (Decides StoryRelay's input quality and Table Tales' centerpiece.)
