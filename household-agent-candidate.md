# Household "chief of staff" agent: candidate evaluation

> Updated: sections 5 and G assume local Glimmer, which is superseded by section K (no GPU; hosted Glimmer for Oct 31, local as a documented path). The latest scores and ranking are in `ranked-candidates.md`.

2026-10-26. Scores and probabilities are my judgement, not data. Web findings come from search summaries and third-party articles, not Instinct's own documentation (none is public, see below). Anything I could not verify is marked **Unverified**.

## Bottom line

This is the best idea of the three as a long-term passion project, and a risky one as a three-minute hackathon demo. Instinct is already a $10B company doing the generic version of this, so a generic "household agent" would lose on Impact and novelty. The idea only works if it is narrowed to the gap Vibhor named: **zero-setup ramp-up and nudging that does not annoy**, plus a **local-first privacy story** that Instinct structurally cannot offer. My recommendation is at the end: keep the cooking guide as the lead for the hackathon, unless Vibhor weights "I will still use this in December" above the rubric, in which case build the household agent narrowed as below. A cheap way to decide is in the last section.

## 1. What Instinct is, and what I could and could not verify

**Verified from multiple third-party sources (reviews, news, founder posts reported by press):**
- Personal agent from Spear Street Technology (founder Noah Shinn). Invite-only beta. You text it on iMessage or WhatsApp or call it. It uses its own cloud computer and connects to Google Workspace (Gmail, Calendar, Drive). Logins can sit in a Vault and purchases go through Stripe Link. [eesel review](https://www.eesel.ai/blog/instinct-ai-review)
- Proactive: it texts or calls first, follows up on dropped threads, reminds you of things you forgot. Early users report real pain from over-eagerness: it sent an email without approval and pinged a reservation site hundreds of times an hour, getting an investor's account banned. [Carly summary](https://www.usecarly.com/blog/what-is-instinct-ai/)
- Reported friction is not setup but **thread sprawl and reliability**: one thread gets crowded, 13 messages for an Amazon order, outages in September with no status page, brittle browser flows (CAPTCHAs, 2FA).
- Trusted-person network: your Instinct coordinates with Instincts of people you approve (the founder reported over 300k coordinations in the first week). [eesel review](https://www.eesel.ai/blog/instinct-ai-review)
- Group chats (announced Oct 5, 2026): an Instinct joins a group chat, including with people who have no account, and your personal agent asks permission before sharing. Early access only. [AI Weekly](https://aiweekly.co/alerts/instinct-opens-ai-agent-to-group-chats-with-non-users-after-hitting-10b-series), [AI Chief](https://aichief.com/news/instinct-expands-ai-agent-to-group-chats-works-without-account-requirements/)
- Terms (per reviews): you appoint it your agent and its agreements bind you; model training on your data is on by default (opt-out); disconnecting does not delete indexed data. This is the basis of the privacy gap below.

**Could not verify:**
- Instinct's own docs. [instinct.com](https://instinct.com) has marketing copy and a login only. No public docs, API, or pricing. I did not find any setting for nudge frequency or quiet hours.
- Whether it reads photos of a whiteboard, merges a weekly plan from scattered sources, or has anything like a "bad day" mode. Absence from reviews is not proof it cannot.
- What Vibhor actually sees in his own account. **His first-hand experience of setup and nudge tuning is better evidence than anything I found.** Ask him which steps were hard.

**Does the evidence support his "setup and remembering" gap?** Only partly. Instinct's pitch is explicitly "no configuration," and reviews do not complain about setup. The documented pain is over-nudging and sprawl, which supports a "nudging that knows when to stop" gap more than a "setup" gap. Group chats with non-users also partly address "wife will not use agent tools." So the gap is a hypothesis to test with Vibhor, not a finding.

## 2. Similar products (commercial and open source)

| Product | What it is | Note |
| --- | --- | --- |
| [Instinct](https://www.eesel.ai/blog/instinct-ai-review) | Invite-only general personal agent via text/call | Cloud, training on by default |
| Zazu AI | Reads email and calendar with family permission, handles school deadlines, groceries, carpools in WhatsApp/iMessage | Closest to the household use case; vendor claims |
| Housemait | WhatsApp bot, plain-English events, tasks, shopping, meal plans, transcribed voice notes | Voice-note capture already exists |
| Sense | Turns emails, photos, screenshots, WhatsApp, PDFs, voice into shared calendar events | Overlaps the whiteboard-photo idea |
| Ohai | Coordinates calendars, chores, meals for a family; from $9.99/month | |
| Dinnerbell | Agentic assistant across family calendar, grocery, to-dos, meal planning (launched April 2026) | App, SMS, email |
| Pally, Orbits, FamPilot, Fami, Family Folder | Cross-app connection, chore reminders, meal-to-grocery, conventional organizers | |
| [OpenClaw](https://blog.openreplay.com/openclaw-open-source-ai-assistant/) | Open-source (MIT), self-hosted agent; connects a model of your choice to files, browser, and WhatsApp, Telegram, Signal, iMessage and more; can run on local models via Ollama | Guides flag security problems; models under 14B reportedly unstable at tool calling |
| Vellum | Open-source assistant as a desktop app (vendor's own description) | |

Sources: [Instinct-adjacent roundup and family organizer search](https://techcrunch.com/2026/10/10/all-the-ai-agents-that-can-live-in-your-text-messages/) (the page returned 404 when fetched, I only saw the search summary), vendor pages. Pricing, privacy terms and whether WhatsApp products use the official Business API are **Unverified**.

**Read:** the generic category is crowded and funded. What I did not find is a household agent that is **local-first**, and none I could confirm that **builds the week from artifacts that already exist** (a whiteboard photo, a pile of forwarded messages) instead of asking the user to configure it.

## 3. Evaluation against the rubric and rules

### Discouraged-project list (avoid: AI medical or mental-health advice, basic RAG, simple image analyzers, education chatbots, job screeners, nutrition coaches, personality analyzers, sports analyzers, political or war)
| Risk | Why | Handling |
| --- | --- | --- |
| Mental-health adjacency | "Bad day" mode and fights over dinner sound like relationship counseling | Make "bad day" a scheduling action only: drop plan, silence nudges, re-plan. No mood detection, no advice, no analysis of the spouse. |
| Nutrition coach | Meal planning | No calories, diets or health claims. Meals are slots on a calendar. |
| Simple image analyzer | Whiteboard photo to JSON | The photo is one input to a persistent state and action loop, not the product. |
| Basic RAG | "Ask about my week" over messages | Avoid a Q&A framing; the agent acts (reminders, list updates, re-plans). |
| Personality analyzer | Wife prefers talking to him; tempting to model her | Do not model her preferences or messages. Hard rule. |

Rule risk is **medium**, manageable by scope. Ask in office hours before building the "bad day" part.

### Judging rubric (my scores, 0 to 10)
| Criterion | Score | Reasoning |
| --- | --- | --- |
| Impact (30%) | 6 | Real and universal, fits "Build for Your World," but reads as convenience. The strongest Impact argument is **private, local household AI plus fewer evening conflicts**, and that needs evidence I do not have. Crowded category. |
| Meta tooling (25%) | 7 | Spark vision for whiteboard photos, structured output, tool calling, Voice Transcribe, optional Glimmer local. Not SAM or video heavy. |
| Demo (25%) | 6 | Demo-able: whiteboard photo to a week view, a voice dump, a bad-day button, a nudge. But the payoff is "nothing went wrong this evening," which is hard to show, and real household data and a spouse cannot go in a public video without consent and redaction. |
| Depth (20%) | 7 | Persistent state, multi-source merge, conflict detection, nudge policy, tools. Depth is available, execution risk is in integrations. |
| **Weighted** | **about 6.5** | |

### Bonus prizes
- **Best Agentic Use-Case ($5K):** plausible fit.
- **Best Build on Open Weights ($10K):** strongest fit of any candidate if run on Glimmer locally (see section 5).
- **Most Viral ($20K):** weak. Personal-life agents are hard to make shareable. A two-agent "settle dinner" clip could travel, but it is a stretch.

### Buildable solo by Oct 31
Core is buildable. Integrations decide it:
- **Channel:** a Telegram bot is the easiest way to get forwarded messages, voice notes and photos with push nudges. **WhatsApp:** the official Business API needs business setup and cannot read his existing chats. Unofficial libraries exist but risk account bans (**Unverified**, from general knowledge, not checked in this session). **iMessage:** no official API, needs a Mac (**Unverified**). So "forward it to the bot" is the realistic capture path. That is also less magic than he wants.
- **Alexa list:** third-party access was cut by Amazon in 2024, and AnyList reports sync is still broken in 2026. [AnyList](https://help.anylist.com/articles/alexa-issue-early-2026/), [Galaxus](https://galaxus.it/en/page/alexa-amazon-makes-life-difficult-for-suppliers-like-bring-33803). Treat Alexa as unreachable. Use the bot's own list, or his phone shares into it.
- **Calendar:** Google Calendar API is feasible; "outdated shared calendar" write access depends on his setup.
- **Evaluation:** no day-1 go/no-go test exists yet for the whiteboard read. Photo handwriting accuracy with Spark is **untested**.

## 4. Demo concept (3 minutes)

1. 0:00 to 0:25: Tuesday, 5:40 PM, nobody knows what is for dinner. The whiteboard says one thing, the calendar another.
2. 0:25 to 1:05: he photographs the whiteboard and forwards a screenshot and a voice note. One picture of the week appears (meals, chores, workouts, conflicts flagged). Groceries sync to the list.
3. 1:05 to 1:50: a gentle nudge at the right time ("chicken needs to thaw by 4"). Shows quiet hours and a nudge budget.
4. 1:50 to 2:25: bad day. One tap: plan dropped, nudges silenced, tonight re-planned with zero guilt, tomorrow reshuffled.
5. 2:25 to 3:00: privacy beat (everything on his own machine, a network log showing what left) and, if built, her agent joining and the two converging on a meal.

## 5. Local-first: can he build this, and what is the real privacy story

**Feasibility.** Mostly yes, with caveats.
- **Model:** Glimmer (project notes: meta-open-weights-deploy) (30B dense, text and image in, Apache 2.0, 128K context). The Q4_K_M GGUF is 16.8 GB plus a 1.4 GB vision file, and runs on a single 24 GB GPU via llama.cpp (about 19 GiB at 131K context). It supports tool calls and images (so whiteboard photos work), via an OpenAI-compatible server. Reasoning cannot be turned off, so replies are slower than the hosted API.
- **Hardware:** one 24 GB GPU (RTX 3090/4090 class). A Mac with 32 GB or more unified memory should also work but I have not verified Glimmer speed there. CPU or mixed is possible but slow. If he lacks one, rent a 24 GB GPU for the build (Modal credit $100) or use Fireworks-hosted Glimmer as a stand-in. A hosted stand-in is not local, so be honest about that in the demo.
- **Local store:** SQLite on his machine for the week, lists, nudge history and consent rules. Local web app or Telegram bot process.
- **Speech:** Muse Voice Transcribe is API only. A local alternative such as Whisper is a different vendor's model; it is fine for privacy but counts less toward "uses Meta tools." **Unverified** whether Voice Transcribe is open weights (I found no sign it is).
- **SAM 3.1:** API only, not needed here.
- **Cloud pieces still needed:** Telegram or WhatsApp is a third-party relay (messages pass through their servers). Calendar sync talks to Google. Web search grounding is a Meta API feature, so a local agent would use its own search tool, which sends the query out.

**What the privacy story honestly is.**
- If everything runs on Glimmer locally, then model inference never leaves his machine. That is a real and rare claim.
- The message channel is the weak point. Telegram bots are not end-to-end encrypted, and WhatsApp's encryption stops at the bot. So "data never leaves my machine" is false if capture goes through a chat app. Accurate claim: **"the model and memory are local; the chat app and calendar are the only external hops, and we show exactly what crosses."**
- If hard cases go to Meta's API (hybrid: Glimmer local, Spark for the hardest handwriting), those prompts leave the machine. Standard mode keeps prompts out of training per the docs, but they still leave. Minimizing it: send only the whiteboard crop, not messages, and show a log. Do not call a hybrid "private" without that qualifier.
- The "do not trust big tech" position and the "uses Meta's API" requirement are in tension. The honest resolution is: local by default, API as an opt-in per call with a visible log. That is also a good demo beat.

**Open-weights bonus ($10K).** Running the whole agent on Glimmer locally is the cleanest possible entry, and probably this idea's biggest advantage over the cooking guide, whose live video loop is too slow for a local 30B model. The pairing pattern (Glimmer local plus Spark for hard steps) is documented in project notes meta-sam-and-cookbook.

**By Oct 31.** Realistic: Glimmer via llama.cpp, SQLite store, Telegram bot, whiteboard photo to structured week, voice via Voice Transcribe (API), one nudge policy, bad-day action. Not realistic: reading his WhatsApp or iMessage history, Alexa, her agent joining. Spark Open (816B) is not locally runnable.

## 6. The real gap, stated carefully (hypothesis)

1. **Cold start from what already exists.** Instinct and Housemait start with "tell it things." A household's truth already lives on a whiteboard and in message threads. An agent that builds the week from a photo and a forward, with no configuration, attacks the ramp-up barrier. **Unverified** that nobody does this: Sense takes photos and screenshots.
2. **Nudging with a built-in exit.** Instinct's documented failure mode is over-eagerness. Nudge budgets, quiet hours, and the bad-day exit are a differentiator I could not find elsewhere.
3. **Local-first household memory**, which a $10B cloud product cannot offer given its training-on-by-default terms.
4. **A neutral party for two people.** Agent-to-agent convergence exists in Instinct's trusted network, but it is unconfirmed for household meal decisions. Stretch tier.

## 7. Tier plan (guaranteed entry, then stretch)

- **Tier 0 (safe entry, by Oct 29):** Telegram bot or local web app; photo of whiteboard or forwarded text to a structured week via Spark 1.3 (hosted); SQLite store; grocery list; one nudge. Public repo, deployed, demo-able.
- **Tier 1 (by Oct 31):** Glimmer local as the default model with a visible "what left the machine" log; voice notes via Voice Transcribe; nudge budget and quiet hours; bad-day exit that re-plans; conflict flags.
- **Tier 2 (stretch, only if Tier 1 is solid):** second agent for the spouse, with consent, converging on a meal; shareable weekly summary; Google Calendar write sync.

## 8. Three-way comparison and recommendation

| | Cooking live guide | Immigration copilot | Household chief of staff |
| --- | --- | --- | --- |
| Weighted score (mine) | about 7.4 to 8.3 depending on framing | about 7.2 | about 6.5 |
| Demo strength | Highest (live attempt, real expert voice) | Lowest | Medium, privacy-limited |
| Meta tooling | Highest (video, SAM, voice, Glimmer optional) | Good, Glimmer local fits well | Good, Glimmer local fits best |
| Open-weights bonus | Weak (video loop too slow locally) | Good | Best |
| Rule risk | Coach and analyzer risk | Legal, political, sensitive data | Mental-health, nutrition, image analyzer adjacent |
| Competition | Low | Crowded | Very crowded, funded |
| Build risk by Oct 31 | Live lag and accuracy, untested | Lowest | Integrations (channel, Alexa, calendar) |
| Long-term personal use | Occasional | Only if he has a case | **Highest** |

**Recommendation.**
1. For winning the hackathon, keep the **cooking guide** as the lead. It has the best demo and rubric fit, and the day-1 test already exists.
2. If Vibhor's priority is a project he keeps using (the hackathon's core ask), the household agent is the one, **but only in the narrowed form** (cold-start from the whiteboard, nudge budget with bad-day exit, local-first on Glimmer). The generic version should not be built.
3. Do not build it as an Instinct competitor. Position it as the local, quiet layer, and note in the demo that it can sit alongside tools like Instinct.

**Cheapest way to decide today:** run two spikes before committing. (a) Photograph the real whiteboard and send it to Spark 1.3 and to local Glimmer, and check how accurately each reads meals, chores and workouts. (b) Ask Vibhor which exact Instinct steps felt like ramp-up and which nudges felt wrong, since that is the evidence I could not get. If the whiteboard read is poor, drop this idea. If it is good and he has a 24 GB GPU, it moves up.

## Questions for Vibhor
- Which Instinct steps were the setup burden, and which nudges were off?
- Does he have a 24 GB GPU or a Mac with 32 GB or more?
- Is Telegram acceptable as the capture channel, or does it need to be WhatsApp or iMessage?

---

# Pass 2 (deep dive, 2026-10-26 evening)

What changed after reading primary pages and re-reading the interview in the project chat. Items marked **Unverified** were not confirmed from a primary source.

## A. What the interview adds (design inputs, Vibhor's own words)
- The failing system is a **weekly whiteboard** that works when the week is calm and dies when travel reshuffles it. The failure is manual upkeep, not the idea of a board.
- Information is spread across six places: his wife's head, WhatsApp, email, regular chat, Alexa voice list, and the board. A shared calendar was tried and went stale.
- He wants the board to stay the home base (eyes-on), the phone to nudge gently, and nudging to stay quiet enough not to annoy. He said a photo of the board would not feel like a chore **if the agent nudges him to take it**.
- He wants an **emergency exit** for a bad day, then a guilt-free return to the plan.
- He wants a **neutral third party** that talks to each of them and helps them converge, and he said he does not know what coming back on track looks like. That is an open design question, not a requirement.
- The dinner fight was a coordination miss at a moment of fatigue, not a planning failure: one person was working to a deadline, the other did not register it.

## B. Reachability, from primary or near-primary sources
| Channel | What is actually reachable | Source and confidence |
| --- | --- | --- |
| WhatsApp (personal chats) | Only via unofficial WhatsApp Web libraries (OpenClaw uses Baileys, QR pairing only, a separate number is recommended, self-chat quirks documented). The OpenClaw docs do **not** discuss ban risk. Secondary sources say unofficial libraries risk account bans. | [OpenClaw WhatsApp docs](https://docs.openclaw.ai/channels/whatsapp) (primary for how it works); ban risk is [secondary](https://zylos.ai/research/2026-01-26-whatsapp-api-automation), Unverified against Meta's terms |
| WhatsApp (official API) | A secondary source says Meta's policy effective Jan 15, 2026 bars general-purpose AI assistants from the Business Platform. | Secondary, Unverified. Check Meta's WhatsApp Business terms before relying on it. |
| iMessage | Needs a Mac that stays awake; OpenClaw's current docs drive the `imsg` tool directly and say BlueBubbles support was dropped; mirrors of older docs disagree. | [OpenClaw docs](https://docs.openclaw.ai/channels/imessage-from-bluebubbles), moderate confidence |
| Telegram | Bots receive your messages because cloud chats are not end-to-end encrypted; Telegram holds the content. | Secondary explainers; the official FAQ at core.telegram.org/techfaq was not opened, so Unverified |
| Alexa shopping list | No third-party API. Amazon cut it in 2024 and AnyList still reports it broken in 2026. | [AnyList](https://help.anylist.com/articles/alexa-issue-early-2026/), good |
| Email and calendar | Gmail and Google Calendar have official APIs (OAuth); not re-verified today. | General knowledge, Unverified in this pass |

**Implication.** There is no clean, official, private way to listen to his existing WhatsApp and iMessage threads. The honest capture path is **forward, share, or photograph into the agent**, which matches what he described wanting (photo of the board, forwarded messages). Do not promise "listens to how you already talk." Also: ingesting his wife's messages needs her consent. Design for what **he** forwards.

## C. OpenClaw, the closest open-source reference
From its [GitHub README](https://github.com/openclaw/openclaw) (I read about 94% of the page): MIT licence; a local **Gateway** is the control plane for sessions, tools, events and channels; "state, memory, and credentials live on your hardware"; models and harnesses are swappable plugins including local models; unknown senders are paired by default and inbound messages are treated as untrusted; tools run on the host unless sandboxed; a daily version check is on by default and can be turned off. Setup is `openclaw onboard --install-daemon`, Node 24.16 or newer. The README does not describe the memory format, and the issue tracker has over 5,000 entries. Security reports from third parties are mixed and I did not verify them. Takeaways: (1) a local gateway plus swappable model is the right shape; (2) "policy enforced by code, not by the model" is a design principle worth copying for nudging; (3) OpenClaw is a general platform with significant setup, which is the exact "ramp-up" gap Vibhor named, so a narrow, near-zero-setup household product is differentiated from it.

## D. Instinct privacy, retested
I could not open Instinct's privacy policy or terms (the page returned only a title), so the training-on-by-default and non-deletion claims in section 1 rest on [one review](https://www.eesel.ai/blog/instinct-ai-review). **Unverified against the primary text.** Say that in any public claim.

## E. Why shared calendars and planners die (evidence status)
I found **no peer-reviewed study** in this pass. What exists is vendor marketing: for example a vendor survey of 93 mothers where only 11% used a shared app and the rest relied on WhatsApp notes-to-self (42%), fridge notes (39%) or nothing (20%) ([RemindHer](https://remindher.app/how-to-start-shared-family-calendar/), self-reported, tiny sample, **weak**). Widely repeated figures such as 71% of mental load falling on mothers could not be traced to a primary source here. A literature pass is running in parallel; treat the above as anecdotal until it reports. The strongest evidence for the design is Vibhor's own account.

## F. Glimmer feasibility check
- Confirmed from the [Glimmer page](https://dev.meta.ai/docs/muse-glimmer): 30B dense, text and image in, Apache 2.0, 128K context, 100+ languages, "built for local agentic workflows", runs on vLLM, SGLang, llama.cpp, Ollama.
- Confirmed from the deploy notes already in project memory: tool calling works on llama.cpp, images are accepted, reasoning cannot be turned off (so replies are slow), a 24 GB GPU holds the Q4_K_M model with about 19 GiB at 131K context.
- **Not known:** handwriting and whiteboard OCR accuracy, whether llama.cpp enforces a JSON schema for Glimmer, speed per photo. The Glimmer page publishes no benchmark numbers. The whiteboard spike below is the only way to find out.

## G. Architecture (local-first, hybrid by consent)
```
 Telegram bot / local web page  <-- photo, forward, voice note, taps
            |
   Gateway process (Python or Node) on his machine
     |-- Policy engine (CODE, not model): nudge budget, quiet hours,
     |     bad-day state, snooze decay, confirm-before-write
     |-- Tools: read_week, upsert_item, add_grocery, schedule_nudge,
     |     set_bad_day, propose_replan, ask_user
     |-- SQLite: week, items, groceries, nudge log, consent rules
     |-- Model client (OpenAI-compatible)
     |      default: local Glimmer via llama.cpp (port 8080)
     |      escalate: Spark API only after he approves the exact payload,
     |                every call logged (the cookbook "asks first" pattern)
     '-- Voice: Muse Voice Transcribe (API) or local Whisper (non-Meta)
```
The model proposes; code decides whether to speak. Whiteboard flow: photo, then Glimmer reads it into a structured week, then the diff against last week is shown back as a short confirm card ("I read Thu dinner as broccoli paratha, right?"). Low-confidence cells are asked about, not guessed.

**Privacy claim to make:** model, memory and nudge policy are local; the chat relay (Telegram) and calendar sync are the only external hops; any Meta API call is opt-in per call and logged. Telegram is not a private channel, so do not call the system "private end to end."

## H. Open question the demo must answer: "live product"
The judging guide says the demo video is the main artifact alongside code and a live product. A purely local app has no URL. Plan: a **hosted demo mode with synthetic data** (Vercel or Modal) plus a one-command local install, and ask Meta in office hours (Discord, 10 to 11 AM ET, weekdays) whether a local-only product satisfies "live product." **Unverified** what the official rules require.

## I. Day-by-day plan to the Oct 31 freeze
Product code starts Oct 27 (building-period rule). Tier 0 must be submittable by Oct 29.

| Date | Goal | Exit test |
| --- | --- | --- |
| Oct 26 (today, throwaway spikes) | Photograph the real whiteboard 5 ways. Send to Spark 1.3 and to Glimmer (local if he has the GPU, otherwise a hosted Glimmer as a stand-in). Compare cell-level accuracy for meals, chores, workouts, groceries. Time one call. | Pass: at least 85% of cells right on Spark, at least 70% on Glimmer, with wrong cells flagged low-confidence. If Spark fails, drop the idea. |
| Oct 27 | Create the public build repo. SQLite schema. Telegram bot skeleton. Whiteboard photo to week via Spark. Confirm card. Attend Agents 101. | Photo in, correct week out, edits saved. |
| Oct 28 | Grocery list from the week and from voice notes. Policy engine (nudge budget, quiet hours). First nudge ("take a photo of the board"). Attend Agents 102 (verifiable agents) and add abstain-and-ask. | A day with at most 2 nudges, all logged. |
| Oct 29 | **Tier 0 submitted**: hosted demo with synthetic data, repo, README, rough video. | Submission accepted. |
| Oct 30 | Tier 1: Glimmer as default model, egress log, bad-day exit with re-plan, conflict flags (travel vs dinner). Attend Fireworks session. | Bad-day replay works on the synthetic week. |
| Oct 31 | Hardening, spend cap, privacy page, demo data. Tier 2 only if Tier 1 is solid. **Feature freeze at end of day.** | Full dry run of the demo script. |
| Nov 1 to 3 | Script, record, edit, submit. | |

## J. Updated honest read
- The single biggest risk is not the model, it is **capture**: with no clean WhatsApp, iMessage or Alexa path, the product depends on him remembering to photograph and forward things, which is the exact failure he described. The gentle nudge to photograph the board is therefore the core mechanic, not a nicety. If that loop does not feel good in a week of real use, the product has not solved his problem.
- The strongest reason to build it is personal fit and the local-first, open-weights angle. The strongest reason not to is a thin demo payoff. Both stand from pass 1.
- The recommendation from section 8 is unchanged: cooking guide leads for the rubric, this one if long-term use outweighs the score.

## K. Hardware update (Vibhor, Oct 26)
He has no 24 GB GPU and none soon; a Mac is possible next month. For Oct 31, Glimmer runs on a hosted endpoint, so section G's "default: local Glimmer" becomes "default: hosted Glimmer, same OpenAI-compatible client, switchable to local by changing the base URL." The honest privacy line is: open weights, memory in his own SQLite file, every outbound call logged, and a documented local path (Glimmer Q4 about 16.8 GB, Apple Silicon with enough unified memory, **speed and support unverified**). See `ranked-candidates.md` for the full note. The Tier 1 plan item for Oct 30 changes from "Glimmer local" to "Glimmer hosted plus the egress log and base-URL switch."
