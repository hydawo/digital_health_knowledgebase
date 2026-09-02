# Böttcher et al. 2022 — Data quality in wearable seizure monitoring across four epilepsy centres, 632 inpatients + 39 outpatients, 128,000 hours

## Quick Facts

| Field | Details |
|---|---|
| Citation | Böttcher S, Vieluf S, Bruno E, Joseph B, Epitashvili N, Biondi A, Zabler N, Glasstetter M, Dümpelmann M, Van Laerhoven K, Nasseri M, Brinkman BH, Richardson MP, Schulze-Bonhage A, Loddenkemper T. "Data quality evaluation in wearable monitoring." *Scientific Reports* 2022;12:21412. DOI [10.1038/s41598-022-25949-x](https://doi.org/10.1038/s41598-022-25949-x). PMC9741649. |
| Study design | Multi-centre secondary analysis proposing and applying a **combined multimodal data-quality assessment tool**; data quality is the outcome, not a diagnostic |
| Sample size (enrolled / analyzed) | **632 inpatients** (37,166 h) and **39 outpatients** (90,776 h). BCH inpatient cohort: 832 recordings from 415 individual patients (multiple admissions and simultaneous devices). |
| Population | People with epilepsy at four centres: **Boston Children's Hospital (BCH)**, **King's College London (KCL)**, **Medical Center University of Freiburg (UKF)**, and a fourth (MCR) cohort |
| Duration | Inpatient recordings (hours to days); outpatient follow-up planned at **6 months** |
| Devices/platforms used | **[Empatica](../../module-01-wearables/profiles/empatica.md) E4** wristband — accelerometry (ACC), electrodermal activity (EDA), blood volume pulse (BVP), skin temperature (TEMP) |
| Funding/COI | Academic multi-centre consortium (Freiburg, Siegen, Boston Children's/Harvard, King's College London, Mayo). |
| Last verified | 2026-08-31 |

## Summary

The only study in this module where **data quality is the primary outcome**, applied across four
independent sites and ~128,000 recorded hours — and it isolates a single design decision that
dominates everything else.

**Recording mode is the dominant determinant of data loss.** Cohorts using the device's **onboard
memory** recorded with **data loss consistently below 10%**. Cohorts using **live data streaming**
lost **up to ~50% on average**, with individual recordings ranging from almost nothing captured to
everything captured. The difference is highly significant (p<0.001), and the authors state plainly
that "the recording mode of the device had the highest impact on data loss."

The second finding is reassuring and separates two things usually conflated: **on-body scores were
consistently above 80% across every cohort**, with low between-individual variance. **Participants
wore the device. The system lost the data.** Compliance and completeness are distinct failure modes,
and this study is the cleanest demonstration of that distinction anywhere in the module.

## Instrumentation and Deployment Model

**Empatica E4** wristband recording four modalities: ACC, EDA, BVP and TEMP. Two recording modes are
compared — **onboard memory storage** versus **live streaming**.

**Device placement varied by clinical need.** In the BCH inpatient cohort, devices were worn on the
**wrist (N=383)** or the **ankle (N=447)** — ankle placement being an alternative **for children with
small wrists**, with placement otherwise determined by patient tolerability in consultation with the
care team. Some patients wore two devices simultaneously (one wrist, one ankle).

**The assessment tool itself** is the paper's contribution, and its three-layer structure is
reusable:

1. **Data completeness** — proportion of expected samples actually present between recording start
   and end. Strictly defined as presence/absence of samples.
2. **On-body score** — estimated percentage of time the device was actually worn, derived from
   modality signatures. Off-body periods are characterised by **a temperature drop in TEMP, random
   noise or regular oscillations in BVP, and low amplitude in ACC variance and EDA**.
3. **Modality-specific signal quality** (EDA, BVP, TEMP), scored **only over periods already
   estimated as on-body** — so signal quality is not contaminated by off-body time.

That layering matters: completeness, wear, and signal quality are three separate questions, and
reporting only one of them (as most studies do) hides the others.

## Data Completeness and Technical Issues

**Per-cohort results (inpatient), mean / median:**

| Cohort | N | Completeness | On-body | EDA quality | BVP quality | TEMP quality |
|---|---|---|---|---|---|---|
| **BCH** | 415 patients (832 recordings) | **98.4% / 100.0%** | 88.3% / 99.7% | 68.9% / 75.9% | 60.6% / 63.3% | 95.5% / 99.4% |
| **KCL** | 29 | **51.5% / 49.6%** | 82.4% / 93.9% | 62.7% / 67.2% | 51.5% / 52.0% | 92.4% / 99.3% |
| **MCR** | 19 | **97.9% / 100.0%** | 99.0% / 100.0% | 78.4% / 91.9% | 63.2% / 58.5% | 99.9% / 100.0% |

The KCL cohort — the streaming cohort — has a **mean completeness of 51.5% with an SD of 26.5 and a
range from 1.9% to 97.5%.** Its on-body score (82.4%) is comparable to the others. Participants at
KCL wore the device essentially as well as everyone else and roughly half the data never arrived.

**Signal quality is modality-dependent and consistently ordered: TEMP (92–100%) ≫ EDA (63–78%) > BVP
(51–63%).** BVP — the photoplethysmography stream, and the one most studies actually want for heart
rate and HRV — was the **worst-quality modality in every cohort**, never exceeding a 63% mean.

**Device placement:** wrist versus ankle **made no meaningful difference to completeness or on-body
scores** (means differed by 0.1%). But **signal quality at the wrist was *lower*** — BVP by 4.7%
(p<0.001) and TEMP by 2.1% (p=0.015). Ankle placement was not a compromise.

**Time of day:** signal quality for some modalities was **higher at night than during the day**,
attributed to less movement and variability during sleep. A **diurnal cycle is visible** in the
quality scores themselves.

**Outpatient dropout:** several participants left before completing the planned 6-month follow-up
(**KCL 5/15; UKF 1/12**), and for others the follow-up was **deliberately shortened to 3 months**
(KCL 3/15; UKF 1/12). Their data were retained in the quality assessment.

**All modalities were affected by artifacts**, and the authors note that artifacts have different
multimodal signatures — which is what makes simultaneous multi-modality assessment more informative
than per-stream checks.

## Feasibility Findings

The authors' conclusion is a methodological call: **a uniformly reported data-quality and multimodal
signal-quality index is feasible, makes study results comparable, and is necessary for developing
seizure-monitoring devices and evaluation routines.** They open by noting that raw data quality "is a
frequently underreported aspect in clinical studies employing these wearables, especially in
quantitative terms" — a criticism this module's other profiles repeatedly bear out.

They also note that **moving to an ambulatory setting may further amplify data loss**, though their
outpatient EDA quality was slightly *better* than inpatient at one site.

## Relevance to Future Study Design

1. **Record to onboard memory, not live streaming, unless real-time access is genuinely required.**
   <10% loss versus up to ~50%. This is the largest single controllable effect on data yield
   documented anywhere in this module, and it is a configuration choice.
2. **If streaming is required, budget roughly half the data** — and expect enormous
   between-participant variance (1.9% to 97.5% completeness at KCL).
3. **Report completeness, on-body time, and signal quality separately.** Conflating them makes an
   infrastructure failure look like a compliance failure. Here, 82% on-body coexisted with 51%
   completeness.
4. **Expect PPG/BVP to be your weakest modality** (51–63% quality) and skin temperature your
   strongest (92–100%). Design endpoints accordingly, and be sceptical of studies reporting
   wrist-PPG-derived metrics without a signal-quality denominator.
5. **Ankle placement is a legitimate alternative to the wrist** — no completeness penalty, and
   slightly *better* BVP and TEMP quality. Useful for paediatric cohorts and anyone with wristband
   tolerance problems (see [RADAR-AD](radar-ad-feasibility-usability.md)).
6. **Signal quality varies diurnally.** Analyses comparing day and night periods must adjust for
   quality, or a data-quality artefact will masquerade as a circadian finding.

## Evidence Confidence

**Verified** for all completeness, on-body and signal-quality figures, the recording-mode comparison,
the placement comparison, and the cohort sizes — primary reported results read from the published
PDF.

**One important interpretive caution.** The recording-mode comparison is **between cohorts at
different sites, not randomised within a site.** KCL was both the streaming cohort and a distinct
clinical population and setting. The p<0.001 is real, and the mechanism (streaming loses packets;
onboard storage does not) is highly plausible — but site, population and mode are confounded, so
this is **Corroborated** rather than experimentally isolated. The effect size is large enough that
the direction is not in doubt.

**Scope note:** this study sits near the validation boundary that `CLAUDE.md` uses to separate
Module 1 from Module 3, and was flagged as an ambiguous inclusion in
[`../_inventory-and-scope-decisions.md`](../_inventory-and-scope-decisions.md). It is here because
its unit of analysis is **data completeness across a multi-centre deployment**, not sensor accuracy
against a reference standard. Signal-quality indices for the E4's individual modalities belong in
[`../../module-01-wearables/validation-evidence.md`](../../module-01-wearables/validation-evidence.md).

**Setting dependence, stated by the authors:** results must be read in the context of their
collection setting; inpatient monitoring-unit conditions differ substantially from free-living
ambulatory use.

## Key Links

- Paper (OA): https://doi.org/10.1038/s41598-022-25949-x
- Europe PMC: https://europepmc.org/article/PMC/PMC9741649
- Local PDF: `../literature/2022-scientificreports-wearable-monitoring-data-quality-epilepsy.pdf`

## Related profiles

- Device: [Empatica](../../module-01-wearables/profiles/empatica.md)
- Same device in a psychiatric deployment:
  [`sleepsight-schizophrenia-rest-activity.md`](sleepsight-schizophrenia-rest-activity.md)
- Wristband tolerance and placement:
  [`radar-ad-feasibility-usability.md`](radar-ad-feasibility-usability.md)
- Bluetooth-tethered wearable as the fragile component:
  [`dp-schizophrenia-tolerability.md`](dp-schizophrenia-tolerability.md)

## Sources

1. Böttcher S, et al. *Scientific Reports* 2022;12:21412. DOI 10.1038/s41598-022-25949-x. Full text
   and tables read from the published PDF (via Europe PMC, PMC9741649), 2026-08-31. Establishes
   every figure in this profile.
