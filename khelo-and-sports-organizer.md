# Khelo, its competitors, and a sports-organizer agent for the hackathon

2026-10-26. Read from the `vibhortayal/khelo` repo (README, CLAUDE.md, docs/PLAN.md, decision-log.md; I did not read the code) and the landing pages of the competitors Vibhor listed. Competitor facts are from marketing pages only, so **vendor claims are unverified**. Playtomic returned 403 and was not read.

## What Khelo is today (from its own docs)
- A PWA (Next.js 15, React 19, Supabase, Vercel) to find players, log games and run tournaments. Launch plan: a **table tennis pilot** with casual games; first 100 users planned for Fremont (decision log #4, later amended).
- Core idea: a **community replaces the WhatsApp group**. Fun score entry (opponent confirms or disputes), emoji banter, five badges, virtual bets with weekly points, leaderboard, invite-link join.
- Status: Run A (mock-data preview) done. Run B (real backend) has sign-in, communities, games, reactions and comments, badges and bets merged; **B7b (staging setup) and B8 (pilot launch) are not done**. **Tournaments are slice 3, not built.** Open game requests are slice 2, not built.
- Repo created around Oct 20, so it predates the hackathon's Oct 27 start.

## Competitors (landing pages only)
| Product | What it is | AI mentioned on the page |
| --- | --- | --- |
| [Playinga](https://playinga.com/en/) | Sports social network and management: registration, brackets, round-robin and group scheduler, real-time scoring, standings; white-label licence for clubs and federations; claims 75+ sports and 120K+ teams | No |
| [Crewters](https://crewters.com) | Sports social network (iOS, waitlist): swipe matching, pickup games, leagues with auto-generated fixtures, live streaming, peer ratings, scout discovery | No |
| [Bantr](https://www.bantrsports.com/) | Adult recreational league management: messaging, RSVPs, registration, stats, captain fee collection | No |
| [SportsVybe](https://sportsvybe.com/) | Venue booking and facility management (tagline only; tournaments and matchmaking not described) | Not shown |
| [Playtomic](https://app.playtomic.com/) | Not read (403). From general knowledge it is a racquet-sports court booking and matchmaking app; **unverified here** | Unknown |

**Read:** the tournament and league category is crowded and funded, and Playinga already covers brackets and scheduling at scale. None of the pages I read advertise AI, which suggests an AI-native angle is open, though a landing page is weak evidence of what is inside the products.

## Where Khelo is different
Community as a WhatsApp replacement, casual-game banter and bets, small-group warmth. That is a social product, not a bracket engine, so Khelo should not compete head on with Playinga's tournament tooling.

## Where Meta models could fit (hypotheses, untested)
1. **Voice or photo score entry.** "Me and Raj beat Sam and Joe twenty-one seventeen." Voice Transcribe plus Spark extracts players, teams and score, then the opponent still confirms (Khelo already has confirm and dispute). It removes the main friction in the pilot's core loop.
2. **WhatsApp-to-game.** A pasted or forwarded group message ("anyone up for doubles Thursday 7?") becomes an open game request (Khelo slice 2). Same reachability limits as the household agent: forward or paste, not read WhatsApp.
3. **Live session director** for a round-robin or Americano evening: late arrivals, court counts, rotation fairness, spoken announcements. Prior art is deterministic scheduling ([PlayMore](https://www.playpickleball.com/playmore-app-pickleball-scheduling-round-robin/) and others, from the earlier search); whether any use an LLM live is unverified.
4. **Rule-compiler for formats** ("round robin, partners rotate, first to 11, win by 2") from Paper Games, to feed Khelo's tournament slice. A hypothesis that the same engine serves both.

## Hackathon fit: three caveats that matter
1. **Existing-code rule.** The participant guide, as recorded in project memory, says the demo may show only what was built during the hackathon, and that **startups** may build on existing code if they identify new work. Khelo existed before Oct 27, and Vibhor is in the **Indie** track. So building the agent inside the Khelo repo and demoing Khelo is likely a violation. I have not read the official rules (the page is login-walled). **Ask in Discord office hours (10 to 11 AM ET, weekdays) before deciding.** A safe shape is a new, separate repo for the agent, built from Oct 27, with Khelo shown only as a clearly disclosed integration target, and even that needs the organizers' confirmation.
2. **Time conflict.** Khelo's own plan still has staging setup (B7b) and the pilot launch (B8) pending. A hackathon week of agent work competes with finishing the pilot he actually wants to run.
3. **Rule risk.** Scheduling and score entry are not sports analysis, but anything that analyzes play, strokes or lines would hit the "sports analyzers" avoid-list.

## Rubric view of a "sports organizer agent" entry (my scores)
Impact 6 (organizer pain is real in his own account, but I have no sourced numbers), Meta tooling 7, Demo 7 (live round-robin with voice is watchable, but needs players on camera), Depth 7, weighted about 6.7. Same as the earlier court-director estimate. Assumption-based: Spark extraction accuracy on spoken scores in Hindi-English mixes, and live latency.

## Recommendation
Do not make Khelo the hackathon entry, because of the existing-code rule and the pilot time conflict. Keep it as the reason the **score-by-voice** and **format-compiler** ideas are worth having: if the household home brain or Paper Games wins the week, the same pieces (Voice Transcribe extraction, a checked rules spec) can flow into Khelo after Nov 4. If Vibhor wants an entry that feeds Khelo directly, ask the organizers first, and consider whether the Startup track would be allowed.
