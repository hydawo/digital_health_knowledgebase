# Polar

## Quick Facts

| Field | Details |
|---|---|
| Organization | Polar Electro Oy, Finland |
| Category | Sports/physiology sensor manufacturer; the closest thing to research-grade hardware sold at consumer prices |
| Current status | Active |
| Platforms/devices | Polar H10 / H9 chest straps, Verity Sense / OH1 optical armbands, Vantage and Grit X watch lines, Pacer, Ignite, Polar 360/Loop, Polar Team Pro |
| Open source | **No.** The Polar BLE SDK is source-available on GitHub under Polar's own "Software Development Kit Limited License Agreement" (free, modifiable, Polar-owned, terminable on 90 days' notice), not an open-source licence [13]; devices and cloud are closed |
| Hosting/deployment | Direct BLE streaming to a researcher's own app (no cloud required), **or** Polar Flow cloud + AccessLink API |
| Pricing model | Device purchase; no subscription for core use (optional Fitness Program EUR 9.99 a month); SDK and AccessLink free at present |
| Last verified | 2026-10-11 (vendor fact record); earlier passes 2026-08-21; H10 accelerometer re-confirmed 2026-10-09; AccessLink scope, limits and history, Polar 360 SDK specs, privacy roles and H10 and Verity Sense US prices re-verified 2026-10-10 |

## Summary

- Polar occupies a distinct and important position: it is the only vendor here that **sells raw-signal access as a first-class, openly documented, free feature** on inexpensive consumer hardware. The **Polar BLE SDK is public on GitHub** under Polar's own limited licence (source-available, not open source; see Pricing), streams raw ECG and accelerometer directly over Bluetooth to an app the researcher writes, and requires no partner programme, no approval, no fee, and no vendor cloud [13].

- The **Polar H10 chest strap** is, in practice, the field-standard reference device for heart rate and RR-interval measurement in exercise and physiology research. Polar states it was used in over 600 scientific studies in 2022 to 2023 and describes it as a gold-standard reference technology for HR in field settings, a vendor claim, but one broadly consistent with how the device is used in the literature.

- The trade-off is that Polar is a **sensor company, not a longitudinal-monitoring ecosystem**. The H10 and Verity Sense are session devices: they need a phone or watch nearby (or use limited internal memory), they are not 24/7 wearables, and Polar offers nothing resembling a research participant-management platform. For continuous free-living monitoring across weeks, Polar's watch line goes through the Polar Flow cloud and AccessLink API, which is a much more conventional (and more limited) consumer API: open to any registered Polar Flow user, but returning exercises only from the last 30 days and only after a participant links to the study's client, with continuous HR at 5-minute intervals (Verified 2026-10-10).

## Products / Platform Architecture

- Two quite different access paths, frequently confused:

### Path 1, Polar BLE SDK (direct, raw, no cloud)
- A source-available Android/iOS SDK, under Polar's "Software Development Kit Limited License Agreement" [13], that connects directly to Polar sensors over Bluetooth LE and streams raw data. No account, no cloud, no API key. Data lands in the researcher's own app. This is the research-relevant path.
- **Licence terms (Verified, 2026-10-11) [13]:** free while the licensee complies; use, copy and modify allowed with the notice kept, for private or commercial software; the grant is limited to enabling data transfer between Polar products and your software; Polar keeps all ownership and has no duty to update or support; not intended for medical use. Termination is on 90 days' written notice, or immediately for an uncured breach (7 days) or insolvency, after which all SDK copies must be deleted. The deletion clause does not name participant data collected through the SDK. GitHub reports the repository licence as NOASSERTION.

### Path 2, Polar Open AccessLink (cloud API)
- Polar's REST API providing access to data recorded by Polar consumer devices and synced to Polar Flow, basic user information, training sessions, daily activity, and (on supported devices) sleep and recharge data. Conventional OAuth consumer API, mostly summary-level, with two finer-grained exceptions: exercise samples include **RR interval in ms when the session was recorded with a Polar H6, H7, H9 or H10 chest strap**, and continuous heart rate is returned as 5-minute samples. Re-read 2026-10-10 (changelog entry 13.01.2026); see Data Access for limits.
- A third exception, added 2026-10-11 (Verified) [8]: the **Elixir Biosensing** resource (beta since 19.12.2023) returns body and sleep skin temperature, SpO2 test results and **wrist ECG test results that include the waveform as samples (amplitude in mV with a time offset in ms)**, plus quality levels, average HR, HRV, RR and pulse transit time. These are on-demand spot tests from the watch line, not continuous recording, and the ECG sample rate is not documented. Polar labels the wrist ECG test not for medical or diagnostic use [24].
- Deprecations (Verified, 2026-10-11) [8]: the transactional endpoints for Exercises and Daily activity were deprecated on 18.08.2025 and for Physical info on 13.01.2026, in favour of non-transactional endpoints; no removal date is published.

### Path 3, Polar Team Pro
- A team-sport system: sensors with GNSS positioning and IMU, real-time telemetry, and an API for exporting performance data to third-party analysis platforms. Polar reports it was used in 180 scientific studies in 2022 to 2023.

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | Verity Sense | Raw PPG, 22-bit in SDK mode | 28 to 176 Hz in SDK mode | In SDK mode, HR and PPI streaming are not available; it is raw PPG and IMU or Polar's derived pulse intervals, not both. |
| ECG | H10; watch line (wrist ECG spot test) | H10: raw, in microvolts, over the SDK. Watches: waveform samples in mV through AccessLink Elixir (beta), not through the SDK | H10 130 Hz; watch ECG rate not documented | Verified from `documentation/products/PolarH10.md`. Internal memory logs HR only, so a phone-free protocol captures HR, not ECG. Watch ECG route per AccessLink docs [8] and a Polar staff reply in SDK issue #887 [17] (2026-10-11). |
| Accelerometer | H10 and Verity Sense | Raw, per axis in mG | H10 25, 50, 100 or 200 Hz at plus or minus 2 to 8 g; Verity Sense 52 Hz normal, 26 to 416 Hz in SDK mode | The first pass recorded a contradiction on H10 accelerometry; the product documentation settles it as available. |
| Gyroscope | Verity Sense | Raw | 52 Hz normal, 26 to 416 Hz in SDK mode, up to 2000 degrees per second |  |
| Magnetometer | Verity Sense | Raw | 10 to 100 Hz, plus or minus 50 Gauss |  |
| Temperature | Watch line; Loop / 360 | Skin temperature streamed over the SDK; body and sleep skin temperature through AccessLink Elixir | Loop / 360 1 to 4 Hz; watch line to be queried from the device | Watch line per `PolarVantageV3andGritX2Pro.md` [16]; whether stored skin temperature can be read back is in conflict (see Watch line section). |
| SpO2 | Watch line | SpO2 test results (spot tests), via SDK export and AccessLink Elixir | Spot test | Verified 2026-10-11 [8][16]. |
| GPS | Watch line | Unclear | Unclear |  |
| Barometer / altimeter | Watch line | Pressure streamed over the SDK (online streaming only) | To be queried from the device | Verified 2026-10-11 [16][17]. |
| EDA | No | Not applicable | Not applicable |  |
| Ambient light | No | Not applicable | Not applicable |  |
| Other | Heart rate and R-R interval (H10); PPI (Verity Sense) | Raw over BLE | 1 Hz HR with RR in ms | Verity Sense also records offline. |

**Verification.** Verified from Polar's per-product SDK documentation (`PolarH10.md`, `PolarVeritySense.md`) in the 2026-08-21 second pass; see the notes below for the two corrections that pass made.

### Notes from earlier verification passes

- *(Rewritten 2026-08-21 second pass from the per-product SDK documentation, which resolves the contradiction previously recorded here.)*

### Polar H10, verified stream specifications

| Stream | Specification |
|---|---|
| Heart rate | BPM **and RR interval in ms**, sample rate **1 Hz** |
| **ECG** | **130 Hz, in µV** |
| **Accelerometer** | **25 / 50 / 100 / 200 Hz**, ranges **±2 / ±4 / ±8 g**, per-axis in mG |
| HR broadcast | Continuous BLE transmission (standard HR profile) |
| Internal recording | Onboard logging, **HR only, 1-second sample interval**; start/stop and retrieve stored sessions |

- **Verified** (`documentation/products/PolarH10.md`).

- **Contradiction resolved.** The first pass recorded a conflict between Polar's research-tools page (claiming H10 gives "raw sample data, such as ECG and 3D acceleration") and the SDK README's device matrix (which did not mark accelerometer for H10). The product documentation settles it: **the H10 does stream triaxial accelerometry, at up to 200 Hz and ±8 g.** The README matrix was incomplete. **Re-confirmed 2026-10-09 (Verified):** `PolarH10.md` (last changed 2026-03-13) still lists "Accelerometer data with sample rates of 25Hz, 50Hz, 100Hz and 200Hz and range of 2G, 4G and 8G", and the current README no longer carries a device capability matrix at all; it links each product to its own documentation page, so the conflicting source no longer exists.

- Note the asymmetry in onboard recording: the H10 can *stream* ECG and ACC over BLE, but its **internal memory logs heart rate only**. A phone-free H10 protocol therefore captures HR, not ECG.

### Polar Verity Sense, verified stream specifications

- Normal mode, with both online streaming and **offline recording**:

| Stream | Specification |
|---|---|
| Heart rate | BPM |
| **PPG** | Raw PPG values |
| **PPI** | Pulse-to-pulse interval in ms (PPG-derived) |
| Accelerometer | **52 Hz**, ±8 g, per-axis in mG |
| **Gyroscope** | **52 Hz**, ±2000 °/s |
| **Magnetometer** | 10 / 20 / 50 / 100 Hz, ±50 Gauss |

- **SDK mode** (firmware 1.1.5+) substantially expands this:

| Stream | Rates | Range | Resolution |
|---|---|---|---|
| Accelerometer | **26 to 416 Hz** | ±2 to ±16 g | 16-bit |
| Gyroscope | **26 to 416 Hz** | 250 to 2000 °/s | 16-bit |
| **PPG** | **28 to 176 Hz** | | **22-bit** |
| Magnetometer | 10 to 100 Hz | ±50 Gauss | 16-bit |

- **Verified** (`documentation/products/PolarVeritySense.md`).

- **Two corrections to the first pass.** (1) The Verity Sense **has a gyroscope and magnetometer**, which the README matrix omitted, it is a full 9-axis IMU plus optical sensor. (2) The first pass listed ECG for Verity Sense; **the product documentation does not list ECG for this device**, and it would be surprising for an optical armband. Treat Verity Sense as PPG-only for cardiac signal.

- **Offline recording caveat (Reported, 2026-10-11).** A Polar staff reply in SDK issue #887 says the offline recording API "is currently supported only by Polar H10" [17], which disagrees with the Verity Sense and Polar 360 product docs. The product docs are kept as governing; the reply may mean the H10's separate internal recording. Confirm with Polar before relying on Verity Sense offline recording.

- **In SDK mode, HR and PPI streaming/recording are not available**, you get raw PPG and IMU, but lose Polar's derived pulse intervals. That is a real design choice a protocol must make up front: Polar's PPI algorithm, or your own from 22-bit raw PPG at up to 176 Hz, but not both simultaneously.

### Watch line (Vantage V3/M3, Grit X2/Pro, Pacer/Pacer Pro)

- **Online streaming only (Verified, 2026-10-11) [16]:** heart rate, accelerometer (**50 Hz, 8 g**), PPG, PP intervals, gyroscope, magnetometer, pressure and skin temperature. Settings for PPG, gyroscope, magnetometer, pressure and skin temperature must be queried from the device; Polar has not published them [17].
- Streaming works only from the watch's exercise-wait view after a manual pairing and sharing step; **SDK mode is not supported on watches** [16].
- **No ECG over the SDK.** A Polar staff reply (issue #887, 2026-10-05) says the wrist ECG is not available through the BLE SDK [17]; the watch ECG reaches researchers only through AccessLink Elixir (see Path 2).
- **Stored 24/7 data is in conflict (Unclear, 2026-10-11).** The watch-line SDK product page lists data export of 24/7 HR samples, 24/7 PPi samples and skin temperature [16]; Polar staff (issues #887 and #886, 2026-10-05) say the Vantage V3 does not save these for SDK loading and that they are available only by live streaming [17]. Plan a watch-line study on live streaming or AccessLink and pilot any SDK read-back. Offline recording is not claimed for the watches in either source.

### Polar 360 / Loop, SDK specifications (added 2026-10-10)

- Per `documentation/products/Polar360.md` (read 2026-10-10, **Verified**): accelerometer 12 to 400 Hz online and 1 to 50 Hz offline, plus or minus 2 to 16 g; **PPG 22, 50 or 100 Hz online and offline, 24-bit, green channels**; skin temperature 1, 2 or 4 Hz; PP interval and 24/7 PPI samples. **24/7 PPI is not continuous** (Corroborated, Polar staff reply in issue #886, 2026-10-05) [17]: it is stored as automatically triggered measurement sessions whose schedule, length and day/night differences are undocumented, so measure coverage in a pilot before relying on it for HRV. The device has **15 MB** of storage shared by activity, sleep and SDK offline recordings, so data must be synced and deleted regularly. This makes the 360 the only Polar device in this profile with a documented multi-day raw-PPG offline path, bounded by 15 MB.

### Why this matters

- **22-bit raw PPG at up to 176 Hz from a $104.95 armband (Polar US list price, 2026-10-10), with a 9-axis IMU at up to 416 Hz, over a free, source-available SDK with no registration, no approval, no cloud and no fee, is the single most permissive raw-signal offer in this entire module.** It beats Samsung's 25 Hz accelerometer, beats Withings' ~25 Hz, and is obtained without a partner programme. The trade-off is form factor and wear duration, not signal quality.

## Derived Metrics / Analytics

- Via Polar Flow / AccessLink: training session summaries, daily activity, sleep, and Polar's proprietary recovery metrics (Nightly Recharge, Sleep Plus Stages, Training Load Pro, Recovery Pro, Orthostatic Test). These are conventional consumer-grade derived metrics. Per the AccessLink docs (Verified, 2026-10-11) [8], Nightly Recharge HRV is RMSSD, Cardio Load is TRIMP-based, and SleepWise (alertness and circadian bedtime) and Elixir biosensing were released in beta.

- Via the BLE SDK: essentially none, you get signals, and the analysis is yours. That is the point.

## Active Data Collection

- None. Polar has no survey/EMA capability. A study needing self-report must pair Polar sensors with a separate instrument or a Module 2 platform.

## Researcher and Study Management Features

- **None from Polar directly** for the SDK path. Team Pro provides a coaching-oriented management console for squads with real-time telemetry, which some field studies repurpose, but it is not a research participant-management system.

- There is no enrolment portal, adherence dashboard, or remote configuration. A study using the BLE SDK is building all of that itself, or using a third-party platform. Several third-party research tools integrate Polar sensors (e.g. Fibion's research offerings; Stanford's `wearipedia` includes a Polar H10 extraction guide).

### Research program and academic data access (added 2026-10-10)

- **No academic tier or academic price is published** (Corroborated, 2026-10-11) [15]. Polar's science pages describe the in-house Polar Research Center, list partner institutions, and point researchers to the same developer tools everyone uses.
- **Documented collaboration route (Verified, 2026-10-11) [15].** The "Collaborate with us" page sets out a proposal process for studies done jointly with Polar Electro Oy. Email research@polar.com with a presentation of the research unit, the responsible researcher's CV and recent publications, and a research plan of at most 10 pages including benefits to Polar, a budget and a proposal for Polar support (technology, money, other). Proposals are reviewed on criteria including value for the company, and Polar replies within two weeks; NDAs are used if needed. An accepted study gets a signed research agreement, and the research partner handles ethics approval. No eligibility rule is published, and studies outside Polar's interests are rejected (Corroborated). Status: active, inviting proposals as of 2026-10-11.
- A separate Polar-linked grant, the Seppo Saynajakangas Science Foundation, is open only to Finnish citizens studying in northern Finland, so it is not an access route for most study teams.
- **What academics get is what everyone gets, at no fee:** the BLE SDK (raw ECG, accelerometer, PPG and IMU, no registration) and AccessLink (any registered Polar Flow user can create a client). AccessLink limits: exercises only from the last 30 days and only after the participant links to the client, continuous HR at 5-minute intervals, activity no older than 365 days, rate limits of 500 + 20 x users per 15 minutes and 5,000 + 100 x users per 24 hours, under the AccessLink Limited License Agreement. **Verified** (polar.com/accesslink-api, 2026-10-10). The API agreement excludes EU Digital Markets Act gatekeepers; no review step is otherwise documented (Verified, 2026-10-11) [14].
- **Polar 360 B2B:** Polar sells the 360 band to businesses as a platform to build apps on through the SDK or API; pricing and B2B partnerships go through a contact form, with no published price or minimum commitment (2026-10-11) [25].
- **Active:** yes (AccessLink changelog 13.01.2026; BLE SDK release 8.4.0 on 2026-10-01).

## Data Access and Export

| Route | What you get | Constraints |
|---|---|---|
| **BLE SDK live stream** | Raw ECG, ACC, PPG, PPI, gyro, magnetometer, temperature (device-dependent) | Requires a phone/app within Bluetooth range and running; you write the app |
| **Device internal memory** | H10 and Verity Sense have built-in memory for offline recording | Capacity-limited; a session-recording model, not weeks of continuous capture |
| **Polar Flow export** | Session files, CSV/TCX exports; participant self-export at account.polar.com; sync to Apple Health and Google Fit | Consumer-grade, summary-level. The route for anything older than AccessLink's windows [19] |
| **Open AccessLink API (v3)** | Exercises with per-session samples (HR, speed, cadence and others, plus **RR interval in ms when recorded with a Polar H6, H7, H9 or H10 chest strap**), continuous HR in **5-minute** samples, daily activity, sleep, Nightly Recharge, SleepWise alertness and circadian bedtime (last 28 days), Elixir biosensing (beta: body and sleep skin temperature, wrist ECG test results with waveform samples in mV, SpO2 test results; last 28 days), user info; webhooks | OAuth 2.0; "Any registered Polar Flow user can create API client"; governed by the AccessLink Limited License Agreement. **Only exercises uploaded to Flow in the last 30 days, and only those uploaded after the user registered with your client, are returned**; activity lists default to 28 days and reject dates older than 365 days. Rate limits: 500 + 20 x users per 15 minutes and 5,000 + 100 x users per 24 hours. Verified 2026-10-10 (polar.com/accesslink-api). |
| **Team Pro API** | Performance data for third-party analysis platforms | Team-sport oriented; rate limit about 1 request per second (Verified, 2026-10-11) [26] |

- The internal-memory feature is important for field research: **Verity Sense and H10 can record without a phone present** and be offloaded later, which enables protocols (swimming, occupational settings, paediatric use) where carrying a phone is impossible. Recording duration is limited and should be checked per device.

- **Operational caveats (Verified, 2026-10-11).** AccessLink webhooks are switched off automatically after 7 days of failed delivery, and calls return 403 if the user has not accepted all mandatory consents [8]. The H10 drops its BLE connection 45 seconds after it is taken off the strap, so keep it on a worn strap while downloading a long internal recording [27]. Biosensing data (ECG, SpO2, temperature) is limited to the last 28 days or a range of at most 28 days [8].

## APIs, SDKs, and Extensibility

- **Polar BLE SDK**, source-available under Polar's limited licence [13], Android and iOS, at https://github.com/polarofficial/polar-ble-sdk. Community wrappers exist for Flutter/Dart, Python (`polar-python`), and CocoaPods.
- **SDK breaking changes (Verified, 2026-10-11) [18]:** 7.0.0 (2026-04-15) moved Android from RxJava to Kotlin Flow and 8.0.0 (2026-05-27) moved iOS from RxSwift to Combine and Swift Concurrency; both need app changes. 8.4.0 (2026-10-01) says 9.0.0 will add Xcode 27 support, which drops iOS versions before 15, and asks users to move off CocoaPods, which goes read-only by 2 December 2026. A study app pinned to an older SDK should plan for this.
- **Polar Open AccessLink**, REST + OAuth.
- **Team Pro API**.
- Standard Bluetooth Heart Rate Profile support means H10/Verity Sense also work with generic BLE HR tooling and with third-party research apps out of the box, a low-friction integration path.
- Devices also support ANT+ (H10, Verity Sense), broadening compatibility with gym and lab equipment.

## Deployment and Infrastructure

- For the SDK path: none required beyond the researcher's own app and storage. **No vendor cloud is involved at all**, which is unusual and valuable, there is no vendor DPA, no rate limit and no retention policy on the raw-data path. It is not free of vendor risk, though: Polar can end the SDK licence on 90 days' notice, after which all SDK copies must be deleted, and the SDK had two breaking major releases in 2026 with a third announced [13][18].

- For AccessLink: vendor cloud, OAuth, standard. The API agreement runs until either party gives 30 days' written notice, and Polar may suspend or terminate access immediately for any or no reason; on termination the licensee must delete all copies of Polar data, including data a study has already pulled (Verified, 2026-10-11) [14]. Load testing without Polar's approval is prohibited [14].

## Participant Experience

- **H10 chest strap:** high fidelity, but a chest strap is uncomfortable for continuous multi-day wear, can cause skin irritation, and requires wetting the electrodes. Adherence over weeks is poor. It is a **session device**.
- **Verity Sense / OH1 armband:** worn on the upper arm or forearm, better tolerated than a chest strap, better signal than a wrist for exercise, but still not a 24/7 device and not a sleep device.
- **Polar watches (Vantage, Grit X, Pacer, Ignite, 360/Loop):** conventional wrist wearables with good battery life; these are the option for continuous free-living monitoring, at the cost of losing continuous raw ECG. The watch line's wrist ECG is an on-demand spot test whose waveform is available only through AccessLink Elixir, not the SDK [8][17].
- Polar 360 is a screenless band aimed at organisational/health-programme deployments.
- iOS and Android both supported.
- Devices are inexpensive relative to research-grade alternatives, making per-participant provisioning realistic.

## Privacy, Security, and Compliance

- The BLE SDK path is the strongest privacy story in this module: **no data leaves the participant's device except by the researcher's own code.** Compliance attaches entirely to the researcher's stack.
- For the Polar Flow/AccessLink path, Polar is EU-based (Finland), which is generally favourable for GDPR. **Roles (Verified, Polar privacy notice, read 2026-10-10):** Polar Electro Oy is the data controller for Polar Flow, and "Polar is not responsible for customer shared data once it is transferred out of Polar's system". So data a participant links to a study through AccessLink is a transfer the participant authorises, with the research team as an independent recipient, not a processor arrangement. Polar acts as data processor under a signed agreement only for B2B products such as Polar Team Pro and GoFit. No HIPAA or BAA language appears in the notice.
- **Processor agreement (Corroborated, 2026-10-11) [9][14]:** for Team Pro (and GoFit) the customer signs an unpublished agreement under which Polar is processor; no DPA applies to AccessLink, where Polar and the developer are each controllers, or to the BLE SDK. BAA and HIPAA statements: not public (no mention on any page checked, 2026-10-11).
- **GDPR and transfers (Corroborated, 2026-10-11) [9][19]:** Polar says it complies with the GDPR, and a separate Data Notice covers the EU Data Act. The privacy notice says transfers outside the EU/EEA use the EU-US, UK-US and Swiss-US Data Privacy Frameworks or standard contractual clauses. Polar Electro is not on the Commerce Department's DPF list, active or inactive (browser check, 2026-10-11), so the verifiable route is standard contractual clauses; the DPF wording most likely refers to US recipients' certification (inference).
- **Data residency (Corroborated, 2026-10-11) [9][19][21]:** Polar Flow and Team Pro service data is stored on Polar's servers in the EU (Ireland and Sweden), hosted on AWS in the EU; email addresses or user IDs may go to providers outside the EU for notifications and error reporting. No customer choice of region is offered (inferred from absence).
- **Certifications (2026-10-11) [20]:** Polar publishes only ISO 9001:2015 for Polar Electro Oy (Kiwa, valid until 2028-08-31) and ISO 14001:2015 for its Malaysian manufacturing subsidiary (SGS, valid to 2027-01-07). ISO 27001 and SOC 2: not public (Corroborated).
- **Retention (Verified, 2026-10-11) [14][19]:** Polar keeps Flow data while the account is active; Team Pro data is kept 180 days after the licence ends unless earlier deletion is requested. AccessLink licensees must revoke and delete a member's token when the member asks or the relationship ends.
- **Polar's own use of data (Verified, 2026-10-11) [9][19]:** Polar uses customer data internally for R&D, including developing and testing new algorithms, with identifiers removed as far as possible; users can opt out in Polar Flow or account.polar.com. No explicit AI or ML wording. Neither the API agreement nor the SDK licence addresses AI or ML use of data by licensees (not public).
- **FDA (Verified, 2026-10-11) [28]:** no 510(k), PMA or establishment registration for Polar Electro in openFDA. The SDK licence says the SDK and devices are not intended for medical use [13].

## Pricing

- **SDK: free, under Polar's proprietary limited licence** (source-available, not open source; free "subject to You being in compliance") [13]. No partner programme, no approval gate, no licence fee. This is the cheapest path to raw physiological signal in the entire module.
- **Devices:** H10 and Verity Sense are inexpensive consumer sensors, each listed at **$104.95** on Polar's US store (2026-10-10, Verified). Prices in other regions were not checked and are not recorded here. Watches span a wider range: on 2026-10-11 the US store listed Pacer $299.90, Ignite 3 $399.99, Vantage V3 $699.99 and Grit X2 Pro $999.99, and POLAR Loop $199.99 (Verified) [23]. Team Pro is a system-level purchase. Polar 360 for business has no published price; it goes through a contact form [25].
- **No subscription** for core functionality; Polar Flow stays free and Loop is sold as subscription-free. An optional **Fitness Program** (needs a Polar watch) is free to try, then **EUR 9.99 a month**; no USD price is published (Verified, 2026-10-11) [22].
- Polar Flow / AccessLink: free at present, but the API agreement says Polar "reserves the right to charge fees from time to time at its discretion" (Verified, 2026-10-11) [14]. No minimum commitment; see Deployment for termination terms.
- No academic or volume discount is published (not public, 2026-10-11); a collaboration proposal may ask Polar for support in technology or money, decided case by case [15].
- **Device price check 2026-10-10:** Polar's US store lists the H10 at **$104.95** and the Verity Sense at **$104.95** (polar.com/us-en, Verified). The Verity Sense page has moved to `/us-en/products/accessories/polar-verity-sense` (the old `/us-en/sensors/verity-sense` path returns a 404 page). This replaces the earlier "~$95" Verity Sense figure and the unsourced EUR 80 to 120 retail range.
- **Cost per raw-ECG-capable participant is roughly an order of magnitude below Empatica and ActiGraph/Ametris.**

## Research Evidence and Validation

- **Polar H10 is the de facto field reference for HR and RR intervals.** Polar states it was used in over 600 scientific studies in 2022 to 2023 and describes it as a golden-standard reference technology for HR measurement in field settings. It is routinely used *as the criterion measure* when validating other wearables, which is itself the strongest evidence of its standing, though it also means the H10's own validation is somewhat circular in the applied literature.
- Polar reports Team Pro was used in 180 scientific studies over the same period and that over 1,000 peer-reviewed papers per year cite Polar technology. **These are vendor claims** (status: Reported) and the counting methodology is not stated.
- Polar's *watch-based* consumer metrics have not fared as well: Polar was not included in either the 2024 *Sensors* or 2025 Schyvens PSG comparisons, so its sleep-staging validity against PSG is **not established** by those benchmarks.
- The critical distinction: **Polar's raw-signal hardware is well validated; Polar's derived consumer metrics are not particularly better evidenced than any competitor's.** Use Polar for signals, not for scores.

## Strengths

- **Free, source-available SDK with raw ECG, accelerometer, PPG, and beat-to-beat intervals**, no approval, no fee, no vendor gatekeeping (under Polar's limited licence, terminable on 90 days' notice). Unique in this module.
- H10 is the accepted field reference for HR/RR and is cheap enough to deploy widely.
- HRV computed by the researcher from RR intervals, using published methods, full construct transparency, no vendor black box.
- No vendor cloud on the raw path: no rate limits, no retention policy, minimal compliance surface. Vendor risk remains through the SDK licence (90 days' notice) and breaking SDK releases.
- On-device memory enables phone-free recording in constrained settings.
- Standard BLE HR profile and ANT+ support give broad third-party compatibility.
- Very low cost per participant for raw-signal capability.
- iOS and Android.
- EU-based vendor, favourable for GDPR-sensitive studies.

## Limitations

- **Not a continuous-monitoring ecosystem.** Chest straps and armbands are session devices; adherence over weeks is poor.
- **No study management of any kind**, no enrolment, no adherence monitoring, no remote configuration.
- Requires the research team to write a mobile app for the SDK path (or adopt third-party tooling).
- The raw path requires a phone in Bluetooth range and running, or reliance on limited internal memory.
- Watch-line consumer metrics are unremarkable and their sleep staging is unvalidated against PSG in the major comparisons.
- Device capability matrix in the SDK documentation contains at least one apparent error; per-device verification is necessary.
- Sampling rates not documented at the top level of the SDK.
- No survey/EMA capability.
- Watch-line SDK access is narrow: streaming only from the exercise-wait view, no ECG, and stored 24/7 data read-back in conflict between Polar's docs and its staff (2026-10-11).
- AccessLink is a conventional consumer API, not a research API: no backfill before a participant registers with the client, a 30-day window for exercises, and 5-minute continuous HR.

## Best-Fit Use Cases

- **HRV research** requiring genuine beat-to-beat intervals and researcher-computed metrics.
- Exercise physiology, sports science, and cardiac autonomic function research.
- Ambulatory/laboratory sessions, stress-reactivity protocols, and paced-breathing studies.
- Providing the **criterion measure** in a study validating another wearable.
- Studies needing raw signal on a small budget.
- Studies where no data may touch a vendor cloud.
- Occupational and field settings where a phone cannot be carried (using onboard memory).

## Poor-Fit Use Cases

- Multi-week or multi-month continuous free-living monitoring on a single device.
- Sleep staging research.
- Large remote cohorts needing adherence monitoring and automated data collection.
- Studies without mobile development capacity and without third-party tooling.
- Studies requiring integrated survey/EMA.
- Step count, energy expenditure, or general activity as primary endpoints (use a wrist device or research-grade actigraph instead).

## Open Questions

- *(Directed to Polar: https://www.polar.com/en/developers , research enquiries via https://www.polar.com/en/science/ )*

- ~~Resolve the device capability matrix~~, **RESOLVED from the per-product SDK docs.** H10 does
- stream accelerometry (25/50/100/200 Hz, ±2/4/8 g). Verity Sense does **not** list ECG, but does have gyroscope and magnetometer. The SDK README matrix is incomplete; the product docs govern.
- Documented sampling rates and configurable ranges for H10 ECG/ACC and Verity Sense PPG/ACC.
- Internal memory recording capacity and maximum continuous duration for H10 and Verity Sense (the SDK docs give 15 MB only for Polar 360).
- Battery life under continuous raw streaming for each sensor.
- ~~Whether Open AccessLink exposes any beat-to-beat/RR data, or only session summaries.~~ ~~AccessLink rate limits, historical depth, and backfill.~~ Resolved 2026-10-10 (Verified, polar.com/accesslink-api): AccessLink returns exercise RR intervals when a Polar chest strap was used; rate limits are 500 + 20 x users per 15 minutes and 5,000 + 100 x users per 24 hours; there is no backfill before a user registers with the client, and exercises older than 30 days are not returned.
- Polar Flow / AccessLink: partly answered 2026-10-10 (controller-to-controller transfer under the privacy notice; no HIPAA or BAA language). Still open: whether Polar will sign a BAA, and whether a research institution can get a Team-Pro-style processor agreement. Data residency (EU, Ireland and Sweden) and certifications (ISO 9001 and 14001 only) answered 2026-10-11 from the vendor fact record.
- Whether stored 24/7 HR, PPi and skin temperature can be read back from Vantage V3 / Grit X2 watches over the SDK (product doc and Polar staff reply in #887 disagree, 2026-10-11), and whether Verity Sense supports offline recording given the same reply.
- The sample rate of AccessLink Elixir wrist ECG data (undocumented as of 2026-10-11).
- Methodology behind the "600 studies" and "1,000 papers per year" claims.
- ~~Polar 360's data-access model, is it SDK-accessible or cloud-only?~~ Answered 2026-10-10: SDK-accessible (see Watch line section).

## Vendor Fact Record

<!-- facts:begin -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | Polar Research Center collaboration ("Collaborate with us"): a research unit sends a research co-operation proposal for a study done jointly with Polar Electro Oy, and may ask for Polar support in technology, money or other forms. Polar also markets the H10, Verity Sense, the AccessLink API, the BLE SDK and Team Pro as research tools, but researchers buy and use these on standard terms; that is product information, not a program with its own terms. [V, 2026-10-11] |
| Who can join the research program | No published eligibility rule. The proposal is expected from a research unit (institute, university, department or similar) with a responsible researcher, and proposals are rated partly on their value to Polar, so studies outside Polar's interests are rejected or wait-listed. [C, 2026-10-11] |
| How to apply, and any approval or review step | Email a research co-operation application to research@polar.com with a presentation of the research unit, the responsible researcher's CV and recent publications, and a research plan of at most 10 pages that includes benefits to Polar, a budget and a proposal for Polar support (technology, money, other). Proposals are reviewed on criteria including "value for the company", and Polar replies within two weeks; NDAs are used if needed. An accepted study gets a signed research agreement, and the research partner handles ethical approvals. [V, 2026-10-11] |
| Whether the program is active, paused, renamed or closed | Active as of 2026-10-11; the collaboration page invites proposals and gives a submission address. No pause or closure announced. [C, 2026-10-11] |
| Whether the general developer or API program is open to new applicants | Open. Any Polar Flow user can self-register an AccessLink API client at admin.polaraccesslink.com after accepting the API Limited License Agreement; no review step is documented, but EU Digital Markets Act gatekeepers are excluded. The Team Pro API uses the same admin portal. The BLE SDK is public on GitHub (release 8.4.0, 2026-10-01) under Polar's own limited licence. Polar 360 is also sold B2B as a band to build apps on through the SDK or API. [V, 2026-10-11] |
| Participant or user limits before approval or by tier | Not public [2026-10-11] |
| How academic access differs from commercial or consumer access | No separate academic tier. AccessLink and the BLE SDK are free on the same terms for everyone, and the SDK licence allows private and commercial use. The only research-specific route is the collaboration proposal, which Polar chooses whether to support; B2B partnerships go through a contact form. [C, 2026-10-11] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | **Polar H10 chest strap:** USD 104.95 (US store, 2026-10-11) [V, 2026-10-11]<br>**Polar Verity Sense:** USD 104.95 (US store, 2026-10-11) [V, 2026-10-11]<br>**POLAR Loop:** USD 199.99 (US store, 2026-10-11) [V, 2026-10-11]<br>**Watches:** US store, 2026-10-11: Pacer $299.90, Ignite 3 $399.99, Vantage V3 $699.99, Grit X2 Pro $999.99 [V, 2026-10-11] |
| Consumer subscription or membership price | No subscription needed for Polar Flow or the devices. The optional Fitness Program (needs a Polar watch) is free to try, then EUR 9.99 a month; the live product page shows this price on 2026-10-11, as did the April 2025 launch release. POLAR Loop is sold as subscription-free. [V, 2026-10-11] |
| Research or academic pricing or discount | Not public [2026-10-11] |
| Fees for API, SDK, platform or data access | **AccessLink and Team Pro API:** Free at present, but Polar reserves the right to charge fees at its discretion. [V, 2026-10-11]<br>**BLE SDK:** Free of charge while the licensee complies. The SDK ships under Polar's proprietary "Software Development Kit Limited License Agreement", not an open-source licence: you may use, copy and modify it with the notice kept, for private or commercial software, but the grant is worldwide, non-exclusive, non-transferable and limited to enabling data transfer between Polar products and your software; Polar keeps all ownership; Polar has no duty to provide updates or support; and the SDK and devices are not intended for medical use. Termination terms are under retention_terms (BLE SDK). [V, 2026-10-11] |
| Minimum order, term or commitment | **AccessLink API:** None. The API agreement runs until either party gives 30 days' written notice; Polar may also suspend or terminate access immediately for any or no reason. [V, 2026-10-11]<br>**Business and B2B (Polar 360, volume device orders):** Not public [2026-10-11] |
| Whether pricing requires contacting sales | **Consumer devices:** Consumer watches and sensors have public list prices. [V, 2026-10-11]<br>**Polar 360 and B2B:** Polar 360 (the business band) and B2B partnerships go through a contact form; no price is published. [V, 2026-10-11] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | **BLE SDK, Polar H10:** Heart rate with RR intervals, ECG in microvolts, and 3-axis accelerometer, streamed live; the internal recording holds HR only. [V, 2026-10-11]<br>**BLE SDK, Polar Verity Sense:** PPG, PP intervals, heart rate, accelerometer, gyroscope and magnetometer, by live streaming or offline recording on the sensor. [V, 2026-10-11]<br>**BLE SDK, POLAR Loop and Polar 360:** Green-channel PPG, PP intervals, accelerometer, skin temperature and heart rate (streaming and offline recording), plus export of 24/7 HR and PPi samples stored on the device. [V, 2026-10-11]<br>**BLE SDK, Vantage V3, Vantage M3, Grit X2 Pro and Grit X2:** Online streaming only: heart rate, accelerometer (50 Hz, 8 g), PPG, PP intervals, gyroscope, magnetometer, pressure and skin temperature. Streaming works only from the watch's exercise-wait view after a manual pairing and sharing step; SDK mode is not supported on watches. No ECG over the SDK: Polar staff say the wrist ECG is not available through the BLE SDK. [V, 2026-10-11]<br>**AccessLink API (Polar Flow cloud):** No raw PPG or accelerometer. Closest to raw are exercise samples (with RR intervals when an H6, H7, H9 or H10 strap was used), exercise FIT/TCX/GPX files, and 5-minute continuous heart rate. The Elixir Biosensing resource (beta) returns wrist ECG test results that include the ECG waveform as samples (amplitude in mV with a time offset in ms) plus quality levels, average HR, HRV, RR and pulse transit time, and SpO2 test results, from the watch line's on-demand spot tests. The cloud API is therefore the only route to a Polar watch's ECG. [V, 2026-10-11] |
| Derived or processed metrics available to researchers | AccessLink: exercises (with optional samples, zones, Training Load Pro), daily activity (steps, calories, activity zones), 5-minute continuous heart rate, sleep and Sleep Plus Stages, Nightly Recharge (overnight HRV as RMSSD, breathing rate, ANS charge), Cardio Load (TRIMP-based), SleepWise alertness and circadian bedtime, and Elixir biosensing (body and sleep skin temperature, wrist ECG and SpO2 test results). SDK on Loop/360 and the watch line: steps, active time, calories, MET samples, Nightly Recharge, sleep. [V, 2026-10-11] |
| Documented sampling rates or temporal resolution | **BLE SDK:** H10: ECG 130 Hz; accelerometer 25, 50, 100 or 200 Hz; HR and RR at 1 Hz. Verity Sense: accelerometer and gyroscope 52 Hz by default (more options in SDK mode), PPG 55 Hz by default (28 to 176 Hz in SDK mode), magnetometer 10 to 100 Hz. Loop/360: PPG 22 Hz, accelerometer 50 Hz, skin temperature 1 to 4 Hz. Vantage V3 / Grit X2 line: accelerometer 50 Hz; other stream settings must be queried from the device. [V, 2026-10-11]<br>**AccessLink API:** Continuous (24/7) heart rate in 5-minute samples; training-session samples at a finer interval through the exercise endpoints. On Loop/360 the device's own 24/7 HR is 5-minute averages at low activity and 60 samples per minute at high activity. [V, 2026-10-11]<br>**BLE SDK, 24/7 PPi on Polar 360 and Loop:** Not continuous. 24/7 PPi is stored as automatically triggered measurement sessions; the trigger schedule, session length and day/night differences are undocumented. Each interval carries an error estimate and skin-contact, movement and online/offline flags. Polar advises measuring coverage in a pilot. [C, 2026-10-11] |
| How far back data can be retrieved | **AccessLink API:** Nothing from before the user registered with the client. Exercises: last 30 days. Sleep, Nightly Recharge, SleepWise: last 28 days. Daily activity and activity samples: up to 365 days back, in windows of at most 28 days. Biosensing (ECG, SpO2, temperature): last 28 days or a range of at most 28 days. Older data needs the participant's own export from account.polar.com. [V, 2026-10-11] |
| Export, API, SDK or file routes | AccessLink REST API (OAuth2, JSON or XML, webhooks, exercise FIT/TCX/GPX files); BLE SDK for Android and iOS (live streaming, and offline or stored data read from the device); Team Pro API for Team Pro data; participant self-export at account.polar.com; sync to Apple Health and Google Fit. [V, 2026-10-11]<br>**BLE SDK, stored 24/7 data on Vantage V3, Vantage M3, Grit X2 Pro and Grit X2:** The watch-line SDK product page lists data export of 24/7 HR samples, 24/7 PPi samples and skin temperature data; a Polar staff reply (issue #887, 2026-10-05) says the Vantage V3 does not save 24/7 HR, PPi or skin temperature for SDK loading and that these are available only by online streaming. (conflict) [U, 2026-10-11] |
| API rate limits | **AccessLink API:** Dynamic, per partner, recalculated daily. 15-minute limit 500 + 20 x registered users; 24-hour limit 5000 + 100 x registered users. Excess returns HTTP 429. Load testing without Polar's approval is prohibited. [V, 2026-10-11]<br>**Team Pro API:** About 1 request per second per client. [V, 2026-10-11] |
| Terms on retaining, storing or deleting data | **AccessLink and Polar Flow:** API licensees must stop access, revoke and delete the member's token when the member asks or the relationship ends, and must delete all copies of Polar Data when the agreement ends. No fixed retention period for retrieved data while the agreement runs. Polar keeps Flow data while the account is active; Team Pro data is kept 180 days after the licence ends unless earlier deletion is requested. [V, 2026-10-11]<br>**BLE SDK licence:** The licence runs until terminated on 90 days' written notice (the clause reads "terminated by Polar by either Party"); Polar may also terminate immediately for a material breach not cured within 7 days, or on the licensee's insolvency. On termination for any reason the licensee must stop using the SDK and delete all copies of the SDK and of Polar's Confidential Information. The clause does not name participant Data collected through the SDK, unlike the API agreement. [V, 2026-10-11] |
| Terms on using data to train AI or ML models | **API and SDK licensees:** Not public [2026-10-11]<br>**Polar's own use of user data:** Polar uses customer data internally for R&D, including developing and testing new algorithms, with identifiers removed as far as possible; users can opt out in Polar Flow or account.polar.com. No explicit AI or ML wording. [V, 2026-10-11] |
| Announced shutdowns, deprecations or migrations, with dates | **AccessLink API:** Transactional endpoints for Exercises and Daily activity deprecated on 18.08.2025, and for Physical info on 13.01.2026, in favour of new non-transactional endpoints. No removal date published. [V, 2026-10-11]<br>**BLE SDK:** Breaking major releases in 2026: 7.0.0 (2026-04-15) moved Android from RxJava to Kotlin Flow, and 8.0.0 (2026-05-27) moved iOS from RxSwift to Combine and Swift Concurrency; both need app changes. 8.4.0 (2026-10-01) says the next major release, 9.0.0, will add Xcode 27 support, which drops pre-iOS 15, and asks users to move off CocoaPods, which goes read-only by 2 December 2026. [V, 2026-10-11] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-11] |
| Whether a data processing agreement is offered | For B2B services (Team Pro, and per the privacy notice GoFit) the customer signs an agreement under which Polar is the data processor and the customer the controller; that agreement is not published. No DPA applies to AccessLink, where Polar and the API developer are each controllers, or to the BLE SDK, where the licensee alone is responsible for the data. [C, 2026-10-11] |
| Published HIPAA statement | Not public [2026-10-11] |
| Published GDPR statement | Polar says it complies with the GDPR. Polar Electro Oy (Finland) is the controller for Polar Flow data, AccessLink developers are also controllers for the data they receive, and for Team Pro Polar is the processor. Transfers outside the EU/EEA use the EU-US, UK-US and Swiss-US Data Privacy Frameworks or standard contractual clauses. A separate Data Notice covers the EU Data Act. [C, 2026-10-11] |
| ISO/IEC 27001 status and evidence | Not public [2026-10-11] |
| SOC 2 status and evidence | Not public [2026-10-11] |
| FDA clearances, from the FDA database | Not public [2026-10-11] |
| Where data is stored, and residency options | Polar Flow and Team Pro service data is stored on Polar's servers in the EU (Ireland and Sweden), hosted on AWS in the EU; email addresses or user IDs may go to service providers outside the EU for notifications and error reporting. No customer choice of region is offered. BLE SDK data never passes through Polar unless the device also syncs to Polar Flow. [C, 2026-10-11] |

<!-- facts:end -->

## Key Links

- Official site: https://www.polar.com/
- Developers portal: https://www.polar.com/en/developers
- **Polar BLE SDK (GitHub, source-available under Polar's limited licence):** https://github.com/polarofficial/polar-ble-sdk
- H10 SDK documentation: https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/products/PolarH10.md
- Verity Sense SDK documentation: https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/products/PolarVeritySense.md
- Research tools: https://www.polar.com/en/science/research-tools/
- Polar science: https://www.polar.com/en/science
- Open AccessLink: https://www.polar.com/accesslink-api/
- Polar Team Pro: https://www.polar.com/en/business/team-pro
- Third-party extraction guide (Stanford wearipedia): https://wearipedia.readthedocs.io/en/latest/notebooks/polar_h10.html
- SDK licence: https://github.com/polarofficial/polar-ble-sdk/blob/master/Polar_SDK_License.txt
- API agreement: https://www.polar.com/en/legal/polar-api-agreement
- Research collaboration proposals: https://www.polar.com/en/science/collaborate-with-us

## Sources

1. Polar BLE SDK repository. https://github.com/polarofficial/polar-ble-sdk (accessed 2026-08-21). **Primary.** Establishes public availability of the source (licence terms are in [13]), Android/iOS support, streamable data types (HR, ECG, ACC, PPG), and the per-device support matrix, the latter containing apparent errors, see body text.
2. Polar, Research tools. https://www.polar.com/en/science/research-tools/ (accessed 2026-08-21). **Primary (vendor).** Establishes H10 raw ECG and 3D acceleration access, Verity Sense PPG and acceleration with built-in memory and SDK connectivity, Open AccessLink's scope, Team Pro's GNSS/IMU/real-time telemetry and API, and the vendor claims of 600+ H10 studies, 180 Team Pro studies (2022 to 2023), and 1,000+ papers per year.
3. Polar developers portal. https://www.polar.com/us-en/developers (accessed 2026-08-21).
4. Polar H10 and Verity Sense per-product SDK documentation. https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/products/PolarH10.md ; .../PolarVeritySense.md (retrieved in the 2026-08-21 second pass and re-read 2026-10-09; `PolarH10.md` last changed 2026-03-13). **Primary.** Resolves the capability-matrix discrepancy: H10 streams ECG at 130 Hz and accelerometry at 25 to 200 Hz, plus or minus 2 to 8 g.
5. Fibion, "Using Polar SDK & API in Research." https://web.fibion.com/articles/polar-sdk-api-research-fibion/ (accessed 2026-08-21). Secondary; corroborates real-time streaming of HR, RR intervals, and accelerometer from H10 and Verity Sense.
6. Stanford wearipedia, Polar H10 extraction guide. https://wearipedia.readthedocs.io/en/latest/notebooks/polar_h10.html (accessed 2026-08-21). Evidence of academic tooling.
7. Schyvens A.-M. et al. *SLEEP Advances* 2025;6(2):zpaf021. https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472, noted as **not** including Polar.
8. Polar AccessLink API v3 documentation. https://www.polar.com/accesslink-api/ (accessed 2026-10-10; changelog entry 13.01.2026). **Primary.** Any registered Polar Flow user can create a client; Limited License Agreement; RR interval samples with H6, H7, H9 or H10; continuous HR in 5-minute samples; 30-day and post-registration exercise window; 28-day default and 365-day limit for activity; rate-limit formulas; webhooks.
9. Polar privacy notice. https://www.polar.com/en/legal/privacy-notice (accessed 2026-10-10). **Primary.** Polar Electro Oy as controller; not responsible for data transferred out; processor role for Team Pro and GoFit under agreement; no HIPAA language.
10. Polar BLE SDK product documentation, Polar 360. https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/products/Polar360.md (accessed 2026-10-10; latest SDK release 8.4.0, 2026-10-01). **Primary.**
11. Polar H10 product page, Polar USA store. https://www.polar.com/us-en/sensors/h10-heart-rate-sensor (accessed 2026-10-10). $104.95 list price.
12. Polar Verity Sense product page, Polar USA store. https://www.polar.com/us-en/products/accessories/polar-verity-sense (accessed 2026-10-10). $104.95 list price.
13. Polar Electro Oy, "Software Development Kit Limited License Agreement" (Polar_SDK_License.txt). https://github.com/polarofficial/polar-ble-sdk/blob/master/Polar_SDK_License.txt (accessed 2026-10-11). **Primary.** Proprietary limited licence: free while compliant, use/copy/modify with notice, limited grant, Polar ownership, no support duty, not for medical use, 90-day termination and deletion of SDK copies.
14. Polar API Limited License Agreement. https://www.polar.com/en/legal/polar-api-agreement (accessed 2026-10-11). **Primary.** Free at present with fees reserved; 30-day notice and immediate suspension; deletion of data on termination; gatekeeper exclusion; load-testing ban; controller roles.
15. Polar, "Collaborate with us." https://www.polar.com/en/science/collaborate-with-us (accessed 2026-10-11). **Primary.** Research co-operation proposal process, review criteria, two-week reply, research agreement.
16. Polar BLE SDK watch-line documentation. https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/products/PolarVantageV3andGritX2Pro.md ; https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/UsingSDKWithWatches.md (accessed 2026-10-11). **Primary.** Watch-line streams, 50 Hz accelerometer, data export list, SDK mode not supported on watches.
17. Polar BLE SDK issues #887 and #886, Polar staff replies of 2026-10-05. https://github.com/polarofficial/polar-ble-sdk/issues/887 ; https://github.com/polarofficial/polar-ble-sdk/issues/886 (read 2026-10-11). Vendor staff statements, not documentation: no ECG over the SDK on Vantage V3, no stored 24/7 data for SDK loading, stream settings queried from device, 24/7 PPi as triggered sessions.
18. Polar BLE SDK releases 7.0.0, 8.0.0 and 8.4.0. https://github.com/polarofficial/polar-ble-sdk/releases (accessed 2026-10-11). **Primary.** Breaking majors and the announced 9.0.0 iOS 15 floor and CocoaPods move.
19. Polar Data Notice. https://www.polar.com/en/legal/data-notice (accessed 2026-10-11). **Primary.** Self-export at account.polar.com, EU storage in Ireland and Sweden, retention while the account is active, Team Pro 180 days, internal R&D use, EU Data Act.
20. Polar ISO certificates. https://polar.com/img/documents/iso/ISO_9001_Certification_PEOY_en.pdf ; https://www.polar.com/img/documents/iso/PEM_ISO_14001_2015_certification.pdf (accessed 2026-10-11). **Primary.**
21. Polar service providers. https://www.polar.com/en/legal/polar-service-providers (accessed 2026-10-11). **Primary.** AWS hosting in the EU; sub-processor role.
22. Polar Fitness Program. https://www.polar.com/us-en/fitness-program ; launch release https://www.polar.com/en/media-room/polar-introduces-fitness-program (accessed 2026-10-11). **Primary.** EUR 9.99 a month after a free trial; Flow remains free.
23. Polar US store product pages for Pacer, Ignite 3, Vantage V3, Grit X2 Pro and Loop. https://www.polar.com/us-en/pacer ; https://www.polar.com/us-en/ignite3 ; https://www.polar.com/us-en/vantage/v3 ; https://www.polar.com/us-en/grit-x2-pro ; https://www.polar.com/us-en/loop (accessed 2026-10-11).
24. Polar support, wrist ECG. https://support.polar.com/en/wrist-ecg (accessed 2026-10-11). Not for medical or diagnostic use.
25. Polar 360 for business and Polar for Business. https://www.polar.com/en/business/polar-360 ; https://www.polar.com/en/business (accessed 2026-10-11). B2B build-on-SDK-or-API positioning; contact form, no published price.
26. Polar Team Pro API documentation. https://www.polar.com/teampro-api/ (accessed 2026-10-11). About 1 request per second.
27. Polar BLE SDK Known Issues. https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/KnownIssues.md (accessed 2026-10-11). H10 disconnects 45 seconds after removal from the strap.
28. openFDA 510(k), PMA and registration searches for "polar electro." https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm (queried 2026-10-11). No records.
