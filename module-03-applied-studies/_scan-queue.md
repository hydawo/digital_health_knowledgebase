# Module 3 — Weekly scan queue

**Append-only.** The automated weekly literature-scan routine adds candidates here; a
human-initiated session reads full texts, builds profiles, and removes entries it has resolved.

**The routine does not write profiles.** See
[`../shared/weekly-literature-scan.md`](../shared/weekly-literature-scan.md) for why: Module 3
asserts what happened in a deployment, which cannot be established from an abstract. Abstract-level
screening in this project has a measured platform-misattribution rate of roughly **3 in 12**.

**Every entry below is `Reported` until its full text has been read.** In particular, the
"technology" column records what the *search* suggests, not what the study actually deployed.

## How to work this queue

1. Retrieve full text (Europe PMC `fullTextXML`, `?pdf=render`, or NCBI `efetch`; `pdftotext -layout`
   for tables).
2. **Verify from Methods which platform/device was actually deployed.** If it is not what the queue
   says, correct it and say so.
3. Verify the first author from the full text or publisher PDF byline — **not** search metadata.
   PMC's JATS `contrib-group` for JMIR articles orders editors and authors inconsistently.
4. Build the profile, or record a rejection with its reason in
   [`literature-index.json`](literature-index.json)'s `rejected` array.
5. Remove the entry from this queue.

---

## Pending

| Found | DOI | PMCID | Title | Venue / year | Apparent technology | Signals | OA |
|---|---|---|---|---|---|---|---|
| 2026-10-05 | 10.2196/101615 | — | Feasibility and Preliminary Effects of AI-Generated Personalized Sleep Feedback in High School Female Soccer Players: Pilot Randomized Controlled Trial | JMIR Form Res, 2026 | Fitbit (C1 wearable query) | feasibility (primary outcome), adherence (valid Fitbit wear nights), data completeness (message delivery, questionnaire completion) | Likely OA (JMIR CC BY policy); PMCID not yet indexed |
| 2026-10-05 | 10.3389/fphys.2026.1914161 | PMC13623721 | Integrating technology-assisted behavioral management into a summer obesity prevention intervention program: a pilot controlled trial | Front Physiol, 2026 | Fitbit + ActiGraph (C1 wearable query) | acceptability (explicit questionnaire), attrition (1/14 withdrew wk1), engagement (app-use decline post-camp) | OA (Frontiers CC BY; PMCID present) |
| 2026-10-05 | 10.2196/88773 | PMC13626640 | Enhancing a Behavioral Intervention Using Rest-Activity Rhythm Monitoring via a Consumer Wearable in Older Dementia Caregivers and People With Dementia: Feasibility and Acceptability Study | JMIR Form Res, 2026 | Apple Watch (C1 wearable query) | feasibility + acceptability (explicit), adherence (valid-day/active-user rates differ sharply by subgroup) | OA (JMIR CC BY; PMCID present) |
| 2026-10-05 | 10.2196/92359 | PMC13626187 | Feasibility and Acceptability of Oura Ring Sleep Monitoring in Older Adults Admitted From the Emergency Department: Prospective Cohort Study | JMIR Form Res, 2026 | Oura Ring (C1 wearable query) | feasibility + acceptability (explicit), attrition (29 approached → 15 enrolled → 14 completed), wear time (≥75% threshold) | OA (JMIR CC BY; PMCID present) |
| 2026-10-05 | 10.1007/s10461-026-05317-w | — | Efficacy of Tailored Messages for 28-Week Exercise Sustainability in People with HIV | AIDS Behav, 2026 | ActiGraph (C1 wearable query) | retention/attrition (118 → 92 re-randomized, explicit "robust to attrition"), adherence (monthly ActiGraph wear-week protocol) | Unclear/likely Paywalled (Springer subscription journal; no PMCID indexed) |
| 2026-10-05 | 10.1371/journal.pdig.0001691 | PMC13614584 | Optimizing accelerometer implementation in a gerotherapeutic trial: Feasibility, adherence, and operational insights of ABLE | PLOS Digit Health, 2026 | ActiGraph wGT3X-BT (C1 wearable query) | feasibility + adherence (title-level, explicit), retention/attrition (17% dropout, Cox model), technical ("device operational concerns" assessed) | OA (PLOS CC BY; PMCID present) |
| 2026-09-07 | 10.4037/aacnacc2026416 | — | Challenges of Using Fitness Trackers in Critical Care | *AACN Advanced Critical Care* 2026 | Fitbit | compliance (device placement/patient compliance issues); technical failure (devices "unreliable and inaccurate," study terminated early) | Unclear (no PMC listed; subscription journal) |
| 2026-09-07 | 10.1016/j.gerinurse.2026.104269 | — | The feasibility and efficacy of weighted blankets as a sleep intervention for people with behavioural and psychological symptoms of dementia: a pilot randomised crossover trial | *Geriatric Nursing* 2026 | Withings (Sleep Analyser) | feasibility/acceptability (explicitly stated high); compliance (variable adherence to protocol); technical failure ("the Withings did not adequately measure sleep") | Unclear (no PMC listed; Elsevier subscription journal) |
| 2026-09-07 | 10.2196/95194 | PMC13524361 | A One-Year Study Using Digital Biomarkers From Sensing Technologies to Assess Changes in Physical Activity Levels and Sleep Quality in Nursing Home Residents With Dementia: Observational Study | *JMIR Nursing* 2026;9 | Garmin (Vivoactive 5 / Venu 3) — also uses a non-profiled Somnofy radar-based sensor alongside it | adherence/acceptability (88–96%, explicitly quantified); retention/attrition (11 enrolled, 9 in final analysis); longitudinal (baseline/6-month/1-year) | OA (JMIR, CC BY license; PMC available) |
| 2026-09-14 | 10.1002/pan.70309 | — | Continuous Wrist-Derived Heart Rate Correlates With mYPAS Scores and Detects Between-Assessment Heart-Rate Elevations in Children: A Feasibility Study | *Paediatric Anaesthesia*, 2026 | Empatica EmbracePlus (wrist wearable) | feasibility (title); attrition (32 consented → 15 analyzable) | Paywalled (no PMC copy found) |
| 2026-09-28 | 10.1016/j.exger.2026.113337 | — | A reproducible pipeline for processing commercial wearable step-count data in aging cohorts: Application and evaluation in the STRRIDE-PD reunion study | Experimental Gerontology, 2026 | Garmin (step-count pipeline) | data completeness; wear-time inference | Unclear (no PMC id) |
| 2026-09-28 | 10.1111/jgs.70726 | — | Development and Preliminary Feasibility Testing of PACERS, a Physical Activity-Centered Intervention for Rural Older Adults With Hypertension | J Am Geriatr Soc, 2026 | Fitbit | feasibility; recruitment/retention/fidelity/adherence | Unclear (no PMC id) |
| 2026-09-28 | 10.1002/pon.70616 | PMC13613989 | Making Interventions More Effective: Changes in Theoretical Constructs During Delivery of a Peer-Led Physical Activity Program for Breast Cancer Survivors | Psycho-Oncology, 2026 | Fitbit | engagement; longitudinal | PMC deposit exists **Conflict:** the 2026-10-05 run rejected this (no-cohort: webMFT breast-cancer-survivor PA program (Fitbit 'active minutes', n=30 analysed of 61 randomised); theoretical-construct (self-efficacy/social-support) mediation analysis. 'Engagement' and 'longitudinal' sign). Kept because an earlier run queued it. |
| 2026-09-28 | 10.1111/acem.70408 | — | Smartphone-Based Measurement of Cognition and Physical Function in Older Emergency Department Patients: A Feasibility Study | Acad Emerg Med, 2026 | Apple Watch / Apple ResearchKit | feasibility; completion-rate reporting | Unclear (no PMC id) |
| 2026-09-28 | 10.2196/88466 | PMC13592238 | Clinical Implementation of Wearable-Derived Sleep and Activity Reporting for Inpatient Psychiatric Monitoring | JMIR Form Res, 2026 | GENEActiv | feasibility; usability; technical-failure/barriers | PMC deposit exists (JMIR, typically CC BY) |
| 2026-09-28 | 10.1177/03331024261492220 | — | Migraine attack prediction using wearable biosensor data | Cephalalgia, 2026 | Empatica EmbracePlus | feasibility; longitudinal (~1-month monitoring) | Unclear (no PMC id) **Conflict:** the 2026-10-05 run rejected this (architecture: Empatica EmbracePlus migraine-attack ML prediction model (n=27, ~31 days/participant). States 'feasibility of migraine attack prediction' -- algorithmic/prediction-method feasibility, not operational-deploy). Kept because an earlier run queued it. |

Platform attribution is Reported — verify from full text before profiling.

---

## Backlog carried in from the manual discovery passes

These are **not** routine output. They are candidates already identified and not yet built, kept here
so the queue is the single place to look for "what could be profiled next".

| Source file | Unbuilt candidates | Notes |
|---|---|---|
| [`_onnela-module3-candidates.md`](_onnela-module3-candidates.md) | ~18 of 27 | 9 built. Six have **no open-access route at all** — concentrated in *Ann Surg*, *Neurosurgery*, *Psychiatry Research*, *QoL Research*, and including the only ingestible-sensor and only audio/speech studies in the set. |
| [`_recency-scan-2026-09.md`](_recency-scan-2026-09.md) | ~20 of 30 listed | Date-sorted pass. 5 built from it. |
| [`_citation-graph-scan-2026-09.md`](_citation-graph-scan-2026-09.md) | ~60 of 71 screened | **Beiwe-heavy for methodological reasons, not because Beiwe deployments are more common** — its anchor papers simply have more citations. Do not build these out without a matching pass on other platforms. |

| [`_device-side-scan-2026-09.md`](_device-side-scan-2026-09.md) | 30 ranked plus 31 lower priority | Date-sorted device-side pass, 2026-09-03 evening. Six Polar candidates (the device had none), Garmin best served, first EmbracePlus candidate, four Withings, and deployments in Uganda, Burkina Faso, Nepal, Ecuador, Jamaica, Thailand, Lithuania, Korea, Japan, Singapore, Taiwan and remote Aboriginal Australia. Every attribution Reported until full text is read. |
| [`_across-the-board-scan-2026-09.md`](_across-the-board-scan-2026-09.md) | 65 ranked | Topic-first, ACM-venue and grey-literature pass, 2026-09-03 evening. Non-Beiwe platform yield the name searches missed (RADAR-base 4, mindLAMP 4, m-Path 3, Avicenna, LifeData, MetricWire 1 each), South Africa and Kenya deployments, and two Beiwe deployments with 2024 collection windows that may be the first post-heartbeat figures. Overlaps the device-side scan on about 20 candidates, flagged in the file. Grey literature was weak. |
| 2026-09-03 coverage pass (this file's own backlog) | 5 | Panda 2020 *JAMA Surg* 155:123-129 and Panda 2021 *Ann Surg Oncol* 28:985-994 (passive streams of the cancer-surgery Beiwe cohort); Kubala et al., US Navy shipboard Oura, N=853, 71% of days underway (via Gong 2025 review); a Hispanic pregnancy Oura cohort, N=15, adherence 80% to 31% postpartum (same source); Hirten 2025 IBD Forecast (Q120), profile once Supplemental Table 1 is obtained. |
| Evidation profile pass, 2026-09-03 | 2 | Goodday et al. 2024 *JMIR* 26:e57827 (six cohorts on the Evidation platform, median retention 77.2 percent, device-level adherence for Oura, Garmin and Apple Watch) and Cho et al. 2025 *Lancet Digit Health* (Evidation arm of 89,479 participants, five months of daily surveys). Both PDFs or full text stored under `module-02-digital-phenotyping/literature/evidation/`. Evidation now has a Module 2 profile, so both qualify for Module 3 screening. |

**Known gaps that none of the above closes:** no head-to-head comparison of Beiwe, mindLAMP and
RADAR-base (three candidates have looked like one and turned out not to be); geography is
overwhelmingly US and Western European.
