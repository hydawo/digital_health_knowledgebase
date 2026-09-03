# Torous, Barnett and Staples 2017 to 2018 - Beiwe's first schizophrenia pilot, 17 outpatients, no payment for app use, no reminders

## Quick Facts

| Field | Details |
|---|---|
| Citation | Anchor: Torous J, Staples P, Barnett I, Sandoval LR, Keshavan M, Onnela JP. "Characterizing the clinical relevance of digital phenotyping data quality with applications to a cohort with schizophrenia." *npj Digital Medicine* 2018;1:15. DOI [10.1038/s41746-018-0022-8](https://doi.org/10.1038/s41746-018-0022-8). PMC6550248. Co-sources on the same deployment: Barnett I, Torous J, Staples P, Sandoval L, Keshavan M, Onnela JP. "Relapse prediction in schizophrenia through digital phenotyping: a pilot study." *Neuropsychopharmacology* 2018;43:1660-1666. DOI [10.1038/s41386-018-0030-z](https://doi.org/10.1038/s41386-018-0030-z). PMC6006347. Staples P, Torous J, Barnett I, Carlson K, Sandoval L, Keshavan M, Onnela JP. "A comparison of passive and active estimates of sleep in a cohort with schizophrenia." *npj Schizophrenia* 2017;3:37. DOI [10.1038/s41537-017-0038-0](https://doi.org/10.1038/s41537-017-0038-0). PMC5643440. Protocol: Torous et al. 2016, *JMIR Mental Health* 3:e16. |
| Study design | Observational pilot, up to three months, with in-clinic assessments every 30 days. Three analyses of one cohort. |
| Sample size (enrolled / analyzed) | 17 enrolled. 16 with any usable data. 15 analysed for anomaly detection. 14 completed at least one phone survey. 13 completed at least one in-clinic sleep questionnaire. |
| Population | Outpatients with schizophrenia in active treatment at a state mental health clinic in Boston. Mean age 26.4. 15 of 17 male. |
| Duration | Up to 90 days per participant. 1,075 person-days across the 15 analysed, median follow-up 79 days. |
| Devices/platforms used | [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md) on participant-owned Android and iOS phones. Accelerometer 10 Hz, 60 s on, 60 s off. GPS 1 Hz, 60 s on, 600 s off. Anonymised call and text logs, screen state, charging state. Symptom surveys of 23 questions delivered in the app. |
| Funding/COI | NIH and NIMH 1DP2MH103909 (Onnela), the Harvard McLennan Dean's Challenge, the Natalia Mental Health Foundation, a National Library of Medicine training grant and a Dupont Warren Fellowship (Torous). All three papers declare no competing interests. The authors are the platform's developers reporting their own platform. |
| Last verified | 2026-09-03 |

## Summary

This is the deployment Beiwe was built for, and the module had no entry for it. It is here as one profile because the three papers report one cohort. Staples 2017 states it followed the 2016 protocol paper, Torous 2018 cites the same protocol and refers to the sleep analysis on "this patient cohort elsewhere," and all three give the same 17 enrolled, the same clinic, the same sampling schedule and the same five relapses.

What it adds is a support model at the bottom of the module's range. Participants "were not paid for app use, not given additional support for app use, and not provided with check in calls or study staff reminders to use the app." They received $25 per clinic visit and $25 a month for the use of their own phone, and that stipend "was not tied to app use." They could not see their data until the study ended. The authors did this deliberately, to keep app use close to real-world conditions.

The results under that model are the numbers to carry. Mean coverage in the first month was 50.2% for GPS and 46.9% for accelerometer, measured against the configured schedule. Accelerometer availability across participants averaged 46% with a range of 2.1% to 89.1%. About half of the three-times-weekly surveys were completed. Among the 14 who took any survey, 12 averaged more than two of the three per week.

Two failure modes in this cohort appear nowhere else in the module in this form. One participant never connected his phone to Wi-Fi, and because uploads were Wi-Fi only, his data "are unfortunately not available for analysis." Two of the five participants who relapsed uninstalled the app, one three weeks and one a week before hospitalisation.

## Instrumentation and Deployment Model

Bring your own device, on purpose. The relapse paper argues that the platform "runs on both Android and Apple smartphones," so no one was excluded for phone type, and that using personal phones "is the only way to scale these types of studies." The data-quality paper adds that the study avoided "payments tied to use of the app, check-in calls or coaching around the app, providing subjects with new phones or study phones" to limit confounding of phone use.

Participants installed the app at the initial clinic visit. Surveys arrived at 10 a.m. on Mondays, Wednesdays and Fridays and covered mood, anxiety, sleep, psychosis and medication adherence. The relapse paper describes the survey schedule as "biweekly" and "twice per week," while the other two papers say three times a week. The inconsistency is recorded here and not resolved.

Uploads used Wi-Fi rather than cellular data "in order to eliminate data charges to the subjects."

Participants could call the study investigator for help. No coaching, therapy, check-in calls or extra appointments were attached to the study.

## Recruitment and Retention

Recruitment was clinic-based. Eligibility required a phone able to run the app (Android 5.0 or iOS 9.0 or later), clinician approval, and capacity to consent. The number approached is not reported.

| Stage | n | Source |
|---|---|---|
| Enrolled | 17 | all three papers |
| Never connected the phone to Wi-Fi, no data uploaded | 1 | Barnett 2018 |
| Under one week of follow-up | 1 | Barnett 2018 |
| Analysed for anomaly detection | 15 | Barnett 2018 |
| With any usable sensor data | 16 | Torous 2018 |
| Completed at least one phone survey | 14 | Torous 2018 |
| Completed at least one in-clinic PSQI | 13 | Staples 2017 |
| Experienced a clinical relapse | 5 | Barnett 2018, Torous 2018 |

Staples 2017 reports that "over 90% of subjects used the Beiwe platform for over 6 weeks." A three-month retention rate is not given in any of the papers, and reasons are not given for the participant with under a week of follow-up or the four without a PSQI.

Relapse was defined as psychiatric hospitalisation or an increase in level of care. Of the five relapsers, three had enough data before relapse for analysis. The other two had uninstalled the app one and three weeks before hospitalisation.

## Data Completeness and Technical Issues

Torous 2018 defines coverage against the configured burst schedule. Each on-cycle is a burst, each observation a ping, and coverage is observed pings over expected pings. Under that definition, mean coverage in the first month was 50.2% for GPS and 46.9% for accelerometer. GPS had fewer bursts, lower within-burst frequency and shorter bursts than accelerometer. Within-burst accelerometer frequency "varies widely by patient, which may depend on the make and type of each user's phone." Coverage "generally depends little on length of follow-up."

Staples 2017 reports accelerometer availability over 30 days as a mean of 46% across participants with a range of 2.1% to 89.1%, and notes that sleep-estimate accuracy fell as missingness rose.

Survey completion is reported two ways. Staples 2017 says "only approximately 50% of EMAs sent to the subjects were completed." Torous 2018 says that of the 14 who completed at least one survey, 12 (86%) averaged more than two of the three weekly surveys. The denominators differ and both are recorded. Time from viewing a survey to completing it fell over the study, which the authors read as familiarity.

Operating system mattered in both directions. Android phones showed significantly less GPS coverage than iOS, accelerometer coverage did not differ significantly, and iPhones had less accelerometer coverage and more GPS coverage on average. Android users were more prompt in starting and finishing surveys. The per-OS counts are in a supplement not included in the PDF.

Explanations the authors offer for lost passive data are the participant turning GPS off, the sensor answering only some queries, sampling shorter or at a different rate than requested, GPS failing indoors, and the phone entering an inactivity mode in which sensors are not recorded. A phone lying still might also ignore accelerometer requests while its GPS becomes easier to fix.

One relapser had reliable collection for a month, then "no data were collected for 2 days prior to the significant behavioral anomalies." Another "ceased responding to any surveys in the 3 weeks prior to relapse despite nearly complete passive data coverage." The active stream stopped and the passive stream did not.

Acceptability was asked about once. "No subjects indicated that passive data made them feel paranoid or afraid."

All collection here predates the platform's 2024 heartbeat feature by several years.

## Feasibility Findings

The authors conclude that digital phenotyping in psychotic disorders is feasible on personal phones, that total passive coverage was "moderately less than expected," that survey timing varies greatly between people, and that 50% coverage "might be sufficient to provide clinical insight" for questions about sedentariness and sociability. They also conclude that data quality and non-random missingness "need careful consideration," and that metadata about coverage and survey latency is not independent of symptom scores.

The sleep paper's conclusion is narrower. Passive sleep monitoring is feasible in schizophrenia "in a scalable and affordable manner," but missing accelerometer data "may not be as accurate, limiting feasibility."

## Relevance to Future Study Design

This is what an unsupported Beiwe deployment looks like. Roughly half the scheduled passive data, half the surveys, and one participant in seventeen lost entirely. Every later Beiwe entry in the module that reports better figures reports more support, more money or both. Compare [Pellegrini 2022](beiwe-transdiagnostic-outpatient-completeness.md), which the authors themselves contrast with this cohort.

Wi-Fi-only upload is a participant-cost decision with a data-loss consequence. It cost one of seventeen here. Later studies on other platforms ran into the same trade ([Bae 2023](aware-binge-drinking-jitai-sensor-loss.md)).

Uninstalling the app before relapse is a failure mode that a completeness dashboard reads as dropout. Two of five relapsers did it. If the clinical event of interest is the thing that makes people leave, the study loses the cases it exists to catch.

Report OS effects per stream. This 2018 paper already found opposite directions for GPS and accelerometer on the same phones, which is the pattern the module later confirmed at scale ([McInerney 2024](beiwe-type-2-diabetes-feasibility.md)).

Record the survey schedule consistently across papers. The same cohort is described as twice and three times weekly in its own publications.

## Evidence Confidence

Verified. The enrolment count, the Wi-Fi and under-one-week exclusions, the 15 analysed and the 1,075 person-days with median 79, the five relapses and two pre-relapse uninstalls, the no-payment and no-reminder support model, the $25 visit and phone-use stipends, the sampling configuration, the first-month coverage figures, the accelerometer availability mean and range, both survey completion statements, the direction of the OS differences, the "over 90% for over 6 weeks" statement, the demographics, and the funding statements were read from the three published papers on 2026-09-03.

Reported. The per-OS participant counts and the coverage regression tables are in supplements not included in the PDFs.

Unclear. The survey frequency, given as twice weekly in one paper and three times weekly in the other two.

Not assessed here. The relapse-prediction result (anomaly rate 71% higher in the two weeks before relapse), the sleep-estimate agreement with the PSQI, and the metadata-to-symptom associations are the papers' own subjects.

Conflict note. All three papers declare no competing interests. They are written by the platform's developers about the platform's first clinical pilot. A 2019 review with two of the same authors discloses Otsuka and Mindstrong funding that the 2017 and 2018 papers do not mention. The figures here are unflattering to the platform, which is the main reason they are treated as Verified rather than discounted.

## Key Links

- Anchor paper (OA, CC BY): https://doi.org/10.1038/s41746-018-0022-8
- Relapse paper: https://doi.org/10.1038/s41386-018-0030-z
- Sleep paper (OA, CC BY): https://doi.org/10.1038/s41537-017-0038-0
- Protocol: https://doi.org/10.2196/mental.5165
- Local PDFs (already held by Module 2; not duplicated): `../../module-02-digital-phenotyping/literature/onnela-lab/2018-torous-npjdigitalmedicine-characterizing-clinical-relevance-digital-phenotyping-data.pdf`, `../../module-02-digital-phenotyping/literature/onnela-lab/2018-barnett-neuropsychopharmacologyo-relapse-prediction-schizophrenia-through-digital-phenotyping.pdf`, `../../module-02-digital-phenotyping/literature/onnela-lab/2017-staples-npjschizophrenia-comparison-passive-active-estimates-sleep-cohort.pdf`

## Related profiles

- Platform: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- The supported contrast on the same platform: [`beiwe-transdiagnostic-outpatient-completeness.md`](beiwe-transdiagnostic-outpatient-completeness.md)
- Other schizophrenia deployments: [`dp-schizophrenia-tolerability.md`](dp-schizophrenia-tolerability.md), [`sleepsight-schizophrenia-rest-activity.md`](sleepsight-schizophrenia-rest-activity.md), [`mindlamp-relapse-3site.md`](mindlamp-relapse-3site.md)
- Survey non-completion as signal: [`beiwe-inpatient-suicide-pilot.md`](beiwe-inpatient-suicide-pilot.md)
- OS effects by stream: [`beiwe-type-2-diabetes-feasibility.md`](beiwe-type-2-diabetes-feasibility.md), [`beiwe-missing-data-sociodemographic.md`](beiwe-missing-data-sociodemographic.md)
- Wi-Fi-gated upload: [`aware-binge-drinking-jitai-sensor-loss.md`](aware-binge-drinking-jitai-sensor-loss.md)

## Sources

1. Torous J, Staples P, Barnett I, Sandoval LR, Keshavan M, Onnela JP. *npj Digit Med* 2018;1:15. DOI 10.1038/s41746-018-0022-8. Full text read from the published PDF, 2026-09-03. Establishes the coverage figures, survey adherence with definition, OS differences, the pre-relapse survey cessation and the support model.
2. Barnett I, Torous J, Staples P, Sandoval L, Keshavan M, Onnela JP. *Neuropsychopharmacology* 2018;43:1660-1666. DOI 10.1038/s41386-018-0030-z. Full text read from the published PDF, 2026-09-03. Establishes the funnel, person-days, the Wi-Fi loss, the two uninstalls and the acceptability statement.
3. Staples P, Torous J, Barnett I, Carlson K, Sandoval L, Keshavan M, Onnela JP. *npj Schizophr* 2017;3:37. DOI 10.1038/s41537-017-0038-0. Full text read from the published PDF, 2026-09-03. Establishes the demographics, the accelerometer availability range, the EMA completion statement, the six-week usage statement and the compensation model.
