# Althobiani et al. 2023 - RADAR-base with Garmin vivoactive 4, home spirometry and pulse oximetry in COPD, ILD and post-COVID-19 patients, N=60, 6 months

## Quick Facts

| Field | Details |
|---|---|
| Citation | Althobiani MA, Ranjan Y, Jacob J, Orini M, Dobson RJB, Porter JC, Hurst JR, Folarin AA. "Evaluating a Remote Monitoring Program for Respiratory Diseases: Prospective Observational Study." *JMIR Formative Research* 2023;7:e51507. DOI [10.2196/51507](https://doi.org/10.2196/51507). PMID 37999935 / PMC10709787. Epub 2023-11-24. |
| Study design | Three-arm prospective observational cohort feasibility study (the RALD study, Remote Assessment of Lung Disease and Impact on Physical and Mental Health). ISRCTN 16275601. Feasibility measured as adherence, engagement, retention, acceptability and data integrity. |
| Sample size (enrolled / analyzed) | 162 assessed for eligibility. 60 recruited (20 COPD, 20 ILD, 20 post-COVID-19). 55 (92%) retained at 6 months. Acceptability surveys returned by 57. |
| Population | Patients from the Royal Free Hospital and University College Hospital, London, UK. Median age 64. 42% (25/60) women. 47% (28/60) reported a disability. COPD patients needed at least 2 exacerbations in the past year. |
| Duration | 180 days per participant. Recruitment given as August 2021 to January 2022 (Methods) and screening as July 2021 to November 2022 (Results). |
| Devices/platforms used | [RADAR-base](../../module-02-digital-phenotyping/profiles/radar-base.md) active questionnaire app (surveys, audio tasks, notifications). [Garmin vivoactive 4](../../module-01-wearables/profiles/garmin.md) for passive heart rate, SpO2, respiration, sleep, stress and activity. A finger pulse oximeter read manually into the app. NuvoAir AirNext Bluetooth spirometer (COPD and ILD only). REDCap for consent and periodic surveys. |
| Funding/COI | NIHR Maudsley and UCLH Biomedical Research Centres, Health Data Research UK, the IMI2 BigData@Heart consortium (grant 116074), UKRI, NIHR ARC South London, UCL Institute of Health Informatics, and King Abdul Aziz University via the Saudi Arabian Cultural Bureau. Wellcome Trust funded one author for unrelated research. No vendor funding or vendor-employed author is declared. Participant compensation is not reported. |
| Last verified | 2026-10-31 |

## Summary

This is the module's only respiratory deployment of RADAR-base, and it pairs the platform with a Garmin watch rather than the Fitbit used in the RADAR-CNS studies. It is included for an explicit burden gradient across four collection modes in the same patients over six months.

The passive watch stream held up best. Mean wear was 18.66 hours a day (SD 4.69), against an expected maximum of about 23 hours once daily charging is allowed for. Individual daily means ranged from 7.72 to 23.58 hours. Weekly and monthly wear fell to 72.6% and 64.4% of available time.

Spirometry was the most burdensome stream. Of 7200 requested sessions, 4248 (59%) were performed. Of those performed, 90.3% (3836/4248) were of acceptable ATS quality.

Retention was 92% by enrolment status. It was lower by data contribution. 54% (31/57) contributed data for the full 180 days and 81% (46/57) for more than 150 days. The paper also piloted "protocol holidays," a structured break offered to participants who wanted to drop out.

## Instrumentation and Deployment Model

Provisioned. After e-consent and baseline REDCap questionnaires, participants were mailed a kit containing the spirometer, the Garmin watch, the pulse oximeter and "sometimes a smartphone." The number given a study phone is not reported. Phone operating system is not reported.

Every participant attended an enrolment session on installing and using the RADAR questionnaire app, the spirometer and the watch. A follow-up call came the next day. The first spirometry session was supervised by video call. Later sessions were unsupervised.

The study team checked data daily. Missing data triggered contact or a reminder through the RADAR app. Daily notifications from the RADAR app also prompted spirometry.

The Garmin sampled SpO2 and respiratory rate every minute, heart rate every 15 seconds, stress and body battery every 3 minutes, and steps every 15 minutes. Continuous heart rate and SpO2 had to be switched on manually on each watch. Garmin data with negative values, which mark a metric the watch could not calculate, were treated as missing.

Watch wear was inferred from the presence of heart rate data. The authors note this undercounts wear when a loose strap stops the watch computing heart rate.

## Recruitment and Retention

The research team screened clinic lists and explained the study a week before recruitment. Interested patients received the information sheet and consent form by email through REDCap.

| Stage | n |
|---|---|
| Assessed for eligibility | 162 |
| Recruited | 60 (20 per cohort) |
| Dropped out | 5 |
| Retained at 6 months | 55 (92%) |
| Contributed data for the full 180 days | 31 of 57 (54%) |
| Contributed data for more than 150 days | 46 of 57 (81%) |

The reasons for exclusion between the 162 assessed and the 60 recruited are not given in the text. The flowchart figure was not read. The denominator of 57 for the data-based retention figures is not explained.

Dropout reasons were reported for all five. One died in the first week. One felt unwell. Two found the protocol too time-consuming. One left over privacy concerns.

Protocol holidays let a participant pause and name a return date. The number of participants who took one is not reported. The median retention at 0.5 survival probability was 179.9 days without a holiday and 165.1 days with one. The authors also modelled each holiday-taker as if they had dropped out at the start of the first holiday. Retention was better when post-holiday data were counted.

## Data Completeness and Technical Issues

Adherence fell as task burden and frequency rose. The authors grouped streams into four burden tiers.

| Stream | Adherence reported |
|---|---|
| Garmin passive data (lowest burden) | 70% to 90% for most data types. SpO2 lower because of daytime motion artefact. |
| PHQ-8, every 14 days (low burden) | Mean 84.7% COPD, 85.4% post-COVID, 92.3% ILD |
| Daily pulse oximeter entry (high burden) | Mean 67.9% COPD, 64.1% post-COVID, 65.5% ILD |
| Audio tasks, every 21 days (high burden) | Mean 64.8% to 81.2% across task and cohort |
| Spirometry (highest burden) | 59% of 7200 requested sessions performed. Weekly adherence 94% ILD and 84% COPD. |

The post-COVID-19 cohort had the lowest wearable adherence and the lowest overall retention. The authors describe it as the most hands-off cohort, with less study-team contact than the COPD and ILD cohorts.

Missing data reasons came from participant contact and were grouped in Table 4 by frequency. Personal circumstances came first, then device and technical problems, then health and access limits.

The named technical failure modes are specific.

- Recurrent background synchronisation failures with the Garmin watches were the main cause of missing passive data. Garmin's support fixes were not one-size-fits-all and needed substantial study-team troubleshooting.
- Continuous heart rate and SpO2 needed manual activation, which caused errors.
- App freezing, automatic log-out and test errors forced repeated logins.
- Phone changes broke compatibility.
- Participants forgot to charge, lost chargers, had the wrong plug type, or deleted the apps.
- Skin irritation from the watch and device-related sleep problems were reported.

The watch's red and green sensor lights disrupted sleep for 66% (38/57) of acceptability respondents. In the same survey 82% (47/57) said they would wear it overnight.

No iOS versus Android breakdown is given.

## Feasibility Findings

The authors conclude that multimodal remote monitoring was feasible and acceptable in all three respiratory groups. Passive wearable collection gave higher adherence, engagement and retention than any active method. Adherence was inversely related to the effort a task required.

They credit the high retention to patient-representative involvement, simple remote recruitment, team communication, real-time monitoring of data streams and regular calls. They recommend training sessions, readily available technical support, and flexible protocols such as protocol holidays. They suggest a wireless oximeter that uploads automatically would raise oximetry adherence.

Acceptability was high. 74% (42/57) found the RADAR app efficient. 77% (44/57) said they would likely use it for future monitoring. 90% (36/40) found daily home spirometry highly acceptable.

## Relevance to Future Study Design

A Garmin vivoactive 4 delivered about 18.7 hours of wear a day for six months in older respiratory patients. The price was a sync-troubleshooting load the authors describe as substantial and unsolved by vendor guidance.

Budget for manual configuration of each watch. Continuous heart rate and SpO2 are off by default and switching them on was itself a source of error.

Ask whether overnight wear matters. Two thirds of respondents reported sleep disruption from the sensor lights, which matters for any study using the watch for sleep or nocturnal SpO2.

Expect a manually transcribed daily reading to sit near two thirds completion. The pulse oximeter task required reading a device and typing the value into the app. It ran about 20 points below the fortnightly PHQ-8.

Report retention both ways. Here 92% stayed enrolled but only 54% contributed data for the full 180 days.

Protocol holidays are a cheap retention tool with an unmeasured denominator. Future studies should report how many participants took one.

## Evidence Confidence

Verified. The recruitment, dropout and retention counts, the wear-time figures, the spirometry session counts and quality grades, the per-questionnaire completion means, the protocol-holiday retention medians, the acceptability percentages, the named technical failure modes and the funding statement were read from the Europe PMC full-text XML (PMC10709787, CC BY 4.0) on 2026-10-31.

Reported. The Garmin adherence range of 70% to 90% is stated in the text as a summary of a figure that was not read. The burden-tier survival curves were read from the text's description only.

Unclear. The recruitment window is given two ways (August 2021 to January 2022, and July 2021 to November 2022). The denominator of 57 for data-based retention is not explained. Whether participants were paid is not stated.

Not assessed here. Whether Garmin SpO2 or respiratory rate agreed with the reference pulse oximeter belongs with Module 1's [Garmin profile](../../module-01-wearables/profiles/garmin.md).

## Key Links

- Paper (OA, CC BY 4.0): https://doi.org/10.2196/51507
- Europe PMC: https://europepmc.org/article/PMC/PMC10709787
- Protocol: RR2-10.2196/28873
- Local PDF: none held

## Related profiles

- Platform: [RADAR-base](../../module-02-digital-phenotyping/profiles/radar-base.md)
- Device: [Garmin](../../module-01-wearables/profiles/garmin.md)
- Other RADAR-base deployments in this module: [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md), [`radar-base-treatment-engagement.md`](radar-base-treatment-engagement.md), [`radar-ad-feasibility-usability.md`](radar-ad-feasibility-usability.md)
- Other Garmin deployments: [`garmin-low-income-physical-activity.md`](garmin-low-income-physical-activity.md), [`garmin-nursing-home-dementia-one-year.md`](garmin-nursing-home-dementia-one-year.md)
- Passive outlasting active: [`oura-tempredict-healthcare-worker-adherence.md`](oura-tempredict-healthcare-worker-adherence.md)

## Sources

1. Althobiani MA, Ranjan Y, Jacob J, Orini M, Dobson RJB, Porter JC, Hurst JR, Folarin AA. *JMIR Form Res* 2023;7:e51507. DOI 10.2196/51507. Full text, Tables 1 to 4 and figure captions read from the Europe PMC full-text XML (PMC10709787), 2026-10-31. The first author is taken from the XML author records, not a PDF byline. Establishes every figure in this profile.
