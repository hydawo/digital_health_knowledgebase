# Module 1 — Validation Evidence

Full extraction from the primary validation literature, read in full rather than summarized.
**Last verified: 2026-08-21.**

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

## 3. Can Oura and WHOOP be compared? A bridged estimate

They have **never been tested under the same protocol.** Robbins 2024 excluded WHOOP; Schyvens 2025
excluded Oura. Both vendors market a "most accurate" claim from the study that excluded the other.

However, **Apple Watch Series 8 and the Fitbit Sense line appear in both studies**, which permits a
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

**It is an estimate, not a result.** A head-to-head Oura vs WHOOP PSG study remains the single
highest-value missing piece of evidence in this module.

**What can be said without inference:** WHOOP 4.0 had the best *deep-sleep classification accuracy*
of the six devices Schyvens tested (69.63%) while simultaneously having the second-worst *overall*
agreement (κ=0.37). Those are compatible — a device that over-assigns deep sleep will catch most
true deep epochs while misclassifying much else. **Citing WHOOP's deep-sleep number without its
kappa is misleading, and the first draft of this knowledge base did exactly that.**

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

## 6. What the evidence base does not contain

| Gap | Consequence |
|---|---|
| No Oura vs WHOOP head-to-head | Both "most accurate" claims are unfalsifiable as stated |
| Samsung absent from every major multi-device PSG comparison | The platform with the best raw-data access has the weakest validation record |
| Empatica absent from consumer head-to-heads | Cannot compare EmbracePlus sleep detection to Oura/WHOOP |
| Skin tone not systematically recorded in either PSG study | PPG performance across skin tones is a known physical concern and remains unquantified here |
| All PSG validations are single-night, laboratory, 8-hour windows | Systematically overestimates real-world agreement, by the authors' own admission |
| Current-generation hardware untested | Oura Ring 5 (June 2026), WHOOP 5.0/MG, Apple Series 11, Fitbit Air all postdate every study above |
| No validation of Oura Health Radar, Samsung Antioxidant Index, Apple hypertension notifications, or WHOOP Blood Pressure Insights located | The newest and most clinically consequential features are the least evidenced |

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
