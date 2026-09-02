# Bladon et al. 2026 — CONNECT nested pilot: Fitbit vs Apple Watch vs Samsung Galaxy Watch in psychosis, N=105 over 20 weeks

## Quick Facts

| Field | Details |
|---|---|
| Citation | Bladon S, Ainsworth J, Cahuantzi R, Cella M, Drake RJ, Eisner E, Emsley R, Faulkner S, Greenwood K, Gumley A, Haddock G, Kendall K, Kenny A, Lees J, Lewis S, Martin GP, Schwannauer M, Sperrin M, Walters J, Walsh A, Whelan P, Wykes T, **Bucci S**. "Evaluating Wearable Devices for Remote Monitoring in Psychosis: Pilot Study Nested Within the CONNECT Cohort Study." *JMIR Formative Research* 2026;10:e86049. DOI [10.2196/86049](https://doi.org/10.2196/86049). PMID 42413039 / PMC13340901. Published 2026-07-07. |
| Study design | **Nested device-selection pilot** inside a prospective observational cohort, with **three pre-specified objectives** (choice, acceptability, data quality) and a **pre-registered decision rule** in the statistical analysis plan for which device(s) to carry forward. Non-randomised: participants chose their device. |
| Sample size (enrolled / analyzed) | **107 recruited → 105 in the pilot cohort.** 76 (72.4%) completed a follow-up assessment; 70 (66.7%) completed ≥1 satisfaction item; **85 in the quantitative analysis (87 participant-device periods** after 2 device switches). |
| Population | People with an **ICD-10 F20–F29 schizophrenia-spectrum diagnosis**, ≥16 years, ≥1 acute psychosis episode in the past 2 years requiring unscheduled acute care, no relapse in the previous 12 weeks. Recruited via NHS mental health services at **6 UK sites** (Manchester, Sussex, South London, Glasgow, Edinburgh, South Wales). Median age 33.0 (IQR 24.0–45.0), 56.2% male, 53.3% White, **39% in the most deprived IMD quintile**, **82.9% receiving welfare benefits**. |
| Duration | Recruitment 2024-03-14 to 2024-07-31; pilot end 2024-10-21; data-continuity analysis to **week 20**. Follow-up assessments at 3–6 months. |
| Devices/platforms used | **[Fitbit](../../module-01-wearables/profiles/fitbit-google.md) Charge 5**, **[Samsung](../../module-01-wearables/profiles/samsung.md) Galaxy Watch 5**, **[Apple Watch](../../module-01-wearables/profiles/apple-watch-healthkit.md) SE**, participant's choice constrained by phone OS. Underlying infrastructure: the **CONNECT platform**, built on modified **CareLoop** and **[RADAR-base](../../module-02-digital-phenotyping/profiles/radar-base.md)** technologies by the University of Manchester Digital Health Software Team, with outsourced support from Hyve. UK AWS storage. Study Android phones provided to those without a suitable handset; £10/month data costs covered; £20 per clinical assessment. |
| Funding/COI | NHS/academic multi-site. **Platform-developer COI: S Bucci (senior author), J Ainsworth and two others are cofounders of CareLoop Health Ltd**, a University of Manchester spin-out whose technology underpins the CONNECT platform being used. JTRW has grant support from Takeda and Akrivia (unrelated). REC 23/WM/0044; ISRCTN 24746936. |
| Last verified | 2026-09-02 |

## Summary

The module's best-designed multi-device comparison, and the one that most cleanly separates the two
things studies usually conflate.

**Participants liked all three devices about equally. The devices did not perform anything like
equally.** Satisfaction across 29 questionnaire items produced no consistent winner — Apple Watch and
Fitbit each ranked first or joint-first on 11 items, Samsung on 9. Data completeness, on the same
cohort, differed by a factor of three:

| Metric (median % of possible) | Fitbit | Apple Watch | Samsung Galaxy |
|---|---|---|---|
| Valid step-count days | **74.8%** (IQR 32.1–96.9) | 64.3% (30.0–76.8) | 37.5% (15.4–60.7) |
| Valid heart-rate days | **80.1%** (26.7–95.0) | 49.3% (21.5–86.0) | 31.2% (8.5–46.0) |
| Valid sleep days | **49.4%** (12.5–87.3) | 23.6% (0–56.1) | **4.8%** (1.9–17.6) |
| **Valid heart-rate *hours*** | **53.0%** (21.3–92.4) | 28.8% (10.5–57.6) | **15.8%** (3.4–30.1) |

And the **most chosen device was the worst performing one**: 43.8% chose Samsung, 25.7% Apple Watch,
21.9% Fitbit.

The consequence is the paper's real contribution — a documented, pre-specified process for making a
device decision on data rather than preference, and an honest account of what that decision cost. The
Samsung Galaxy Watch was dropped from the main CONNECT cohort. **It was also the device
disproportionately chosen by Black and Black British participants (29.8% of Samsung users vs 12.8%
Apple), those in the most deprived IMD quintile (55.3% vs 28.6%), and the least employed group
(10.6% employed).** The authors state the tension plainly: *"While the decision taken was data-driven,
it may have unintended implications for inclusivity and representativeness in the CONNECT cohort."*

**This is a new finding for the module and it sharpens finding #6** (BYOD trades representativeness
for wear compliance). Here the trade-off appears **within a provisioned study**, through device
*choice*: optimising on data quality silently de-selects the most under-represented participants,
because device preference is socially patterned.

## Instrumentation and Deployment Model

**Researcher-provisioned, participant-chosen, OS-constrained.** iPhone users could take an Apple Watch
or a Fitbit; Android users an Android smartwatch or a Fitbit. Participants who already owned a
compatible device could keep using it (and were then excluded from objectives 2 and 3, because prior
familiarity would confound satisfaction and completeness). **Participants without a suitable
smartphone were provided with an Android phone.**

**Device selection rationale, stated:** commercial rather than research-grade devices, chosen for
uptake and adherence evidence, cost, sensor range, and **feasibility of accessing data for research —
explicitly including Fitbit intraday data and Apple SensorKit**. This is a rare instance of a study
naming *data-access architecture* as a device-selection criterion up front, which Module 1's profiles
argue is the decisive axis.

**Onboarding** was researcher-led after the baseline assessment, with an App and Wearable Guide.
Median onboarding times, on a subset of 52: **Apple Watch 60 min (IQR 58–98), Samsung 60 min (30–180),
Fitbit 90 min (83–120)** — no significant difference, and notably **all around an hour or more**. Any
study budgeting 15 minutes for wearable onboarding in a clinical population should look at those
numbers.

**A pre-registered decision rule** existed before the data: if one device clearly won on both quality
and acceptability it would be adopted; if not, a non-inferiority analysis of Fitbit against the
smartwatches (Fitbit preferred on cost and simplicity); if inconclusive, collect a further 6 months.

**Only 11.4% of the cohort owned and used a wearable before joining** — against a 41% UK adult
population estimate and 21% among people with psychosis-related disorders. This is a low-baseline
population, which makes the onboarding and troubleshooting figures more transferable to comparable
clinical cohorts than to consumer-user samples.

## Recruitment and Retention

107 recruited across 6 sites in ~4.5 months; **2 sites under-recruited (7 each against a 10 minimum)**,
which the authors flag as a possible source of demographic imbalance given documented between-site
demographic differences.

**Device choice at onboarding (n=105):** Samsung 46 (43.8%), Apple Watch 27 (25.7%), Fitbit 23
(21.9%), own device 3, **declined a wearable entirely 6 (5.7%)**. Over the study, 5 changed: 2
switched device, 2 stopped using a wearable, 1 who had initially declined started.

**Follow-up:** 76/105 (72.4%) completed a follow-up assessment; 70/105 (66.7%) completed at least one
satisfaction item.

**Exclusions before the quantitative analysis** are reported and materially shape the results:
participants using their own device (3), participants with unresolvable **data file downloading and
merging issues** (affecting all three device groups), and participants with **no passive data at all
— every one of them in the Samsung group**, due to withdrawal or disengagement soon after onboarding.
The authors excluded the latter because including them, all from one arm, "risked disproportionately
biasing the results" — a defensible choice that nonetheless **removes the Samsung group's worst cases
from the Samsung group's completeness figures**. The 15.8% median hourly heart-rate coverage is
therefore an *optimistic* estimate for that device.

## Data Completeness and Technical Issues

**Two definitions are used and the authors are explicit about why, which is exemplary.**

- **Objective 2 — "valid day": any day with any recorded sleep, heart-rate or step data**, expressed
  as a percentage of days between onboarding and the earlier of pilot end or withdrawal. They state
  this "may overestimate meaningful wear time" and adopted it only because **Samsung step counts are
  available as daily totals only**, so a finer common denominator did not exist.
- **Objective 3 — "valid heart-rate hour": any hour with ≥1 heart-rate observation**, as a proportion
  of total possible hours assuming continuous 24-hour wear.

The gap between the two definitions on the same data is large — Fitbit 80.1% of valid days versus
53.0% of valid hours; Samsung 31.2% versus 15.8% — and it is a clean, in-paper demonstration of the
module's central methodological warning. **A "valid day" metric roughly doubles the apparent
completeness of an hourly one.**

**Continuity over 20 weeks** (≥3 days of valid heart-rate data per week):

| | Week 1 | Week 20 |
|---|---|---|
| Fitbit | **95% (19/20)** | 62.5% (5/8) |
| Apple Watch | 85.2% (23/27) | 57.1% (4/7) |
| Samsung Galaxy | **40% (16/40)** | 16.7% (3/18) |

**Fitbit stayed above 50% in every one of the 20 weeks; Samsung never reached 50% in any week.**

**Named technical failure modes, with counts** — 30 queries escalated to the software team:

- **Samsung: 20 of 30 (66.7%).** **17 of those 20 were traced to a newly enforced Samsung privacy
  policy that blocked data transmission.** A vendor policy change, mid-study, unilaterally degrading a
  study's primary data stream. This is the same class of event as the Google Play call/SMS
  restriction recorded in [Niemeijer 2023](carp-mpath-sense-performance-study.md) and
  [RADAR-MDD](radar-mdd-recruitment-retention.md), and it is the clearest single instance in the
  module of **vendor risk as a study risk**.
- **Fitbit: 6 (20%)** — 4 hardware malfunctions, 2 data-flow problems.
- **Apple Watch: 4 (13.3%)** — older iOS versions preventing pairing; participants logged out of the
  app, disrupting upload.
- **A silent data-corruption failure that no completeness metric would have caught: 98% of Samsung
  sleep data had duplicated start timestamps across sleep stages and missing end timestamps, making
  it impossible to derive sleep duration at all.** Sleep data were nominally "present" for 80% of
  Samsung users. They were unusable. **Completeness and correctness are different, and only one of
  them is routinely reported.**

**Metric resolution differed sharply between devices** even where the metric name was the same: Fitbit
minute-level step counts; **Apple Watch via SensorKit every few seconds, plus raw accelerometer
access**; **Samsung daily step totals only**. Fitbit and Apple Watch offered additional physiological
metrics; Samsung did not.

**Passive and active engagement moved together** across all three device groups, and Poisson models
adjusting for completed active-symptom-monitoring questionnaires showed **only weak evidence that
completeness differences were attributable to device choice** rather than to general study engagement
— an important caveat the authors do not bury. Adjusting for demographics, **being male was
associated with higher wearable data completeness (IRR 1.38, 95% CI 1.01–1.90)**; age, ethnic group,
employment, benefits and deprivation were not.

## Feasibility Findings

Fitbit was retained for the main cohort on data quality and cost. **Apple Watch was also retained**,
for three stated reasons: it was chosen more often than Fitbit, so dropping smartwatches risked
uptake; keeping two devices tests whether a relapse-prediction model can avoid single-device
dependence; and its richer metrics (including SensorKit raw accelerometer) support feature extraction
in a subsample. **Samsung was discontinued** on data volume, data quality, limited physiological
outputs, and staff troubleshooting burden.

The authors' own framing of the central lesson: *"devices may be acceptable to participants, but this
does not necessarily result in higher data completeness"*, and a nested device-evaluation pilot is
therefore **good practice before committing a large cohort**.

**Limitations they name and that constrain reuse:** it is not possible to separate non-wear from
hardware failure from pipeline failure; **only the Apple Watch provides an explicit wear indicator**,
so heart rate is a proxy for wear everywhere else; device allocation was by participant choice, not
randomised, so groups differ demographically; and results are specific to three device models at one
moment in a fast-moving firmware landscape.

## Relevance to Future Study Design

1. **Run a nested device-selection pilot with a pre-registered decision rule before committing a
   large cohort.** This is the transferable design contribution, independent of which device won.
2. **Do not select a device on acceptability data.** Satisfaction was flat across three devices whose
   completeness differed threefold. If you measure only acceptability, you will choose the wrong
   device — and here, the most-preferred device was the worst performer.
3. **Optimising on data quality can de-select your least-represented participants.** Samsung was
   disproportionately chosen by Black participants, the most deprived quintile, and the least
   employed. A data-driven device decision is not demographically neutral. **Report the demographics
   of the arm you are dropping.**
4. **Vendor policy change is a live study risk.** 17 of 30 escalations traced to one Samsung privacy
   policy enforced mid-study. Ask, before selecting: what happens to this data pipeline if the vendor
   changes its terms next quarter?
5. **Check correctness, not just completeness.** 98% of Samsung sleep records were present and
   unusable. A completeness dashboard would have shown green.
6. **Budget an hour or more per participant for wearable onboarding** in a clinical population with
   11% prior wearable use — 60 to 90 minutes median across all three devices.
7. **State whether your denominator is days or hours.** Fitbit reads 80.1% or 53.0% depending only on
   that choice, in the same paper on the same data.
8. **Passive and active engagement co-vary.** After adjusting for active-questionnaire completion,
   the device effect weakened. Some of what looks like a device difference is a participant
   engagement difference that happens to be correlated with device choice.

## Evidence Confidence

**Verified** — all recruitment, choice and follow-up counts; the full baseline demographic table
including the IMD and ethnicity breakdowns by device; both completeness definitions; every median and
IQR in the two completeness tables with their Kruskal-Wallis/Bonferroni p-values; the week-1 and
week-20 continuity figures; the 30 escalated queries with their device breakdown and the 17/20 Samsung
privacy-policy attribution; the 98% Samsung sleep-timestamp corruption; the onboarding-time medians;
the 11.4% prior wearable ownership; the Poisson IRR 1.38 sex association; the retained/discontinued
decisions and their stated reasons. Read from the PMC full-text XML (PMC13340901), 2026-09-02.

**Corroborated, not experimentally isolated** — that the device *caused* the completeness differences.
Allocation was by participant choice, groups differed demographically at baseline, and the authors'
own Poisson models adjusting for active engagement found **only weak evidence** for a device-attributable
effect. The mechanism for Samsung's poor showing is partly identified (the privacy-policy block, the
timestamp corruption, daily-only step resolution) but non-wear, hardware failure and pipeline failure
cannot be separated. **Read the ranking as a decision that was correct for this study, not as a
general device ranking.**

**Selection effect inside the completeness figures.** Participants with **no** passive data — all
Samsung — were excluded from the quantitative analysis. Samsung's reported completeness is therefore
an over-estimate.

**COI — the strongest in this batch.** The senior author and three co-authors cofounded CareLoop
Health Ltd, whose technology (alongside RADAR-base) underlies the CONNECT platform through which all
data flowed. The platform itself is not the object of comparison — three third-party consumer devices
are — which limits the exposure, but the platform's data-pipeline failures ("issues with the
downloading and merging of data files, which affected participants in each wearable group") are
attributable to the authors' own infrastructure and are reported without quantification.

**No accuracy validation.** Data completeness is a proxy for quality; no comparison against
research-grade reference devices was performed. Sensor-accuracy questions belong to Module 1.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.2196/86049
- Europe PMC: https://europepmc.org/article/PMC/PMC13340901
- ISRCTN 24746936: https://www.isrctn.com/ISRCTN24746936
- Local PDF: **not stored** — the Europe PMC render and the JMIR PDF endpoint both refuse automated
  retrieval. Full text read from PMC full-text XML.

## Related profiles

- Devices: [Fitbit/Google](../../module-01-wearables/profiles/fitbit-google.md),
  [Samsung](../../module-01-wearables/profiles/samsung.md),
  [Apple Watch/HealthKit/SensorKit](../../module-01-wearables/profiles/apple-watch-healthkit.md)
- Platform: [RADAR-base](../../module-02-digital-phenotyping/profiles/radar-base.md)
- Other RADAR-base deployments: [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md),
  [`radar-mdd-longterm-engagement.md`](radar-mdd-longterm-engagement.md),
  [`radar-ad-feasibility-usability.md`](radar-ad-feasibility-usability.md),
  [`radar-base-treatment-engagement.md`](radar-base-treatment-engagement.md)
- Vendor/OS policy change degrading a data stream mid-study:
  [`carp-mpath-sense-performance-study.md`](carp-mpath-sense-performance-study.md),
  [`mindlamp-relapse-3site.md`](mindlamp-relapse-3site.md)
- Configuration/infrastructure losing data that participants supplied:
  [`empatica-epilepsy-data-quality.md`](empatica-epilepsy-data-quality.md)
- Representativeness cost of device requirements: [`byod-demographic-imbalance.md`](byod-demographic-imbalance.md),
  [`aware-light-smartsense-d-youth-depression.md`](aware-light-smartsense-d-youth-depression.md)
- Device chosen by the user group: [`sleepsight-schizophrenia-rest-activity.md`](sleepsight-schizophrenia-rest-activity.md)

## Sources

1. Bladon S, Ainsworth J, Cahuantzi R, et al. *JMIR Form Res* 2026;10:e86049. DOI 10.2196/86049.
   Full text and all tables read from PMC full-text XML (PMC13340901), 2026-09-02. Establishes every
   figure in this profile.
