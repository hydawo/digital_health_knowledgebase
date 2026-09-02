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

_(empty — the routine has not yet run against Module 3. First firing expected the Monday following
2026-09-02.)_

| Found | DOI | PMCID | Title | Venue / year | Apparent technology | Signals | OA |
|---|---|---|---|---|---|---|---|

---

## Backlog carried in from the manual discovery passes

These are **not** routine output. They are candidates already identified and not yet built, kept here
so the queue is the single place to look for "what could be profiled next".

| Source file | Unbuilt candidates | Notes |
|---|---|---|
| [`_onnela-module3-candidates.md`](_onnela-module3-candidates.md) | ~18 of 27 | 9 built. Six have **no open-access route at all** — concentrated in *Ann Surg*, *Neurosurgery*, *Psychiatry Research*, *QoL Research*, and including the only ingestible-sensor and only audio/speech studies in the set. |
| [`_recency-scan-2026-09.md`](_recency-scan-2026-09.md) | ~20 of 30 listed | Date-sorted pass. 5 built from it. |
| [`_citation-graph-scan-2026-09.md`](_citation-graph-scan-2026-09.md) | ~60 of 71 screened | **Beiwe-heavy for methodological reasons, not because Beiwe deployments are more common** — its anchor papers simply have more citations. Do not build these out without a matching pass on other platforms. |

**Known gaps that none of the above closes:** no head-to-head comparison of Beiwe, mindLAMP and
RADAR-base (three candidates have looked like one and turned out not to be); geography is
overwhelmingly US and Western European.
