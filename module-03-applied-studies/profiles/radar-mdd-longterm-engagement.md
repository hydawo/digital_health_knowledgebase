# Zhang et al. 2023 — RADAR-MDD long-term retention and engagement patterns, N=614, up to 94 weeks

## Quick Facts

| Field | Details |
|---|---|
| Citation | Zhang Y, Pratap A, Folarin AA, Sun S, Cummins N, Matcham F, et al., RADAR-CNS consortium. "Long-term participant retention and engagement patterns in an app and wearable-based multinational remote digital depression study." *npj Digital Medicine* 2023;6:25. DOI [10.1038/s41746-023-00749-3](https://doi.org/10.1038/s41746-023-00749-3). PMID 36806317 / PMC9938183. |
| Study design | Secondary analysis of the RADAR-MDD observational cohort — survival analysis (Cox PH) plus unsupervised K-means clustering of per-participant daily data-availability vectors |
| Sample size (enrolled / analyzed) | **614 analyzed** (of the 623 enrolled in RADAR-MDD); primary cohort observed to a common 43 weeks, secondary cohort of **313** observed to 94 weeks |
| Population | Adults with current/prior recurrent MDD. Median age 49 (range 18–80); **75.7% female (N=465)**; predominantly White at the two sites collecting ethnicity. Sites: KCL London (350), CIBER Barcelona (146), VUMC Amsterdam (118). |
| Duration | Nov 2017 – Apr 2021; 43-week and 94-week observation windows |
| Devices/platforms used | [RADAR-base](../../module-02-digital-phenotyping/profiles/radar-base.md) active + passive apps; **Fitbit Charge 2/3** ([Fitbit/Google](../../module-01-wearables/profiles/fitbit-google.md)); Android only |
| Funding/COI | IMI2 grant 115902 (EU Horizon 2020 + EFPIA). Industry co-authors from **H. Lundbeck A/S** (Annas) and **Janssen** (Vairavan, Narayan). |
| Last verified | 2026-08-31 |

## Summary

The analytic companion to [Matcham et al. 2022](radar-mdd-recruitment-retention.md) on the same
cohort. Where Matcham reports *what* the retention and availability numbers were, this paper asks
*who* disengages, *when*, and *from which data stream* — and it is the most directly actionable
paper in this module for anyone designing a long remote study.

Three findings do real work for study design. First, **retention is stream-specific, and the
ordering is stable**: the wearable outlasts the phone, and passive phone sensing is the *worst*
performer, not the best. Second, **participants who stop doing surveys frequently keep wearing the
wearable** — 44.6% of the least-engaged survey group kept supplying Fitbit data for an average of 42
weeks — so "disengaged" is not a single state and should not be modelled as one. Third,
**disengagement is predictable early and non-randomly distributed**: younger participants, more
severely depressed participants, non-White participants, and participants slower to answer survey
notifications all disengage more, which means naive analysis of the resulting data is biased toward
older, less symptomatic, White participants.

## Instrumentation and Deployment Model

Same stack as the parent study: RADAR-base passive app, RADAR-base active app (PHQ-8 and RSES every
2 weeks), and a researcher-provided Fitbit Charge 2 or 3. Android only.

Three data streams are analysed separately throughout, and the distinction is the paper's main
methodological contribution:

- **Phone-Active** — completion of the bi-weekly surveys.
- **Phone-Passive** — smartphone sensor data (GPS every 10 min, Bluetooth hourly, battery every
  10 min, phone usage event-triggered).
- **Fitbit-Passive** — wearable data.

**Deployment model detail that turns out to matter:** **151 participants (25.1%) were iPhone users
who were given an Android smartphone to use as their primary phone** for the study duration. That
subgroup is directly compared against participants using their own phones, giving a rare natural
experiment on provisioned-vs-BYOD handsets.

## Recruitment and Retention

**Retention at the common 43-week horizon (primary cohort, N=614):**

| Data stream | Retained at 43 weeks | Retained at 94 weeks (secondary cohort, N=313) |
|---|---|---|
| **Fitbit-Passive** | **67.6% (N=415)** | **54.0% (N=169)** |
| Phone-Active (surveys) | 54.6% (N=335) | 48.2% (N=151) |
| **Phone-Passive (phone sensors)** | **47.7% (N=293)** | **39.3% (N=123)** |

The ordering — wearable > surveys > phone passive sensing — holds at both horizons. The authors note
this retention is significantly higher than in prior remote digital studies, and attribute that to
deliberate engagement strategies rather than to anything intrinsic (see Feasibility Findings).

**Multivariate Cox proportional-hazards predictors of dropping out** (HR > 1 = higher risk of
ceasing to contribute):

- **Age — the strongest and most consistent predictor.** Relative to the youngest group (18–30),
  the oldest group (>60) had the lowest risk across all three streams: Phone-Active HR=0.56
  (p=0.02), Phone-Passive HR=0.56 (p=0.02), **Fitbit-Passive HR=0.42 (p=0.01)**. Older participants
  stayed longer. This held in the 94-week cohort too.
- **Study-provided phone — significantly worse than BYOD.** Participants using the study-provided
  Android phone had a *higher* risk of ceasing to contribute both active (HR=1.67, p=0.03) and
  passive (HR=1.65, p=0.03) phone data than participants using their own phones. The authors'
  proposed explanation: participants likely did not actually use the provided phone as their primary
  device in daily life.
- **Smartphone brand mattered.** Motorola (HR=0.26, p<0.001) and Samsung (HR=0.57–0.58, p<0.001)
  users contributed both active and passive phone data significantly longer than other brands. The
  authors attribute this to differing vendor policies on how long an app may collect granular
  passive data in the background — an OEM-level effect on data collection that is invisible in most
  study protocols.
- **Site mattered for the wearable.** Versus CIBER Barcelona, KCL (HR=0.59, p=0.03) and VUMC
  (HR=0.40, p<0.001) participants were less likely to stop sharing Fitbit data.

## Data Completeness and Technical Issues

K-means clustering of daily data-availability vectors produced three engagement subgroups per
stream (C1 most, C2 medium, C3 least engaged):

| Stream | Most engaged (C1) | Least engaged (C3) |
|---|---|---|
| Phone-Active | 37.6% (N=231), median **20** bi-weekly surveys (IQR 18–21) | 33.2% (N=204), median **4** surveys (IQR 1–6) |
| Phone-Passive | 42.2% (N=259), median **283** days (IQR 257–298) | 33.7% (N=207), median **32** days (IQR 4–67.5) |
| Fitbit-Passive | **66.3% (N=407)**, median **294** days (IQR 274–301) | **17.6% (N=108)**, median **18** days (IQR 0–67) |

**The cross-stream migration finding — the most useful single result in this paper.** Participants
who largely stopped doing surveys did *not* generally leave the study; they kept wearing the Fitbit.
**65.4% (N=151) of the C2 survey cluster and 44.6% (N=91) of the C3 survey cluster moved into the
most-engaged Fitbit cluster**, contributing passive wearable data for an average of 42 weeks.

**Who ends up in the least-engaged cluster** (all comparisons C3 vs C1):

- **Higher baseline depression severity.** C3 participants had roughly **4 more PHQ-8 points** at
  baseline (Phone-Active C3 median 13.0 [7–17] vs C1 9.0 [6–15], p=0.003), with the same pattern for
  both passive streams (p<0.001). The authors state the least-engaged group was up to **16× less
  likely** to share active or passive data.
- **Younger.** Phone-Active C1 median age 53.0 vs C3 48.0 (p=0.003); Phone-Passive C1 52.0, C3 46.0
  (p=0.01) — roughly a 5-year gap.
- **Less likely to be White.** Proportion White in C3 (77.8%) was significantly lower than C1
  (95.1%) and C2 (84.0%) for Phone-Active (p<0.001), with the same direction for both passive
  streams. **This is an equity finding, not a footnote:** the data that survives to analysis is
  disproportionately from White participants.
- **Slower to respond to notifications.** C1 median survey response time **73.7 min** (IQR 31.3–215.8)
  vs C3 **302.4 min** (IQR 122.3–527.1), p<0.001 — a ~3.8 h difference. C3 also took *longer to
  complete* each survey (61.6 s vs 50.3 s, p<0.001). Both are available in the first weeks of a study
  and are proposed as early-warning markers.

**Why phone passive sensing performed worst.** The authors attribute it to battery and mobile-data
consumption from high-resolution passive collection, leading participants to disable collection or
uninstall the app — plus brand-level background-execution limits. This inverts the common assumption
that passive collection is the low-burden option: it is low-*effort* but not low-*cost* to the
participant's device.

**Technical caveats acknowledged:** survey versions changed mid-study, technical bugs (including
missing notifications) were fixed during collection, surveys were added over time, and the three
sites started at different times. Differences between Fitbit Charge 2 and Charge 3 were **not
tracked**, so device-generation effects cannot be separated. Contact-log effects are explicitly
bidirectional — the most engaged cluster was contacted *least* (3.0 vs 5.0 contacts, p<0.001),
which reflects those participants needing less help, not support being counterproductive.

## Feasibility Findings

The authors credit four concrete engagement strategies for retention above prior comparable studies,
and these should be read as the cost of the numbers above:

1. **"Human-in-the-loop"** — the research team proactively contacted participants about Fitbit
   malfunctions, app problems, 3-month assessment reminders, and to congratulate them on the 1-year
   milestone.
2. **Monetary incentives, cyclically timed.** Participants were **not** paid for completing remote
   surveys or sharing passive data, but were compensated for enrolment, for 3-monthly clinical
   assessments, and for additional interviews — a cadence the authors argue indirectly incentivised
   staying enrolled. Participants also kept the Fitbit.
3. **Participant-centric design** — a patient advisory board of service users shaped the protocol and
   app design from the outset.
4. **Recruiting a cohort with the condition of interest** — clinically enriched cohorts are known to
   retain better than healthy volunteers.

Even so, **17.6–33.7% of the cohort across streams did not remain engaged long-term.**

Explicit design recommendations from the authors: use early markers (younger age, higher baseline
symptom severity, delayed survey responses) to triage a high-dropout-risk subgroup for tailored
contact; consider **over-recruiting participants matching the low-engager profile** to counteract
data imbalance; and deploy near-real-time monitoring of incoming data for socio-technical bias so
that falling compliance is caught while intervention is still possible.

## Relevance to Future Study Design

1. **Model retention per stream, not per participant.** A single "retention rate" for a multimodal
   study is close to meaningless — the same cohort returned 67.6%, 54.6%, and 47.7% depending on
   which stream you ask about.
2. **Provisioning phones made things worse, not better.** The intuition that giving participants a
   study phone removes friction is contradicted here (HR≈1.66 for ceasing to contribute). If a
   platform's OS restriction forces provisioning, treat that as a retention cost — and note this
   compounds the Android-switching withdrawals found in the parent paper.
3. **Budget passive phone sensing as the most fragile stream.** Battery/data cost and OEM background
   limits make it the first thing to go. Sampling rates are a retention variable, not just a
   resolution variable.
4. **A wearable is the durable channel for participants who stop engaging actively.** If the design
   needs *any* signal from low-engagement participants over a long horizon, the wearable is where it
   will come from.
5. **Expect a demographically skewed surviving sample and plan for it analytically.** Age, symptom
   severity, and ethnicity all structure who is still contributing at 43 weeks.
6. **Instrument survey response latency from day one** — it is free, passive, and predicts long-term
   engagement.

## Evidence Confidence

**Verified** for all retention rates, hazard ratios, cluster statistics, and demographic
associations — primary reported results of the paper, read from the full text.

**Corroborated** for the causal attribution of high retention to the four engagement strategies: the
strategies were genuinely deployed and the retention is genuinely higher than comparators, but this
is a single-cohort observational study with **no randomisation of engagement strategy**, so the
attribution is the authors' reasoning rather than a tested effect. The authors say as much and call
for randomised designs.

Limits the authors state: open enrolment with no stratification or randomisation of recruitment;
under-representation of participants over 70; predominantly White and female; PHQ-8 is a screening
rather than diagnostic instrument; cross-country differences in education, language, income and
currency limit between-site comparison; Fitbit Charge 2 vs 3 differences untracked; **Android only,
so nothing here generalises to iOS**; and compensation for clinical assessments limits
generalisability to wholly uncompensated cohorts.

Note this is a **secondary analysis of the same 623-participant cohort** as
[Matcham et al. 2022](radar-mdd-recruitment-retention.md) — the two papers are not independent
evidence, and their retention figures differ legitimately because they measure different things
(outcome-assessment completion vs. per-stream data contribution survival).

## Key Links

- Paper (OA): https://doi.org/10.1038/s41746-023-00749-3
- Europe PMC: https://europepmc.org/article/MED/36806317
- RADAR-CNS consortium: https://www.radar-cns.org
- Local PDF: `../literature/2023-zhang-npjdigitalmedicine-radar-mdd-longterm-retention-engagement.pdf`

## Related profiles

- Platform: [RADAR-base](../../module-02-digital-phenotyping/profiles/radar-base.md)
- Device: [Fitbit / Google](../../module-01-wearables/profiles/fitbit-google.md)
- Same cohort: [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md)
- Same platform, different disease area: [`radar-ad-feasibility-usability.md`](radar-ad-feasibility-usability.md)

## Sources

1. Zhang Y, et al. *npj Digital Medicine* 2023;6:25. DOI 10.1038/s41746-023-00749-3. Full text
   retrieved from Europe PMC (PMC9938183), 2026-08-31. Establishes every figure in this profile.
