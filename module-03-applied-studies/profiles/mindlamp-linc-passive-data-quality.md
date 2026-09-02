# Calvert et al. 2026 — LINC: operationalising passive data quality on mindLAMP, N=373 over 2–3 weeks

## Quick Facts

| Field | Details |
|---|---|
| Citation | Calvert E, Lane E, Flathers M, **Torous J**. "LINC: a framework for maintaining high-quality passive data in digital phenotyping studies." *Scientific Reports* 2026;16:10160. DOI [10.1038/s41598-026-41435-0](https://doi.org/10.1038/s41598-026-41435-0). PMID 41724791 / PMC13022485. Published 2026-02-22. |
| Study design | Framework paper (**Launch, Interact, Notify, Correct**) with a **single-arm observational demonstration cohort** and no concurrent control. Data quality is the outcome. |
| Sample size (enrolled / analyzed) | **417 enrolled → 373 analysed.** 19 disqualified (fraudulent or non-US address), 25 withdrew. |
| Population | Young adults 18–24, predominantly college students, **non-clinical** (median PHQ-9 4.0, GAD-7 4.0). 74.3% female (277), 53.1% White (198), 76.9% students (287), **90.3% iOS (337)**. Mean age 21 (SD 1.9). |
| Duration | 2-week observational phase + optional 1-week social-media detox (2–3 weeks total). Recruitment window 03/2024–03/2025. |
| Devices/platforms used | **[mindLAMP](../../module-02-digital-phenotyping/profiles/mindlamp.md)**, BYOD. GPS at 1 Hz, accelerometer at 5 Hz, screen state. **Cortex** (open-source Python) for feature extraction; `GPSmobility` R package for mobility traces. Apple Health / Google Fit installed as intermediaries for step count. |
| Funding/COI | McChord Foundation grant to John Torous. **Platform-developer authorship: Torous leads the mindLAMP/Division of Digital Psychiatry group at BIDMC and the study evaluates his own platform.** Declared: Torous has received research support from Otsuka (unrelated) and advises Boehringer Ingelheim. IRB BIDMC #2023P001009. |
| Last verified | 2026-09-02 |

## Summary

This is the paper this module has been waiting for: it takes the operational practices that every
phenotyping team improvises and never writes down, names them, ships them as reusable checklists and
Python scripts in supplementary materials, and reports what happened when they were applied to a
373-person cohort.

The headline number is **median GPS-based passive data quality of 0.92 (IQR 0.59–0.98)** — the
highest median in any published mindLAMP deployment. For context, the authors tabulate six prior
mindLAMP studies whose medians run **0.12 to 0.80**, with most below 0.60. The study's *first
quartile* (0.59) approaches or exceeds the *median* of most of them.

But the paper's most transferable contribution is not the number. It is three things:

1. **A definition of passive data quality that is cheap to compute and hard to game.** The proportion
   of the day's **144 non-overlapping 10-minute bins** containing at least one GPS ping. Actual over
   expected, against wall-clock time, not against a duty cycle.
2. **A quantified floor.** Below ~50% data quality, GPS-derived features stop being trustworthy — home
   time is underestimated by **two to four hours**, and correlations between home time and screen
   duration, entropy and step count attenuate and destabilise.
3. **The operational cost of achieving it.** **Mean 1.3 troubleshooting contacts per participant**
   (SD 1.2), **468 interventions over roughly a year (~9/week)**, handled by **two research
   assistants**.

The authors are careful, and unusually so for a framework paper, that **none of this is causal**:
there is no control arm, and the cohort is short-duration, non-clinical, young and 90% iOS.

## Instrumentation and Deployment Model

**BYOD on mindLAMP**, GPS at 1 Hz and accelerometer at 5 Hz, configured per device by a research
assistant at onboarding.

The four LINC components, as actually implemented:

**Launch** — a standardised RA-led onboarding: location permission set to "Always Allow" (iOS) /
"Allow all the time" (Android); battery optimisation, low power mode and adaptive battery reviewed
and disabled; Apple Health or Google Fit installed as a data intermediary; sampling rates set on
device. RAs worked from a step-by-step checklist; participants were emailed an annotated-screenshot
version afterwards and repeatedly told to keep the phone charged, not disable location, and **not
force-quit the app**.

**Interact** — a **daily EMA at 7:00 pm** existing specifically to force the app into the foreground,
because "iOS 15+, Android 12+ implement aggressive background process management that restricts
sensor access for apps not regularly used." Plus **weekly personalised data-summary reports** shared
with participants as an engagement lever.

This is the same architectural problem [Beukenhorst et al.](beiwe-als-adherence.md) documented on
Beiwe and [Niemeijer et al.](carp-mpath-sense-performance-study.md) on CARP — and LINC's answer is
the *opposite* of Beiwe's. Beiwe added a **server-side `heartbeat` push** to remove the need for
participant action. LINC deliberately keeps a **participant-initiated daily task** and uses it as the
wake mechanism. Two platforms, two opposite solutions to the same OS constraint. Neither is
zero-touch.

**Notify** — a daily backend Python script computing per-participant quality, with three explicit
flag thresholds: **quality < 0.50**, **0% for 24 h**, or **no EMA for 3 days** (chosen because prior
work found quality declines significantly without app interaction after that point). Flagged
participants were reviewed on the mindLAMP dashboard, which shows last passive/active timestamps and
a GPS-availability heatmap by time and date.

**Correct** — a standardised troubleshooting algorithm: email outreach with an OS-specific checklist
covering (1) disable battery optimisation / low power mode, (2) verify permissions, (3) re-engage via
EMA. Video call available if needed; follow-up monitoring after each intervention.

All checklists, email templates, dashboard scripts and the decision tree are in the supplementary
materials and are explicitly intended for reuse.

## Recruitment and Retention

**417 enrolled → 373 analysed (89.4%).** Two attrition sources are reported separately, and one of
them is notable:

- **19 disqualified as fraudulent or non-US address (4.6% of enrolments).** This is the second study
  in this module to report screening out fraudulent remote participants, after
  [Siebers et al.](metricwire-fraudulent-participation.md). It is now reproduced on a different
  platform, in a different country, with a different detection method — supporting the module's
  finding that remote incentivised recruitment attracts fraud as a routine rather than exceptional
  problem.
- **25 withdrew (6.0%).** No reasons reported.

No enrolment funnel above consent (screened, approached, ineligible) is reported.

## Data Completeness and Technical Issues

**Definition, stated precisely:** passive data quality = proportion of the 144 non-overlapping
10-minute bins in a 24-hour day containing **at least one GPS data point**. Computed daily per
participant; participant-level figures are medians over the study period.

**Distribution across 373 participants:**

| | Value |
|---|---|
| Median (Q2) | **0.92** |
| Q1 | 0.59 — 75.0% (n=279) exceeded this |
| Q3 | 0.98 — 25.0% (n=93) exceeded this |
| Above 0.50 | 79.0% (n=296) |
| Below 0.10 | **14.2% (n=53)** |
| **Exactly zero passive data** | **9.7% (n=36)** |

**Active data (daily EMA completion): median 0.95.** 97.0% above 0.50; Q1 0.81; 37.3% (n=139) at a
perfect 1.0; 1.9% (n=7) completed no surveys at all.

**The definitional caveat is in the paper's own text and matters enormously.** The authors note that
**their companion analysis of the same cohort reports a median passive quality of 0.78 and a median
EMA completion of 0.76 "when using all days in the weekly collection periods."** That is a **14-point
gap on passive and a 19-point gap on active, from the same raw data, from the same group, differing
only in which days enter the denominator.** This module's central methodological warning could not
have a cleaner illustration — and here both figures appear in the same paper.

A second, smaller denominator inconsistency: the Results state that 31.6% (118) needed no
intervention and 35.7% (133) needed one — 67.3% needing "minimal to no" support — while the
Discussion says "the majority of participants (77.3%) were only contacted once or twice." The 77.3%
is (133+64)/255, i.e. **of those contacted**, not of the cohort. Both are correct; the denominators
differ.

**Troubleshooting outcomes:**

| Contacts required | n | % of 373 |
|---|---|---|
| None | 118 | 31.6% |
| One | 133 | 35.7% |
| Two | 64 | 17.2% |
| Three or more | 58 | 15.5% |

**Mean 1.3 contacts/participant (SD 1.2); 468 interventions over ~1 year (~9/week), run by two RAs.**

Of the **255 contacted at least once**, **179 (70.2% of contacted; 48.0% of the cohort) recovered and
sustained quality above 0.50.** The single most common resolvable cause was **Low Power Mode
inadvertently enabled**. **40 participants (10.7%) stayed below 0.50 despite intervention**,
attributed to outdated handsets or restrictive OS versions, and **36 (9.7%) never produced any
passive data at all** — device incompatibility, or non-response to repeated contact. The authors are
explicit that this residue is **intrinsic to BYOD** and that a framework "may help identify but
cannot fully address" it.

**The consequence-of-missingness analysis** (a single participant's high-quality day, downsampled):

- 5–10 s sampling: home-time error near zero.
- Beyond 10 min: error and variance rise sharply.
- **30–60 min intervals (≈0.50 quality or lower): home time consistently underestimated by two to
  four hours**, with fragmented trajectories and unreliable home-location identification.
- Empirically (no downsampling), correlations between home time and entropy / screen duration / step
  count were stable above ~50–55% quality and attenuated, with widening CIs, below it.

The authors caution that this downsampling is *regular* missingness; real sub-0.50 data has
irregular gaps and is likely worse.

## Feasibility Findings

The authors' own claim is deliberately modest: LINC is **feasible to run** (1.3 contacts/participant,
~9 interventions/week, two RAs) and the cohort achieved quality above published mindLAMP benchmarks —
but **"causal attribution to LINC components requires controlled comparison against standard
practices,"** and study duration, population, recruitment and platform improvements over time are all
uncontrolled alternative explanations.

They state that LINC is intended to **complement, not replace, imputation** — reducing extreme and
systematic missingness before modelling rather than repairing it afterwards.

## Relevance to Future Study Design

1. **Adopt the 10-minute-bin definition, or state yours as explicitly.** It is computable from any
   GPS stream, needs no duty-cycle knowledge, and is directly comparable to the seven mindLAMP
   studies tabulated here.
2. **Treat 0.50 as a hard analytic floor, not a soft target.** Below it, home time is wrong by hours
   and multi-feature correlations become unstable. This is the module's first quantitative,
   feature-level justification for a completeness threshold.
3. **Budget the monitoring, because it is affordable.** ~9 interventions/week and 1.3 contacts per
   participant for a 373-person study, run by two RAs, is a real but small line item. This is the
   first study in the module to quantify the *staffing* cost of data-quality management rather than
   just recommending it.
4. **Expect ~10% of a BYOD cohort to yield nothing, and ~11% more to resist intervention.** Roughly
   one in five participants is not fixable by outreach. Size the cohort accordingly rather than
   treating this as a failure of the protocol.
5. **Check Low Power Mode first.** It was the most common single remediable cause across 255
   contacted participants.
6. **Note which wake mechanism your platform uses.** LINC's engagement requirement *is* the keepalive.
   On a platform with a server-side heartbeat the daily-EMA justification weakens — and on a platform
   with neither, plan for one.
7. **Publish both denominators.** This paper and its companion give 0.92 and 0.78 for the same cohort.
   Reporting only the flattering one is the field's default and this pair shows the size of the gap.

## Evidence Confidence

**Verified** — the 417→373 flow with its 19 fraud/address disqualifications and 25 withdrawals; all
demographics including 90.3% iOS; the 0.92/0.59/0.98 quality distribution with every percentile count;
the 14.2%-below-0.10 and 9.7%-zero figures; the 0.95 EMA median with its distribution; the
intervention counts (118/133/64/58, mean 1.3, 468 total, ~9/week, two RAs); the 179/255 recovery and
40/36 non-recovery counts; the three flag thresholds; the Spearman r=0.94 active–passive correlation;
Table 1's six comparator mindLAMP studies (n=86/695/96/76/70/37; medians 0.12/0.43/0.80/0.58/0.77/0.71);
the downsampling result and the 0.50–0.55 stability threshold; the companion-analysis medians of 0.78
and 0.76. All read from the full text and PDF (PMC13022485), 2026-09-02.

**Reported, and flagged as such by the authors** — that LINC caused the observed quality. There is no
control arm. Duration (2–3 weeks vs up to 52 in the comparators), a non-clinical young sample, and
platform improvements over the 2019–2025 span of Table 1 are all uncontrolled. **The comparison in
Table 1 is between studies with different populations, durations and even metrics** — Study 6's 0.71
is footnoted as "mean percent of day with GPS data," a *different metric* from the median-proportion
figure used elsewhere in the same table. Read Table 1 as orientation, not as a ranking.

**Unclear / not reported** — the pre-consent funnel; withdrawal reasons; **any OS-stratified
completeness**, despite a 90.3%/9.7% iOS/Android split that the Limitations section explicitly names
as a possible driver of the headline result. Given the module's unresolved iOS/Android question
(Tier 15 Q111), the absence of this breakdown is the paper's most frustrating omission.

**COI.** Torous is the platform's principal academic developer, and the framework's demonstration
cohort is his own group's study, benchmarked against six of his own group's prior studies. Two things
temper it: the framework's resources are published in full for independent reuse, and the paper
reports its unflattering residue plainly (9.7% zero data, 10.7% unfixable, 14.2% below 0.10). The
claim most exposed is the implicit one that LINC explains the gap to 0.12–0.80 — which the authors
themselves decline to make.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.1038/s41598-026-41435-0
- Europe PMC: https://europepmc.org/article/PMC/PMC13022485
- mindLAMP docs: https://docs.lamp.digital/
- Cortex (feature extraction): https://github.com/BIDMCDigitalPsychiatry/LAMP-cortex
- Local PDF: `../literature/2026-calvert-scientificreports-linc-framework-passive-data-quality.pdf`

## Related profiles

- Platform: [mindLAMP](../../module-02-digital-phenotyping/profiles/mindlamp.md)
- Other mindLAMP deployments: [`mindlamp-relapse-3site.md`](mindlamp-relapse-3site.md),
  [`lamp-schizophrenia-cognition-unpaid.md`](lamp-schizophrenia-cognition-unpaid.md),
  [`mindlamp-global-cognitive-multisite.md`](mindlamp-global-cognitive-multisite.md)
- The opposite solution to the same OS constraint (server-side heartbeat):
  [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
- Coverage-ratio-not-volume, and an independently derived heartbeat:
  [`carp-mpath-sense-performance-study.md`](carp-mpath-sense-performance-study.md)
- Fraudulent remote participants: [`metricwire-fraudulent-participation.md`](metricwire-fraudulent-participation.md)
- Two defensible rates for one cohort: [`avicenna-ema-suicidal-ideation-iatrogenic.md`](avicenna-ema-suicidal-ideation-iatrogenic.md)
- Completeness as a separate question from wear: [`empatica-epilepsy-data-quality.md`](empatica-epilepsy-data-quality.md)

## Sources

1. Calvert E, Lane E, Flathers M, Torous J. *Sci Rep* 2026;16:10160. DOI 10.1038/s41598-026-41435-0.
   Full text and Table 1 read from the published PDF and PMC XML (PMC13022485), 2026-09-02.
   Establishes every figure in this profile.
