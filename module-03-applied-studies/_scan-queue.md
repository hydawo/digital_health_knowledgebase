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
| 2026-09-07 | [10.4037/aacnacc2026416](https://doi.org/10.4037/aacnacc2026416) | — | Challenges of Using Fitness Trackers in Critical Care | *AACN Advanced Critical Care* 2026 | Fitbit | compliance (device placement/patient compliance issues); technical failure (devices "unreliable and inaccurate," study terminated early) | Unclear (no PMC listed; subscription journal) |
| 2026-09-07 | [10.1016/j.gerinurse.2026.104269](https://doi.org/10.1016/j.gerinurse.2026.104269) | — | The feasibility and efficacy of weighted blankets as a sleep intervention for people with behavioural and psychological symptoms of dementia: a pilot randomised crossover trial | *Geriatric Nursing* 2026 | Withings (Sleep Analyser) | feasibility/acceptability (explicitly stated high); compliance (variable adherence to protocol); technical failure ("the Withings did not adequately measure sleep") | Unclear (no PMC listed; Elsevier subscription journal) |
| 2026-09-07 | [10.2196/95194](https://doi.org/10.2196/95194) | PMC13524361 | A One-Year Study Using Digital Biomarkers From Sensing Technologies to Assess Changes in Physical Activity Levels and Sleep Quality in Nursing Home Residents With Dementia: Observational Study | *JMIR Nursing* 2026;9 | Garmin (Vivoactive 5 / Venu 3) — also uses a non-profiled Somnofy radar-based sensor alongside it | adherence/acceptability (88–96%, explicitly quantified); retention/attrition (11 enrolled, 9 in final analysis); longitudinal (baseline/6-month/1-year) | OA (JMIR, CC BY license; PMC available) |

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
