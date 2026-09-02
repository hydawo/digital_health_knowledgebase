# Niemeijer et al. 2023 — m-Path Sense pilot: CARP Mobile Sensing coverage and user experience, N=104 over 3 weeks

## Quick Facts

| Field | Details |
|---|---|
| Citation | Niemeijer K, Mestdagh M, Verdonck S, Meers K, **Kuppens P**. "Combining Experience Sampling and Mobile Sensing for Digital Phenotyping With m-Path Sense: Performance Study." *JMIR Formative Research* 2023;7:e43296. DOI [10.2196/43296](https://doi.org/10.2196/43296). PMID 36881444 / PMC10031448. |
| Study design | Platform-development paper **with a real 3-week pilot cohort**, evaluated against two pre-stated criteria: **sampling reliability** and **perceived user experience**. Included here for the pilot's deployment data, not for its architecture description. |
| Sample size (enrolled / analyzed) | **104** participants contributing data. **52 iOS (50%) / 52 Android (50%)** — an unusually clean natural experiment on OS. |
| Population | Dutch-speaking adults (≥18) recruited via Facebook groups and a KU Leuven experiment-recruitment system, **selected on availability and on neuroticism scores (BFI-2) to achieve variability**. Excluded: non-native Dutch speakers, under-18s, and phones older than **Android 7.0 / iOS 13.0**. |
| Duration | **3 weeks (21 days)**, ESM questionnaires delivered while mobile sensing ran in the background. |
| Devices/platforms used | **m-Path Sense** = **[m-Path](../../module-02-digital-phenotyping/profiles/m-path.md)** (ESM) fused with **[CARP Mobile Sensing (CAMS)](../../module-02-digital-phenotyping/profiles/carp-mobile-sensing.md)**, the DTU Flutter framework. Plus **`mpathsenser`**, a companion R package extracting raw data into SQLite. Participant-owned phones. |
| Funding/COI | Academic — KU Leuven. **This is a platform paper written by the platform's own developers**, evaluating their own software. Ethics: KU Leuven SMEC G-2020-2200-R3[AMD]. |
| Last verified | 2026-09-01 |

## Summary

**The only deployment-with-a-cohort this module has been able to locate for CARP Mobile Sensing** — and the reason is that CAMS is a *framework*, not a product: it ships inside other people's apps, and those apps get the citations. Here it is the sensing engine underneath m-Path.

Its central finding is a number every phenotyping study should have to state and almost none do:

> **The relative coverage rate — actual measurements ÷ expected measurements — hovered around 0.50.** Roughly **half** of the data the sampling schema specified was never collected.

The absolute data volume looks abundant (69.51 GB across 104 participants over 21 days; 430.43 GB decompressed; 84.3 million observations after binning accelerometer and gyroscope to one value per second). The authors' point is that **abundance is not coverage**, and only the ratio against the schema reveals the shortfall. Cause: the OS pushing the app into the background and eventually killing it — Android's doze mode and its iOS equivalents.

And then the OS comparison, which contradicts the folk wisdom:

| | Android (n=52) | iOS (n=52) |
|---|---|---|
| Median number of gaps (≥5 min with no data from any sensor) | 157 | 165 |
| **Median gap duration** | **7.55 minutes** | **47.36 minutes** |
| Mean total gap time over 21 days | 4.50 days (old OS) / 6.43 days (new OS) | **1.68 weeks (old) / 1.99 weeks (new)** |

**Both platforms produce a similar *number* of gaps; iOS gaps are roughly six times longer**, costing iOS participants around two of every three weeks of sensing. This is the reverse direction from [McClaine et al.](aware-chemotherapy-engagement.md), who found Android yield *lower* than iOS under AWARE. **The two findings cannot both be general. Treat OS-yield asymmetry as framework- and configuration-specific and measure it in your own pilot.**

## Instrumentation and Deployment Model

**BYOD with an OS floor.** Phones older than Android 7.0 or iOS 13.0 were excluded at prescreening for technical compatibility — a lighter-touch version of the handset problem that cost [SmartSense-D](aware-light-smartsense-d-youth-depression.md) seven withdrawals.

**Architecture, stated plainly by the authors:** m-Path provided the ESM layer ("well established in both research and clinical settings", >15,000 users, >500,000 questionnaires completed since 2019); **CAMS was added to provide mobile sensing**, and is "specifically designed to be integrated into other apps, acting as a loosely coupled component." This is the adoption model Module 2's [CARP profile](../../module-02-digital-phenotyping/profiles/carp-mobile-sensing.md) describes — a library, not a portal — and this paper is its clearest published instance.

**A named regulatory constraint on data streams:** m-Path Sense **supports call and text logs on Android**, but because collecting them "is against Google's policy," **they are not included in the Google Play Store version**. This is the same platform-policy erosion that removed call/SMS logs from [RADAR-MDD](radar-mdd-recruitment-retention.md) and rendered the CrossCheck benchmark dataset unreproducible per [Cohen et al.](mindlamp-relapse-3site.md) Documented here as a distribution-channel constraint rather than an OS one.

**Transparency features:** a **permanent notification (Android) or blue dot (iOS)** while sensing is active; an in-app view of which sensors are running, the participant's ID, and how much data has been collected; and withdrawal by deleting the app.

**Incentive:** compliance-graduated — full remuneration of **€70 (US $79) or 10 course credits at ≥75% ESM compliance**, with **each 10-percentage-point drop costing €10 or one credit**. The same shape as [Bonnier et al.](mpath-nssi-ema-benefits-challenges.md)'s €20–€100 gradient.

## Recruitment and Retention

Convenience recruitment (Facebook groups, university participant pool) with **purposive selection on neuroticism** to ensure variability. No enrolment funnel, screening-exclusion counts or withdrawal figures are reported; **104 is the number who contributed data**, and no retention rate can be derived. ESM compliance is likewise not reported as a cohort figure — only referenced through the incentive threshold.

This is a real limitation for a Module 3 entry, and it reflects the paper's purpose: it is measuring the software, not the cohort.

## Data Completeness and Technical Issues

**Volume:** 83,875 files across 104 participants — **5.51% JSON (4,622) and 94.49% ZIP (79,253)** — totalling 69.51 GB, **37.50 files and 31.10 MB per participant per day**. The SQLite database after binning: **84,299,462 observations, 18.30 GB.**

**iOS produced far more data per person** — 140.12 MB of JSON and 921.42 MB of ZIP versus Android's 60.13 MB and 212.23 MB — and filled a 5 MB file in a **median 8.83 minutes**, versus Android's **1.80 hours**. So iOS yields more data *while it is running* and far longer gaps *when it is not*. Volume and coverage move in opposite directions across the OS split, which is exactly why the coverage ratio is the metric that matters.

**Coverage: the relative coverage rate frequently hovered around 0.50.**

**Gaps** (a gap = ≥5 minutes with no measurement from any sensor), over the 21-day pilot:

- **Android: median 157 gaps, median duration 7.55 minutes.**
- **iOS: median 165 gaps, median duration 47.36 minutes.**
- Mean **total** gap time differed significantly by OS (F1,102 = 52.10; P<.001; partial η² = 0.34) — Android 4.50 days (old OS versions) / 6.43 days (new), iOS 1.68 weeks (old) / 1.99 weeks (new).
- **Old vs new OS versions within a platform did not differ significantly** (F1,102 = 3.69; P=.06). The platform matters; the version does not.

**Named technical failure modes:**

1. **OS background termination** (Android doze mode and equivalents) — the dominant cause of gaps, and the authors note both Android and Apple "have become increasingly strict in recent years."
2. **Truncated JSON files.** When the app is killed mid-write, the JSON file is left with incorrect endings and is not valid JSON. On restart the app opens a **new** file rather than continuing, so **the presence of loose JSON files among the ZIPs is itself a diagnostic of app kills** — a genuinely useful, transferable data-quality signal.
3. **iOS file deletion by the OS.** Early in the study, **12/104 (11.5%) iOS users had m-Path Sense's files deleted by the operating system**, stopping the app. Fixed by reinstalling.
4. **App crashes or freezes on start-up** — reported by **18/104 (17.3%)** of participants, though occurring in only **2.23% of Android ESM beeps** and **0.45% of iOS beeps**.
5. **Battery drain** — reported at **1.34% (133/9,924) of Android beeps** and **15.00% (1,365/9,096) of iOS beeps**; at debriefing, **27/104 (25.9%)** described it as noticeable but manageable.

**The mitigation the authors were implementing** — "send a signal to the server every 5 minutes to show that it is still [running]" — is the same architectural answer as **Beiwe's `heartbeat` push**, arrived at independently. See this module's README finding on purely-passive collection not existing.

## Feasibility Findings

**Authors' conclusion:** the total data gathered is "sufficient for most studies, even though it is lower than the intended sampling frequency owing to OS limitations"; minor battery drain was reported but not considered problematic for the assessed participants' user experience; and reliable passive collection with mobile phones "remains challenging" while being "a promising approach toward digital phenotyping when combined with ESM."

The ease of use of the ESM component was **deliberately not investigated**, since m-Path was already widely used — so this paper says nothing about the survey experience, only about the sensing layer.

## Relevance to Future Study Design

1. **Report a coverage ratio, not a data volume.** 69.51 GB sounds like success; 0.50 coverage is the truth. Any study reporting passive-sensing "success" in gigabytes, file counts, or observations should be read as not having computed the ratio.
2. **Measure the number *and* duration of gaps separately.** Equal gap counts with 6× duration differences produced completely different effective coverage across OS.
3. **Do not assume the OS-yield direction.** This study and [McClaine et al.](aware-chemotherapy-engagement.md) disagree in direction on the same question. Pilot it.
4. **OS version is not the lever; OS platform is.** No significant old-vs-new difference within either platform.
5. **Loose JSON files are a free app-kill counter.** Any framework writing chunked files can expose the same diagnostic.
6. **Expect a heartbeat mechanism to be necessary.** Two independent platforms converged on server-side keepalives.
7. **Store-distribution policy can silently remove a data stream.** Call and SMS logs are supported by the code and absent from the Play Store build. Check what the *distributed* build actually collects, not what the framework supports.
8. **Budget the storage.** 31.10 MB per participant per day, and 430 GB decompressed for 104 participants over 21 days, is a real infrastructure cost that scales linearly with cohort size.

## Evidence Confidence

**Verified** — the 104-participant 50/50 iOS-Android split and handset make-up, the 21-day duration, all volume figures (69.51 GB, 430.43 GB decompressed, 83,875 files with the JSON/ZIP split, 84,299,462 observations, 18.30 GB SQLite, 37.50 files and 31.10 MB per participant per day), the ~0.50 coverage rate, all gap counts and durations with the ANOVA statistics, the five named technical failure modes with their participant and beep-level rates, the incentive structure, the OS-version floor, and the Google Play call/SMS-log exclusion. Read from the full text (Europe PMC PMC10031448), 2026-09-01.

**Reported** — the attribution of gaps to OS background-termination behaviour. Highly plausible, consistent with every other platform in this module, and supported by the platform difference; not directly instrumented.

**Unclear / not reported** — ESM compliance as a cohort figure; enrolment funnel; withdrawals; retention. This is a performance study of software, and its cohort reporting is correspondingly thin.

**Scope note.** `CLAUDE.md` excludes "platform-architecture/methods papers with no deployment cohort." This paper **has** a deployment cohort of 104 over 21 days, and its coverage, gap and failure-mode data are among the most operationally specific in the module. It is included on that basis. The architectural description of m-Path Sense belongs to — and should be catalogued in — Module 2.

**COI — the strongest in this batch.** The authors are the developers of m-Path and m-Path Sense at KU Leuven, publishing an evaluation of their own platform. Two things temper it materially: the headline sampling finding is **unflattering** (half the intended data was not collected), and five distinct technical failure modes are named with rates. The user-experience conclusion ("not considered problematic") is the claim most exposed to the COI, and rests on debriefing self-report from a young, self-selected, incentivised, non-clinical sample.

**CARP-specific caveat.** This is evidence about **CAMS embedded in m-Path Sense, configured by the m-Path team, on a Belgian university sample**. It is not evidence about CAMS in general, nor about DTU's own CARP-based applications. Module 2's [CARP profile](../../module-02-digital-phenotyping/profiles/carp-mobile-sensing.md) records "adoption outside DTU" as an open question; this paper answers it affirmatively for at least one external group, which is itself a finding.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.2196/43296
- Europe PMC: https://europepmc.org/article/PMC/PMC10031448
- m-Path: https://m-path.io/
- CARP Mobile Sensing (Flutter package): https://pub.dev/packages/carp_mobile_sensing
- `mpathsenser` R package: https://github.com/koenniem/mpathsenser
- Local PDF: `../literature/2023-niemeijer-jmirformres-mpath-sense-performance-study.pdf`

## Related profiles

- Platforms: [CARP Mobile Sensing](../../module-02-digital-phenotyping/profiles/carp-mobile-sensing.md), [m-Path](../../module-02-digital-phenotyping/profiles/m-path.md)
- Contradictory OS-yield direction: [`aware-chemotherapy-engagement.md`](aware-chemotherapy-engagement.md)
- OS background limits and heartbeat mitigation: [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
- Vendor/OS policy erosion of call and SMS streams: [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md), [`mindlamp-relapse-3site.md`](mindlamp-relapse-3site.md)
- Configuration dominating data loss: [`empatica-epilepsy-data-quality.md`](empatica-epilepsy-data-quality.md)
- Other m-Path deployments: [`mpath-avatar2-esm-engagement.md`](mpath-avatar2-esm-engagement.md), [`mpath-nssi-ema-benefits-challenges.md`](mpath-nssi-ema-benefits-challenges.md)

## Sources

1. Niemeijer K, Mestdagh M, Verdonck S, Meers K, Kuppens P. *JMIR Form Res* 2023;7:e43296. DOI 10.2196/43296. Full text read from Europe PMC (PMC10031448), 2026-09-01. Establishes every figure in this profile, and establishes that m-Path Sense is built on CARP Mobile Sensing.
