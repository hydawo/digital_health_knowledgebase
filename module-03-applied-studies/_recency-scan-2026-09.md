# Module 3 — Recency scan (date-sorted discovery), 2026-09-01

**Purpose.** The initial Phase 1 discovery sorted by citation count, which structurally under-samples
recent work. This pass re-ran the same 20 technology queries **sorted by publication date**, restricted
to **first publication on or after 2024-06-01**, to close that gap.

## Result: the bias was real

- **64 candidates** screened in (same screening rules as Phase 1: digital-health context term,
  ≥2 deployment-reality signals, non-review, validation-flagged titles dropped), excluding the 19 already
  profiled.
- **62 of 64 (96%) had NOT been surfaced by the citation-sorted pass at all.**

This confirms the bias flagged in `_inventory-and-scope-decisions.md` and means the Phase 1 baseline
should be read as covering *well-established* deployments, not current practice.

## Per-platform yield for the five previously uncovered Module 2 platforms

This pass was run partly to find deployment studies for the platforms with no Module 3 entry. The
honest result is mixed, and the nulls are themselves findings:

| Platform | Recent candidates | Note |
|---|---|---|
| **MetricWire** | **7** | Best yield. Several EMA engagement/feasibility studies. |
| **Avicenna / Ethica** | **5** | Needs manual verification — 'Avicenna' is highly ambiguous. |
| **m-Path** | **1** | Single candidate. |
| **AWARE** | **0 usable in this scan — CONCLUSION OVERTURNED, see below** | This scan found only a false positive. A follow-up pass found **≥7 qualifying AWARE deployments and profiled 3**. The null was an artefact of this scan's method, not of the literature. |
| **CARP Mobile Sensing** | **0** | No qualifying candidate found. |

### CORRECTION (2026-09-01, after the uncovered-platforms pass)

**The AWARE null was wrong, and the reason matters more than the result.**

This scan queried AWARE as a **quoted phrase set** (`"AWARE framework" OR "AWARE app" OR "AWARE
Light" OR "AWARE-Light"`), which returned **579 hits** in the date window — not zero. The failure was
downstream: **Europe PMC does not honour the phrase quoting for this term**, matching `aware` and
`framework` as loose tokens instead. Date-sorting then surfaced pure noise — the 60 most recent hits
are titles like "Geometry-aware Gaussian primitives", "Wavefield-Aware quality control",
"causality-aware interpretable modeling". Genuine AWARE deployments never entered the retrieved
window, and the one that did was a false positive.

A follow-up pass found **≥7 qualifying AWARE deployments and profiled 3**. See
[`_uncovered-platforms-report.md`](_uncovered-platforms-report.md).

**The CARP null is real, but structural rather than evidentiary.** CARP Mobile Sensing (CAMS) is a
**Flutter library embedded inside other people's apps**, so its deployments publish under the
application's name — m-Path Sense, DiaFocus, mCardia, Wrist Angel — and never name CARP in the
title or abstract. Five Europe PMC query forms, arXiv and OpenAlex were tried; only an **OpenAlex
citation-graph pass** found the ecosystem. One qualifying deployment was profiled.

**The generalisable lesson for this module's discovery method:** platform-name search
**structurally cannot find framework-shaped platforms**, and **cannot filter platforms whose name is
an ordinary English word** when the index ignores phrase quoting. Both classes need citation-graph or
ecosystem-based discovery instead. Any future null from a name-based query should be treated as
unproven until a citation-graph pass has been run.

## Highest-value recent candidates (top 30 by screening score)

| Date | Technologies | OA | DOI | Title |
|---|---|---|---|---|
| 2026-07-07 | apple-watch/fitbit/samsung | N | `10.2196/86049` | Evaluating Wearable Devices for Remote Monitoring in Psychosis: Pilot Study Nested Within the CONNECT Coh |
| 2024-09-12 | beiwe | Y | `10.1186/s44247-024-00116-6` | "Anything that would help is a positive development": feasibility, tolerability, and user experience of s |
| 2026-01-28 | beiwe/mindlamp/radar-base | Y | `10.1093/geroni/igag007` | Multimodal passive smartphone sensing in older adults: a guide for clinical scientists based upon an ongo |
| 2026-03-01 | avicenna-ethica | Y | `10.1111/jora.70118` | In the moment, out of reach? Experience sampling with adolescents in the context of school smartphone ban |
| 2026-06-05 | garmin | Y | `10.2196/76991` | Automated Physical Activity Support for Adults and Youth From Low-Income Communities: Single-Arm Pilot St |
| 2026-04-21 | axivity-geneactiv/beiwe | Y | `10.1038/s41746-026-02639-w` | Quantifying sleep wake rhythms in the hospital environment with digital technologies. |
| 2026-06-19 | actigraph/fitbit | N | `10.1002/mus.70323` | Comparison of Consumer Smartwatch and Research-Grade Accelerometer-Derived Step Counts in Amyotrophic Lat |
| 2026-06-23 | apple-watch/garmin | Y | `10.1093/pnasnexus/pgag181` | Heart rate synchrony as a marker of real-world social engagement. |
| 2026-07-31 | fitbit | N | `10.3390/ijerph23081003` | Move Toward Recovery: A Feasibility Study for a Physical Activity Intervention to Reduce Post-Surgical Pa |
| 2026-02-10 | avicenna-ethica | Y | `10.1136/bmjopen-2025-113370` | Ecological momentary assessment of daily patient-reported outcomes and actigraphy-measured physical activ |
| 2026-04-02 | withings | Y | `10.2196/77033` | Evaluation of a Contactless Sleep Monitoring Device for Sleep Stage Detection at Home in a Healthy Popula |
| 2026-04-27 | beiwe | Y | `10.2196/84618` | Digital Phenotyping via Passive Network Traffic Monitoring: Prospective Observational Study in University |
| 2026-04-29 | withings | Y | `10.3390/bios16050250` | Unobtrusive Sensing at Home Towards Healthcare 5.0: Technologies, Applications, and Future Directions. |
| 2026-05-27 | polar | Y | `10.1136/bmjopen-2025-115440` | Fun Exercise for Older Adults (FEXO): study protocol for a randomised controlled trial on intrinsic capac |
| 2026-06-11 | oura | Y | `10.2196/77818` | Digital Health Monitoring and Intervention Suite for Stress in Frontline Nurses: Prospective Cohort Trial |
| 2025-12-08 | axivity-geneactiv | N | `10.1037/fsh0001032` | Distress dynamics in patient and partner dyads early after stroke/transient ischemic attack: A pilot feas |
| 2026-02-22 | mindlamp | Y | `10.1038/s41598-026-41435-0` | LINC: a framework for maintaining high-quality passive data in digital phenotyping studies. |
| 2026-05-12 | apple-watch | N | `10.1186/s40814-026-01830-w` | Feasibility of early interval training in patients recovering from heart valve surgery due to infective e |
| 2026-08-13 | actigraph | N | `10.1088/1361-6579/ae87f1` | Comparison of activPAL and ActiGraph measured moderate to vigorous physical activity in people with COPD. |
| 2025-02-07 | beiwe | Y | `10.2196/59161` | Exploring the Relationship Between Smartphone GPS Patterns and Quality of Life in Patients With Advanced  |
| 2025-05-15 | mindlamp | Y | `10.2196/67659` | Mobile Therapeutic Attention for Treatment-Resistant Schizophrenia (m-RESIST) Solution for Improving Clin |
| 2025-05-29 | metricwire | Y | `10.1016/j.beth.2025.05.007` | Engagement in Ecological Momentary Assessment of Suicidal Thoughts and Behaviors: A Mixed Methods Study. |
| 2025-07-23 | whoop | Y | `10.2196/64955` | Inter- and Intrapersonal Associations Between Physiology and Mental Health: A Longitudinal Study Using We |
| 2025-08-08 | avicenna-ethica | Y | `10.2196/65260` | Effects of Information Length and Implementation Intentions on Adherence to Weight Management Strategies: |
| 2025-09-03 | beiwe | Y | `10.2196/71375` | Measuring Psychological Well-Being and Behaviors Using Smartphone-Based Digital Phenotyping: An Intensive |
| 2025-10-03 | radar-base | Y | `10.2196/71145` | A Dual In-Person and Remote Assessment Approach to Developing Digital End Points Relevant to Autism and C |
| 2025-12-02 | metricwire | Y | `10.2196/76741` | Optimizing an App-Based Just-in-Time Adaptive Intervention for Stimulant Use Among Sexual Minority Men Li |
| 2026-01-16 | m-path | Y | `10.1016/j.conctc.2026.101602` | The efficacy of home-based virtual reality exposure therapy as an add-on to behavioral therapy for childr |
| 2026-01-30 | metricwire | Y | `10.2196/87201` | Real-Time Exposure to Intersectional Minority Stressors and Alcohol Use: Protocol for an Ecological Momen |
| 2026-02-06 | samsung | Y | `10.2196/78098` | Evaluating a Wearable-Based Pain Monitoring System in Palliative Cancer Care: Usability and Feasibility S |

## Notable finds

- **Calvert, Lane, Flathers & Torous 2026 — 'LINC: a framework for maintaining high-quality passive data
  in digital phenotyping studies' (*Scientific Reports*, `10.1038/s41598-026-41435-0`).** Directly
  addresses this module's central theme and postdates every baseline study. **High priority.**
- ~~**Shen et al. 2026** — multimodal passive smartphone sensing in older adults (*Innovation in Aging*,
  `10.1093/geroni/igag007`). Spans Beiwe, mindLAMP *and* RADAR-base — a rare cross-platform guide.~~
  **CORRECTED 2026-09-02 from full text: it uses none of those three.** It deploys a **bespoke iOS app
  built on Apple SensorKit** (TechSANS); Beiwe appears only as a later, unanalysed Android build. The
  "cross-platform guide" characterisation came from abstract-level screening and was wrong.
  **Module 3 still has no Beiwe/mindLAMP/RADAR-base head-to-head comparison** — that gap is open.
  Profiled anyway, on its own merits, as this module's first **Apple SensorKit** deployment.
- **McInerney et al. 2024 — Beiwe feasibility/tolerability/user experience (*BMC Digital Health*,
  `10.1186/s44247-024-00116-6`).** Reports retention, feasibility and completeness together.
- ~~**Ball et al. 2025** — engagement in EMA of suicidal thoughts and behaviors (*Behavior Therapy*,
  `10.1016/j.beth.2025.05.007`). MetricWire; mixed methods on engagement.~~ **CORRECTED: this is
  not a MetricWire study.** The full text states **90% (n=90) received EMA through "Realtime EXP" by
  LifeData** and only **10% (n=10) through Catalyst by MetricWire**. Verified against the PMC deposit
  (PMC13289574). Not profiled here. **LifeData is now profiled in Module 2**
  ([`../module-02-digital-phenotyping/profiles/lifedata.md`](../module-02-digital-phenotyping/profiles/lifedata.md)).
  **Naming note:** the product is actually **RealLife Exp** — Europe PMC returns 74 hits for
  `"RealLife Exp"` versus **1** for `"Realtime EXP"`, which is Ball et al.'s own rendering and was
  inherited verbatim into this file. Search on "RealLife Exp" or "LifeData".
- **Mahmood et al. 2026 — digital phenotyping via passive network traffic monitoring (*JMIR Formative
  Research*, `10.2196/84618`).** Novel passive modality; reports retention, adherence and feasibility.
- Several 2026 multi-device comparisons (Apple Watch + Fitbit + Samsung in psychosis; consumer smartwatch
  vs research-grade accelerometer step counts) that would serve the multi-device priority area.

## Caveats

- Screening was **abstract-based only**. No full texts were read in this pass; every characterisation
  above is **Reported** pending verification.
- Several candidates are **protocol papers** with no results yet (flagged in Phase 1 as generally
  out of scope) — e.g. the JMIR Research Protocols entries.
- 'Avicenna', 'AWARE', 'CARP', 'Polar' and 'm-Path' remain ambiguous search terms; the context filter
  removes most false positives but not all. Verify platform usage before profiling.
- Cut-off of 2024-06-01 was chosen to overlap the citation-sorted pass; studies from 2023–mid-2024 that
  are not yet well cited may still be under-represented.
