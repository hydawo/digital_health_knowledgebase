# Beiwe

## Quick Facts

| Field | Details |
|---|---|
| Organization | Onnela Lab, Harvard T.H. Chan School of Public Health |
| Category | Open-source smartphone digital phenotyping platform (passive sensing + active EMA) |
| Current status | Active, commits to `beiwe-backend` and `beiwe-ios` observed as recently as Jan, Feb 2026 |
| Platforms/devices | Native iOS and Android apps ("Beiwe2") |
| Open source | Yes, BSD-3-Clause across backend, iOS, and Android repos |
| Hosting/deployment | Self-hosted on AWS (own account), or managed via the Beiwe Service Center (BSC) |
| Pricing model | Software free; self-hosting incurs AWS costs; BSC is a paid managed service with study-specific quoted pricing |
| Last verified | 2026-09-03 (third pass: wiki and Forest documentation) |

## Summary

- Beiwe is Harvard's open-source smartphone platform for high-throughput digital phenotyping, developed and maintained by the Onnela Lab. It pairs a configurable iOS/Android data-collection app with a Django/AWS backend for study management, and hands off analysis to a companion Python package, **Forest**, that the same lab develops. The platform is BSD-3-licensed end to end, so a technically capable research team can self-host on its own AWS account at zero licence cost, or use the **Beiwe Service Center (BSC)**, the Onnela Lab's own managed-hosting service, to avoid running the infrastructure themselves.

- This knowledge base's owner works professionally with the Beiwe Service Center. The assessment below is written to the same evidence standard as every other profile in this knowledge base: documented facts only, vendor/lab claims held to "Reported" unless independently corroborated, and limitations stated as plainly as strengths.

## Products / Platform Architecture

- **Beiwe2 apps** (iOS, Android), passive sensor collection plus configurable surveys/EMA, available on the App Store / Play Store for use with open-source backend deployments, or sideloaded.
- **beiwe-backend**, Django application deployed on AWS (S3 for raw data storage, EC2 for app servers, Elastic Beanstalk for scaling, RDS/PostgreSQL for the study database). Provides the researcher-facing study-management web portal.
- **Forest**, a separate, Onnela-Lab-maintained Python package (BSD-3) that turns Beiwe's raw passive data into processed/summary statistics (mobility metrics, sociability metrics, etc.). Forest can run standalone against exported raw data, or be invoked from within a Beiwe backend deployment to generate on-demand daily/hourly summaries stored back in the study's relational database.
- **Beiwe Service Center (BSC)**, a paid, Onnela-Lab-run instance of the same open-source stack. Studies run on the lab's own production AWS deployment rather than the researcher's; BSC adds study design consultation, IRB-documentation assistance, a beta-testing phase, participant support, and final analysis using production Forest packages.

### Beiwe and Forest, relationship, stated precisely

- Beiwe and Forest are **separate open-source repositories with separate release cadences**, developed by the same lab, designed to be used together but not bundled as one artifact. Beiwe collects and stores raw sensor and survey data; Forest is the analysis layer that turns that raw data into derived, research-usable metrics (e.g., mobility statistics from GPS, sociability statistics from call/text logs). A study can use Beiwe without Forest (working directly from raw exports) or use Forest against Beiwe data collected years earlier. The BSC packages both together as part of its managed service, but that is a service-delivery choice, not evidence that the two are architecturally fused. **Verified** from `onnela-lab/beiwe-backend` and `onnela-lab/forest` READMEs and the Onnela Lab's own platform page.

## Sensors and Data Streams

- Every Module 2 profile uses the same table so platforms can be compared row by row. Rows are the passive streams named in `CLAUDE.md`. "Yes" and "No" are used only where a primary source says so; "Unclear" means nothing current was verified, and "No (OS)" means the operating system does not expose the stream to any third-party app. Confidence and sources are stated under the table. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Stream | Android | iOS | Raw or derived | Sampling configurable | Notes |
|---|---|---|---|---|---|
| GPS / location | Yes | Yes | Raw. Timestamp, latitude, longitude, altitude, accuracy. | Yes. On and off durations, plus a location fuzzing parameter. | GPS is typically accurate to 10 to 20 m per the wiki. Fuzzing offsets the true position for privacy. |
| Accelerometer | Yes | Yes | Raw. x, y, z. | Yes. On and off durations and a rate setting. | The wiki warns that Android rate settings map to a handful of real frequencies and vary by device. Test a few handsets before fixing values. |
| Gyroscope | Yes | Yes | Raw. x, y, z. | Yes. On and off durations and a rate setting. | Same Android rate caveat as the accelerometer. |
| Magnetometer | No | Yes | Raw, uncalibrated field in x, y, z. | Yes. On and off durations. | iOS only. The wiki invites an issue on the Android repo for anyone who needs it. |
| Barometer | No | No | Not applicable | Not applicable | Not a Beiwe stream. |
| Ambient light | No | No | Not applicable | Not applicable | Not a Beiwe stream. |
| Proximity | No | Yes | Event. Near user or not near user. | No | iOS only, and only while the app is open. |
| Device motion / activity recognition | No | Yes | Derived by iOS. Roll, pitch, yaw, rotation rate, gravity, user acceleration, magnetic field. | Yes. On and off durations. | The DeviceMotion composite stream. No OS activity-recognition labels are collected on either platform. |
| Screen state | Yes | Conflicting documentation | Event. Screen on and off on Android; locked and unlocked on iOS. | No | The Supported Data Streams page lists Power State as Android only. The older Passive Data page shows iOS Power State events with lock, unlock and battery level. Recorded as a documentation conflict, see Open Questions. |
| App usage | No | No | Not applicable | Not applicable | Screen-on time is the only usage proxy. No per-app usage on either platform. |
| Battery / charging | Yes | Conflicting documentation | Event. Plugged, unplugged, and on iOS a battery level per the older page. | No | Same conflict as screen state. |
| Network / connectivity | No | Yes | Event. Wi-Fi, cellular or unreachable. | Periodic check | The Reachability stream, described by the wiki as partially deprecated after iOS changes. |
| Wi-Fi | Yes | No | Raw scan. Hashed router MAC, frequency, RSSI. | Yes. Periodic timer. | Intended as an indoor-mobility proxy. Apple restrictions prevent the same on iOS. |
| Bluetooth | Yes | No | Raw scan. Hashed MAC addresses of nearby devices. | Yes. Timer aligned to the hour. | The wiki calls its limitations complex. Android 6 and later stop reporting true MAC addresses. |
| Calls (metadata) | Yes | No (OS) | Metadata. Hashed number, call type, duration. | No | Unavailable by design on iOS. |
| SMS (metadata) | Yes | No (OS) | Metadata. Hashed number, direction, message length. | No | Unavailable by design on iOS. MMS included. |
| Keyboard | No | No | Not applicable | Not applicable | Not a Beiwe stream. |
| Audio / microphone | Yes | Yes | Raw recordings, through audio survey items only. | Scheduled as a survey | Active, not passive. No continuous audio capture. |
| Notifications | No | No | Not applicable | Not applicable | Not collected as a data stream. Survey notification and heartbeat history is held server-side and is available through the API. |
| Device information | Yes | Yes | Identifiers file at enrolment. Device OS and version, manufacturer, model, app version, hashed phone number and MAC. | Not applicable | Written once at enrolment and again if the participant re-enrols. |

**Verification.** Verified 2026-09-03 from the Beiwe wiki's Supported Data Streams page and its Passive Data page (file layouts and per-stream descriptions), read from a clone of the `onnela-lab/beiwe-backend` wiki. The two pages disagree on whether Power State exists on iOS, and the older page carries a banner saying it may be out of date; both readings are recorded rather than resolved. Sampling schedules are duty cycles set per study in the device settings. Data are written as timestamped CSV files per stream per hour.

## Derived Metrics / Analytics

- Forest is the Onnela Lab's Python analysis package for Beiwe data, released separately under BSD-3. Its documentation site is forest.beiwe.org. Verified 2026-09-03 from that site.
- Subpackages and what each produces:

| Subpackage | Input stream | Output | Notes |
|---|---|---|---|
| `jasmine` | GPS | Hourly or daily mobility summaries from imputed trajectories | Sparse online Gaussian process imputation of missing segments (Barnett and Onnela 2020). Optional OpenStreetMap places of interest. Refuses to run when fewer than 5% of files hold 60 s of data, a threshold the caller can change. |
| `willow` | Calls and texts | Daily or hourly communication summaries | Android only, since iOS exposes no logs. |
| `oak` | Accelerometer | Walking time, steps and cadence per hour or day | Walking recognition with published default tuning (step frequency 1.4 to 2.3 Hz, minimum 3 s of walking). |
| `sycamore` | Survey timings, survey answers, audio recordings | Survey delivery, opening, submission and per-question timing summaries | Needs the study configuration export, survey history and interventions files from the backend to estimate deliveries. |
| `poplar` | All streams | Readers, time and timezone helpers, the `data_streams.csv` table of which streams exist per OS | Utility layer used by the others. |
| `bonsai` | None | Simulated GPS and call or text data | For testing pipelines, not for analysis. |

- `jasmine` daily summary statistics, as documented (the hourly variant uses minutes rather than hours):

| Variable | What it measures |
|---|---|
| Observed duration, day and night | Hours the GPS was on, overall and split 8 am to 8 pm and 8 pm to 8 am. Quantifies missingness. |
| Home time | Hours at the most-visited significant location between 8 pm and 8 am across follow-up. |
| Distance traveled | Sum of flight lengths, km. |
| Radius of gyration | Time-weighted mean distance of visited places from their centroid, km. |
| Maximum diameter | Largest distance between any two places visited, km. |
| Maximum distance from home | km. |
| Number of significant locations | Pauses of 15 minutes or more at least 50 m apart, clustered by k-means. |
| Total flight time, average and SD of flight length and duration | Flights are straight-line movements with no pause or direction change; defaults w = r = 10 m on 10 s samples. |
| Total pause time, average and SD of pause duration | A pause is under r metres of movement in 30 s. |
| Significant location entropy | Shannon entropy of time shares across significant locations. |
| Minutes of GPS data missing | Per day. |
| Physical circadian rhythm, and its weekday or weekend stratified form | Routine score in [0, 1] after Canzian and Musolesi 2015, 30-minute bins. |

- `willow` outputs per day or hour: counts of incoming, outgoing and missed calls and of unique callers in each direction, total call minutes in and out, sent and received SMS and MMS counts, unique correspondents, characters sent and received, and two reciprocity counts.
- `oak` outputs per day or hour: walking time in seconds, steps, cadence.
- `sycamore` outputs: submissions and deliveries with time to open, time to submit and survey duration; per-question answers with time spent and number of answer changes; a summary that flags when submitted surveys exceed estimated deliveries, which happens after manual resends or configuration changes.
- Forest can run against exported raw data or from inside a backend deployment to write daily and hourly summaries back to the study database. The lab frames analysis, not collection, as the bottleneck in digital phenotyping; Reported.
- `bonsai` and `poplar` were not previously recorded in this profile; the `oak` step-count and walking-recognition methods are validated in Straczkiewicz 2023 (two versions) in the Module 2 catalogue.

## Active Data Collection

- Surveys and EMA are scheduled per study in the backend portal. The Beiwe wiki holds a survey JSON specification, a skip-logic (branching) specification and a survey-scheduling and push-notification specification, so branching and scheduled delivery are documented platform features (Verified 2026-09-03 from the wiki page list; the specification contents were not read this pass).
- Audio survey items record participant speech as a file; `sycamore` reports their submission frequency and duration but does not process the audio.
- Three active data streams reach the researcher: `survey_timings` (per-question timing, the preferred source), `survey_answers` (final submissions, a fallback because timing files are not always uploaded) and `audio_recordings`. Verified 2026-09-03 from the Forest `sycamore` documentation.
- Survey notifications and their resends are tracked server-side with sent, received and check-in times per notification, visible on a per-participant Notification History page and through the API. Verified 2026-09-03 from the wiki's notification page.

- Question types include slider, radio button, checkbox, numeric and free-text open response, and information blocks; branching may only key off slider, radio and numeric answers. A survey can be shown once immediately on enrolment.
- Audio surveys carry a researcher-written prompt on the recording screen; the wiki suggests text asking participants not to say names or places. Image surveys exist as a stream (`beiwe_image_survey_bytes` in the summary statistics), though no wiki page describing them was read.

## Researcher and Study Management Features

- Web-based study administration portal (part of `beiwe-backend`): study creation, device/participant registration, survey configuration, data-stream configuration (sampling rates, upload behavior). Multi-study support exists in that a single backend deployment can host multiple studies. Adherence/data-flow monitoring, audit logging, and role-based admin accounts were referenced in the repo/wiki but not independently verified in depth this session.

### From the wiki's Research Administration Manual and dashboard page (added 2026-09-03, Verified)

- Portal tasks for collaborators: create participant IDs and temporary passwords, create and deploy written surveys, audio surveys and image surveys, download data. Study admin and site admin roles exist; enabling Forest and editing a study need one of them.
- Survey scheduling has three modes. Absolute (an exact date and time in the study time zone, delivered on registration if the participant joins later), relative (days before or after a per-participant intervention date, set on the participant page), and a repeating weekly schedule. The study time zone must be set before any survey is sent, since changing it resets surveys.
- Branching logic is built from NOT, OR and AND blocks and single conditionals over slider, radio-button and numeric open-response questions. Contradictory logic saves without error; only unparseable references fail. Randomized question selection (with or without replacement) exists but disables branching in that survey.
- Survey question text accepts Unicode for other languages, but the app's own interface strings are English only.
- Data monitoring: a study dashboard shows data volume per stream per participant per day, and the wiki recommends checking it once or twice a week. The dashboard is being deprecated in favour of Tableau, fed by the summary-statistics endpoints above.
- Forest runs per study once enabled, through a Create Forest Tasks page, with tasks picked up by a cron job about every five minutes.
- Per-participant pages show the latest heartbeat, the notification token status and the notification history.

## Data Access and Export

- Raw data lands in S3 (self-hosted) or the BSC's AWS storage, and is described as being made available to researchers, including "access to raw data and summary metrics" under the BSC service model. Data is encrypted on-device before upload, in transit (RSA-AES hybrid), and at rest with a study-specific master key; phone numbers and other identifiers are hashed (SHA-256 + PBKDF2) with device-specific salts that are never uploaded. **Verified** from the `beiwe-backend` README's security section. Bulk/API-level export mechanics, exact file formats, and retention defaults were not independently re-verified against current documentation this session.

### From the wiki (added 2026-09-03, Verified)

- Raw data are downloaded per participant, per stream and per date range either from the study web page or through the Data Download API. The API keeps a registry of files already fetched and downloads only new data on each call. A reference script, `data_access_api_reference/download_data.py`, needs an access key and secret key from the portal's Manage Credentials page and the deployment URL.
- Downloads use a separate 64-character key pair from the portal login, required on every download because data are encrypted on the server.
- Before data reach the API they are batched. A processing manager checks for new uploads every 6 minutes; rows are sorted by timestamp, given a human-readable UTC column beside the millisecond timestamp, binned by hour, and deduplicated. Stream-specific fixes are applied (survey ID inserted into survey timings rows, call log columns corrected, Wi-Fi scan timestamps inserted per row, Android app log structured).
- Uploads default to Wi-Fi only in most studies. Data buffer on the phone until Wi-Fi is available, so the dashboard lags for participants without it. Studies can choose cellular upload, which the wiki says makes uploads near real-time.
- A summary-statistics API returns one JSON row per participant per day with two families of fields. Data-quantity fields give decrypted bytes per stream per day (accelerometer, ambient audio, app log, Bluetooth, calls, device motion, GPS, gyro, identifiers, image survey, iOS log, magnetometer, power state, proximity, reachability, survey answers, survey timings, texts, audio recordings, Wi-Fi). Forest fields carry the jasmine, willow and sycamore daily statistics. Filters are start and end date, participant IDs, fields and limit; queries over 60 seconds time out. Endpoints: `/tableau/summary-statistics/v1/<study_object_id>` and `/tableau/participant-table/v1/<study_object_id>`, with Tableau Web Data Connector wrappers, authenticated by the same key pair in `X-Access-Key-Id` and `X-Access-Key-Secret` headers. An OpenAPI specification sits at `api/tableau_api/spec.yaml` in the backend repository.
- A study can be configured as a "production study", after which researchers can download only processed outputs from the analysis pipeline rather than raw GPS. This is the higher-security setting.
- Retention defaults and deletion procedures are not stated on the pages read.

## APIs, SDKs, and Extensibility

- Fully open source (BSD-3) across backend, iOS, and Android, the strongest extensibility position of any platform in this module by definition: a research team can fork and modify any layer. **Updated 2026-08-25 (second pass):** a direct fetch of `onnela-lab/beiwe-backend`'s repository structure confirms a `data_access_api_reference` directory exists in the codebase, indicating some form of documented data-access API is part of the backend. However, the README content retrieved this session did not detail the endpoint functionality, so whether this constitutes a public, researcher-facing REST API comparable to competitors' documented APIs, or an internal/administrative interface, remains **Unclear** rather than resolved, this is a narrower open question than the prior "no API identified" framing, not a fully closed one.

- ~~Whether `data_access_api_reference` is a public researcher-facing API was Unclear.~~ Resolved 2026-09-03 from the wiki. It is: `download_data.py` (raw data with an incremental registry) and `other_api_reference_script.py` (every API the platform provides, kept updated by the developers) are documented reference scripts, and the summary-statistics endpoints have an OpenAPI specification. Credentials are issued per researcher from the portal.

## Deployment and Infrastructure

- **Self-hosted**: AWS only (S3, EC2, Elastic Beanstalk, RDS/PostgreSQL). Requires "moderate AWS and Python expertise," per the backend README. No documented support for non-AWS clouds.
- **Managed (BSC)**: runs on the Onnela Lab's own AWS deployment; researchers do not manage infrastructure. Pricing is quote-based, computed from three study-specific variables (see Pricing).
- Backend uses rolling releases; mobile apps use semantic versioning.

- The open-source version is "provided as-is" with no ongoing technical support from the Onnela Lab, per the wiki's FAQ; the two supported routes are self-deployment from the wiki instructions (single server or server cluster) or paid help from the platform's contract developers, Zagaran. Verified 2026-09-03.
- Adding Forest to a self-hosted deployment means installing the data-processing requirements on the worker server and restarting processing; the wiki has a Forest Setup page.

## Participant Experience

- Native app on the participant's own or a study-provisioned phone; background passive collection plus scheduled surveys. Battery impact, permission burden, and BYOD-vs-provisioned suitability were **not independently benchmarked** this session, this is a real gap given how decisive these factors were for wearables in Module 1, and should be treated as an open question pending direct testing or BSC/Onnela Lab documentation review.

### The background-execution constraint, and `heartbeat` (added 2026-08-31)

- Both iOS and Android apply power-saving limits to background apps, so **no app can run in the background indefinitely, it must be returned to the foreground periodically for background sensor collection to persist**. Beukenhorst et al. (2022), analysing three Beiwe ALS studies, state the consequence bluntly: *"longitudinal passive data collection without active data collection is not possible."* This is an OS-level constraint applying to every smartphone sensing platform, not a Beiwe-specific defect, and it means a genuinely zero-touch passive protocol does not exist on any platform in this module. **Verified**, see [`../../module-03-applied-studies/profiles/beiwe-als-adherence.md`](../../module-03-applied-studies/profiles/beiwe-als-adherence.md).

- Beiwe subsequently added a **`heartbeat`** mechanism (also called *keepalive*) that directly addresses this: a **scheduled server-side push notification** whose purpose is to wake the app so background collection resumes. Development timeline, from the `onnela-lab/beiwe-backend` public commit history (**Verified**):

| Date | Change |
|---|---|
| 2024-01-12 → 2024-02 | Built and tested on the `push-notification-heartbeat` branch; migration, cron task, participant logging, and heartbeat messages added |
| 2024-04-08 | **Heartbeat message and interval made configurable per study** |
| 2024-05-14 | Fields added for Android push notification support |
| 2024-05-15 | Participant page updated to always display the latest heartbeat datapoint |
| **2024-05-29** | **Experiment flag removed, heartbeat globally enabled** |
| 2024-06-06 | Heartbeat API endpoint implemented |
| 2024-08-29 | Performance fix for retrieving latest app heartbeat |

- **What this does and does not change.** The underlying OS behaviour is unchanged. Heartbeat substitutes a *server-triggered* wake for a *participant-initiated* one, so the dependency on periodic foregrounding remains, but the trigger no longer has to be an active research task the participant must complete. A **low-active-burden** protocol is therefore materially more viable on Beiwe from mid-2024 onward than the published literature (all of which predates the feature) can show; a **zero-touch** protocol still is not.

- **Consequence for every Beiwe completeness figure in this knowledge base:** the two main sources, Beukenhorst et al. 2022 (data 2016 to 2021) and Kiang et al. 2021 (data 2015 to 2018), are both **pre-heartbeat**, and should be read as **lower bounds on data yield**, not as current platform performance. The magnitude of the improvement is not publicly published; logged as Tier 14 Q106 in [`../../shared/unresolved-questions.md`](../../shared/unresolved-questions.md).

- Whether comparable server-triggered keepalive mechanisms exist and are enabled by default on RADAR-base, mindLAMP, AWARE, Avicenna, MetricWire, m-Path or CARP was **not established**, a genuine and currently undocumented differentiator, logged as Tier 14 Q107.

### How heartbeat and survey resends work (added 2026-09-03, Verified from the wiki)

- The app pings the server every 5 minutes. The wiki notes an August 2026 iOS bug that makes the ping more frequent than that.
- The KeepAlive timer is configured per study in Device Settings, with a duration and a message. If the app has not checked in within the duration, the server sends the message by push notification. The default duration is 1 hour and the default message is "Beiwe may not be running correctly, please open the Beiwe app."
- The heartbeat history is available through the data access API and is described by the wiki as a rough proxy for when the app was running, with the caveat that it cannot cover periods without coverage.
- Survey notifications on iOS can be cleared by the participant before the app receives them. The backend tracks sent, received and check-in times for every notification, resends an unacknowledged notification after a configurable interval, and lets a researcher resend manually per participant.
- The wiki's own warning: the fastest way to make participants uninstall the app is to bombard them with notifications.
- Notification delivery depends on a token the device must periodically send to the server; its status is shown on each Participant Page, and a missing token nearly always means the app is not running or has been uninstalled.

### From the wiki (added 2026-09-03, Verified)

- Everything in the app sits behind a login with a minimum 6-character password, except the "Call My Clinician" button and the survey reminders. The app logs out after a configurable period of inactivity.
- A forgotten password is reset by phoning the study's research assistant (the collaborator's staff, not the Onnela Lab), identifying by Beiwe ID only, and receiving a temporary password.
- One participant ID registers on one phone at a time; a second phone with the same ID is refused. Reinstalling the app on a new phone regenerates the on-device key, so hashed identifiers change and a new identifiers file is written.
- Data upload over Wi-Fi only is the usual configuration, chosen to spare participants data charges; the trade-off is upload delay, and in one profiled study a participant who never joined Wi-Fi lost all data (see [`../../module-03-applied-studies/profiles/beiwe-schizophrenia-state-clinic-pilot.md`](../../module-03-applied-studies/profiles/beiwe-schizophrenia-state-clinic-pilot.md)).

## Privacy, Security, and Compliance

- **Verified**: multi-stage encryption (on-device, in-transit RSA-AES hybrid, at-rest with study master key) and identifier hashing, per the backend README.
- **Updated 2026-08-25 (second pass):** a direct fetch of `onnela-lab/beiwe-backend`'s README surfaces the platform's own compliance framing precisely: it states the system "may interact with laws covering PII or PHI like HIPAA in the United States", an acknowledgment that HIPAA-relevant data may pass through the system, **not a HIPAA-compliance certification claim**. No mention of GDPR, SOC 2, or ISO certification was found in this fetch. This is a materially more precise finding than "not independently verified" but does not change the conclusion: no compliance certification is documented, and none should be inferred.
- GDPR/DPA, SOC 2, and IRB-support specifics remain **not independently verified against current documentation**. Do not infer regulatory compliance from "Harvard" as an institutional affiliation, CLAUDE.md's instruction not to infer compliance from general claims applies here as much as to any vendor.
- Self-hosting gives a research team full data custody (the Onnela Lab is never in the data path); using the BSC puts the Onnela Lab's AWS deployment in the data path, which is a materially different governance posture and should be weighed like any other vendor-hosted arrangement.

### From the wiki's privacy page and IRB FAQ (added 2026-09-03, Verified)

- Identity: participants are known to the platform only by a random 8-character ID; names and contact details stay with the collaborating site behind its own firewall.
- Indirect identifiers (call and text phone numbers, Wi-Fi and Bluetooth MAC addresses) are replaced on the phone by PBKDF2 and SHA-256 surrogates using a per-installation key that is never uploaded, so the same number maps to the same 88-character string on one phone and cannot be reversed by the server.
- Encryption chain: the device holds the public half of a 2048-bit RSA key from registration, encrypts a per-use AES key with it, and the server re-encrypts received data under a per-study master key before storage on S3. Connections are TLS. The wiki cites Amazon's HIPAA compliance whitepaper for EC2 and S3 and notes that hosted studies' data sit in the Onnela Lab AWS account, accessible only to Onnela and authorised staff.
- GPS and audio recordings are named by the Onnela Lab IRB as the two streams that can contain identifying information; GPS fuzzing and the production-study setting are the mitigations.
- Portal passwords need 8 or more characters with lower case, upper case, a digit and a special character. There is no account lockout after failed attempts (on the feature request list), and the portal timeout is longer than 15 minutes; data downloads need the separate 64-character credential pair.
- None of this is a certification. HIPAA applicability is acknowledged, GDPR, SOC 2 and ISO are not mentioned anywhere read.

## Pricing

- **Software**: free, BSD-3-Clause, no licence fee under either deployment path.
- **Self-hosting**: AWS infrastructure costs only (S3/EC2/RDS), which scale with study size and are not separately published, this is a "your AWS bill" cost, not a Beiwe-specific fee.
- **Beiwe Service Center**: **Verified 2026-08-25 (second pass, resolving unresolved-question #85)**, a direct fetch of the BSC's own overview page (`hsph.harvard.edu/research/onnela-lab/beiwe-service-center/`) now returns actual rate figures, not only the methodology: **Fixed Monthly Cost: $1,937/month**; **Variable Cost: $6 per Active Participant Month**. The page's own worked examples show total contract costs ranging from **$24,144 to $27,564** depending on study duration and participant-months. This resolves what was, as of 2026-08-24, the module's clearest "methodology published, rates not" gap, Beiwe now has among the more transparent pricing of any platform in this module. (Rates may change over time; re-verify before using in a real budget.)

## Research Evidence and Validation

- Beiwe has been used across numerous published studies, including deployments at Harvard-affiliated teaching hospitals, per the Onnela Lab's own platform page. This session did **not** conduct the kind of systematic published-use-count or methods-paper survey CLAUDE.md's "Evidence of use" section calls for; that remains an open task (see Open Questions). As an infrastructure platform rather than a measurement device, "validation" here is less about signal accuracy (Module 1's concern) and more about published, reproducible use, which was not exhaustively catalogued this session.

## Strengths

- Fully open source across every layer (backend, iOS, Android, and the Forest analysis package) under a permissive BSD-3 licence, a research team can audit, fork, and modify anything.
- Two genuinely distinct deployment paths, free self-hosted vs. paid managed (BSC), giving smaller or infrastructure-constrained teams a route that doesn't require in-house AWS/Django expertise.
- Documented, specific, multi-stage encryption and identifier-hashing design, unusual in this module for how concretely it is written into the public README rather than asserted only in marketing copy.
- Native iOS and Android apps under active, visible development (recent commit activity in both mobile repos).
- A dedicated, purpose-built analysis package (Forest) rather than leaving derived-metric computation entirely to the researcher.

## Limitations

- Self-hosting requires real AWS/Django/Python engineering capacity; this is a genuine adoption barrier relative to fully managed commercial platforms (Avicenna Research, MetricWire) in this module.
- ~~Whether the data access API is a documented researcher-facing API was not resolved.~~ Resolved 2026-09-03; it is documented, with reference scripts and an OpenAPI specification for the summary-statistics endpoints. Raw data still arrive as per-stream hourly CSV rather than through a query interface.
- ~~iOS/Android feature and sampling parity was not independently verified this session and should not be assumed.~~ Resolved 2026-09-03; the stream table records the per-OS availability. Calls, SMS, Wi-Fi and Bluetooth are Android only; magnetometer, proximity, device motion and reachability are iOS only.
- GDPR/DPA/SOC 2 compliance posture remains undocumented; the backend README's own language ("may interact with laws covering PII or PHI like HIPAA") is an acknowledgment of applicability, not a certification claim. Do not infer compliance from Harvard's institutional affiliation.
- ~~BSC pricing is not public; every study needs a quote.~~ **Resolved 2026-08-25**: BSC publishes actual rate figures ($1,937/month fixed + $6/Active Participant Month variable) on its own overview page, see Pricing above.
- Branching logic and scheduling are documented in wiki specifications not yet read in full; the Forest catalogue is now recorded; bulk-export file formats are per-stream hourly CSV per the wiki, and the Data Download API page was not read this pass.

## Best-Fit Use Cases

- Studies where full data custody, algorithmic transparency, and freedom to modify the collection app are priorities (self-hosted path).
- Teams that want an established, actively maintained open-source stack but prefer not to run their own AWS infrastructure (BSC path).
- Research questions centered on GPS mobility and communication-log sociability metrics, where Forest's existing analysis routines are directly applicable.

## Poor-Fit Use Cases

- Teams needing a no-code, point-and-click study builder with a polished commercial dashboard and immediate third-party integrations (see Avicenna Research, MetricWire, m-Path for that profile shape).
- Studies requiring real-time integration with external systems. The documented API serves downloads and daily summary statistics with a 6-minute batching cycle, not streaming.
- Very small pilots where BSC's quote-based pricing model is disproportionate to study size (self-hosting may be more appropriate, if AWS/Django capacity exists).

## Open Questions

- *(Directed to: Onnela Lab / Beiwe Service Center, https://beiwe.hsph.harvard.edu, hsph.harvard.edu/research/onnela-lab)*

- ~~Does the `data_access_api_reference` directory in `beiwe-backend` document a public, researcher-self-service REST API, or an internal/administrative interface only?~~ Resolved 2026-09-03, see Data Access and Export.
- ~~What are the exact iOS-vs-Android differences in passive-stream sampling and background execution?~~ Resolved 2026-09-03 from the wiki, see the stream table. One conflict remains: whether Power State (screen and charging events) exists on iOS. The Supported Data Streams page says no, the older Passive Data page shows iOS events.
- ~~What is the full per-metric catalog within Forest's `jasmine` (mobility), `willow` (communication/sociability), and `sycamore` (survey) subpackages?~~ Resolved 2026-09-03 from forest.beiwe.org, see Derived Metrics. How the metrics are versioned across releases is still open.
- What GDPR/DPA, SOC 2, or comparable compliance documentation exists for BSC-hosted studies specifically (as distinct from self-hosted deployments where the researcher is the data controller)?
- ~~What are actual BSC rate figures?~~ **Resolved 2026-08-25**, see Pricing above.
- What published, systematic count of Beiwe-based peer-reviewed studies exists (this session did not attempt an exhaustive literature count)?

## Key Links

- Official site / Onnela Lab platform page: https://hsph.harvard.edu/research/onnela-lab/digital-phenotyping-and-beiwe-research-platform/
- Beiwe Service Center: https://beiwe.hsph.harvard.edu/
- Backend repository: https://github.com/onnela-lab/beiwe-backend
- iOS app repository: https://github.com/onnela-lab/beiwe-ios
- Android app repository: https://github.com/onnela-lab/beiwe-android
- Forest (analysis package): https://github.com/onnela-lab/forest
- Beiwe wiki (researcher and developer pages): https://github.com/onnela-lab/beiwe-backend/wiki
- Forest documentation: https://forest.beiwe.org/en/latest/
- Beiwe/Forest documentation site (older): https://jponnela.com/bf20/

## Sources

1. Onnela Lab, "Digital Phenotyping and Beiwe Research Platform." https://hsph.harvard.edu/research/onnela-lab/digital-phenotyping-and-beiwe-research-platform/ (accessed 2026-08-24). **Primary.** Data types, iOS/Android support, architecture summary, BSD-3 licence, self-host vs BSC paths.
2. `onnela-lab/beiwe-backend` README. https://github.com/onnela-lab/beiwe-backend (accessed 2026-08-24). **Primary.** Django/AWS architecture, encryption design, identifier hashing, BSD-3 licence, related repos.
3. `onnela-lab/forest` repository. https://github.com/onnela-lab/forest (accessed 2026-08-24). **Primary.** Forest's purpose and relationship to Beiwe.
4. Beiwe Service Center overview. https://www.beiwe.org/beiwe-service-center-overview/ and https://hsph.harvard.edu/research/onnela-lab/beiwe-service-center/ (accessed 2026-08-24). **Primary.** BSC service scope, pricing methodology (fixed + variable fee structure).
5. `onnela-lab` GitHub organization (activity check). https://github.com/onnela-lab (accessed 2026-08-24). Recent commit activity across `beiwe-backend` (Jan 2026) and `beiwe-ios` (Feb 2026) used to support "Active" status.
6. `onnela-lab/beiwe-backend` repository structure and README (second-pass re-fetch). https://github.com/onnela-lab/beiwe-backend (accessed 2026-08-25). **Primary/Verified.** Confirms `data_access_api_reference` directory exists; confirms README's precise HIPAA-applicability language ("may interact with laws covering PII or PHI like HIPAA"), distinct from a compliance certification claim.
7. `onnela-lab/forest` README (second-pass re-fetch). https://github.com/onnela-lab/forest (accessed 2026-08-25). **Primary/Verified.** Confirms subpackage structure: `jasmine` (GPS mobility metrics), `willow` (call/text communication metrics), `sycamore` (survey-completion metrics).
8. Beiwe Service Center overview (second-pass direct fetch). https://hsph.harvard.edu/research/onnela-lab/beiwe-service-center/ (accessed 2026-08-25). **Primary/Verified.** Actual rate figures: $1,937/month fixed + $6/Active Participant Month variable; worked examples totaling $24,144, $27,564.
9. Beiwe wiki, "Supported Data Streams" and "Passive Data" pages, read 2026-09-03 from a clone of the `onnela-lab/beiwe-backend` wiki repository. **Primary/Verified.** Per-stream OS availability, configurability, file layouts, the GPS fuzzing parameter, the Android sampling-rate caveat, and the Power State documentation conflict.
10. Beiwe wiki, "Survey Notification Resends, The App Heartbeat, and KeepAlive Notifications," read 2026-09-03. **Primary/Verified.** Five-minute heartbeat, one-hour default KeepAlive timer and message, survey resend mechanics, notification token.
11. Forest documentation, forest.beiwe.org (jasmine, willow, oak, sycamore, poplar, bonsai and passive-data pages), read 2026-09-03. **Primary/Verified.** Subpackage catalogue and every summary statistic named in Derived Metrics.
12. Beiwe wiki, "Data Download API," "Tableau API," "Data batching and indexing details" and "Forest Setup," read 2026-09-03. **Primary/Verified.** Download API and registry, credential model, summary-statistics endpoints and field list, batching cadence and guarantees, Forest enablement.
13. Beiwe wiki, "Beiwe Data Privacy and Security," "IRB FAQs," "FAQs for Prospective Beiwe Users," "Monitoring Data Using the Dashboard" and "Beiwe Research Administration Manual" (old-wiki folder), read 2026-09-03. **Primary/Verified.** Identifier handling, encryption chain, participant authentication, portal password rules, survey scheduling and branching, dashboard deprecation, open-source support terms.
