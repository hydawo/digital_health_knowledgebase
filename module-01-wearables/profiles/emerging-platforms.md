# Emerging and Specialist Platforms

Platforms that materially belong in the Module 1 comparison but did not warrant a full profile in
this pass, either because they are narrower in scope, or because public documentation is too thin
to fill the template honestly. Each entry states what was established and what was not.

**Last verified: 2026-08-21; RingConn, Circular and Amazfit / Zepp section added 2026-10-09; Ultrahuman access, Biostrap (now Sensor Bio), Verily status and Zepp research partnerships re-checked 2026-10-10.** These entries close the discovery gap recorded in the first pass.

---

## Ultrahuman (Ring Air), the second ring with raw data

| Field | Detail | Confidence |
|---|---|---|
| Organization | Ultrahuman (India / UAE) |
| Product | Ultrahuman Ring AIR; **M1 CGM patch**; UltraSignal developer platform |
| **Raw data** | UltraSignal gives developers "the Ring AIR's Photoplethysmography (PPG), temperature and accelerometer data stream". The page says "data stream", not "raw"; format and rates are not documented | **Verified** for the wording (2026-10-10); raw-signal format **Unclear** |
| Developer platform | **UltraSignal**, described as "the world's first wearable-based developer platform" | **Verified** |
| Access | Two routes. **UltraSignal** (PPG, temperature, accelerometer stream): submit a short application for a Ring AIR developer kit; applications are reviewed with priority to apps using the ring's data, and selected developers are loaned a developer kit. **Partner API**: OAuth 2.0 for "approved apps" (client ID and secret issued at partner onboarding, base URL partner.ultrahuman.com, access tokens last about a week), returning derived ring metrics (sleep, movement, steps, heart rate, HRV, temperature, VO2 max, Recovery Index, Movement Index, Metabolic Score) and CGM metrics (glucose, average glucose, variability, HbA1c, time in target) by user consent and scope (`ring_data`, `cgm_data`, `profile`). No approval timeline, price or user cap is published. Corrected 2026-10-10: the current Partner API post does not describe a whitelist or token step | **Verified** (Ultrahuman blog, 19 September 2025, and UltraSignal page, read 2026-10-10) |
| Derived metrics | Recovery Score, Sleep Score, Movement Index, HRV, resting HR, skin temperature deviation, nightly SpO2 | **Reported** |
| Sampling rates | **Not documented** | **Unclear** |
| Pricing | Not disclosed | **Unclear** |
| Validation | **No independent PSG or ECG validation located** | **Unclear** |

**Why it matters.** Ultrahuman offers developers a PPG data stream from a ring. Oura's public API does
not. If a study needs finger-PPG data, for custom pulse-wave analysis, or because a ring is the only
form factor a population will tolerate overnight, Ultrahuman's UltraSignal is the only published ring
route found, though whether its stream is the raw waveform is not documented. (Note also that the
UltraSignal page title names Ring PRO while the body names Ring AIR.)

**Research program and academic data access.** No academic program is published. Academics use the
same two routes as companies: UltraSignal (loaned kit, selection-based, which implies small scale) for
the sensor stream, or the Partner API for derived metrics by participant consent. No retention,
AI-training or data-sharing terms were read; the Partner API documentation linked from the blog was
not opened. **Unclear.**

The **M1 CGM patch integration** makes Ultrahuman the only consumer ecosystem here combining ring
biometrics and continuous glucose in a single API. For metabolic research that is a genuinely
distinctive combination. **Reported.**

**Why to be cautious.** No independent validation was located, UltraSignal is selection-based with a
loaner-kit model that implies limited scale, sampling rates are undocumented, and pricing is unknown.
Treat as promising and unproven.

Links: https://www.ultrahuman.com/ultrasignal/ · https://www.ultrahuman.com/blog/accessing-the-ultrahuman-partnership-api/ · https://www.ultrahuman.com/us/partners/ · support@ultrahuman.com

---

## Biostrap (now Sensor Bio), consumer company that pivoted to research

| Field | Detail | Confidence |
|---|---|---|
| Organization | Biostrap, now trading as **Sensor Bio** (sensorbio.com). Biostrap's home and research pages carry a banner, "Biostrap is now Sensor Bio", and the research page's demo link goes to sensorbio.com/get-started | **Verified** (2026-10-10) |
| Products | Wrist biosensor; **Activity Pod** (leg-worn); armband and chest-strap HRMs; **Thermo Patch** (FDA-cleared continuous temperature, ±0.1 °C) | **Corroborated** |
| **Raw data** | "Biostrap provides access to raw and/or processed **PPG, gyroscope, and accelerometer** data to researchers via the RPM dashboard or custom data pipelines"; the home page offers "Continuous, raw physiological data including PPG and **IBI**". Sensor Bio's site: "Full access to raw PPG and derived physiological signals, timestamped and exportable" | **Verified** that the vendor states this (2026-10-10); a vendor claim, so the capability itself is **Corroborated** |
| **Configurable sampling** | Researchers can customise **device settings and sampling rates** | **Verified** |
| Study tooling | Customisable participant UX, enrolment workflows, **integrated behavioural health surveys**, educational widgets, automated reporting, compliance notifications | **Verified** |
| Integration | API or **Bluetooth SDKs** | **Reported** |
| Validation claims | "14 publications and 22 clinical studies"; partners named include NIHMD (COVID-19), Regeneron (neuromuscular disease), UNLV Athletics; a registered validation trial for ejection fraction and cardiac output (NCT05279066) | **Reported**, vendor-compiled counts |
| Pricing | Not public; demo booking via sensorbio.com/get-started. No academic program or pricing found | **Unclear** |
| Compliance claim | Research page: "Research Platform (HIPAA Compliant)"; home page: "HIPAA-compliant web platform" | Vendor statement, **Corroborated** at most |

**Why it matters.** Biostrap is one of the few platforms combining **raw PPG + configurable sampling
+ integrated surveys + a participant-management dashboard** in one product. That combination, signal access *and* study operations *and* EMA, is otherwise only approached by Samsung's Research
Stack and Labfront. Biostrap explicitly repositioned from consumer to medical/research, unveiling a
next-generation device with raw sensor data at HLTH as part of that shift. **Reported.**

The multi-device framework (wrist + leg pod + chest strap + temperature patch) is also unusual: leg
placement for gait, balance and jump metrics is not available from any other vendor in this module.

**Research program and academic data access.** No separate academic program. Sensor Bio markets
"Raw data access, IRB-friendly workflows, and reproducible signal quality for academic and research
studies", as a white-label platform with APIs. Access terms, user caps, retention and pricing are not
published; a demo is the only entry point. **Unclear** beyond the vendor's statements (2026-10-10).

**Why to be cautious.** Sampling rates undocumented (configurable per the research page, but no Hz figures), pricing opaque, the company has rebranded, validation counts are
vendor-compiled and the most recent registered trial located dates from 2022. Company scale is much
smaller than the majors, which is a continuity risk for multi-year studies.

Links: https://biostrap.com/research/ · https://biostrap.com/science/ · https://biostrap.com/validation/ · https://biostrap.com/rpm/ · https://sensorbio.com/ · https://sensorbio.com/get-started/

---

## Verily Study Watch, the clinical-research-only wearable

| Field | Detail | Confidence |
|---|---|---|
| Organization | Verily (Alphabet) |
| Status | In use across clinical trials since 2017. **Re-checked 2026-10-10: no current Study Watch product page found** (verily.com study-watch URLs return 404) and no 2026 Study Watch announcement found; Verily's 2026 research-wearable news concerns the Samsung Galaxy Watch instead | **Unclear** (2026-10-10; was "Active, not discontinued", Corroborated) |
| Availability | **Never sold for consumer use**, a clinical research tool only | **Corroborated** |
| **Data streams** | Records **ECG, heart rate, electrodermal activity (EDA), and inertial movement** | **Corroborated** |
| **Raw data** | Researchers can "analyse the raw data points that power digital biomarkers"; the device **stores weeks of raw data at a time** | **Corroborated** |
| Regulatory | FDA 510(k) clearances including **on-demand ECG** and **irregular pulse monitoring**. A bid to add a Parkinson's virtual motor exam was **rejected by FDA** | **Corroborated** |
| Platform | Verily **Pre** precision health platform; **Viewpoint Evidence** solution | **Corroborated** |
| Pricing / access | Not public; enterprise and pharma engagement | **Unclear** |

**Why it matters.** Study Watch records **EDA alongside ECG**. Empatica has EDA without ECG. Corrected
2026-10-10: Samsung Galaxy Watch8 and later also expose both through the Health Sensor SDK (raw EDA at
1 Hz and on-demand raw ECG at 500 Hz; see `samsung.md`). Multi-week
onboard raw storage plus FDA clearances places it alongside Empatica and Ametris in the
regulated-research tier.

### The March 2026 Verily, Samsung collaboration, significant for Module 1

Verily and Samsung Electronics America announced a collaboration bringing **Galaxy Watch 8** data
into Verily's **Pre** platform, with sensor data surfaced in **Viewpoint Evidence**. The partnership
gives researchers **access to raw device signals, photoplethysmography, and motion from the
accelerometers and gyroscopes**. **Corroborated** (Verily press release; MedCity News, March 2026).

This independently corroborates the Samsung raw-signal capability documented in `samsung.md`, and it
creates a **third access route** to Galaxy Watch raw data alongside the Samsung Health Sensor SDK (formerly the Privileged Health SDK) and the
open-source Research Stack, this one packaged for pharmaceutical clinical trials rather than
academic self-build.

**Why to be cautious for academic use.** There is no self-serve route. Verily sells to pharma and
large research organisations, pricing is unpublished, and the Study Watch has never been available
for purchase. An academic group cannot simply buy one.

Links: https://verily.com/ · https://verily.com/perspectives/verily-and-samsung-collaborate-to-accelerate-clinical-research-with-the-galaxy-watch-and-pre-platform · https://clinicaltrials.gov/study/NCT06041373

---

## RingConn, Circular and Amazfit / Zepp, data-access check (2026-10-09)

A desk check of primary sources for whether any of these offers researchers a data route beyond the consumer app. None publishes a research API. Zepp Health advertises research partnerships on its "Data analytics" page (zepp.com/data-analytics), citing "partnerships with 20 independent research laboratories, hospitals, pharmaceutical companies and universities" at the end of 2020 and 42 million active users in the first half of 2021, but states no data-access terms, application route or whether partners receive individual-level data (read 2026-10-10; corrected from "none publishes a research programme"). RingConn and Circular publish neither (as checked 2026-10-09; not rechecked 2026-10-10).

| Platform | What is documented | Research data access | Confidence |
|---|---|---|---|
| **RingConn** (Ninenovo) | Syncs to Health Connect on Android 9 and later since Google Fit sync ended on 1 October 2025 (RingConn blog, 7 August 2025). Company-run studies with Shanghai Jiao Tong University and hospitals, including a 2026 *npj Digital Medicine* paper on bilateral ring PPG, per a company press release. | No public developer API, SDK or research programme found. Researchers can read whatever RingConn writes to Health Connect (and reportedly Apple Health) through those OS stores, which means summary metrics, not raw PPG. A community reverse-engineered BLE project (OpenCircuit) exists and is not a supportable research route. | No API: **Reported** (absence of evidence on the vendor site and in search). Health Connect sync: **Verified**. Apple Health sync: **Unclear**, not confirmed on a RingConn page. |
| **Circular** (Circular Ring 2) | Consumer ring with ECG and FDA-cleared AFib detection per trade coverage. Companion app on iOS; the store listing names circular.xyz/help for support, and that page returned 403 to automated fetch. | No developer API, export documentation, OS health-store integration or research programme found on circular.xyz or in search. | **Unclear**. Needs Circular to confirm (support@circular.xyz). |
| **Amazfit / Zepp Health** | Zepp OS developer framework (docs.zepp.com) for on-watch Mini Programs. The device-app API exposes an `Accelerometer` (x, y, z in cm/s², from API level 3.0, with `FREQ_MODE_LOW`, `FREQ_MODE_NORMAL` and `FREQ_MODE_HIGH` and no Hz values published), a `Gyroscope` with the same pattern, `HeartRate` as bpm values plus a per-minute array for the current day, and `BloodOxygen` as SpO2 results. | No raw PPG in the documented API. Accelerometer and gyroscope can be read only by building and side-loading a watch app that runs while the study needs data. No cloud research API or research programme found; the developer.zepp.com landing page is a JavaScript shell with no retrievable text. Third-party aggregators offer normalised summaries: Terra lists "Activity, Daily and Sleep" data types for Zepp, "normalized by the Terra unified API", polled every 5 to 10 minutes because Zepp does not notify Terra of changes (tryterra.co/integrations/zepp, 2026-10-10). The Thryve Zepp integration page cited earlier now returns 404 (2026-10-10). Unofficial reverse-engineered cloud access exists and is not a supportable research route. | On-device sensor API: **Verified** from docs.zepp.com (rates still unpublished, rechecked 2026-10-10). No research cloud API: **Reported**. Accelerometer rate per mode: **Unclear**. Research partnerships: vendor page, figures from 2020 to 2021. |

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
   (a PPG stream from a ring, raw format undocumented), **Biostrap / Sensor Bio** (raw PPG and IBI with configurable rates, per the vendor), **Movesense** (512 Hz ECG,
   1.6 kHz IMU), **Verily** (ECG + EDA + inertial, weeks of onboard raw), and **Garmin** (raw accel
   via SDK, BBI via cloud API).
2. **A ring with a developer PPG stream now exists** (Ultrahuman UltraSignal). Oura's closed-data position is a vendor choice, not a
   constraint of the form factor.
3. **The raw-data tier is no longer synonymous with expensive.** Polar (~$95) and Movesense sit
   alongside Empatica (~$1,750/3 yr) and Ametris.
4. **Verily, Samsung means Galaxy Watch raw signal now has a commercial clinical-trial route**, not
   just a self-build one.

## Sources

See `../sources.md` entries S-EMG-01 through S-EMG-08, and S-EMG-09 through S-EMG-13 (added 2026-10-09).

Added 2026-10-10 (rows for `../sources.md` proposed to the coordinator):
- Ultrahuman, UltraSignal page. https://www.ultrahuman.com/ultrasignal/ (accessed 2026-10-10). **Primary.** PPG, temperature and accelerometer "data stream"; application and loaned developer kit.
- Ultrahuman blog, "Accessing the Ultrahuman Partnership API", 19 September 2025. https://www.ultrahuman.com/blog/accessing-the-ultrahuman-partnership-api/ (accessed 2026-10-10). **Primary.** OAuth 2.0 for approved apps, scopes and data list.
- Biostrap, home and research pages. https://biostrap.com/ ; https://biostrap.com/research/ (accessed 2026-10-10). **Primary.** "Biostrap is now Sensor Bio" banner; raw PPG and IBI; raw and/or processed PPG, gyroscope and accelerometer; HIPAA claim.
- Sensor Bio home page. https://sensorbio.com/ (accessed 2026-10-10). **Primary, vendor.** "Full access to raw PPG and derived physiological signals, timestamped and exportable".
- Zepp Health, Data analytics page. https://www.zepp.com/data-analytics (accessed 2026-10-10). **Primary, vendor.** Research partnerships (end-2020 figure).
- Terra, Zepp integration page. https://tryterra.co/integrations/zepp (accessed 2026-10-10). **Secondary (aggregator).** Activity, Daily and Sleep data types.
- Verily, study-watch URLs https://verily.com/solutions/study-watch and https://verily.com/perspectives/verily-study-watch (HTTP 404 on 2026-10-10).
