# Emerging and Specialist Platforms

Platforms that materially belong in the Module 1 comparison but did not warrant a full profile in
this pass, either because they are narrower in scope, or because public documentation is too thin
to fill the template honestly. Each entry states what was established and what was not.

**Last verified: 2026-08-21; RingConn, Circular and Amazfit / Zepp section added 2026-10-09.** These entries close the discovery gap recorded in the first pass.

---

## Ultrahuman (Ring Air), the second ring with raw data

| Field | Detail | Confidence |
|---|---|---|
| Organization | Ultrahuman (India / UAE) |
| Product | Ultrahuman Ring AIR; **M1 CGM patch**; UltraSignal developer platform |
| **Raw data** | **Raw PPG, accelerometer, and temperature** exposed to developers | **Corroborated** |
| Developer platform | **UltraSignal**, described as "the world's first wearable-based developer platform" | **Verified** |
| Access | Apply for a **loaned developer kit**; applications reviewed, priority to projects leveraging Ring AIR capabilities. The Partner API is **whitelist-only**, requiring a token from partner.ultrahuman.com; approval at Ultrahuman's discretion, taking several days | **Corroborated** |
| Derived metrics | Recovery Score, Sleep Score, Movement Index, HRV, resting HR, skin temperature deviation, nightly SpO2 | **Reported** |
| Sampling rates | **Not documented** | **Unclear** |
| Pricing | Not disclosed | **Unclear** |
| Validation | **No independent PSG or ECG validation located** | **Unclear** |

**Why it matters.** Ultrahuman exposes raw PPG from a ring. Oura does not, at any price. If a study
needs finger-PPG waveform data, for custom pulse-wave analysis, or because a ring is the only form
factor a population will tolerate overnight, **Ultrahuman is currently the only route**.

The **M1 CGM patch integration** makes Ultrahuman the only consumer ecosystem here combining ring
biometrics and continuous glucose in a single API. For metabolic research that is a genuinely
distinctive combination. **Reported.**

**Why to be cautious.** No independent validation was located, the developer programme is
discretionary and whitelist-based with a loaner-kit model that implies limited scale, sampling rates
are undocumented, and pricing is unknown. Treat as promising and unproven.

Links: https://www.ultrahuman.com/ultrasignal/ · https://www.ultrahuman.com/blog/accessing-the-ultrahuman-partnership-api/ · https://www.ultrahuman.com/us/partners/ · support@ultrahuman.com

---

## Biostrap, consumer company that pivoted to research

| Field | Detail | Confidence |
|---|---|---|
| Organization | Biostrap |
| Products | Wrist biosensor; **Activity Pod** (leg-worn); armband and chest-strap HRMs; **Thermo Patch** (FDA-cleared continuous temperature, ±0.1 °C) | **Corroborated** |
| **Raw data** | "Access to raw and/or processed **PPG, gyroscope, and accelerometer** data" via the RPM dashboard or custom pipelines. Biostrap states it deliberately keeps PPG waveform data in its raw state | **Corroborated** |
| **Configurable sampling** | Researchers can customise **device settings and sampling rates** | **Verified** |
| Study tooling | Customisable participant UX, enrolment workflows, **integrated behavioural health surveys**, educational widgets, automated reporting, compliance notifications | **Verified** |
| Integration | API or **Bluetooth SDKs** | **Reported** |
| Validation claims | "14 publications and 22 clinical studies"; partners named include NIHMD (COVID-19), Regeneron (neuromuscular disease), UNLV Athletics; a registered validation trial for ejection fraction and cardiac output (NCT05279066) | **Reported**, vendor-compiled counts |
| Pricing | Not public; "Book a Meeting" | **Unclear** |

**Why it matters.** Biostrap is one of the few platforms combining **raw PPG + configurable sampling
+ integrated surveys + a participant-management dashboard** in one product. That combination, signal access *and* study operations *and* EMA, is otherwise only approached by Samsung's Research
Stack and Labfront. Biostrap explicitly repositioned from consumer to medical/research, unveiling a
next-generation device with raw sensor data at HLTH as part of that shift. **Reported.**

The multi-device framework (wrist + leg pod + chest strap + temperature patch) is also unusual: leg
placement for gait, balance and jump metrics is not available from any other vendor in this module.

**Why to be cautious.** Sampling rates undocumented, pricing opaque, validation counts are
vendor-compiled and the most recent registered trial located dates from 2022. Company scale is much
smaller than the majors, which is a continuity risk for multi-year studies.

Links: https://biostrap.com/research/ · https://biostrap.com/science/ · https://biostrap.com/validation/ · https://biostrap.com/rpm/

---

## Verily Study Watch, the clinical-research-only wearable

| Field | Detail | Confidence |
|---|---|---|
| Organization | Verily (Alphabet) |
| Status | **Active, not discontinued.** In use across multiple clinical trials since 2017 | **Corroborated** |
| Availability | **Never sold for consumer use**, a clinical research tool only | **Corroborated** |
| **Data streams** | Records **ECG, heart rate, electrodermal activity (EDA), and inertial movement** | **Corroborated** |
| **Raw data** | Researchers can "analyse the raw data points that power digital biomarkers"; the device **stores weeks of raw data at a time** | **Corroborated** |
| Regulatory | FDA 510(k) clearances including **on-demand ECG** and **irregular pulse monitoring**. A bid to add a Parkinson's virtual motor exam was **rejected by FDA** | **Corroborated** |
| Platform | Verily **Pre** precision health platform; **Viewpoint Evidence** solution | **Corroborated** |
| Pricing / access | Not public; enterprise and pharma engagement | **Unclear** |

**Why it matters.** Study Watch is one of only two devices in this whole module offering **EDA
alongside ECG** (the other is nothing, Empatica has EDA without ECG; Verily has both). Multi-week
onboard raw storage plus FDA clearances places it alongside Empatica and Ametris in the
regulated-research tier.

### The March 2026 Verily, Samsung collaboration, significant for Module 1

Verily and Samsung Electronics America announced a collaboration bringing **Galaxy Watch 8** data
into Verily's **Pre** platform, with sensor data surfaced in **Viewpoint Evidence**. The partnership
gives researchers **access to raw device signals, photoplethysmography, and motion from the
accelerometers and gyroscopes**. **Corroborated** (Verily press release; MedCity News, March 2026).

This independently corroborates the Samsung raw-signal capability documented in `samsung.md`, and it
creates a **third access route** to Galaxy Watch raw data alongside the Privileged Health SDK and the
open-source Research Stack, this one packaged for pharmaceutical clinical trials rather than
academic self-build.

**Why to be cautious for academic use.** There is no self-serve route. Verily sells to pharma and
large research organisations, pricing is unpublished, and the Study Watch has never been available
for purchase. An academic group cannot simply buy one.

Links: https://verily.com/ · https://verily.com/perspectives/verily-and-samsung-collaborate-to-accelerate-clinical-research-with-the-galaxy-watch-and-pre-platform · https://clinicaltrials.gov/study/NCT06041373

---

## RingConn, Circular and Amazfit / Zepp, data-access check (2026-10-09)

A desk check of primary sources for whether any of these offers researchers a data route beyond the consumer app. None publishes a research API or research programme.

| Platform | What is documented | Research data access | Confidence |
|---|---|---|---|
| **RingConn** (Ninenovo) | Syncs to Health Connect on Android 9 and later since Google Fit sync ended on 1 October 2025 (RingConn blog, 7 August 2025). Company-run studies with Shanghai Jiao Tong University and hospitals, including a 2026 *npj Digital Medicine* paper on bilateral ring PPG, per a company press release. | No public developer API, SDK or research programme found. Researchers can read whatever RingConn writes to Health Connect (and reportedly Apple Health) through those OS stores, which means summary metrics, not raw PPG. A community reverse-engineered BLE project (OpenCircuit) exists and is not a supportable research route. | No API: **Reported** (absence of evidence on the vendor site and in search). Health Connect sync: **Verified**. Apple Health sync: **Unclear**, not confirmed on a RingConn page. |
| **Circular** (Circular Ring 2) | Consumer ring with ECG and FDA-cleared AFib detection per trade coverage. Companion app on iOS; the store listing names circular.xyz/help for support, and that page returned 403 to automated fetch. | No developer API, export documentation, OS health-store integration or research programme found on circular.xyz or in search. | **Unclear**. Needs Circular to confirm (support@circular.xyz). |
| **Amazfit / Zepp Health** | Zepp OS developer framework (docs.zepp.com) for on-watch Mini Programs. The device-app API exposes an `Accelerometer` (x, y, z in cm/s², from API level 3.0, with `FREQ_MODE_LOW`, `FREQ_MODE_NORMAL` and `FREQ_MODE_HIGH` and no Hz values published), a `Gyroscope` with the same pattern, `HeartRate` as bpm values plus a per-minute array for the current day, and `BloodOxygen` as SpO2 results. | No raw PPG in the documented API. Accelerometer and gyroscope can be read only by building and side-loading a watch app that runs while the study needs data. No cloud research API or research programme found; the developer.zepp.com landing page is a JavaScript shell with no retrievable text. Third-party aggregators (Terra, Thryve) offer normalised summaries of daily activity, sleep and heart rate. Unofficial reverse-engineered cloud access exists and is not a supportable research route. | On-device sensor API: **Verified** from docs.zepp.com. No research cloud API: **Reported**. Accelerometer rate per mode: **Unclear**. |

**Bottom line.** None of the three is a research-access platform in the sense Ultrahuman (UltraSignal) or Samsung (Health Sensor SDK) now are. For a study that wants their data, the realistic routes are OS health stores (Health Connect, Apple Health) or an aggregator, at summary-metric resolution. Zepp OS is the only one with a documented on-device route to motion sensors, and that requires building a watch app. Only the vendors can confirm whether an unpublished partner or research arrangement exists.

---

## Not investigated in this pass

Recorded so their absence remains a known gap rather than an implied judgement.

| Technology | Note |
|---|---|
| **Samsung Galaxy Ring (as a distinct research target)** | Smart ring with no separate research data pathway assessed beyond the Samsung profile. RingConn and Circular were checked on 2026-10-09; see the section above |
| **Whoop 5.0 vs 4.0** | Whether the Schyvens 2025 result on the 4.0 transfers to current hardware is unknown |
| **Activinsights / GENEActiv production status** | Checked 2026-10-09: still sold by quote, product page republished January 2026, no discontinuation notice. Manufacturing status and lead times not public. See `axivity-geneactiv.md` |
| **Open Movement project maintenance** | Checked 2026-10-09: repository active (last push 2026-08-18), OmGui last released 2022-10-31 (v45), AX3 firmware V50, AX6 firmware V56. See `axivity-geneactiv.md` |
| **Muse, Dreem and EEG wearables** | Deliberately deferred as a distinct modality |
| **Dexcom, Abbott and CGM generally** | Deliberately deferred to a connected-medical-devices module. Note that both Labfront and Ultrahuman now integrate CGM with wearables, so this boundary is eroding |

---

## Where these platforms change the Module 1 conclusions

1. **"Only Samsung, Polar, Withings and Empatica expose raw signal" was wrong.** Add **Ultrahuman**
   (raw PPG from a ring), **Biostrap** (raw PPG with configurable rates), **Movesense** (512 Hz ECG,
   1.6 kHz IMU), **Verily** (ECG + EDA + inertial, weeks of onboard raw), and **Garmin** (raw accel
   via SDK, BBI via cloud API).
2. **A ring with raw PPG now exists.** Oura's closed-data position is a vendor choice, not a
   constraint of the form factor.
3. **The raw-data tier is no longer synonymous with expensive.** Polar (~$95) and Movesense sit
   alongside Empatica (~$1,750/3 yr) and Ametris.
4. **Verily, Samsung means Galaxy Watch raw signal now has a commercial clinical-trial route**, not
   just a self-build one.

## Sources

See `../sources.md` entries S-EMG-01 through S-EMG-08, and S-EMG-09 through S-EMG-13 (added 2026-10-09).
