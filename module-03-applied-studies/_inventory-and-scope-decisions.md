# Module 3 — Phase 1: Inventory and Scope Decisions

**Sessions:** 2026-08-31 (baseline), 2026-09-01 (extension), 2026-09-02 (recency + citation-graph).
**Status:** **55 profiles / 54 distinct deployments.** The
19-study baseline plus a 21-study extension — a platform-coverage pass closing the AWARE / Avicenna /
MetricWire / m-Path / CARP gap (12 profiles) and an Onnela-tranche pass (9 profiles). 18 of the 27
staged Onnela candidates remain unbuilt; ~30 recency candidates remain unbuilt.

This file records how the Module 3 study universe was enumerated, what was screened in and out, and
the judgment calls that will affect later comparisons. Per `CLAUDE.md`, Module 3's unit of analysis
is the **study**, not the technology, so the inventory could not be built from a fixed list the way
Modules 1 and 2 were.

---

## Discovery method

Per `CLAUDE.md`'s Module 3 Phase 1 note, discovery ran **from the device/platform side**, not from a
list of studies.

**Pass 1 — technology × deployment terms.** Europe PMC REST API, one query per Module 1/2 technology
(20 technologies), each ANDed with a deployment-reality term block (`feasibility OR adherence OR
retention OR compliance OR "wear time" OR deployment OR attrition OR "data completeness" OR "missing
data" OR acceptability OR usability OR "real-world" OR longitudinal`), restricted to `SRC:MED` or
`SRC:PPR` and first publication date 2018-01-01 to 2026-12-31, sorted by citation count, 100 records
per technology.

Total hit counts per technology (before screening) ranged from 98 (Movesense) to 10,545 (ActiGraph).
The 2,000 retrieved records reduced to **121 unique screened-in candidates**.

**Automated screening rules applied to pass 1:**

- Required a digital-health context term in title/abstract (wearable, smartwatch, smartphone,
  actigraph, EMA, remote monitoring, sensor, etc.) — this removed the large false-positive classes
  from ambiguous platform names (**Polar** → polar bears/polar regions; **Avicenna** → the historical
  physician; **AWARE** → the ordinary English word; **CARP** → the fish; **Oura**, **Samsung**,
  **m-Path** similar).
- Required **≥2** distinct deployment-reality signals (retention, adherence, feasibility,
  completeness, technical failure, longitudinal).
- Down-weighted titles matching pure-validation language (validate, accuracy, agreement,
  polysomnography, Bland-Altman, criterion validity) — these are Module 1's territory by explicit
  scope rule.
- Up-weighted multi-technology records (a Module 3 priority area), large N, and open access.

**Pass 2 — targeted supplementary queries.** Pass 1's deployment vocabulary systematically favoured
digital-phenotyping platforms over consumer wearables, so a second pass ran eight targeted queries
covering BYOD study designs, All of Us Fitbit, the Apple cohort studies, decentralized/remote trials,
consumer-wearable adherence, wearable + phenotyping-platform combinations, attrition methodology, and
explicit device-failure language.

**Known bias in the discovery method (recorded for future passes):** both passes sorted by citation
count, which favours older and higher-profile work and under-samples 2025–2026 publications. Pass 2's
citation sort also dragged in high-citation clinical guidelines and AHA statistical statements that
are irrelevant here. A future pass should re-run sorted by date to catch recent deployments.

---

## Screening outcome

| | Count |
|---|---|
| Records retrieved (pass 1) | ~2,000 across 20 technologies |
| Unique candidates surviving automated screening | 121 |
| Of those, non-review primary studies | 103 |
| Multi-technology candidates (priority area) | 9 |
| Flagged as likely pure-validation, deprioritized | 6 |
| **Selected for the initial baseline profile set** | **19** |

---

## Baseline set selected (19 studies)

Selected to cover both modules, both deployment models (BYOD vs provisioned), a range of durations
(8 weeks to 2+ years), and all four Module 3 priority areas. Full texts were obtained for all 19.

| Slug | Technologies | Why selected |
|---|---|---|
| `radar-mdd-recruitment-retention` | RADAR-base + Fitbit | Flagship retention/data-availability paper; N=623, 3 countries, up to 24 months |
| `radar-mdd-longterm-engagement` | RADAR-base + Fitbit | Per-stream retention survival analysis + engagement clustering on the same cohort |
| `radar-ad-feasibility-usability` | RADAR-base ecosystem, Axivity, Fitbit, Dreem, +4 more | 8 concurrent device types across all AD severity stages |
| `radar-base-treatment-engagement` | RADAR-base | RMT engagement during active psychological treatment, mixed methods |
| `beiwe-als-adherence` | Beiwe | RCT + 2 observational studies; adherence decay in a progressive neurodegenerative population |
| `beiwe-adolescent-feasibility` | Beiwe | Long-term mental-health monitoring in adolescents |
| `beiwe-chronic-disease-substudy` | Beiwe | N=2,394 — the largest Beiwe deployment found; embedded in 2 prospective cohorts |
| `beiwe-missing-data-sociodemographic` | Beiwe | Who is missing from digital-phenotyping data — equity/missingness |
| `beiwe-inpatient-suicide-pilot` | Beiwe + movisensXS | Inpatient → post-discharge transition; high-risk population. **Correction:** discovery tagged this "Beiwe + Empatica"; no Empatica device was used. |
| `mindlamp-relapse-3site` | mindLAMP | 3 sites, 2 countries (US + India) — cross-national deployment |
| `sleepsight-schizophrenia-rest-activity` | Fitbit Charge HR + Purple Robot | Acceptability and barriers to long-term use in psychosis. **Correction:** discovery tagged this as Empatica; the E4 was tested and *rejected* by the user group. |
| `empatica-epilepsy-data-quality` | Empatica | Data quality/completeness as the primary outcome, 4 epilepsy centres |
| `withings-postop-remote-monitoring` | Withings | Older surgical oncology patients; implementation lessons |
| `movesense-palliative-support-trial` | Movesense + wrist device | Hospitalised palliative patients — an unusual and demanding setting |
| `byod-demographic-imbalance` | Consumer wearables, cross-cutting | BYOD study design as a source of demographic imbalance |
| `allofus-fitbit-step-counts` | Fitbit (BYOD) | Largest consumer-wearable research deployment in existence |
| `apple-heart-data-management-lessons` | Apple Watch | Data-management lessons at ~419k enrolment scale |
| `dp-schizophrenia-tolerability` | Smartphone phenotyping | Adherence, feasibility and *tolerability* explicitly as outcomes |
| `fitbit-heart-study-afib` | Fitbit | ~455k enrolment; siteless recruitment and return-rate operations |

---

## Scope decisions and exclusions

| Decision | Rationale |
|---|---|
| **Systematic reviews and scoping reviews excluded from the profile set** | Module 3's unit of analysis is a deployment. Reviews of deployments are useful pointers and are retained in `sources.md`, but a review has no cohort, no retention rate, and no technical failure log of its own. |
| **Pure validation/accuracy studies excluded** | Explicit `CLAUDE.md` scope rule — that is Module 1's literature library. Six candidates were flagged and dropped on this basis. |
| **Platform architecture/methods papers excluded** | Explicit `CLAUDE.md` scope rule — Module 2's territory. This removed several Beiwe/Forest methods papers surfaced by the search (GPS imputation with missingness, mobility inference from sparse GPS traces). They remain valuable but belong in Module 2's literature library. |
| **EMA-only platforms admitted, with the precedent recorded rather than set silently** | `CLAUDE.md` admits a Module 3 study when its platform is profiled in Module 1 or 2. LifeData was profiled in Module 2 on 2026-09-02, which makes two previously-blocked deployments eligible — **Nock et al. 2026** (N=619, the largest study in the Onnela tranche) and **Ball et al. 2025**. **The judgment call:** LifeData is EMA/ePRO-only — its sole sensor stream is GPS captured *with* a survey response, and what Nock et al. call "passive" data is **survey response metadata, not phone sensors**. Admitting these studies therefore widens Module 3 from *passive-sensing deployments* toward *app-based EMA deployments generally*, and they will be the precedent. **Decision: admit them**, on the grounds that (a) Module 2's own scope already includes EMA-centric commercial platforms, and (b) Module 3's value is operational reality — an N=619 deployment reporting 81.1% any-data and declining survey initialisation is exactly the content this module exists for, whether the stream is active or passive. **Condition: any such profile must state plainly that it is an EMA deployment, not a passive-sensing one**, so the feasibility matrix is not read as comparing like with like. Note also that both studies come from the same Harvard/Boston programme, so they are not independent replications. |
| **Studies using technologies not profiled in Modules 1 or 2 were not absorbed** | Per `CLAUDE.md`, these are flagged as candidates for Module 1/2 expansion instead. **Candidates noted this pass:** the **Dreem** EEG sleep headband, the **Fibaro** home-sensor system, and the **CANedge** automotive data logger (all in RADAR-AD); **Connecare** (clinical remote-monitoring platform, Jonker et al.); **movisensXS** (EMA platform, Wang et al.); **Ilumivu mEMA** (EMA platform, Raugh et al.); and **Purple Robot** (Northwestern CBITs sensing app, Meyer et al.) — none profiled in Module 1 or 2. Wrist-worn alcohol biosensors also surfaced repeatedly and are unprofiled. |
| **Protocol papers (no results yet) generally excluded** | ART-CARMA (RADAR-base ADHD study) was screened in but is a protocol paper with no deployment outcomes yet. Retained in `sources.md` as one to revisit. |
| **Citation-sorted discovery accepted for the baseline, flagged for correction** | Recorded above as a known bias. The baseline is deliberately weighted toward well-established, heavily-cited deployments; recency coverage is a known gap for the next pass. |

## Ambiguous inclusion calls (recorded rather than silently resolved)

- **`allofus-fitbit-step-counts`** (Master et al., *Nature Medicine* 2022) is primarily an
  epidemiological paper, not a feasibility paper. It is included because the All of Us Fitbit cohort
  is the largest BYOD consumer-wearable research deployment available and its inclusion criteria and
  wear-time requirements are themselves major deployment-reality facts. A reader looking for a
  feasibility-first paper should go to `byod-demographic-imbalance` instead.
- **`fitbit-heart-study-afib`** and the Apple Heart Study are fundamentally screening/detection
  studies. They earn Module 3 entries for their **operational** content at very large scale
  (enrolment funnels, notification and return rates, siteless recruitment), not for their clinical
  findings.
- **`empatica-epilepsy-data-quality`** sits close to the validation boundary — it is about signal
  quality. It is included because its unit of analysis is *data completeness across a multi-centre
  deployment*, not sensor accuracy against a reference standard.

## Relationship to the Onnela Lab publication sweep

A parallel effort this session catalogued the Onnela Lab (Harvard Chan) Digital Health &
Phenotyping publication list into Modules 1 and 2. Many of those papers are applied Beiwe
deployments that also qualify for Module 3. The agreed routing rule, following `CLAUDE.md`:

- **Catalog layer:** every paper gets exactly one citation entry, in the module that owns the
  *technology* (Module 2 for Beiwe/Forest/phenotyping, Module 1 for wearables).
- **Deep operational layer:** the subset that reports how the deployment went *additionally* gets a
  Module 3 study profile, with the catalog entry carrying a forward pointer. Content is linked, not
  duplicated.
- Beiwe/Forest **methods and architecture** papers stay catalog-only in Module 2.

**Outcome of that sweep (completed 2026-08-31):** 113 distinct Digital Health & Phenotyping papers
catalogued — 91 into Module 2, 22 into Module 1, 3 already present and deduplicated by DOI. 71 PDFs
obtained. **27 were triaged as Module 3 candidates** and are staged in
[`_onnela-module3-candidates.md`](_onnela-module3-candidates.md), ranked by operational content, each
with a forward pointer from its catalog row. Rankings there were made from abstracts only and are
labelled **Reported** pending full-text extraction.

**Scope decision on the combined pool.** The Onnela candidates plus this pass's baseline would make
~46 profiles, which is more than one session can build to the depth Module 3's template requires
without degrading quality. Decision: **complete the 19-study baseline first**, since it was selected
for cross-module and cross-priority-area coverage, then treat the 27 Onnela candidates as the
**second tranche**. Three of them are strong enough to jump the queue in the next pass and are noted
here so the ranking is not lost:

1. **Mercier et al. 2020** (spinal cord injury, Beiwe, N=43) — reports **retention broken out by
   financial-incentive arm (78% with vs. lower without)**. This module currently has *no* study that
   isolates the effect of incentives on retention, and every high-retention study in the baseline
   confounds incentives with other support. PDF not obtained.
2. **Johnson et al. 2023** (ALS, Beiwe + ActiGraph Insight Watch + Modus StepWatch, N=40, 6 months)
   — reports wearable wear compliance and app survey compliance **side by side across two wearable
   form factors**, which is rare and directly serves the multi-device priority area.
3. **Yi et al. 2025** (Beiwe EMA + minute-level accelerometer/GPS embedded in Nurses' Health Study II,
   N=181) — a phenotyping substudy inside a major established cohort, the same design pattern as the
   baseline's `beiwe-chronic-disease-substudy`.

Note the second tranche is heavily Beiwe-weighted by construction (it comes from one lab). It
should not be built out without a matching pass on the other Module 2 platforms, or the module's
evidence base will tilt toward Beiwe for reasons of sampling rather than merit — an explicit risk to
the objectivity `CLAUDE.md` requires for Beiwe specifically.

**Resolution (2026-09-01):** both passes were run **in parallel** precisely to avoid that tilt. The
platform-coverage pass added 12 profiles across all five previously uncovered platforms; the Onnela
pass added 9. Outcome: **Beiwe is 11 of 40 profiles (28%)** rather than 11 of 28 (39%), and every
other Module 2 platform now has at least one entry. Residual concerns, recorded rather than resolved:

- The 11 Beiwe profiles are **not 11 independent observations** — nine share an author.
- **Every Beiwe figure in the module is pre-`heartbeat`** (newest collection window closes 2023),
  making Beiwe's evidence base simultaneously the largest and the most systematically dated. Logged
  as Tier 15 Q115.
- Mitigating: **none of the Onnela tranche's transferable findings are Beiwe-specific** — incentive
  structure, clinician gatekeeping, smartphone-ownership exclusion, wear-time definitions and
  recruitment channel are all platform-general.

## Open discovery gaps for the next pass

1. ~~Re-run discovery sorted by **date rather than citations** to cover 2025–2026 deployments.~~
   **Done 2026-09-01** — see [`_recency-scan-2026-09.md`](_recency-scan-2026-09.md). The bias was
   confirmed and was large: **62 of 64** screened-in recent candidates had not been surfaced by the
   citation-sorted pass at all. The Phase 1 baseline should therefore be read as covering
   *well-established* deployments rather than current practice. A residual gap remains for
   2023–mid-2024 work that is neither recent enough for the date-sorted cut-off (2024-06-01) nor yet
   well cited.
2. Garmin, Polar and Apple Watch deployments remain thinly represented. **ActiGraph, Oura and
   Samsung gained entries in the extension.** The pass-1 deployment vocabulary favoured phenotyping
   platforms.
3. No non-English-language deployments were captured; Europe PMC coverage skews Anglophone.
4. Grey literature — consortium reports, trial registry records with posted results, and vendor
   case studies — was not searched at all.
5. Deployments in low- and middle-income settings are almost absent from the baseline (mindLAMP's
   India sites are the sole representation).
6. **Two structural blind spots in the discovery method, both found the hard way and both worth
   fixing before the next pass:**
   - **Ordinary-word platform names.** Europe PMC does not honour phrase quoting for `"AWARE
     framework"`, so a phrase query still returned 579 date-window hits dominated by
     "geometry-aware", "causality-aware" and similar. Genuine AWARE deployments never entered the
     retrieved window and the recency scan wrongly concluded a null. **At least 7 qualifying AWARE
     deployments exist; 3 are now profiled.**
   - **Framework-shaped platforms.** CARP Mobile Sensing is a Flutter library embedded in other
     people's apps and publishes under *their* names (m-Path Sense, DiaFocus, mCardia, Wrist Angel).
     Five Europe PMC query forms, arXiv and OpenAlex were tried; **only the OpenAlex citation-graph
     pass found the ecosystem.**

   **Consequence: treat any future null from a name-based query as unproven until a citation-graph
   pass has been run.**

7. **Citation-graph discovery (OpenAlex) run 2026-09-02** —
   [`_citation-graph-scan-2026-09.md`](_citation-graph-scan-2026-09.md). Finds deployments that cite a
   platform's methods paper without naming it, which is the only route that works for framework-shaped
   platforms. **It confirmed the CARP null by a second independent method** (the Bardram anchors have
   only 14 citing works since 2018 in total), and it cross-validated the date-sorted pass by
   independently re-surfacing several of the same high-value papers.

   **But it has its own failure mode, and the rate is high: 3 of the first ~12 candidates examined
   were attributed to the wrong platform**, because citing a platform and deploying it are different
   things and background citations are common. Treat every citation-graph platform attribution as
   **Reported** until confirmed from full text.

8. **Remaining gaps after three discovery methods:** **AWARE is now the least-served covered platform**
   (7 unbuilt candidates); Module 3 still has **no head-to-head comparison of Beiwe, mindLAMP and
   RADAR-base** (the candidate that looked like one used none of them); no low-income-country
   deployment beyond Ecuador and India; grey literature still unsearched.

9. **AWARE coverage pass, 2026-09-02** — see
   [`_aware-build-report.md`](_aware-build-report.md). The "7 unbuilt AWARE candidates" figure carried
   forward from the previous pass **did not survive inspection**: one was LINC (already profiled, and
   mindLAMP not AWARE) and roughly four were reviews, platform-architecture or design papers, all
   explicitly out of scope.

   A dedicated pass over **all 425 papers citing the AWARE anchor since 2016** established the real
   shape of the seam:

   | Deployment signals in abstract | Papers |
   |---|---|
   | 0 | 215 |
   | 1 | 106 |
   | 2 | 31 |
   | 3+ | **2** |
   | No abstract | 68 |

   **AWARE has the inverse problem to CARP.** CARP has almost no citing literature; AWARE has 425
   citing papers that overwhelmingly *use* it as a toolkit and report findings rather than
   deployments. Five profiles were built; all five verified from full text as genuine AWARE
   deployments, though **two used author-modified builds** (NIIMA/Niimpy; an app "based on the AWARE
   framework"). That derivative-build pattern means platform-level aggregation for AWARE will degrade
   as it accumulates — a caution for any future comparison table.

10. **A third structural blind spot: venue-shaped invisibility.** The best topic-matched AWARE
    candidate (`10.1145/3711043`, "Participant Engagement and Data Quality") **could not be obtained
    in full text at all** — ACM DL serves a challenge page, no preprint exists, it is not in PMC. It
    was left unprofiled rather than written from its abstract. AWARE's deployment-reality literature
    lives in CSCW/IMWUT/UbiComp, outside the biomedical indexes this module's discovery route can
    see. Joins the two blind spots recorded at item 6.
