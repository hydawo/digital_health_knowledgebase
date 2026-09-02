# Raugh et al. 2021 — Digital phenotyping adherence, feasibility and tolerability in outpatients with schizophrenia, N=109

## Quick Facts

| Field | Details |
|---|---|
| Citation | Raugh IM, James SH, Gonzalez CM, Chapman HC, Cohen AS, Kirkpatrick B, Strauss GP. "Digital phenotyping adherence, feasibility, and tolerability in outpatients with schizophrenia." *Journal of Psychiatric Research* 2021;138:436–443. DOI [10.1016/j.jpsychires.2021.04.022](https://doi.org/10.1016/j.jpsychires.2021.04.022). PMID 33964681 / PMC8192468 (author manuscript). |
| Study design | Case-control observational study explicitly designed around three aims: **adherence, feasibility, and tolerability**. Mixed-model ANOVAs, multivariate regression, and structured debriefing interviews. |
| Sample size (enrolled / analyzed) | **109** — 54 outpatients with schizophrenia (SZ), 55 demographically matched healthy controls (CN). Groups matched on age, sex, parental education and race; **CN had higher personal education**. |
| Population | Community-recruited adults; SZ additionally recruited from outpatient mental health centres. SCID-5 diagnosis. Exclusions: lifetime neurological disorder, substance abuse within 6 months; CN also screened out for psychotic/bipolar history and family history of psychosis. |
| Duration | **6 days** — much shorter than any other study in this module |
| Devices/platforms used | **Study-provided smartphones** running Ilumivu's **mEMA** app + Empatica's **Alert** app, plus an **[Empatica](../../module-01-wearables/profiles/empatica.md) smartband**. Not a Module 2 platform in the Beiwe/RADAR sense — see Evidence Confidence. |
| Funding/COI | Academic (University of Georgia, Louisiana State, University of Nevada Reno). **Participants were compensated for survey completion.** |
| Last verified | 2026-08-31 |

## Summary

The only study in this module that measures **tolerability as a formal outcome** rather than
inferring it from dropout — and the one that most cleanly separates *adherence by data stream type*
within a single protocol. Its central contribution is a strict ordering of passive stream
reliability that maps onto **computational and hardware demand**, not onto participant willingness:

**Accelerometry (86.7%/90.3%) > Geolocation (72.7%/77.5%) > Ambient audio (39.7%/49.9%) > Smartband
(20.0%/28.0%)** for SZ/CN respectively.

The smartband figure is the striking one. **A wrist-worn ambulatory psychophysiology device returned
about a fifth of its expected data over six days** — and the authors attribute this specifically to
Bluetooth connectivity and troubleshooting difficulties, noting their own prior work with the same
device achieved 88.5%. That is a nearly fourfold swing attributable to integration problems rather
than participants.

The reassuring finding: **passive adherence did not differ significantly between SZ and CN**, and
**both groups rated the experience as highly tolerable** (positive ratings ~8.6–8.8 out of 10,
negative ~1.0–1.3). Schizophrenia was a barrier to *active* survey completion, not to being
monitored.

## Instrumentation and Deployment Model

**Fully provisioned** — smartphones and smartbands were supplied, not BYOD. The authors name this as
a limitation but defend it as ensuring consistent technology for a controlled first evaluation.

Onboarding included being shown how to use the apps and **completing a practice survey with a
research assistant** to confirm response formats were understood.

**Active streams** (mEMA): momentary/signal-contingent, morning, event-contingent, and evening
surveys. Designed to take **under five minutes**, using **skip logic** to reduce burden. Two quality
mechanisms are worth copying:

- **Infrequency items** from the Chapman Anhedonia Scales — one randomly selected item placed about
  three-quarters through each momentary survey, to detect inattentive responding.
- **Per-screen response time** recorded in seconds.

**Evening surveys asked why surveys had been skipped that day**, from a fixed list: driving, bathing,
exercising, meeting or class, busy, misplaced the phone, technical issues, phone battery died,
annoyed with the prompts, didn't notice the alarm, didn't want to, other. This is the most direct
missingness-attribution instrument in the module.

**Passive streams and their configurations:**

| Stream | Source | Configuration |
|---|---|---|
| Accelerometry (ACL) | Phone | One sample per change in XYZ motion; magnitude = root sum of squares |
| Geolocation (GPS) | Phone | Every 10 min **or** on movement >10 m; also on survey completion; **samples retained only if accurate to <35 m** |
| Ambient sound (VOX) | Phone | 5 seconds every 10 min at 16 kHz |
| Accelerometry, EDA, skin temperature | Empatica smartband | 32 Hz accelerometry; **skin conductance and temperature at 4 Hz**; physiologically implausible values deleted (EDA <0.1 or >39.95 µS; temp <20 or >40 °C); epoched to 1-minute periods |

**Smartband operational constraints, stated explicitly:** ~30-hour battery, so participants were
instructed to **charge it every other night**; data relayed to the phone over **Bluetooth**, with
only **14 hours of on-band storage** as buffer; wear instructed at all times except submersion.

## Recruitment and Retention

Six days is too short for meaningful attrition analysis, and the paper does not frame retention as
an outcome. Its equivalent question is adherence, below.

## Data Completeness and Technical Issues

**Adherence by stream — the core table** (mean %, SD; k = number of samples):

| Stream | SZ | CN | Effects |
|---|---|---|---|
| **Active (overall)** | **63.8%** (34.1) | **75.3%** (28.7) | Group F=6.11*, Data Type F=15.66***, interaction ns; **Cohen's d = 0.53** |
| — Morning | 75.3% (28.4) | **85.5%** (25.7) | Highest of all survey types |
| — Event | 64.8% (39.2) | 78.8% (31.0) | |
| — Evening | 59.3% (36.9) | 70.0% (30.7) | |
| — Momentary | **55.7%** (28.2) | 66.7% (23.8) | Lowest |
| **Passive (overall)** | — | — | Group ns, **Data Type F=118.96***, interaction ns; d=0.24 |
| — **Accelerometry** | **86.7%** (31.5) | **90.3%** (25.8) | Best |
| — Geolocation | 72.7% (40.0) | 77.5% (39.1) | |
| — Ambient audio | 39.7% (33.0) | 49.9% (29.5) | |
| — **Smartband** | **20.0%** (30.1) | **28.0%** (32.3) | **Worst** |

Every passive stream differed significantly from every other (ACL > GPS > VOX > Band).

**Two headline contrasts:**

1. **Active adherence: SZ significantly lower than CN**, medium effect (d=0.53), consistent across
   all four survey types (no interaction).
2. **Passive adherence: no significant group main effect in the primary ANOVA.** (Follow-up
   longitudinal models did find a Group effect favouring CN — see below — so the honest reading is
   "no difference in the headline analysis, small difference in the longitudinal models.")

**Decay over six days:** active adherence **decreased after day 1, significantly on days 4 and 5**.
Passive adherence also declined significantly over study days. Adherence was higher on weekdays than
weekends; in CN, Saturday was significantly lower than every weekday, while **in SZ no day-of-week
differences were significant** — the controls' routine mattered, the patients' did not.

**Why each passive stream failed — the authors' mechanistic account, which is the most transferable
part of this paper:**

- **Smartband (20%/28%)** — difficulty using the band, forgetting to charge it, and **Bluetooth
  connectivity and troubleshooting difficulties**. Explicitly contrasted with the same team's prior
  **88.5%** with the same device class.
- **Ambient audio (40%/50%)** — phone placement (microphone covered) and computational demand.
- **Geolocation (73%/78%)** — computationally demanding, dependent on satellite communication.
- **Accelerometry (87%/90%)** — least computationally demanding. But note a measurement subtlety the
  authors raise: phone accelerometry was movement-triggered, so missing samples may represent a
  phone left on a surface, a genuinely stationary participant, or both — **missingness and the
  signal are confounded**.

**Generalisable principle they state:** *"Passive data types that are less computationally demanding
(i.e., accelerometry) may be more consistently recorded than those that require more device
processing power (i.e., geolocation)."*

**Predictors of adherence:**

- **SZ, active:** only **social/vocational functioning (LOF)** predicted adherence (event surveys,
  β=0.5, p<0.05). **Age, education, cognition, number of children, employment, mean survey time,
  positive symptoms and negative symptoms were all non-significant** — a substantial set of null
  results against plausible hypotheses.
- **CN, active:** greater age predicted lower event-survey adherence (β=−0.34); longer mean survey
  time predicted lower event (β=−0.35) and evening (β=−0.32) adherence.
- **SZ, passive:** greater **positive symptoms predicted less accelerometry data**; **higher
  education predicted better smartband adherence**; higher negative symptoms and greater functioning
  were associated with **reduced ambient audio**.
- **CN, passive:** nothing predicted adherence.

The positive-symptoms/accelerometry association is interpreted carefully by the authors: it could
reflect **not carrying the phone due to concerns about being monitored**, or a genuine reduction in
movement. They state the study cannot distinguish these — an important, honest caveat for anyone
treating passive activity data as a symptom measure in psychosis.

## Feasibility Findings

Feasibility was supported on four measures:

- **Survey completion time: 2.5 min (SZ) vs 2.17 min (CN)** — about a minute faster than a 2008
  comparator. SZ were slower and *less* variable, but **completed no fewer items**.
- **Infrequency-item endorsement was low and did not differ by group** (SZ 1.01%, CN 1.12%,
  p=0.237) — but was predicted by **number of items** (β=0.37, p=0.002) and **total survey time**
  (β=0.38, p=0.001). Longer surveys produce worse-quality responses, measurably.
- **Obstacles were endorsed at similar rates in both groups**; the most frequent were **difficulties
  with the smartband** and being "busy."
- **Adherence cut-offs:** a **50% cut-off would exclude disproportionately more SZ than CN
  participants**; effects were comparable at lower thresholds. The authors recommend **25% as best
  practice for both active and passive**, checking that it does not disproportionately exclude
  either group, and suggest **daily-adherence rather than total-study-adherence cut-offs** to retain
  more active data. They stress cut-offs must be clearly reported.

**Tolerability (Aim 3) — measured, not inferred.** Structured debriefing interviews found **no group
difference** on positive (F=0.82, p=0.37) or negative (F=1.07, p=0.306) ratings. **Positive: SZ
8.81 (SD 0.91), CN 8.56 (SD 1.16). Negative: SZ 0.96 (SD 1.27), CN 1.29 (SD 1.19).** The authors
emphasise this extends known tolerability of active methods to **passive methods and ambulatory
psychophysiology**.

## Relevance to Future Study Design

1. **Rank passive streams by computational and hardware demand when planning yield.** Accelerometry
   is robust; anything requiring a radio link, satellite fix, or continuous processing is not. The
   ACL > GPS > VOX > Band ordering is the practical takeaway.
2. **A Bluetooth-tethered wearable is the single most fragile component** in a smartphone-plus-band
   design — 20–28% here versus 88.5% in the same team's earlier work. Pilot the *pairing*, not just
   the sensor.
3. **Schizophrenia impairs active but not passive participation.** Design around this: for this
   population, weight passive collection and keep surveys to morning slots.
4. **Morning surveys outperform momentary ones** in both groups (75–85% vs 56–67%). Scheduling is a
   lever.
5. **Use 25% adherence cut-offs, not 50%** — and check the cut-off does not disproportionately
   exclude the clinical group. This is a concrete, checkable equity test that most papers skip.
6. **Keep surveys short for validity, not just adherence** — item count and total time both
   predicted careless responding.
7. **Ask participants why they skipped**, via an evening survey with a fixed reason list. Cheap, and
   it converts missingness from unexplained to attributable.
8. **Beware confounding missingness with signal** in movement-triggered accelerometry, especially
   where symptoms plausibly affect both.

## Evidence Confidence

**Verified** for all adherence rates, statistical tests, tolerability ratings, timing metrics and
predictor models — primary reported results read from the full text (NCBI PMC author manuscript).

**Scope caveat — read this before comparing to other profiles.** **Only six days.** Every other
study here runs weeks to years. Adherence over six days should not be compared directly against
6-month or 18-month figures; the decay this study detects between day 1 and days 4–5 is the *start*
of curves that other profiles follow to completion.

**Platform caveat.** This uses **Ilumivu mEMA and Empatica's Alert app on provisioned phones**, not
one of Module 2's profiled research platforms. It is included because its stream-by-stream adherence
decomposition and its formal tolerability measurement are not replicated anywhere in the
platform-specific literature — but its *absolute* numbers are properties of this software stack, not
of Beiwe, RADAR-base, or mindLAMP. mEMA is not currently profiled in Module 2; flagged as a possible
expansion candidate in `../_inventory-and-scope-decisions.md`.

**Limitations the authors state:**

- Context variables (location, activity, social interaction) were collected **only when surveys were
  completed**, so context effects on adherence cannot be studied — partly mitigated by the evening
  skip-reason survey.
- **Devices were provided**, so results may not generalise to BYOD designs. Given
  [Zhang et al.'s](radar-mdd-longterm-engagement.md) finding that *provisioned* phones retained
  worse, the direction of this bias is genuinely unclear.
- **Participants were compensated for survey completion**, which meta-analysis associates with
  greater adherence.
- Adherence estimates may be specific to this study's design.

**One additional caution this profile adds:** the paper reports "no significant Group effect" for
passive adherence in the primary ANOVA, but the follow-up longitudinal models found significant
Group main effects favouring CN on instance (p=0.037), study day (p=0.018) and weekday (p=0.013),
and the discussion states "passive adherence is generally lower in SZ than CN." Treat the
no-difference claim as **Corroborated with qualification**, not settled: the headline analysis and
the longitudinal models point slightly different ways, and the true difference is small.

## Key Links

- Paper: https://doi.org/10.1016/j.jpsychires.2021.04.022
- Europe PMC (author manuscript): https://europepmc.org/article/MED/33964681
- **PDF not obtained** — *Journal of Psychiatric Research* is paywalled and the PMC author-manuscript
  PDF route returned HTML. Full text was read via the NCBI PMC XML deposit. Logged as Tier 14 Q110
  in `../../shared/unresolved-questions.md`.

## Related profiles

- Device: [Empatica](../../module-01-wearables/profiles/empatica.md)
- Same population, different platform, longer horizon:
  [`mindlamp-relapse-3site.md`](mindlamp-relapse-3site.md),
  [`sleepsight-schizophrenia-rest-activity.md`](sleepsight-schizophrenia-rest-activity.md)
- Passive-outlasts-active on research platforms:
  [`beiwe-adolescent-feasibility.md`](beiwe-adolescent-feasibility.md),
  [`beiwe-als-adherence.md`](beiwe-als-adherence.md)

## Sources

1. Raugh IM, et al. *J Psychiatr Res* 2021;138:436–443. DOI 10.1016/j.jpsychires.2021.04.022. Full
   text and tables read from the NCBI PMC author-manuscript XML deposit (PMC8192468), 2026-08-31.
   Establishes every figure in this profile.
