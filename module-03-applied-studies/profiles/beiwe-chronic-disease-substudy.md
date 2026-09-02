# Yi et al. 2024 — Beiwe substudy embedded in the Nurses' Health Study 3 and Growing Up Today Study, N=2,394, 1 year, 11.1 TB

## Quick Facts

| Field | Details |
|---|---|
| Citation | Yi L, Hart JE, Straczkiewicz M, Karas M, Wilt GE, Hu CR, Librett R, Laden F, Chavarro JE, **Onnela JP**, James P. "Measuring Environmental and Behavioral Drivers of Chronic Diseases Using Smartphone-Based Digital Phenotyping: Intensive Longitudinal Observational mHealth Substudy Embedded in 2 Prospective Cohorts of Adults." *JMIR Public Health and Surveillance* 2024;10:e55170. DOI [10.2196/55170](https://doi.org/10.2196/55170). PMC11512133. |
| Study design | Intensive longitudinal observational mHealth substudy **embedded in two ongoing nationwide prospective cohorts** (NHS3 and GUTS). Stated objective is explicitly feasibility and scalability, measured as protocol adherence. |
| Sample size (enrolled / analyzed) | **2,394 analyzed** — 1,703 (71.1%) from NHS3, 691 (28.9%) from GUTS. Recruitment funnel below. **The largest Beiwe deployment identified in this module.** |
| Population | US adults. Mean age 41.8 (SD 8.1); **93.9% female, 93.7% White**; 60.0% married; 75.9% non-smokers; mean BMI 27.4 (SD 6.7). Nurses and nurses' children — high SES, and the authors say so plainly. |
| Duration | Enrolment Jul 2021 – Aug 2022; collection ended 15 Jun 2023. Intended 1 year per participant; **mean follow-up 214 days (SD 148)**. |
| Devices/platforms used | **[Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)** on participants' own smartphones (BYOD, Android + iOS), processed with the **Forest** library (`jasmine` for GPS) on AWS |
| Funding/COI | Academic (Harvard Chan, Harvard Medical School/Harvard Pilgrim, Brigham and Women's, UC Davis). Onnela, Beiwe's originator, is a co-author. **Participants were not compensated.** |
| Last verified | 2026-08-31 |

## Summary

The scale test. If the question is "can smartphone digital phenotyping be bolted onto an existing
epidemiological cohort at thousands of participants for a year," this is the paper that answers it,
and the answer is a qualified yes with a very specific set of costs.

Three things make it the most operationally useful study in the module. First, it publishes the
**complete recruitment funnel** — 32,441 invited down to 2,394 registered — which almost no
deployment paper does, and which is the number anyone planning a cohort substudy actually needs.
Second, it reports **compliance banded per participant and broken out by operating system**,
revealing that roughly a third of enrolled participants supply almost nothing while roughly 40%
supply nearly everything. Third, it quantifies the **data engineering reality**: 11.1 TB raw
collapsing to 1.9 GB processed, and an explicitly named "steep learning curve" for the computing
infrastructure.

It is also, unusually, an **uncompensated** cohort — which makes its adherence figures a clean
counterpoint to the incentive-supported RADAR studies.

## Instrumentation and Deployment Model

**BYOD, both operating systems: 1,743 iOS (72.8%), 645 Android (27.0%), 6 who switched mid-study.**
Note this is close to the inverse of [Kiang et al.'s](beiwe-missing-data-sociodemographic.md) 77%
Android pooled sample — a reminder that OS mix is a property of the recruited population, not of the
platform.

**Sampling configuration (the duty cycles matter for interpreting everything below):**

- **GPS: 90 seconds on, 810 seconds off** — a position estimate roughly every 15 minutes.
- **Accelerometer: triaxial at 10 Hz, 30 seconds on / 60 seconds off** in 90-second intervals.
- Interval collection was chosen explicitly **to minimise battery consumption**.
- **Surveys every 10 days**, topic rotating on a fixed schedule: sitting, physical activity, sleep,
  mood, stress and enjoyment, food-frequency sections (vegetables, meat, beverages, nuts and dairy,
  fruits), and green-space visits. A pet-ownership survey ran at registration.

**Participant instructions:** keep the smartphone on their person during waking hours and at home at
night, and **sync over Wi-Fi at least once a week**. Weekly Wi-Fi access was an eligibility
criterion.

**Eligibility** required (1) owning a smartphone, (2) weekly Wi-Fi access, (3) living in the 48
contiguous states — plus cohort-specific prior-engagement criteria (NHS3: ≥2 completed main
questionnaires plus expressed interest in biospecimen collection; GUTS: current responder answering
yes to biospecimen questions on the 2019 questionnaire). **Participants already enrolled in another
NHS3/GUTS substudy were excluded.**

**Privacy design worth noting:** no personal or health-related information was entered through
Beiwe; raw data encrypted before transmission to AWS; accelerometer data deleted from temporary
analytical storage after processing; both production and analytics servers behind two-factor
authentication and SSH keys.

## Recruitment and Retention

**The recruitment funnel — the most reusable table in this profile:**

| Stage | N | % of previous | % of invited |
|---|---|---|---|
| Invited to eligibility screening | **32,441** | — | 100% |
| Completed the screener | 3,470 | **10.7%** | 10.7% |
| Determined eligible | 3,410 | 98.3% | 10.5% |
| Completed consent | 2,796 | 82.0% | 8.6% |
| **Downloaded and registered the app** | **2,394** | 85.6% | **7.4%** |

**Enrolling 2,394 participants required inviting 32,441 — a 7.4% end-to-end yield, and the screener
step alone lost 89.3%.** For anyone sizing a cohort substudy, this ratio is the planning figure.
Note this is a *pre-engaged* population (existing cohort members with a history of returning
questionnaires), so 7.4% should be treated as an optimistic ceiling for a cold-recruited sample.

**Follow-up length, overall and by OS** (defined as app registration date to last data transmission
or the 1 Nov 2022 download date, whichever came first):

| Retained at least | Overall | Android (n=645) | iOS (n=1,743) |
|---|---|---|---|
| 7 days | 2,039 (85.2%) | 523 (81.1%) | 1,510 (86.6%) |
| 2 weeks | 1,954 (81.6%) | 501 (77.7%) | 1,447 (83.0%) |
| 1 month | 1,867 (78.0%) | 472 (73.2%) | 1,390 (79.8%) |
| 3 months | 1,669 (69.7%) | 405 (62.8%) | 1,259 (72.2%) |
| **6 months** | **1,371 (57.3%)** | **324 (50.2%)** | **1,042 (59.8%)** |

**iOS retained better than Android at every horizon**, with the gap widening over time (5.5
percentage points at 7 days → 9.6 points at 6 months).

**Selection effects the authors report honestly:** comparing substudy participants against the
active parent cohorts, the substudy skewed **older, more White, more non-smoking, and higher BMI**
than active NHS3, and **more female, less married, higher BMI** than active GUTS. They also note the
male:female ratio among those invited was slightly higher than among those not invited, because
male NHS3 recruitment began in later cycles — making the sample slightly less representative of the
cohort as a whole.

## Data Completeness and Technical Issues

**Volume:** 11.1 TB received — **10.5 TB accelerometer, 243.5 GB GPS, 23,682 survey submissions**.

**Per-participant averages:** 14.8 (SD 5.9) valid hours/day of GPS and 13.2 (SD 4.8) valid hours/day
of accelerometer data. Using a 10-hour cutoff, **51.5% (1,232/2,394) and 53.2% (1,274/2,394) of
participants had >50% valid data collection days** for GPS and accelerometer respectively.

**Participant-level compliance bands — the key distributional finding:**

| Band | GPS overall | Android | iOS | Accel overall | Android | iOS |
|---|---|---|---|---|---|---|
| **Excellent (≥75%)** | 946 (39.5%) | 172 (**26.7%**) | 769 (**44.1%**) | 1,021 (42.7%) | 241 (37.4%) | 775 (44.5%) |
| Good (~50–75%) | 286 (12.0%) | 109 (16.9%) | 177 (10.2%) | 254 (10.6%) | 76 (11.8%) | 178 (10.2%) |
| Fair (~25–50%) | 328 (13.7%) | 94 (14.6%) | 234 (13.4%) | 311 (13.0%) | 79 (12.3%) | 232 (13.3%) |
| **Poor (≤10%)** | **834 (34.8%)** | 270 (**41.9%**) | 563 (32.3%) | **808 (33.8%)** | 249 (38.6%) | 558 (32.0%) |

The distribution is **strongly bimodal**: about 40% excellent, about 34% poor, and only ~26% in
between. A mean compliance figure would badly misdescribe this cohort. **Android users were far less
likely to be "excellent" on GPS (26.7% vs 44.1%) and more likely to be "poor" (41.9% vs 32.3%)** —
consistent in direction with Kiang et al.'s finding of higher GPS non-collection on Android.

At the participant-day level, **40.4% of potential observation days had GPS data and 40.0% had
accelerometer data**; restricted to each participant's actual follow-up period, this rises to
**68.8% (GPS) and 68.2% (accelerometer)**. The gap between those two framings is entirely
app-deletion — and the authors attribute the shortfall primarily to **participants deleting the app
before the end of follow-up (i.e. unenrolling by uninstalling) rather than to dead batteries or app
malfunction**.

**Survey response — the weakest stream.** Mean of **10 (SD 11) surveys per participant**, with a
**mean response rate of 36% (SD 17%, median 41%)**. The pet survey at registration achieved
**82.7%** (1,980/2,394) — an onboarding-moment effect worth noting. Early rotating surveys ranged
from 26.7% (Emotion, Aug 2021) up to 79.8% (Emotion, Oct 2021), with several in the 47–51% band.
Median completion time was **53 seconds (SD 197; median 21 s)**.

**Documented challenges, stated by the authors:**

1. **"A steep learning curve for exploring, setting up, and fine-tuning an optimized computing
   infrastructure"** for managing, processing and analysing this data volume — named as a genuine
   obstacle for teams without the technical skills. They used AWS.
2. **Occupational access restriction:** a large proportion of participants were **nurses who may not
   be permitted to carry personal smartphones during work hours**. The authors did not collect data
   on whether participants could carry phones at work, so they cannot quantify it — a self-identified
   gap and a striking one, given it plausibly explains a meaningful share of daytime missingness in
   precisely this cohort.
3. **Missingness by design:** much of it follows directly from the on-off duty cycles.
4. **No exit survey.** They did not ask departing participants why they dropped out, and did not
   collect feedback on survey experience — so their burden-reduction strategy (shortening surveys)
   could not be evaluated.

**Processing outcome:** 10.5 TB of raw accelerometer data reduced to **1.9 GB processed**, via
Forest's `jasmine` GPS imputation (filtering participants with insufficient data and coordinates
with <50 m horizontal accuracy, identifying flights and pauses, then imputing missing flights and
pauses) plus walking recognition. The authors present the cloud-based approach as
**cost-effective**, eliminating local raw-data storage.

**Derived outputs:** participants spent an average of **14.6 (SD 7.5) hours/day at home** and **1.6
(SD 1.6) hours/day on trips**, with **1,046 (SD 1,029) steps/day** recorded — the very large SD on
steps, and the low absolute value, both reflect phone-carriage patterns rather than true ambulation
and should not be read as physical-activity estimates.

## Feasibility Findings

The authors' stated conclusion: adherence "was either higher or similar to most previous studies
with shorter follow-up periods and smaller sample sizes," and the effort produced a large linkable
dataset. Their framing throughout is that **duration and scale were achieved without compromising
data resolution** — 7–14 days is the norm for intensive longitudinal studies, and this ran a year.

They also concede directly that **"the missingness in the aforementioned datasets may affect our
ability to answer research questions related to associations between environmental exposures and
health behaviors"** — a notably honest statement about their own primary scientific aim.

## Relevance to Future Study Design

1. **Budget the recruitment funnel at roughly 13:1 invitations-to-enrolments**, even in a
   pre-engaged cohort. The screener is where nearly 90% is lost.
2. **Expect a bimodal compliance distribution, not a central tendency.** ~40% excellent / ~34% poor
   means analytic sample size is roughly half the enrolled N for anything requiring dense data.
   Report banded compliance rather than means.
3. **Android under-performs iOS on both retention and compliance**, and the gap widens with time.
   An Android-heavy population needs a larger N for the same analytic yield.
4. **App deletion is the dominant loss mechanism**, not technical failure — which makes it a
   retention/engagement problem, addressable by contact and incentives, rather than an engineering
   one. This cohort had **neither compensation nor an exit survey**; both are cheap additions.
5. **Ask whether participants can physically carry their phone during the hours you care about.**
   The nurses-at-work problem is a whole occupational class of daytime missingness that no sampling
   configuration can fix, and the authors could not quantify it because they never asked.
6. **Onboarding-moment surveys get answered.** 82.7% at registration versus a 36% ongoing mean.
   Front-load anything essential.
7. **Budget data engineering explicitly.** 11.1 TB → 1.9 GB is a large reduction, but the authors
   name infrastructure setup as one of only two major challenges they encountered.
8. **This is the uncompensated baseline.** 57.3% still contributing at 6 months with no payment for
   participation is a useful floor against RADAR-MDD's compensated ~80% outcome completion.

## Evidence Confidence

**Verified** for the recruitment funnel, retention-by-OS table, compliance bands, data volumes,
survey response rates and derived mobility outputs — all primary reported results read from the
published PDF.

**Corroborated** for the claim that adherence was "higher or similar to most previous studies" —
plausible and directionally supported by the other profiles in this module, but it is a narrative
comparison against studies of very different design, not a systematic benchmark.

**Generalisability — the central caveat, stated by the authors:** participants came from two cohorts
"which primarily consisted of White female individuals of a relatively high SES" (93.9% female,
93.7% White), and they warn findings "may not be applicable to other populations." Combined with
eligibility criteria requiring **smartphone ownership and weekly Wi-Fi access**, this is a textbook
instance of the BYOD selection problem documented in
[Cho et al.](byod-demographic-imbalance.md) — and worth noting that even this highly-engaged,
high-SES, pre-consented population yielded only 7.4% end to end.

**Pre-heartbeat.** Data collection ran Jul 2021 – Jun 2023; Beiwe's heartbeat/keepalive was globally
enabled 2024-05-29. These compliance figures predate it — see
[`beiwe-als-adherence.md`](beiwe-als-adherence.md) and Tier 14 Q106 in
`../../shared/unresolved-questions.md`. Given that app deletion (not background suspension) was the
authors' stated dominant loss mechanism, heartbeat would plausibly help less here than in studies
where the app remained installed but dormant.

**COI:** Onnela, Beiwe's originator, is a co-author. The reported figures include a 34.8% "poor"
compliance band and an acknowledgement that missingness may compromise the study's own scientific
aims, so the paper is not presenting the platform flatteringly.

## Key Links

- Paper (OA): https://doi.org/10.2196/55170 · https://publichealth.jmir.org/2024/1/e55170
- Europe PMC: https://europepmc.org/article/PMC/PMC11512133
- Forest (analysis library used): https://github.com/onnela-lab/forest
- Local PDF: `../literature/2024-jmir-beiwe-chronic-disease-drivers-substudy.pdf`

## Related profiles

- Platform: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- Same platform, missingness modelled directly:
  [`beiwe-missing-data-sociodemographic.md`](beiwe-missing-data-sociodemographic.md)
- Same platform, no engagement scaffolding, small clinical cohorts:
  [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
- BYOD selection effects: [`byod-demographic-imbalance.md`](byod-demographic-imbalance.md)
- Compensated, supported contrast at similar duration:
  [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md)

## Sources

1. Yi L, et al. *JMIR Public Health Surveill* 2024;10:e55170. DOI 10.2196/55170. Full text and
   tables read from the published PDF (via Europe PMC, PMC11512133), 2026-08-31. Establishes every
   figure in this profile.
