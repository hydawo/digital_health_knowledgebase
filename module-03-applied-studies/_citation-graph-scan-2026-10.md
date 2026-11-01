# Module 3 - Citation-graph discovery pass 2 (OpenAlex), 2026-10-31

Second OpenAlex citation-graph pass, the "matching pass on other platforms" that
[`_citation-graph-scan-2026-09.md`](_citation-graph-scan-2026-09.md) said must come before its
Beiwe-heavy backlog is built out. It also refreshes Beiwe for works published since 2026-08-01.

## Anchors

| Platform | Anchor paper(s) | OpenAlex ID | Window | Citing works |
|---|---|---|---|---|
| AWARE | Ferreira 2015; Nishiyama 2020 (AWARE on iOS, new this pass) | W2078074240, W3041110519 | 2018 on | 358 |
| CARP | Bardram 2020 (2 records); CARP demonstration 2025 (new) | W4287754165, W3036631247, W7117478350 | 2018 on | 14 |
| m-Path | Mestdagh 2023; m-Path Sense 2023 (new) | W4387742524, W4318212610 | 2018 on | 251 |
| mindLAMP | Torous 2022 (JMIR) | W4206048551 | 2018 on | 91 |
| RADAR-base | Ranjan 2018; RADAR-MDD protocol 2019 (new) | W2904206377, W2912143189 | 2018 on | 321 |
| Polar | Schaffarczyk 2022, Polar H10 HRV validity (new platform) | W4293715556 | 2018 on | 348 |
| Beiwe | the three anchors of pass 1 | W2347128633, W4200567269, W2392412101 | 2026-08-01 on | 84 |

Avicenna, MetricWire and LifeData still have no anchor paper, so this method cannot reach them.

## Filter

1. Drop any DOI already in the ledger (`dois_seen`, `rejected`) or cited in an existing profile.
2. Keep articles and preprints only. Drop titles or abstracts that say review, meta-analysis or protocol.
3. Require a digital-health context term and at least two deployment-reality signals in the title or
   abstract (feasibility, acceptability, adherence, compliance, retention, attrition, missingness,
   recruitment, wear time, technical issues, engagement).

**119 works passed.** A title read then dropped 68: preprint duplicates of published papers, three
already profiled under their published DOI (RADAR-MDD recruitment, RADAR-MDD long-term engagement,
m-Path dementia ESM), perspectives, qualitative clinician studies, guides, validation studies and
platforms not profiled in Modules 1 or 2 (JTrack, SensorW, SMAAT). **51 go to full-text screening.**

Every platform label below is what the citation suggests, not what was deployed. Pass 1 measured
3 wrong attributions in 12.

## Candidates sent to full-text screening

| Batch | Year | OA | Cited platform | DOI | Title |
|---|---|---|---|---|---|
| A | 2026 | Y | m-Path | `10.21203/rs.3.rs-10880727/v1` | Feasibility and Acceptability of using Ecological Momentary Assessment Among Youth with recent Suicidal attemp |
| A | 2025 | Y | m-Path | `10.1016/j.invent.2025.100804` | Feasibility, acceptability and preliminary clinical outcomes of a brief coping-focused intervention for delusi |
| A | 2025 | Y | m-Path | `10.2196/79296` | Smartphone-Based Mindfulness and Mentalization Ecological Momentary Interventions for Common Mental Health Pro |
| A | 2025 | Y | m-Path | `10.2196/74103` | A Social Support Just-in-Time Adaptive Intervention for Individuals With Depressive Symptoms: Feasibility Stud |
| A | 2025 | Y | m-Path | `10.3389/fpsyt.2025.1470554` | Reasons for non-participation and dropout in a longitudinal study of an app-based support service among adult  |
| A | 2023 | Y | m-Path | `10.2196/47179` | Remote Symptom Monitoring With Ecological Momentary Computerized Adaptive Testing: Pilot Cohort Study of a Pla |
| A | 2024 | Y | m-Path | `10.1016/j.chb.2024.108360` | Real-time incentivizing survey completion with game-based rewards in experience sampling research may increase |
| A | 2025 | Y | m-Path | `10.1080/1612197x.2025.2563323` | Feasibility of ecological momentary assessment during cognitive behavioural therapy in athletes: a single-case |
| A | 2024 | Y | m-Path | `10.2196/49857` | An Ecological Mobile Momentary Intervention to Support Dynamic Goal Pursuit: Feasibility and Acceptability Stu |
| A | 2025 | Y | m-Path | `10.2196/69556` | Just-in-Time Delivery of Cognitive Behavioral Therapy-Based Exercises: Single-Case Experimental Design With Ra |
| A | 2025 | Y | m-Path | `10.2196/77036` | Leveraging No-Code Digital Platforms for Designing an Integrated Smartphone-Based Ecological Momentary Interve |
| A | 2025 | Y | m-Path | `10.2196/79360` | Mobile-Based Ecological Momentary Intervention for Improving Physical Activity in Adults Without Regular Physi |
| A | 2026 | Y | m-Path | `10.1016/j.jad.2026.121783` | Validating an aphasia-accessible ecological momentary assessment for daily depressive affect: A preliminary in |
| A | 2024 | Y | m-Path | `10.1001/jamanetworkopen.2024.40510` | The Short-Term Course of Nonsuicidal Self-Injury Among Individuals Seeking Psychiatric Treatment |
| B | 2023 | Y | RADAR-base | `10.2196/51507` | Evaluating a Remote Monitoring Program for Respiratory Diseases: Prospective Observational Study |
| B | 2023 | Y | RADAR-base | `10.2196/44126` | Barriers to and Facilitators of Using Remote Measurement Technology in the Long-Term Monitoring of Individuals |
| B | 2023 | Y | RADAR-base | `10.2196/45233` | Challenges in Using mHealth Data From Smartphones and Wearable Devices to Predict Depression Symptom Severity: |
| B | 2024 | Y | RADAR-base | `10.2196/59623` | Development and Initial Evaluation of a Digital Phenotype Collection System for Adolescents: Proof-of-Concept  |
| B | 2025 | Y | RADAR-base | `10.1016/j.sleep.2025.106830` | Application of down-phase targeted auditory stimulation during sleep in a home setting: A feasibility study ac |
| B | 2026 | Y | RADAR-base | `10.1038/s44482-026-00029-3` | The Digital Mental Health Study assessed feasibility of large-scale digital sensing for depression and anxiety |
| B | 2022 | Y | RADAR-base | `10.1016/j.jad.2022.05.005` | Predictors of engagement with remote sensing technologies for symptom measurement in Major Depressive Disorder |
| B | 2023 | Y | RADAR-base | `10.2196/44214` | Engagement With a Remote Symptom-Tracking Platform Among Participants With Major Depressive Disorder: Randomiz |
| B | 2025 | Y | RADAR-base | `10.1007/s41347-025-00530-1` | Acceptability of Remote Monitoring Technologies for Early Warning of Major Depression |
| B | 2026 | Y | RADAR-base | `10.21203/rs.3.rs-9381221/v1` | Feasibility and exploration of remote multimodal sleep measurement in autistic and nonautistic smartphone user |
| C | 2024 | Y | mindLAMP | `10.2196/59974` | Mobility-Based Smartphone Digital Phenotypes for Unobtrusively Capturing Everyday Cognition, Mood, and Communi |
| C | 2026 | Y | mindLAMP | `10.1177/20552076261458952` | Active and passive data collection using mHealth to monitor mental wellness: Pilot findings from the Texas res |
| C | 2026 | Y | Beiwe | `10.1080/29973368.2026.2723021` | Examining the Feasibility, Acceptability, and Preliminary Outcomes of Integrating a Recovery App to Recovery H |
| C | 2024 | Y | mindLAMP | `10.2196/65222` | Testing the Feasibility, Acceptability, and Potential Efficacy of an Innovative Digital Mental Health Care Del |
| C | 2026 | Y | Beiwe | `10.7759/cureus.117257` | Longitudinal Mood Monitoring and Classification of Self-Reported Mental Health Status Using Feels.ai: Feasibil |
| C | 2024 | Y | mindLAMP | `10.2196/62725` | Assessing Digital Phenotyping for App Recommendations and Sustained Engagement: Cohort Study |
| C | 2025 | Y | mindLAMP | `10.1016/j.inpsyc.2025.100123` | Barriers and facilitators to usability of a smartphone-based digital mental health tool in older adults: Insig |
| C | 2023 | Y | mindLAMP | `10.2196/46491` | Implementing Technologies to Enhance Coordinated Specialty Care Framework: Implementation Outcomes From a Deve |
| C | 2024 | Y | mindLAMP | `10.37349/edht.2024.00007` | Functionality and feasibility of cognitive function training via mobile health application among youth at risk |
| C | 2026 | Y | Beiwe | `10.2196/89485` | Sighing Dynamics as a Candidate Digital Biomarker for Anxiety in Daily Life Using Wearable Respiratory Monitor |
| C | 2026 | Y | Beiwe | `10.64898/2026.09.18.26363439` | Smartphone Passive Digital Phenotyping in Frontotemporal Lobar Degeneration |
| D | 2022 | Y | AWARE | `10.2196/40765` | Recruitment and Retention in Remote Research: Learnings From a Large, Decentralized Real-world Study |
| D | 2025 | Y | AWARE | `10.1145/3711043` | Participant Engagement and Data Quality: Lessons Learned from a Mental Wellness Crowdsensing Study |
| D | 2026 | Y | Polar | `10.1186/s13102-025-01507-6` | Co-development and implementation of a group-based arm-crank exercise programme in the community for individua |
| D | 2023 | Y | AWARE | `10.1016/j.sleh.2023.01.014` | Feasibility and acceptability of mobile methods to assess home and neighborhood environments related to adoles |
| D | 2025 | Y | AWARE | `10.2196/82465` | Multimodal Sleep Measurement and Alignment Analysis in Outpatients With Major Depressive Episode: Observationa |
| D | 2023 | Y | CARP | `10.1145/3586579` | DiaFocus: A Personal Health Technology for Adaptive Assessment in Long-Term Management of Type 2 Diabetes |
| D | 2024 | Y | Polar | `10.1016/j.jss.2024.07.009` | Feasibility of Wearable Sensors to Assess Cognitive Load During Clinical Performance: Lessons Learned and Blue |
| D | 2024 | Y | Polar | `10.2196/53645` | Effects of Missing Data on Heart Rate Variability Measured From A Smartwatch: Exploratory Observational Study |
| D | 2025 | Y | Polar | `10.1111/inm.13499` | Examining the Feasibility and Acceptability of Identifying Signs of Social Anxiety, in University Students Age |
| D | 2026 | Y | m-Path | `10.21203/rs.3.rs-10394948/v1` | Assessing The Feasibility and Acceptability of Ecological Momentary Assessment in Measuring the Everyday Exper |
| D | 2026 | Y | m-Path | `10.3758/s13428-026-03164-0` | The effect of incentive type on data quality and quantity in an experience sampling study in a student populat |
| D | 2026 | Y | m-Path | `10.1177/02692163261416264` | Uncovering fluctuations in daily symptoms and well-being among people with advanced cancer: An experience samp |
| D | 2024 | Y | m-Path | `10.1016/j.jcbs.2024.100839` | Feasibility, acceptability and outcomes of a contextual schema therapy-based mobile program for depressive sym |
| D | 2024 | Y | m-Path | `10.1016/j.cdnut.2024.104479` | Development and User Experience Evaluation of an Experience Sampling-Based Dietary Assessment Method |
| D | 2025 | Y | m-Path | `10.3758/s13428-025-02777-1` | Fabla: A voice-based ecological assessment method for securely collecting spoken responses to researcher quest |
| D | 2024 | Y | m-Path | `10.2196/60461` | Acceptability, User Satisfaction, and Feasibility of an App-Based Support Service During the COVID-19 Pandemic |

## Screening outcome

Full-text screening of all 51 is done (reports `_screening-reports/2026-10-31-citation-graph-A.md` to `-D.md`).

- **23 new profiles from 24 papers** (Hackett 2024 and Calvert 2026 share one profile). Module 3 now has 98 profiles.
- 27 rejected, 4 of them `unobtainable` behind bot checks (10.1145/3711043, 10.1145/3586579 DiaFocus, 10.1016/j.jss.2024.07.009, 10.1080/29973368.2026.2723021).
- The cited platform was wrong for many candidates. None of the 4 Beiwe-tagged papers deployed Beiwe. RADAR-base was wrong or overstated for 4 of 10.
- CARP is still at one profile. The DiaFocus pilot (Lind 2025) is already covered by Q112, whose full text never names CARP.

Merged 2026-11-01: `feasibility-matrix.md` Table 11, `sources.md` S80 to S103, README counts, Q103, Q112 and Q118 updates, manual sweep #19.
