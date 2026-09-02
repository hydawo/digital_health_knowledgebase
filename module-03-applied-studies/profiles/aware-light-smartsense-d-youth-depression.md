# Camargo et al. 2025 — SmartSense-D: AWARE-Light + actigraphy in young people with MDD, N=40

## Quick Facts

| Field | Details |
|---|---|
| Citation | Camargo A, Tagliaferri SD, D'Alfonso S, Zhang T, Munoz Z, Davies P, Alvarez-Jimenez M, **van Berkel N**, **Kostakos V**, Schmaal L. "SmartSense-D: A safety, feasibility, and acceptability pilot study of digital phenotyping in young people with major depressive disorder." *Digital Health* 2025;11:20552076251330509. DOI [10.1177/20552076251330509](https://doi.org/10.1177/20552076251330509). PMID 40297349 / PMC12034961. |
| Study design | Pilot longitudinal cohort with **safety, feasibility and acceptability as pre-registered primary outcomes against explicit numeric criteria**; secondary exploratory linear mixed models. STROBE-reported. |
| Sample size (enrolled / analyzed) | **48 consented → 40 (83%) completed the full protocol.** Of the 8 who did not, **7 withdrew because of technical issues with the AWARE-Light app** and 1 for personal reasons. |
| Population | Young people aged **16–25** with DSM-5/MINI-confirmed major depressive disorder, recruited from **four headspace youth mental health clinics, Melbourne, Australia**. Baseline QIDS-16 mean **15.65** (moderate-to-severe). 47.5% unemployed; 45% living with both parents. |
| Duration | **8 weeks** (56 days) of passive sensing and actigraphy; EMA required for ≥6 of those weeks, with optional break weeks. |
| Devices/platforms used | **[AWARE-Light](../../module-02-digital-phenotyping/profiles/aware-framework.md)** (Android-only build of the AWARE framework) for both EMA and passive sensing, plus an unnamed **wrist-worn actigraphy device**. |
| Funding/COI | Academic — University of Melbourne / Orygen / headspace. **Two AWARE-Light co-developers (van Berkel, Kostakos) are co-authors** and the paper evaluates their tool. |
| Last verified | 2026-09-01 |

## Summary

The most direct evidence in this module that **an app-compatibility problem can be a study's dominant failure mode** — larger than participant burden, larger than clinical severity, larger than anything about the population.

Two numbers carry the profile. **Fourteen of 48 participants (29%) hit compatibility problems between AWARE-Light and their specific Android handset model** and had to be issued a loan phone (from personal spare devices or the study team) to take part at all. And **7 of the 8 participants who did not complete withdrew specifically because of technical issues with the app** — technical failure accounted for 87.5% of all attrition.

Both facts sit alongside a genuinely reassuring acceptability result (83.1% agreed the app was usable and comfortable; 79.8% comfortable with passive sensing; **no adverse events** in a moderate-to-severely depressed adolescent and young-adult sample) and a pattern of **wildly uneven completeness across passive streams within one app on one platform**: location and unlock duration ~79% of days, communication metadata **38.4%**.

## Instrumentation and Deployment Model

**BYOD with a hard platform gate, retrofitted to partial provisioning.** Owning and regularly using an **Android** smartphone was an inclusion criterion, "as the used application only collects data from Android devices." iOS owners were excluded outright — the same design constraint that, in [RADAR-MDD](radar-mdd-recruitment-retention.md), accounted for 11% of withdrawals, and here reduces the eligible pool before recruitment even starts.

That gate did not go far enough: **14/48 participants had model-specific incompatibilities with AWARE-Light on their own Android device**, and were moved onto loan handsets sourced ad hoc.

**Active stream:** AWARE-Light delivered EMA **twice daily (midday and 8pm)**. The morning survey had 12 items (affect, sleep quality, substance use, significant events); the evening survey repeated those minus sleep and added eight (perceived stress, anxiety, worry, rumination, loneliness, social interaction, most positive and most negative event pleasantness). Items were drawn from PSQI, DASS, PSWQ, RRS and the UCLA Loneliness Scale. **Participants could opt to take a break from EMA during week 4 and/or week 8**; six did.

**Passive streams (AWARE-Light):** location (GPS + surrounding networks, **sampled every 180 s** — latitude, longitude, speed, altitude, accuracy, feeding location entropy, transitions and variance), communication metadata, screen unlock duration, social media use, and inter-key delay.

**Wearable:** a wrist-worn actigraphy device. **The specific make and model is not named in the full text** — do not cite this study as evidence about any named actigraph.

## Recruitment and Retention

- **48 consented; 40 (83%) completed the full protocol**, exceeding the pre-registered feasibility criterion.
- **Attrition cause is unusually clean: 7/8 technical (AWARE-Light), 1/8 personal.**
- 25% were aged 16–18, 42% 19–22, 32% 23–25. Gender identity was diverse (55% female, 25% male, 10% gender queer, 10% transgender) against 70% female sex assigned at birth.

## Data Completeness and Technical Issues

The study set three numeric feasibility criteria in advance and **met one, missed one, and partially met one** — a level of pre-specification rare in this module.

| Criterion | Threshold | Result |
|---|---|---|
| 1. Full protocol completion | not stated numerically in text; met | **83% (40/48)** — met |
| 2. EMA completion | ≥80% of participants completing ≥65% of surveys in first 3 weeks | **72% (26/36)** — **missed**. Over the ≥6-week period, **61% (22/36)** |
| 3. Missing days of actigraphy / passive sensing | valid = >39 of 56 days (70%) | actigraphy **56% (20/38)**; passive sensing **81% (22/27)** of the technically-clean subset |

**Actigraphy.** 38/40 (95%) provided any actigraphy data — **one watch was defective and another failed to store data**. Only 20/38 (56%) reached the 70%-of-days threshold. Causes named: non-compliance with wearing, and **limited availability of wristband devices causing staggered start and end dates** — a logistics constraint, not a participant one.

**Passive sensing — and an important denominator.** Passive analysis was restricted to **27 of 38 participants "who did not encounter significant technical difficulties."** Within that already-filtered subset:

| Stream | Mean days with data (of 56) | % of period | Participants ≥39 days |
|---|---|---|---|
| Max unlock duration | 43.4 (SD 11.9) | **79.0%** | 19/27 (70.4%) |
| Location | 43.1 (SD 11.9) | **78.4%** | 19/27 (70.4%) |
| Social media use | 34.8 (SD 12.8) | **63.3%** | 10/27 (37.0%) |
| Inter-key delay | 32.8 (SD 12.4) | **59.6%** | 7/27 (25.9%) |
| Communication | 21.1 (SD 17.2) | **38.4%** | 7/27 (25.9%) |
| EMA (for comparison) | 35.9 | **65.3%** | — |

**The spread inside one app on one OS is the finding.** A two-fold difference between location (78.4%) and communication metadata (38.4%) means "passive smartphone sensing worked" is not a statement a study can make at the app level — it must be made per stream. Communication metadata is also the stream most exposed to Android permission tightening, and its SD (17.2 days on a mean of 21.1) indicates the failure was near-total for some participants rather than uniformly partial.

Note also that **passive completeness here (38–79%) is not higher than active completeness (65.3%) across the board** — location and unlock beat EMA, three streams did not. This is a partial counterexample to the module's "passive outlasts active" pattern, and it arises because the pattern is really about *which* passive stream.

## Feasibility Findings

**Safety:** no adverse events reported. In a cohort with moderate-to-severe MDD including 16-year-olds, this matters, and joins [Kivelä et al.](avicenna-ema-suicidal-ideation-iatrogenic.md) and [Spangenberg et al.](metricwire-post-discharge-ema-reactivity.md) as evidence that intensive self-monitoring in high-risk mental-health populations does not produce measurable harm at the group level.

**Acceptability:** 83.1% agreed with usability/comfort items (39.5% strongly agree, 32.3% agree, 11.3% slightly agree); **61.1% disagreed with having privacy concerns**; 83.3% disagreed that the app made them upset; **79.8% comfortable with passive sensing specifically**.

**Authors' conclusion:** the combined active + passive protocol was "safe, and acceptable among young people with MDD." The feasibility verdict is more qualified than the abstract's framing suggests — criterion 2 was missed, and criterion 3 was met only for a technically-clean subset.

## Relevance to Future Study Design

1. **Pilot the app against a device-model list, not against the OS.** "Android-only" was not a sufficient technical specification: 29% of consented participants still could not run the app on their own handset. A pre-enrolment handset compatibility check would have caught this — and would function like the **one-week trial period** [Cohen et al.](mindlamp-relapse-3site.md) used, but earlier and cheaper.
2. **Hold loan phones in reserve, and budget them.** This study improvised, sourcing spares from participants' own drawers. Note the counter-evidence: [Zhang et al.](radar-mdd-longterm-engagement.md) found that *provisioning* a phone was associated with **worse** long-term retention (HR≈1.66). Loaners solve enrolment and may cost engagement.
3. **Report passive completeness per stream.** A single app-level figure would have hidden a 2× spread.
4. **Actigraphy device inventory is a data-quality variable.** Insufficient wristbands caused staggered monitoring windows, which is a design defect that shows up in the data as missingness.
5. **Attribute attrition causes.** Because this study did, we know its dropout was almost entirely technical — and therefore fixable — rather than a burden problem inherent to the population.

## Evidence Confidence

**Verified** — the 48/40 flow, the 7-technical/1-personal attrition split, the 14/48 compatibility count, all three pre-registered criteria and their outcomes, every per-stream completeness figure, the acceptability percentages, and the no-adverse-events result. Read from the full text (Europe PMC PMC12034961), 2026-09-01.

**Unclear** — the actigraphy device model (not named), and the true passive-sensing completeness across the *whole* cohort. The reported 81%-meeting-threshold figure is computed on 27 of 38 participants selected for *not* having significant technical difficulties, which is a favourable denominator; the corresponding whole-cohort figure is not reported and cannot be reconstructed.

**COI:** **Niels van Berkel and Vassilis Kostakos, co-developers of AWARE-Light, are co-authors**, and the paper evaluates AWARE-Light. The paper reports a technical failure mode severe enough to cause 7 withdrawals and 14 handset swaps, which is strongly against interest and increases confidence in the negative findings. The acceptability framing is more exposed.

**Related papers on the same cohort — do not double-count.** At least two further analyses of this Melbourne AWARE-Light cohort exist: Mavragani et al., *JMIR Formative Research* 2025 (nomophobia and smartphone-inferred behaviours in youth with depression, N=41, PMC11888105) and an *Early Intervention in Psychiatry* 2025 paper on physical activity and psychological symptoms (N=40, PMC11847758). Sample sizes, site and platform match; treat these as analyses of one deployment, not three.

## Key Links

- Paper (OA, CC BY-NC): https://doi.org/10.1177/20552076251330509
- Europe PMC: https://europepmc.org/article/PMC/PMC12034961
- AWARE-Light: https://awarelight.github.io/
- Local PDF: `../literature/2025-camargo-digitalhealth-smartsense-d-aware-light-youth-depression.pdf`

## Related profiles

- Platform: [AWARE](../../module-02-digital-phenotyping/profiles/aware-framework.md)
- Android-only requirement as a recruitment constraint: [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md)
- Provisioned phones and retention: [`radar-mdd-longterm-engagement.md`](radar-mdd-longterm-engagement.md)
- Pre-enrolment technical screening: [`mindlamp-relapse-3site.md`](mindlamp-relapse-3site.md)
- Safety of intensive monitoring in high-risk mental-health cohorts: [`avicenna-ema-suicidal-ideation-iatrogenic.md`](avicenna-ema-suicidal-ideation-iatrogenic.md)

## Sources

1. Camargo A, et al. *Digital Health* 2025;11:20552076251330509. DOI 10.1177/20552076251330509. Full text read from Europe PMC (PMC12034961), 2026-09-01. Establishes every figure in this profile.
2. Mavragani A, et al. *JMIR Form Res* 2025;9:e57512 (PMC11888105) and *Early Interv Psychiatry* 2025 (PMC11847758) — identified as sibling analyses of the same cohort; abstracts and methods sections only, **Reported**.
