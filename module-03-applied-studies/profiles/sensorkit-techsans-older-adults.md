# Shen et al. 2026 — Apple SensorKit multimodal passive sensing in older adults (TechSANS), N=21 over ~6 months

## Quick Facts

| Field | Details |
|---|---|
| Citation | Shen Y, Huang M, Park JH, Benge JF, Rousseau JF, Lester-Smith RA, Thomaz E. "Multimodal passive smartphone sensing in older adults: a guide for clinical scientists based upon an ongoing cohort study." *Innovation in Aging* 2026;10(4):igag007. DOI [10.1093/geroni/igag007](https://doi.org/10.1093/geroni/igag007). PMID 41853224 / PMC12995428. Published online 2026-01-28. |
| Study design | **Methodological guide plus feasibility/adherence analysis** drawn from an ongoing observational cohort, with an exploratory cross-sectional GLMM analysis of 145 digital measures against baseline cognitive status. |
| Sample size (enrolled / analyzed) | **21 participants** with baseline cognitive assessments available (recruited through June 2024 from an ongoing study). **3 ended participation early**; **1 further excluded from all statistical analyses** for app-related data loss. |
| Population | Adults **≥65** in and beyond the Austin, Texas metro area. Mean age **75.81 ± 4.86**; **17.71 ± 1.79 years of education**; 13 cisgender women / 8 cisgender men; **20 of 21 non-Hispanic White**. Baseline: 17 cognitively normal, 3 possible MCI, 1 possible dementia. |
| Duration | Intended 1 year per participant; this analysis uses data within 6 months of each participant's baseline cognitive assessment, cut off 2024-11-26. Recruitment began May 2023. |
| Devices/platforms used | **TechSANS**, a purpose-built **iOS** app using **[Apple SensorKit](../../module-01-wearables/profiles/apple-watch-healthkit.md)** for device usage, keyboard typing, communication and ambient light, plus Core Motion/Health for motion, activity, gait, pedometer and location. Data to AWS (HIPAA-compliant) on Wi-Fi while charging or >50% battery. REDCap for identifiable data. **An Android version was later built on [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md) but is not analysed here.** |
| Funding/COI | NIH R01AG077017. **Conflict of interest: none declared.** IRB: University of Texas at Austin STUDY00002933. |
| Last verified | 2026-09-02 |

## Summary

**Platform attribution correction — read this first.** Both discovery scans list this study as
spanning **Beiwe, mindLAMP and RADAR-base**, and the recency scan describes it as "a rare
cross-platform guide." **That is wrong.** The full text names Beiwe and mindLAMP exactly once each,
in a single sentence of the Application Development section: an Android build was *later* created on
Beiwe (and is not analysed), and Avicenna and mindLAMP are mentioned as **publicly available
SensorKit-enabled alternatives** for readers who cannot build their own app. RADAR-base does not
appear at all. The deployed platform is **TechSANS**, a bespoke iOS app, and the analysis is
iOS-only. The module still has **no** study comparing Beiwe, mindLAMP and RADAR-base head to head.

With that corrected, what remains is still valuable and fills two genuine gaps: **older adults** (the
oldest cohort in the module by some margin) and **Apple SensorKit as a deployed research
instrument**, which Module 1 profiles as a capability but which no Module 3 entry had yet shown in
the field.

The operational core: **each participant contributed on average 141 days of usable digital measures,
74.4% of the data inclusion period** — under a demanding daily-inclusion rule (≥14 h of sensing
between 06:00 and midnight). And the withdrawal reasons are unusually specific and unusually useful.

## Instrumentation and Deployment Model

**BYOD iOS.** Eligibility required being ≥65, owning a smartphone with basic operating skills, having
home Wi-Fi, and having a collateral informant aged ≥21.

**SensorKit is the load-bearing dependency and the paper says so explicitly:** device usage, keyboard
typing, communication and ambient light **all require Apple's SensorKit entitlement, "exclusively
granted to approved research studies."** The authors direct readers to Apple's own access process and
warn that it requires additional Apple review. **Because the entitlement was granted for this study
alone, the app cannot be distributed for external use** — which is why they point readers at
Avicenna and mindLAMP as SensorKit-enabled alternatives.

This is the operational face of what Module 1's
[Apple profile](../../module-01-wearables/profiles/apple-watch-healthkit.md) records as a
multi-month critical path: a study can obtain unique iOS behavioural streams, and the resulting
instrument is then locked to that study.

**Power/bandwidth policy:** upload only on Wi-Fi, and only while charging or above 50% battery — a
deliberate, documented duty cycle that reduces battery burden and shifts data latency.

**Privacy design as a retention mechanism.** At onboarding, participants were shown **sample data
from each modality** to illustrate what was actually collected, and were **shown how to disable
individual data streams**. The result: **no participant withdrew for privacy reasons, and only one
participant turned off a single data stream over the whole study.** Given that participant-facing
transparency is usually argued for on ethical grounds alone, this is direct evidence it is also
cheap in data terms.

## Recruitment and Retention

Recruitment (from May 2023) used referrals from an urban outpatient neurodegenerative-conditions
clinic, newspaper advertisements targeting adults 55+, and presentations at retirement communities;
participation was open nationwide.

No pre-consent funnel (approached / screened / ineligible) is reported.

**Of the 21 in this analysis, 3 ended participation early:**

- **1 withdrew at 4 months citing lack of perceived benefit**, in an observational study with no
  intervention and — crucially — **no compensation of any kind**.
- **2 withdrew at the 6-month milestone attributed to technical problems with the app.** The
  underlying issues were fixed by a later app update, but "both participants became frustrated and
  withdrew."

A **fourth** participant was excluded from all statistical analyses because of app difficulties
causing significant data loss "despite multiple troubleshooting attempts by the study team."

So **4 of 21 (19%) were lost to either technical failure or unrewarded burden**, and **3 of those 4
were technical.**

## Data Completeness and Technical Issues

**Definition, stated precisely, and it is a strict one.** A day yields digital measures only if it has
**≥14 hours of sensing between 06:00 and midnight**; location features requiring home identification
additionally need **≥1 hour of data between midnight and 06:00**. Days without time-zone information
were discarded, as were days with time-zone transitions (travel). Exceptions — distance travelled,
total moving time, time of first movement, convex hull — need only the daytime criterion.

**Result: mean 141 days of digital measures per participant, 74.4% of the data inclusion period.**

Missing-data handling is deliberately conservative and worth copying: **missingness was preserved as
potentially meaningful** rather than imputed wholesale. Imputation was applied *only* to empty
event-based streams (activities, pedometer, typing, communication) **on days that already met the
daytime sensing threshold**, where an empty stream means "no calls happened", not "no data arrived".

**Named technical failure modes:**

1. **iOS background execution constraints requiring active participant maintenance.** The paper states
   it plainly: although the app required no active interaction, **"iOS system constraints required
   participants to keep the app running in the background (ie, not swipe it away from the app
   switcher) and to reopen it after each phone restart."** This is the module's finding #3 —
   purely passive smartphone collection does not exist — reproduced on a **fourth** independent
   architecture (after Beiwe, CARP and mindLAMP), and here on **iOS specifically**, with a bespoke
   first-party app rather than a general-purpose platform. It is not a platform defect. It is the OS.
2. **Phones switched off overnight** — 2 participants — which removed the midnight–06:00 hour needed
   for home identification, so whole-day location features could not be computed for those days.
3. **Voice input instead of typing** — 2 participants never accumulated 30 days of typing events, so
   typing-timing and error-distance measures were dropped for them. A behavioural, not technical,
   source of stream-specific missingness that a study relying on keystroke dynamics must plan for.
4. **Unreproducible iOS-level failures**: **no text-message records for one participant, and no Health
   app data for another.** Neither could be reproduced in internal testing; both were attributed to
   iOS malfunction. The team reports such events were rare in later enrolees.

## Feasibility Findings

The authors conclude that multimodal passive smartphone sensing is feasible in older adults, on the
basis of 141 days / 74.4% coverage per participant and no privacy-driven attrition.

Their own "considerations for improvement" section is the most decision-relevant part of the paper,
and it contradicts an assumption several other studies in this module rest on:

> **"Findings from this feasibility analysis suggest that, even with low-burden data collection,
> compensation may play an important role in reducing attrition."**

They ran an uncompensated study on the explicit reasoning that passive collection is low-burden and
therefore does not need payment, and lost a participant to "lack of perceived benefit." Their
recommended remedies are one-time payment, milestone rewards, **or non-monetary benefit such as
returning cognitive-assessment results** — the latter unavailable to them because assessments were
administered by graduate students rather than licensed clinicians.

They also recommend that **"smartphone operating skills" be assessed through practical tasks rather
than self-report**, having found the background-maintenance requirement too demanding for some
participants, and that apps be tested extensively pre-release because technical frustration itself
caused withdrawals.

## Relevance to Future Study Design

1. **Budget the SensorKit entitlement as a study-specific, non-transferable asset.** Approval is
   per-study and per-Apple-review; the resulting app cannot be reused. If the streams you need are
   SensorKit-only, either take that path or use a platform that already holds the entitlement
   (Avicenna, mindLAMP).
2. **iOS still requires the app to be kept out of the app switcher and reopened after reboot.** Any
   iOS-only protocol must instruct participants explicitly and must expect to lose the participants
   who cannot sustain it. In this cohort that was 3 of 21.
3. **Low burden is not a substitute for compensation.** This is the module's clearest counter-example
   to the reading that passive studies can run unpaid. It sits directly against
   [Liu 2019](lamp-schizophrenia-cognition-unpaid.md), where unpaid patients out-engaged unpaid
   controls threefold, and alongside [Mercier 2020](beiwe-spinal-cord-injury-incentives.md)'s finding
   that incentives buy *enrolment persistence*. The synthesis is not "incentives don't matter" but
   **"incentives buy persistence, and persistence is what a 12-month passive study needs."**
4. **Show participants their own raw data and how to switch streams off.** Zero privacy withdrawals
   and one stream disabled across the cohort. The intuition that offering an off-switch will cost you
   data is not supported here.
5. **State the daily inclusion rule.** 74.4% coverage under a ≥14 h/day rule is a materially different
   claim from 74.4% under "any data on the day", and this module contains studies using both.
6. **Preserve informative missingness.** Imputing an empty communication stream as zero on a day with
   adequate sensing, and leaving it missing otherwise, is a defensible and rarely-articulated rule.
7. **Assess smartphone competence by task, not self-report.**

## Evidence Confidence

**Verified** — the platform (TechSANS, bespoke iOS, SensorKit-dependent) and the fact that Beiwe and
mindLAMP were **not** the deployed platforms; the cohort composition and demographics; the 141-day /
74.4% coverage figure; the daily inclusion criteria; the imputation rule; all four named technical
failure modes with their participant counts; the three withdrawals and their stated reasons; the
absence of compensation and the authors' own conclusion about it; the privacy-transparency result (no
privacy withdrawals, one stream disabled). Read from the full text and PDF (PMC12995428), 2026-09-02.

**Reported** — the attribution of the missing text-message and Health-app streams to iOS malfunction.
Not reproducible in internal testing, by the authors' own account.

**Unclear / not reported** — the pre-consent funnel; whether the 74.4% figure would differ under a
less strict daily rule; any Android or Beiwe data, since the Android build postdates this analysis.
**No OS-stratified comparison is possible: the analysis is iOS-only.**

**Small and homogeneous.** N=21, **20 of 21 non-Hispanic White**, mean 17.7 years of education. The
authors name this as a limitation and note that older adults with regular smartphone use are more
likely to enrol than those with severe cognitive decline and limited use — the same
selection-into-digital-competence effect that
[Cho 2022](byod-demographic-imbalance.md) documents for BYOD generally.

**Scope note.** TechSANS is not itself a Module 1 or Module 2 technology. This profile is scoped as an
**Apple SensorKit deployment**, which Module 1's
[Apple profile](../../module-01-wearables/profiles/apple-watch-healthkit.md) does cover, and its
findings are read as evidence about SensorKit-based collection rather than about any particular app.

## Key Links

- Paper (OA): https://doi.org/10.1093/geroni/igag007
- Europe PMC: https://europepmc.org/article/PMC/PMC12995428
- Apple SensorKit access process: https://www.researchandcare.org/resources/accessing-sensorkit-data/
- Local PDF: `../literature/2026-shen-innovaging-multimodal-passive-smartphone-sensing-older-adults.pdf`

## Related profiles

- Device/ecosystem: [Apple Watch / HealthKit / SensorKit](../../module-01-wearables/profiles/apple-watch-healthkit.md)
- Platform mentioned but not deployed: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md),
  [mindLAMP](../../module-02-digital-phenotyping/profiles/mindlamp.md)
- The same OS constraint on three other architectures: [`beiwe-als-adherence.md`](beiwe-als-adherence.md),
  [`carp-mpath-sense-performance-study.md`](carp-mpath-sense-performance-study.md),
  [`mindlamp-linc-passive-data-quality.md`](mindlamp-linc-passive-data-quality.md)
- Compensation and engagement, pointing the other way:
  [`lamp-schizophrenia-cognition-unpaid.md`](lamp-schizophrenia-cognition-unpaid.md),
  [`beiwe-spinal-cord-injury-incentives.md`](beiwe-spinal-cord-injury-incentives.md)
- Selection into digital competence: [`byod-demographic-imbalance.md`](byod-demographic-imbalance.md)
- Threshold choice determining analytic N: [`actigraph-als-upper-limb-wear-time.md`](actigraph-als-upper-limb-wear-time.md)

## Sources

1. Shen Y, Huang M, Park JH, Benge JF, Rousseau JF, Lester-Smith RA, Thomaz E. *Innov Aging*
   2026;10(4):igag007. DOI 10.1093/geroni/igag007. Full text read from the published PDF and PMC XML
   (PMC12995428), 2026-09-02. Establishes every figure in this profile, and establishes that the
   deployed platform was TechSANS on Apple SensorKit, **not** Beiwe, mindLAMP or RADAR-base.
