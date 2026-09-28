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
| 2026-09-28 | 10.1016/j.exger.2026.113337 | — | A reproducible pipeline for processing commercial wearable step-count data in aging cohorts: Application and evaluation in the STRRIDE-PD reunion study | Experimental Gerontology, 2026 | Garmin (step-count pipeline) | data completeness; wear-time inference | Unclear (no PMC id) |
| 2026-09-28 | 10.1111/jgs.70726 | — | Development and Preliminary Feasibility Testing of PACERS, a Physical Activity-Centered Intervention for Rural Older Adults With Hypertension | J Am Geriatr Soc, 2026 | Fitbit | feasibility; recruitment/retention/fidelity/adherence | Unclear (no PMC id) |
| 2026-09-28 | 10.1002/pon.70616 | PMC13613989 | Making Interventions More Effective: Changes in Theoretical Constructs During Delivery of a Peer-Led Physical Activity Program for Breast Cancer Survivors | Psycho-Oncology, 2026 | Fitbit | engagement; longitudinal | PMC deposit exists |
| 2026-09-28 | 10.1111/acem.70408 | — | Smartphone-Based Measurement of Cognition and Physical Function in Older Emergency Department Patients: A Feasibility Study | Acad Emerg Med, 2026 | Apple Watch / Apple ResearchKit | feasibility; completion-rate reporting | Unclear (no PMC id) |
| 2026-09-28 | 10.1371/journal.pdig.0001691 | PMC13614584 | Optimizing accelerometer implementation in a gerotherapeutic trial: Feasibility, adherence, and operational insights of ABLE | PLOS Digital Health, 2026 | ActiGraph | feasibility; adherence; wear time; attrition/dropout | PMC deposit exists (PLOS, typically CC BY) |
| 2026-09-28 | 10.2196/88466 | PMC13592238 | Clinical Implementation of Wearable-Derived Sleep and Activity Reporting for Inpatient Psychiatric Monitoring | JMIR Form Res, 2026 | GENEActiv | feasibility; usability; technical-failure/barriers | PMC deposit exists (JMIR, typically CC BY) |
| 2026-09-28 | 10.1177/03331024261492220 | — | Migraine attack prediction using wearable biosensor data | Cephalalgia, 2026 | Empatica EmbracePlus | feasibility; longitudinal (~1-month monitoring) | Unclear (no PMC id) |

Platform attribution is Reported - verify from full text before profiling.

---

## Backlog carried in from the manual discovery passes

These are **not** routine output. They are candidates already identified and not yet built, kept here
so the queue is the single place to look for "what could be profiled next".

| Source file | Unbuilt candidates | Notes |
|---|---|---|
| [`_onnela-module3-candidates.md`](_onnela-module3-candidates.md) | ~18 of 27 | 9 built. Six have **no open-access route at all** — concentrated in *Ann Surg*, *Neurosurgery*, *Psychiatry Research*, *QoL Research*, and including the only ingestible-sensor and only audio/speech studies in the set. |
| [`_recency-scan-2026-09.md`](_recency-scan-2026-09.md) | ~20 of 30 listed | Date-sorted pass. 5 built from it. |
| [`_citation-graph-scan-2026-09.md`](_citation-graph-scan-2026-09.md) | ~60 of 71 screened | **Beiwe-heavy for methodological reasons, not because Beiwe deployments are more common** — its anchor papers simply have more citations. Do not build these out without a matching pass on other platforms. |

| 2026-09-03 coverage pass (this file's own backlog) | 5 | Panda 2020 *JAMA Surg* 155:123-129 and Panda 2021 *Ann Surg Oncol* 28:985-994 (passive streams of the cancer-surgery Beiwe cohort); Kubala et al., US Navy shipboard Oura, N=853, 71% of days underway (via Gong 2025 review); a Hispanic pregnancy Oura cohort, N=15, adherence 80% to 31% postpartum (same source); Hirten 2025 IBD Forecast (Q120), profile once Supplemental Table 1 is obtained. |

**Known gaps that none of the above closes:** no head-to-head comparison of Beiwe, mindLAMP and
RADAR-base (three candidates have looked like one and turned out not to be); geography is
overwhelmingly US and Western European.
