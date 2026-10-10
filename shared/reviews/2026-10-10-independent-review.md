# Independent review, 2026-10-10 (INCOMPLETE: interim report)

**Status: interim.** This run was ended before most sub-reviews finished. Fifteen parallel sub-reviews were started. Each one writes its findings to the scratch folder `/private/tmp/claude-501/-Users-hydawo-Downloads-Claude-Code-digital-health-knowledgebase/10738b5b-b0d3-4e47-afda-65cded3520e1/scratchpad/review/` (outside the repo). When this report was written, only the link check (1e) and a few spot checks had finished. Everything below comes from sources read in this session. Nothing about the unfinished parts is claimed here.

## 1. Summary

- Links checked: 566 unique URLs from the four `sources.md` files and the M1, M2 and M4 literature libraries.
  - 361 returned 200. Another 56 (JMIR, 202) and 7 (PubMed, 203) are live pages behind bot checks.
  - 120 returned 403, which are bot blocks (publishers, MDPI, Wiley, OUP and others). These are not counted as dead.
  - The GitHub 503 and 429 errors were rate limits. All of those pages are live when fetched through raw.githubusercontent.com.
  - 9 links are truly dead. 2 more returned 404 to curl, but their DOIs are registered in Crossref, so a bot block is likely. 1 link sends curl to a Google sign-in page.
- Claims checked in full: 1 catalogue row (L033), plus the dead-link findings. Parts 1a to 1d, 1f, 1g, the question resolution and the research-programs section were still running at handback. No counts for them are reported here.
- Overall trustworthiness: no judgement yet, since the fact-check sample has not been compiled.

## 2. Findings (so far)

| ID | Severity | File:line | File says | Source says | Source URL (accessed 2026-10-10) | Proposed replacement |
|---|---|---|---|---|---|---|
| R-001 | Major | module-02-digital-phenotyping/literature-library.md:229 | L033 title "...clinical inference and decision-baking"; "no DOI or indexed record located"; link is a Proofpoint urldefense wrapper | Crossref has the medRxiv preprint 10.1101/2024.10.03.24314808, posted 2024-10-04, title "Data Missingness in Digital Phenotyping: Implications for Clinical Inference and Decision-Making", authors Shen, Abdelkader, Isaac, Sarno, Kurz, Silbersweig, Onnela, Barron. There is also a 2026 JMIR preprint, 10.2196/preprints.95468 (TRIM framework, Barron et al.) | https://api.crossref.org/works/10.1101/2024.10.03.24314808 | Title: "Data Missingness in Digital Phenotyping: Implications for Clinical Inference and Decision-Making"; Status: "medRxiv preprint (2024), https://doi.org/10.1101/2024.10.03.24314808; later version JMIR preprint 10.2196/preprints.95468 (2026)" |
| R-002 | Minor | module-02-digital-phenotyping/sources.md:51; profiles/beiwe.md:277 | https://www.beiwe.org/beiwe-service-center-overview/ | HTTPS times out. HTTP redirects to an hsph.harvard.edu 404. The page that works is https://hsph.harvard.edu/research/onnela-lab/beiwe-service-center/ (200) | as listed | Replace the beiwe.org URL with https://hsph.harvard.edu/research/onnela-lab/beiwe-service-center/ |
| R-003 | Minor | module-01-wearables/sources.md:174 | developer.garmin.com/gc-developer-program/health-api/summaries/ | 404; the parent page returns 200 | https://developer.garmin.com/gc-developer-program/health-api/ | Use the parent URL |
| R-004 | Minor | module-01-wearables/sources.md:175 | https://developer.ouraring.com/docs | 404 | https://cloud.ouraring.com/v2/docs (200) | Use https://cloud.ouraring.com/v2/docs |
| R-005 | Minor | module-02-digital-phenotyping/sources.md:84, 200 | docs.lamp.digital/about/publications/ | 404; root returns 200 | https://docs.lamp.digital/ | Use the root URL, or mark the link dead |
| R-006 | Minor | module-02-digital-phenotyping/sources.md:90 | https://mindlamp.discourse.group/ | Host does not resolve (DNS) | n/a | Mark as "Dead (domain no longer resolves, 2026-10-10)" |
| R-007 | Minor | module-02-digital-phenotyping/sources.md:133 | MetricWire Atlassian "Missing Alerts Troubleshooting" page | 404 | n/a | Mark as dead |
| R-008 | Minor | module-02-digital-phenotyping/sources.md:174 | phidatalab.org/software__trashed/purple-robot-android-apps/ | 404; the slug is a trashed WordPress page | n/a | Mark as dead |
| R-009 | Minor | module-01-wearables/sources.md:255 | androidcentral Fitbit Air article | 404 | n/a | Mark as dead or replace with Google's own launch page |
| R-010 | Minor | module-01-wearables/sources.md:246 | thryve.health zepp-amazfit-integration | 404 | n/a | Mark as dead |
| R-011 | Note | module-04-methods-and-reviews/literature-library.md:58; module-01-wearables/literature-library.md:117; research-library-wearables.md:425 | 10.1038/s41746-025-01757-1; 10.5664/jcsm.8356 | Publisher returns 404 to curl, but Crossref has both records with matching titles. Probably a bot block | https://api.crossref.org/works/10.1038/s41746-025-01757-1 | No change; check in a browser |
| R-012 | Note | module-01-wearables/sources.md:39 | Health Connect data-types page | curl is redirected to a Google sign-in page | n/a | Check in a browser |

## 3. Question resolutions

Not compiled. The sub-reviews for the non-vendor sections and vendor checklists A and B were still running. Their output will be at `scratchpad/review/Q1_questions_nonvendor.md`, `Q2_vendor_A.md` and `Q3_vendor_B.md`.

## Research programs and academic data access

Not compiled. The output will be at `scratchpad/review/R1_programs_m1.md` and `R2_programs_m2.md`.

## 4. Method

- Links: a Python script ran curl with a browser user agent, HEAD then GET, following redirects, 16 threads. Every link that did not return 200 or 403 was then re-checked one at a time, and GitHub links were checked through raw.githubusercontent.com.
- Module 3 sample: Python `random.seed(20261010)`, then `random.sample` over the sorted profile filenames, k=12. Selected: metricwire-post-discharge-ema-reactivity, beiwe-spine-disease-mobility, metricwire-beiwe-bdd-remote-ema-passive, mpath-dementia-esm-feasibility, apple-heart-data-management-lessons, mindlamp-global-cognitive-multisite, oura-tempredict-healthcare-worker-adherence, aware-stand-mood-prediction-adherence, beiwe-chronic-disease-substudy, beiwe-nurses-health-study-burst, beiwe-cancer-surgery-survey-retention, beiwe-fitbit-gynecologic-cancer-hope.
- Sub-reviews started, with output files in the scratch folder: A1 (diff, M1 profiles and sources), A2 (diff, M1 evidence and libraries), A3 (diff, M2, OS limits, M3 queue, explorer), A4 (the 34 closures from 2026-10-10), B1 and B2 (matrix samples), C1 and C2 (Module 3 profiles), D (Crossref, 60 or more rows), F (consistency and confidence markers), Q1 to Q3 (questions), R1 and R2 (research programs).
- Could not access: the 120 bot-blocked publisher pages. Nothing behind a login was attempted.
