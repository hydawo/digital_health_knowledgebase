# McInerney et al. 2024 — Beiwe feasibility, tolerability and user experience in type 2 diabetes, N=85 over 2 months

## Quick Facts

| Field | Details |
|---|---|
| Citation | McInerney AM, Schmitz N, Matthews M, Deschênes SS. "'Anything that would help is a positive development': feasibility, tolerability, and user experience of smartphone-based digital phenotyping for people with and without type 2 diabetes." *BMC Digital Health* 2024;2:55. DOI [10.1186/s44247-024-00116-6](https://doi.org/10.1186/s44247-024-00116-6). PMID 39282098 / PMC11390910. Published 2024-09-12. |
| Study design | Feasibility, tolerability and user-experience analysis nested in **The Smartphone, Behaviour, and Mood study**, an observational digital-phenotyping study. Mixed methods: quantitative missingness plus a structured feedback questionnaire with free-text responses. |
| Sample size (enrolled / analyzed) | **85 downloaded the app → 82 completed baseline → 69 completed 2-month follow-up (81.2%) → 68 completed the feedback questionnaire.** |
| Population | Adults 18–70 in the **Republic of Ireland**, with and without **type 2 diabetes**. Recruited via Diabetes Ireland (a national charity), social media, local radio and newspapers. Of the 68 feedback completers: 35 with T2D, 33 without; the T2D group was older, more male, more often married, and more often retired or disabled. |
| Duration | Data collection **February–August 2021**. Per participant: baseline + 1-month + 2-month questionnaires, with twice-daily EMA over **57 days**. |
| Devices/platforms used | **[Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)**, BYOD. Passive: GPS, accelerometer, and **call/text counts on Android only**. Active: 08:00 morning survey (sleep duration, sleep quality) and 19:00 evening survey (mood, social interactions and their positivity, exercise), each with a **3-hour response window**. |
| Funding/COI | Ad Astra Fellows PhD Studentship (AMM); UCD seed funding; CIHR PCG-155452. **Competing interests: none declared.** No platform-developer authorship. Ethics: UCD Human Research Ethics Committee. |
| Last verified | 2026-09-02 |

## Summary

The most decision-relevant thing in this paper is a table the authors do not foreground:

> **On Beiwe, iPhone users were missing 70% of morning and 70.6% of evening EMA responses. Android
> users were missing 21.3% and 26.8%. Both differences p < 0.001.**

That is a **~49-point iOS penalty on active data**, in a cohort of 69 completers with a 62% Android
/ 38% iOS split that was stable between completers and dropouts. And in the **same** cohort, on the
**same** platform, **passive** accelerometer and GPS missingness showed **no significant association
with phone type at all**.

This bears directly on the module's open contradiction (Tier 15 Q111). Three Beiwe studies were
recorded as favouring iOS; [Niemeijer 2023](carp-mpath-sense-performance-study.md) on CARP and
[McClaine 2024](aware-chemotherapy-engagement.md) on AWARE pointed the other way. This study is
**Beiwe, and it points the other way, and it does so only for the active stream.** The most defensible
reading is now that **OS asymmetry is stream-specific before it is platform-specific**: the direction
of the effect can differ between the active and passive streams *of the same deployment*, so any
study quoting "an OS effect" without saying which stream is under-specified.

The paper's other contribution is a durable finding about acceptability: **tolerability of the data
collection itself was high (76.5%–89.7% "not a problem" across five domains), while confidence in
sharing that data with a clinician split sharply by illness status — 93.9% of people with T2D versus
53.1% without (p < 0.001).**

## Instrumentation and Deployment Model

Straightforward BYOD Beiwe, two short daily surveys with 3-hour windows, plus GPS, accelerometer and
Android-only communication metadata.

**The Android-only call/text limitation is a platform-policy artefact, not a Beiwe defect**, and it
recurs across this module: it removed call/SMS from
[RADAR-MDD](radar-mdd-recruitment-retention.md), was excluded from the Play Store build of
[m-Path Sense](carp-mpath-sense-performance-study.md), and rendered the CrossCheck benchmark
unreproducible per [Cohen et al.](mindlamp-relapse-3site.md). Here it means **51 of 82 participants
had a communication stream and 31 did not**, purely by handset.

**No compensation is described.**

> **Pre-`heartbeat` lower bound.** All data here were collected **February–August 2021**, well before
> Beiwe's server-side **`heartbeat`/keepalive** push was globally enabled on **2024-05-29**. The
> completeness figures in this profile should be treated as **lower bounds** for current Beiwe
> deployments, not as current performance — see [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
> and Tier 14 Q106 in [`../../shared/unresolved-questions.md`](../../shared/unresolved-questions.md).
> The **relative** iOS/Android difference is less obviously affected than the absolute levels, since
> heartbeat targets background wake rather than survey delivery — but it has not been re-measured
> post-heartbeat and should not be assumed stable.

## Recruitment and Retention

**Retention was 81.2%** (69 of 85 who downloaded the app); attrition 18.8%.

**A reporting error to be aware of if you read the paper directly.** The Attrition subsection states
"18.8% of those who downloaded the app completed the 2-month follow-up." That is inverted: the
Abstract ("Attrition was 18.8%"), the Discussion ("low attrition, with 81.2% of participants who
downloaded the app…") and the participant counts (69/85 = 81.2%) all agree that **18.8% is the
attrition rate, not the completion rate.** Use 81.2% retention.

**Discontinuation reasons** were mostly unavailable — "the majority did not provide reasoning but
ceased responding to the research team." Two were named: **one participant found mood reflection
distressing**, and **one found survey notifications bothersome**. The first is a small but real
instance of the assessment-reactivity concern that
[Kivelä 2024](avicenna-ema-suicidal-ideation-iatrogenic.md) and
[Spangenberg 2026](metricwire-post-discharge-ema-reactivity.md) examine directly.

No pre-consent funnel is reported.

## Data Completeness and Technical Issues

**Definitions, as stated.** EMA missingness = percentage of expected survey responses (2 morning + 6
evening items) over **57 days**. Passive missingness = **daily-level**, with a day counted missing if
insufficient usable data was collected in 24 hours to generate a daily summary score (specifically,
daily time spent at home).

**Active data (EMA):**

| | Morning | Evening |
|---|---|---|
| Completers (n=69) | 40.4% missing | 44.0% missing |
| Dropouts (n=13) | 83.4% missing | 85.9% missing |
| **Completers, iPhone** | **70.0% missing** | **70.6% missing** |
| **Completers, Android** | **21.3% missing** | **26.8% missing** |
| | t(66)=8.623, p<0.001 | t(66)=7.965, p<0.001 |

**Passive data:**

| Stream | Completers | Dropouts |
|---|---|---|
| Accelerometer | **9.1% missing** | 49.9% missing |
| GPS | **14.4% missing** | 65.5% missing |
| Call/text (Android only, n=51) | 33.6% (completers, n=42) | 70.8% (dropouts, n=9) |

Overall Android call/text missingness across all 51 Android users: **40.2% of days.**

**Passive out-performed active by a wide margin in completers — 9.1%/14.4% missing versus
40.4%/44.0%** — reproducing the module's most robust cross-platform pattern for the sixth time. And
the pattern within passive streams (**accelerometer more complete than GPS**, 9.1% vs 14.4%) matches
the reliability-tracks-radio-and-compute ordering established by
[Raugh 2021](dp-schizophrenia-tolerability.md) and
[de Angel 2023](radar-base-treatment-engagement.md).

**Dropouts were massively less complete on every stream while still enrolled**, on both active
(83–86% missing) and passive (50–66% missing) data. Early completeness therefore separates eventual
dropouts here as cleanly as it did in [Beukenhorst 2022](beiwe-als-adherence.md), supporting run-in
designs and early targeted outreach.

**No significant association between EMA missingness and T2D status or any sociodemographic
covariate** — consistent with the module's null on baseline disease severity predicting attrition,
and with [Kiang 2021](beiwe-missing-data-sociodemographic.md) for the sociodemographic part.

**Participant-reported technical problems** (from 23 of 68 who answered the free-text prompt; 14 of
those 23 mentioned app issues):

- **Surveys absent after their own notification** — *"Sometimes surveys weren't there despite sending
  a notification"*; *"I would get a notification to do a survey and then when I clicked it, I'd just
  see a black screen until I reset the app and logged back in."*
- The app described as *"a bit temperamental."*
- **Schedule incompatibility, not app failure**: a taxi driver working evenings could not answer the
  19:00 survey before its 3-hour window closed; another participant was *"not near Wi-Fi first thing
  in morning."* These are protocol-design misses, and both would have been fixed by participant-set
  timing — the lever that produced this module's highest mental-health compliance in
  [Clark 2025](metricwire-sgm-youth-ema-feasibility.md).

## Feasibility Findings

**Tolerability was high and uniform.** Across five aspects — daily survey length, baseline/follow-up
questionnaire length, daily survey frequency, type of phone sensor data collected, and perceived
effect on storage/battery — **"not a problem" was selected 76.5%–89.7% of the time.**

Two significant age effects: **older participants were more likely to rate daily survey length as a
"minor problem"**, and **age was associated with perceived storage/battery impact**, with younger
people more likely to call it minor and **older adults more likely to call it serious**.

**The hypothetical-clinical-use question is where the study finds its sharpest split.** Asked whether
they would be comfortable with a healthcare provider accessing smartphone-derived data:

- **People with T2D: 93.9% yes.**
- **People without T2D: 53.1% yes.** χ²(1)=14.012, p<0.001.
- **Employment also mattered:** 88.2% of those uncomfortable were employed or in education, versus
  50% of those comfortable (χ²(1)=7.647, p=0.006).

Free-text reasoning tracks the split. Participants without T2D raised privacy and, notably,
*epistemic* objections — *"I am concerned about … possible use of my data to draw conclusions about
me that might not be correct"*; *"phone data is limited in what it can actually tell you about a
person's lived experiences."* Participants with T2D framed it in terms of unmet clinical need —
*"You meet your doctor a couple of times per year, it's hard to explain all issues in such a small
window of opportunity"* — and the paper's title quote, *"anything that would help is a positive
development."*

Three free-text responses were **inconsistent with the yes/no answer given** (e.g. "Yes, I would feel
comfortable" alongside "feels a little intrusive") and were removed. A useful reminder that
single-item acceptability measures are noisier than they look.

## Relevance to Future Study Design

1. **On Beiwe, iOS lost roughly half again as much EMA data as Android in the same cohort — and the
   passive streams showed no OS effect.** Do not carry a single OS assumption across streams. Measure
   active and passive missingness by OS separately in your own pilot.
2. **Passive beat active by ~30 points in completers, and accelerometer beat GPS.** Consistent with
   five other studies here; safe to plan around, with magnitudes checked locally.
3. **Early completeness is a dropout predictor.** Dropouts were missing 83–86% of surveys and 50–66%
   of passive data *while still enrolled*. Instrument it and act on it.
4. **A fixed 3-hour response window excludes shift workers.** Two of the free-text complaints were
   schedule, not software. Participant-set timing is the cheapest available fix.
5. **Willingness to share is not the same as tolerating collection, and it is conditioned by illness.**
   93.9% versus 53.1%. A healthy-control arm may be substantially less willing to permit clinical
   data sharing than the patient arm, which has design consequences for any study that plans to
   return data to care.
6. **Older participants report more burden from survey length and battery.** Small effects, but they
   point the opposite way to the usual assumption that passive collection is age-neutral.
7. **Treat every Beiwe completeness figure from before mid-2024 as a lower bound.**

## Evidence Confidence

**Verified** — the participation flow (85/82/69/68) and the 81.2%/18.8% retention/attrition; all EMA
and passive missingness figures including the OS-stratified table with its t-statistics and p-values;
the Android-only call/text limitation and the 51/31 split; the tolerability distribution
(76.5%–89.7% "not a problem"); the age–tolerability associations; the 93.9% vs 53.1% hypothetical-use
split with χ² and p; the employment association; the two named discontinuation reasons; the free-text
quotations. Read from the full text and published PDF (PMC11390910), 2026-09-02.

**Internal inconsistency, noted above:** the Attrition subsection inverts the retention statement.
The abstract, discussion and raw counts agree on 81.2% retention.

**Pre-heartbeat.** Collection Feb–Aug 2021. All completeness figures are pre-`heartbeat` lower bounds.

**Unclear / not reported** — the pre-consent funnel; discontinuation reasons for the majority of
dropouts; compensation, if any; whether the iOS EMA penalty reflects notification delivery,
survey rendering (the "black screen" reports), or the 3-hour window interacting with iOS
notification handling. **The mechanism is unidentified, and identifying it would materially advance
Tier 15 Q111.**

**Generalisability.** Single-country (Ireland), 82.4% White Irish among feedback completers,
convenience-recruited through a diabetes charity — so the T2D arm is plausibly more
research-engaged and more health-motivated than a clinic-recruited sample would be, which is the most
likely confound on the 93.9% willingness figure.

**No COI.** Independent of the Beiwe developers.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.1186/s44247-024-00116-6
- Europe PMC: https://europepmc.org/article/PMC/PMC11390910
- Local PDF: `../literature/2024-mcinerney-bmcdigitalhealth-beiwe-feasibility-tolerability-type-2-diabetes.pdf`

## Related profiles

- Platform: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- **The iOS/Android contradiction:** [`carp-mpath-sense-performance-study.md`](carp-mpath-sense-performance-study.md),
  [`aware-chemotherapy-engagement.md`](aware-chemotherapy-engagement.md),
  [`beiwe-missing-data-sociodemographic.md`](beiwe-missing-data-sociodemographic.md)
- Passive-outlasts-active and early completeness as a dropout predictor:
  [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
- Within-passive stream ordering: [`dp-schizophrenia-tolerability.md`](dp-schizophrenia-tolerability.md),
  [`radar-base-treatment-engagement.md`](radar-base-treatment-engagement.md)
- Vendor/OS policy erosion of call and SMS streams: [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md),
  [`mindlamp-relapse-3site.md`](mindlamp-relapse-3site.md)
- Participant-set prompt timing: [`metricwire-sgm-youth-ema-feasibility.md`](metricwire-sgm-youth-ema-feasibility.md)
- EMA reactivity and distress: [`avicenna-ema-suicidal-ideation-iatrogenic.md`](avicenna-ema-suicidal-ideation-iatrogenic.md),
  [`metricwire-post-discharge-ema-reactivity.md`](metricwire-post-discharge-ema-reactivity.md)

## Sources

1. McInerney AM, Schmitz N, Matthews M, Deschênes SS. *BMC Digit Health* 2024;2:55.
   DOI 10.1186/s44247-024-00116-6. Full text and tables read from the published PDF and PMC XML
   (PMC11390910), 2026-09-02. Establishes every figure in this profile.
