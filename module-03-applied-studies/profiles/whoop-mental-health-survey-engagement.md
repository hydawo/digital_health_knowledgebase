# Presby et al. 2025 — WHOOP in-app mental-health surveys, 181,574 members over 13 months

## Quick Facts

| Field | Details |
|---|---|
| Citation | Presby DM, Jasinski SR, Capodilupo ER, Holmes KE, von Hippel W, Grosicki GJ, Lee V. "Inter- and Intrapersonal Associations Between Physiology and Mental Health: A Longitudinal Study Using Wearables and Mental Health Surveys." *Journal of Medical Internet Research* 2025;27:e64955. DOI [10.2196/64955](https://doi.org/10.2196/64955). PMID 40700646 / PMC12310073. Published 2025-07-23. |
| Study design | Retrospective longitudinal analysis of **existing consumer-device users**, with monthly in-app surveys. GLMMs plus cross-lagged SEM. No researcher-provisioned devices, no recruitment, no consent process beyond the platform's research-use terms. |
| Sample size (enrolled / analyzed) | **181,574 considered → 170,320 (PHQ-2/GAD-2/combined) and 172,283 (PSS) eligible → intrapersonal subsample 3196 and 3197.** |
| Population | WHOOP members aged >21 in both hemispheres. 67% men / 33% women; mean age 37.4 (SD 10.4); mean BMI 26.4. **Self-selected consumer subscribers** — the authors note this "likely represent[s] a higher socioeconomic status." |
| Duration | **13 months (March 2022 – April 2023)**, monthly surveys. |
| Devices/platforms used | **[WHOOP](../../module-01-wearables/profiles/whoop.md) strap 3.0 and 4.0**, participant-owned. Continuous PPG heart rate and 3-axis accelerometry; vendor-proprietary derived metrics (sleep duration/efficiency/consistency, RHR, HRV, respiratory rate, heart-rate zones, physical activity level). Surveys delivered through the WHOOP mobile app: **PHQ-2, GAD-2, PSS**. |
| Funding/COI | **"WHOOP, Inc provided support in the form of salaries or income for all authors."** DP, SJ, EC, KEH, WvH, GJG and VL acted as employees, consultants or contractors for WHOOP. The company "did not otherwise play a role in the study design, data collection or analysis, decision to publish, or preparation of the manuscript." IRB-exempt (Advarra) — de-identified data, consent to research use. **No participant compensation.** |
| Last verified | 2026-09-02 |

## Summary

The largest cohort in this module by two orders of magnitude, and it is here for one operational
finding rather than for its physiological results.

**7,942,176 days of wear-time data. 307,860 survey responses. And a mean of 1.84 survey responses per
person across 13 monthly survey invitations.**

That is roughly **14% survey completion** in an already-engaged, self-selected, paying consumer
cohort, with the survey delivered inside an app they open voluntarily every day. When the authors
needed participants with enough repeated observations for within-person analysis, they required
**≥8 survey responses plus ≥7 days with >1000 minutes of wear per survey window** — and **170,320
became 3196. A 1.9% survival rate.**

This is finding #7 in [`../README.md`](../README.md) — *enrolment scale does not survive a multi-step
protocol* — in a new and instructive form. Apple Heart went 419,297 → 450 and Fitbit Heart 455,699 →
1,057 through **multi-vendor confirmatory clinical workflows**. Here there is no confirmatory
workflow, no shipping, no clinic visit, no second vendor: just **a monthly two-item questionnaire
inside an app the participant already uses**, and the funnel is still 98% deep.

**The passive stream, meanwhile, was abundant.** The same people wore the device well enough to
generate ~4.1 million (14-day-window) and ~7.9 million (28-day-window) participant-days. The gap
between passive abundance and active scarcity is the widest in this module, and it is reached without
any of the burdens (provisioned hardware, study apps, clinical assessments) that studies usually blame
for active-data attrition.

## Instrumentation and Deployment Model

**No deployment in the conventional sense.** This is a **secondary analysis of an existing consumer
user base**, and its operational lessons are of that specific kind. There was no recruitment, no
onboarding, no researcher contact, no troubleshooting, no compensation, and no attrition in the
study-design sense — only voluntary response.

**Surveys** were "delivered through the WHOOP mobile app to all interested WHOOP members" monthly:
PHQ-2 (depression), GAD-2 (anxiety) and PSS (perceived stress, linearly rescaled 0–6 to match), plus a
summated combination score.

**Wearable data pairing rule, stated:** each survey response was paired with the preceding **14 days**
(PHQ-2/GAD-2, matching their 2-week recall) or **28 days** (PSS, matching its 1-month recall) of
device data. **Windows with fewer than 7 days of wearable data were excluded.** Southern-hemisphere
responses were shifted 6 months to align seasons — a small but transferable detail for any
multi-hemisphere consumer cohort.

**All physiological metrics are vendor-derived, not raw.** RHR is a weighted mean of sleep heart rate;
HRV is a weighted RMSSD over sleep interbeat intervals, weighted toward probable slow-wave sleep and
the end of the sleep episode; sleep consistency is an adapted sleep-irregularity index over a 4-day
window; heart-rate zones are percentages of *estimated* maximal heart rate. **None of these are
independently reproducible from raw data**, which is the standing limitation Module 1's
[WHOOP profile](../../module-01-wearables/profiles/whoop.md) records for the platform and which
applies to every physiological result in the paper.

## Recruitment and Retention

There is no funnel to report in the usual sense, which is exactly what makes the numbers useful as a
ceiling.

| Stage | n |
|---|---|
| Considered for eligibility | **181,574** |
| Eligible (PHQ-2/GAD-2/combination; gender + ≥7 days data) | 170,320 |
| Eligible (PSS) | 172,283 |
| **Intrapersonal subsample** (≥8 survey responses **and** ≥7 days with >1000 min wear per window) | **3196 / 3197 (1.9%)** |

**Mean survey responses per person: 1.84 (SD 1.79)** in the interpersonal sample, versus **10.68 (SD
1.52)** in the intrapersonal subsample. Maximum possible was 13.

**Mean days of wearable data preceding each survey: 13.2 (SD 1.5)** of a possible 14, and **24.7 (SD
5.1)** of a possible 28. Conditional on responding, wear was near-complete.

**Total days of metrics: 4,123,851 (14-day analyses) and 7,942,176 (28-day analyses).**

**Gender skew is severe: 67% men, 33% women**, in a cohort that is not researcher-recruited. This is a
different representativeness failure from the one
[Cho 2022](byod-demographic-imbalance.md) documents for BYOD research cohorts — here the skew is the
**consumer product's own market**, inherited wholesale by any study that analyses its users. The
intrapersonal subsample also skews **older** (mean 40.7 vs 37.4) than the full eligible set, so the
1.9% who survive the engagement filter are not a random draw from the 170,320.

## Data Completeness and Technical Issues

**No technical failure modes are reported at all.** No sync failures, no app crashes, no battery
issues, no non-wear analysis, no data-flow problems. For a study of 7.9 million device-days that is
conspicuous, and it is the direct consequence of the design: the analysis begins after every filter
has been applied, so anything that failed is simply absent from the denominator.

**The definitions that do the work are inclusion filters, not completeness measures:**

- ≥7 days of wearable data in the 14- or 28-day window preceding a survey.
- For the intrapersonal subsample: ≥8 survey responses, and ≥7 days with **>1000 minutes (>16.7 h) of
  data in a 24-hour period** per window.

That >1000-minute criterion is one of the strictest daily wear thresholds in the module — compare
[Master 2022](allofus-fitbit-step-counts.md)'s ≥10 hours plus ≥100 steps and
[Carlson 2026](garmin-low-income-physical-activity.md)'s ≥8 hours plus ≥100 steps — and it is applied
only to the subsample, which is part of why that subsample is 1.9% of the whole.

**Extreme-value clipping** (BMI at 17 and 40 kg/m², age at 70) and exclusion of participants not
selecting "man" or "woman" further shape the analytic set.

## Feasibility Findings

The paper does not frame itself as a feasibility study, and its own limitations section focuses on
selection bias, recall bias, unmeasured confounding, menstrual phase, and the narrowness of the
PHQ-2/GAD-2/PSS instruments. What it demonstrates operationally is:

1. **Passive collection at consumer scale is essentially free and essentially complete**, conditional
   on people continuing to use a product they bought — 13.2 of 14 days, 7.9 million participant-days,
   no researcher contact, no compensation.
2. **Attaching even a minimal active assessment to that population collapses it.** A two-item monthly
   questionnaire achieved 1.84 responses in 13 months.
3. **Consumer-cohort analyses inherit the product's demographics**, not the population's — 67% male,
   mean age 37, likely higher SES by the authors' own account.

The authors mitigate selection bias by "leverag[ing] a large sample size and conduct[ing] within-person
analyses" — which is the correct move statistically, and which relies entirely on the 1.9%.

## Relevance to Future Study Design

1. **If your design needs repeated active responses from a consumer-device cohort, plan for ~2 of 13
   and a 1.9% survival rate to an ≥8-response threshold.** These are the best-case numbers: paying
   subscribers, in-app delivery, a two-item instrument, an app opened daily.
2. **The passive/active gap is a property of the *modality*, not of study burden.** Every other study
   in this module that reports both can attribute the gap partly to research burden — provisioned
   hardware, study apps, clinical visits. This one cannot. The gap is still ~7× at the person level.
3. **Vendor-employed authorship and vendor-derived metrics are inseparable here.** Every physiological
   variable is a proprietary algorithm output whose definition is described but not reproducible.
   Findings about *those metrics* are not portable to another device even where the metric name
   matches.
4. **A consumer cohort's demographics are the product's demographics.** 67% male is not a recruitment
   failure; it is WHOOP's customer base. Any study proposing "recruit from an existing wearable user
   base for scale" is proposing to inherit that.
5. **State the wear threshold.** >1000 min/day is defensible and unusually strict; it is a major
   driver of the 1.9%, and a study quoting a comparable filter and a different survival rate is not
   necessarily disagreeing.
6. **Align the passive window to the instrument's recall period.** 14 days for PHQ-2/GAD-2, 28 for
   PSS. Simple, rarely done, and it removes an obvious source of mismatch.
7. **Shift southern-hemisphere dates by 6 months** in any global consumer cohort where seasonality is
   a covariate.

## Evidence Confidence

**Verified** — the full eligibility flow (181,574 → 170,320 / 172,283 → 3196 / 3197); the survey-response
means (1.84 and 10.68) and the maximum of 13; the total days of metrics (4,123,851 and 7,942,176); the
mean days of data preceding each survey (13.2 and 24.7); the demographic composition of both samples;
all inclusion filters including the >1000-minute criterion and the ≥7-day requirement; the survey
instruments and their pairing windows; the BMI/age clipping; the hemisphere adjustment; the COI
statement and the absence of compensation. Read from the published PDF and PMC XML (PMC12310073),
2026-09-02.

**Not assessed here** — the study's physiological and mental-health association findings. They are the
paper's own subject, they rest on **vendor-proprietary derived metrics that cannot be independently
reproduced**, and sensor/metric validity belongs to Module 1's
[WHOOP profile](../../module-01-wearables/profiles/whoop.md) and literature library rather than to
this module.

**COI — the strongest vendor relationship in the module.** *All* authors were salaried or paid by
WHOOP, Inc; seven of seven acted as employees, consultants or contractors. The analysed data are the
company's own product telemetry, the metrics are its own proprietary algorithms, the survey channel is
its own app, and the paper is favourable to wearables as mental-health monitoring tools. The
operational figures extracted in this profile — the response and survival rates — are **unflattering
to that interest**, which is the main reason they are treated as Verified rather than discounted.

**Scope note.** This is not a research deployment: no recruitment, no provisioning, no consent process
beyond platform terms, no researcher–participant contact. It sits at the edge of this module's scope
and is included because its **engagement funnel is a hard empirical ceiling** on what any study
proposing to piggyback on a consumer wearable user base can expect. Its physiological content is out
of scope here.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.2196/64955
- Europe PMC: https://europepmc.org/article/PMC/PMC12310073
- Local PDF: `../literature/2025-presby-jmir-whoop-physiology-mental-health-longitudinal.pdf`

## Related profiles

- Device: [WHOOP](../../module-01-wearables/profiles/whoop.md)
- **Scale not surviving a protocol:** [`apple-heart-data-management-lessons.md`](apple-heart-data-management-lessons.md),
  [`fitbit-heart-study-afib.md`](fitbit-heart-study-afib.md)
- Consumer-cohort representativeness: [`byod-demographic-imbalance.md`](byod-demographic-imbalance.md),
  [`allofus-fitbit-step-counts.md`](allofus-fitbit-step-counts.md)
- Passive outlasting active: [`beiwe-adolescent-feasibility.md`](beiwe-adolescent-feasibility.md),
  [`beiwe-type-2-diabetes-feasibility.md`](beiwe-type-2-diabetes-feasibility.md)
- Wear-time threshold choice: [`allofus-fitbit-step-counts.md`](allofus-fitbit-step-counts.md),
  [`actigraph-als-upper-limb-wear-time.md`](actigraph-als-upper-limb-wear-time.md)
- Another consumer-wearable cohort with self-selected users: [`oura-university-freshmen-sleep.md`](oura-university-freshmen-sleep.md)

## Sources

1. Presby DM, Jasinski SR, Capodilupo ER, Holmes KE, von Hippel W, Grosicki GJ, Lee V. *J Med
   Internet Res* 2025;27:e64955. DOI 10.2196/64955. Full text, Figure 1 flow and Table 1 read from the
   published PDF and PMC XML (PMC12310073), 2026-09-02. Establishes every figure in this profile.
