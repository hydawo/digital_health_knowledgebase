# Module 3 — Citation-graph discovery pass (OpenAlex), 2026-09-02

**Why this pass exists.** Platform-name search failed twice in the previous passes, in two distinct
ways: it cannot filter platforms whose name is an ordinary English word (Europe PMC ignores phrase
quoting for `"AWARE framework"`), and it cannot see *framework-shaped* platforms at all (CARP is a
library embedded in other people's apps and publishes under their names). This pass replaces name
matching with **citation matching**: find every work since 2018 that **cites a platform's own methods
paper**, on the reasoning that a deployment using the platform will cite it even when it never names
it in the title or abstract.

## Anchors used

| Platform | Anchor paper(s) | OpenAlex ID | Citing works since 2018 |
|---|---|---|---|
| AWARE | Ferreira, Kostakos & Dey 2015, *AWARE: Mobile Context Instrumentation Framework* | W2078074240 | 364 |
| CARP | Bardram 2020, *The CARP Mobile Sensing Framework* (2 records) | W4287754165, W3036631247 | **14** |
| m-Path | Mestdagh et al. 2023 | W4387742524 | 184 |
| mindLAMP | Torous et al. 2022, *Enabling Research and Clinical Use of Patient-Generated Health Data* | W4206048551 | 92 |
| RADAR-base | Ranjan et al. 2018 | W2904206377 | 249 |
| Beiwe | Torous et al. 2016; Beiwe platform 2021; Onnela & Rauch 2016 | W2347128633, W4200567269, W2392412101 | 1305 |

## Result

**71 candidates** screened in — same rules as previous passes (digital-health context term,
≥2 deployment-reality signals, non-review, article type), **excluding every DOI already cited in an
existing Module 3 profile**.

| Platform | Screened-in candidates |
|---|---|
| Beiwe | 47 |
| m-Path | 9 |
| mindLAMP | 9 |
| AWARE | 7 |
| RADAR-base | 6 |
| **CARP** | **0** |

### The CARP null is now confirmed twice over, by two independent methods

The Bardram anchor papers have **only 14 citing works since 2018 in total**, and none
qualified. This is no longer a search-method artefact: name-based search missed CARP because it is
framework-shaped, but the citation graph — which is immune to that problem — shows the deployment
literature genuinely is very small. The single profiled CARP deployment
([`profiles/carp-mpath-sense-performance-study.md`](profiles/carp-mpath-sense-performance-study.md))
may be close to the whole of it. Resolving whether DiaFocus is CARP-based (Tier 15 Q112) is now the
highest-value way to grow that evidence base.

### Cross-validation with the date-sorted pass

This pass independently re-surfaced several of the top finds from
[`_recency-scan-2026-09.md`](_recency-scan-2026-09.md) — the LINC framework paper, the passive
network-traffic study, the psychosis multi-wearable pilot — via a completely different retrieval
route. Two independent methods converging on the same papers raises confidence that the high-value
recent literature is now genuinely identified rather than an artefact of one query design.

## Top 30 candidates

| Score | Year | OA | Platform | DOI | Title |
|---|---|---|---|---|---|
| 18 | 2026 | Y | Beiwe | `10.2196/84618` | Digital Phenotyping via Passive Network Traffic Monitoring: Prospective Observational Study in  |
| 17 | 2025 | Y | m-Path | `10.2196/74103` | A Social Support Just-in-Time Adaptive Intervention for Individuals With Depressive Symptoms: F |
| 16 | 2026 | Y | RADAR-base | `10.2196/86049` | Evaluating Wearable Devices for Remote Monitoring in Psychosis: Pilot Study Nested Within the C |
| 16 | 2024 | Y | Beiwe | `10.1186/s44247-024-00116-6` | “Anything that would help is a positive development”: feasibility, tolerability, and user exper |
| 15 | 2026 | Y | AWARE/Beiwe | `10.1038/s41598-026-41435-0` | LINC: a framework for maintaining high-quality passive data in digital phenotyping studies |
| 15 | 2025 | Y | m-Path | `10.1016/j.invent.2025.100804` | Feasibility, acceptability and preliminary clinical outcomes of a brief coping-focused interven |
| 15 | 2022 | Y | Beiwe | `10.1177/20552076221129065` | From hybrid to fully remote clinical trial amidst the COVID-19 pandemic: Strategies to promote  |
| 14 | 2024 | N | mindLAMP | `10.1089/tmj.2024.0023` | The Digital Navigator: Standardizing Human Technology Support in App-Integrated Clinical Care |
| 14 | 2024 | Y | RADAR-base | `10.1038/s41598-024-67767-3` | Mitigating data quality challenges in ambulatory wrist-worn wearable monitoring through analyti |
| 13 | 2024 | Y | AWARE/Beiwe | `10.1007/s41347-024-00443-5` | Improving the Science of Adolescent Social Media and Mental Health: Challenges and Opportunitie |
| 13 | 2025 | Y | m-Path | `10.1038/s44400-025-00023-1` | Experience sampling in dementia: feasibility, utility and methodological insights from a high-i |
| 13 | 2024 | Y | m-Path | `10.2196/49857` | An Ecological Mobile Momentary Intervention to Support Dynamic Goal Pursuit: Feasibility and Ac |
| 13 | 2024 | Y | m-Path | `10.1186/s44247-024-00120-w` | Recovery at your fingertips: pilot study of an mHealth intervention for work-related stress amo |
| 13 | 2024 | Y | Beiwe/mindLAMP | `10.2196/59974` | Mobility-Based Smartphone Digital Phenotypes for Unobtrusively Capturing Everyday Cognition, Mo |
| 13 | 2025 | Y | Beiwe/mindLAMP | `10.1016/j.inpsyc.2025.100123` | Barriers and facilitators to usability of a smartphone-based digital mental health tool in olde |
| 13 | 2025 | Y | Beiwe | `10.2196/71377` | Feasibility of Collecting and Linking Digital Phenotyping, Clinical, and Genetics Data for Ment |
| 13 | 2025 | Y | Beiwe | `10.1007/s12671-025-02631-7` | Exploring Visceral Body Scan, Somatosensory Body Scan, and External Meditation: A Randomized Co |
| 13 | 2024 | N | Beiwe | `10.1093/milmed/usae144` | Evaluating the Acceptability and Feasibility of Collecting Passive Smartphone Data to Estimate  |
| 12 | 2025 | Y | Beiwe/mindLAMP | `10.1038/s41537-025-00660-8` | Mobile cognitive remote assessment of schizophrenia: a global multi-site pilot study |
| 12 | 2025 | Y | Beiwe | `10.2196/69749` | Implementing Digital Tools for Mental Health Support in Young Individuals in Colombia: Mixed Me |
| 11 | 2025 | Y | m-Path | `10.1007/s00415-025-13219-5` | Randomised feasibility study evaluating eye movement desensitisation and reprocessing therapy f |
| 11 | 2025 | Y | m-Path | `10.1080/1612197x.2025.2563323` | Feasibility of ecological momentary assessment during cognitive behavioural therapy in athletes |
| 11 | 2025 | Y | m-Path | `10.3758/s13428-025-02777-1` | Fabla: A voice-based ecological assessment method for securely collecting spoken responses to r |
| 11 | 2023 | Y | mindLAMP | `10.1093/jamiaopen/ooad044` | CardinalKit: open-source standards-based, interoperable mobile development platform to help tra |
| 11 | 2022 | Y | Beiwe | `10.2196/25586` | Dose–Response Effects of Patient Engagement on Health Outcomes in an mHealth Intervention: Seco |
| 11 | 2020 | Y | Beiwe | `10.1093/jamia/ocaa007` | Self-monitoring diabetes with multiple mobile health devices |
| 11 | 2023 | Y | Beiwe | `10.2196/47006` | Digital Phenotyping for Mood Disorders: Methodology-Oriented Pilot Feasibility Study |
| 11 | 2023 | Y | Beiwe | `10.2196/40197` | Utility of Smartphone-Based Digital Phenotyping Biomarkers in Assessing Treatment Response to T |
| 11 | 2018 | Y | Beiwe | `10.1038/s41537-018-0048-6` | A crossroad for validating digital tools in schizophrenia and mental health |
| 11 | 2025 | Y | Beiwe | `10.1200/cci-24-00201` | Feasibility and Acceptability of Collecting Passive Smartphone Data for Potential Use in Digita |

## Corrections to this file's own candidate list (2026-09-02)

The caveat below about citation ≠ deployment was borne out immediately. Three candidates were
attributed to the wrong platform by this pass's screening, all caught on full-text reading:

| Candidate | This file said | Full text says |
|---|---|---|
| **Shen et al. 2026**, *Innovation in Aging*, `10.1093/geroni/igag007` | Beiwe / mindLAMP / RADAR-base — "a rare cross-platform guide" | **None of the three.** A bespoke iOS app on **Apple SensorKit** (TechSANS); Beiwe is a later, unanalysed Android build |
| **Mahmood et al. 2026**, *JMIR Formative Research*, `10.2196/84618` | Beiwe | **No phenotyping platform deployed at all** — VPN-based network-traffic sensing. Beiwe appears once, as a background citation |
| **Van der Donckt et al. 2024**, `10.1038/s41598-024-67767-3` | RADAR-base | An **Empatica E4** tooling paper. Rejected from Module 3 on scope (no new deployment cohort) |

**The rate matters: 3 of the first ~12 candidates examined were mis-attributed.** Citation-graph
discovery finds papers that *cite* a platform, and background citations are common. Treat every
platform attribution in the table above as **Reported** until confirmed from full text — this is not
a theoretical caveat.

A separate retrieval note: **PMC's JATS `contrib-group` for JMIR articles lists handling editors
before authors.** Parsing it naively returns non-authors as the first names on the byline. Use the
PDF byline as authoritative.

## Caveats

- **Screening is abstract-based only.** No full texts were read in this pass; every characterisation
  is **Reported** pending verification.
- **Citing a platform's methods paper does not prove the platform was used.** Many citations are
  background or related-work references. Verify from full text before profiling — the same error
  class that produced two wrong device attributions in the baseline pass.
- **Beiwe dominates the yield (47 of 71)**, an artefact of its anchors having far more citations
  (806 + 735 + 85) than the others. This does **not** mean Beiwe deployments are more common in
  proportion; it means the anchor set is unbalanced. Do not read the platform counts as a measure of
  relative platform activity, and do not build out the Beiwe candidates without a matching pass on
  the others — the same tilt risk recorded in `_inventory-and-scope-decisions.md`.
- MetricWire and Avicenna/Ethica have **no usable anchor paper** — both are commercial platforms
  without a canonical methods citation — so citation-graph discovery does not work for them. They
  remain reachable only by name-based search, which for them is adequate (their names are
  distinctive enough).
