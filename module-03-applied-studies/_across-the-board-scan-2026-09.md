# Module 3 across-the-board discovery scan, 2026-09-03

**Purpose.** Every earlier discovery pass for this module searched either from the platform side or, in the parallel pass run the same day, from the device side. This pass ran three strands that none of them covered. Strand 1 is topic-first (deployment-reality vocabulary first, technology second) across Europe PMC, date-sorted, 2023 to 2026. Strand 2 is the ACM venue blind spot (IMWUT, CSCW, UbiComp, CHI) via OpenAlex. Strand 3 is grey literature (ClinicalTrials.gov posted results, consortium output, vendor pages).

**Status of every attribution in this file. Reported, not Verified.** No full text was read. Every technology named below is what a title or abstract says, and every deployment signal is what an abstract mentions. Both must be confirmed from the Methods before anything is profiled. This project has a measured abstract-level platform-misattribution rate of roughly 3 in 12, and this pass gives no reason to expect better.

**No PDFs were downloaded and no other file was edited.** This file is the whole output. Nothing was committed.

**Reconciliation baseline.** Every hit was checked by DOI and PMCID against `literature-index.json`, `_scan-queue.md`, `_onnela-module3-candidates.md`, `_recency-scan-2026-09.md`, `_citation-graph-scan-2026-09.md`, every Module 3 profile, every `.md` and `.json` in the repo, and the 150 stored PDFs under the three `literature/` folders (matched on year plus first-author surname, so PDF matches are approximate and were hand-checked before being listed). One more file appeared in the module directory while this scan was running, `_device-side-scan-2026-09.md` (uncommitted, written by the parallel device-side pass). It was not in the reconciliation brief, but it overlaps this scan, so its DOIs were also checked and the overlap is listed separately rather than counted as new.

---

## Method and hit counts

### Strand 1. Topic-first, Europe PMC REST

Endpoint `https://www.ebi.ac.uk/europepmc/webservices/rest/search`, `format=json`, `pageSize=100`, `resultType=lite`, `sort=P_PDATE_D desc`, cursor paging to a maximum of 300 records per query. Date block `FIRST_PDATE:[2023-01-01 TO 2026-12-31]` on every query.

Shared deployment-signal block `SIG`

```
(adherence OR retention OR attrition OR "wear time" OR "data completeness" OR missingness OR "technical issues" OR "lessons learned" OR compliance OR "data quality" OR dropout)
```

Shared context block `CTX`

```
(feasibility OR "remote monitoring" OR longitudinal OR pilot OR cohort OR deployment)
```

| ID | Query (abbreviated) | Hits | Retrieved |
|---|---|---|---|
| S1a | `(TITLE:"digital phenotyping" OR ABSTRACT:"digital phenotyping" OR TITLE:"passive sensing" OR ABSTRACT:"passive sensing") AND SIG AND CTX` | 324 | 300 |
| S1b | `(TITLE:wearable OR TITLE:smartwatch OR TITLE:"smart ring") AND (TITLE:feasibility OR TITLE:adherence OR TITLE:retention OR TITLE:"lessons learned" OR TITLE:"data completeness" OR TITLE:"wear time" OR TITLE:"real-world" OR TITLE:"remote monitoring") AND SIG` | 223 | 223 |
| S1c | `(ABSTRACT:"RADAR-base" OR ABSTRACT:"RADAR-CNS" OR ABSTRACT:"RADAR-MDD" OR ABSTRACT:"RADAR-AD" OR TITLE:"RADAR-base") AND SIG` | 11 | 11 |
| S1d | `(ABSTRACT:mindLAMP OR ABSTRACT:"LAMP app" OR ABSTRACT:"LAMP platform" OR TITLE:mindLAMP) AND SIG` | 21 | 21 |
| S1e | `(ABSTRACT:"AWARE framework" OR ABSTRACT:"AWARE-Light" OR ABSTRACT:"AWARE Light" OR ABSTRACT:"AWARE app") AND (ABSTRACT:smartphone OR ABSTRACT:"passive sensing" OR ABSTRACT:"mobile sensing") AND SIG` | 1 | 1 |
| S1f | `(ABSTRACT:"Avicenna Research" OR ABSTRACT:"Avicenna app" OR ABSTRACT:"Ethica Data" OR ABSTRACT:"Ethica app" OR ABSTRACT:"formerly Ethica") AND (ABSTRACT:"ecological momentary" OR ABSTRACT:smartphone OR ABSTRACT:"experience sampling") AND SIG` | 2 | 2 |
| S1g | `ABSTRACT:MetricWire AND SIG` | 1 | 1 |
| S1h | `(ABSTRACT:"m-Path" OR ABSTRACT:"mPath app") AND (ABSTRACT:"experience sampling" OR ABSTRACT:"ecological momentary" OR ABSTRACT:smartphone) AND SIG` | 12 | 12 |
| S1i | `(ABSTRACT:"CARP Mobile Sensing" OR ABSTRACT:"Copenhagen Research Platform" OR ABSTRACT:"CARP platform" OR ABSTRACT:"CAMS framework") AND SIG` | 1 | 1 |
| S1j | `(ABSTRACT:"LifeData" OR ABSTRACT:"RealLife Exp") AND SIG` | 2 | 2 |
| S1k | `(ABSTRACT:Beiwe OR TITLE:Beiwe) AND SIG` | 16 | 16 |
| S1l | LMIC block. `(TITLE:wearable OR TITLE:smartphone OR ABSTRACT:"digital phenotyping" OR ABSTRACT:"passive sensing" OR ABSTRACT:Fitbit OR ABSTRACT:Garmin OR ABSTRACT:Oura) AND (ABSTRACT:"low- and middle-income" OR ABSTRACT:LMIC OR ABSTRACT:"sub-Saharan" OR 22 named countries) AND (feasibility OR adherence OR "wear time" OR retention OR "data completeness" in ABSTRACT)` | 64 | 64 |
| S1m | Multi-device block. `(ABSTRACT:"multiple wearables" OR ABSTRACT:"multi-device" OR paired device names such as Fitbit AND Oura, Garmin AND Fitbit, "Apple Watch" AND Fitbit, WHOOP AND Oura, Empatica AND smartphone) AND (feasibility OR adherence OR "wear time" OR retention OR "data completeness" OR missingness OR compliance in ABSTRACT)` | 34 | 34 |
| S1n | Platform head-to-head block. `((ABSTRACT:Beiwe OR ABSTRACT:mindLAMP OR ABSTRACT:"RADAR-base" OR ABSTRACT:"AWARE framework") AND (ABSTRACT:compared OR ABSTRACT:comparison OR ABSTRACT:"head-to-head")) AND (ABSTRACT:platform OR ABSTRACT:app)` | 11 | 11 |
| S1o | Device block. `(ABSTRACT: any of Oura, WHOOP, Garmin, Fitbit, "Apple Watch", Empatica, Withings, "Samsung Galaxy Watch", "Polar Vantage", "Polar Verity", ActiGraph, GENEActiv, Axivity) AND (TITLE: feasibility OR adherence OR retention OR "lessons learned" OR "real-world" OR "remote monitoring" OR "wear time" OR "data completeness" OR engagement OR compliance) AND (ABSTRACT: "wear time" OR adherence OR retention OR attrition OR "data completeness" OR missing OR dropout OR technical)` | 166 | 166 |

Funnel. 1,065 records retrieved, 795 unique. 59 matched the reconciliation baseline by DOI, PMCID or PDF. 137 were dropped on title alone (review, protocol, validation, accuracy, agreement, algorithm). Abstracts were fetched for the remaining 599 (589 retrieved). A candidate survived only if its abstract named a Module 1 or Module 2 technology and carried at least two distinct deployment-signal terms. 136 survived. Of those, 20 are also in the parallel device-side scan and are listed under "Already known" rather than as new.

Trap notes. The AWARE query (S1e) returned one hit and it was the HEAR-aware hearing-loss app, a false positive. Per this module's rule that a name-query null is unproven for AWARE, CARP, Polar, Oura, Samsung, Avicenna and m-Path, that null is recorded as unproven, not as absence. The CARP query (S1i) returned only the already-profiled Niemeijer m-Path Sense paper, consistent with the known finding that CARP publishes under application names. The platform head-to-head query (S1n) returned no genuine cross-platform comparison. Eight of its eleven hits were unrelated or already known, and the rest compare a single platform's metrics against clinical measures. The Beiwe versus mindLAMP versus RADAR-base head-to-head gap stays open. The m-Path query surfaced three duplicate preprint versions of one aphasia EMA paper and two of one simulation paper, which were collapsed.

### Strand 2. ACM venue blind spot, OpenAlex

Endpoint `https://api.openalex.org/works`, `filter=from_publication_date:2022-01-01`, `sort=publication_date:desc`, `per-page=50`, three pages per query, `select` restricted to id, doi, title, date, primary_location, open_access, type, ids, authorships, locations. OA route recorded from `open_access.oa_url` plus a check for any arXiv location.

| ID | `search=` | Hits | Retrieved |
|---|---|---|---|
| S2a | `"passive sensing" "participant engagement"` | 105 | 105 |
| S2b | `"passive sensing" "data quality"` | 631 | 150 |
| S2c | `"passive sensing" compliance` | 1,138 | 150 |
| S2d | `AWARE framework mobile sensing engagement` | 111,716 | 150 |
| S2e | `AWARE framework smartphone data quality` | 106,759 | 150 |
| S2f | `"digital phenotyping" "data quality" engagement` | 558 | 150 |
| S2g | `"mobile sensing" study compliance participants "lessons learned"` | 79 | 79 |
| S2h | `"experience sampling" smartphone compliance "passive sensing"` | 220 | 150 |
| S2i | `"AWARE framework"` | 12,441 | 150 |
| S2j | `"AWARE-Light"` | 179 | 150 |
| S2k | `"mobile sensing" "in the wild" study participants compliance` | 153 | 150 |
| S2l | `"digital phenotyping" "lessons learned"` | 362 | 150 |
| S2m | `"passive sensing" study "attrition"` | 270 | 150 |
| S2n | `"Beiwe" OR "mindLAMP" OR "RADAR-base" comparison platforms` | 1,793,255 | 150, unusable |

Trap notes. OpenAlex does not honour phrase quoting for "AWARE" either. S2d, S2e and S2i are dominated by "risk-aware", "geometry-aware", "hardware-aware" and similar. Date-sorting then fills the window with noise, exactly as Europe PMC did in the recency scan. The usable AWARE hits below came from the S2j "AWARE-Light" query and from venue-restricted screening of the other queries. S2n's OR syntax was interpreted as a bare-word search and is recorded only so nobody repeats it. Of 1,050 unique OpenAlex works across all queries, 33 sit in an ACM or ubiquitous-computing venue, and 14 of those plus 12 non-ACM works from the same queries passed a title-and-abstract screen.

### Strand 3. Grey literature

ClinicalTrials.gov v2. `https://clinicaltrials.gov/api/v2/studies?query.term=<term>&filter.overallStatus=COMPLETED&aggFilters=results:with&pageSize=200`, with `fields` restricted to the identification, status, design, interventions and participant-flow modules. Note for the next run. The v2 API rejects `EnrollmentInfo` and `FlowDropWithdrawCount` as field names. Piece paths such as `protocolSection.designModule` and `resultsSection.participantFlowModule` work.

| Term | Completed trials with posted results |
|---|---|
| Oura ring | 2 |
| WHOOP strap | 0 |
| Garmin | 17 |
| Fitbit | 183 |
| Empatica | 2 |
| Beiwe | 1 |
| mindLAMP | 0 |
| RADAR-base | 6, all false positives (Radar-A dialysis, RADAR delirium, RadAR compression device, and similar) |
| Apple Watch | 29 |
| Withings | 11 |
| ActiGraph | 196 |
| digital phenotyping smartphone | 0 |

406 unique registrations. 64 were device-relevant by title, intervention text or a device-related withdrawal reason. Only a handful record a withdrawal reason that names the device or its data. The rest use the registry's generic categories, so the registry is a poor source of device-specific attrition. The Beiwe hit is the HOPE trial and SMART study registration (NCT03022032, completed 2020, N=102, "SMART study app + Beiwe study app + Fitbit"), which is already covered by the Panda and Wright Module 2 PDFs.

Consortium output was searched in Europe PMC with the same deployment-signal block. `("Mobilise-D" OR "Mobilise D") AND SIG, 2023 to 2026` returned 120. `("IDEA-FAST" OR "IDEA FAST") AND SIG, 2022 to 2026` returned 96. `("RADAR-CNS" OR "RADAR-MDD" OR "RADAR-AD" OR "RADAR-Epilepsy" OR "RADAR-MS") AND SIG, 2023 to 2026` returned 104.

Vendor pages were probed with curl. `ouraring.com/research` and `empatica.com/research/` return 404. `whoop.com/us/en/unite/` and `mobilise-d.eu/publications/` return a Cloudflare challenge. `garmin.com/en-US/health/`, `idea-fast.eu/publications/` and `actigraphcorp.com/case-studies/` load but carry no adherence, retention or completion figures in their page text. Vendor case studies therefore contributed nothing this pass and would need a browser session.

---

## Ranked NEW candidates

Ranking weighs, in order, whether the paper's own outcome is deployment reality (adherence, wear time, retention, missingness, technical failure) rather than a clinical finding, then priority-area fit (LMIC, non-Beiwe platform, multi-device, head-to-head), then scale and duration, then OA availability. "Tech" is the technology as named in the abstract. "Signals" quotes the abstract. Confidence is Reported for every row, so the column instead grades how strongly the abstract itself supports Module 3 inclusion (high, medium, low).

| Rank | Date | Tech (per abstract) | DOI or identifier | PMCID | OA and route | Title (shortened) | Deployment signals in abstract | Why it matters | Conf. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2024-01-19 | RADAR-base + Fitbit, MDD | 10.2196/44214 | PMC10837755 | Yes, PMC and JMIR | Engagement With a Remote Symptom-Tracking Platform Among Participants With MDD, RCT | 100 participants, n=50 per arm, completion 50% to 95% across measures, "engagement" as the trial outcome | An RCT whose primary outcome is engagement with RADAR-base itself. Non-Beiwe platform. Complements the profiled Zhang 2023 and Matcham 2022 RADAR-MDD entries | high |
| 2 | 2023-02-01 | mindLAMP, 1,178 participants pooled | 10.1136/bmjment-2023-300718 | PMC10231441 | Yes, PMC | Increasing the value of digital phenotyping through reducing missingness, retrospective review of prior studies | Pooled mindLAMP cohorts May 2019 to March 2022, college, schizophrenia, depression and anxiety, missingness by sampling frequency, population and device | The largest missingness analysis for a non-Beiwe platform found in any pass. Directly on this module's central theme | high |
| 3 | 2023-02-28 | Fitbit Inspire HR, MS, rehab and home | 10.3389/fdgth.2023.1006932 | PMC10012422 | Yes, PMC | Feasibility and scalability of a fitness tracker study, persons with multiple sclerosis (BarKA-MS) | 45 participants, up to 8 weeks, 96% weekly survey completion, 99% and 97% valid wear days in clinic and at home, explicit "lessons learned" and scalability checklist | Lessons-learned paper with wear-day figures in two settings | high |
| 4 | 2025-05-02 | AWARE (per venue and abstract), mental wellness crowdsensing | 10.1145/3711043 | none | ACM DL only, previously unobtainable | Participant Engagement and Data Quality, Lessons Learned from a Mental Wellness Crowdsensing Study (CSCW) | Title is the module's theme | Re-surfaced by S2. OpenAlex now lists `dl.acm.org/doi/pdf/10.1145/3711043` as OA, but `_aware-build-report.md` records that URL as serving a challenge page. Worth one more retrieval attempt through a browser before leaving it on the unobtainable list | high if obtainable |
| 5 | 2026-01-24 | Oura ring + study smartwatch EMA | 10.31234/osf.io/fdsqt_v1 | none | Yes, PsyArXiv preprint | Feasibility assessment of smartwatch based EMA of mood with concurrent smart ring assessment of sleep and activity | 2 weeks, "device adherence, EMA completion rate, and patterns of missingness" as the outcomes, mean EMA compliance 90% | Multi-device (ring plus watch) with missingness patterns by time of day. Preprint, so treat as lower certainty | high |
| 6 | 2026-05-19 | Wearable, unnamed in abstract, cirrhosis | 10.21203/rs.3.rs-9633932/v1 | none | Yes, Research Square preprint | Clinical and Demographic Determinants of Adherence to Digital Monitoring in Cirrhosis | 111 enrolled 2023 to 2025, adherence defined as days with at least 80% data transmission, met on 65.6% of eligible days, dropout and attrition modelled | Adherence as the primary outcome with a stated definition. Device must be identified from Methods before it can count | medium |
| 7 | 2025-08-25 | Avicenna, rural South Africa, HIV risk | 10.2196/67519 | PMC12377519 | Yes, PMC | Leveraging Smartphone Mobility Data to Understand HIV Risk Among Rural South African Young Adults, Feasibility | 207 enrolled in two phases 2021 to 2023, provisioned then BYOD, 28.4% of expected weekly location points, troubleshooting after 48 to 72 h gaps, reverse billing and gamification | LMIC and Avicenna at once, with completeness figures and engagement tactics. Phase I provisioned versus Phase II BYOD is a natural comparison | high |
| 8 | 2024-01-01 | Garmin vivoactive 3, Kampala slums | 10.1177/20552076241288754 | PMC11489944 | Yes, PMC | Feasibility and acceptability of wearable devices and daily diaries among young women in the slums of Kampala | 60 women, two 5-day pilots, all responded to diaries, all but one reported non-stop wear, data completeness reported | LMIC, low-income setting. Short duration limits what it can say about retention. Also in the device-side scan, listed here because LMIC is this strand's priority | medium |
| 9 | 2023-12-04 | Wearable activity trackers, Kenya, adolescents | 10.1017/gmh.2023.85 | PMC10755372 | Yes, PMC | Using wearable activity trackers for research in the global south, lessons learned from adolescent psychotherapy research in Kenya | Procurement, on-site support, a dedicated operator, paper information sheets | Labelled a perspective, so may fall under no-cohort. Included because it is the only sub-Saharan lessons-learned paper found and the device must be checked | medium |
| 10 | 2026-02-13 | Fitbit + EMA, 1,314 adults, Czechia | 10.1007/s12529-025-10433-3 | none | No, Springer | Participant-Level Characteristics Predicting Adherence to Long-Term EMA and Fitbit Monitoring in the 4HAIE Cohort | 12 months, four 2-week EMA bursts, adherence as valid Fitbit days and completed surveys | Largest long-duration adherence-predictor analysis found. Paywalled | high |
| 11 | 2025-04-08 | Garmin Vivosmart 4 + Labfront + EMA, older adults | 10.2196/69952 | PMC12015335 | Yes, PMC | Longitudinal and Combined Smartwatch and EMA in Racially Diverse Older Adults, Feasibility, Adherence, Acceptability | 44 adults 55+, 4 weeks, 23 h per day wear instruction, daily sync of two apps, adherence reported | Garmin has one profile. Multi-app sync burden is documented. Also in the device-side scan | high |
| 12 | 2025-05-07 | Garmin vivosmart 4, axial spondyloarthritis, 1 year | 10.2196/68645 | PMC12077851 | Yes, PMC | Feasibility of Long-Term Physical Activity Measurement With a Wearable Activity Tracker in Patients With axSpA | Trial, technical and operational feasibility separated, days worn, missing data, synchronisation reminders, tracker replacements | One-year Garmin deployment with replacement counts. Also in the device-side scan | high |
| 13 | 2023-08-01 | Fitbit Charge 3 + EMA, post-ED suicidal ideation | 10.1001/jamanetworkopen.2023.28005 | PMC10410485 | Yes, PMC | EMA and Passive Sensing in the Prediction of Short-Term Suicidal Ideation in Young Adults | 8 weeks, 14,708 EMAs at 64.4% adherence, wristband worn about half the time at 55.6% adherence | Clinical prediction paper but with explicit dual-modality adherence figures | medium |
| 14 | 2023-07-21 | Fitbit + EMA, same cohort as rank 13 | 10.1016/j.psychres.2023.115347 | none | No, Elsevier | Acceptability and feasibility of EMA with augmentation of passive sensor data in young adults at high risk for suicide | 106 participants, 2 months, EMA 62.1% and Fitbit 53.6% adherence, 81% completed EMA versus 63% completed Fitbit, previous-day ideation predicted lower next-day wear | The feasibility companion to rank 13. Paywalled. If both are profiled, note the shared cohort | high |
| 15 | 2025-09-03 | Smartwatch µEMA, 177 participants, 12 months | 10.1145/3749541 | none | ACM DL PDF listed as OA | Longitudinal User Engagement with Microinteraction EMA (IMWUT) | 1.37 million µEMA and 14.9K EMA surveys, completed versus withdrew groups compared | Engagement over a year at scale. The smartwatch and app are not named in the abstract, so this may be a custom platform and fall outside scope | medium |
| 16 | 2025-10-22 | Smartwatch + smartphone EMA, TIME study, N=246 | 10.2196/67117 | none | Yes, JMIR | Understanding Longitudinal EMA Completion, 12 Months of Burst Sampling | Completion 13% to 95% by burst and modality | Same TIME programme as rank 15. Platform unnamed in the abstract | medium |
| 17 | 2024-09-07 | Mobile sensing app, n=145 | 10.2196/55694 | none | Yes, JMIR | Design Guidelines for Improving Mobile Sensing Data Collection, Prospective Mixed Methods | Authorization prompting strategies compared, background-event and notification permission failures in the field | Directly about OS permission failure modes. Platform unnamed, likely custom | medium |
| 18 | 2025-04-23 | Passive sensing + EMA, MS, 2 cohorts | 10.2196/70871 | none | Yes, JMIR accepted preprint | Longitudinal Digital Phenotyping of Multiple Sclerosis Severity Using Passively Sensed Behaviors and EMA | n=97 and n=88 screened, 44 and 39 analysed, completion 72% to 95% | CMU group whose earlier MS work used AWARE. Platform not named in the abstract, so unverified | medium |
| 19 | 2026-03-31 | Oura + mobile app, mental health | 10.2196/77761 | none | Yes, JMIR | Feasibility and Acceptability of a Mobile App and Wearable Device for Collecting Mental Health Survey and Passively Sensed Data | Attrition, completeness and adherence figures from 47% to 96.1% | Oura with a completeness outcome. App unnamed | medium |
| 20 | 2024-06-05 | Oura + REDCap, pregnancy | 10.1371/journal.pdig.0000517 | PMC11152270 | Yes, PMC | Feasibility of continuous smart health monitoring in pregnant population, mixed method | Ring wear above 80% until gestational week 35, falling to about 31% postpartum, survey completion by cadence | Oura over a full pregnancy with a documented drop-off point. Also in the device-side scan | high |
| 21 | 2026-04-13 | Fitbit Charge 3, AYA sarcoma, up to 3 years | 10.2196/87591 | PMC13075630 | Yes, PMC | Physical Activity Monitoring in Adolescents and Young Adults With Cancer, Observational Feasibility | 63 patients, 57.1% wore 10+ h per day in the first 30 days, 23.8% thereafter | Three-year horizon with the sharpest documented adherence collapse found | high |
| 22 | 2024-09-03 | Oura, Garmin, Apple Watch, smart scales, 6 cohorts | 10.2196/57827 | PMC11408887 | Yes, PMC | Value of Engagement in Digital Health Technology Research, Evidence Across 6 Unique Cohort Studies | Retention above 80% in month 1 and above 50% for the active period, median adherence over 80% for Oura and over 90% for Garmin and Apple except cancer and postpartum cohorts | Multi-device, multi-cohort engagement synthesis from one vendor-side group (4YouandMe). Check COI. Also in the device-side scan | high |
| 23 | 2025-06-13 | Fitbit, Apple Watch, Garmin (BYOD mix), adolescent athletes | 10.2196/54630 | PMC12180680 | Yes, PMC | Feasibility of Data Collection Via Consumer-Grade Wearable Devices in Adolescent Student Athletes | 34 athletes, hourly and daily adherence defined by heart-rate presence, 4 to 6 weeks post clearance | BYOD across three ecosystems with an hourly adherence definition. Also in the device-side scan | high |
| 24 | 2023-01-01 | Fitbit, stroke and COPD, 3 months | 10.1177/20552076231176160 | PMC10192672 | Yes, PMC | The feasibility of remotely monitoring physical, cognitive, and psychosocial function in individuals with stroke or COPD | 73 participants, average daily wear time, number needing sync reminders, reminders per completed assessment | Quantifies staff effort per unit of adherence, which almost no paper does | high |
| 25 | 2025-06-09 | Beiwe, stroke and TIA, 8+ weeks | 10.1016/j.mcpdig.2025.100240 | PMC12381640 | Yes, PMC | Real-World Smartphone Data Predicts Mood After Ischemic Stroke and TIA, proof of concept | 54 enrolled, 35 completed (64.8%), collection March to November 2024 | A Beiwe deployment whose window post-dates the 2024 heartbeat feature, which every current Beiwe profile predates. Deployment detail beyond completion is unknown | medium |
| 26 | 2025-04-04 | Beiwe GPS, family caregivers and advanced cancer, 24 weeks | 10.1186/s12885-025-14009-y | PMC11971861 | Yes, PMC | Associations between smartphone GPS data and psychological health among family caregivers and patients with advanced cancer | BYOD, enrolled Aug 2021 to Jul 2023, Facebook and clinic recruitment, 24-week passive GPS | Dyadic Beiwe deployment in caregivers. Abstract carries no completeness figure, so may fail criterion c | medium |
| 27 | 2024-10-04 | Beiwe, chronic musculoskeletal pain, 85 patients | 10.1101/2024.10.03.24314808 | none | Yes, medRxiv | Data Missingness in Digital Phenotyping, Implications for Clinical Inference and Decision-Making | Completeness at day, hour and minute level, missingness versus accelerometer and imputed GPS, model stability across missingness levels | Missingness as the object of study. Likely the same cohort as the profiled Fu 2024 pain programme, so check duplicate-cohort | medium |
| 28 | 2026-02-14 | RADAR-base + Fitbit, RADAR-MDD secondary | 10.1016/j.nsa.2026.106985 | PMC12936773 | Yes, PMC | Sleep, Steps, and Screens, digital markers and smartphone cognition in depression | RADAR-MDD multicentre, Fitbit sleep and steps, RADAR-Base screen time | Secondary analysis. Deployment content probably thin. Listed because it is 2026 RADAR output | low |
| 29 | 2025-01-27 | RADAR-AD device set | 10.1186/s13195-025-01675-0 | PMC11771057 | Yes, PMC | RADAR-AD, assessment of multiple remote monitoring technologies for early detection of Alzheimer's disease | Main results paper of the consortium | The profiled Muurling 2024 entry covers feasibility and usability. This is the results paper and may add attrition and completeness figures. Check duplicate-cohort | medium |
| 30 | 2024-10-29 | RADAR-base + Fitbit, ADHD | 10.2196/54531 | PMC11798566 | Yes, PMC | Identifying Digital Markers of ADHD in a Remote Monitoring Setting, Prospective Observational | Completion figures mentioned | ART study, RADAR-base outside the RADAR-CNS disease set. Deployment content unknown | medium |
| 31 | 2025-01-29 | mindLAMP, Digital Clinic, 258 enrolled | 10.2196/65222 | PMC11822323 | Yes, PMC | Testing the Feasibility, Acceptability, and Potential Efficacy of the Digital Clinic, Open Trial | 215 of 258 completed the 8-week programme (83.3%) | Largest mindLAMP care-delivery cohort found. Feasibility content beyond completion unknown | medium |
| 32 | 2024-11-19 | mindLAMP, app-matching cohort | 10.2196/62725 | PMC11615540 | Yes, PMC | Assessing Digital Phenotyping for App Recommendations and Sustained Engagement, Cohort Study | 1 week of mindLAMP sensing then randomised to feedback arms, engagement as outcome | Engagement outcome. Sensing window is short | low |
| 33 | 2024-06-28 | mindLAMP, schizophrenia, Boston and two India sites, up to 12 months | 10.1371/journal.pdig.0000526 | PMC11213313 | Yes, PMC | Digital phenotyping correlates of mobile cognitive measures in schizophrenia, multisite global mental health feasibility trial | 76 individuals, three sites, up to 12 months | Secondary analysis of the profiled three-site cohort. Duplicate-cohort unless it adds completeness figures | low |
| 34 | 2024-09-16 | LifeData, four countries, online recruitment | 10.1371/journal.pone.0307440 | PMC11404800 | Yes, PMC | Lessons learned from the MOMENT study on how to recruit and retain a target population online, across borders, with automated remote data collection | 411 responses in 48 h, 64.5% flagged as fraudulent, reCAPTCHA and attention checks added before LifeData enrolment | LifeData is newly profiled in Module 2 and has one Module 3 entry. Pairs with the profiled Siebers 2025 fraud paper | high |
| 35 | 2025-12-09 | MetricWire (per abstract), FoodMATS-Youth | 10.2196/79306 | PMC12688025 | Yes, PMC | Exploring the Usability and Acceptability of the FoodMATS-Youth App, Mixed Methods | Compliance 92%, response 85.2%, completion 92% | The only new MetricWire hit. Short and small, but MetricWire has few entries | medium |
| 36 | 2026-04-12 | m-Path, aphasia, 27 people, 14 days | 10.1016/j.jad.2026.121783 | PMC13395528 | PMC (embargo status unclear) plus PsyArXiv 10.31234/osf.io/s8zcq_v1 | Validating an aphasia-accessible EMA for daily depressive affect | 89.6% of 56 scheduled EMAs completed | m-Path has one entry. Accessibility population is unusual | medium |
| 37 | 2026-02-17 | EMA app (m-Path per query), post-encephalitis, 4 months | 10.1080/09602011.2026.2619548 | none | No, Taylor and Francis | COPE-EMBRACE, coping with stress after encephalitis using real-time assessment | 20 adults, daily compliance 79.3% (range 37.3 to 97.5), low self-initiated EMA use | Four-month m-Path deployment. Paywalled | medium |
| 38 | 2023-11-21 | m-Path (per query), specialised mental health care | 10.2196/48821 | PMC10698657 | Yes, PMC | Usability of the Experience Sampling Method in Specialized Mental Health Care, Pilot Evaluation | Clients completed 55% of ESM questionnaires, practitioner dashboard | KU Leuven group. Same authors as the profiled Bonnier and Dennard work, so check overlap | medium |
| 39 | 2024-09-01 | Fitbit, narcolepsy cohort, 1 year | 10.1093/sleep/zsae083 | none | No, Oxford | Swiss Primary Hypersomnolence and Narcolepsy Cohort, feasibility of long-term monitoring with Fitbit | 80% adherence over 1 year, biomarker window chosen as the 2 weeks of best adherence | One-year adherence figure. Paywalled | medium |
| 40 | 2025-10-03 | iPhone + Apple Watch, more than 4,000 participants, 12 months | 10.1101/2025.10.01.25337105 | none | Yes, medRxiv | Assessing the feasibility of large-scale digital sensing for depression and anxiety, the Digital Mental Health Study | Recruitment strategy, protocol development, "high participant engagement and adherence over a 12-month period" | Largest Apple Watch cohort found in any pass. Preprint, and adherence figures are not in the abstract | medium |
| 41 | 2025-04-29 | Apple Watch + ResearchKit app, ages 18 to 84 | 10.3389/fdgth.2025.1520971 | PMC12069264 | Yes, PMC | Feasibility, adherence and usability of an observational digital health study built using Apple's ResearchKit | 228 recruited nationwide, 201 (88.16%) completed 8 weeks, task adherence 70.61% to 100% | Remote consent and no-training deployment across a wide age range | high |
| 42 | 2026-08-02 | Oura, 584 first-year students, two semesters | 10.64898/2026.07.30.26359360 | none | Yes, medRxiv | How Quickly Can You Know a Participant? A 3-Week Triage Point for Oura Ring Adherence in College Students | 442 continued into spring, 408 analysable, classifier flags bottom-quartile adherence by week 3 | Operational tool for adherence support. Also in the device-side scan | high |
| 43 | 2026-03-06 | Fitbit, All of Us, 11,901 participants | 10.64898/2026.03.06.26347799 | none | Yes, medRxiv | Population differences in wearable device wear time, rescuing data to address biases | Wear time higher in males and with age, income and education, lower with depressive and anxiety symptoms | Population-level wear-time bias at scale. Registry data, not a deployment the authors ran, so may fall outside scope. Pairs with the profiled Master 2022 All of Us entry | medium |
| 44 | 2025-05-23 | Fitbit, All of Us, postpartum depression | 10.2196/67585 | PMC12144471 | Yes, PMC | Unlocking the Potential of Wear Time of a Wearable Device to Enhance Postpartum Depression Screening | Wear-time consistency as a signal | Same scope caveat as rank 43 | low |
| 45 | 2024-04-01 | Fitbit, pulmonary arterial hypertension, UPHILL | 10.1002/pul2.12381 | PMC11177024 | Yes, PMC | Evaluating the technical use of a Fitbit during an intervention for PAH patients, lessons learned from UPHILL | Technical issues made 37.5% of data unavailable | A technical-failure paper. Short, but the figure is unusual | high |
| 46 | 2024-02-16 | Fitbit + home sensors, opioid use disorder | 10.21203/rs.3.rs-3921917/v1 | none | Yes, Research Square | Recruitment and Retention Challenges in Opioid Use Disorder Studies, a Pilot Digital Monitoring Study | 170 records, 50 eligible, 14 consented, 4 completed | Recruitment funnel collapse documented honestly. Preprint | medium |
| 47 | 2025-02-11 | Fitbit + HealthReact EMA, 4 countries | 10.1371/journal.pone.0318772 | PMC11813119 | Yes, PMC | EMA of physical and eating behaviours, the WEALTH feasibility and optimisation study | 52 participants, median compliance 49%, event-based 34%, declining, technical issues, recommendations for large-scale collection | Multi-country EMA with low compliance and design recommendations | high |
| 48 | 2025-11-20 | Fitbit plus two research accelerometers, NutriNet-Santé | 10.2196/76167 | PMC12679073 | Yes, PMC | Three Body-Worn Accelerometers in the French NutriNet-Santé Cohort, Feasibility and Acceptability | Wear-time compliance under free living, valid day 600+ min, valid week 4+ days, 22-item acceptability questionnaire | Three-device comparison in one cohort. Also in the device-side scan | high |
| 49 | 2026-01-29 | Fitbit, underserved high-school students | 10.2196/80465 | PMC12855722 | Yes, PMC | Assessing Wearable mHealth Adherence in Underserved Adolescents | 63 students, adherence as 21+ valid days, 73% met threshold, predictors modelled | Adherence as the primary outcome | high |
| 50 | 2026-01-24 | Wearable (Fitbit per query), autism, 8-week telehealth | 10.1080/09593985.2026.2618078 | none | No, Taylor and Francis | Comparing methods to measure wearable device adherence for PA monitoring for persons with autism | 27 participants, two adherence definitions compared (10 h heart-rate wear versus 500 steps), field notes on adherence factors | Method comparison for the adherence definition problem the README flags. Paywalled | medium |
| 51 | 2026-07-23 | Axivity AX6, Parkinson inpatients with delirium | 10.2196/91009 | none | No, JMIR (not yet in PMC at scan time) | Using Wearable Devices to Monitor Activity and Sleep in Inpatients With Parkinson Disease With and Without Delirium | Recruitment rate 75.4%, device placement, non-securement, wear time, compliance | Inpatient Axivity deployment. Also in the device-side scan | high |
| 52 | 2023-06-30 | Empatica E4, NICU parents | 10.1016/j.earlhumdev.2023.105814 | PMC11062485 | PMC (author manuscript) | Feasibility of wearable sensors in the NICU, psychophysiological measures of parental stress | 12 dyads, recruitment, retention and adherence, sensor usability | Empatica has two entries. Also in the device-side scan | medium |
| 53 | 2023-11-28 | Empatica E4 + Time2Feel app, parents and children, 10 days | 10.3390/s23239470 | PMC10708754 | Yes, PMC | Feasibility, Acceptability, and Usability of Physiology and Emotion Monitoring in Adults and Children | 44 participants, 10 days | Empatica in children. Deployment detail unknown from abstract | medium |
| 54 | 2024-02-22 | WHOOP, emergency nurses and residents, 6 weeks | 10.2196/51569 | PMC10921319 | Yes, PMC | Investigating the Feasibility of Using a Wearable Device to Measure Physiologic Health Data in Emergency Nurses and Residents | 20 participants, acceptance, adoption and use assessed | WHOOP has few entries. Also in the device-side scan | medium |
| 55 | 2025-11-30 | Fitbit, Garmin or Polar (participant choice) + Smplicare app, 284 older adults | 10.1101/2025.11.27.25341162 | none | Yes, medRxiv | Identifying falls risk using wearables data in older adults, observational cohort | 266 (94%) gave 7+ days, 196 (76%) engaged on at least half of days | Multi-ecosystem BYOD in older adults, and Polar appears in a deployment. Preprint | high |
| 56 | 2025-01-15 | Oura, adolescents, N=103 | 10.48550/arxiv.2501.08851 | none | Yes, arXiv | Digital Phenotyping for Adolescent Mental Health, feasibility study employing machine learning | 34% and 75% figures, completion reported | Oura in adolescents. arXiv only | low |
| 57 | 2024-12-27 | App + wearable (unnamed), myasthenia gravis | 10.2196/58266 | none | Yes, JMIR | App- and Wearable-Based Remote Monitoring for Patients With Myasthenia Gravis, Feasibility and Usability | Adherence 74.3% to 97.9%, technical issues named | Device must be identified from Methods | medium |
| 58 | 2025-12-02 | Fitbit + MEMS + EMA, breast cancer survivors, N=20 | 10.1145/3770864 | PMC12711140 | Yes, PMC | Multimodal Sensing and Modeling of Endocrine Therapy Adherence in Breast Cancer Survivors (IMWUT) | Longitudinal multi-stream collection | Modelling paper. Deployment content probably thin | low |
| 59 | 2025-12-02 | Fitbit, N=300 | 10.1145/3770665 | none | ACM DL PDF listed as OA | Evaluating the Potential of Data-Driven Surveys for Fitness-Tracking Research (IMWUT) | 38% figure, completion | Fitbit data-driven survey engagement in an ACM venue | low |
| 60 | 2025-12-02 | Longitudinal sensing dataset, 29 and 88 participants | 10.1145/3770676 | none | ACM DL PDF listed as OA | LIFETRACE, A Longitudinal Multimodal Dataset on Daily Physical Activity, Well-Being, and Habits (IMWUT) | Completeness reported | Dataset paper. Device unnamed in abstract | low |
| 61 | 2025-12-02 | Longitudinal sensing, imputation | 10.1145/3770647 | none | ACM DL PDF listed as OA | Imputation Matters, An Overlooked Step in Longitudinal Health and Behavior Sensing Research (IMWUT) | Missingness handling across studies | Methods paper on missing data in sensing studies. Likely architecture or no-cohort, but relevant to the README's standardised-definitions gap | low |
| 62 | 2024-11-21 | EMA, adaptive survey length | 10.1145/3699735 | PMC11633767 | Yes, PMC | Ask Less, Learn More, Adapting EMA Survey Length by Modeling Question-Answer Information Gain (IMWUT) | Compliance figures 15% to 95% | EMA compliance engineering. Platform unnamed | low |
| 63 | 2024-05-11 | Fitbit, long COVID | 10.1145/3613904.3642827 | none | Yes, arXiv 2402.04937 | Charting the COVID Long Haul Experience, A Longitudinal Exploration of Symptoms, Activity, and Clinical Adherence (CHI) | Longitudinal, Fitbit named | Deployment reality unknown from abstract | low |
| 64 | 2024-03-06 | Mobile sensing, college | 10.1145/3643501 | none | ACM DL PDF listed as OA | Capturing the College Experience (IMWUT) | Completeness and compliance mentioned | Likely a custom app. Low priority | low |
| 65 | 2022-07-20 | Mobile sensing, 598 participants | 10.1145/3524886 | none | ACM DL PDF listed as OA | Leveraging Mobile Sensing and Bayesian Change Point Analysis to Monitor Community-scale Behavioral Interventions (ACM HEALTH) | 598 participants | Platform unnamed. 2022, so just inside the S2 window | low |
| 66 | 2024-08-01 | Oura, Garmin (4YouandMe cohorts) | see rank 22 | | | | | Consolidated into rank 22 | |

Rows 8, 11, 12, 20, 22, 23, 42, 48, 51, 52 and 54 also appear in the uncommitted `_device-side-scan-2026-09.md`. They are kept in this table because they also satisfy this strand's topic-first criteria, and the parent should de-duplicate when merging the two files.

### Lower-ranked survivors from Strand 1

These 70 or so passed the abstract screen but are intervention trials where the wearable is a delivery tool rather than the measured instrument, or their deployment content is a single completion figure. They are recorded so the weekly routine does not re-surface them as new. DOIs only, grouped by technology as named in the abstract.

Fitbit. 10.2196/56497, 10.2196/82494, 10.1007/s12529-025-10352-3, 10.2196/67108, 10.1016/j.ejon.2024.102649, 10.1093/tbm/ibaf033, 10.1186/s40814-024-01568-3, 10.1093/nop/npae048 (54 brain-tumour patients, 72% wore for the full 4 weeks, borderline for promotion), 10.2196/46418, 10.1093/ptj/pzad070, 10.2196/41221, 10.2196/59074 (pediatric pain, daily compliant wear tracked, borderline for promotion), 10.3390/ijerph21121667, 10.1158/2767-9764.crc-23-0519, 10.1123/pes.2022-0121, 10.1016/j.cct.2023.107318, 10.1097/ajp.0000000000001126, 10.1186/s40814-023-01312-3, 10.3389/fresc.2023.1225641, 10.1186/s12913-026-14066-4, 10.1016/j.psychsport.2026.103154, 10.3390/cancers16234084, 10.2196/86615, 10.1093/ptj/pzad096, 10.2196/65489, 10.1016/j.conctc.2024.101421, 10.1007/s10549-024-07432-5, 10.2147/nss.s497858, 10.1186/s40814-025-01622-8, 10.1186/s12911-024-02833-4, 10.21203/rs.3.rs-3833041/v1, 10.2217/nmt-2022-0028, 10.2196/79591, 10.2196/50135 (FEMFIT, 42 women, 12 weeks, retention reported, borderline), 10.1177/20552076241241244, 10.1186/s12966-023-01406-4, 10.2196/46149 (wear-time analysis across three datasets, methods paper), 10.1186/s40814-026-01865-z, 10.1177/20552076261435865, 10.2196/54595, 10.3389/fpain.2024.1340400, 10.2196/47356, 10.2196/55842, 10.1016/j.gerinurse.2025.103677, 10.1016/j.ygyno.2025.06.020, 10.1002/brb3.70600, 10.1158/2767-9764.crc-23-0148, 10.1093/geroni/igag011, 10.1007/s10865-023-00444-4 (ActiGraph waist, 271 young adults, wear time versus motivation).

Garmin. 10.1093/nop/npae093, 10.1016/j.yebeh.2026.111051, 10.2196/84838 (LETSGO, 378 survivors, 60% synchronised step data over 52 weeks, borderline for promotion), 10.21203/rs.3.rs-10475033/v1 and 10.12688/f1000research.161851.1 (Plymfit, perioperative Garmin, also in the device-side scan), 10.3390/s25030858, 10.21203/rs.3.rs-5159368/v1 (PCD-ENGAGE lessons learned, also in the device-side scan), 10.1371/journal.pdig.0000225 (Parkinson Garmin, also in the device-side scan).

Apple Watch. 10.64898/2026.04.28.26351917 (65 students, EMA engagement 88.7% to 49.2%, passive data from 95.4%, borderline for promotion), 10.1371/journal.pone.0293171, 10.2196/64083, 10.1007/s00403-025-03884-x, 10.2196/55552, 10.1200/cci.24.00040, 10.2196/50795, 10.2196/79639, 10.1177/17455057251361243, 10.1038/s41746-026-02817-w (OverSight iOS app, 25 enrolled, 92% retained at 12 months, app is custom so likely out of scope).

ActiGraph and GENEActiv. 10.1186/s40814-026-01898-4, 10.1186/s44167-026-00101-6 (pregnancy CentrePoint, also in the device-side scan), 10.1007/s12310-025-09767-w, 10.3390/audiolres15010005, 10.3389/fpubh.2024.1379582, 10.21203/rs.3.rs-7409582/v1, 10.1097/pcc.0000000000003657, 10.1016/j.pmedr.2025.103095, 10.1186/s12889-025-25497-9, 10.1123/jpah.2023-0511, 10.1080/02640414.2023.2300562, 10.1016/j.mhpa.2025.100748, 10.1249/mss.0000000000003301 (NHANES wear fatigue, N=13,649, also in the device-side scan), 10.1136/bmjopen-2025-107567, 10.3390/s24030880 (sling-wear algorithm, validation), 10.1159/000535283 (also in the device-side scan), 10.7717/peerj.16990, 10.3390/bioengineering12010018 (Mobilise-D sampling frequency, methods).

Oura. 10.3389/fdgth.2026.1744937 (229 enrolled, 108 provided EMA and Oura data, also in the device-side scan).

Empatica. 10.1016/j.dadr.2026.100457 (laboratory session, not a field deployment), 10.1016/j.actpsy.2026.107116.

mindLAMP. 10.2196/46491 (5 patients), 10.1016/j.scog.2025.100347 (design perspective), 10.1038/s44184-023-00023-0, 10.2196/39258, 10.1038/s41746-023-00977-7, 10.2196/58502 (quality-metrics pipeline, likely architecture).

Beiwe. 10.1038/s41598-024-56979-2 (Israel lockdown, Beiwe used only for daily surveys).

Avicenna. none beyond rank 7.

Polar. Appears only inside rank 55 and the HEARTLOC biofeedback feasibility papers (10.1177/27536351241227261, 10.1101/2023.09.09.23295208), where a Polar chest strap is the biofeedback instrument. Polar still has no deployment-reality study of its own.

---

## Unobtainable or no OA route

Every item below has no `oa_url`, no PMC deposit and no preprint found. They are recorded so the reason for not profiling them is on file.

| DOI | Title (shortened) | Barrier |
|---|---|---|
| 10.1145/3711043 | Participant Engagement and Data Quality, Lessons Learned from a Mental Wellness Crowdsensing Study | OpenAlex marks the ACM DL PDF as OA, but `_aware-build-report.md` records a challenge page. One browser attempt is warranted before this stays on the list |
| 10.1007/s12529-025-10433-3 | 4HAIE adherence predictors, 1,314 adults, 12 months | Springer paywall, no PMC, no preprint found |
| 10.1016/j.psychres.2023.115347 | EMA plus Fitbit acceptability, young adults at high suicide risk | Elsevier paywall. The companion JAMA Network Open paper (rank 13) is OA |
| 10.1093/sleep/zsae083 | Swiss narcolepsy cohort, Fitbit over 1 year | Oxford paywall |
| 10.1080/09602011.2026.2619548 | COPE-EMBRACE, EMA after encephalitis | Taylor and Francis paywall |
| 10.1080/09593985.2026.2618078 | Two adherence definitions compared, autism | Taylor and Francis paywall |
| 10.2196/91009 | Axivity in Parkinson inpatients with delirium | JMIR, not yet in PMC at scan time. Should appear in PMC on the journal's usual schedule |
| 10.1016/j.ejon.2024.102649, 10.1093/tbm/ibaf033, 10.1123/pes.2022-0121, 10.1097/ajp.0000000000001126, 10.1016/j.psychsport.2026.103154, 10.1016/j.yebeh.2026.111051, 10.2196/56497, 10.2196/84838, 10.1123/jpah.2023-0511, 10.1080/02640414.2023.2300562, 10.1016/j.gerinurse.2025.103677, 10.1016/j.ygyno.2025.06.020, 10.2217/nmt-2022-0028 | Lower-ranked survivors | No OA route found |

ACM-hosted items ranked 15, 59, 60, 61, 64 and 65 carry an `oa_url` on `dl.acm.org`, which this project has found to serve a challenge page to scripted requests. Treat them as obtainable only through a browser until proven otherwise.

---

## Grey literature (Strand 3), all lower confidence

### ClinicalTrials.gov posted results

Registry participant-flow data give enrolment and withdrawal counts but almost never a device-specific reason. Three registrations name the device or its data in a withdrawal reason and are the only ones worth a look.

| NCT | Term | Dates | N | What the registry says |
|---|---|---|---|---|
| NCT05659836 | Oura ring, Apple Watch | 2021-05 to 2023-06 | 28, 7 sites | Abbott spinal cord stimulation with Apple Watch and Oura ring. Withdrawal reasons include "Unable to operate wearable devices" (1), "Challenges following up with patient" (1), voluntary withdrawal (2), death (1). Industry-sponsored |
| NCT03335475 | Fitbit | 2017-11 to 2021-04 | 60 | Congenital heart disease physical activity lifestyle study. "Did not wear accelerometer" recorded as a withdrawal reason (4) |
| NCT03853148 | ActiGraph | 2019-02 to 2022-05 | 50 | Activate For Life, low-income older adults. Withdrawal reasons include incomplete questionnaires and missing data (5) |

Other registrations worth cross-referencing to their publications rather than profiling from the registry. NCT05176847 (Fitbit, 243, lost to follow-up 59 across arms), NCT04028843 (Fitbit, SmartMoms, 351, lost to follow-up 71), NCT03907891 (ActiGraph, 224, withdrawals 47 plus), NCT04616768 (Fitbit, PROStep, 108, feasibility trial using PROs and step data), NCT05417438 (Fitbit, Survivor mHealth, 31, "Assessing Feasibility of a Wearable"), NCT04379921 (Apple Watch, spine surgery, 255), NCT05159557 (Apple Watch, dementia caregivers, 63), NCT04464993 (Fitbit, StandUPTV, 110, baseline required 4+ days of server-verified device transmission), NCT03022032 (Beiwe plus Fitbit, HOPE and SMART, 102, already covered by the Panda and Wright PDFs in Module 2).

WHOOP, mindLAMP and "digital phenotyping smartphone" returned no completed trial with posted results. RADAR-base returned only false positives.

### Consortium output

RADAR-CNS. Beyond ranks 1, 28, 29 and 30 above, the following are RADAR-base outputs not in the baseline. 10.2196/45233 (Challenges in Using mHealth Data From Smartphones and Wearable Devices to Predict Depression Symptom Severity, 479 participants, engagement and missingness discussed, PMC10463088, OA). 10.2196/39479 (subjective experience of long-term RMT use, 99 participants, PMC9945920, OA, qualitative). 10.2196/43954 (data visualisation preferences, PMC11530729, OA, qualitative). 10.3390/ijerph20065161 (RADAR-MDD Catalonia during lockdown, PMC10048808, OA). 10.1155/da/1509978 (cognition and depression, 475 participants, PMC11918956, OA). 10.2196/55302 (seasonal circadian, 543 participants, 76.2% figure, PMC11245656, OA). 10.1186/s12888-024-05841-w (STORY eating-disorders protocol, protocol). 10.1186/s12888-025-07546-0 (ART-transition, protocol). 10.1371/journal.pone.0285807 (ethics committees and RMT, case study). 10.2196/41439 (Delphi). The last five are protocol, ethics or consensus papers and fall outside scope. 10.2196/45233 is the one most likely to carry deployment-reality figures.

Mobilise-D. 120 hits, none new for Module 3. The consortium's field device is the McRoberts MoveMonitor, which is not profiled in Module 1, so Mobilise-D deployments fall under the rule that a device not yet profiled is a Module 1 expansion candidate, not a Module 3 entry. The one methods paper that bears on this module's wear-time question is 10.1186/s12966-025-01851-3 (how many hours and days of real-world walking are needed, n up to 565, PMC12639672, OA), which is about analytic validity rather than deployment.

IDEA-FAST. 96 hits. Two are directly about deployment reality and are new. 10.3389/fdgth.2025.1569452 (Returning individual wearable sensor results to participants, perspectives on challenges and lessons learned, PMC11975874, OA) and 10.1093/gerona/glaf027 (pilot of returning results to 20 older adults, PMC12004365, OA). Two technology-acceptance papers from the IDEA-FAST feasibility study, 10.1177/20552076231181239 (PMC10286539) and 10.2196/70873 (PMC13173072), are qualitative. The IDEA-FAST device set includes consumer and research wearables that must be checked against Module 1 before any of these can count. 10.2196/91829 (post-COVID activity pacing, Fitbit, 18 participants, completion figures, PMC13263657) is IDEA-FAST-adjacent and small.

### Vendor case studies

Nothing retrievable by script. See the Strand 3 method note. A browser session against Oura Health, WHOOP Unite, Empatica, Garmin Health and ActiGraph pages is the only way to check whether any vendor publishes adherence or retention figures from customer deployments, and anything found there would be Reported at best and carry a commercial COI.

---

## Already known (where)

Hits that matched the reconciliation baseline. PDF matches are listed only where the title was hand-confirmed against the stored file.

| Date | DOI | Title (shortened) | Where |
|---|---|---|---|
| 2026-07-31 | 10.3390/ijerph23081003 | Move Toward Recovery, post-surgical PA feasibility | _recency-scan-2026-09.md |
| 2026-07-07 | 10.2196/86049 | Wearables for remote monitoring in psychosis, CONNECT | literature-index.json, profile connect-multi-wearable-psychosis, recency and citation-graph scans |
| 2026-05-12 | 10.1186/s40814-026-01830-w | Early interval training after heart valve surgery | _recency-scan-2026-09.md |
| 2026-04-27 | 10.2196/84618 | Passive network traffic phenotyping | literature-index.json, profile vpn-network-traffic-phenotyping |
| 2026-02-22 | 10.1038/s41598-026-41435-0 | LINC framework | literature-index.json, stored PDF 2026-calvert |
| 2026-02-06 | 10.2196/78098 | Samsung palliative pain, Ecuador | literature-index.json, profile samsung-palliative-pain-ecuador |
| 2026-01-28 | 10.1093/geroni/igag007 | Multimodal passive sensing in older adults | literature-index.json, stored PDF 2026-shen |
| 2025-12-29 | 10.2196/69749 | Digital tools for youth mental health, Colombia | _citation-graph-scan-2026-09.md |
| 2025-11-27 | 10.1038/s41537-025-00660-8 | Mobile cognitive remote assessment, global multisite | literature-index.json, stored PDF 2025-castillo |
| 2025-09-08 | 10.1016/j.inpsyc.2025.100123 | Usability barriers, older adults, mindLAMP | _citation-graph-scan-2026-09.md |
| 2025-09-03 | 10.2196/71375 | Psychological well-being via Beiwe, intensive longitudinal | _onnela-module3-candidates.md, literature-index.json, stored PDF 2025-yi |
| 2025-07-01 | 10.1371/journal.pdig.0000883 | Adolescent long-term phenotyping design and feasibility | _onnela-module3-candidates.md, literature-index.json, stored PDF 2025-huang |
| 2025-06-23 | 10.2196/71377 | Linking phenotyping, clinical and genetics data | _citation-graph-scan-2026-09.md |
| 2025-06-03 | 10.2196/67964 | Multimodal passive sensing, college depression | literature-index.json, stored PDF 2025-borelli |
| 2025-05-15 | 10.1016/j.invent.2025.100833 | Next-day negative emotion, BDD | literature-index.json, stored PDF 2025-weingarden |
| 2025-03-01 | 10.1111/eip.70018 | Physical activity and symptoms, young people with MDD (AWARE-Light) | profile aware-light-smartsense-d-youth-depression |
| 2025-02-21 | 10.2196/63622 | Multimodal phenotyping in major depressive episodes | literature-index.json, profile aware-momo-mood |
| 2025-02-19 | 10.2196/57512 | Nomophobia and smartphone-inferred behaviours | profile aware-light-smartsense-d-youth-depression |
| 2025-02-07 | 10.2196/59161 | GPS patterns and quality of life, advanced cancer | _recency-scan-2026-09.md |
| 2025-01-16 | 10.1053/j.gastro.2024.12.024 | Wearables predict IBD flares | literature-index.json, stored PDF 2025-hirten |
| 2025-01-04 | 10.3390/cancers17010139 | DANO neuro-oncology pilot | stored PDF 2025-siddi |
| 2025-01-02 | 10.1200/cci-24-00201 | Passive smartphone data feasibility, oncology | _citation-graph-scan-2026-09.md |
| 2025-01-01 | 10.1177/20552076251330509 | SmartSense-D pilot | literature-index.json, stored PDF 2025-camargo |
| 2025-01-01 | 10.1093/milmed/usae144 | Passive smartphone data, military | _citation-graph-scan-2026-09.md |
| 2024-11-22 | 10.2196/59974 | Mobility phenotypes, everyday cognition | _citation-graph-scan-2026-09.md |
| 2024-10-23 | 10.2196/51259 | Remote monitoring through RADAR-base | stored PDF 2024-rashid, Module 2 literature library |
| 2024-10-18 | 10.1007/s41347-024-00443-5 | Adolescent social media science challenges | _citation-graph-scan-2026-09.md |
| 2024-10-11 | 10.2196/55170 | Environmental and behavioural drivers of chronic disease | _onnela-module3-candidates.md, literature-index.json, stored PDF 2024-yi |
| 2024-10-11 | 10.2196/57439 | Screen time in people with suicidal thoughts | stored PDF 2024-karas-jmirmhealthuhealth |
| 2024-09-12 | 10.1186/s44247-024-00116-6 | Beiwe feasibility and tolerability, type 2 diabetes | literature-index.json, stored PDF 2024-mcinerney |
| 2024-07-24 | 10.1038/s44277-024-00013-w | Social connectivity markers, schizophrenia and bipolar | literature-index.json, stored PDF 2024-valeri |
| 2024-05-30 | 10.1002/acn3.52050 | ALS progression from passive smartphone data | literature-index.json, stored PDF 2024-karas-annclintranslneurol |
| 2024-04-04 | 10.1089/tmj.2024.0023 | Digital Navigator | _citation-graph-scan-2026-09.md |
| 2024-03-02 | 10.1016/j.ebiom.2024.105036 | Upper limb movements in ALS | literature-index.json, stored PDF 2024-straczkiewicz |
| 2024-02-02 | 10.3389/fpain.2024.1327859 | Pain Intervention and Digital Research operational report | _onnela-module3-candidates.md, literature-index.json, stored PDF 2024-fu |
| 2023-12-29 | 10.2196/47006 | Digital phenotyping for mood disorders, pilot | _citation-graph-scan-2026-09.md |
| 2023-12-07 | 10.1097/hc9.0000000000000329 | Alcohol craving from smartphone sensors, liver disease | literature-index.json, stored PDF 2023-wu |
| 2023-10-18 | 10.3389/fdgth.2023.1182175 | m-Path platform paper | stored PDF 2023-mestdagh |
| 2023-09-16 | 10.7759/cureus.45362 | Oura adherence, TemPredict | literature-index.json, stored PDF 2023-shiba |
| 2023-09-01 | 10.2196/40197 | Phenotyping biomarkers and treatment | _citation-graph-scan-2026-09.md |
| 2023-03-07 | 10.2196/43296 | m-Path Sense performance study | literature-index.json, stored PDF 2023-niemeijer |
| 2023-03-06 | 10.1038/s41746-023-00778-y | Wearable and smartphone data quantify ALS | _onnela-module3-candidates.md, literature-index.json, stored PDF 2023-johnson |
| 2023-02-17 | 10.1038/s41746-023-00749-3 | RADAR-MDD long-term retention | literature-index.json, stored PDF 2023-zhang |
| 2023-01-27 | 10.1038/s41537-023-00332-5 | mindLAMP relapse prediction, three sites | literature-index.json, profile mindlamp-relapse-3site |
| 2023-01-24 | 10.2196/42866 | RMT in psychological treatment | literature-index.json, profile radar-base-treatment-engagement |
| 2025-10-03 | 10.2196/71145 | Dual in-person and remote autism endpoints (RADAR-base) | _recency-scan-2026-09.md, _recency-build-report.md |
| 2024-01-01 | 10.1177/20552076241238133 | RADAR-AD feasibility and usability | literature-index.json, profile radar-ad-feasibility-usability |

Also surfaced by the parallel, uncommitted `_device-side-scan-2026-09.md` (20 Strand 1 survivors). 10.2196/68645, 10.2196/69952, 10.2196/91009, 10.1371/journal.pdig.0000517, 10.1177/20552076241288754, 10.1186/s44167-026-00101-6, 10.2196/54630, 10.1016/j.earlhumdev.2023.105814, 10.1371/journal.pdig.0000225, 10.2196/76167, 10.2196/57827, 10.21203/rs.3.rs-10475033/v1, 10.1177/27536351241227261, 10.1159/000535283, 10.64898/2026.07.30.26359360, 10.21203/rs.3.rs-5159368/v1, 10.3389/fdgth.2026.1744937, 10.12688/f1000research.161851.1, 10.2196/51569, 10.1249/mss.0000000000003301. Eleven of them are retained in the ranked table above with a note.

---

## What this pass changes about the module's picture

1. Topic-first search found deployment-reality papers for RADAR-base (an engagement RCT), mindLAMP (a 1,178-participant missingness analysis), Avicenna (a rural South African GPS feasibility study), LifeData (a cross-border recruitment and fraud lessons-learned paper), MetricWire (one small usability study) and m-Path (three EMA deployments) that no platform-name pass surfaced. The platform-name queries in this same pass returned between 1 and 21 hits each, so the topic-first route is the productive one.
2. LMIC coverage moved from one country (India, via mindLAMP) to candidates in South Africa, Uganda and Kenya. All three need full-text confirmation of the device or platform.
3. The Beiwe versus mindLAMP versus RADAR-base head-to-head is still absent from the literature as far as any query here can tell.
4. Two Beiwe deployments with collection windows in 2024 were found (ranks 25 and 26). If either reports completeness, it would be the module's first post-heartbeat Beiwe figure.
5. ACM venues hold engagement and missingness work at a scale the biomedical indexes do not (12-month, 177-participant and 246-participant EMA engagement studies), but most of it uses custom apps and would be Module 2 expansion candidates rather than Module 3 entries. The one AWARE-labelled ACM paper is still the unobtainable 10.1145/3711043.
6. ClinicalTrials.gov is a weak source for device-specific attrition. Three registrations out of 406 record a device-related withdrawal reason.
7. Two structural findings for the discovery method. OpenAlex ignores phrase quoting for AWARE exactly as Europe PMC does, so the name-null rule applies to both indexes. And the PDF-filename reconciliation used here (year plus surname) produced false matches for common surnames (Wang, Li, Huang, Johnson, Lee), which is why PDF matches were hand-checked. A DOI field in the PDF ledger would remove that step.
