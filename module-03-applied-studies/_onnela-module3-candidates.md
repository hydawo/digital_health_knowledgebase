# Onnela Lab — Module 3 candidate triage

**Written 2026-08-31 by the Onnela-publications cataloguing pass. This is a handoff list, not a
module artifact.** It is the only file that pass created in `module-03-applied-studies/`; no profile,
README, or index here was created or modified. Convert or delete as you see fit.

## Where it came from

The Onnela Lab publications page (<https://hsph.harvard.edu/research/onnela-lab/papers/>) lists 114
entries under its "Digital Health and Phenotyping" heading — 113 distinct papers (one is listed
twice). All 113 now have a catalog entry in exactly one module:

- **91 in** [`../module-02-digital-phenotyping/literature-library.md`](../module-02-digital-phenotyping/literature-library.md)
- **22 in** [`../module-01-wearables/literature-library.md`](../module-01-wearables/literature-library.md)

The 27 below are the subset that read as **real research deployments reporting how the deployment
went** — recruitment, retention, adherence, wear time, data completeness, or technical failure modes.
Each already carries a "Module 3 candidate" forward pointer in its catalog row. Methods and
architecture papers (GPS imputation, activity recognition, walking detection, platform description,
statistical methodology) were deliberately **excluded** — they stay catalog-only.

**Already claimed by the Module 3 build and therefore excluded from this list** (still catalogued in
Module 2): `10.2196/31877`, `10.1371/journal.pdig.0000883`, `10.2196/55170`,
`10.1038/s41598-021-94516-7`, `10.1093/biostatistics/kxy059`, `10.1093/jamia/ocab069`. The
inpatient suicidal-thinking pilot `10.1001/jamanetworkopen.2021.0591` does not appear on the lab's
Digital Health & Phenotyping list at all.

**Ranking** is by how much operational detail the abstract actually carries, strongest first. Ranking
was done from Europe PMC abstracts only — none of these full texts were read for operational figures
in this pass, so treat every number below as **Reported** pending your own full-text extraction. Where
a PDF is already on disk, the path is given.

---

### 1. Mercier HW et al., *American journal of physical medicine & rehabilitation* 2020 — "Digital phenotyping to quantify psychosocial well-being trajectories after spinal cord injury"

- **DOI / PMCID:** `10.1097/phm.0000000000001506` / `PMC7680265`
- **Catalog home:** Module 2 (`L083`)
- **Technologies deployed:** Beiwe (smartphone GPS + weekly surveys)
- **Sample size:** 43 enrolled, community-living wheelchair users with spinal cord injury
- **Duration:** 4 months, weekly measurement
- **Operational facts reported:** **Retention broken out by incentive arm — 78% with financial incentive vs. a lower rate without.** Reports enrollment, retention, and participation burden explicitly. The single richest retention comparison in the set.
- **Local PDF:** **PDF not obtained** (PMC route served HTML)

### 2. Johnson SA et al., *NPJ digital medicine* 2023 — "Wearable device and smartphone data quantify ALS progression and may provide novel outcome measures"

- **DOI / PMCID:** `10.1038/s41746-023-00778-y` / `PMC9987377`
- **Catalog home:** Module 1 (`L056`)
- **Technologies deployed:** Beiwe (surveys) + ActiGraph Insight Watch (wrist) / Modus StepWatch (ankle)
- **Sample size:** 40 ambulatory adults with ALS
- **Duration:** 6 months
- **Operational facts reported:** Reports **both** wearable wear compliance and app survey compliance side by side ("adequate"), across two different wearable form factors. Rare dual-modality adherence reporting.
- **Local PDF:** module-01-wearables/literature/research-accelerometers/2023-johnson-npjdigitalmedicine-wearable-device-smartphone-data-quantify-als.pdf

### 3. Yi L et al., *JMIR mHealth and uHealth* 2025 — "Measuring psychological well-being and behaviors using smartphone-based digital phenotyping: An intensive longitudinal observational mHealth pilot study embedded in a prospective cohort of women"

- **DOI / PMCID:** `10.2196/71375` / `PMC12407220`
- **Catalog home:** Module 2 (`L023`)
- **Technologies deployed:** Beiwe (EMA 2x/day + minute-level accelerometer and GPS), inside Nurses' Health Study II
- **Sample size:** 181 participants
- **Duration:** 8-day intensive protocol
- **Operational facts reported:** Purpose-built **feasibility** study: adherence to the EMA schedule, passive-data completeness, and an end-of-study participant feedback survey on the app experience. Directly answers "what does an 8-day Beiwe burst actually yield in an established cohort".
- **Local PDF:** module-02-digital-phenotyping/literature/beiwe/2025-yi-jmirmhealthuhealth-measuring-psychological-well-being-behaviors-smartphone-based-digital.pdf

### 4. Fu M et al., *Frontiers in pain research (Lausanne, Switzerland)* 2024 — "Pain intervention and digital research: An operational report on combining digital research and outpatient chronic disease management"

- **DOI / PMCID:** `10.3389/fpain.2024.1327859` / `PMC10869590`
- **Catalog home:** Module 2 (`L046`)
- **Technologies deployed:** Beiwe (passive smartphone) embedded in an outpatient pain clinic
- **Sample size:** 77 participants
- **Duration:** Ongoing program launched 2022
- **Operational facts reported:** Self-described **"operational report"** — recruitment mechanics of running digital research inside routine clinical care, with an older, comorbid, access-limited population. Operational content is the point of the paper.
- **Local PDF:** module-02-digital-phenotyping/literature/beiwe/2024-fu-frontierspainresearchlau-pain-intervention-digital-research-operational-report.pdf

### 5. Straczkiewicz M et al., *Journal of neuroengineering and rehabilitation* 2026 — "Short prescribed exercises can quantify upper limb functioning in neurodegenerative disease"

- **DOI / PMCID:** `10.1186/s12984-025-01829-z` / `PMC12825179`
- **Catalog home:** Module 1 (`L007`)
- **Technologies deployed:** Wrist-worn accelerometers, prescribed at-home exercise episodes
- **Sample size:** 329 individuals with ALS
- **Duration:** Longitudinal, repeated short episodes
- **Operational facts reported:** Frames itself against the **adherence-over-long-wear-time problem**: reports enrollment, participant adherence, and explicitly compares short-episode against free-living metrics that "require substantial wear time".
- **Local PDF:** module-01-wearables/literature/research-accelerometers/2026-straczkiewicz-jneuroengrehabil-short-prescribed-exercises-can-quantify-upper.pdf

### 6. Straczkiewicz M et al., *Journal of neuroengineering and rehabilitation* 2024 — "Free-living monitoring of ALS progression in upper limbs using wearable accelerometers"

- **DOI / PMCID:** `10.1186/s12984-024-01514-7` / `PMC11662782`
- **Catalog home:** Module 1 (`L029`)
- **Technologies deployed:** Wrist-worn accelerometers (dominant + non-dominant)
- **Sample size:** 202 patients with ALS
- **Duration:** One week of wear every 2–4 weeks, longitudinal
- **Operational facts reported:** Large-cohort **wear-time** reporting; the paper exists specifically to test whether pilot-scale findings generalize and reproduce at scale.
- **Local PDF:** module-01-wearables/literature/research-accelerometers/2024-straczkiewicz-jneuroengrehabil-free-living-monitoring-als-progression-upper-limbs.pdf

### 7. van den Berg L et al., *Quality of life research : an international journal of quality of life aspects of treatment, care and rehabilitation* 2022 — "Feasibility and performance of smartphone-based daily micro-surveys among patients recovering from cancer surgery"

- **DOI / PMCID:** `10.1007/s11136-021-02934-x` / no PMCID
- **Catalog home:** Module 2 (`L075`)
- **Technologies deployed:** Smartphone app delivering daily SF-36 micro-surveys
- **Sample size:** 95 patients who downloaded the app
- **Duration:** Mean 131 days (SD 85), 2017–2019
- **Operational facts reported:** **Response and completion rates quantified and compared** (76% for full-length SF-36 vs. micro-surveys), plus agreement analysis. Direct evidence on survey-burden design tradeoffs.
- **Local PDF:** **PDF not obtained** (no OA source)

### 8. Wright AA et al., *JCO clinical cancer informatics* 2018 — "The HOPE pilot study: Harnessing patient-reported outcomes and biometric data to enhance cancer care"

- **DOI / PMCID:** `10.1200/cci.17.00149` / `PMC6556148`
- **Catalog home:** Module 2 (`L104`)
- **Technologies deployed:** Beiwe (PROs) + wearable accelerometers
- **Sample size:** 10 patients with gynecologic cancer on palliative chemotherapy
- **Duration:** Pilot intervention
- **Operational facts reported:** **Approach-to-consent rate 100%; adherence 90% / 70%** to the two components. Small N but unusually explicit enrollment and adherence funnel.
- **Local PDF:** module-02-digital-phenotyping/literature/beiwe/2018-wright-jcoccinformatics-hope-pilot-study-harnessing-patient-reported-outcomes.pdf

### 9. Lee MS et al., *BMC public health* 2024 — "Vaping habits and respiratory symptoms using a smartphone app platform"

- **DOI / PMCID:** `10.1186/s12889-024-19439-0` / `PMC11289986`
- **Catalog home:** Module 2 (`L034`)
- **Technologies deployed:** Custom smartphone app platform, population-based
- **Sample size:** 306 adults across the US
- **Duration:** 8-day survey participation window per participant, Aug 2020–Mar 2021
- **Operational facts reported:** Population-based recruitment at distance with a fixed per-participant participation window; reports participation structure across daily/weekly/monthly instruments.
- **Local PDF:** module-02-digital-phenotyping/literature/vaping-health-study-app/2024-lee-bmcpublichealth-vaping-habits-respiratory-symptoms-smartphone-app.pdf

### 10. Karas M et al., *Annals of clinical and translational neurology* 2024 — "Tracking ALS disease progression using passively collected smartphone sensor data"

- **DOI / PMCID:** `10.1002/acn3.52050` / `PMC11187949`
- **Catalog home:** Module 2 (`L041`)
- **Technologies deployed:** Beiwe (accelerometer + GPS) with self-entry ALSFRS-R
- **Sample size:** 63 people with ALS
- **Duration:** Longitudinal
- **Operational facts reported:** Enrollment reported; passive sensor data used to derive step counts, so data yield is load-bearing for the result.
- **Local PDF:** module-02-digital-phenotyping/literature/beiwe/2024-karas-annclintranslneurol-tracking-als-disease-progression-passively-collected.pdf

### 11. Pellegrini AM et al., *Brain and behavior* 2022 — "Estimating longitudinal depressive symptoms from smartphone data in a transdiagnostic cohort"

- **DOI / PMCID:** `10.1002/brb3.2077` / `PMC8865149`
- **Catalog home:** Module 2 (`L079`)
- **Technologies deployed:** Beiwe (GPS + accelerometer) + weekly PHQ-8 + biweekly rater MADRS
- **Sample size:** 45 individuals across 4 diagnostic groups
- **Duration:** 8 weeks
- **Operational facts reported:** Enrollment by diagnostic group; a transdiagnostic design where per-group data yield matters.
- **Local PDF:** module-02-digital-phenotyping/literature/beiwe/2022-pellegrini-brainbehav-estimating-longitudinal-depressive-symptoms-smartphone-data.pdf

### 12. Cote DJ et al., *World neurosurgery* 2019 — "Digital phenotyping in patients with spine disease: A novel approach to"

- **DOI / PMCID:** `10.1016/j.wneu.2019.01.297` / `PMC6706326`
- **Catalog home:** Module 2 (`L098`)
- **Technologies deployed:** Beiwe (GPS, WiFi, accelerometer, call/text logs, screen state) + daily VAS pain
- **Sample size:** 105 patients enrolled (55 analyzed)
- **Duration:** Longitudinal, clinic-recruited
- **Operational facts reported:** **Enrolled-vs-analyzed gap is stated (105 → 55)** — one of the clearest attrition signals in the set. Also enumerates the full passive stream set collected.
- **Local PDF:** **PDF not obtained** (PMC route served HTML)

### 13. Panda N et al., *JAMA surgery* 2020 — "Utilizing smartphones to capture novel recovery metrics after cancer surgery"

- **DOI / PMCID:** `10.1001/jamasurg.2019.4702` / `PMC6820047`
- **Catalog home:** Module 2 (`L093`)
- **Technologies deployed:** Beiwe (smartphone accelerometer)
- **Sample size:** 139 individuals, prospective observational
- **Duration:** Jul 2017 – Apr 2019, single academic centre
- **Operational facts reported:** Prospective surgical cohort with a documented approach/enrollment process; postoperative data continuity is the analytic substrate.
- **Local PDF:** **PDF not obtained** (PMC route served HTML)

### 14. Panda N et al., *Annals of surgery* 2022 — "Smartphone-based assessment of preoperative decision conflict and postoperative physical activity among patients undergoing cancer surgery: a prospective cohort study"

- **DOI / PMCID:** `10.1097/sla.0000000000004487` / no PMCID
- **Catalog home:** Module 2 (`L087`)
- **Technologies deployed:** Beiwe (Decision Conflict Scale delivery + accelerometer)
- **Sample size:** 99 patients undergoing cancer surgery
- **Duration:** Jul 2017–2019
- **Operational facts reported:** Reports enrollment and participation for an app-delivered instrument in a surgical population.
- **Local PDF:** **PDF not obtained** (no OA source)

### 15. Straczkiewicz M et al., *Psychiatry research* 2022 — "Combining digital pill and smartphone data to quantify medication adherence in an observational psychiatric pilot study"

- **DOI / PMCID:** `10.1016/j.psychres.2022.114707` / no PMCID
- **Catalog home:** Module 2 (`L062`)
- **Technologies deployed:** Beiwe digital phenotyping + FDA-approved digital pill (ingestible-sensor) system
- **Sample size:** 24 individuals with serious mental illness
- **Duration:** 5 months
- **Operational facts reported:** Explicit **feasibility + data-quality** framing: concludes "a focus on data quality" is the necessary next step. Also the only multi-device (digital pill) deployment in the set.
- **Local PDF:** **PDF not obtained** (no OA source)

### 16. Soon CS et al., *Sleep* 2025 — "A longitudinal study of sleep in university freshmen: facilitating and impeding factors"

- **DOI / PMCID:** `10.1093/sleep/zsaf156` / `PMC12515602`
- **Catalog home:** Module 1 (`L022`)
- **Technologies deployed:** Oura Ring 3 + smartphone time-use app — **Module 1 catalog home**
- **Sample size:** 638 university freshmen
- **Duration:** 20-week semester; 64,642 nights of sleep data
- **Operational facts reported:** Very large per-participant data yield stated outright; a rare consumer-ring longitudinal deployment at cohort scale.
- **Local PDF:** module-01-wearables/literature/oura/2025-soon-sleep-longitudinal-study-sleep-university-freshmen-facilitating.pdf

### 17. Vidal Bustamante CM et al., *JMIR formative research* 2024 — "Precision assessment of real-world associations between stress and sleep duration using actigraphy data collected continuously for an academic year: individual-level modeling study"

- **DOI / PMCID:** `10.2196/53441` / `PMC11094608`
- **Catalog home:** Module 2 (`L039`)
- **Technologies deployed:** Beiwe (daily self-report) + actigraphy
- **Sample size:** 55 college students
- **Duration:** Intensive longitudinal
- **Operational facts reported:** Person-specific modelling that depends on dense per-individual data; reports cohort composition.
- **Local PDF:** module-02-digital-phenotyping/literature/beiwe/2024-vidal-jmirformativeres-precision-assessment-real-world-associations-between-stress.pdf

### 18. Boaro A et al., *Journal of neurosurgery. Spine* 2021 — "Smartphone GPS signatures of patients undergoing spine surgery correlate with mobility and current gold standard outcome measures"

- **DOI / PMCID:** `10.3171/2021.2.spine202181` / `PMC9012532`
- **Catalog home:** Module 2 (`L078`)
- **Technologies deployed:** Beiwe (smartphone GPS only)
- **Sample size:** 39 patients undergoing spine surgery
- **Duration:** Perioperative period
- **Operational facts reported:** Eight daily GPS-derived mobility features across a perioperative window; GPS continuity is the operational risk.
- **Local PDF:** **PDF not obtained** (PMC route served HTML)

### 19. Liu G et al., *Schizophrenia research. Cognition* 2019 — "Assessing the potential of longitudinal smartphone-based cognitive assessment in schizophrenia: A naturalistic pilot study"

- **DOI / PMCID:** `10.1016/j.scog.2019.100144` / `PMC6476810`
- **Catalog home:** Module 2 (`L096`)
- **Technologies deployed:** Smartphone cognitive assessments + sensors (steps, sleep) + self-report
- **Sample size:** 18 with schizophrenia + 17 healthy controls
- **Duration:** 12 weeks
- **Operational facts reported:** **Explicitly states no payment or incentive was offered** — a directly comparable counterpoint to the incentive/retention finding in the SCI study above.
- **Local PDF:** module-02-digital-phenotyping/literature/mindlamp/2019-liu-schizophrresconn-assessing-potential-longitudinal-smartphone-based-cognitive-assessment.pdf

### 20. Staples P et al., *NPJ schizophrenia* 2017 — "A comparison of passive and active estimates of sleep in a cohort with schizophrenia"

- **DOI / PMCID:** `10.1038/s41537-017-0038-0` / `PMC5643440`
- **Catalog home:** Module 2 (`L108`)
- **Technologies deployed:** Beiwe (accelerometer, GPS, screen state) + tri-weekly EMA
- **Sample size:** 17 subjects with schizophrenia
- **Duration:** 3 months
- **Operational facts reported:** Early Beiwe deployment; compares passive vs. active sleep estimates, so passive-data completeness is load-bearing.
- **Local PDF:** module-02-digital-phenotyping/literature/beiwe/2017-staples-npjschizophrenia-comparison-passive-active-estimates-sleep-cohort.pdf

### 21. Torous J et al., *JMIR mental health* 2015 — "Utilizing a personal smartphone custom app to assess the Patient Health Questionnaire-9 (PHQ-9) depressive symptoms in patients with major depressive disorder"

- **DOI / PMCID:** `10.2196/mental.3889` / `PMC4607379`
- **Catalog home:** Module 2 (`L114`)
- **Technologies deployed:** Custom smartphone app (Mindful Moods), pre-Beiwe
- **Sample size:** 13 outpatients with major depressive disorder
- **Duration:** 29–30 days, up to 3 sessions/day
- **Operational facts reported:** **Adherence is the stated primary outcome.** The earliest deployment in the lab record; useful as a historical baseline.
- **Local PDF:** module-02-digital-phenotyping/literature/mindful-moods/2015-torous-jmirmentalhealth-utilizing-personal-smartphone-custom-app-assess.pdf

### 22. Beukenhorst AL et al., *Muscle & nerve* 2021 — "Smartphone data during the COVID‐19 pandemic can quantify behavioral changes in people with ALS"

- **DOI / PMCID:** `10.1002/mus.27110` / `PMC7898508`
- **Catalog home:** Module 2 (`L082`)
- **Technologies deployed:** Beiwe (passive location only)
- **Sample size:** 8 participants with ALS
- **Duration:** Across the March 2020 US state-of-emergency declaration
- **Operational facts reported:** Tiny N, but a natural-experiment design where continuous passive location capture through a disruption is itself the operational finding.
- **Local PDF:** module-02-digital-phenotyping/literature/beiwe/2021-beukenhorst-musclenerve-smartphone-data-during-covid19-pandemic-can.pdf

### 23. Nawabi NLA et al., *Neurosurgery* 2025 — "Assessing mobility in patients with glioblastoma using digital phenotyping – Piloting the digital assessment in neuro-oncology"

- **DOI / PMCID:** `10.1227/neu.0000000000003051` / no PMCID
- **Catalog home:** Module 2 (`L040`)
- **Technologies deployed:** Beiwe (passive smartphone GPS)
- **Sample size:** 15 patients with glioblastoma
- **Duration:** Pre-op, immediate post-op, late post-op
- **Operational facts reported:** Small enrolled cohort with a stated comparison group; pilot-scale operational signal only.
- **Local PDF:** **PDF not obtained** (no OA source)

### 24. Duey AH et al., *Neurosurgery* 2023 — "Daily pain prediction using smartphone speech recordings of patients with spine disease"

- **DOI / PMCID:** `10.1227/neu.0000000000002474` / no PMCID
- **Catalog home:** Module 2 (`L048`)
- **Technologies deployed:** Beiwe (at-home pain surveys + smartphone speech recordings)
- **Sample size:** 60 patients enrolled, 384 observations
- **Duration:** Regular intervals, clinic-recruited
- **Operational facts reported:** Observation count relative to enrollment is stated — a usable yield-per-participant figure. Also the only **audio/speech** collection deployment in the set.
- **Local PDF:** **PDF not obtained** (no OA source)

### 25. Chung Y et al., *Translational psychiatry* 2026 — "Ecological assessment of transdiagnostic clinical symptoms in serious mental illness with daily smartphone surveys"

- **DOI / PMCID:** `10.1038/s41398-026-04218-9` / no PMCID
- **Catalog home:** Module 2 (`L006`)
- **Technologies deployed:** Smartphone daily surveys (serious mental illness outpatients)
- **Sample size:** 56 outpatients
- **Duration:** One year or longer; 3,901 daily surveys + 423 clinical assessments
- **Operational facts reported:** Survey-count-per-participant over a year-plus is stated outright; long-horizon adherence evidence.
- **Local PDF:** **PDF not obtained** (no OA source)

### 26. Nock MK et al., *Journal of psychopathology and clinical science* 2026 — "Using smartphone surveys to predict next-week suicide attempts"

- **DOI / PMCID:** `10.1037/abn0001117` / `PMC13308188`
- **Catalog home:** Module 2 (`L008`)
- **Technologies deployed:** Smartphone surveys 6x/day + passively collected survey metadata
- **Sample size:** 619 patients presenting with suicidal thoughts/behavior
- **Duration:** 3 months; 79,448 survey responses
- **Operational facts reported:** **Largest deployment in the set by participant count.** Survey metadata (e.g. time since last submission) is used as a predictor, which makes response timing an explicit operational variable.
- **Local PDF:** module-02-digital-phenotyping/literature/lifedata/2026-nock-jpsychopatholclinsci-smartphone-surveys-predict-next-week-suicide-attempts.pdf

### 27. Mahalingaiah S et al., *American journal of obstetrics and gynecology* 2022 — "Design and methods of the Apple Women’s Health Study: a digital longitudinal cohort study"

- **DOI / PMCID:** `10.1016/j.ajog.2021.09.041` / `PMC10518829`
- **Catalog home:** Module 1 (`L069`)
- **Technologies deployed:** Apple Research app / Apple Women's Health Study — **Module 1 catalog home**
- **Sample size:** Cohort-scale (tens of thousands)
- **Duration:** Ongoing longitudinal digital cohort
- **Operational facts reported:** Design-and-methods paper reporting enrollment and follow-up architecture for a very large consumer-ecosystem digital cohort. Already in the KB as a Module 1 PDF.
- **Local PDF:** module-01-wearables/literature/apple-watch/2022-mahalingaiah-ajog-apple-womens-health-study-design.pdf

---

## Judgment calls worth knowing about

- **#16 (Soon et al., Oura Ring 3 freshmen) and #27 (Apple Women's Health Study design)** are the two
  candidates whose **catalog home is Module 1, not Module 2**. They are listed here anyway because
  they are genuine deployments with operational content; the catalog/Module-3 split is orthogonal to
  which module holds the citation.
- **#2 (Karas/Berry, npj Digital Medicine 2023)** runs on Beiwe *and* ActiGraph/Modus simultaneously.
  It is catalogued in Module 1 on the wearable, but it is arguably the most Beiwe-relevant deployment
  paper in the whole set — worth a Module 3 profile regardless of where its citation sits.
- **Small-N pilots (#22 glioblastoma, N=15; #21 ALS COVID, N=8; #8 HOPE, N=10)** are included because
  they report clean enrollment/adherence funnels, not because they are large. Drop them if Module 3 is
  meant to carry only substantial deployments.
- **#20 (Torous 2015 Mindful Moods)** predates Beiwe and uses a custom app. Included as a historical
  adherence baseline; exclude if Module 3 is scoped to platform deployments only.

## What was not assessed

No full text was read for operational figures. Several candidates' PDFs could not be obtained at all
(marked above) — chiefly *Annals of Surgery*, *Neurosurgery*, *Psychiatry Research*, *Quality of Life
Research*, and the JAMA-family articles, where Europe PMC's render service returned HTTP 500 or the
PMC route served HTML instead of a PDF. Those will need another retrieval route before their
operational detail can be extracted.
