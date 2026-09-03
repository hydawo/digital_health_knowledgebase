# Weingarden et al. 2025 and 2026 - MetricWire EMA plus Beiwe passive sensing in a nationally recruited body dysmorphic disorder cohort, N=87

## Quick Facts

| Field | Details |
|---|---|
| Citation | Anchor paper. Weingarden H, Meng X, Armey M, Onnela JP, Jaroszewski A, Armstrong CH, Wilhelm S. "Predicting the strength of next-day negative emotion states in body dysmorphic disorder using passive smartphone data: An intensive longitudinal assessment study." *Internet Interventions* 2025;40:100833. DOI [10.1016/j.invent.2025.100833](https://doi.org/10.1016/j.invent.2025.100833). PMID 40486130 / PMC12143762. Published online 2025-05-15, CC BY-NC-ND. Second paper, same deployment. Weingarden H, Jaroszewski AC, Armey M, Hoeppner BB, Armstrong CH, Onnela JP, Wilhelm S. "Predicting concurrent and short-term desire and intent to attempt suicide among people with body dysmorphic disorder using ecological momentary assessment of anxiety and shame." *Journal of Psychopathology and Clinical Science* 2026;135(3):403-412. DOI [10.1037/abn0001054](https://doi.org/10.1037/abn0001054). PMC12614476 (author manuscript). |
| Study design | Approximately three-month naturalistic intensive longitudinal assessment study, single arm, no comparison group. Both papers are secondary analyses of a pre-registered primary study (ClinicalTrials.gov NCT04254575). Mass General Brigham IRB protocol 2019P002041. The 2025 paper models next-day emotion from passive data. The 2026 paper models momentary suicide desire and intent from EMA. |
| Sample size (enrolled / analyzed) | 87 consented and eligible. 2025 paper analysed 83 after removing 3 with no passive smartphone data and 1 with extreme passive-data outliers. 2026 paper analysed all 87 who completed any EMA questionnaire, with 86 in the prospective models. A further 5 were excluded at screening for active suicidal ideation with plan or intent and referred out. Number pre-screened is not reported. |
| Population | US adults aged 18 or over with a primary MINI diagnosis of BDD and a BDD-YBOCS score of 24 or more, plus at least one of suicidal thoughts in the past month, alcohol use in the past two weeks, or marijuana use in the past two weeks. In the 2026 sample of 87, mean age 29.39 (SD 8.99, range 18 to 55), 73.56% female, 72.41% White, 100% with at least one comorbid diagnosis. 85 of 87 endorsed lifetime suicidal ideation on the baseline C-SSRS. |
| Duration | About 3 months. EMA in two 14-day waves, after baseline and after the 1.5-month midpoint, 28 EMA days in total. Passive sensing ran continuously for the full 3 months. Data were collected between July 2020 and May 2023 (2026 paper). |
| Devices/platforms used | [MetricWire](../../module-02-digital-phenotyping/profiles/metricwire.md) for EMA and [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md) for raw GPS and accelerometer, both installed on participants' own iOS or Android phones. Forest produced the daily passive summaries. REDCap held the baseline self-report surveys. No wearable. |
| Funding/COI | NIMH K23MH119372 (Weingarden). Weingarden reports employment at HabitAware, advisory roles with Augmend Health and APA Labs, and research funding from Koa Health. Armey is a compensated member of Ilumivu's scientific advisory board, holds stock options in a company providing EMA services, and the 2026 paper states he "could potentially benefit from the results of this research." Wilhelm reports advisory roles with One Mind, Koa Health, Noom and Jimini Health. Onnela declares none in either paper. Participant compensation is not reported in either paper. |
| Last verified | 2026-09-03 |

## Summary

This is the module's first deployment that runs MetricWire and Beiwe side by side in one clinical cohort, each doing one job. MetricWire delivered the surveys. Beiwe collected raw GPS and accelerometer in the background. The 2025 paper is the only one of the two that uses both streams, and the 2026 paper uses MetricWire data alone.

The deployment was fully remote. Participants were recruited nationally across the United States, screened by video, and walked through app installation by a coordinator on a video call. Nobody met study staff in person. That makes it one of the few Module 3 entries where a clinician-diagnosed psychiatric sample was assembled without a clinic.

The two operational figures worth carrying come from different papers. EMA completion was 72% of 84 prompts, a mean of 61.25 (SD 16.21), with 80.46% of participants completing more than 60% of prompts (2026). The share of participant-days that had both at least one EMA entry and a complete set of daily passive summaries was 85.9% (2025). The second figure is the joint yield of the two platforms on the same day, and it is the number a future dual-platform design needs.

Three of 87 participants produced no passive data at all (2025). The paper does not say why. When passive summaries went missing they tended to go missing together, whole days at a time, rather than one metric at a time.

## Instrumentation and Deployment Model

Bring your own device. Eligibility required an Android or iOS smartphone, Wi-Fi at home, and a computer or tablet for the online surveys (both papers). The 2026 paper adds "insufficient technology literacy to complete study procedures" as an exclusion criterion. How that was assessed is not described.

Two apps were installed on each phone. The 2025 Methods state that "the research coordinator helped eligible participants download two study apps, Metricwire (Metricwire, 2023) and Beiwe (Onnela et al., 2021), for collection of EMA and raw passive smartphone data, respectively." The 2026 paper describes the same virtual setup session but names only MetricWire, because its analysis uses only EMA. Neither paper says whether Beiwe was self-hosted or run through a managed service. Neither names the MetricWire app version or configuration beyond the prompt schedule.

The Beiwe sampling configuration is reported in full (2025). GPS was sampled for 90 seconds every 15 minutes. The accelerometer was sampled at 10 Hz for 10 seconds every 30 seconds. The authors describe these as intermittent "for operational reasons (e.g., preserving battery life)" and state that GPS sampling "creates data gaps by design," with further gaps expected from poor reception indoors. Data were encrypted on the phone while waiting for Wi-Fi upload and re-encrypted on the server. Random offsets were added to latitude and longitude on the phone before upload.

The collection window, July 2020 to May 2023, predates Beiwe's heartbeat feature, which was globally enabled on 2024-05-29. The passive completeness figure here should be read as a pre-heartbeat lower bound, as with the other Beiwe profiles in this module.

Raw GPS and accelerometer were turned into daily summaries with the Forest library. Gaps in the GPS trajectory were imputed with the lab's sparse online Gaussian process method before summaries were computed. Six summary statistics were pre-selected from a larger available set. Home time, distance travelled, number of significant places, total pause time and location entropy came from GPS. Step count came from the accelerometer.

### EMA schedule

Each EMA day carried four questionnaires (2026). One was a morning diary available from 7 am to 11 am, asking about "overall yesterday." Its data were not used in either paper, and its completion rate is not reported. The other three asked about "right now" and were sent at random times inside three windows, 10:00 am to 1:30 pm, 1:45 pm to 5:15 pm, and 5:30 pm to 9:00 pm. Each expired 30 minutes after it was sent. All compliance figures below refer to the 84 "right now" prompts only.

The two waves were separated by 1.5 months. Both papers give the same reason, to reduce burden, increase adherence, and spread the time frame so the emotions sampled would vary more.

### Safety protocol

The EMA carried two suicide items scored 0 to 10 (2026). A desire score of 10 or an intent score of 8 or higher triggered a telephone risk assessment. The number of such calls is not reported. The authors say the choice to exclude people with active ideation and plan or intent at screening was made partly "to balance feasibility of implementing the safety protocol" in a nationally recruited sample they could not reach in person.

## Recruitment and Retention

Recruitment was national and almost entirely online. The 2025 paper lists referrals from colleagues and from the authors' own hospital clinic and research programme, professional organisations, and posts on Facebook, Instagram and Reddit support groups and mental health discussion boards. The 2026 paper adds International OCD Foundation websites and newsletters and describes the online groups as "largely including Reddit communities focused on appearance concerns or mental health."

The funnel had three remote stages. A pre-screening survey, then a phone call with the study coordinator, then a virtual screening and baseline visit over HIPAA-compliant video with a study clinician (a licensed psychologist specialising in BDD or a Masters-level pre-doctoral fellow in the same programme). Assessments were audiotaped and 15% were re-rated by an independent assessor (ICC 0.93 for BDD-YBOCS, 100% agreement on the MINI BDD diagnosis).

| Stage | n | Source |
|---|---|---|
| Interested, pre-screened, or phone-screened | not reported | |
| Excluded at screening for active SI with plan or intent, referred out | 5 | 2026 |
| Consented and eligible | 87 | both |
| No passive smartphone data | 3 | 2025 |
| Extreme outliers in passive data | 1 | 2025 |
| Analysed in the passive-sensing paper | 83 | 2025 |
| Completed any EMA questionnaire, analysed in the EMA paper | 87 | 2026 |
| In the 2026 prospective models | 86 | 2026, Table 3 |

The drop from 87 to 86 in the prospective models is not explained in the text. It is visible only in the N row of Table 3.

Retention to the midpoint and endpoint assessments is not reported. Withdrawals are not reported. Neither paper gives a completion rate for the second EMA wave separately from the first, so whether adherence fell between baseline and the 1.5-month midpoint cannot be read from these papers.

## Data Completeness and Technical Issues

### EMA stream (2026)

Out of 84 possible prompts, participants completed a mean of 61.25 (72%), SD 16.21 (19%). 80.46% of participants completed more than 60% of prompts. The authors call this "strong." The power analysis had assumed a 50% completion rate, which the paper describes as underestimated.

The denominators of the two suicide items give a sense of the total EMA volume. Zero scores made up 2,992 (56%) of responses to the desire item and 4,101 (77%) of responses to the intent item. 85.06% of participants endorsed some suicide desire on EMA during the study and 59.77% endorsed some intent.

Compliance for the morning diary is not reported.

### Passive stream and joint yield (2025)

The paper reports one completeness figure, and it is a joint one. "We used the 85.9% of participant days that had both ≥1 EMA entry and complete daily smartphone summary statistics." The denominator is participant-days within the 28 EMA days, since only those days could carry an EMA entry. Passive completeness across the full three months, by day or by participant, is not reported.

The missingness pattern is described rather than counted. "Missing data across smartphone summary statistics usually occurred simultaneously for a given participant, such that if one summary statistic was missing, some or all others were missing for that day." Because five of the six summaries derive from GPS, and Forest computes them from the same imputed trajectory, a day with no usable GPS loses all five at once. The paper does not separate GPS-day loss from accelerometer-day loss.

Three participants had no passive data. Whether they never installed Beiwe, installed it and it never uploaded, or uninstalled it is not stated. One further participant was dropped for extreme outliers in the passive summaries, without a definition of extreme.

### What is absent

No app crashes, upload failures, battery complaints, permission problems, OS-update effects or support contacts are reported in either paper. No iOS versus Android breakdown is given for enrolment, EMA completion or passive completeness. The papers are prediction studies and treat completeness as a preamble to modelling.

## Feasibility Findings

The 2026 paper lists "strong EMA compliance over 84 prompts and 28 days" as a methodological strength, alongside the size of the clinician-diagnosed BDD sample.

The 2025 paper's design recommendation runs the other way. "Due to the burden of collecting EMA 3 times daily, we collected emotion ratings for 28 days; future studies could collect EMA-rated outcomes fewer times per day over more days, to increase days with both sensor and EMA data and, subsequently, power." The sensor stream ran for 90 days but only 28 of those could be paired with an outcome.

The 2025 paper also argues against adding a wearable. Wearable physiology "may strengthen model performance," but "it limits model generalizability, because it requires individuals to purchase and consistently use an additional device." The authors count reliance on the participant's own phone as a strength of the design.

On eligibility, the 2026 authors say they "carefully designed eligibility criteria related to suicide risk, with the goal of balancing external validity, participant safety, and feasibility / person power," and that managing imminent risk in a nationally recruited sample was too complex to admit people with active plan or intent.

## Relevance to Future Study Design

A dual-platform smartphone study in a remotely recruited psychiatric sample can reach 72% EMA completion with a 30-minute window and three prompts a day, in this cohort with no reported compensation figure. Whether payment was involved cannot be checked from these papers.

The joint figure is the one to plan around. 85.9% of EMA days also had complete passive summaries. If a design needs same-day pairing of active and passive data, the useful denominator is the intersection of the two streams, not either stream alone, and the intersection here was about six days in seven.

Passive summary loss arrives as whole days. A pipeline that derives several metrics from one GPS trajectory will lose them together, so counting missing metrics overstates independent failures and counting missing days is the honest unit.

Budget for a small number of participants who yield no passive data at all. Here it was 3 of 87. The cause is unknown, which is itself the lesson. A study that wants to know why should log installation, first upload and last upload per participant at the time, because it cannot be reconstructed afterwards.

A remote safety protocol changes who can be enrolled. Telephone risk assessment on EMA thresholds was feasible only after excluding the five people at highest risk at screening. The cohort is therefore less severe than the disorder, and the papers say so.

Neither paper reports the second wave separately. A future study with the same two-wave design should report each wave, since the 1.5-month gap is exactly where adherence could be expected to change.

## Evidence Confidence

Verified. The eligibility criteria, the 87 consented and eligible, the 3 with no passive data, the 1 outlier and the 83 analysed, the Beiwe sampling configuration, the encryption and GPS-offset handling, the six Forest summary statistics, the 85.9% joint completeness figure, the whole-day missingness description, the EMA windows and 30-minute expiry, the funding statement and the 2025 conflict declarations were all read from the published PDF of the 2025 paper (Internet Interventions, CC BY-NC-ND) on 2026-09-03.

Verified. The four-questionnaire EMA day including the unused morning diary, the 1.5-month wave separation, the July 2020 to May 2023 collection window, the three-stage remote funnel, the 5 exclusions at screening, the safety-protocol thresholds, the 72% completion with mean 61.25 (SD 16.21) and 80.46% above 60%, the 50% completion assumption in the power analysis, the N of 86 in the prospective models, the sample characteristics, and the 2026 conflict declarations including the Ilumivu statement were all read from the PMC author manuscript of the 2026 paper on 2026-09-03.

Reported. The PMCIDs in Quick Facts were supplied with the profiling brief. The 2025 PDF does not print its PMCID, and the 2026 manuscript states only that it will be available in PMC from 2025-11-14. The 2025 PMID 40486130 is printed in the 2026 paper's reference list.

Unclear. Why 3 participants produced no Beiwe data, whether the 86 in Table 3 reflects one participant with a single EMA observation or something else, and whether the 85.9% figure is computed over 83 or 87 participants. The 2025 text places it in the Methods after the 83 are defined, so 83 is the more likely denominator, but the paper does not say.

Not assessed here. The random forest and cumulative link model results in the 2025 paper, and the mixed-model results on suicide desire and intent in the 2026 paper, are clinical findings and are not deployment content.

Conflict note. One co-author is a paid advisor to Ilumivu, an EMA vendor that competes with MetricWire, and holds stock options in an EMA services company. The 2026 paper states he could benefit from the results. The deployment figures in this profile are simple counts and proportions and neither paper compares platforms, so the conflict does not bear on the numbers carried here. The Beiwe developer is a co-author on both papers and declares no conflict.

## Key Links

- 2025 paper (OA, CC BY-NC-ND): https://doi.org/10.1016/j.invent.2025.100833
- 2025 Europe PMC: https://europepmc.org/article/PMC/PMC12143762
- 2026 paper: https://doi.org/10.1037/abn0001054
- 2026 Europe PMC (author manuscript): https://europepmc.org/article/PMC/PMC12614476
- Registration: https://clinicaltrials.gov/study/NCT04254575
- Local PDF, 2025: `../../module-02-digital-phenotyping/literature/beiwe/2025-weingarden-internetinterventions-predicting-strength-next-day-negative-emotion-states.pdf` (held by Module 2; not duplicated)
- Local PDF, 2026: `../../module-02-digital-phenotyping/literature/beiwe/2026-weingarden-jpsychopatholclinsci-predicting-concurrent-short-term-desire-intent-attempt.pdf` (held by Module 2; not duplicated)

## Related profiles

- Platforms: [MetricWire](../../module-02-digital-phenotyping/profiles/metricwire.md), [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- Other MetricWire deployments in this module: [`metricwire-post-discharge-ema-reactivity.md`](metricwire-post-discharge-ema-reactivity.md), [`metricwire-sgm-youth-ema-feasibility.md`](metricwire-sgm-youth-ema-feasibility.md)
- Suicide-risk EMA on Beiwe with a safety protocol: [`beiwe-inpatient-suicide-pilot.md`](beiwe-inpatient-suicide-pilot.md)
- Beiwe passive completeness in psychiatric outpatients, also pre-heartbeat: [`beiwe-transdiagnostic-outpatient-completeness.md`](beiwe-transdiagnostic-outpatient-completeness.md)
- Remote online recruitment and its risks: [`metricwire-fraudulent-participation.md`](metricwire-fraudulent-participation.md)

## Sources

1. Weingarden H, Meng X, Armey M, Onnela JP, Jaroszewski A, Armstrong CH, Wilhelm S. *Internet Interventions* 2025;40:100833. DOI 10.1016/j.invent.2025.100833. Full text, Table 1 and Table 2 read from the published PDF, 2026-09-03. Establishes the enrolment and exclusion counts, the Beiwe configuration, the Forest pipeline, the 85.9% joint completeness figure and the missingness description.
2. Weingarden H, Jaroszewski AC, Armey M, Hoeppner BB, Armstrong CH, Onnela JP, Wilhelm S. *Journal of Psychopathology and Clinical Science* 2026;135(3):403-412. DOI 10.1037/abn0001054. Full text, Tables 1 to 3 and the notes to Figures 1 and 2 read from the PMC author manuscript PDF, 2026-09-03. Establishes the EMA completion figures, the four-questionnaire schedule, the collection window, the screening exclusions, the safety-protocol thresholds and the conflict statements.
