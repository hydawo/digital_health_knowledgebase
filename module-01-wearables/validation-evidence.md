# Module 1 — Validation Evidence

Full extraction from the primary validation literature, read in full rather than summarized.
**Last verified: 2026-08-21.** Sections 3, 6b and 6c updated 2026-10-09 (open-questions pass).

This file exists because the summary figures circulating about wearable sleep accuracy — including
the ones in the first draft of this knowledge base — are systematically misleading. Reading the
papers changes the conclusions.

---

## 1. Schyvens et al. 2025, *SLEEP Advances* 6(2):zpaf021 — six devices vs PSG

**Design.** Laboratory validation, Antwerp University Hospital, April 2023–August 2024.
**N = 62 adults** (52 male, 10 female; mean age 46.0 ± 12.6). Single-night PSG; each participant
wore 2–4 wearables simultaneously on both wrists. AASM scoring, 30-second epochs, epoch-by-epoch
comparison over the 8-hour lights-out period. **Funded by Flanders Innovation & Entrepreneurship
(VLAIO HBC.2021.0387); authors declare no conflicts.** **Verified** — full text read.

**Devices:** Fitbit Charge 5, Fitbit Sense, Withings ScanWatch, Garmin Vivosmart 4, Whoop 4.0,
Apple Watch Series 8.

### Overall agreement — Cohen's kappa (the headline result)

| Rank | Device | κ | Interpretation |
|---|---|---|---|
| 1 | **Apple Watch Series 8** | **0.53** | Moderate |
| 2 | Fitbit Sense | 0.42 | Moderate |
| 3 | Fitbit Charge 5 | 0.41 | Moderate |
| 4 | Whoop 4.0 | 0.37 | Fair |
| 5 | Withings ScanWatch | 0.22 | Fair |
| 6 | Garmin Vivosmart 4 | 0.21 | Fair |

### Sleep/wake detection

| Device | Sensitivity (%) | Specificity (%) |
|---|---|---|
| Apple Watch Series 8 | 96.27 ± 4.57 | 52.15 ± 21.25 |
| Garmin Vivosmart 4 | 95.92 ± 6.10 | 29.39 ± 26.38 |
| Withings ScanWatch | 94.32 ± 10.94 | 31.09 ± 20.12 |
| Whoop 4.0 | 93.58 ± 9.42 | 40.13 ± 23.55 |
| Fitbit Sense | 93.33 ± 3.85 | 48.80 ± 20.67 |
| Fitbit Charge 5 | 91.68 ± 7.28 | 47.51 ± 17.37 |

**The universal pattern: high sensitivity, poor specificity.** Every device detects sleep well and
detects *wake* badly. Specificity ranges 29–52%. A device that calls almost everything sleep scores
well on sensitivity and is useless for quantifying fragmentation.

### Per-stage accuracy (% of PSG epochs correctly classified)

| Device | Wake | Light | Deep | REM |
|---|---|---|---|---|
| Apple Watch Series 8 | 52.15 | **83.27** | 50.66 | **68.57** |
| Fitbit Sense | 48.80 | 73.30 | 50.86 | 61.29 |
| Fitbit Charge 5 | 47.67 | 72.42 | 51.50 | 59.96 |
| Whoop 4.0 | 40.13 | 61.99 | **69.63** | 61.99 |
| Withings ScanWatch | 31.09 | 53.04 | 66.74 † | n/a † |
| Garmin Vivosmart 4 | 27.64 | 60.33 | 47.46 | 33.10 |

† ScanWatch uses **three-state classification, combining REM and N3 into a single "deep sleep"
category**. Its 66.74% "deep" figure is therefore not comparable to the four-state devices, and it
overestimated that combined category by **+73.20 minutes (p<0.001)**.

### Bias vs PSG

| Device | n | TST bias (min) | SE bias (%) | WASO bias (min) | SOL bias (min) |
|---|---|---|---|---|---|
| Fitbit Sense | 37 | +6.31 (ns) | +2.20 * | −12.38 * | −4.35 (ns) |
| Fitbit Charge 5 | 39 | +11.12 (ns, p=0.051) | +3.39 * | −16.86 * | +6.56 (ns) |
| Apple Watch Series 8 | 20 | +19.60 ** | +4.44 ** | −21.23 ** | +1.88 (ns) |
| Whoop 4.0 | 40 | +24.46 * | +4.10 ** | −19.15 ** | −10.95 ** |
| Garmin Vivosmart 4 | 25 | +38.44 ** | +8.17 *** | −38.34 *** | +2.84 (ns) |
| Withings ScanWatch | 41 | +39.87 *** | +10.19 *** | −47.94 *** | +6.59 (ns) |

\* p<0.05 · \*\* p<0.01 · \*\*\* p<0.001 · ns = not significant

**Every device underestimated WASO**, by 12 to 48 minutes. If your endpoint is sleep fragmentation
or nocturnal awakenings, consumer wearables will systematically flatter your participants.

### Data loss — an underreported operational finding

| Device | Failures / attempts |
|---|---|
| Garmin Vivosmart 4 | **18 / 43** |
| Apple Watch Series 8 | **15 / 35** |
| Withings ScanWatch | 0 / 41 |

Cause unknown; no device malfunction detected. **Verified.** In a supervised laboratory setting
with expert operators, the Garmin and Apple devices failed to produce usable sleep data on roughly
40% of nights. Any power calculation for a free-living study should assume worse.

### Authors' conclusion

Devices with higher kappa — Apple Watch Series 8 (0.53), Fitbit Sense (0.42), Fitbit Charge 5
(0.41) — "could be effectively used to track prolonged and significant changes in sleep
architecture," but the devices "currently do not serve as replacements for PSG in clinical
diagnoses."

### Limitations named by the authors

Single night per participant; 8-hour lights-out window only (not real-world 24h use); sample
heavily male (52/62); **skin tone and race/ethnicity not systematically collected — a significant
omission for PPG validation**; age clustered around 46; mixed healthy/suspected-apnea sample with
subgroups too small (n=2–27) to stratify; proprietary algorithms updated periodically, so results
are not reproducible across firmware versions.

---

## 2. Robbins et al. 2024, *Sensors* 24(20):6532 — three devices vs PSG

**Design.** Single-night inpatient validation, Brigham and Women's Hospital. **N = 35 healthy
adults** (ages 20–50; 57% female; 57% White, 23% Asian, 9% Black/African American). Eligibility:
6–9 h habitual sleep, BMI 18.5–29.9, screened negative for sleep disorders. 8-hour scheduled sleep
opportunity, PSG with 6-channel EEG, EOG, ECG, chin EMG; AASM scoring in 30-second epochs.
**Verified** — full text read.

**Devices:** Oura Ring Gen3 (non-dominant index finger), Fitbit Sense 2 (wrist), Apple Watch
Series 8 (wrist).

### ⚠️ Funding and conflicts — read before citing

> **Funded by Oura Ring Inc.** The lead author serves on Oura's Medical Advisory Board and receives
> consulting fees from Oura. Co-authors report extensive industry consulting including sleep-related
> companies.

**Verified from the paper's own disclosures.** This does not invalidate the results — the protocol
is sound and it is peer-reviewed — but a vendor-funded study whose lead author sits on that vendor's
advisory board, and which concludes that vendor's product is the most accurate, is a *Corroborated*
finding with a declared interest, not an independent one. It should never be cited without the
disclosure attached.

### Per-stage sensitivity and precision

| Device | | Light | Deep | REM |
|---|---|---|---|---|
| **Oura Ring Gen3** (n=35) | Sensitivity | 78.2% | **79.5%** | 76.0% |
| | Precision | 79.5% | 77.0% | 79.1% |
| **Fitbit Sense 2** (n=33) | Sensitivity | 78.0% | 61.7% | 67.3% |
| | Precision | 72.8% | 73.2% | 73.1% |
| **Apple Watch Series 8** (n=29) | Sensitivity | 86.1% | 50.5% | 82.6% |
| | Precision | 72.7% | 87.8% | 77.7% |

### Agreement

| Device | Sleep–wake κ | Four-stage κ |
|---|---|---|
| Oura Ring Gen3 | 0.60 | **0.65** |
| Apple Watch Series 8 | 0.60 | 0.60 |
| Fitbit Sense 2 | 0.52 | 0.55 |

### Bias

| Device | Notable biases |
|---|---|
| Oura | TST +9 min (ns); SE and WASO not significantly different from PSG |
| Fitbit Sense 2 | Light +18 min (p<0.001); Deep −15 min (p<0.001); WASO +3 min (ns) |
| Apple Watch S8 | Light **+45 min** (p<0.001); Deep **−43 min** (p<0.001); WASO −10 min (p=0.02); Wake −7 min (p<0.01) |

### Intraclass correlation coefficients — the finding that gets ignored

| Measure | Oura | Fitbit | Apple |
|---|---|---|---|
| Total Sleep Time | 0.74 | 0.56 | 0.85 |
| Sleep Efficiency | 0.74 | 0.56 | 0.85 |
| Light Sleep | 0.40 | 0.52 | 0.37 |
| **Deep Sleep** | **0.32** | **0.36** | **0.13** |
| **REM Sleep** | **0.27** | **0.13** | **0.37** |

**This is the single most important table in the sleep-validation literature for research planning.**
Even the best-performing device has *poor* ICC for deep sleep (0.32) and REM (0.27). Epoch-level
agreement statistics look respectable; between-person reliability of the stage summaries does not.

A study using nightly deep-sleep minutes or REM minutes as an outcome is, on this evidence, largely
measuring device noise. Total sleep time and sleep efficiency are the only stage-derived measures
with good-to-excellent ICC on any device.

### Device failures

Fitbit 2/35, Apple Watch 6/35 recorded no data despite proper initialization. **Verified.**

### Limitations named by the authors

Single night; healthy participants only; scheduled 8-hour window "overestimates concordance"
relative to 24-hour real-world use; black-box algorithms with no raw sensor data or algorithm
transparency, limiting reproducibility; results do not extend to other brands or models.

---

## 3. Can Oura and WHOOP be compared?

**Corrected 2026-08-24, and again 2026-10-09.** A companion research pass (`research-library-wearables.md`) found a direct
head-to-head this file previously said did not exist. The 2026-10-09 pass then found two PSG studies that
include both devices (§3c), on older hardware. That claim is retired below; a bridged
estimate is retained only for the specific outcome — PSG-scored sleep-stage kappa — that still has
no direct comparison.

### 3a. Resting HR and HRV — a genuine head-to-head now exists

**Dial MB, Hollander ME, Vatne EA, Emerson AM, Edwards NA, Hagen JA. 2025.** "Validation of
nocturnal resting heart rate and heart rate variability in consumer wearables." *Physiological
Reports* 13(16):e70527. Ohio State University Human Performance Collaborative / Air Force Research
Laboratory, Wright-Patterson AFB.

**Design.** 13 adults (6 female), **536 nights**, an ECG chest-strap reference, with **Garmin
Fenix 6, Oura Gen3, Oura Gen4, Polar Grit X Pro, and WHOOP 4.0 worn simultaneously** by the same
participants on the same nights. This is the first located study placing Oura and WHOOP under one
protocol against a shared reference.

| Device | Resting HR — CCC | Resting HR — MAPE |
|---|---|---|
| **Oura Gen4** | **0.98** | 1.94% ± 2.51% |
| **Oura Gen3** | **0.97** | 1.67% ± 1.54% |
| WHOOP 4.0 | 0.91 ("moderate") | 3.00% ± 2.15% |
| Polar Grit X Pro | 0.86 ("poor") | 2.71% ± 2.75% |

| Device | HRV (RMSSD) — CCC | HRV — MAPE |
|---|---|---|
| **Oura Gen4** | **0.99** | 5.96% ± 5.12% |
| **Oura Gen3** | **0.97** | 7.15% ± 5.48% |
| WHOOP 4.0 | 0.94 | 8.17% ± 10.49% |
| Garmin Fenix 6 | 0.87 | 10.52% ± 8.63% |
| Polar Grit X Pro | 0.82 | 16.32% ± 24.39% |

Both Oura generations rank highest on HRV, WHOOP is next ("moderate" per the paper's CCC bands),
and Garmin/Polar trail. Garmin was excluded from the RHR analysis only (its RHR figure is a
rolling 30-minute window with no reportable timestamp, making night-to-night alignment with the
Polar H10 reference impossible) — it is included in the HRV analysis, where the underlying
comparison does not have that alignment problem.

> ✅ **Confidence: Verified.** Full text read directly from the local PDF
> (`literature/oura/2025-dial-physiologicalreports-nocturnal-rhr-hrv-validation.pdf`), resolving the
> prior 403/CAPTCHA block. **Funding disclosure confirmed:** "This study was financially supported by
> the Air Force Research Laboratory (AFRL)." **Conflict of interest confirmed:** "The authors declare
> that they have no competing interests." No wearable-vendor funding of any kind — this is an
> independent, government-funded validation with a clean COI statement, among the strongest-provenance
> studies in this file. Design: N=13 adults (7 male, 6 female), 536 nights, Polar H10 ECG chest strap
> as reference, Garmin Fenix 6 / Oura Gen 3 / Oura Gen 4 / Polar Grit X Pro / WHOOP 4.0 worn
> simultaneously. Both raw (CCC/MAPE) and Z-score-normalized (per-subject baseline) analyses were run
> and agree on device ranking.

**What this resolves and what it doesn't.** This closes the "no direct comparison at all" gap for
**resting heart rate and HRV**: Oura leads WHOOP on both, under a shared protocol, in a real
(if small, N=13) sample. It does **not** address PSG-scored sleep-stage classification — Dial et al.
did not use polysomnography, so §3b below still applies to that specific question.

### 3b. Sleep-stage kappa specifically: no PSG head-to-head on current hardware, bridged estimate retained

**Corrected 2026-10-09:** Robbins 2024 and Schyvens 2025 are not the only PSG studies. Miller et al.
2022 and Grandner et al. 2023 both put Oura and WHOOP under one PSG protocol (§3c), but on Oura
Gen2/V2 and WHOOP 3.0. For **Oura Gen3 or later against WHOOP 4.0 or later**, there is still no shared
protocol: Robbins 2024 excluded WHOOP; Schyvens 2025 excluded Oura. The indirect bridge below is retained for this narrower question
only — do not extend it to resting HR or HRV, where §3a above is now direct evidence rather than an
estimate.

**Apple Watch Series 8 and the Fitbit Sense line appear in both PSG studies**, which permits a
cautious indirect comparison anchored on the shared devices.

| Device | Robbins 2024 four-stage κ | Schyvens 2025 κ | Δ |
|---|---|---|---|
| Apple Watch Series 8 | 0.60 | 0.53 | −0.07 |
| Fitbit Sense / Sense 2 | 0.55 | 0.42 | −0.13 |

Schyvens' protocol yields systematically lower kappa (older, heavier, partly sleep-disordered
sample; more device-wearing simultaneously). Anchoring on Apple Watch as the bridge:

- **Oura Gen3** scored **κ +0.05 relative to Apple Watch** in Robbins.
- **Whoop 4.0** scored **κ −0.16 relative to Apple Watch** in Schyvens.

**Inference (labelled as such, not a finding):** on the available evidence, Oura's four-stage
agreement is probably somewhat *better* than Apple Watch's, and WHOOP's is probably meaningfully
*worse*. The gap between Oura and WHOOP is likely substantial, in Oura's favour — but this is a
two-device bridge across studies with different populations and different hardware generations
(Oura Gen3, not Ring 4/5; Whoop 4.0, not 5.0), and Robbins was Oura-funded.

**It is an estimate, not a result.** A head-to-head Oura vs WHOOP **PSG sleep-stage** study on current
hardware remains the single highest-value missing piece of evidence in this module. The one direct
older-generation comparison (Miller 2022, §3c) found the two tied on four-stage kappa, which is a
reason to hold the bridged "Oura well ahead" inference loosely. (Resting HR and HRV, the other
outcome this bridge used to stand in for, now have direct evidence — see §3a.)

**What can be said without inference:** WHOOP 4.0 had the best *deep-sleep classification accuracy*
of the six devices Schyvens tested (69.63%) while simultaneously having the second-worst *overall*
agreement (κ=0.37). Those are compatible — a device that over-assigns deep sleep will catch most
true deep epochs while misclassifying much else. **Citing WHOOP's deep-sleep number without its
kappa is misleading, and the first draft of this knowledge base did exactly that.**

### 3c. PSG studies with Oura and WHOOP in the same protocol (added 2026-10-09)

Found by PubMed `(whoop[tiab]) AND (polysomnograph*[tiab])` (8 hits, date-sorted) and
`(oura[tiab]) AND (whoop[tiab])` (9 hits), checked 2026-10-09.

**Miller DJ, Sargent C, Roach GD. 2022.** "A Validation of Six Wearable Devices for Estimating Sleep,
Heart Rate and Heart Rate Variability in Healthy Adults." *Sensors* 22(16):6317,
doi:10.3390/s22166317. CQUniversity Appleton Institute. N=53 (26 F, age 25.4 ± 5.9), one lab night,
9 h in bed, PSG plus ECG, all six devices worn at once.

| Device | Two-state κ | Four-stage κ | Agreement | Deep sens. | REM sens. | Wake sens. | TST bias (min) |
|---|---|---|---|---|---|---|---|
| Somfit (5-state) | 0.48 | **0.52** | 65% | 65% | 58% | 57% | −5.5 |
| **WHOOP 3.0** | 0.44 | **0.44** | 60% | 62% | 66% | 56% | −12.2 |
| **Oura Gen2** | **0.51** | **0.43** | 61% | 62% | 52% | 57% | +1.5 |
| Polar Vantage V | 0.44 | 0.28 | 51% | 33% | 49% | 51% | −0.8 |
| Garmin FR245 | 0.35 | 0.25 | 50% | 28% | 50% | 27% | +43.8 |
| Apple Watch S6 (3-state) | 0.30 | 0.20 | 53% | n/a | n/a | 26% | +39.5 |

Heart rate and RMSSD against ECG (ICC): WHOOP 0.99 / 0.99, Apple 0.96 / 0.67, Polar 0.93 / 0.65, Oura
0.85 / 0.63, Somfit 0.65 / 0.69, Garmin 0.41 / 0.24. WHOOP's (and Somfit's) values come from R-R data
supplied by the vendor and compared over matched windows, so they are not processed the same way as
the app-reported values of the other devices.

> **Funding and COI, read directly:** "This study was funded by the Australian Institute of Sport."
> COI: the three authors "are members of a research group at Central Queensland University (i.e., The
> Sleep Lab) that receives support for research (i.e., funding, equipment) from WHOOP Inc. However,
> WHOOP was not involved in the design, conduct or reporting of this study." WHOOP staff, blinded to
> PSG, supplied WHOOP's 30-s epochs. **Verified** (full text read). Tier B for WHOOP by this KB's
> definition; for Oura it is a study run by a WHOOP-supported lab.

**Grandner MA, Bromberg Z, Hadley A, Morrell Z, Graf A, Hutchison S, Freckleton D. 2023.**
"Performance of a multisensor smart ring to evaluate sleep." *Sleep* 46(1):zsac152,
doi:10.1093/sleep/zsac152. Happy Ring development study; Oura V2, WHOOP 3.0, Fitbit Charge 4 and
Actiwatch 2 as comparators against one in-lab PSG night (and Dreem 2 at home). In the lab: sleep/wake
accuracy Oura 0.88 ± 0.05 (n=30), WHOOP 0.86 ± 0.05 (n=33); specificity 0.49 vs 0.54. Stage-level
results are in a supplement not read here. **Five of seven authors are Happy Health employees, and data
collection and analysis were done by the Happy Health team.** **Verified** (full text read via PMC).

**Reading.** On the only direct PSG comparison, WHOOP 3.0 and Oura Gen2 are effectively tied on
four-stage kappa (0.44 vs 0.43), with Oura better at wake/sleep and WHOOP better at REM. Both devices
and both algorithms have since been replaced, and the lab running the study is WHOOP-supported. This
does not settle the current-generation question, but it removes the claim that no comparison exists.

**Other independent Oura PSG data, for context.** Lee T et al. 2023 (*JMIR mHealth uHealth*
11:e50983, N=75, two Korean sleep centres, mean AHI 18; most authors employed by Asleep, a competing
sleep-app maker): four-stage κ Galaxy Watch 5 0.42, Fitbit Sense 2 0.42, Pixel Watch 0.40, **Oura Ring 3
0.35**, Apple Watch 8 0.30. Searles ME et al. 2026 (*SLEEP Advances* 7(1):zpag006, NIH-funded, no
financial disclosures): in older adults (n=19), Oura Gen3 underestimated TST by 75.5 min and
overestimated deep sleep by 71.5 min. Both **Verified** from the full text. Neither is Oura-funded, and
neither reproduces Robbins' ranking of Oura first.

---

## 4. Garmin Enhanced BBI — Garmin Health technical note, November 2023

**Verified** — the PDF was retrieved and read directly.

### What it is

Beat-to-Beat Intervals measured directly from the PPG sensor. Garmin distinguishes BBI (PPG-derived)
from RRI (ECG-derived R-wave to R-wave). Enhanced BBI uses a different signal-processing chain from
Garmin's legacy BBI, preserving signal bandwidth rather than heavily filtering it — the legacy
approach's filtering "limited the bandwidth with the consequence of sometimes affecting the accuracy
of higher frequency HRV markers such as RMSSD."

### The confidence flag — genuinely unusual

Every beat carries a binary confidence metric (1 = high, 0 = low). Garmin states this is
**"unique in the industry"**: the confidence is provided *per heartbeat*, not as an aggregated
statistic like RMSSD or SDNN where the device has already applied arbitrary outlier rejection. The
researcher performs their own outlier rejection and computes whatever HRV metrics they want.

Low confidence arises from three causes:
1. **Motion** — most common. Above a higher motion threshold the device declines to report a beat
   at all, leaving a gap in the series.
2. **Signal quality** — usually fit: optical sensor not seated against the skin, low perfusion, or
   the wearer lying on the limb and compressing the watch.
3. **Abnormally high HRV** — beats judged implausibly short or long. Garmin notes the tuning dataset
   included "many recordings of heart rhythms besides sinus rhythm, including atrial fibrillation
   and frequent PVCs."

Garmin explicitly warns the confidence flag "is not 100% specific, and sometimes marks accurate
beats with low confidence."

### Accuracy evidence — read the sample size

**N = 1.** One 56-year-old male, BMI 25.9, one night (22:06–05:56), Garmin Venu 2 Plus on the left
wrist versus a Firstbeat Bodyguard 2 ECG monitor.

| Metric | Value |
|---|---|
| Total beats | 26,248 |
| High-confidence beats | 24,468 (**93.13%**) |
| Mean error (RRI − BBI), high-confidence beats | **0.506 ms** |
| SD of error | **8.55 ms** |
| Mean RRI / BBI | 1078.6 ms / 1078.0 ms |
| SD RRI / BBI | 92.90 ms / 93.99 ms |
| Pearson r (high-confidence) | **0.975** |

**Assessment:** the agreement is genuinely excellent — sub-millisecond mean error against an ECG
reference is what you would want for HRV work. But this is a **single-subject, single-night
demonstration published by the manufacturer**, titled "An Example Night." It is a *Reported*
existence proof, not validation. Garmin's own framing is that Enhanced BBI "approaches the accuracy
of an ECG-based RRI measurement system."

### The constraint everyone misses

> "Garmin Enhanced BBI is measured during the user's **sleep interval**."

**Verified, from Garmin's own document.** Enhanced BBI is **not** a 24-hour beat-to-beat stream. It
is a nocturnal one, deliberately, because sleep is "a period of low motion and good blood
perfusion, which provides the best PPG signal." A study needing daytime or during-stressor
beat-to-beat data cannot use Enhanced BBI as delivered and must go to the Health SDK's real-time
streaming (or to a chest strap).

### Access

Available "to select partners via the Garmin Health Standard SDK **as well as through the Garmin
Health API**." **Verified.** This matters: BBI is not SDK-only, so a study can get beat-to-beat data
through the cloud API without building and maintaining a mobile app.

Devices require a **gen-4 optical sensor or higher**; Vivosmart 5 and Venu 3 are cited as common
research choices. Via Fitabase (since early 2025) participants install the standard Garmin Connect
app and authorize by OAuth — **no custom app, no chest strap, no side-loading**. **Verified**
(Fitabase knowledge base).

---

## 5. Cross-platform accuracy findings (steps, heart rate, energy expenditure)

From Fuller et al. 2020 (*JMIR mHealth uHealth* 8(9):e18694), Chevance et al. 2022 (10(4):e35626),
and a living umbrella review of systematic reviews. **Corroborated** — via search summaries of the
abstracts and results, not full-text reads.

| Measure | Finding |
|---|---|
| **Heart rate** | Mean bias ≈ ±3%. Broadly acceptable for most research |
| **Steps** | Mostly underestimated; MAPE −9% to +12%. Apple and Samsung highest validity; Apple, Fitbit and Garmin accurate roughly 50% of the time |
| **Energy expenditure** | Mean bias −3 kcal/min (−3%), error range −21.3% to +14.8%. **No brand fell within acceptable accuracy limits** |
| **Fitbit specifically** | Underestimates HR, EE and steps versus criterion; acceptable on average for steps and HR; **EE may be inaccurate for research purposes** |

**Standing conclusion: do not use consumer-wearable energy expenditure as a primary or secondary
endpoint on any platform.** This is the most robust cross-brand finding in the wearable literature
and it has not changed in six years.

---

## 6a. Funding transparency, applied symmetrically — new from the sponsorship-tiered library

**Added 2026-08-24**, from `research-library-wearables.md`, which tiers ~90 papers across Oura,
WHOOP, and Apple Watch by funding/authorship (A = vendor-employee, B = vendor-funded/independent
authors, C = fully independent), with a Verified/Corroborated/Unclear marker on every tier
assignment. Full detail lives in that file; the findings below are the ones that change how this
file's own claims should be read.

**The funding-disclosure treatment in this file was asymmetric, and that asymmetry has now been
corrected.** Robbins 2024's Oura funding and advisory-board conflict is flagged prominently above.
The equivalent fact about WHOOP and Apple was previously missing:

- **WHOOP's own most-cited early validation, Berryhill et al. 2020 (*J Clin Sleep Med* 16(5):775–783,
  University of Arizona), was directly grant-funded by WHOOP Inc.** — authors are not WHOOP
  employees and reported no personal conflicts, but the funding line is WHOOP's, the same pattern as
  Robbins/Oura. **Verified** (funding statement read directly). WHOOP's own marketing describes this
  study as independent confirmation, which is true of authorship but not of funding.
- **A separate CQUniversity author cluster (Miller, Bellenger, and colleagues) recurs across
  several WHOOP papers**, and one member (Dean Miller) holds a **WHOOP-sponsored research
  position at CQU**. The widely-marketed "99.7% HR / 99% HRV accuracy" figure (Bellenger et al. 2021,
  *Sensors*, funded by the Australian Institute of Sport — genuinely independent funding,
  **Verified**) is real, but the device tested was **WHOOP 2.0**, two hardware generations behind
  current WHOOP 5.0 — a caveat dropped in marketing use of that figure. Later papers from the same
  author cluster (Miller et al. 2020 *J Sports Sciences*; Bellenger et al. 2022 water polo HRV study)
  have not had their funding sections directly read and should not be assumed independent by
  default given the cluster's established sponsorship pattern.
- **Apple's own flagship validation — the Apple Heart Study (*NEJM* 2019, 419,297 participants) —
  was itself Apple-sponsored**, with named Apple co-authors and Stanford PIs disclosing grants/
  personal fees from Apple. **Verified** ("the study was sponsored by Apple," read directly). This
  is not disqualifying — it is large, rigorous, and peer-reviewed — but it is the same category of
  fact this file already flags for Robbins/Oura, and it was previously omitted here. **Apply the
  same disclosure standard to all three vendors' flagship studies, not only Oura's.**

**Oura's in-house sleep-staging paper is separately worth naming.** Kinnunen H, Altini M. 2021,
"The Promise of Sleep," *Sensors* 21(13):4302 — both authors Oura Health staff. This is Oura's own
algorithm-validation paper (Tier A / vendor-authored), distinct from Robbins 2024 (Tier B /
vendor-funded, independent authors). Neither should be read as independent evidence; they are two
different kinds of non-independent evidence and are sometimes conflated.

**A systematic review adds a field-wide caveat, not specific to Oura.** Gong et al. 2025,
*Diagnostics*/JMIR preprint (Korean government-funded, no industry funding, **Verified**, full text
read): of 107 studies on smart rings, **77 (72%) involved Oura specifically** — Oura dominates the
smart-ring evidence base by volume — but **65% of the 107 underlying studies had moderate-to-high
risk of bias**. That bias-risk figure applies to the field's methodology generally, not to Oura's
device performance specifically, but it is a material caveat on the weight any single study from
this literature should carry.

**Apple's validation record outside AFib is more mixed than a single "Apple Heart Study" citation
suggests.** From independently-funded studies (SFI-funded UCD/Insight Centre group, **Verified** on
both):
- **VO2max**: Apple Watch underestimated by ~6 mL/kg/min vs. indirect calorimetry (MAPE 13.31%),
  concluded "not sufficiently accurate to inform clinical decision-making" (Doherty et al. 2025,
  *PLOS ONE*, n=28).
- **HRV**: underestimated by 8.31 ms (MAPE 28.88%), **fails equivalence testing** against a Polar
  H10/Kubios reference, though resting HR itself showed excellent agreement (MAPE 5.91%) (Doherty
  et al. 2024, *Sensors* 24(19):6220, n=39, 316 measurements).
- **Fall detection**: in wheelchair users specifically, sensitivity was **4.7%** (14/300 fall trials
  detected) — starkly worse than Apple's general-population marketing framing (Abou et al. 2022,
  *Assistive Technology*, University of Illinois, n=25, funding not confirmed). A specific,
  actionable finding for any study involving mobility-impaired participants.
- **AFib detection** varies widely by population and method across independent studies: irregular-
  rhythm-notification sensitivity ranged from **21.4%** (Inocian et al. 2024, Philippines, n=140,
  Holter-referenced) to **72%** by-subject (Wasserlauf et al., AHA-funded, explicit "Apple was not
  involved" statement, n=30), while the on-demand ECG app itself performed much better
  (94.8% pooled sensitivity, Shahid et al. 2025 meta-analysis, **Unclear** confidence — funding not
  confirmed). **Irregular-rhythm notifications and the ECG app are different features with very
  different accuracy profiles and should not be conflated.**

None of this overturns the Apple Heart Study's core finding or displaces AFib detection as Apple's
strongest evidence asset. It does mean **"Apple's validation record" should not be read as uniformly
strong outside cardiac rhythm** — VO2max and HRV specifically have independent evidence of poor
accuracy, and fall detection has an independently-documented population-specific failure mode.

## 6b. What the evidence base does not contain

| Gap | Consequence |
|---|---|
| **No Oura vs WHOOP PSG sleep-stage head-to-head on current hardware** (resting HR/HRV head-to-head exists, §3a; older-generation PSG comparisons exist, §3c, added 2026-10-09) | Sleep-stage "most accurate" claims for Gen3+/4.0+ are still unfalsifiable as stated |
| **No independent (non-vendor-funded/authored) SpO2 validation for Oura or WHOOP**, on either device, at all (rechecked 2026-10-09, §6c) | Both devices market a wellness feature with no third-party accuracy evidence |
| **No independent skin/body-temperature validation for Oura or WHOOP**, on either device, at all (rechecked 2026-10-09, §6c) | Both devices build illness-detection and cycle-tracking features on unvalidated-by-third-parties sensing |
| ~~Samsung absent from every major multi-device PSG comparison~~ Corrected 2026-10-09: Galaxy Watch 5 is in Lee 2023 (κ 0.42, joint best wearable) and Galaxy Watch 2 in Byun 2023 (OSA patients); Samsung's newer derived metrics (Antioxidant Index, Vascular Load) still have no located validation (§6c) | Samsung's sleep and SpO2 evidence is thin and partly Samsung-funded; its newest metrics are unvalidated |
| Empatica absent from consumer head-to-heads; wrist EDA does not track palmar/finger EDA (§6c) | Cannot compare EmbracePlus sleep detection to Oura/WHOOP; E4 wrist EDA should not be treated as a substitute for palmar EDA |
| Skin tone not systematically recorded in either PSG study, nor in any consumer-device PSG validation located (searched 2026-10-09, §6c) | PPG performance across skin tones is a known physical concern and remains unquantified here |
| All PSG validations are single-night, laboratory, 8-hour windows | Systematically overestimates real-world agreement, by the authors' own admission |
| Current-generation hardware untested | Oura Ring 5 (June 2026), WHOOP 5.0/MG, Apple Series 11, Fitbit Air all postdate every study above. Rechecked 2026-10-09: Oura Gen4 has independent data only for resting HR/HRV (Dial 2025, no difference from Gen3); no WHOOP 5.0/MG or Oura Ring 5 validation located |
| No validation of Oura Health Radar, Samsung Antioxidant Index, or WHOOP Blood Pressure Insights located. Apple hypertension notifications: vendor validation only (white paper + FDA 510(k) K250507, sensitivity 41.2%), no peer-reviewed publication of the pivotal study (§6c) | The newest and most clinically consequential features are the least evidenced |

## 6c. Open-questions pass, 2026-10-09

Each item below records what was searched, so a later pass can tell a true gap from a search gap.
PubMed searches used E-utilities sorted by publication date; Europe PMC searches covered full text of
open-access papers and preprints.

**SpO2 and temperature for Oura and WHOOP: still no independent validation.** PubMed
`(oura[tiab] OR whoop[tiab]) AND (SpO2 OR "oxygen saturation" OR oximet* OR "blood oxygen")` returned
2 hits (a vascular-age paper and a ketogenic-diet trial), neither a validation. PubMed
`(oura OR whoop) AND temperature` returned 21 hits: association and prediction studies (TemPredict,
cycle tracking, sleep onset), most Oura-affiliated, none comparing the sensor with a reference
thermometer. Europe PMC full-text searches pairing Oura or WHOOP with reference oximeters (Masimo,
Nonin, arterial blood gas) or temperature references (iButton, thermometer) found none. For contrast,
wrist devices do have independent SpO2 work: Walzel et al. 2023 (*Sensors* 23(22):9164, Czech Technical
University grants, no conflicts) tested Apple Watch 8, Galaxy Watch 5 and Withings ScanWatch against a
Masimo Radical-7 during induced hypoxemia (N=18), and all three met the ISO ≤4% Arms limit; Jiang et al.
2026 (*JMIR Form Res* 10:e85253) found Apple Watch Series 7 Arms 5.82% below 88% SaO2 against arterial
blood gas. **Confidence: Corroborated** (searched, abstracts read; absence cannot be Verified).

**Skin tone in PSG validations: none located for an in-scope consumer device.** PubMed
`polysomnograph* AND (wearable* OR smartwatch* OR ring OR oura OR fitbit OR "apple watch") AND
(fitzpatrick OR "skin tone" OR "skin color" OR "skin pigmentation")` returned 3 hits, none a consumer
sleep tracker. Europe PMC full-text search of PSG studies mentioning Fitzpatrick or skin tone alongside
a consumer brand returned 27 hits; the in-scope ones say skin tone was not measured (Searles 2026: sample
"primarily White and, although not measured, fair-skinned"; Labie 2025, Fitbit Sense in knee OA: one
African American participant). Several report race or ethnicity instead (Robbins 2024, Grandner 2023,
Lee 2023 by centre only), which is not a proxy for skin tone. The nearest exception is outside the
module's device list: Nelson et al. 2025 (*J Sleep Res* 34(5):e70036, Verily-authored, N=41) ran an
exploratory skin-tone subgroup analysis of the Verily Numetric Watch against PSG. Apple's hypertension
510(k) reports a Fitzpatrick I-IV vs V-VI subgroup (sensitivity risk ratio 1.11, 95% CI 0.84 to 1.47),
but that study is not a PSG validation. Apple's October 2025 sleep-staging white paper reports
self-reported race and ethnicity, not Fitzpatrick type. **Confidence: Corroborated.**

**Apple hypertension notifications: the validation exists, but only as vendor documents.** The
pivotal study is described in Apple's white paper (September 2025) and the FDA 510(k) summary for
K250507 (cleared 11 September 2025). N=2,229 adults without diagnosed hypertension enrolled, 1,863 with
≥15 days of usable data, 30 days of wear against an FDA-cleared home cuff: sensitivity **41.2%** (95% CI
37.2 to 45.3), specificity **92.3%** (90.6 to 93.7); stage 2 sensitivity 53.7%. Lower sensitivity under
age 60 (risk ratio 0.69) and at BMI ≤30 (0.67). No peer-reviewed publication of the pivotal study was
found in PubMed or Europe PMC as of 2026-10-09. Independent commentary: Cohen JB et al. 2026,
*Hypertension* 83(2):e26031 (critique; notes the 510(k) predicate was an ECG-based cardiomyopathy
notifier and no ISO/IEEE cuffless protocol was used; two authors disclose Apple stock), and Cohen JB et
al. 2026, *JAMA* 335(11):1001 (population screening model, NIH/NHMRC funding). **Verified** (FDA
summary and Apple white paper read directly).

**Movesense: independent validation exists.** Rogers et al. 2022 (*Sensors* 22(5):2032, vs 12-lead
ECG, N=21) and Martín Gómez et al. 2024 (*Sensors* 24(17):5713, vs 3-lead ECG, N=21; R-peak
sensitivity 99.7%) for ECG; Martín Gómez et al. 2025 (*J Biomech* 190:112873, vs force plate, N=14) for
IMU step timing. Movesense supplied the sensors for both ECG studies; no vendor authors. Detail in
`profiles/movesense.md`. **Verified** (ECG papers' funding and COI read in the PDFs).

**Empatica wrist EDA vs palmar/finger EDA: poor agreement.** Menghini et al. 2019 (*Psychophysiology*
56(11):e13441, N=40, finger skin-conductance reference): wrist SC "showed neither correlation nor
visual resemblance with finger SC signal." Milstein and Gordon 2020 (*Front Behav Neurosci* 14:148,
N=30, MindWare reference): "The E4 failed to produce reliable EDA data." Hu et al. 2024 (*Behav Res
Methods* 56(7), N=67 lab, MindWare reference): ICC 0.09 for skin conductance level and 0.38 for SCR
count; valid EDA data about 41 to 43% of the time. EmbracePlus has only an exploratory comparison with
the E4 (Brandebusemeyer et al. 2026, *Sensors* 26(14):4376), not against a palmar reference.
**Corroborated** (abstracts; Milstein PDF stored).

**Samsung derived metrics.** Sleep: Lee T et al. 2023 (Galaxy Watch 5, four-stage κ 0.42, authors from
a competing app maker) and Byun et al. 2023 (*Chronobiol Int* 40(5):596, Galaxy Watch 2 in 127 OSA
patients, TST underestimated by 24.9 min, independent). Sleep apnea: Alavi et al. 2026 (*J Clin Sleep
Med* 22:150, Stanford, N=152, AUROC 0.94 for AHI ≥15; funding not stated in the abstract). SpO2: Browne
et al. 2024 (*J Clin Sleep Med* 20(9):1479, Galaxy Watch 4 vs PSG oximetry, RMSE 2.54%, Samsung research
grant) and Walzel 2023 (above). HR/HRV: Sarhaddi et al. 2022 (*PLoS One* 17(12):e0268361, Gear Sport,
independent). **Antioxidant Index and Vascular Load: nothing found** (PubMed `(samsung OR "galaxy
watch") AND (carotenoid* OR antioxidant* OR "vascular load" OR "arterial stiffness")`, and
`(wearable* OR smartwatch*) AND ("antioxidant index" OR "vascular load")`, 2026-10-09). Proposed text
for `profiles/samsung.md` is held by the agent that owns it. **Corroborated** (abstracts).

**Oura's research-page count.** `ouraring.com/science-and-research` read 2026-10-09 says
"130+ peer-reviewed publications" and "Powering research published in over 130 peer-reviewed
publications". Wayback Machine snapshots carry "over 130" from November 2025 through September 2026
and no count in July 2024, December 2024 or June 2025 snapshots. No "170+" figure was found on that page
in any snapshot checked. **Verified** (live page) / **Corroborated** (history).

---

## Sources

Schyvens et al. 2025: https://pmc.ncbi.nlm.nih.gov/articles/PMC12038347/ (also
https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472)
Robbins et al. 2024: https://pmc.ncbi.nlm.nih.gov/articles/PMC11511193/ (also
https://www.mdpi.com/1424-8220/24/20/6532)
Garmin Enhanced BBI: https://www8.garmin.com/garminhealth/news/Garmin-Enhanced-BBI_Final.pdf
Fitabase EBBI guide: https://fitabase.com/resources/knowledge-base/learn-about-garmin-data/collecting-enhanced-beat-to-beat-interval-data-using-garmin-devices/
Fuller et al. 2020: https://mhealth.jmir.org/2020/9/e18694/
Chevance et al. 2022: https://mhealth.jmir.org/2022/4/e35626
Umbrella review: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11560992/
Dial et al. 2025: https://physoc.onlinelibrary.wiley.com/doi/10.14814/phy2.70527
Gong et al. 2025: JMIR preprint #83508 / *Diagnostics* (MDPI)
Doherty et al. 2025 (VO2max): https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0323741
Doherty et al. 2024 (HRV): https://pmc.ncbi.nlm.nih.gov/articles/PMC11478500/
Abou et al. 2022 (wheelchair fall detection): https://www.tandfonline.com/doi/full/10.1080/10400435.2021.1923087
Miller et al. 2022 (six devices incl. Oura Gen2 and WHOOP 3.0 vs PSG): https://doi.org/10.3390/s22166317 (PMC9412437); PDF `literature/whoop/2022-miller-sensors-six-wearables-sleep-hr-hrv-validation.pdf`
Grandner et al. 2023 (Happy Ring, Oura V2, WHOOP 3.0 vs PSG): https://doi.org/10.1093/sleep/zsac152 (PMC13396806)
Lee T et al. 2023 (11 consumer sleep trackers vs PSG): https://doi.org/10.2196/50983 (PMC10654909)
Searles et al. 2026 (Oura Gen3, Fitbit Sense 2, nearables, older adults): https://doi.org/10.1093/sleepadvances/zpag006 (PMC12936866)
Walzel et al. 2023 (smartwatch SpO2 vs Masimo): https://doi.org/10.3390/s23229164; PDF `literature/apple-watch/2023-walzel-sensors-smartwatches-hypoxemia-reference-oximeter.pdf`
Jiang et al. 2026 (Apple Watch S7 SpO2 vs arterial blood gas): https://doi.org/10.2196/85253
Nelson et al. 2025 (Verily Numetric Watch vs PSG, skin-tone subgroup): https://doi.org/10.1111/jsr.70036
Apple hypertension white paper (Sept 2025): https://www.apple.com/health/pdf/Hypertension_Notifications_Validation_Paper_September_2025.pdf; PDF `literature/apple-watch/2025-apple-whitepaper-hypertension-notifications.pdf`
FDA 510(k) summary K250507: https://www.accessdata.fda.gov/cdrh_docs/pdf25/K250507.pdf
Cohen et al. 2026 (*Hypertension*): https://doi.org/10.1161/HYPERTENSIONAHA.125.26031 ; Cohen et al. 2026 (*JAMA*): https://doi.org/10.1001/jama.2025.26925
Movesense: https://doi.org/10.3390/s22052032 ; https://doi.org/10.3390/s24175713 ; https://doi.org/10.1016/j.jbiomech.2025.112873
Empatica EDA: Menghini 2019 https://doi.org/10.1111/psyp.13441 ; Milstein 2020 https://doi.org/10.3389/fnbeh.2020.00148 ; Hu 2024 https://doi.org/10.3758/s13428-024-02387-3 ; Brandebusemeyer 2026 https://doi.org/10.3390/s26144376
Samsung: Byun 2023 https://doi.org/10.1080/07420528.2023.2191720 ; Browne 2024 https://doi.org/10.5664/jcsm.11178 ; Alavi 2026 https://doi.org/10.1007/s44470-026-00159-8 ; Sarhaddi 2022 https://doi.org/10.1371/journal.pone.0268361
Oura research page: https://ouraring.com/science-and-research (read 2026-10-09)

**Full funding/COI tiering for ~90 papers across Oura, WHOOP, and Apple Watch** — including every
paper cited in §6a with its Verified/Corroborated/Unclear confidence marker — lives in
`research-library-wearables.md`, not duplicated here.
