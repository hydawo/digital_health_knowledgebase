# Clark et al. 2025 — Community-codesigned EMA of minority stress and suicidal ideation in SGM youth (MetricWire), N=50

## Quick Facts

| Field | Details |
|---|---|
| Citation | Clark K, Phillips K, Park E, Argiros A, Nikolaidis-Konstas A, Sexton J, Cyperski M, Kleiman E, Pachankis J. "Development, feasibility, and acceptability of a smartphone-based ecological momentary assessment of minority stress and suicidal ideation among sexual and gender minority youth." *PLOS ONE* 2025;20(8):e0330204. DOI [10.1371/journal.pone.0330204](https://doi.org/10.1371/journal.pone.0330204). PMID 40794631 / PMC12342249. |
| Study design | Two-part study. **Study 1**: protocol co-design through focus groups/interviews with **16 parents of SGMY, 16 SGMY, and 6 clinicians/researchers**. **Study 2**: prospective feasibility and acceptability evaluation of the resulting protocol, with weekly acceptability surveys and post-study exit interviews. |
| Sample size (enrolled / analyzed) | **50** in Study 2 — **19 adolescents (13–17) and 31 young adults (18–24)**. |
| Population | Sexual and gender minority youth (SGMY) aged 13–24 with **past-year suicidal ideation** (ASQ) and **current at-least-mild depression** (PHQ-9 ≥5), in the **US Southeast**. |
| Duration | **28 consecutive days**, **3 EMA surveys/day** (morning, afternoon, evening; max 84 per person), plus a weekly acceptability survey and an exit interview. |
| Devices/platforms used | **[MetricWire](../../module-02-digital-phenotyping/profiles/metricwire.md)** on participants' own iOS or Android phones. |
| Funding/COI | Academic (Vanderbilt, Rutgers, Yale and collaborators). **No platform relationship stated.** |
| Last verified | 2026-09-01 |

## Summary

The **highest EMA compliance of any mental-health cohort in this module — 80.21% (SD 16.92, Mdn 83.93, range 38.10–100.00%)** over 28 days of thrice-daily prompting in adolescents and young adults with past-year suicidal ideation and current depression. That is remarkable given that [Spangenberg et al.](metricwire-post-discharge-ema-reactivity.md) cite post-discharge suicidality-EMA compliance figures of 14–21%.

The paper's own explanation is its **Study 1**: the protocol was **co-designed with the population before deployment**, and the co-design changed concrete design parameters rather than just tone. Three specific examples are traceable from focus-group input to protocol feature:

- **Three surveys per day was chosen by the participants themselves**, explicitly reasoning about **school mobile-phone policies** ranging from full restriction to free periods.
- **The risk-escalation protocol was amended** so that emergency services are considered only in high-risk cases where the emergency contact is unresponsive — and instead of calling 911 or law enforcement, the team compiled **local mobile crisis services for each participant's area**. This is a direct response to SGMY concerns about police involvement.
- Protocol **language** was adjusted ("LGBTQ+" vs "queer").

The two additional operational findings worth carrying: **compliance declined every week** (87.24% → 82.00% → 77.33% → 74.29%), and **adolescents complied less than young adults (73.93% vs 84.06%, P=.03) — driven specifically by morning surveys.**

## Instrumentation and Deployment Model

**Pure BYOD.** Access to a personal smartphone running iOS or Android — "both of which are compatible with the EMA software (MetricWire)" — was an eligibility criterion. Unlike [SmartSense-D](aware-light-smartsense-d-youth-depression.md)'s Android-only gate, cross-platform support removed a whole class of exclusion.

**Safety and risk monitoring — the most fully specified protocol of its kind in this module.** It is triggered by a single EMA item ("Right now, what is your urge to kill yourself?", 0–10), banded into **None/Low (0–5), Moderate (6–8), High (9–10)**:

- All participants receive a standing crisis-resource message (Crisis Text Line, NowMattersNow, the 988 hotline, The Trevor Project) and a reminder to review the **Stanley-Brown Safety Plan** they completed at baseline.
- Higher bands trigger staff risk-assessment outreach. If a participant does not answer the risk-assessment call, they receive **voicemail and text messages with an explicit two-hour deadline**, after which the study team contacts their **emergency contact**.
- **Emergency services only if high risk *and* the emergency contact is unresponsive** — routed to **local mobile crisis services** rather than 911/law enforcement.
- Participants are briefed on the entire procedure in advance.

Anyone designing a remote study that collects active suicidal-ideation items should treat this as a template.

**Recruitment scope changed mid-study.** The residency criterion was initially **Tennessee only**, then **expanded after several months of slow recruitment of 13–17-year-olds** — a concrete, dated example of adolescent recruitment being the binding constraint in a high-risk-youth study.

**Incentives.** Study 1 focus-group participants received a **$40 gift card per session**. Study 2's incentive structure was itself shaped by focus-group input; the specific per-survey amounts are not extracted here.

## Recruitment and Retention

- **50 enrolled in Study 2** (19 adolescents, 31 young adults). No enrolment funnel, screening-failure count, or withdrawal count is reported in the extracted text — so **no retention rate can be quoted**, only compliance.
- Recruitment slowness in the 13–17 bracket forced a geographic expansion of eligibility. The authors present this as a practical lesson.

## Data Completeness and Technical Issues

**Overall compliance: M = 80.21%, SD = 16.92%, Mdn = 83.93%, range 38.10–100.00%.**

**Weekly decline** (one-way repeated-measures ANOVA, Huynh-Feldt corrected: F(2.69, 131.92) = 13.45, P<.001, ηp² = .22):

| Week | Mean | SD | Median |
|---|---|---|---|
| 1 | **87.24%** | 13.21 | 92.86% |
| 2 | 82.00% | 17.77 | 88.10% |
| 3 | 77.33% | 22.82 | 85.71% |
| 4 | **74.29%** | 22.15 | 76.19% |

Weeks 2, 3 and 4 each differed significantly from week 1. A multilevel model estimated a **−4.35 percentage-point decline per week** (95% CI −5.71 to −3.00, P<.001). **The SD roughly doubles from week 1 to week 3** — decay is concentrated in a subgroup, not spread evenly.

**Age-group difference** (Mann-Whitney U = 187.00, P=.03, z=−2.15, r=.30):

| Group | Median | Mean | SD |
|---|---|---|---|
| Adolescents (13–17, n=19) | 77.38% | **73.93%** | 17.75 |
| Young adults (18–24, n=31) | 90.48% | **84.06%** | 15.43 |

**The difference was significant only for morning surveys** (P=.002 after Bonferroni correction) — the same time-of-day pattern [Achterberg 2026](avicenna-adolescent-esm-school-phone-bans.md) attributes to sleep, and [Kivelä et al.](avicenna-ema-suicidal-ideation-iatrogenic.md) to chronotype and window length. Three independent studies in this module now find morning prompts to be the weakest slot.

**Neither baseline suicide-attempt history (P=.99) nor non-suicidal self-injury history (P=.42) predicted compliance** — extending the module's cross-cutting null on clinical severity as an attrition predictor to a second high-risk youth cohort.

No app crashes, sync failures or platform faults are reported.

## Feasibility Findings

**Authors' conclusion:** smartphone-based EMA is **feasible and acceptable** for studying real-time minority stress and suicidal-ideation intensity in high-risk SGMY, and **incorporating community-member feedback during study development helps ensure cultural responsiveness and enhance compliance.**

**Weekly acceptability surveys** reported the EMA as **easy to complete, private, understandable, minimally burdensome, and at least moderately engaging.** "Private" is a notable dimension in a population for whom device access may not be confidential from family.

**Exit-interview themes:** facilitators of high engagement, barriers to engagement, intervention implications, and suggested improvements.

## Relevance to Future Study Design

1. **Co-design the protocol parameters, not just the wording.** Survey frequency, risk-escalation routing, and language were all set by the population. 80% compliance in this cohort is the result being claimed for that process — plausibly, though not experimentally.
2. **Design the risk protocol around what the population fears.** Routing to local mobile crisis services rather than police, with an explicit two-hour window before contacting an emergency contact, is a concrete, reusable pattern.
3. **Expect −4.35 percentage points of compliance per week over a month**, with the variance concentrating in a subgroup. Four weeks is short; longer protocols should model the decay, as [Spangenberg et al.](metricwire-post-discharge-ema-reactivity.md) show at 26 weeks.
4. **Adolescents are not young adults.** A ten-point compliance gap, localised to morning surveys, is schedulable away.
5. **Move morning prompts later, or widen their window.** Three studies here converge on this.
6. **Adolescent recruitment will be the bottleneck.** This study had to expand its eligible geography to fill the 13–17 stratum.
7. **Report the enrolment funnel.** Its absence here means the strong compliance figure cannot be paired with a retention figure.

## Evidence Confidence

**Verified** — the two-study design and Study 1 sample composition, the N=50 / 19 / 31 split, the 28-day 3×/day protocol, the overall compliance figure with SD, median and range, all four weekly means with SDs and medians and the ANOVA and multilevel statistics, the age-group comparison with its test statistic, the morning-survey-specific difference, both null clinical-history predictors, the full risk-monitoring protocol, the $40 focus-group incentive, and the Tennessee-to-wider-Southeast eligibility change. Read from the full text (Europe PMC PMC12342249), 2026-09-01.

**Reported** — the causal claim that community co-design *produced* the high compliance. Study 1 demonstrably shaped the protocol, and the compliance is demonstrably high, but no comparison arm or non-co-designed control exists. Treat as a plausible mechanism, not a demonstrated effect.

**Unclear / not reported** — enrolment funnel, withdrawals, retention rate; the Study 2 per-survey incentive amounts; whether the compliance denominator counts partially-completed surveys.

**Small-sample caution the authors state themselves:** "it is imperative to consider the small sample size at the highest level of analysis due to the presence of only 19 adolescents and 31 young adults." Age-group inferences rest on 19 people.

**COI:** none identified relating to MetricWire.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.1371/journal.pone.0330204
- Europe PMC: https://europepmc.org/article/PMC/PMC12342249
- Platform: https://metricwire.com/
- Local PDF: `../literature/2025-clark-plosone-ema-minority-stress-sgm-youth-feasibility.pdf`

## Related profiles

- Platform: [MetricWire](../../module-02-digital-phenotyping/profiles/metricwire.md)
- Long-term compliance decay in a suicidality cohort: [`metricwire-post-discharge-ema-reactivity.md`](metricwire-post-discharge-ema-reactivity.md)
- Adolescent ESM and school phone access: [`avicenna-adolescent-esm-school-phone-bans.md`](avicenna-adolescent-esm-school-phone-bans.md)
- Morning-prompt weakness and compliance predictors: [`avicenna-ema-suicidal-ideation-iatrogenic.md`](avicenna-ema-suicidal-ideation-iatrogenic.md)
- Long-term adolescent digital phenotyping: [`beiwe-adolescent-feasibility.md`](beiwe-adolescent-feasibility.md)

## Sources

1. Clark K, et al. *PLOS ONE* 2025;20(8):e0330204. DOI 10.1371/journal.pone.0330204. Full text read from Europe PMC (PMC12342249), 2026-09-01. Establishes every figure in this profile.
