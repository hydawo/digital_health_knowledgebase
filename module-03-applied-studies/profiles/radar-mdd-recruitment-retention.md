# Matcham et al. 2022 — RADAR-MDD: recruitment, retention and data availability, N=623, 3 countries, up to 24 months

## Quick Facts

| Field | Details |
|---|---|
| Citation | Matcham F, Leightley D, Siddi S, Lamers F, White KM, Annas P, de Girolamo G, et al., on behalf of the RADAR-CNS consortium. "Remote Assessment of Disease and Relapse in Major Depressive Disorder (RADAR-MDD): recruitment, retention, and data availability in a longitudinal remote measurement study." *BMC Psychiatry* 2022;22:136. DOI [10.1186/s12888-022-03753-1](https://doi.org/10.1186/s12888-022-03753-1). PMID 35189842 / PMC8860359. |
| Study design | Multi-centre prospective observational cohort (naturalistic; no withdrawal for non-provision of sensor data) |
| Sample size (enrolled / analyzed) | **623 enrolled** (target was 600); 445 (71.4%) provided outcome data at 1-year; 181 (29.1%) participated a full 2 years; 497 (79.8%) participated for the maximum time available to them; **126 (20.2%) withdrew prematurely** |
| Population | Adults ≥18 with recurrent, non-psychotic MDD (≥2 lifetime episodes, most recent within 2 years). Skewed White and female relative to the general and depressed populations — the authors flag this as a generalisability limit. |
| Duration | Recruitment Nov 2017 – Jun 2020 (30 months); follow-up 11–24 months per participant; **median participation 541 days** (IQR 401–730, range 0–1217). Data collection ended Apr/May 2021. |
| Devices/platforms used | [RADAR-base](../../module-02-digital-phenotyping/profiles/radar-base.md) (passive + active apps), **Fitbit Charge 2/3** ([Fitbit/Google profile](../../module-01-wearables/profiles/fitbit-google.md)), THINC-it® cognitive app, REDCap for 3-monthly outcomes |
| Funding/COI | IMI2 Joint Undertaking grant 115902 (EU Horizon 2020 + EFPIA). **Substantial industry co-authorship**: employees of H. Lundbeck A/S (JCB, PA) and Janssen (QL, NM, SV, VN, NVM, several holding company stock). Funder stated as not involved in design/collection/analysis. |
| Last verified | 2026-08-31 |

## Summary

The single most useful deployment-reality paper in the digital-phenotyping literature, and the
reference point against which other multimodal remote-measurement studies should be read. RADAR-MDD
is the largest multimodal remote measurement technology (RMT) study in mental health, and — unusually
— it was written up explicitly to report *how the deployment went* rather than what it found
clinically. It reports recruitment, withdrawal reasons, and per-stream data availability across
active app tasks, smartphone passive sensing, and a wrist wearable, over a median 1.5 years per
participant across three countries.

The headline is a genuine two-part finding. Retention against *researcher-administered* outcomes was
excellent (~80% completion at every follow-up timepoint). Availability of *sensor and app-generated*
data was far lower and highly variable by stream — and only **110 participants (17.7%) had >50% of
expected data across all data types simultaneously**. For any study design that depends on
multi-stream fusion, that second number is the one that governs feasibility, not the retention rate.

## Instrumentation and Deployment Model

- **Platform:** RADAR-base, running two separate apps — a passive monitoring app (pRMT) and an
  active monitoring app (aRMT).
- **Passive smartphone streams:** ambient noise, ambient light, location/GPS, app usage, Bluetooth
  connectivity, phone usage, battery level. Most data available for **GPS location and battery
  level**; least for **phone usage**.
- **Active tasks:** PHQ-8 and Rosenberg Self-Esteem Scale every 2 weeks (max 52 responses); a
  speech task every 2 weeks (a phonetically balanced Aesop passage plus a free-response question);
  and an ESM protocol delivering brief mood/stress/sociability items several times daily for 6-day
  bursts.
- **Cognitive tasks:** THINC-it® app every 6 weeks (PDQ-5 plus four computerised tasks), a
  **third-party app integrated into RADAR-base rather than native to it** — this turns out to matter
  a great deal (see below).
- **Wearable:** Fitbit Charge 2/3, researcher-provided and **kept by the participant at study end**
  (a deliberate retention incentive worth noting for budgeting).
- **Outcomes:** primary/secondary outcome questionnaires delivered 3-monthly by REDCap, separate
  from the RMT stack.
- **Deployment model: researcher-provisioned wearable, participant-owned phone — but Android only.**
  Eligibility required an existing Android phone *or willingness to switch to Android as the
  participant's only phone*. This is a RADAR-base architectural constraint surfacing as an
  eligibility criterion, and it produced measurable attrition (below).

## Recruitment and Retention

Recruitment used multiple channels — existing consented research cohorts (UK and NL), primary and
secondary mental health services (UK, Barcelona), charity websites, circulars, and Twitter — and
mixed face-to-face with remote enrolment. It **exceeded its target of 600 despite the COVID-19
pandemic**, which the authors attribute to that channel and modality flexibility.

Retention:

| Measure | Value |
|---|---|
| Completion rate, primary/secondary outcomes, among those eligible at each timepoint | **~80% at all follow-up timepoints** |
| Participated for maximum time available | 497 / 623 (**79.8%**) |
| Withdrew prematurely | 126 / 623 (**20.2%**) |
| Provided outcome data at 1 year | 445 (71.4%) |
| Participated a full 2 years | 181 (29.1%) |

**Reasons for withdrawal** (the most decision-relevant table in the paper):

- **Loss to follow-up — n=47 (37.3% of all withdrawals)**, the single largest category.
- **Problems using the Android study phone, among those who had switched from an iPhone for the
  study — n=14 (11.1% of all withdrawals).** An Android-only platform requirement cost this study
  roughly one in nine of its withdrawals.
- Study burden — n=8 total: "too demanding" (n=6), "not meeting expectations" (n=2). Notably small.

The authors situate ~80% against published conventions where 50/60/70% follow-up is described as
adequate/good/very good, and argue this represents excellent availability of the primary outcomes.

## Data Completeness and Technical Issues

**2.9 TB of compressed data** were collected in total. Availability differed sharply by stream.

**Active app data (aRMT) — strong:**

| Stream | Participants with *any* data | Median completed |
|---|---|---|
| PHQ-8 | 95.3% | 21 (IQR 9–31) of max 52 |
| RSES | 94.5% | 20 (IQR 9–30) |
| Speech task | 82.2% | 12 (IQR 2–23) |

**Cognitive tasks (THINC-it®) — weak.** Over 84% of participants had *any* data (PDQ5 90.5%, Code
Breaker 84.4%, Spotter 84.8%, Symbol Check 84.6%, Trails 89.9%), but **~60% of participants had
<26% of expected data**, and medians were only ~5 completions each. The authors give three
explanations, all of them transferable design lessons:

1. **Integration lag and sync loss.** THINC-it data only began arriving in March 2018 — the first
   four months of the study have no cognitive data at all — and there were early sync failures
   between THINC-it and RADAR-base, with potential data loss.
2. **App-switching cost.** THINC-it is a separate app with different branding and feel; it has **no
   inbuilt notification system**, so notifications came from the RADAR-base aRMT app and the
   participant had to switch apps to comply. Every additional hop is a place to lose motivation.
3. **Task burden.** Cognitive tasks demand more attention than questionnaires, plausibly harder for
   symptomatic participants.

**Wearable (Fitbit) — moderate and declining:**

- **Mean wear-time 62.5% (SD 9.1pp) across a median 541 days**, i.e. **15.1 h/day (SD 2.2)**.
- **Wear-time decreased over time**; a visible trough between study days ~290–380.
- Data availability was highly stream-dependent: **step count was the best-covered stream (~50% of
  participants supplied >75% of expected data)**, while **Fitbit "activity" data was the worst
  (only ~5% of participants at >75%)** — and activity was the *only* stream where baseline
  depression status made a significant difference (χ²=14.1, p=0.002), with symptomatic participants
  disproportionately in the <26% band. Activity data mixes Fitbit's proprietary algorithm output
  with manual participant entry, which likely explains both its poor coverage and its sensitivity
  to symptom state.
- Collection depended on a three-link chain that the authors make explicit: participant wears device
  → participant charges and syncs it → **Fitbit's servers return the data**. The third link is
  outside the research team's control.

**Cross-stream completeness — the key number:** only **110 participants (17.7%) had >50% of expected
data across all data types**. The authors frame this directly as an indicator of how much
recruitment and data collection is required to support genuinely multiparametric analysis.

**Documented technical failure modes:**

- **OS-level attrition of data streams mid-study.** Google Play Store permission changes in
  **January 2019 removed access to text and call log data entirely** — at a point when one site had
  recruited only 30 participants and another had not started. Those streams are unreportable for
  this cohort. This is the clearest documented case of a platform vendor deleting a planned data
  stream out from under a running study.
- **Iterative app changes during live collection.** RADAR-base and its apps were developed and
  piloted *within* the main data collection period, with continual updates (some forced by Android
  OS changes). The authors state plainly that a participant running 2019–2020 had a different user
  experience from one running 2020–2021 — a within-study measurement-heterogeneity problem, not just
  an inconvenience.
- **Cross-app sync failures** (THINC-it, above).
- **Aggregation heterogeneity:** each stream has different temporal validity and aggregation
  requirements (sleep midday–midday vs. activity midnight–midnight; heart rate every ~5s vs.
  GPS aggregation that depends on the handset). There is no single correct way to summarise
  availability across streams.

Missing data were **not** handled by withdrawing non-compliant participants — a deliberate design
choice to preserve a truthful picture of fluctuating adherence. The authors also deliberately use
"availability" rather than "completeness", because their counts include partial and corrupted data.

## Feasibility Findings

The study's own conclusion: collecting RMT data from a clinical population **is feasible**, and
active and passive collection are **comparably** feasible in this group — a finding that cuts
against the common assumption that passive collection is inherently more reliable because it asks
less of the participant.

Two qualifications the authors state themselves:

- **Availability depends on data type, and burden is the discriminator** — higher-burden sources
  (cognitive tasks; keeping a wearable charged) yield less data.
- **Baseline depression severity did not predict data availability** (no significant association for
  PHQ-8, RSES, speech, any THINC-it task, any passive sensor, or Fitbit wear-time; activity data was
  the lone exception). This is a substantively important negative result: the widespread worry that
  depressed participants will systematically under-supply data was not borne out at baseline. The
  authors note that *time-varying* symptom state may still predict adherence, and flag missingness-
  as-relapse-signal as future work.

Explicit recommendation for future study design: participants had **close contact with the research
team throughout** — technical support, questionnaire reminders, and risk assessments (341 risk
assessments were conducted, 9.0% of 3777 depression measurements). The authors state that future
work must establish **the minimum research-team contact time required to obtain usable data**,
because the staffing model here is not obviously viable for real-world implementation. Treat the
availability figures in this paper as an *upper bound conditioned on a well-staffed support model*.

## Relevance to Future Study Design

What a future study team should take from this before choosing a RADAR-base + consumer-wearable
design:

1. **Budget for retention against outcomes and completeness against sensors separately.** ~80%
   outcome retention and 17.7% cross-stream >50% completeness came out of the same study. If the
   analysis plan requires several streams simultaneously per participant, size the study off the
   second number.
2. **Platform-imposed OS restrictions are an eligibility criterion and an attrition source.**
   RADAR-base's Android requirement forced iPhone users to switch phones, and difficulty with the
   switched phone was the second-largest withdrawal reason (11.1%). Any platform without genuine iOS
   parity carries this cost.
3. **Do not integrate a third-party task app without native notification support.** THINC-it's
   ~60%-of-participants-under-26%-completeness is the clearest natural experiment available on what
   app-switching costs in a long study.
4. **Assume vendor and OS policy changes will delete streams mid-study.** Plan streams so that the
   loss of call/SMS metadata (or any similarly permission-sensitive stream) does not invalidate the
   primary analysis.
5. **Wearable wear-time decays.** 62.5% over ~18 months, with a visible slump around months 10–12,
   is a realistic planning figure for a provisioned Fitbit in a clinical cohort — and considerably
   below figures from short (8-week) studies or from general-population studies that filter out
   low-wear days. The authors explicitly criticise Radin et al.'s much higher 22.6 h/day figure as
   inflated by excluding days under 1000 minutes of wear.
6. **Letting participants keep the device** and running an actively staffed support desk are part of
   why these numbers look as good as they do; they are cost lines, not free.

## Evidence Confidence

**Verified** for all feasibility, retention, withdrawal-reason, wear-time, and per-stream
availability figures — these are the paper's primary reported results, drawn from the full text, in
a paper whose stated purpose is exactly this reporting.

Two caveats on *interpretation* rather than on the numbers:

- **COVID-19 confounding is acknowledged but not quantified.** Most recruitment predates the
  pandemic but follow-up spans it; the authors expect it may have increased dropout and reduced
  adherence, and defer the analysis to other work. Retention figures should be read as
  pandemic-affected.
- **Industry co-authorship is substantial** (Lundbeck and Janssen employees among the authors, some
  holding equity), though the reported findings are operational rather than product-favourable, and
  the funder is stated not to have been involved in design, collection, or analysis. The
  device vendor (Fitbit) is not a funder or author — so the wear-time findings in particular carry
  no vendor-favourability concern.

## Key Links

- Paper (OA): https://doi.org/10.1186/s12888-022-03753-1
- Europe PMC: https://europepmc.org/article/MED/35189842
- RADAR-CNS consortium: https://www.radar-cns.org
- Protocol paper (referenced as [18] in this paper): see `../sources.md`
- Local PDF: `../literature/2022-matcham-bmcpsychiatry-radar-mdd-recruitment-retention.pdf`

## Related profiles

- Platform: [RADAR-base](../../module-02-digital-phenotyping/profiles/radar-base.md)
- Device: [Fitbit / Google](../../module-01-wearables/profiles/fitbit-google.md)
- Companion analyses of the same cohort: [`radar-mdd-longterm-engagement.md`](radar-mdd-longterm-engagement.md)

## Sources

1. Matcham F, et al. *BMC Psychiatry* 2022;22:136. DOI 10.1186/s12888-022-03753-1. Full text
   retrieved from Europe PMC (PMC8860359), 2026-08-31. Establishes every figure in this profile.
