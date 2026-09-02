# Achterberg 2026 — Adolescent ESM under a national school smartphone ban (Avicenna), N=195

## Quick Facts

| Field | Details |
|---|---|
| Citation | Achterberg M. "In the moment, out of reach? Experience sampling with adolescents in the context of school smartphone bans and shifting societal norms." *Journal of Research on Adolescence* 2026;36(1):e70118. DOI [10.1111/jora.70118](https://doi.org/10.1111/jora.70118). PMID 41508716 / PMC12783947. **Sole-authored.** |
| Study design | Feasibility/methods evaluation embedded in an ESM study: compliance, prompt-level nonresponse analysis, careless-responding checks, and post-study participant evaluation. |
| Sample size (enrolled / analyzed) | **211 signed up (70% of those approached) → 195 completed the full ESM protocol** after attrition. |
| Population | Dutch adolescents aged **14–17** (mean 16.12, SD 0.79; 52% female), from schools across the Netherlands; **85% in the West (South/North Holland, Utrecht); 99% identified as ethnically Dutch**. Spanning prevocational (VMBO/MAVO), general secondary (HAVO) and pre-university (VWO) tracks. |
| Duration | **17 days**, deliberately spanning **11 school days and 6 weekend days**; **6 prompts/day**, max 102 observations per person. |
| Devices/platforms used | **[Avicenna Research](../../module-02-digital-phenotyping/profiles/avicenna-research-ethica.md)** app on participants' own phones, paired with **WhatsApp** for engagement. |
| Funding/COI | Academic — Erasmus University Rotterdam. **No platform-developer relationship**; the platform is described as chosen for robustness and prior successful use. |
| Last verified | 2026-09-01 |

## Summary

The only study in this module where the binding operational constraint is **a law**. The Netherlands introduced a nationwide school smartphone ban during this study's setup phase, and the paper is essentially a test of whether experience sampling with adolescents survives it.

It does. **Compliance was 78% (95% CI 74.7–80.6, SD 0.19, range 18–100%)** despite **88% of participants reporting school-based restrictions and 56% reporting parental restrictions** — comparable to the general ESM benchmark (79%) and slightly above the adolescent-specific benchmark (74%). Compliance was even **higher on weekdays (80%) than weekends (75%)**.

But the honest reading is that the compliance number was *bought*, not observed. The protocol was redesigned around the ban — 17 days to guarantee enough non-school observations, prompts scheduled to avoid class time — and layered with an engagement stack (a WhatsApp community, gamified group feedback, €2.50/day plus an Apple Watch lottery for the 50 most compliant). This is what it costs to keep adolescent ESM viable under current norms, and the paper is valuable precisely because it itemises that cost.

## Instrumentation and Deployment Model

**Pure BYOD**, on adolescents' own phones, under third-party restrictions the researcher does not control.

**Protocol design as a response to the constraint.** The 17-day window was chosen deliberately: **11 school days + 6 weekend days**, so that "even if school-time prompts were consistently missed, participants could still provide up to 80 observations — sufficient for within-person analyses." That is an explicit design margin built for anticipated institutional data loss, and it is transferable to any setting with enforced device-free periods (workplaces, wards, custodial settings, schools).

**Platform choice, and why.** Avicenna was selected for **customisable scheduling, offline functionality, and GDPR-compliant data storage** — offline capture being directly relevant when phones are locked away during the day. The app's **real-time progress tracker** was used operationally to send personalised compliance feedback on days 4, 8, 11 and 15.

**The engagement stack (all four components matter):**

1. **A WhatsApp Community** — one-way broadcast preserving participant privacy, used for reminders and low-threshold contact, chosen because it was already embedded in adolescents' routines and the Avicenna prompt was competing against an estimated ~237 daily notifications.
2. **Financial incentive** — €7.50 for the start questionnaire, **€2.50 per day** completed, up to **€50** total.
3. **A prize lottery** — an Apple Watch, drawn among the **top 50 most compliant** participants.
4. **Gamification** — group-level results shared back through the WhatsApp community.

Institutional letters were also provided to schools.

## Recruitment and Retention

- **211 signed up (70%)**; **195 completed the full protocol**. The paper reports the 211→195 shrinkage as "attrition" without breaking down reasons.
- Recruitment used QR codes and let adolescents pick their preferred communication channel — the author notes that email-based approaches are easily overlooked by this group.
- **Representativeness is the weak point:** 99% ethnically Dutch, 85% from the west of the country. This is a geographically and ethnically narrow sample, and the paper is transparent about it.

## Data Completeness and Technical Issues

**Compliance: M = 78% (95% CI 74.7–80.6%), SD 0.19, range 18–100%.**

Benchmarks the author cites: general ESM samples **M = 79%** (Wrzus & Neubauer 2023); adolescent samples specifically **M = 74%** (van Roekel et al. 2019).

**Weekday 80% vs weekend 75%** — the reverse of the direction one would predict from a school ban, and the reverse of the weekend effect [McClaine et al.](aware-chemotherapy-engagement.md) found in adults with cancer (OR 0.90 for weekends). Structured days appear to help adolescent compliance more than free access to a phone does.

**Prompt-level nonresponse attribution — the most transferable table in the paper.** Missed prompts cluster by time of day, with distinct causes:

| Time of day | Dominant reason for nonresponse |
|---|---|
| Early morning | **Sleep** |
| Late morning | **School** |
| Evening | **Work** |

The author's framing: adolescents' unavailability "is shaped not only by school or parental policies, but also by internal rhythms, shifting priorities, and momentary disengagement." Institutional restriction is one cause among several, and not the largest.

**Data quality checks:**

| Check | Result |
|---|---|
| Careless responding (<3 s on three emotion items) | flagged in **14.3% of participants** — in line with prior work; treated as non-systematic |
| "Long string" responses (identical answers to all four items) | **0.08% of all entries** |
| Self-rated own honesty (0–100) | **91** |
| Estimated others' honesty | **80** |

**Careless and long-string responses were deliberately not excluded**, to avoid sampling bias — the reasoning being that adolescents experiencing greater burden are likelier to produce them, so removing them removes the burdened. This is a defensible and unusual analytic choice worth flagging to anyone writing a cleaning protocol.

**No app crashes, sync failures, or platform technical problems are reported.** Given the paper's methodological focus, this silence is more likely to mean "none noteworthy" than "not examined", but it is not stated either way.

## Feasibility Findings

**Author's conclusion:** adolescent ESM "remains feasible and ecologically valid when protocols are flexibly aligned with real-world constraints," and aligning design with adolescents' everyday realities becomes *more* essential as restrictions intensify.

Participant evaluation:

| Measure | Result |
|---|---|
| Would participate again in a similar study | **99%** |
| Overall experience (0–100) | **69.43** |
| Grade given to the study (0–10) | **7.5** |
| Reported motivators | financial incentives, scientific contribution, social connection |

Burden was described as "sometimes demanding" but "manageable" — six prompts plus a daily diary questionnaire.

The author also notes higher compliance among girls than boys, consistent with prior adolescent ESM work, though the study was not designed to examine this.

## Relevance to Future Study Design

1. **Design the observation window around the periods you will lose.** 17 days for a protocol that only needs ~80 usable observations, sized so that total school-time loss is survivable, is a directly reusable pattern.
2. **Institutional device restrictions are now a first-class design parameter for adolescent research**, and they are spreading. A study designed before 2024 assumptions may not replicate.
3. **The ESM prompt is competing with ~237 daily notifications.** Pairing the research app with a channel adolescents already attend to (here WhatsApp) is the mechanism the author credits most.
4. **A tiered incentive structure worked**: per-day payment for baseline effort, a compliance-ranked lottery for the tail. Note this makes the 78% figure conditional on a fairly generous incentive package — up to €50 plus a lottery — and it should not be transferred to unfunded designs.
5. **Attribute nonresponse by prompt, not by person.** Knowing that early-morning misses are sleep and late-morning misses are school tells you to move the prompts; knowing only that compliance was 78% does not.
6. **Consider *not* excluding careless responses.** Exclusion may systematically remove the most burdened participants.

## Evidence Confidence

**Verified** — the 211/195 flow and 70% sign-up rate, the demographic composition, the 17-day/6-prompt structure and 102-observation maximum, the 78% compliance figure with CI, SD and range, the weekday/weekend split, the 88%/56% restriction prevalence, the careless-responding and long-string rates, the honesty ratings, the incentive structure, and the 99%/69.43/7.5 evaluation figures. Read from the full text (Europe PMC PMC12783947), 2026-09-01.

**Reported** — the attribution of nonresponse to sleep, school and work. These come from the study's own nonresponse items, i.e. participant self-report, not from objective context data.

**Unclear** — how much of the 78% is attributable to which engagement component. Four engagement mechanisms plus a redesigned schedule were deployed simultaneously with no arms varying them; the compliance figure cannot be decomposed. Also unclear: the reasons for the 211→195 attrition.

**Generalisability caution the author states:** 99% ethnically Dutch, 85% from one region, self-selected via school-based recruitment, in a country with a *national* school ban. Findings about compliance under restriction may not transfer to settings with patchier or differently-enforced rules.

**COI:** none identified. Sole-authored by an academic developmental psychologist with no stated relationship to Avicenna Research. The paper evaluates a method under a policy constraint, not a product.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.1111/jora.70118
- Europe PMC: https://europepmc.org/article/PMC/PMC12783947
- Platform: https://avicennaresearch.com/
- Local PDF: `../literature/2026-achterberg-jresadolesc-esm-adolescents-school-smartphone-bans.pdf`

## Related profiles

- Platform: [Avicenna Research (Ethica)](../../module-02-digital-phenotyping/profiles/avicenna-research-ethica.md)
- Adolescent long-term digital phenotyping compliance: [`beiwe-adolescent-feasibility.md`](beiwe-adolescent-feasibility.md)
- Weekend/weekday compliance effect in the opposite direction: [`aware-chemotherapy-engagement.md`](aware-chemotherapy-engagement.md)
- Age as a compliance predictor in an adolescent/young-adult EMA sample: [`metricwire-sgm-youth-ema-feasibility.md`](metricwire-sgm-youth-ema-feasibility.md)

## Sources

1. Achterberg M. *J Res Adolesc* 2026;36(1):e70118. DOI 10.1111/jora.70118. Full text read from Europe PMC (PMC12783947), 2026-09-01. Establishes every figure in this profile. Sole authorship confirmed from the article XML author list, not from search metadata.
