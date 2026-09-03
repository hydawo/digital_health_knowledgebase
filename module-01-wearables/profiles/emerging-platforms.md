# Emerging and Specialist Platforms

Platforms that materially belong in the Module 1 comparison but did not warrant a full profile in
this pass, either because they are narrower in scope, or because public documentation is too thin
to fill the template honestly. Each entry states what was established and what was not.

**Last verified: 2026-08-21.** These entries close the discovery gap recorded in the first pass.

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

## Not investigated in this pass

Recorded so their absence remains a known gap rather than an implied judgement.

| Technology | Note |
|---|---|
| **RingConn, Circular, Samsung Galaxy Ring (as a distinct research target)** | Smart rings with no established research data pathway identified |
| **Amazfit / Zepp Health** | Significant install base outside the US; Zepp OS SDK and data access for research not assessed |
| **Whoop 5.0 vs 4.0** | Whether the Schyvens 2025 result on the 4.0 transfers to current hardware is unknown |
| **Activinsights / GENEActiv production status** | Whether the line remains in active supply |
| **Open Movement project maintenance** | Current status of OmGui and the AX firmware |
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

See `../sources.md` entries S-EMG-01 through S-EMG-08.
