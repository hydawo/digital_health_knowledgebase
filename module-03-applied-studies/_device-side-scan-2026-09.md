# Module 3 device-side discovery scan (date-sorted), 2026-09-03

**Purpose.** Every earlier discovery pass for this module searched from the platform side, so the Module 1 wearables with the thinnest coverage (Polar with no profile, Garmin with one, ActiGraph with two, Withings with one, Empatica with two) were never searched on their own terms. This pass ran one date-sorted Europe PMC query block per device, 2019 to 2026, and screened the results from abstracts only.

**Status of every attribution in this file. Reported, not Verified.** No full text was read. The device named in the "Device(s) per abstract" column is what the abstract says was worn, and the deployment signals are what the abstract mentions. Both must be confirmed from the Methods before a profile is written. Abstract-level screening in this project has a measured platform-misattribution rate of roughly 3 in 12, and this pass gives no reason to expect better.

**No PDFs were downloaded and no other file was edited.** This file is the whole output.

---

## Method

### Query construction

Two rounds were run against `https://www.ebi.ac.uk/europepmc/webservices/rest/search` with `format=json`, `pageSize=100`, `resultType=core`, `sort=P_PDATE_D desc`, cursor paging to a maximum of 300 records per device, `(SRC:MED OR SRC:PPR)`, `FIRST_PDATE:[2019-01-01 TO 2026-12-31]`, and `NOT (PUB_TYPE:"Review" OR PUB_TYPE:"Systematic Review" OR PUB_TYPE:"Meta-Analysis")`.

Every query ANDed three blocks. A device block, a deployment block, and a digital-health context block. The context block was required because Polar, Oura, Samsung and Galaxy are ordinary words or surnames, and this project has already shown that Europe PMC does not honour phrase quoting reliably.

Deployment block (round 1, unfielded)

```
(retention OR adherence OR "wear time" OR feasibility OR "data completeness" OR attrition OR "remote monitoring" OR missingness OR dropout)
```

Deployment block (round 2, restricted to titles so that the date-sorted window reached back to 2019 for the high-volume devices)

```
(TITLE:feasibility OR TITLE:feasible OR TITLE:adherence OR TITLE:"wear time" OR TITLE:retention OR TITLE:compliance OR TITLE:acceptability OR TITLE:missing OR TITLE:missingness OR TITLE:attrition OR TITLE:engagement OR TITLE:"real-world" OR TITLE:"remote monitoring" OR TITLE:"lessons learned")
```

Context block (both rounds)

```
(wearable OR smartwatch OR ring OR accelerometer OR "remote monitoring" OR "digital phenotyping")
```

Device blocks

| Device | Device block |
|---|---|
| Oura | `("Oura ring" OR "Oura rings" OR "Oura Health")` |
| WHOOP | `("WHOOP strap" OR "WHOOP band" OR "WHOOP wearable" OR "WHOOP device" OR "WHOOP 4.0" OR "WHOOP inc")` |
| Garmin | `(Garmin)` |
| Polar | `("Polar Vantage" OR "Polar H10" OR "Polar Verity" OR "Polar Ignite" OR "Polar Electro" OR "Polar OH1" OR "Polar M430" OR "Polar A370" OR "Polar A360" OR "Polar Grit" OR "Polar Pacer" OR "Polar Unite" OR "Polar watch" OR "Polar smartwatch" OR "Polar sports watch" OR "Polar M600" OR "Polar V800" OR "Polar Loop" OR "Polar Active" OR "Polar Flow")` |
| Samsung | `("Galaxy Watch" OR "Samsung Gear" OR "Samsung Galaxy" OR "Samsung Health" OR "Galaxy Fit" OR "Samsung smartwatch" OR "Samsung wearable")` |
| Withings | `(Withings)` |
| ActiGraph | `(ActiGraph OR "Actigraph GT" OR "wGT3X" OR "GT9X")` |
| Axivity / GENEActiv | `(Axivity OR GENEActiv OR "AX3 accelerometer" OR "AX6 accelerometer")` |
| Empatica | `(Empatica OR EmbracePlus OR "E4 wristband" OR "E4 wearable")` |
| Movesense | `(Movesense)` |

### Hit counts

| Device | Round 1 hits | Round 1 fetched (oldest date reached) | Round 2 hits | Round 2 fetched (oldest date reached) |
|---|---|---|---|---|
| Oura | 326 | 300 (2020-05) | 46 | 46 (2020-05) |
| WHOOP | 74 | 74 (2020-01) | 9 | 9 (2020-01) |
| Garmin | 1,083 | 300 (2024-08) | 167 | 167 (2019-01) |
| Polar | 893 | 300 (2023-04) | 105 | 105 (2019-01) |
| Samsung | 861 | 300 (2023-07) | 116 | 116 (2019-01) |
| Withings | 374 | 300 (2021-01) | 70 | 70 (2019-01) |
| ActiGraph | 5,468 | 300 (2023-02) | 504 | 300 (2020-09) |
| Axivity / GENEActiv | 1,236 | 300 (2024-05) | 160 | 160 (2019-01) |
| Empatica | 512 | 300 (2021-04) | 68 | 68 (2019-02) |
| Movesense | 50 | 50 (2019-03) | 6 | 6 (2021-10) |

The round 1 window for Garmin, Polar, Samsung, ActiGraph and Axivity did not reach 2019. That is a coverage limit of this pass, partly closed by round 2, and the pre-2023 Garmin, Polar and Samsung literature outside round 2's title filter remains unsearched.

### Screening

Automatic first stage. A hit survived only if (a) the device was named in the title or abstract by the regexes above (a Polar hit needed "Polar" followed by a product word, so "polar" alone never counted), (b) the title did not contain protocol, review, validation, validity, accuracy, agreement, reliability or calibration, (c) Europe PMC's publication type was not Review or Meta-Analysis, and (d) at least one deployment signal (retention, adherence or compliance, wear time, feasibility, completeness or missingness, attrition or dropout, technical failure, recruitment) appeared in the abstract. 294 unique records survived round 1 and 107 further records survived round 2.

Manual second stage. Every survivor with two or more signals, and every one-signal survivor for a priority device, was read at abstract level and excluded if it was a laboratory or single-session study, a data-aggregation paper with no cohort, a device-comparison whose only outcome was agreement, a platform or interoperability paper, a qualitative-only interview study, or a study where the device measured an outcome and the abstract said nothing about how the device deployment went.

### Reconciliation

DOIs and PMCIDs were checked against `literature-index.json` (dois_seen, pmcids_seen, records, rejected), `_scan-queue.md`, `_onnela-module3-candidates.md`, `_recency-scan-2026-09.md`, `_citation-graph-scan-2026-09.md`, every Module 3 profile, the Module 1 and 2 library index JSONs and library markdown, and the filenames under `module-01-wearables/literature/` and `module-02-digital-phenotyping/literature/` by first author and year. 406 known identifiers in total.

---

## New candidates, ranked

Ranking weighs (1) the module's stated priority devices, Polar first, then Garmin, ActiGraph, Withings, Empatica, (2) deployment outside North America and Western Europe, (3) the number and specificity of deployment signals in the abstract, and (4) duration and scale. OA route. "PMC" means the Europe PMC `fullTextXML` and `?pdf=render` routes should work. "Author manuscript" means the PMC copy is the accepted manuscript and may lack tables. Preprints are open at the server named.

| # | Date | Device(s) per abstract | DOI | PMCID | OA and route | Title (first author, venue) | Deployment signals in abstract | Rationale |
|---|---|---|---|---|---|---|---|---|
| 1 | 2025-05-07 | Garmin vívosmart 4 | 10.2196/68645 | PMC12077851 | Yes, PMC | Feasibility of Long-Term Physical Activity Measurement With a Wearable Activity Tracker in Patients With Axial Spondyloarthritis. 1-Year Longitudinal Observational Study (Thomassen, JMIR Hum Factors) | eligibility, inclusion rate, days worn, minutes recorded as % of possible, missing data, sync reminders, tracker replacements, wear-pattern clustering | A full year of Garmin wear inside an RCT with technical and operational feasibility reported separately. Norway. The single strongest Garmin candidate found. |
| 2 | 2026-03-31 | Garmin smartwatches | 10.2196/81123 | PMC13037767 | Yes, PMC | Determining a Likely Mechanism of Missingness in Repeated Measures Sleep Data From Wearable Fitness Trackers. Longitudinal Analysis (Mobley, JMIR Mhealth Uhealth) | missingness patterns and mechanism, 300 women, 5 days, urban informal settlement | Kampala, Uganda. Missingness is the whole subject. Pairs with #3 from the same project. |
| 3 | 2024-10 | Garmin vívoactive 3 | 10.1177/20552076241288754 | PMC11489944 | Yes, PMC | Feasibility and acceptability of wearable devices and daily diaries to assess sleep and other health indicators among young women in the slums of Kampala, Uganda (Nielsen, Digit Health) | 60 women, 5 days, 93.2% median HR coverage, 87.5% of devices lasted 5 days on battery, discomfort, safety concerns | The pilot behind #2. Battery, comfort and personal-safety findings from a low-income setting the module has none of. |
| 4 | 2022-09-30 | Withings Pulse HR (plus Tucky thermometer patch) | 10.3389/fpubh.2022.972177 | PMC9561896 | Yes, PMC | Using wearable devices to generate real-world, individual-level data in rural, low-resource contexts in Burkina Faso, Africa. A case study (Huhn, Front Public Health) | 150 HDSS residents aged 6+, 3 weeks, acceptability questionnaire every 4 days, data completeness and plausibility | Burkina Faso. Withings is a priority device and the module has no African deployment at all. |
| 5 | 2025-04-08 | Garmin Vivosmart 4 with Labfront | 10.2196/69952 | PMC12015335 | Yes, PMC | Longitudinal and Combined Smartwatch and Ecological Momentary Assessment in Racially Diverse Older Adults. Feasibility, Adherence, and Acceptability Study (Holmqvist, JMIR Hum Factors) | 44 older adults, 4 weeks, 23 h/day wear target, daily sync of two apps, training time, wear time, EMA adherence | Smartwatch plus EMA in a racially diverse older cohort with MCI. Directly comparable with the module's Beiwe EMA figures. |
| 6 | 2026-08-02 | Oura Ring | 10.64898/2026.07.30.26359360 | none | Yes, medRxiv preprint | How Quickly Can You Know a Participant? A 3-Week Triage Point for Oura Ring Adherence in College Students (Loftness, medRxiv) | 584 students, two semesters (8 and 15 weeks), 442 continued, 408 analysable, wear-time trajectories, early-warning classifier | Largest Oura adherence cohort found and the only one that turns adherence into an operational triage rule. Preprint, so unrefereed. |
| 7 | 2024-01-28 | Polar H10 with Elite HRV app, plus Fitbit | 10.1177/27536351241227261 | PMC10826406 | Yes, PMC | HEART Rate Variability Biofeedback for LOng COVID Dysautonomia (HEARTLOC). Results of a Feasibility Study (Corrado, Adv Rehabil Sci Pract) | 13 completers, 4 weeks twice daily, independent technology use, data completeness, adherence | The best Polar candidate found. Small, but it reports completeness and adherence for a home-based Polar H10 protocol. UK. |
| 8 | 2026-02-09 | Polar A370 | 10.1186/s13018-025-06591-5 | PMC12983556 | Yes, PMC | Correlation between smartwatch-measured daily walking steps and patient-reported functional outcomes following total knee arthroplasty. A prospective cohort study (Achawakulthep, J Orthop Surg Res) | 96 enrolled, 86 completed 6 months, provisioned watch | Thailand. Six months of provisioned Polar wear in surgical patients. The abstract gives retention only, so wear-time detail must come from full text. |
| 9 | 2026-03-12 | Polar H10 with a dedicated app | 10.3389/fcvm.2026.1798233 | PMC13017397 | Yes, PMC | Impact of a combined care ambulatory and home-based aerobic exercise program using wearables on anxiety and depression in patients with metabolic syndrome (Zupkauskiene, Front Cardiovasc Med) | 132 adults, 6-month home phase, randomised | Lithuania. Six months of Polar H10 use at home. Adherence is in the abstract only as a word, so this may prove thin. |
| 10 | 2019-04-03 | Polar Active watch | 10.1186/s12889-019-6697-1 | PMC6446303 | Yes, PMC | SKIP (Supporting Kids with diabetes In Physical activity). Feasibility of a randomised controlled trial of a digital intervention for 9-12 year olds with type 1 diabetes mellitus (Knox, BMC Public Health) | 49 children, 6 months, feasibility RCT, end-of-study questionnaire, interviews | Paediatric Polar deployment with feasibility as the primary aim. UK. |
| 11 | 2021-03-22 | Polar A360 | 10.1007/s11764-021-01030-w | none | No, publisher paywall | Adherence to a lower versus higher intensity physical activity intervention in the Breast Cancer and Physical Activity Level (BC-PAL) Trial (McNeil, J Cancer Surviv) | 30 tracker users, 12 weeks, weekly tracker-measured adherence, baseline predictors of adherence | Polar tracker used as the adherence instrument itself. Paywalled, so profile only if a copy can be obtained legitimately. |
| 12 | 2022-02 | Polar H10 with Elite HRV, daily 5-min morning readings | 10.1097/htr.0000000000000764 | PMC9203863 | Author manuscript | Neurobehavioral Symptoms and Heart Rate Variability. Feasibility of Remote Collection Using Mobile Health Technology (Nabasny, J Head Trauma Rehabil) | 64 participants, 2-week EMA, remote HRV collection feasibility | Remote daily Polar H10 protocol in a TBI cohort. Feasibility is in the title. |
| 13 | 2026-04-09 | Samsung Galaxy Watch5 with DEDICAT app | 10.31234/osf.io/p6n5b_v1 | none | Yes, PsyArXiv preprint | Piloting the Depression Digital Forecasting Tool (DEDICAT). Feasibility and Acceptability in an At-Risk Population (Maerevoet, PsyArXiv) | 21 adults, 3 weeks, EMA adherence 57.6%, passive data availability, missingness patterns, recruitment challenges | Samsung plus smartphone passive sensing with missingness modelled. Belgium. Preprint. |
| 14 | 2026-08-10 | Samsung Galaxy Watch 6 with custom app | 10.12701/jyms.2026.43.53 | none | Journal is open access at publisher, no PMC deposit yet | Culturally adapted wearable mobile health intervention for physical activity and cognitive function in middle-aged Koreans. A pilot feasibility study (Shin, J Yeungnam Med Sci) | 304 enrolled, 302 completed 12 weeks, usability | Seoul. Large single-arm Samsung deployment with near-total completion. Wear-time detail not in abstract. |
| 15 | 2025-11-20 | ActiGraph waist, Fitbit wrist, activPAL thigh worn simultaneously | 10.2196/76167 | PMC12679073 | Yes, PMC | Three Body-Worn Accelerometers in the French NutriNet-Santé Cohort. Feasibility and Acceptability Study (Soumaré, JMIR Form Res) | 126 participants, 7 days, three devices at once, 22-item acceptance questionnaire per device | Multi-device in one cohort, which is a stated module priority. France. |
| 16 | 2023-09-12 | ActiGraph GT3X+ wrist | 10.1249/mss.0000000000003301 | PMC10872893 | Author manuscript | Does Wrist-Worn Accelerometer Wear Compliance Wane over a Free-Living Assessment Period? An NHANES Analysis (Lamunion, Med Sci Sports Exerc) | N = 13,649, 7 days, wear fatigue of 18 min/day, by age group, time of day and weekend | The only population-scale wear-fatigue estimate found for any device. Secondary analysis of a national survey deployment. |
| 17 | 2026-04-25 | ActiGraph CentrePoint Insight | 10.1186/s44167-026-00101-6 | PMC13245044 | Yes, PMC | Feasibility and acceptability of longitudinal measurement of 24-hour movement profiles across pregnancy using research-grade devices paired with sleep diaries (Ryan, J Act Sedentary Sleep Behav) | 10 participants, 10 to 35 weeks gestation, continuous wear, valid-day definition, diary completion, comfort | Continuous ActiGraph wear for around 25 weeks with an explicit adherence definition. Small. |
| 18 | 2023-01-19 | ActiGraph wGT3X-BT waist, 24 h wear | 10.1186/s13104-022-06266-y | PMC9849105 | Yes, PMC | Acceptability and use of waist-worn physical activity monitors in Jamaican adolescents. Lessons from the field (Smith, BMC Res Notes) | 79 adolescents, 7 days, validity by school and demographic, written participant feedback | Jamaica. "Lessons from the field" framing. |
| 19 | 2026-06-29 | ActiGraph wGT3x-BT | 10.1186/s13690-026-01984-2 | none | Not flagged OA by Europe PMC; Archives of Public Health is normally open at publisher | International study of 24-hour movement behaviours among preschool children (SUNRISE). A pilot study from Nepal (Subedi, Arch Public Health) | 99 children, feasibility and acceptability of the protocol, focus groups, technical notes | Nepal. Sibling SUNRISE pilots exist for Ecuador (10.1111/cch.70288, PMC13158317, 86.1% with a valid day) and Portugal (10.1111/cch.70255). One profile could cover the multi-country pilot programme. |
| 20 | 2019-01-31 | ActiGraph GT3X Link wrist | 10.1016/j.heliyon.2019.e01193 | PMC6360339 | Yes, PMC | Compliance with wrist-worn accelerometers in primiparous early postpartum women (Wolpern, Heliyon) | 201 eligible, 82.6% and 70.1% received and wore a functional device in window at two time points, compliance-enhancing protocol | Reports the device-logistics funnel, which few studies do. |
| 21 | 2026-02-02 | Empatica EmbracePlus | 10.2196/74375 | PMC12910266 | Yes, PMC | Digital Health Tools Embedded in a Cancer Genetics Clinic. Observational Study (Nagaraj, JMIR Form Res) | 12-month observation, survival analysis of engagement by age and genetic status, families aged 5+ | The first EmbracePlus (not E4) deployment found, in a clinic-embedded paediatric-inclusive cohort. Canada. |
| 22 | 2019-09-24 | Empatica E4 | 10.2196/13725 | PMC6783695 | Yes, PMC | Using Wearable Physiological Monitors With Suicidal Adolescent Inpatients. Feasibility and Acceptability Study (Kleiman, JMIR Mhealth Uhealth) | 50 inpatients, mean 18 h/day worn, discomfort, qualitative interviews | Inpatient E4 wear time in a high-acuity adolescent population. |
| 23 | 2025-05-30 | Empatica E4 | 10.2196/65559 | PMC12143850 | Yes, PMC | Collecting Real-Life Psychophysiological Data via Wearables to Better Understand Child Behavior in a Children's Psychiatric Center. Mixed Methods Study on Feasibility and Implementation (Hagoort, JMIR Form Res) | feasibility of reliable data during daily activities, CFIR implementation evaluation | Netherlands. Implementation-science framing of an E4 deployment in routine care. |
| 24 | 2023-06-30 | Empatica E4 | 10.1016/j.earlhumdev.2023.105814 | PMC11062485 | Author manuscript | Feasibility of wearable sensors in the NICU. Psychophysiological measures of parental stress (Stein Duker, Early Hum Dev) | 12 dyads, recruitment and enrolment, retention and adherence, sensor usability | E4 worn by parents in a NICU. Small. |
| 25 | 2025-04-05 | Empatica E4 plus pulse oximeter | 10.1136/bmjopen-2024-089598 | PMC11973797 | Yes, PMC | COVID-19 Early Detection in Doctors and Healthcare Workers (CEDiD) study. A cohort study on the feasibility of wearable devices (Zargaran, BMJ Open) | 30 healthcare workers, 30 days, daily swabs, feasibility in the title | Streaming E4 wear over a month in working clinicians. UK. |
| 26 | 2025-02-21 | Empatica E4, Fitbit Sense and Oura ring worn simultaneously | 10.1186/s12938-025-01353-0 | PMC11846298 | Yes, PMC | Cross-evaluation of wearable data for use in Parkinson's disease research. A free-living observational study on Empatica E4, Fitbit Sense, and Oura (Reithe, Biomed Eng Online) | 31 participants, 2 weeks, uptime calculation per device | Three Module 1 devices on the same wrist and finger for two weeks. Risk that it screens as validation. Norway. |
| 27 | 2024-06-14 | Fitbit, Garmin, Sense-IT and Empatica E4 in crossover | 10.3389/fpsyt.2024.1330993 | PMC11212012 | Yes, PMC | Putting the usability of wearable technology in forensic psychiatry to the test. A randomized crossover trial (de Looff, Front Psychiatry) | one week per device, staff and patients, usability, acceptance, continuous use | Forensic psychiatric setting with a head-to-head continuous-use comparison. Netherlands. |
| 28 | 2023-01-20 | Withings digital BP cuff plus smartwatch (eFHS) | 10.2196/40784 | PMC9898831 | Yes, PMC | Increasing Engagement in the Electronic Framingham Heart Study. Factorial Randomized Controlled Trial (Trinquart, J Med Internet Res) | 2x2x2 factorial trial of notification strategies, weekly transmission as the adherence outcome | An experiment on the adherence mechanism itself, inside a large e-cohort. Withings priority. |
| 29 | 2025-01-15 | Fitbit and Withings inside iCardia4HF | 10.2196/55586 | PMC11780297 | Yes, PMC | Patient-Centered mHealth Intervention to Improve Self-Care in Patients With Chronic Heart Failure. Phase 1 Randomized Controlled Trial (Kitsiou, J Med Internet Res) | recruitment and retention rates as key feasibility measures, 8 weeks | Withings in a clinical RCT with recruitment and retention as the feasibility outcome. |
| 30 | 2024-08 | Withings ScanWatch plus Biobeat patch | 10.1177/20552076241277039 | PMC11363237 | Yes, PMC | Wearables are a viable digital health tool for older Indigenous adults living remotely in Australia (Henson, Digit Health) | 11 participants, 5 days, heat above 36 C, variable connectivity, co-design | Remote Aboriginal community deployment. Small and mostly qualitative, but a setting the module lacks. |

### Further new candidates, lower priority

These passed screening but rank below the table above, mostly because the abstract carries only one or two signals or the cohort is small. Same Reported status.

| Date | Device(s) per abstract | DOI | PMCID | OA | Title (first author, venue) | Signals | Note |
|---|---|---|---|---|---|---|---|
| 2026-08-28 | Garmin Vivoactive 5 or Venu 3, plus Somnofy radar | 10.2196/95194 | none | JMIR, no PMC deposit yet | A One-Year Study Using Digital Biomarkers From Sensing Technologies ... Nursing Home Residents With Dementia (Boyle, JMIR Nurs) | recruitment, adherence, 7-day windows at 0, 6 and 12 months | Norway. The 2025 proof-of-concept from the same cohort is 10.3390/s25216635 (PMC12610480). |
| 2026-08-20 | Garmin Vivofit 4 | 10.21203/rs.3.rs-10475033/v1 | none | Research Square preprint | Plymfit Study. Feasibility of wrist-worn, commercially available, activity monitor use in perioperative care (Hunter) | 75 eligible, 50 recruited, stop-modify-go criteria, preoperative adherence | UK. The F1000 record (10.12688/f1000research.161851.1) is the protocol and was excluded. |
| 2026-07-23 | Axivity AX6, lumbar and wrist | 10.2196/91009 | none | JMIR, no PMC deposit yet | Using Wearable Devices to Monitor Activity and Sleep in Inpatients With Parkinson Disease With and Without Delirium. Feasibility and Acceptability Study (Bate, J Med Internet Res) | recruitment, placement, nonsecurement, wear time | UK inpatient delirium cohort, up to 7 days. |
| 2026-07-03 | Oura ring plus daily EMA app | 10.3389/fdgth.2026.1744937 | none | Frontiers, open at publisher | Identifying risk factors for drug use recurrence with ecological momentary assessment, wearable technologies, and machine learning (Mahoney, Front Digit Health) | 270 days in three phases, recruitment from treatment and sober living, adherence, attrition | US. Long Oura deployment in substance use disorder. |
| 2025-12-04 | Oura Ring | 10.2196/78613 | PMC12677873 | Yes | Oura Ring Behavioral Feedback Intervention for Alcohol Reduction in Young Adults. User Experience Evaluation of a Pilot Randomized Trial (Griffith, J Med Internet Res) | 60 participants, 6 weeks, daily diaries, acceptability and feasibility | US. |
| 2026-01 | Oura Ring or Fitbit with Welloop app | 10.1177/20552076261466410 | PMC13338537 | Yes | Feasibility and behavioral impact of a wearable-supported digital health intervention ... Kobe City (Hayashi, Digit Health) | 130 participants, about 12 weeks, participants bore their own mobile costs | Japan. Signals are thin in the abstract. |
| 2023-09-28 | Oura Ring | 10.3389/fcdhc.2023.1251411 | PMC10569025 | Yes | A holistic approach to preventing type 2 diabetes in Asian women with a history of gestational diabetes mellitus. A feasibility study and pilot randomized controlled trial (Liew, Front Clin Diabetes Healthc) | feasibility, recruitment from a multi-ethnic community | Singapore. |
| 2024-09-03 | Oura, Garmin and other wearables across six cohorts | 10.2196/57827 | PMC11408887 | Yes | Value of Engagement in Digital Health Technology Research. Evidence Across 6 Unique Cohort Studies (Goodday, J Med Internet Res) | adherence, retention and engagement across six studies with participant-centric design | Overlaps the existing TemPredict profile for the healthcare-worker cohort, so use it for the other five cohorts only. |
| 2022-03-08 | Garmin and Oura | 10.1038/s41598-022-07764-6 | PMC8904796 | Yes | Real-time infection prediction with wearable physiological monitoring and AI to aid military workforce readiness during COVID-19 (Conroy, Sci Rep) | 9,381 personnel, 599,174 user-days, June 2020 to April 2021 | Scale is exceptional. The abstract reports no adherence figure, so it may screen out as an algorithm paper. |
| 2025-10-17 | Garmin Fenix 6 under PPE | 10.2196/72324 | PMC12533933 | Yes | Predicting Risk of Heat-Related Injuries for Individuals Wearing Personal Protective Equipment Using Smartwatches. Feasibility Observational Study (Hegarty-Craver, JMIR Form Res) | data quality under PPE, comfort, when a watch cannot be worn | Occupational, convenience cohorts. |
| 2025-11-14 | Garmin smartwatches | 10.2196/67721 | PMC12617830 | Yes | Effects of Heat Adaptation Behaviors on Resting Heart Rate Response to Summer Temperatures in Older Adults. Wearable Device Panel Study (Chen, JMIR Public Health Surveill) | 83 older adults, May to September continuous wear | Taipei. No adherence figure in the abstract. |
| 2023-11-01 | Garmin Vivofit 2 plus tablet eDiary | 10.1183/23120541.00366-2023 | PMC10752267 | Yes | Using an electronic diary and wristband accelerometer to detect exacerbations and activity levels in COPD. A feasibility study (Finney, ERJ Open Res) | 25 patients, 3 months, eDiary compliance by age, severity and exacerbation frequency | UK. |
| 2023-04-07 | Garmin Vivosmart 4 plus symptom app | 10.1371/journal.pdig.0000225 | PMC10081770 | Yes | Feasibility and patient acceptability of a commercially available wearable and a smart phone application in identification of motor states in Parkinson's disease (Liikkanen, PLOS Digit Health) | 65 participants, about 4 weeks at home, acceptability | Finland. |
| 2021-06-24 | Garmin Vívofit HR | 10.1097/cu9.0000000000000030 | PMC8772679 | Yes | Feasibility of wearable activity trackers in cystectomy patients to monitor for postoperative complications (Slade, Curr Urol) | 20 patients, 30 days, compliance surveyed by phone every 10 days | US. |
| 2020-05-29 | Garmin Vivoactive HR | 10.1111/ecc.13254 | PMC7535960 | Author manuscript | A feasibility study of an unsupervised, pre-operative exercise program for adults with lung cancer (Finley, Eur J Cancer Care) | 30 participants, 79% completed, 71% synced successfully, transmission days | US. Sync failure is quantified. |
| 2024-11-08 | Garmin (decentralised trial) | 10.21203/rs.3.rs-5159368/v1 | none | Research Square preprint | Lessons learned from PCD-ENGAGE, a decentralized mobile health clinical trial for the management of primary ciliary dyskinesia (Sahota) | decentralised RCT, co-design, engagement | UK. Garmin is named in the abstract, but the body of the abstract is about the trial design. |
| 2026-05-24 | Withings Sleep Analyser (under-mattress, not worn) | 10.64898/2026.05.22.26353861 | none | medRxiv preprint | InSleep46. Deployment of a remote monitoring device for the detection and monitoring of dementia risk in older adult populations (King-Robson, medRxiv) | 263 recruited (74%), 245 set up (93%), 62% needed at least one troubleshooting call, 603 calls, 14-month follow-up | UK 1946 birth cohort. The device is a bed sensor, so it is in scope only if the Withings profile is read to cover it. The troubleshooting-load figures are exactly this module's subject. |
| 2025-03-06 | Apple Watch 7, Garmin Fenix 6 Pro, Withings ScanWatch | 10.1007/s10877-025-01273-3 | PMC12474713 | Yes | Postoperative use of fitness trackers for continuous monitoring of vital signs. A survey of hospitalized patients (Helmer, J Clin Monit Comput) | compliance, adverse events, whole hospital stay | Germany. Same first author as the Movesense palliative profile, different study. |
| 2022-09-01 | Withings Steel HR plus accelerateIQ | 10.1159/000526438 | PMC9710428 | Yes | Remote Monitoring of Vital and Activity Parameters in Chronic Transfusion-Dependent Patients. A Feasibility Pilot Using Wearable Biosensors (Tonino, Digit Biomark) | 5 patients, 98.9% of Withings data usable | Netherlands. Five participants. |
| 2021-04-23 | Apple, Fitbit, Garmin, Oura, Polar, Samsung, Withings via mSpider | 10.2196/23806 | PMC8074951 | Yes | Consumer-Based Activity Trackers as a Tool for Physical Activity Monitoring in Epidemiological Studies During the COVID-19 Pandemic. Development and Usability Study (Henriksen, JMIR Public Health Surveill) | 35 provisioned plus 113 BYOD participants, 2019 onward | Norway. Half system-development paper, so it may screen out as architecture. |
| 2019-04-17 | Withings Activité Pop and Body scale | 10.1089/tmj.2019.0017 | PMC7071022 | Author manuscript | Telehealth-Based Health Coaching Increases m-Health Device Adherence and Rate of Weight Loss in Obese Participants (Alencar, Telemed J E Health) | 25 participants, device adherence as outcome | US. |
| 2024-02-22 | WHOOP band | 10.2196/51569 | PMC10921319 | Yes | Investigating the Feasibility of Using a Wearable Device to Measure Physiologic Health Data in Emergency Nurses and Residents. Observational Cohort Study (Agarwal, JMIR Form Res) | 20 participants, 6 weeks, 10 of 20 used the device consistently | US. |
| 2021-10-22 | WHOOP Strap 2.0 | 10.1080/17434440.2021.1990038 | none | No, paywalled | Feasibility of a wearable biosensor device to characterize exercise and sleep in neurology residents (Niotis, Expert Rev Med Devices) | 16 of 22 eligible enrolled, 11 met a 6-month minimum use requirement | US. |
| 2020-01 | WHOOP | 10.14283/jpad.2019.39 | PMC8202529 | Author manuscript | Feasibility of Using a Wearable Biosensor Device in Patients at Risk for Alzheimer's Disease Dementia (Saif, J Prev Alzheimers Dis) | 34 of 40 screened agreed, one device lost before collection | US. |
| 2023-11-20 | GENEActiv wrist and lumbar | 10.1159/000535283 | PMC11014463 | Yes | Monitoring Gait and Physical Activity of Elderly Frail Individuals in Free-Living Environment. A Feasibility Study (Camerlingo, Gerontology) | 50 older adults, 2 weeks at home, compliant-day definitions per site, comfort questionnaire | US. Pfizer authors, check COI. |
| 2022-09-29 | Axivity AX3 plus Chronicle passive phone sensing | 10.2196/40572 | PMC9562053 | Yes | Feasibility of Measuring Screen Time, Activity, and Context Among Families With Preschoolers. Intensive Longitudinal Pilot Study (Parker, JMIR Form Res) | 30-day protocol, 7-day EMA, second 14-day protocol months later, retention | US. iOS screen time by screenshot is a documented OS workaround. |
| 2025-11-14 | GENEActiv | 10.2196/81107 | PMC12617961 | Yes | Sleep and Activity Patterns as Transdiagnostic Behavioral Biomarkers in Psychiatry. Longitudinal Observational Study From the DeeP-DD Study (Hamitouche, JMIR Form Res) | 8 outpatients, up to 5 months, feasibility case series | Canada. Very small. |
| 2025-12-20 | ActiGraph and activPAL | 10.1177/07334648251408186 | PMC12857642 | Author manuscript | Physical Activity and Sedentary Behavior in Assisted Living Residents. Feasibility and Acceptability of a Longitudinal Study (Son, J Appl Gerontol) | 50 residents, 6 months, 12% withdrew | US. |
| 2023-08-29 | ActiGraph GT3X+ waist | 10.1007/s10865-023-00444-4 | PMC10902189 | Author manuscript | Wearable device adherence among insufficiently-active young adults is independent of identity and motivation for physical activity (Wu, J Behav Med) | N = 271, 7 days, psychological predictors of wear adherence | US. Adherence is the outcome. |
| 2026-01-27 | Samsung Galaxy Watch, plus smartphone | 10.2196/79334 | PMC12822865 | Yes | Evaluation of Hospice@Home for Home-Based Palliative Care. Development and Usability Pilot Study (Kwon, JMIR Form Res) | 5 dyads, 3-week beta, technical logs, challenges | Korea. Mostly a development paper. |
| 2023-02-13 | Samsung Galaxy Watch cuffless BP | 10.1038/s41440-023-01215-z | none | No, paywalled | Feasibility and measurement stability of smartwatch-based cuffless blood pressure monitoring. A real-world prospective observational study (Han, Hypertens Res) | 760 users, 4 weeks post-calibration, 1.5 readings/day, 19.7% measured every day | Korea. BYOD data-upload design. Borderline validation. |

### Screened and excluded at abstract level

Recorded so the next pass does not re-screen them. Laboratory or single-session (Oesterle 2026 E4 methadone, Cole 2021 Polar M600 smoking, Muñoz-Vergara 2022 Polar H10 yoga, Lee 2026 Galaxy Watch 6 tilt-table, Sazhina 2025 Polar H10 EMG, Fukuyama 2026 Garmin hospital volunteers, Sousan 2026 Garmin single shift). Device only measured an outcome with no deployment content in the abstract (Bladen 2026, Li 2026, Sun 2026, van Tilburg 2026, Bell 2026 LB3P, Joy 2026, Tonetti 2026, Nakfoor 2026, Bladen 2026 haemophilia, Anger 2026, Boice 2025, Panchal 2026). Aggregate or population data with no study cohort (Pépin 2020 Withings 740,000 users, Jang 2023 Galaxy Watch survey, Keusch 2025 data donation). Interoperability, platform or dataset papers (Abedian 2025 Garmin FHIR, Corponi 2024 E4 open datasets, Wigman 2025 AMP SCZ design paper, Henriksen 2021 kept as low priority only). Qualitative or preference-only (Lassell 2026 device preferences, Peterson 2023 women's tracker preferences, Karregat 2025 ScanWatch versus Holter interviews, Goodday 2026 co-design framework). Protocols (Hunter 2025 F1000, Pavicic 2026 Frauenherzen). Military recruit attrition rather than study attrition (Decorte 2025). Supplement and consumer-device trials with no wearable-deployment content (De Jesus 2026, D'Adamo 2024). Fitbit rather than Garmin per abstract (Ransom 2025, 10.2196/54630, PMC12180680, a strong adolescent-athlete Fitbit adherence study that belongs in a Fitbit-side pass, not this one).

---

## Already known

Surfaced by this pass and excluded from the tables because they are already in the ledger, a scan file or a stored PDF.

| DOI | Where it is already known | Title |
|---|---|---|
| 10.2196/86049 | `_recency-scan-2026-09.md`, `_citation-graph-scan-2026-09.md`, profile `connect-multi-wearable-psychosis.md` | Bladon 2026, Evaluating Wearable Devices for Remote Monitoring in Psychosis (Fitbit, Samsung, Apple Watch) |
| 10.1002/mus.70323 | `_recency-scan-2026-09.md` | Jewett 2026, Consumer Smartwatch and Research-Grade Accelerometer Step Counts in ALS (Fitbit Sense plus ActiGraph GT9X) |
| 10.1371/journal.pdig.0000517 | `_scan-queue.md` backlog, by description only ("a Hispanic pregnancy Oura cohort, N=15", via the Gong 2025 review). Not yet in the ledger by DOI. | Sharifi-Heris 2024, Feasibility of continuous smart health monitoring in pregnant population (Oura, PMC11152270). This pass supplies the DOI and PMCID the queue entry lacks. |
| 10.2196/76991 | Module 3 stored PDF `literature/2026-carlson-jmirmhealth-garmin-physical-activity-low-income-communities.pdf` and `_recency-scan-2026-09.md` | Carlson 2026, Automated Physical Activity Support for Adults and Youth From Low-Income Communities (Garmin) |
| 10.2196/64955 | Profile `whoop-mental-health-survey-engagement.md`, stored in Module 1 and Module 3 | Presby 2025, WHOOP physiology and mental health |
| 10.2196/91288 | Module 1 stored PDF, whoop folder | Grosicki 2026, Alcohol Use Trajectories During the First 72 Weeks of WHOOP Membership |
| 10.7759/cureus.45362 | Module 1 stored PDF, oura folder | Shiba 2023, Adherence to Multi-Modal Oura Ring Wearables Among Healthcare Workers |
| 10.1038/s41598-022-07314-0 | Profile `oura-tempredict-healthcare-worker-adherence.md`, Module 1 stored PDF | Mason 2022, TemPredict |
| 10.1093/sleep/zsaf156 | Module 1 stored PDF, oura folder | Soon 2025, Longitudinal study of sleep in university freshmen |
| 10.1053/j.gastro.2024.12.024 | Module 1 stored PDF, oura folder, and `_scan-queue.md` (Hirten, pending supplement) | Hirten 2025, IBD flares from wearables |
| 10.3390/s24237475 | Module 1 stored PDF, oura folder | Liang 2024, nocturnal HR and HRV from Oura |
| 10.3389/fpsyt.2021.625247 | Module 1 stored PDF, oura folder | Moshe 2021, Predicting depression and anxiety from smartphone and wearable data |
| 10.2196/67964 | Module 3 stored PDF `literature/2025-borelli-jmirformres-multimodal-passive-sensing-college-depression.pdf` | Borelli 2025, Depressive symptoms in college students from multimodal passive sensing (Oura, Samsung) |
| 10.1371/journal.pone.0295899 | Module 1 stored PDF, whoop folder | Jasinski 2024, maternal HRV as a biomarker of preterm birth (WHOOP) |
| 10.1371/journal.pone.0243693 | Module 1 stored PDF, whoop folder | Miller 2020, respiratory rate and COVID-19 risk (WHOOP) |

Two further author-year filename matches (an Oura dataset paper matching a 2026 Wang file, and an Empatica overcrowding paper matching the 2023 Zhang RADAR-MDD file) were false positives of the filename check and were kept as new. Neither made the ranked table.

---

## What this pass says about the gaps

- **Polar now has six candidates, none strong.** The Polar literature is dominated by laboratory HRV work. The deployment-shaped studies use the H10 chest strap in home biofeedback or exercise programmes (Corrado, Zupkauskiene, Nabasny) or an older Polar activity watch in a paediatric or oncology trial (Knox, McNeil, Achawakulthep). Any of the first three would give Polar its first profile. None reports a wear-time definition in the abstract.
- **Garmin is far better served than the module's single profile suggests.** Thomassen 2025 alone would change the module's picture of consumer-tracker feasibility over a year, and the Kampala pair (Mobley 2026, Nielsen 2024) adds a low-income setting.
- **Geography.** Uganda, Burkina Faso, Nepal, Ecuador, Jamaica, Thailand, Lithuania, Korea, Japan, Singapore, Taiwan and remote Aboriginal Australia all appear above. The module currently has none of these.
- **Empatica moves from E4-only to EmbracePlus.** Nagaraj 2026 is the first EmbracePlus deployment found. The module's Empatica evidence is otherwise all E4, a discontinued device.
- **Movesense returned nothing new.** Fifty hits in round 1, six in round 2, and none was a deployment beyond the palliative trial already profiled. Treat as unproven rather than absent, per the module's own rule on name-based nulls.
- **Round 1's date window did not reach 2019 for the five high-volume devices.** Round 2's title filter partly compensates, but pre-2023 Garmin, Polar, Samsung, ActiGraph and Axivity deployments whose titles do not carry a deployment word remain unsearched. A further pass with the deployment block moved to ABSTRACT: fields, or with a year-by-year date split, would close that.
- **Fitbit and Apple Watch were deliberately not queried** because they are already the module's best-covered devices. Ransom 2025 (Fitbit Sense, adolescent athletes, hourly and daily adherence definitions) surfaced incidentally and is worth a Fitbit-side pass of its own.
