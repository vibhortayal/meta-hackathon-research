# Candidate: US visa and immigration helper

2026-10-26. Evaluated against the same rubric and rules as the other ideas. Scores are my judgement, not data. Web findings come mostly from search summaries and vendor or law-firm pages, so treat figures as indicative. Nothing here is legal advice.

## Verdict

Real pain, and technically the safest of the three to build by Oct 31, but the demo is less vivid, the field is crowded, and it carries more rule risk than the others (legal advice limits, "anything political" on the avoid list, sensitive personal data). It is a strong candidate if Vibhor knows the problem firsthand. It is a close call against the live guide, not a clear win either way.

## The pain points (what is actually unsolved)

- **Evidence and consistency errors drive delays.** About 19.7% of O-1 adjudications in FY2025 got a Request for Evidence ([Manifest Law summary of USCIS data](https://manifestlaw.com/blog/o1-visa-statistics-applicants-should-know)). Practitioner reports put EB-1A RFE rates near 50% by early 2025 ([Raju Law](https://rajulaw.com/increased-rfe-rates)). Processing times for some categories reportedly rose to about 12 months by May 2026 (unverified). A law-firm blog reports a USCIS policy from Aug 5, 2026 allowing denial without an RFE when evidence is missing at filing; I did not find the primary USCIS announcement, so check uscis.gov before relying on it.
- **Cost and language.** Attorney help is expensive and many applicants need guidance in their own language. JustiGuide's founder cites complexity, cost and native-language help as the core problems ([TechCrunch](https://techcrunch.com/2025/11/26/justiguide-wants-to-use-ai-to-help-people-navigate-the-u-s-immigration-system)).
- **Fraud.** Notario fraud (non-lawyers filling forms for pay) is a documented harm, which is why advice rules are strict ([CLINIC](https://www.cliniclegal.org/sites/default/files/2019-11/Stopping-Immigration-Services-Scams-A-Tool-for-Advocates-and-Lawmakers.pdf)).
- I found no reliable data on form-level rejection rates or applicant confusion.

## What already exists (crowded)

| Product | Audience | What it does |
| --- | --- | --- |
| [JustiGuide](https://techcrunch.com/2025/11/26/justiguide-wants-to-use-ai-to-help-people-navigate-the-u-s-immigration-system) | Individuals, founders, lawyers | AI portal in 12 languages, form help, lawyer matching; 47,000 users per the founder |
| [Imagility](https://imagility.co/) | Attorneys and petitioners | Form auto-fill and error checks before filing |
| [VisaCompanion AI](https://visacompanion.ai/) | Applicants | Eligibility analysis, petition drafts, RFE risk prediction (self-reported) |
| [Docketwise AI](https://www.docketwise.com/blog/ai-for-immigration-lawyers/) | Immigration lawyers | Extracts data from documents and maps it into USCIS forms |
| [Citizenshipworks](https://palegalaid.net/node/24510) | Free, naturalization | Eligibility interview, red flags, English, Spanish and Chinese |
| Hackathon-style entries (VisaAI on [Devpost](https://devpost.com/software/visaai), a German visa assistant that placed first at an AI Tinkerers event) | Applicants | Checklists and multilingual Q&A, some with simulated extraction |

A plain "visa chatbot" would be basic RAG and look like a dozen others. Differentiation has to come from the agent doing real work on documents.

## Rule and risk check

| Risk | Detail | Handling |
| --- | --- | --- |
| Unauthorized practice of law | In immigration cases only attorneys and DOJ-accredited representatives may give legal advice ([USCIS scam guidance, via Reyes Blum](https://reyesblum.com/fake-immigration-lawyer-ai-video-check/)). I found no rule specifically on consumer AI tools. | Information and organization only: no eligibility verdicts, no strategy, no "you should file X". Frame it as case-file preparation for self-filers, clinics and attorneys. Get a real lawyer's view before any real-world launch. |
| "Anything political" is on the avoid list | Immigration is politically charged, though helping with paperwork takes no side. | Neutral, administrative framing. Avoid policy commentary entirely. Ask Meta in office hours. |
| Sensitive personal data | Passports, A-numbers, addresses. | Synthetic documents only in repo and demo. Privacy story: run extraction locally on Glimmer so real documents never leave the device. |
| Out-of-date rules | USCIS policy changes quickly. | Cite form-instruction versions with dates; show "verify on uscis.gov" in the output. |
| "Basic RAG" and "AI-for-education chatbot" | Q&A over instructions would fit both. | Build an agent that extracts, cross-checks and asks questions, not a Q&A bot. |

## Scoped version that fits the rules: case-file copilot

A voice-first helper that turns a messy pile of documents into an organized, consistent case file.

1. **Intake by voice** in Hindi, English or Spanish (Voice Transcribe, Spark, Glimmer for 100+ languages).
2. **Document extraction** from photos and PDFs of synthetic passports, approval notices and pay stubs into structured data (Spark vision and PDF input, structured output).
3. **Cross-checks with tools:** name spelled differently across documents, passport expiring before the requested stay, gaps in address or travel history, date arithmetic for time windows. Computed, not guessed, with the source document shown for each flag.
4. **Asks the user** when documents conflict, and records the answer.
5. **Output:** a checklist built from the public form instructions, an organized evidence packet, and a plain-language summary in the user's language, with a "show this to an accredited representative or attorney" note.

Meta models: Spark (documents, reasoning, tools), Voice Transcribe, Glimmer (local privacy, multilingual, open-weights bonus). SAM 3.1 and Muse Image are not natural fits.

## Rubric comparison (my judgement)

| Idea | Impact 30% | Meta tooling 25% | Demo 25% | Depth 20% | Weighted | Chance it works by Oct 31 | Rule risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Live expert guide (cooking) | 7 | 9 | 8 | 7 | 7.8 | about 60%, untested | coach, nutrition-adjacent |
| Immigration case-file copilot | 8.5 | 7 | 6.5 | 7 | 7.3 | about 90% | legal advice, political, personal data |
| Energy retrofit agent | 8 | 7 | 6 | 7 | 7.1 | about 80% | low |

The probabilities are guesses. Expected scores come out close (guide about 7.4, copilot about 7.2 once the guide's failure case falls back to a weaker idea), so this is a risk-profile choice, not a clear winner.

## Recommendation

1. Keep the live guide as the lead only if the day-1 test passes and the office-hours answer on the coach and analyzer risk is acceptable.
2. Make the immigration case-file copilot the fallback instead of the energy retrofit agent. It beats energy on impact, multilingual fit and the local-privacy open-weights story, and extraction is more reliable than live video.
3. If Vibhor knows this problem firsthand and wants to lead with it, that is a defensible choice, because the theme asks for "a problem you know firsthand". In that case, reorder: copilot first, guide second.

## Questions for Vibhor

- Do you know this problem firsthand (your own or someone close to you)? That is the strongest reason to lead with it.
- Which audience: individual self-filers, community clinics, or attorneys?
- Which languages besides Hindi and English?
