# Lubitz et al. 2022 — The Fitbit Heart Study: a siteless remote trial, N=455,699

## Quick Facts

| Field | Details |
|---|---|
| Citation | Lubitz SA, Faranesh AZ, Selvaggi C, Atlas SJ, McManus DD, Singer DE, Pagoto S, McConnell MV, Pantelopoulos A, Foulkes AS. "Detection of Atrial Fibrillation in a Large Population Using Wearable Devices: The Fitbit Heart Study." *Circulation* 2022;146:1415–1424. DOI [10.1161/CIRCULATIONAHA.122.060291](https://doi.org/10.1161/CIRCULATIONAHA.122.060291). PMC9640290. |
| Study design | Prospective, single-arm, **siteless remote clinical trial** |
| Sample size (enrolled / analyzed) | **455,699 enrolled**; 4,728 (1.0%) received an irregular heart rhythm detection (IHRD); **1,057 contributed an analyzable ECG patch** for the primary outcome |
| Population | US adults ≥22 without diagnosed AF, not on oral anticoagulants, no pacemaker/defibrillator. **Median age 47 (IQR 35–58); only 12% aged ≥65; 71% female; 73% White.** |
| Duration | Enrolment 6 May – 1 Oct 2020; **median 122 days (IQR 110–134) at risk** for an IHRD |
| Devices/platforms used | **[Fitbit](../../module-01-wearables/profiles/fitbit-google.md)** — Ionic, Charge 3/4, Versa/Lite/2/3, Sense, Inspire HR/2 (participant-owned) with Android or iOS; **BioTelemetry ePatch** single-lead ECG; **PlushCare** telehealth |
| Funding/COI | **Fitbit LLC (Google LLC)** — three authors are Fitbit/Google employees (Faranesh, McConnell, Pantelopoulos). **Individual-level data explicitly not made available**, citing confidentiality and *company policy regarding user data*. |
| Last verified | 2026-08-31 |

## Summary

The direct comparator to [the Apple Heart Study](apple-heart-data-management-lessons.md), run two
years later at similar scale, and the two together give this module its clearest picture of what
happens operationally in a very large siteless consumer-wearable trial.

Two findings stand out for deployment planning. First, **wear time was extraordinary — a median of
23 hours per day (IQR 22–24), with 85% of at-risk days exceeding 18 hours of wear.** This is far
above anything achieved by a *researcher-provisioned* device in this module (compare RADAR-MDD's
62.5% wear-time over 18 months), and the reason is straightforward: these were devices participants
had already chosen to buy and wear. **The BYOD design that damages representativeness is the same
design that produces near-total wear compliance.** That tradeoff is the single most useful thing
these two studies teach jointly.

Second, the **post-notification funnel collapsed in almost exactly the same way as Apple's**, despite
a **$50 incentive per telehealth visit** that Apple did not offer: 4,728 notified → 1,671 (35.3%)
completed a first telehealth visit → **~24–25% wore and returned an ECG patch**. Paying participants
$50 per visit produced a *lower* first-visit rate than AHS's unpaid 44%.

## Instrumentation and Deployment Model

**Pure BYOD** — participants used Fitbit devices they already owned, with their own paired
smartphone. **56% used smartwatches, 44% used fitness trackers**, so the cohort spans two quite
different form factors. A valid phone number and email were required.

**Algorithm design** (relevant to interpreting the wear-time figure): the algorithm ran **centrally
on a server** using routinely collected PPG data after device sync — not on-device — and was
"unlocked centrally only for users who consented." It analysed PPG **only during periods when the
accelerometer indicated the participant was stationary**, to suppress motion artefact. Data were
processed as **5-minute tachograms acquired every 2.5 minutes (50% overlap)**; **11 consecutive
irregular tachograms** triggered an IHRD notification.

Note the contrast with Apple's design (one-minute tachograms, opportunistic sampling every few hours
at rest, escalating to ~every 15 minutes, notification on 5 of 6 irregular tachograms).

**Post-notification protocol:** telehealth visit via PlushCare → mailed BioTelemetry ePatch →
wear one week → return by prepaid mail → results in a PlushCare portal → second telehealth visit.
**Up to $50 incentive for completing each telehealth visit.** Participants with abnormal findings
were encouraged to see their own provider or given a local referral.

**Retrospective data inclusion — a design choice with measurable consequences.** IHRDs could be based
on pulse tachogram data from **up to 30 days before enrolment**; 2,422 (51.2%) of notifications were
generated this way. Those participants then received their ECG patches substantially later
(**32±19 days vs 16±13 days** from notification) and were less likely to complete the 90-day survey
(29.0% vs 34.7%). Mining retrospective data doubled the notification yield but degraded the
follow-up chain.

## Recruitment and Retention

Recruitment ran through **email, in-app notifications, social media and other marketing channels** —
i.e. against an existing installed user base, which is why 455,699 enrolled in under five months.

**The engagement funnel:**

| Stage | N | % of previous | % of notified |
|---|---|---|---|
| Enrolled | 455,699 | — | — |
| **IHRD notification** | **4,728** | **1.0%** | 100% |
| Completed first telehealth visit | **1,671** | **35.3%** | 35.3% |
| — of whom excluded for pre-existing AF confirmed at visit | 142 (8%) | | |
| **Wore and returned an analyzable ECG patch** | **1,057** | | **~22%** |

**IHRD rate by age:** 3.6% (2,070) among those ≥65, versus 0.7% (2,658) among those <65 — a
five-fold difference, in a cohort that was only 12% aged ≥65. The population most likely to benefit
was the least represented.

**Cumulative incidence of IHRD at 90 days** among those contributing ≥1 hour of wear: **0.94%
(95% CI 0.91–0.97)**, and similar (0.87%) among the prospective-data-only subgroup.

**Why people didn't attend — actually asked, and the answer is instructive.** Post-notification
surveys were completed by 916/1,671 (54.8%) of telehealth attenders versus 588/3,057 (19.3%) of
non-attenders (p<0.001). Among non-attending respondents, **the most common reason (n=139, 23.6%)
was that they had discussed the notification with their own doctor instead of the study telehealth
provider.** That is not disengagement — it is participants routing around the study protocol into
usual care, which is arguably the *correct* clinical behaviour and which no retention strategy would
fix. It is a category of "loss to follow-up" that deserves separate accounting.

**Differential attrition, characterised:** those who initiated a telehealth visit were slightly
younger, more likely female and White, and had **fewer cardiovascular comorbidities** — though the
authors describe the differences as modest. The direction matters: the sicker participants were
marginally less likely to complete the confirmatory pathway.

## Data Completeness and Technical Issues

**Wear time — the headline operational number:**

- **Median 23 hours/day (IQR 22–24).**
- **85% of at-risk days had ≥18 hours of wear (IQR 54%–96%).**

Note the IQR on that last figure spans 54% to 96%, so while the median participant wore the device
almost constantly, a quarter of participants were below 54% of days at ≥18 hours. The median is
excellent; the distribution has a long tail.

**ECG patch failures — a hardware attrition class worth budgeting:**

- **18 patches returned with no data at all**, possibly due to activation error.
- **32 patches were not readable** by BioTelemetry systems, from corrupted data or device damage.
- Replacement patches were sent where data were unanalyzable.
- **Median patch wear 7.0 days (IQR 6.2–7.0)** — essentially full compliance once applied.

**Latency:** median **18.6 days (IQR 10.9–30.7)** from IHRD notification to the start of ECG patch
monitoring. For a paroxysmal arrhythmia, a two-to-three-week gap between detection and confirmatory
monitoring is itself a source of false negatives — and it was far worse for the retrospective-data
subgroup (32 days mean).

**Primary outcome:** AF was present in **340/1,057 (32.2%)** of participants with an IHRD
notification and an analyzable patch. Note the trial was powered against an expected PPV of 80%
(target 155 participants with an IHRD *during* patch wear, 80% power to test PPV >70%); the
headline 32.2% is a different quantity — the yield of the whole notification-to-patch pathway rather
than the tachogram-level PPV.

**A stated design constraint with operational force:** because PPG-based detection operates during
inactivity, **"wearing devices at night may maximize the sensitivity,"** and **"detection of atrial
fibrillation during periods of active motion remains a challenge."** Night-time wear is therefore a
protocol requirement for this class of study, not an optional extra — which in turn makes charging
schedule a first-order design question.

## Feasibility Findings

The study demonstrates that a **siteless trial can enrol at massive scale against an installed
consumer base** and can achieve wear compliance no provisioned-device study in this module comes
close to. It equally demonstrates that **enrolment scale does not carry through a multi-step
confirmatory protocol**: 455,699 enrolled produced 1,057 analyzable primary-outcome records, a yield
of 0.23%.

The **$50-per-visit incentive did not solve the funnel**. Read alongside AHS's unpaid 44%
first-contact rate, this is reasonable evidence that modest financial incentives are not the binding
constraint on post-notification engagement in these trials — and the survey data suggest why:
roughly a quarter of non-attenders had simply taken the finding to their own physician.

## Relevance to Future Study Design

1. **BYOD consumer wearables deliver wear compliance that provisioned research devices cannot.**
   23 h/day median versus RADAR-MDD's 15.1 h/day mean over a longer horizon. If wear time is the
   binding constraint, participant-owned devices win decisively.
2. **The same design costs you representativeness.** 71% female, 73% White, only 12% aged ≥65 — in a
   trial about a condition whose detection rate was five times higher in the ≥65 group. Read with
   [Cho et al.](byod-demographic-imbalance.md)
3. **Two independent trials at ~450k scale lost ~75–80% of their notified cohorts** at the same
   points. Treat the post-notification funnel as the design's actual sample-size determinant.
4. **Modest incentives did not close the gap.** Budget engagement design, not just payment.
5. **Ask non-attenders why.** "I took it to my own doctor" (23.6%) is a fundamentally different
   category from disengagement and should be reported separately in future trials.
6. **Retrospective data mining is a real but costly lever** — it produced half the notifications
   while lengthening time-to-confirmation by ~16 days and reducing survey completion.
7. **Budget for confirmatory-device failure**: 50 of ~1,100 patches (~4.5%) returned unusable.
8. **Minimise notification-to-confirmation latency.** 18.6 days median is long for a paroxysmal
   condition.

## Evidence Confidence

**Verified** for enrolment, demographics, wear-time distribution, IHRD rates, the engagement funnel,
patch failure counts, latency figures and the 32.2% AF yield — primary reported results read from
the full text.

**COI — the most significant in this module.** The study was conducted by **Fitbit LLC (Google LLC)**
with three Fitbit/Google authors, evaluating Fitbit's own algorithm on Fitbit's own devices. Two
specific consequences:

- **Individual-level data are explicitly not available**, cited to participant confidentiality *and*
  "company policy regarding user data." Only the protocol and statistical analysis plan are shared.
  Independent verification of these figures is therefore not possible.
- The **wear-time figures are derived from "Fitbit device software metrics"** — the manufacturer's
  own proprietary wear-detection, not an independent measure. A 23 h/day median should be read with
  that in mind; it is a vendor-defined quantity. Treat wear time here as **Corroborated** rather than
  Verified against an external standard.

None of this impugns the engagement-funnel figures, which run against commercial interest.

**Scope note:** this is primarily a detection/screening trial. It earns a Module 3 entry for its
operational content at scale, not for its AF-detection performance, which belongs in
[`../../module-01-wearables/validation-evidence.md`](../../module-01-wearables/validation-evidence.md).

**Availability:** *Circulation* is paywalled (CC BY-NC-ND on the article itself) and the PMC
author-manuscript PDF route returned HTML. **No PDF obtained**; full text read from the NCBI PMC XML
deposit. Logged as Tier 14 Q110 in `../../shared/unresolved-questions.md`.

## Key Links

- Paper: https://doi.org/10.1161/CIRCULATIONAHA.122.060291
- Europe PMC: https://europepmc.org/article/PMC/PMC9640290
- Local PDF: **not obtained** — see above
- Protocol and statistical analysis plan: in the article's Supplemental Material

## Related profiles

- Device: [Fitbit / Google](../../module-01-wearables/profiles/fitbit-google.md)
- The direct comparator at similar scale:
  [`apple-heart-data-management-lessons.md`](apple-heart-data-management-lessons.md)
- BYOD representativeness: [`byod-demographic-imbalance.md`](byod-demographic-imbalance.md)
- The other very large Fitbit BYOD cohort:
  [`allofus-fitbit-step-counts.md`](allofus-fitbit-step-counts.md)

## Sources

1. Lubitz SA, et al. *Circulation* 2022;146:1415–1424. DOI 10.1161/CIRCULATIONAHA.122.060291. Full
   text read from the NCBI PMC XML deposit (PMC9640290), 2026-08-31. Establishes every figure in
   this profile.
