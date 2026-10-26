# Hackathon idea landscape research

> Note: this is the early prior-art study for the energy retrofit, repair agent and robot planner ideas. The chosen idea is now the live expert guide; see `build-plan.md`. The energy retrofit agent is the fallback.

Oct 26, 2026 · @Vibhor Tayal

## Verdict

Build the energy retrofit agent. It has commercial neighbours but no open-weights, local, verifiable version that I could find, and that gap is the story for both the Impact score and the open-weights bonus. Findings come from web searches; most pages were read as search summaries, not opened in full, so vendor claims are unverified.

## Energy retrofit: prior art

No project I found goes from a homeowner's phone video to a costed, verifiable retrofit plan using open weights.

| Project | Type | What it does | Gap vs. our idea |
| --- | --- | --- | --- |
| [Kelvin](https://techcrunch.com/2024/06/10/kelvin-wants-to-help-save-the-planet-by-applying-ai-to-home-energy-audits) | Startup (France) | Computer vision on photos and video to speed up audits | Closed, aimed at auditors, not Meta models |
| [Praxis Plus app](https://wearebrain.com/work/sustainability-check-praxis-plus-app/) | Retailer app | One room photo gives tips and a shopping list | Shallow, no costed plan |
| [Snugg Pro iAudit](https://snuggpro.com/blog/item/iaudit-pro) | Pro software | Savings-to-investment ratio, costs, rebates per recommendation | For auditors, manual data entry |
| [NEEP Remotely pilot](https://neep.org/sites/default/files/media-files/remotely_one_pager.pdf) | Utility pilot | App walkthrough feeds an auto-generated energy model | Pilot, tied to utility programs |
| [HeatPump MCP server](https://llmbase.ai/de/mcp-servers/heat-pump/) | Open source | Heat pump sizing, cost and cold-climate checks as agent tools; 81 models, TMY3 weather | Tools only, no perception or full audit |
| [Code for Boston heat-load tool](https://ost.ecosyste.ms/api/v1/projects/45458) | Open source (MIT) | Heat load and heat pump capacity check | Calculator, no AI |
| [Residential retrofit LLM paper](https://arxiv.org/abs/2602.20181) | Research | LLM fine-tuned with LoRA on 536,416 simulated U.S. homes | Code not confirmed public |
| [Korean window study](https://doaj.org/article/11a0e605801547df97dccfc3b06e41bc) | Research | Window insulation estimated from photos, about 80% accuracy | Windows only |

The open gap: a free agent that sees the house, calls verified sizing and cost tools, and shows its math. The sizing MCP server and EnergyPlus-style tools could be reused if licenses allow, credited openly as pre-existing work.

## Alternatives: repair agent and robot planner

Both alternatives have stronger direct competitors than the energy idea.

| Idea | Closest prior art | Read |
| --- | --- | --- |
| Verifiable repair agent | [ResolveGrid](https://www.businesswire.com/news/home/20260514354794/en/) (agentic AI, computer vision and remote experts for technicians, May 2026); [Dedicatted](https://aws.amazon.com/marketplace/pp/prodview-o2ytujvtdscbg) on AWS; [AWS automotive technician guidance](https://docs.aws.amazon.com/solutions/building-an-automotive-technician-with-multimodal-agentic-ai-on-aws/) | Crowded with funded vendors. Risk of looking like basic RAG over manuals. |
| Sim-to-robot task planner | [SeeDo](https://www.github.com/ai4ce/SeeDo) (NYU, IROS 2025): human demo video to robot plan using SAM, SAM2, GroundingDINO and a VLM; PyBullet, not MuJoCo | Published, open source and close to the idea. Ours would need a clear new angle, such as Meta models plus MuJoCo. Heaviest solo build. |

Neither has a natural reason to run on local open weights, so the open-weights bonus is harder to argue for them. That is my judgement, not a finding.

## Repair agent: deeper look

The repair space is busy with commercial products, but I found no open-source project combining equipment manuals, citation-checked answers and multimodal input.

| Project | Segment | What it does |
| --- | --- | --- |
| [ResolveGrid](https://www.businesswire.com/news/home/20260514354794/en/) | Enterprise field service | Agentic AI, computer vision and remote experts guide technicians; May 2026 launch (press release page returned 403, so details are from the search summary) |
| [ChargePoint AI tool](https://autotechinsight.spglobal.com/news/5277800/chargepoint-launches-ai-powered-tool-to-diagnose-and-repair-ev-charging-stations) | EV chargers | Photos of a faulty station are analyzed to flag faults; 2024 |
| [FixMynd](https://appgoblin.info/apps/6766394491) | Consumer iOS app | Photo gives a diagnosis, tool list and cost estimate; May 2026 |
| [ACLogics](https://hunted.space/product/aclogics) | Pro HVAC | Error-code matching, fix plans, nameplate photo scan; little traction |
| [Copeland Mobile Scout AI](https://www.achrnews.com/articles/164015-new-copeland-mobile-ai-feature-enhances-troubleshooting-education-and-productivity) | HVAC incumbent | AI chatbot in a contractor app |
| [Dedicatted](https://aws.amazon.com/marketplace/pp/prodview-o2ytujvtdscbg) | Enterprise (AWS) | Voice, image and text guidance, predictive troubleshooting |
| [Grounded Support Agent](https://github.com/Jasveersinghok/grounded_support_agent) | Open source | Verify-or-abstain: no answer ships unless grounded in a source; text support, not repair |

**Fit with the rubric**

- **Impact:** real, but it targets a market where funded vendors already ship, so the story must be a clear underserved user, such as independent technicians.
- **Meta tooling:** strong use of Spark (reasoning and tool use), Voice Transcribe and SAM 3.1; less natural for on-device open weights.
- **Risks:** it can read as basic RAG over manuals, which the rules discourage. A visible verification loop and honest abstaining are what would separate it.
- **Demo:** good if you have a real faulty device on camera, which adds a hardware dependency to the build.

**Bottom line:** feasible and demo-friendly, with more direct competition than the energy idea and a weaker open-weights case. The energy retrofit agent stays my pick; the repair agent is the best backup.

## Open-source angle for the bonus

The bonus text I have says only "Best Build on Open Weights (Glimmer/Spark Open)"; the public event page does not describe it, so the judging criteria are unknown.

- **Muse Spark Open** (Oct 15): 816B parameters, 42B active, 1M context, agentic and multimodal. Too large to run locally, so use a hosted endpoint. Day-zero support in SGLang, vLLM, llama.cpp, MLX and Unsloth. ([PyTorch](https://pytorch.org/blog/muse-spark-open/), [Meta dev blog](https://dev.meta.ai/resources/blog/build-with-muse-spark-open))
- **Muse Glimmer** (Aug 10): about 30B, Apache 2.0, built for a laptop or single consumer GPU, with an ExecuTorch on-device path. Sources disagree on whether it is multimodal; check the model card. ([CNBC](https://www.cnbc.com/2026/08/10/meta-muse-glimmer-open-weight-ai.html))
- **PyTorch stack Meta promotes:** TorchTitan for SFT, LoRA and RL on Spark Open; Helion kernels; ExecuTorch.

**Plan:** run the privacy-sensitive perception and reasoning on Glimmer locally, use Spark Open hosted for heavy reasoning, and as a stretch, LoRA-tune Glimmer with TorchTitan on energy-audit tool-calling traces and release adapter, dataset and recipe. Skip kernel and inference-engine work; it sits outside the theme.

## Risks and mitigations

| Risk | Mitigation |
| --- | --- |
| Judges see it as a known idea (Kelvin and others) | Lead the demo with the open, local, verifiable-math angle, not novelty of audits |
| Looks like a simple image analyzer, which the rules discourage | Make the tool-calling agent loop and shown calculations the centerpiece |
| Pre-existing sizing tools count as outside work | Reuse only with a compatible license, credit them in the repo and video, build the integration during the hackathon |
| Glimmer may not handle images | Check the model card first; fall back to SAM 3.1 plus Spark via the API for vision |
| Fine-tuning stretch eats time | Tier 2 only, after a submitted Tier 0 |
| Savings numbers wrong | Use published cost and weather data, show inputs and ranges, label estimates |

## Sources

As of 2026-10-26. Mostly web-search summaries; vendor and performance claims are unverified.

- [Muse Spark Open, PyTorch blog](https://pytorch.org/blog/muse-spark-open/) and [Build with Muse Spark Open](https://dev.meta.ai/resources/blog/build-with-muse-spark-open) (opened)
- [Event page](https://cerebralvalley.ai/e/meta-ai-developer-hackathon) (opened; no bonus-prize detail)
- [CNBC on Muse Glimmer](https://www.cnbc.com/2026/08/10/meta-muse-glimmer-open-weight-ai.html), [TechCrunch on Spark Open](https://techcrunch.com/2026/10/15/meta-launches-an-open-weight-model-that-runs-on-macs/)
- Retrofit prior art and repair and robot alternatives: the links in the tables above
