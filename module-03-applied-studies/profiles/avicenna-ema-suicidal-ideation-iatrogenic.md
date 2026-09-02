# Kivelä et al. 2024 — Acceptability, feasibility and iatrogenic effects of EMA of suicidal ideation (Ethica/Avicenna), N=82

## Quick Facts

| Field | Details |
|---|---|
| Citation | Kivelä LMM, Fiß F, van der Does W, Antypa N. "Examination of Acceptability, Feasibility, and Iatrogenic Effects of Ecological Momentary Assessment (EMA) of Suicidal Ideation." *Assessment* 2024;31(6):1292–1308. DOI [10.1177/10731911231216053](https://doi.org/10.1177/10731911231216053). PMID 38098238 / PMC11292966. |
| Study design | Prospective observational study (part of the larger **SAFE** study) with **acceptability, feasibility, compliance predictors and iatrogenic effects as the explicit aims**. Multilevel models of within-study affect/ideation trajectories plus retrospective participant-report. |
| Sample size (enrolled / analyzed) | **209 signed up → 90 attended intake → 8 excluded → 82 enrolled → 81 completed** (1 dropout, retained in analyses). |
| Population | Adults with **current suicidal ideation** (C-SSRS ≥3, or ≥2 if symptomatic in the past 2 months), recruited online in the Netherlands. Mean age **27 (SD 8.6)**; 77% female, 10% nonbinary/trans; 55% Dutch nationality; 45% highly educated. Excluded: bipolar, psychotic, or severe substance-dependence diagnoses. |
| Duration | **21 days**, 4 prompts/day, up to **40 questions per prompt** — a heavy protocol. (The wider SAFE study added 24h/day actigraphy over the same 3 weeks and a subsequent year of weekly EMA; those are not analysed here.) |
| Devices/platforms used | **[Ethica, now Avicenna Research](../../module-02-digital-phenotyping/profiles/avicenna-research-ethica.md)** — participant-owned Android or iOS smartphone. |
| Funding/COI | Academic — Leiden University, Institute of Psychology. **No platform-developer authorship**; a rare clean-COI entry in a module where developer authorship is pervasive. |
| Last verified | 2026-09-01 |

## Summary

The single most useful entry in this module for anyone who has to *define* what "acceptability" means before quoting a number, because it deliberately publishes **two defensible acceptability rates for the same study that differ by 59 percentage points**:

> **39%** — the share of people who signed up and ultimately started data collection.
> **98%** — the share of eligible people who completed the intake and then started data collection.

Both are honest. Neither is wrong. Which one a reader sees determines whether this looks like a recruitment disaster or a triumph, and the authors' own framing — "our acceptability rate was fairly low" — chooses the pessimistic one.

The study's substantive contribution is on **safety**: over 21 days of four-times-daily suicidal-ideation assessment, **no systematic affect or ideation reactivity appeared in the EMA data itself**, yet **22% retrospectively reported mood worsening and 18% reported suicidal-ideation reactivity** — and those participants were identifiable in advance by borderline traits, PTSD, and higher baseline depression, anxiety and ideation severity.

## Instrumentation and Deployment Model

**Pure BYOD.** Possession of an Android- or iOS-compatible smartphone was an eligibility criterion; no devices were provisioned.

**Protocol.** Four prompts/day at pseudo-randomised times within fixed windows (07:00–09:00, 12:00–14:00, 16:00–18:00, 20:00–22:00), with a **reminder 30 minutes after** an unanswered prompt. Response windows: **180 minutes for the morning assessment, 120 minutes** for daytime and evening.

**Three app behaviours the authors document, which materially shape the data:**

- **The app does not allow saving and resuming** — a questionnaire must be completed in one sitting.
- **Partial responses are not saved**; only fully-completed EMA entries were recorded. Compliance is therefore a *completion* rate, not a *start* rate — stricter than [McClaine et al.](aware-chemotherapy-engagement.md)'s ≥50% threshold and comparable to [Dennard et al.](mpath-avatar2-esm-engagement.md)'s 100%-complete rule.
- **Participants could submit unscheduled extra entries at any time.** Visual inspection suggested these were most often filed just after a missed prompt expired, or late in the evening. This is a platform affordance that partially compensates for missed prompts and would inflate a naive "entries collected" count relative to a strict scheduled-prompt denominator.

**Monitoring.** Research staff watched completed/expired survey counts through the **Ethicadata.com (now avicennaresearch.com) web portal**, and participants were told they would receive a **phone call if they filed no EMA for 72 hours**. The authors believe wanting to avoid that call raised compliance.

**Incentive design is unusual and worth copying.** There was no per-response payment. Instead, participants were told at intake they would receive a **personalised feedback report based on their own data**, whose quality depended on how much and how well they responded. None declined it at intake, and **76/82 (93%) ultimately received one.**

## Recruitment and Retention

The funnel, in full:

| Stage | n |
|---|---|
| Signed up online and invited to intake | 209 |
| Attended intake interview | 90 |
| Excluded after interview | 8 (declined 2; no local GP 2; probable bipolar 2; psychotic disorder 1; severe substance dependence 1) |
| **Enrolled and started EMA** | **82** |
| Dropped out during the 21-day EMA period | 1 |
| **Retention** | **99%** |

The **119-person gap between signing up and attending intake** is where the 39% figure comes from, and the authors' explanation is direct: "Online-based recruitment is likely to attract a higher number of people curious about the study rather than serious intent to participate." Their retention (99%) sits above the 60–96% they cite from the literature.

## Data Completeness and Technical Issues

**Compliance: M = 78%, Median = 84%** of scheduled EMAs — against a cited literature median of **70%** across 23 EMA studies of suicidal ideation (Kivelä et al. 2022).

**Predictors of lower compliance** — and note that the significant ones are *not* the ones usually assumed:

| Factor | Result |
|---|---|
| Student status | **Students 74% vs non-students 83%**, t(79)=2.12, P=.037, d=0.47 |
| Current anxiety disorder | **75% vs 84%**, t(79)=2.00, P=.049, d=0.45 |
| Borderline personality traits (PAI-BOR) | P=.056 (not significant) |
| Suicide attempt history | P=.846 |
| Baseline depression (BDI) | P=.628 |
| Baseline suicidal ideation (BSSI) | P=.223 |
| Baseline anxiety symptoms (HADS-A) | P=.302 |
| Insomnia severity (ISI) | P=.743 |
| Quality of life (Q-LES-Q-SR) | P=.833 |

**Symptom severity did not predict compliance; a diagnosis and an occupation did.** The anxiety-disorder finding lines up with the module's cross-cutting pattern that anxiety, not disease severity, predicts disengagement.

**Morning prompts had the lowest compliance**, which the authors attribute partly to their own 3-hour window and to chronotype, and partly to a documented general tendency for morning assessments to underperform.

**Post-test questionnaire compliance was only 71%**, and the authors flag this as a likely upward bias in their post-test ideation improvement — those in a better state were likelier to complete it.

## Feasibility Findings

**Within-EMA reactivity: none detected.** No systematic positive- or negative-affect reactivity, and no systematic ideation trajectory, across 21 days.

**Retrospective self-report tells a different story:**

| Retrospective rating | Share |
|---|---|
| Rated the overall experience as positive | **69%** |
| Reported mood worsening | **22%** |
| Reported suicidal-ideation reactivity | **18%** |

**Who reported iatrogenic effects:** participants with **more borderline personality traits, PTSD, and higher depressive, anxiety and suicidal-ideation symptom severity**. The authors' conclusion is carefully bounded: EMA is well tolerated in suicide research, *and* a identifiable minority report subjective mood effects afterwards.

The divergence between the objective and subjective measures is itself the finding. A study that only modelled its EMA trajectories would have concluded "no reactivity" and missed a fifth of its participants reporting harm.

## Relevance to Future Study Design

1. **State the denominator whenever you state an acceptability rate.** 39% and 98% describe the same study. This module's [`feasibility-matrix.md`](../feasibility-matrix.md) warning about non-standardised definitions has no cleaner illustration.
2. **Online sign-up inflates the top of the funnel and predicts nothing.** If a study is powered off sign-ups, it will be under-recruited; if it is powered off post-intake eligibility, it will be roughly right.
3. **A personalised feedback report is a viable non-cash incentive.** 78% mean compliance on a 21-day, 4×/day, up-to-40-item protocol, with no per-response payment, is at the high end of this module. Note the trade: the report is itself a potential intervention, and the authors concede it may have driven their post-test ideation improvement.
4. **Ask retrospectively about harm; do not infer it from the data.** No modelled reactivity, 22% self-reported mood worsening.
5. **Screen for the iatrogenic-risk profile at baseline** (BPD traits, PTSD, higher symptom severity) — not to exclude, but to plan check-ins.
6. **Check whether the platform saves partial responses**, because it determines what "compliance" can even mean. Ethica/Avicenna did not, at the time of this study; it also permitted unscheduled extra entries, which cuts the other way.

## Evidence Confidence

**Verified** — the complete participant funnel, both acceptability figures and their definitions, the 99% retention, the 78%/84% compliance figures, every compliance predictor with its test statistic, the three retrospective percentages, the null within-EMA reactivity result, and the platform behaviours (no save/resume, no partial saves, unscheduled entries, 72-hour call rule, feedback-report incentive). Read from the full text (Europe PMC PMC11292966), 2026-09-01.

**Reported** — the authors' attributions for high compliance (feedback-report incentive, desire to avoid the 72-hour phone call, self-selection). Plausible and internally consistent, but not experimentally isolated; no arm varied them.

**Unclear** — how much the personalised feedback report acted as an intervention rather than an incentive. The authors raise this themselves as an alternative explanation for their post-test ideation reduction and cannot resolve it.

**Stated limitations:** the sample self-selected heavily (only 43% of sign-ups attended intake); post-test compliance was 71%, biasing the post-test comparison; response content was deliberately **not** monitored in real time, which the authors note is generally recommended but can suppress honest reporting.

**COI:** none identified relating to the platform. The authors are clinical-psychology researchers at Leiden with no stated relationship to Ethica/Avicenna, and the paper does not evaluate the platform as such — it evaluates a method. This makes its platform-behaviour observations unusually credible.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.1177/10731911231216053
- Europe PMC: https://europepmc.org/article/PMC/PMC11292966
- Platform: https://avicennaresearch.com/ (formerly ethicadata.com)
- Local PDF: `../literature/2024-kivela-assessment-ema-suicidal-ideation-iatrogenic-effects.pdf`

## Related profiles

- Platform: [Avicenna Research (Ethica)](../../module-02-digital-phenotyping/profiles/avicenna-research-ethica.md)
- Same population, complementary qualitative evidence on reactivity: [`metricwire-post-discharge-ema-reactivity.md`](metricwire-post-discharge-ema-reactivity.md)
- Missingness as signal in a suicidal-ideation cohort: [`beiwe-inpatient-suicide-pilot.md`](beiwe-inpatient-suicide-pilot.md)
- Strict vs lenient completion definitions: [`aware-chemotherapy-engagement.md`](aware-chemotherapy-engagement.md), [`mpath-avatar2-esm-engagement.md`](mpath-avatar2-esm-engagement.md)

## Sources

1. Kivelä LMM, Fiß F, van der Does W, Antypa N. *Assessment* 2024;31(6):1292–1308. DOI 10.1177/10731911231216053. Full text read from Europe PMC (PMC11292966), 2026-09-01. Establishes every figure in this profile.
