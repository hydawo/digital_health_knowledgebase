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
| 2026-10-26 | 10.1136/bmjopen-2026-121681 | PMC13691778 | Feasibility and acceptability of a remote blood pressure monitoring pharmacist-led telehealth programme in an emergency department transition care clinic: a pilot randomised controlled trial | BMJ Open 2026;16(10):e121681 | Withings (BPM Connect Pro) | feasibility, acceptability, retention (27 screened, 24 randomised, 16/24 completed 12-week visit) | Open (BMJ Open) |

**2026-10-22:** the 16 rows then pending were screened from full text (7 profiled, 9 rejected; see
`feasibility-matrix.md` Part F and the ledger). Five rejections are `unobtainable` only because the publisher
served a bot check to scripts. Re-screen these from a PDF fetched by hand in a browser:
10.1111/jgs.70726 (PACERS), 10.1016/j.gerinurse.2026.104269 (weighted blankets), 10.1002/pan.70309
(EmbracePlus, paediatric anaesthesia), 10.1177/03331024261492220 (EmbracePlus, migraine), 10.1111/acem.70408
(Apple Watch, older ED patients). 10.4037/aacnacc2026416 is closed access. Leads: Pinto 2025 J Cancer Surviv
10.1007/s11764-025-01811-7 (parent trial of a rejected Fitbit paper); two earlier DIPH.DEM papers,
10.3390/s25216635 and 10.3389/fragi.2026.1768935 (same cohort as the Boyle 2026 profile).

**2026-10-24:** the four rows then pending were screened from full text (1 profiled, Hallihan 2026; 3 rejected; report `_screening-reports/2026-10-24-queue.md`). PROPHESY (10.1016/j.aucc.2026.101711) is `unobtainable` only because of a bot check; re-screen from a PDF fetched by hand.

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
| 2026-10-09 | 10.1200/CCI-24-00201 | — | Odom et al. companion feasibility report to the BMC Cancer Beiwe caregiver study (10.1186/s12885-025-14009-y) | JCO Clin Cancer Inform 2025;9:e2400201 | Beiwe, Harvard-hosted (from the BMC Cancer paper) | the BMC Cancer paper defers feasibility to this report and has itself only N consented and N usable (58 and 46, abstract says 48); not yet read | Unknown |
| Evidation profile pass, 2026-09-03 | 2 | Goodday et al. 2024 *JMIR* 26:e57827 (six cohorts on the Evidation platform, median retention 77.2 percent, device-level adherence for Oura, Garmin and Apple Watch) and Cho et al. 2025 *Lancet Digit Health* (Evidation arm of 89,479 participants, five months of daily surveys). Both PDFs or full text stored under `module-02-digital-phenotyping/literature/evidation/`. Evidation now has a Module 2 profile, so both qualify for Module 3 screening. |

**Known gaps that none of the above closes:** no head-to-head comparison of Beiwe, mindLAMP and
RADAR-base (three candidates have looked like one and turned out not to be); geography is
overwhelmingly US and Western European.
