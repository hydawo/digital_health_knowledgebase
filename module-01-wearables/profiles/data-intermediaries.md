# Data Intermediaries and Aggregation Layers (cross-cutting)

## Why this file exists

Nine times out of ten, the practical question "how do I get wearable data into my study?" is not
answered by a vendor API directly. It is answered by a middle layer that either (a) supplies the
study-operations tooling the device vendors do not, or (b) normalizes several vendor APIs behind
one schema.

These are not wearable ecosystems, so they do not get the full profile template. But omitting them
would misrepresent how wearable research is actually done, and the choice of intermediary is often
a bigger determinant of study feasibility than the choice of device.

**Confidence caveat for this whole file:** most entries here were characterized from vendor
marketing pages and secondary sources rather than deep primary documentation review. Treat
everything below as **Reported** unless explicitly marked otherwise, and verify before selecting.

**Last verified:** 2026-08-21; Fitabase, Labfront, Fitrockr, Terra and Thryve pricing and access terms re-verified 2026-10-10; those five corrected against their vendor fact records 2026-10-22 (vendor fact record; records judged 2026-10-11 for Labfront and 2026-10-21 for the other four). Where an entry below cites `../../facts/<company>.yaml`, the confidence shown is the record's, not this file's blanket **Reported**.

**Dated context, 2026-10-10.** Two vendor routes these platforms sit on top of are closed to new direct applicants: Google is "not onboarding new projects" on the Google Health API and turns the legacy Fitbit Web API off on 30 October 2026, since moved to 2 November (`fitbit-google.md`), and Garmin has paused new Connect Developer Program access requests since spring 2026 (Corroborated; `garmin.md`). For a new study, an intermediary that already holds access is currently the main way to reach Garmin data. Terra is no longer one of them for new customers: since a page change between 2026-10-14 and 2026-10-21 its Garmin integration asks the customer to supply its own Garmin app credentials (Verified; `../../facts/terra.yaml`, developer_program_status). For Fitbit, Thryve's direct Google Health route (and Validic's) requires each customer's own Google Cloud project, verified app and CASA (Corroborated). Terra's docs say the opposite for Terra: Terra manages the Google Health credentials and the customer registers no Google app; Terra does not say whether its project has passed Google's restricted-scope review and CASA (Verified as to what Terra says; `../../facts/terra.yaml`). The Google Health app's writes to Apple Health and Health Connect give an on-device route with no Google Health API project (Corroborated; `../../facts/fitbit-google.yaml`, 2026-10-11). **Update 2026-10-21.** Google's notice was removed by 2026-10-19, so the Google Health API is apparently open to new projects again (Corroborated, no announcement). A study can apparently open its own project, with Google's restricted-scope review and, above 100 users, verification and CASA. The Garmin pause is unchanged.

---

## Category 1, Research operations platforms

These supply participant management, adherence monitoring, and de-identified export. They are what
a research team buys because Fitbit and Garmin do not provide it.

### Fitabase, **the incumbent for Fitbit/Garmin research**

| Field | Detail | Confidence |
|---|---|---|
| Supports | Fitbit (now Google Health, including the screenless Fitbit Air) and Garmin, including Garmin Index blood pressure monitor readings; study-controlled or participant-owned devices. A second Fitbit device on the same Google Health account interferes with collection | **Verified** (`../../facts/fitabase.yaml`, raw_streams) |
| Granularity | No raw accelerometer or PPG. Fitbit: heart rate every 3 to 15 seconds, sleep stages 30 seconds, minute-level steps, intensity, METs, calories, SpO2 and Active Zone Minutes, HRV 5-minute readings, hourly and daily totals. Garmin (API route): heart rate 15 seconds, stress 3 minutes, Pulse Ox minute level, 15-minute activity epochs. No GPS or location, by design | **Verified** (`../../facts/fitabase.yaml`, sampling_rates, raw_streams) |
| Garmin beat-to-beat | Two routes. Garmin API route: Enhanced BBI with a per-beat confidence flag, captured at the wrist **during sleep**, gen 4 or later sensors, a paid premium dataset. Garmin SDK route: participants sync through the Fitabase Engage app instead of Garmin Connect (2026-07-29 blog, App Store release notes); daytime coverage, rate, Enhanced versus legacy BBI and eligibility are not stated | API route **Verified**; SDK route **Corroborated** (vendor pages only; `../../facts/fitabase.yaml`, raw_streams [Garmin]) |
| History | Garmin: pre-connection data only if the participant turns on Garmin Connect's off-by-default Historical Data permission; no maximum look-back published. Fitbit / Google Health: whether pre-connection data can be pulled is not clearly documented; devices hold minute and second data only 5 to 7 days before syncing. Ask Fitabase | Garmin **Verified**; Fitbit **Unclear** (`../../facts/fitabase.yaml`, history_depth) |
| Study tooling | Monitoring dashboards, device battery and sync status, participant tagging, de-identified profiles, customizable data capture windows, unlimited batch exports | **Verified** |
| API and export routes | CSV from participant report pages and unlimited batch exports; the Fitabase API add-on (Daily Activity, Profiles, Sync and Batch Export endpoints, key-authenticated, customer projects only); the Aggregate Data API for bulk JSON or CSV; scheduled batch exports at most daily; webhooks on participant connection-status changes (2026-03-11). API reference and rate limits sit in a customer-only portal | **Verified** (`../../facts/fitabase.yaml`, export_routes, rate_limits) |
| Engage | Relaunched 2026-04-21 (branching logic, triggers, randomization, an AI flow builder). On 2026-10-21 the Engage pages still label the Mobile App and Wrist App "Preview · Summer 2026", while the Fitabase Engage iPhone app is live (version 1.6.8, 9 October). General availability is not stated; no Google Play listing found; no Engage price published | **Verified** (`../../facts/fitabase.yaml`, program_status) |
| Track record | Homepage: used in "over 1,100 research studies"; customers page: "900+ Institutions, 2500+ Studies" (both read 2026-10-21; the two figures disagree and neither gives a method); research library: "1650 publications have used Fitabase", last updated 5 October 2026 (read 2026-10-10) | **Reported** (vendor claims; counting methods not stated) |
| Pricing | **Not public.** "Custom Pricing for Every Study". Charged extras, all unpriced: the Fitabase API, automated batch exports, SMS messages and reminders (partly per message segment), the Aggregate Data API, Food and Weight exports, and Garmin Enhanced BBI. Custom development is capacity-limited, with a limited number of custom projects accepted each year. No minimum term in the public Terms. Contact hello@fitabase.com | **Verified** that it is non-public (`../../facts/fitabase.yaml`, api_platform_fees, quote_required, 2026-10-21) |
| Retention | On cancellation, identifiable information is deleted and backups expire on schedule, but Fitabase may keep using de-identified data. Accounts inactive more than 30 days may be closed. The 90-day post-collection deletion appears only in Fitabase's example IRB text, not in the Terms or Privacy Policy, so confirm it in the contract | **Verified** (`../../facts/fitabase.yaml`, retention_terms) |
| Compliance | FAQ: "the option to run your project completely de-identified". No page names HIPAA, a BAA or GDPR, and no customer DPA is published. Hosting is US only, on Microsoft Azure (region not stated). No ISO 27001 or SOC 2 claim of its own; the security page quotes Azure's certification against the superseded ISO/IEC 27001:2005. Small Steps Labs LLC (Fitabase) is **Active on the Data Privacy Framework registry** (EU-U.S., Swiss-U.S., UK Extension; non-HR data; self-assessment), with five recorded lapses, the latest 2026-09-07 to 2026-10-16 | **Verified** (`../../facts/fitabase.yaml`, baa, dpa, hipaa_statement, gdpr_statement, iso27001, soc2, data_residency, 2026-10-21) |
| Fitbit migration | Google turns off the Fitbit Web API on 2 November 2026 (moved from 30 October on 2026-10-23; Fitabase's pages still said 30 October on 2026-10-30). Reauthorization for the Google Health API opened in Fitabase on 15 October; links keep working through 30 November; it cannot be done programmatically. On 14 October, 29 of 40 exports were available from the Google Health API, 8 were "Transition delayed" (including Intraday Calories, Intraday METs and ECG Logs; Google Health ECG import is paused) and 3 classic sleep exports were Fitbit API only. On 19 October Fitabase extended all active Fitbit projects ending before 2027-01-01 to that date at no charge. The Fitabase API itself is unchanged | **Verified** (`../../facts/fitabase.yaml`, deprecations; recheck after 2 November) |

Fitabase is the single most important non-device entity in Module 1. If a study is using Fitbit and
does not have engineering capacity, Fitabase is effectively the default, and its (unpublished) cost
should be budgeted from the start. Note that Fitabase's Engage roadmap moves it toward the survey/
EMA territory of the Module 2 platforms, a convergence worth tracking.

Open question: does Fitabase execute a HIPAA BAA as standard? No page mentions HIPAA or a BAA
(re-checked 2026-10-21). Its de-identification framing suggests a deliberate strategy of staying
outside PHI, which is a different compliance posture from a BAA. **Not public, ask directly.**

### Labfront, published pricing

**Added 2026-08-21 second pass.** Labfront was missing from the first draft. It is one of two
research-operations platforms in this file that publish their prices (Fitrockr, below, is the other;
corrected 2026-10-10, the 2026-08-21 text called Labfront the only one).

| Field | Detail | Confidence |
|---|---|---|
| Devices supported | **Garmin** (vívosmart 5, vívoactive 5, Index BPM, Index S2 scale; the CIRQA Smart Band is also on the compatible-devices page and is the device in the 2026 Labfront x Garmin Health grant), **Movesense Medical, HR2 and Flash** (participants start each Movesense recording manually; updated 2026-10-11 from `../../facts/movesense.yaml`), **Dexcom G7 CGM** | **Verified** |
| Garmin data | **Beat-to-Beat Interval**, steps, heart rate, oxygen saturation, respiration, accelerometer, naps, wheelchair activities | **Verified** |
| Movesense data | **RR-interval, ECG, IMU, accelerometer, gyroscope, magnetometer** | **Verified** |
| **Higher resolution than stock** | Labfront has a Garmin partnership letting it **configure devices via the Garmin Health SDKs to increase sensor resolution**, capturing higher-resolution data than Garmin normally collects, explicitly including beat-to-beat/interbeat intervals for HRV | **Corroborated** |
| Included in all tiers | Physiological data collection, **survey tools (EMA)**, event tracking | **Verified** |
| Dexcom | CGM data only after Dexcom approves the study, about 2 months including a data use agreement | **Verified** (`../../facts/labfront.yaml`, raw_streams [Advanced plan]) |

#### Published pricing, **Verified** (labfront.com/pricing, re-read 2026-10-10; checked against `../../facts/labfront.yaml` 2026-10-22)

| Tier | Price | Participants | Notes |
|---|---|---|---|
| **Tester** | **Free** | 5; 2 device types per project | Downloads limited to the last 30 days (older data is kept and unlocked on upgrade). Includes beat-to-beat intervals and 25 Hz accelerometry; Movesense IMU 12.5 Hz and ECG 125 Hz, recordings up to 15 min |
| **Basic** | **$500 / year** | 20 included, **$10** each additional | **One** device integration (Garmin Connect *or* Dexcom). **No beat-to-beat interval, actigraphy, accelerometer or Movesense data**; heart rate 1 min, respiration, SpO2 and stress 3 min, steps 15 min |
| **Advanced** | **$1,250 / year** | 20 included, **$25** each additional | **All** integrations (Garmin, Dexcom, Movesense). Heart rate 1 s to 60 min; respiration, SpO2 and stress 10 s to 60 min; BBI every beat; actigraphy 10 s to 1 min; accelerometer 25, 50 or 100 Hz; Movesense IMU 12.5 to 208 Hz, ECG 125, 250 or 500 Hz, recordings up to 12 h |
| Analytics packages | HRV linear $4,000; HRV non-linear $6,000; sleep actigraphy $3,000; sleep regularity and timing $5,000; each plus **$50 per participant** | | Optional add-ons; require Advanced. Developer Access (Beta) from $4,000: an S3 bucket refreshed every 6 hours, no external API or SDK. Data Audit from $500. (The 2026-08-21 figure of $2,000 is superseded.) |

Billing terms (Verified; `../../facts/labfront.yaml`, minimum_commitment, user_cap): USD, annual in
advance, automatic renewal unless cancelled at least 30 days before renewal. Fees are refundable only
if cancelled within 30 days of the start or renewal date, with no prorated refund after that. Every
participant account counts toward the total, even on a shared device. Short studies are negotiated
by email.

"Unlimited data history" on paid plans is dashboard access, not a storage term. Research data is
typically kept 3 years after study completion, deletion can be requested at any time, and the Terms
say terminating all services deletes the account's data; no page reconciles closing an account within
those 3 years (Verified; `../../facts/labfront.yaml`, retention_terms). Paid plans list "Retroactive
Garmin Data Access"; a separately quoted service announced in 2022 pulls existing Garmin Connect data
up to two years back and needs participants' Garmin Connect login details, which an IRB may object to
(`../../facts/labfront.yaml`, history_depth).

**Programmes** (Verified; `../../facts/labfront.yaml`, research_program, program_status, 2026-10-11):

- **Labfront Grants**: typically one year of Advanced with 20 participants, an analytics package and
  devices, run with partners including Garmin Health. Open calls on 2026-10-11 were the Labfront x
  Garmin Health grant on the CIRQA Smart Band (value $5,500, deadline 2026-11-02), Sleep Science
  (deadline 2026-11-27) and Aging Science (deadline 2026-12-07). The pricing page still calls grants
  rolling and year-round. Garmin-sponsored grants exclude private companies. Earlier named examples
  include a Sleep Research Society Foundation sleep grant and an ACSM-linked award (2026-08-21 reading).
- **Research Collaborator Program**: free to any academic institution, by form and selection;
  collaborator-only grants, product discounts, a device loaner programme and a dedicated liaison.
- Device discounts on Garmin (typically around 20%) and Movesense, by quote. No academic discount on
  platform plans is published.

**Compliance and data terms** (`../../facts/labfront.yaml`):

- Hosting is US only, on AWS, with undated plans for EU servers. The pages disagree on the region: the
  current FAQ and trust page say Virginia, the 2022 Security Statement (still the document Labfront
  points IRBs to) says primarily Ohio. **Conflict**, Corroborated (data_residency).
- **AI training: conflict.** The Privacy Policy (updated 2025-12-30) covers participants' Experiment
  Data, including wearable data, says Labfront uses data to train its machine learning models, and
  allows sharing de-identified data with third parties. The FAQ and trust page say Labfront does not
  access project data. No opt-out is described. Get a written answer before an IRB submission
  (ai_training_terms, Unclear).
- HIPAA alignment and GDPR adherence are Labfront's own claims (Corroborated). No BAA is mentioned
  anywhere (not public). A DPA, a data use agreement template and a completed HECVAT are available on
  request.
- Kiipo Co. (Labfront) is **Active on the Data Privacy Framework registry** (EU-U.S., Swiss-U.S., UK
  Extension; non-HR data; certified 2026-01-05, next due 2027-01-05). Verified.
- SOC 1/2/3 and ISO 27001 are the AWS data centres' certifications, not Labfront's own (Unclear). The
  StateRAMP badge reflects GovRAMP membership; GovRAMP's product list does not name Labfront or Kiipo.

#### Why this changes the picture

A 40-participant Garmin study with high-resolution BBI and EMA costs **$1,250 + 20 × $25 = $1,750
per year** in platform fees, plus devices. It must be on Advanced: Basic carries no beat-to-beat data. That is a fully specified, publicly quotable budget line, which only Labfront and Fitrockr permit among the research platforms here.

It also **removes the Garmin SDK licence question from the critical path** for many studies: rather
than negotiating a Garmin Health SDK licence, a team can buy Labfront Advanced and inherit Labfront's
partnership-derived ability to raise sampling resolution.

**Labfront vs Fitabase, briefly:**

| | Labfront | Fitabase |
|---|---|---|
| Devices | Garmin, Movesense, Dexcom | **Fitbit**, Garmin |
| Pricing | **Published** | Custom quote only |
| EMA/surveys | **Included in all tiers** | Engage, relaunched April 2026; iPhone app live, pages still labelled "Preview · Summer 2026" on 2026-10-21; unpriced |
| Free tier | **Yes, 5 participants** | No |
| Track record | Smaller; grant-driven academic focus | **1,100+ studies** (homepage), **2,500+ studies** (customers page) and **1,650 publications** (research library, updated 5 October 2026), vendor figures that disagree |
| Fitbit support | **No** | Yes |

If your study is Fitbit-based, Fitabase remains the main research-operations option (Fitrockr also lists Google/Fitbit). If it is Garmin-based,
Labfront is cheaper, transparent, includes EMA, and adds Movesense and CGM; Fitrockr is the other published-price option.

Links: https://www.labfront.com/ · https://www.labfront.com/pricing · https://www.labfront.com/compatible-devices · https://www.labfront.com/grant · https://www.labfront.com/collaborator · https://help.labfront.com/garmin-overview · https://help.labfront.com/privacy-policy · https://www.labfront.com/trust-security

### Fitrockr, published pricing and Garmin research grants (added 2026-10-10)

**Confidence for this section: mostly Reported.** fitrockr.com blocks scripts (an HTTP 403
firewall), so its fact record rests on Wayback captures (latest 2026-10-07) and on one researcher's
live reading of 2026-10-21 that could not be re-checked. Every Fitrockr-sourced fact below is
**Reported** unless marked otherwise, and the record is due for a by-hand browser check by
2026-11-04 (`../../facts/fitrockr.yaml`). The figures marked "2026-10-10" were read before the site
moved its pricing from /research/pricing/ to /pricing/; those readings are no longer the current
ones where they differ.

| Field | Detail | Confidence |
|---|---|---|
| Organization | Fitrockr (Digital Rebels GmbH, Berlin) | **Reported** |
| Devices | Claims "700+ wearables"; the compatible-devices page lists Garmin, Apple, Google, Fitbit, Samsung, Withings, Polar, WHOOP, Oura, Dexcom and others, via direct integrations and Apple Health / Health Connect. Garmin is the main source | **Reported** (vendor) |
| Garmin data | Through the Fitrockr app's direct device sync (not Garmin Connect): raw and enhanced beat-to-beat intervals (every beat), accelerometer fixed at 25 Hz and gyroscope fixed at 32 Hz (paid add-on, not adjustable), actigraphy, zero crossing and skin temperature, plus heart rate, stress, SpO2 and respiration at configurable epochs. Through Garmin Connect sync, Fitrockr "supports less data" and HRV is limited to RMSSD in 5-minute intervals during sleep. GPS can be switched off per study | **Reported** (`../../facts/fitrockr.yaml`, raw_streams, sampling_rates) |
| History | Garmin Connect-linked users: up to 2 years can be imported (EUR 500 setup, researcher B's reading). Direct Fitrockr app sync: only what is still on the watch, and a full watch overwrites its oldest files | **Reported** (`../../facts/fitrockr.yaml`, history_depth) |
| Study tooling | Participant compliance and adherence tracking, tasks and scheduled push notifications, multi-language participant apps (now Fitrockr Sync), dashboards, raw data downloads (41 export options in Excel, CSV or JSON); surveys and notifications are a paid add-on (+20% on licence). REST data API and a separate live-data API on request, documentation not public | **Reported** (vendor) |
| Pricing, research and clinical trials | Trial free for 2 weeks, up to 5 device connections. **Basic** from €50 or $55 per month; **Pro** from €150 or $165 per month ("enhanced" wearable data, additional data types). Both: 5 device licences included, 3-month minimum contract and renewals (the terms say no automatic renewal unless agreed); additional device licences €1 to €7.50 per month on Basic and €1 to €15 on Pro. Add-ons as read live on 2026-10-21: accelerometer and gyroscope +25% on licence, API access +20%, live streaming +20%, surveys +20%, on-premise hosting €5,000 + 20%, historic Garmin Connect import €500 setup, and a **Data Vault at €250 per month** for post-project access. The 2026-07-13 capture had the Data Vault at €150, live streaming at €500 + 20%, accelerometer and gyroscope "Volume Based" on Pro only, and a per-stream Basic versus Pro sampling table that is no longer on the live page. Contracts are set in a quote (fixed price per project or pay-as-you-go); teams with limited research funds are asked to request a custom quote | **Reported** (`../../facts/fitrockr.yaml`, api_platform_fees, minimum_commitment, quote_required) |
| Hosting and compliance | Germany cloud hosting included (one help page says Germany or Switzerland); country-of-choice cloud, on-premise and closed-network military on-premise hosting as add-ons. "HIPAA certified" names no certifier (HHS issues no HIPAA certification). The 2026-09-19 privacy policy says Fitrockr may act as a Business Associate under a BAA for covered entities; BAA text not published, and the January 2026 policy had no such offer. A DPA governs processing where required. ISO 27001 is claimed for the hosting centre only, not Fitrockr; Google CASA is claimed with no letter published. No SOC 2 claim. No FDA record (Verified) | **Reported** (`../../facts/fitrockr.yaml`, data_residency, hipaa_statement, baa, dpa, iso27001, soc2) |
| Retention and AI | Each research project runs on its own server instance, deleted with its data at the end of the study. The 2026-09-19 terms add a post-termination retrieval period, then deletion or return. Read-only access afterwards is the paid Data Vault; a BSON database dump on request is the self-storage route. The 2026-09-19 terms bar training general-purpose AI on identifiable customer or participant health data unrelated to the project, but do not exclude aggregated or anonymised data | **Reported** (`../../facts/fitrockr.yaml`, retention_terms, ai_training_terms) |
| Deprecations | From 7 September 2025, studies syncing through the Fitrockr app lost Garmin sleep data for 13 older models (including vívoactive 4, Venu, Venu Sq, Forerunner 245, 45 and 55, Instinct); Garmin Connect sync is unaffected. The old iOS participant app is gone; the current app is Fitrockr Sync | **Reported** (`../../facts/fitrockr.yaml`, deprecations) |
| Grants | Garmin Health x Fitrockr rounds by region or theme since 2023. The Asia 2026 round closed on 31 March 2026: five vívoactive 5 watches plus **6 months of platform access for up to 50 participants**, for academic researchers, post-docs and graduate students in Asia. Earlier rounds gave 3 months of access for up to 50 users. The next round is "to be announced"; no standing academic programme | Package **Corroborated** (Garmin's own release); round status **Reported** (`../../facts/fitrockr.yaml`, research_program, program_status) |

Licensing basis is a **conflict** in Fitrockr's own pages (`../../facts/fitrockr.yaml`, user_cap,
Reported). The pricing page bills per connected device with unlimited users, and a 2026 news post says
licences moved from users to devices; the pricing help article still says pricing "is based on user
numbers". If device-based, devices reused across sequential participants would be licensed once
(inference; confirm with Fitrockr, including for older contracts).

### MyDataHelps (CareEvolution)

A research platform with documented export formats for both Apple HealthKit v2 (including
electrocardiogram export format) and Garmin. Referenced in the source review; not evaluated in
depth. **Reported.**

### CentrePoint (Ametris) and Care Portal (Empatica)

Vendor-specific and covered in their own profiles. Distinguishing feature: these are the only
device vendors in Module 1 that supply their own study-operations layer.

---

## Category 2, Unified wearable APIs

These normalize many vendor APIs behind one schema and one OAuth flow. Value proposition: a study
that lets participants bring whatever device they already own.

| Provider | Notes | Confidence |
|---|---|---|
| **Terra API** | Unified API across many wearable brands; widely referenced as the default for multi-brand integration. Open, self-serve developer sign-up. Detail below, from its fact record | Reported; record-based detail Verified or Corroborated as marked |
| **Validic** | Long-established health data connectivity vendor; publishes a Fitbit → Google Health API developer transition guide, indicating active maintenance through the 2026 migration | Reported |
| **Thryve** | EU-based health data API (mHealth Pioneers GmbH, Berlin), Germany-hosted; also sells a Research Partners route, a multimodal clinical trial platform, a Garmin Companion module and runs the Huawei-funded Terve Research platform. Detail below, from its fact record | Reported; record-based detail Verified or Corroborated as marked |
| **Rook** | Wearable/health data API with documented Garmin data-source mapping | Reported |
| **Sahha** | Health data platform; publishes migration guidance for the Fitbit shutdown | Reported |
| **Open Wearables** | **Open-source** wearable API project; has integrated Oura, WHOOP and others as of 2026, and ships an MCP server exposing wearable data to LLM assistants | Reported |

### Terra, from its fact record (`../../facts/terra.yaml`, judged 2026-10-21)

- **Research route.** No academic programme. The Startup Accelerator (up to $100,000 in API credits
  over up to six months, rolling admission, about 0.8% accepted, card required) admits research
  projects if Terra is credited in resulting publications and datasets. Corroborated and Verified.
- **Terms that bite in research** (Verified). Free development accounts are for internal evaluation
  only, so no pilot study on a sandbox; testing and staging are capped at 50 connected users each.
  Clause 1.2(v) of the customer Terms bars publicly disseminating information on the performance of
  the Services or Output, which may reach a methods paper on Terra-delivered data quality; ask for
  written permission first.
- **Whose credentials** (Verified as to what Terra says). Google Health and Fitbit: Terra manages the
  credentials; whether its project has passed Google's restricted-scope review and CASA, or carries a
  user cap, is not stated. Garmin: the customer now supplies its own Garmin credentials (page changed
  between 2026-10-14 and 2026-10-21), so with Garmin's programme paused a new customer may have no
  Garmin route. WHOOP, Strava, Dexcom and Huawei: bring your own keys, so the study is itself the
  provider's developer.
- **Data.** Provider data passed through unsmoothed (heart rate, RR interval, HRV, SpO2, glucose,
  position, raw ECG voltage where the provider supplies them); no raw PPG. The Streaming API add-on
  carries roughly per-second data from BLE/ANT+ devices, Wear OS, Apple Watch and phone sensors.
  **Smart Fill** (August 2026) imputes missing sleep, daily and activity values with a confidence per
  estimated cell; a study must flag or exclude these. History on connect depends on the provider
  (Garmin up to 5 years, Google Health up to 12 months, Polar and Health Connect 30 days).
- **Rate limits: conflict** (Unclear). The rate-limit reference sets 1,825 days per request and 6,000
  requested days per user per hour; the environments page says the REST API has no rate limits.
- **Retention.** End-user data is usually kept two days and never more than six months, with
  exceptions including an active connection; storage is an Enterprise feature, so the study stores
  payloads as they arrive. Personal data is deleted or returned within 90 days of termination (DPA).
- **Terra's own research use** (Verified). The End User Privacy Policy (updated 2026-09-24) lets
  Terra run "statistical, scientific, or market research" on collected data, publish de-identified
  results and keep de-identified derivatives with no time limit; the wording appeared between
  2025-10-16 and 2026-02-24. The Integration Onboarding Terms (2026-10-12) allow use of de-identified
  partner data "for any lawful purpose". No clause names AI training. Anthropic and OpenAI are
  subprocessors for AI-assisted support on anonymised data, with a customer opt-out. No participant
  opt-out from research use is stated, which an IRB will want to know.
- **Compliance.** Signed BAA on Enterprise only. DPA (with EU SCCs and the UK addendum) is part of the
  Terms. HIPAA, GDPR and SOC 2 Type II are Terra's own claims (Corroborated); the Vanta trust centre
  holding the reports blocks automated reads. No ISO 27001 claim. Primary processing in the UK and
  the Netherlands, subprocessors in the US, UK and EU; a dedicated regional instance on Enterprise.
- **Deprecations.** Terra's Fitbit connection runs on the legacy Fitbit Web API; users must move to
  the Google Health connection, sign in again and get a new user_id. The `fitbit_v2` provider was
  renamed `google_health` in July 2026. Peloton and Technogym were removed.

### Thryve, from its fact record (`../../facts/thryve.yaml`, judged 2026-10-21)

- **Research routes.** Thryve Research Partners ("Become a Partner") is the commercial platform with
  study setup support, not a separate academic data-access programme; no research-specific terms or
  price (Verified). **Terve Research**, a European platform for academic and medical institutions
  funded by Huawei and run by Thryve, was announced on 31 August 2026 but was not live on 2026-10-21
  (site still "launching soon", no app listing), against an announcement that two studies would launch
  in September (**conflict**, Unclear). Huawei funding is a point to disclose in ethics review.
- **Plans** (Verified). 14-day trial with 25 users, card and business email required, converting to
  Start Up unless cancelled. Start Up is monthly and cancellable at any time. **Scale Up is only for
  startups founded less than 10 years ago**, so a university is left with Start Up (500 users) or
  Enterprise; Scale Up extra users cost €999 per 10,000. Foundational Analytics are included at no
  charge since December 2025.
- **Google Health** (Verified). Route A, direct: the customer's own OAuth client, Google Cloud project
  and verified app, Google OAuth verification and an annual CASA assessment, capped by Google at 100
  users until both are done. CASA costs $500 to $4,500 per Google; Thryve's own estimate is around
  €1,000 and upwards (Corroborated). Route B, on-device: Thryve's SDK reads what the Google Health app
  writes into Apple Health or Health Connect, with no Google credentials or CASA.
- **Garmin Companion module** (SDK 5.3.0, Verified). Real-time Bluetooth streaming including
  beat-to-beat intervals, needing Garmin Connect on the phone and a Garmin Companion licence requested
  through Thryve support. Whether a production licence or Garmin fee is also needed, and whether the
  route is open during Garmin's developer-programme pause, is not stated.
- **Data.** No sensor-level raw signals from web sources; values come at each source's finest
  granularity, without pre-aggregation. The Apple Health module reads heartbeat series and ECG;
  ThryveBLE (beta) connects Bluetooth heart rate and glucose monitors. Default backfill is 14 days
  before user creation, and Start Up and Scale Up cannot go further. By default participants authorize
  Thryve's shared OAuth app, which requests every scope and shares vendor rate limits across Thryve's
  customers; bringing your own client allows narrower scopes.
- **AI and research use** (Unclear). No AI or model-training clause. The footer-linked General Terms
  (v1.2, January 2020) let Thryve research anonymized data, also with external partners, and use
  aggregate data from customers' use.
- **Deprecations.** Fitbit Web API source end date is a **conflict** inside Thryve's own pages (docs
  table said 29 October 2026 and now just "Deprecated", blog 30 October; Google's own date is now 2 November),
  Corroborated. The docs table now lists a Google Health source (ID 49). Thryve disconnects
  all Fitbit connections within 24 hours of the shutdown and keeps ingested data. The old Samsung
  Health module was removed in SDK 5.3.0 and users must reconnect. Google Fit sources are end of life.

### What unified APIs genuinely solve

- One OAuth flow and one schema instead of six.
- Insulation from vendor API churn, notably, these vendors are absorbing the Fitbit → Google Health
  API migration on behalf of their customers, which in 2026 is a substantial and concrete benefit.
- BYOD studies where participants keep whichever device they own, improving recruitment and
  retention.

### What they do not solve, and the trap to avoid

- **They cannot give you data the underlying vendor does not expose.** No unified API produces raw
  PPG from an Oura ring, because Oura does not expose it. The floor is set by the worst-case vendor.
- **Harmonization is lossy and opaque.** A "sleep stage" from Oura, Fitbit, and WHOOP are outputs of
  three different proprietary algorithms with different validation profiles. Presenting them in one
  normalized field makes them *look* comparable when they are not. In a study where device brand
  varies across participants, **device becomes an uncontrolled confound in every physiological
  variable.** This is the single most important methodological warning in this file.
- They add a third-party data processor to the compliance surface, with its own BAA/DPA
  requirements and its own terms, which must themselves be compatible with the underlying vendor
  terms (see the WHOOP profile: WHOOP's terms prohibit licensing API data to third parties, which
  has obvious implications for routing WHOOP data through an intermediary; through Terra the study
  supplies its own WHOOP credentials and is itself the WHOOP developer). An intermediary can also be
  more than a processor: Terra's End User Privacy Policy lets it use end-user data for its own
  statistical, scientific or market research and keep de-identified derivatives without a time limit
  (`../../facts/terra.yaml`, ai_training_terms).
- Cost is usage-based. Entry prices are public for some vendors (Verified 2026-10-10, re-checked against the fact records 2026-10-22): **Terra** Quick Start from $499 per month billed monthly, or $399 per month billed annually, with 100,000 credits per month; each active authentication (one connected source for one user) costs 200 credits a month, so the included credits cover about 500 connected sources before overage ($0.005 per credit to 1,000,000, then $0.003); the first 400 events per authentication are free, then 0.5 credits each; Streaming add-on $99 per month. Annual renewals need 60 days' notice to cancel; 30-day money-back guarantee. A signed BAA is listed only on the custom-priced Enterprise plan. **Thryve** Start Up from €499 per month for up to 500 users (€0.50 per additional user), Scale Up from €1,000 per month for up to 5,000 users (€999 per extra 10,000; **startups founded less than 10 years ago only**), Enterprise bespoke; Thryve's plan table lists data storage of 1 day (free trial), 2 weeks (Start Up) and 1 month (Scale Up), so data must be pulled or received continuously. Thryve says a BAA and a DPA are standard on every plan (**Corroborated**, vendor statement). Neither publishes academic pricing. Thryve's FAQ calls itself "100% GDPR and HIPAA compliant" and it claims ISO 27001 and ISO 9001, recertified 2025, with certificates only on request (vendor claims, **Corroborated**; no SOC 2 claim) (`../../facts/terra.yaml`, `../../facts/thryve.yaml`).

**Practical guidance:** unified APIs are appropriate for descriptive, engagement, or intervention
studies where the wearable is a behaviour-change tool rather than a measurement instrument. They are
inappropriate where a physiological variable is a primary endpoint, unless device brand is
controlled or explicitly modelled.

---

## Category 3, Open datasets (no device, no API)

The cheapest wearable study is one where someone else already collected the data.

### All of Us Research Program, Fitbit dataset

| Field | Detail | Confidence |
|---|---|---|
| Scale | 59,000+ participants with Fitbit data, spanning 14 years; 39M+ step observations, 31M+ sleep observations | **Verified** |
| Linkage | 46% also contributed EHR, physical measurements, genomics, and survey data | **Verified** |
| Granularity | **Minute-level heart rate and minute-level intraday steps**, plus daily activity summaries, daily sleep summaries, sleep levels, HR zones | **Verified** |
| Structure | Seven All of Us-specific BigQuery tables (`steps_intraday`, `heart_rate_summary`, `heart_rate_minute_level`, `activity_summary`, `sleep_level`, `sleep_daily_summary`, device tables). **Not OMOP CDM** | **Verified** |
| Access | Registered researchers via the Researcher Workbench | **Verified** |
| Caveat | Published work stresses that data quality control (wear-time, completeness filtering) materially changes results | **Corroborated** |

This is the strongest single research asset in the entire Fitbit ecosystem and it requires no
device procurement, no API approval, no participant recruitment, and no exposure to the Fitbit Web API
shutoff on 2 November 2026 or to the Google Health API's onboarding and restricted-scope review.

### UK Biobank accelerometry

100,000+ participants of raw AX3 wrist accelerometry at 100 Hz, ±8 g, seven days, with the full
open analysis toolchain. See `axivity-geneactiv.md`. Access via UK Biobank application.

---

## Decision heuristic

| Situation | Route |
|---|---|
| Physiological variable is a primary endpoint | Single device model, direct vendor API or SDK. **Never a unified API.** |
| Need study operations, no engineering team, **Fitbit** | Fitabase (quote required) |
| Need study operations, no engineering team, **Garmin** | **Labfront** (published pricing, EMA included, free 5-participant tier to pilot) or **Fitrockr** (published pricing, per-device licences); also the practical route while Garmin's own programme is closed to new applicants |
| Need nocturnal beat-to-beat intervals for HRV | **Garmin Enhanced BBI** via Fitabase (Garmin API route, during sleep, paid add-on) or Labfront **Advanced** (not Basic; Tester for a pilot), no custom app needed. Fitabase's Garmin SDK route through the Engage app and Fitrockr's app sync also deliver beat-to-beat data; Fitabase states no daytime coverage or rate for its SDK route |
| Need raw signal | Direct: Polar BLE SDK (cheapest), Movesense (highest rates), Samsung Health Sensor SDK (incl. raw EDA on Galaxy Watch8), Garmin Health SDK, Empatica (EDA), Ultrahuman (ring PPG), Axivity/ActiGraph |
| BYOD, wearable is an intervention not an instrument | Unified API (Terra/Validic/Rook/Thryve) |
| Question can be answered from existing data | All of Us Researcher Workbench or UK Biobank |
| Study uses Fitbit after 2 November 2026 | Fitabase (holds its own project; new-study capacity not stated; every participant must reauthorize, and 11 of 40 exports were not yet on the Google Health API on 2026-10-14), or on-device collection via Apple Health or Health Connect. Thryve's direct route (and Validic's) needs the customer's own Google Cloud project, verified app and CASA (Corroborated); Terra's docs say Terra manages the Google Health credentials, with the review and CASA status of its project not stated. The study's own Google Health API project is apparently possible again (Corroborated 2026-10-21; Google was not onboarding new projects on 2026-10-10), with restricted-scope review and, above 100 users, verification and CASA |

## Vendor Fact Record

### Fitabase

<!-- facts:begin fitabase -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | No separate research or academic program. Fitabase itself is a research-only data platform for studies and trials using Fitbit (now Google Health) and Garmin wearables, with monitoring dashboards and exports. A one-off Fitabase and Fitbit Health Equity Research Initiative (2021) awarded devices and services; no later round found. [C, 2026-10-21] |
| Who can join the research program | Research projects, studies and clinical trials; individuals cannot use Fitabase to access their own data. No other eligibility criteria are published. [V, 2026-10-21] |
| How to apply, and any approval or review step | Sales-led, with no review step. Teams request a demo or quote; Fitabase then issues an invitation code and account creation link. Studies that cannot use participants' personal Google accounts can use Google-created de-identified demo accounts, which need a Google research application with an IRB approval or waiver (about 5 to 7 business days); Fitabase supplies the client ID. [V, 2026-10-21] |
| Whether the program is active, paused, renamed or closed | Active. Fitbit collection is moving to the Google Health API (reauthorization opened in the platform on 2026-10-15). On 2026-10-19 Fitabase extended all active Fitbit projects ending before 2027-01-01 to that date at no charge, because some datasets are not yet available from Google. Fitabase Engage was relaunched on 2026-04-21; on 2026-10-21 the Engage pages still label the Mobile App and Wrist App "Preview · Summer 2026", while the Fitabase Engage iPhone app is live on the App Store (version 1.6.8, Oct 9). [V, 2026-10-21] |
| Whether the general developer or API program is open to new applicants | The Fitabase API is a paid add-on for existing customer projects (key from the project's API portal), not an open developer program. Automated batch exports are a further add-on. The Fitabase API is not changing in the Google Health API migration. [V, 2026-10-21] |
| Participant or user limits before approval or by tier | Not public [2026-10-21] |
| How academic access differs from commercial or consumer access | Not public [2026-10-21] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | n/a |
| Consumer subscription or membership price | n/a |
| Research or academic pricing or discount | Not public [2026-10-21] |
| Fees for API, SDK, platform or data access | No public figures. Fitabase Core is quoted per study. Charged as extras, amounts unpublished, are the Fitabase API, automated batch exports (Batch Export API), SMS messages and reminders (billed partly per message segment), the Aggregate Data API, Food and Weight exports, and Garmin Enhanced BBI. [V, 2026-10-21] |
| Minimum order, term or commitment | Not public [2026-10-21] |
| Whether pricing requires contacting sales | Yes. All pricing, including add-ons, is by custom quote. Custom development is capacity-limited, with a limited number of custom projects accepted each year. [V, 2026-10-21] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | **Fitbit / Google Health:** No raw sensor signals (no raw accelerometer or PPG); Fitabase passes through the highest resolution the partner API gives, including second-level heart rate (every 3 to 15 seconds), 30-second sleep stages and timestamped ECG logs. No GPS or location data is collected, by design. [V, 2026-10-21]<br>**Garmin:** Two documented beat-to-beat routes. (1) Garmin API (OAuth, Garmin Connect app) - Enhanced BBI with a per-beat confidence flag, captured at the wrist during sleep, from devices with a gen 4 or later sensor (premium dataset). (2) Garmin SDK - a 2026-07-29 blog post says Fitabase can pull beat-to-beat intervals with the Garmin SDK when participants sync through the Fitabase Engage app instead of Garmin Connect; daytime coverage and sampling for this route are not stated. Also 15-second heart rate, and Garmin Index blood pressure monitor readings (systolic, diastolic, pulse, source). [C, 2026-10-21] |
| Derived or processed metrics available to researchers | **Fitbit / Google Health:** Steps, intensity and METs, calories, sleep and sleep stages, breathing rate, HRV, SpO2, Active Zone Minutes, cardio fitness score, floors, distance, resting heart rate, skin and core temperature, wear time, plus weight, food and activity logs. [V, 2026-10-21]<br>**Garmin:** Daily stress, steps, floors, VO2max, fitness age, Pulse Ox, Move IQ, body composition, calories, nightly HRV average and 5-minute high, wear time and activity logs; 15-minute epochs; sleep records at each stage change; Body Battery, respiration and sleep scores. [V, 2026-10-21] |
| Documented sampling rates or temporal resolution | **Fitbit / Google Health:** Heart rate every 3 to 15 seconds (variable); sleep stages 30 seconds; minute-level steps, intensity, METs, calories, SpO2 and Active Zone Minutes; HRV 5-minute readings; hourly and daily totals. [V, 2026-10-21]<br>**Garmin:** Heart rate 15 seconds; stress 3 minutes; Pulse Ox minute level; activity epochs 15 minutes (steps, heart rate, distance, MET, intensity, motion); sleep as records at each stage change; Enhanced BBI per beat during sleep. No rate is stated for the Garmin SDK route. [V, 2026-10-21] |
| How far back data can be retrieved | **Garmin:** Data before connection can be pulled by setting sync dates in the past, but only if the participant turns on the off-by-default Historical Data permission in Garmin Connect. No maximum look-back is published. [V, 2026-10-21]<br>**Fitbit / Google Health:** Unclear |
| Export, API, SDK or file routes | CSV downloads from individual participant report pages and unlimited batch exports (minute, hour and day level); the Fitabase API add-on (Daily Activity, Profiles, Sync and Batch Export endpoints, key-authenticated); the Aggregate Data API for bulk JSON or CSV; scheduled batch exports at most daily; webhooks that POST to the customer's HTTPS endpoint when a participant's connection status changes. During the migration, exports gain UTC, time zone and source columns. [V, 2026-10-21] |
| API rate limits | Not public [2026-10-21] |
| Terms on retaining, storing or deleting data | On account cancellation, personally identifiable information is deleted and backups expire on the normal schedule, but Fitabase may keep using de-identified, anonymized historical data. On termination Fitabase may delete all account data, and it may close accounts inactive for more than 30 days. Fitabase's example IRB text says projects are removed and data deleted from servers and backups 90 days after data collection ends. Data already synced is kept through the Google Health API switch. [V, 2026-10-21] |
| Terms on using data to train AI or ML models | Not public [2026-10-21] |
| Announced shutdowns, deprecations or migrations, with dates | Fitabase says Google turns off the Fitbit Web API on 2026-10-30 (Google itself moved the date to 2026-11-02 on 2026-10-23; see facts/fitbit-google.yaml). Every Fitabase participant still collecting after that must reauthorize for the Google Health API, once, either in the Google Health app or by Fitabase link (platform reauthorization opened 2026-10-15); the reconnect option and links keep working through 2026-11-30. Late reauthorization backfills the gap if the device kept syncing to Google. Reauthorization cannot be done programmatically. Exports move dataset by dataset; on 2026-10-14, 29 of 40 were available, 8 delayed (including Intraday Calories, Intraday METs and ECG, whose import is paused) and 3 classic sleep exports Fitbit API only. Active Fitbit projects were extended to 2027-01-01 at no charge. Classic sleep stops being a separate dataset, writing step goals is not yet available, exports gain UTC, time zone and source columns, and the Fitabase API is unchanged. [V, 2026-10-30] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-21] |
| Whether a data processing agreement is offered | Not public [2026-10-21] |
| Published HIPAA statement | Not public [2026-10-21] |
| Published GDPR statement | Not public [2026-10-21]<br>**Data Privacy Framework certification:** Small Steps Labs LLC (display name Fitabase, San Diego) is listed Active on the Commerce Department's Data Privacy Framework registry under the EU-U.S. DPF, the Swiss-U.S. DPF and the UK Extension, for non-HR data. EU-U.S. and Swiss-U.S. first certified 2018-12-07, UK Extension 2024-06-27, next certification due 2027-10-16. Verification method: self-assessment; JAMS as the dispute body. Five recorded lapses, the latest 2026-09-07 to 2026-10-16. [V, 2026-10-21] |
| ISO/IEC 27001 status and evidence | Not public [2026-10-21] |
| SOC 2 status and evidence | Not public [2026-10-21] |
| FDA clearances, from the FDA database | Not public [2026-10-21] |
| Where data is stored, and residency options | United States only, on Microsoft Azure; no other region or residency option is offered. [V, 2026-10-21] |

<!-- facts:end -->

### Labfront

<!-- facts:begin labfront -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | Two programs. (1) Labfront Grants: subsidised or free platform access (typically one year of the Advanced plan with 20 participants), an analytics package and devices, run with partners including Garmin Health. (2) The Research Collaborator Program, free to academic institutions: collaborator-only grants, product discounts, analytics guidance, a device loaner program and a dedicated liaison. [V, 2026-10-11] |
| Who can join the research program | Collaborator Program: any academic institution. Grants are set per call: the 2026 Labfront x Garmin Health grant is open worldwide (EMEA, APAC, Americas) but not to previous recipients of that grant; the 2026 Aging Science grant requires affiliation with an accredited academic, research or professional institution; Garmin-sponsored grants are for academic or healthcare institutions, not private companies. [V, 2026-10-11] |
| How to apply, and any approval or review step | Collaborator Program: an online form, then selection; selected institutions get a dedicated liaison. Grants: a study summary or abstract (about 200 words), a personal statement (200 words max) and a CV, by the call's deadline. The grants FAQ says applications are reviewed roughly every 2 to 3 months and a winner can take up to a month after the deadline to be announced. [V, 2026-10-11] |
| Whether the program is active, paused, renamed or closed | Active. Open 2026 grant calls on 2026-10-11: Labfront x Garmin Health Research Grant built on the Garmin CIRQA Smart Band (value $5,500, deadline 2026-11-02), Sleep Science (deadline 2026-11-27) and Aging Science (deadline 2026-12-07). The pricing page still calls grants rolling and year-round. Collaborator Program taking applications. [V, 2026-10-11] |
| Whether the general developer or API program is open to new applicants | Developer Access is labelled Beta and is a paid add-on (from $4,000) on the Advanced plan only. There is no external API or SDK; access is to an S3 bucket, granted after the project owner emails support, within 5 working days. [V, 2026-10-11] |
| Participant or user limits before approval or by tier | Tester (free): 5 participants, 2 device types per project. Basic: 20 participants included, 1 device type (Garmin or Dexcom). Advanced: 20 included, unlimited device types. Extra participants are billed per participant per year on Basic ($10) and Advanced ($25); every participant account counts, even on a shared device. One Movesense sensor per participant. [V, 2026-10-11] |
| How academic access differs from commercial or consumer access | One public price list for every customer; no separate academic or commercial tier is published. Academic users get extra routes in, namely Garmin and Movesense device discounts, the Collaborator Program (academic institutions only) and Garmin-sponsored grants that exclude private companies. [C, 2026-10-11] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | Labfront sells no hardware and no plan includes devices. Customers get a Garmin discount the FAQ gives as typically around 20% (elsewhere 20 to 25%), and a Movesense discount, by quote. [V, 2026-10-11] |
| Consumer subscription or membership price | Researcher plans (there is no consumer subscription; the participant app is free): Tester free (5 participants, downloads limited to the last 30 days). Basic $500/yr with 20 participants, then $10 per extra participant, one integration (Garmin Connect or Dexcom), no beat-to-beat, actigraphy or accelerometer data. Advanced $1,250/yr with 20 participants, then $25 per extra participant, all integrations and high-resolution data. USD, billed annually in advance. [V, 2026-10-11] |
| Research or academic pricing or discount | No academic discount on platform plans is published. Academic support comes as device discounts, Collaborator Program discounts, and grants giving free platform access (for example one year of Advanced with 20 participants, devices and an analytics package, valued at $5,000 to $5,500). [V, 2026-10-11] |
| Fees for API, SDK, platform or data access | Add-ons, Advanced plan only. Developer Access (S3 bucket of raw data, Beta): from $4,000. Analytics reports: HRV linear $4,000, HRV non-linear $6,000, sleep actigraphy $3,000, sleep regularity and timing $5,000, each plus $50 per participant. Data Audit: from $500. [V, 2026-10-11] |
| Minimum order, term or commitment | Annual subscription paid in advance; no monthly billing (short studies negotiable by email). Subscriptions renew automatically unless cancelled at least 30 days before renewal. Fees are refundable only if the service is cancelled within 30 days of the start or renewal date; otherwise non-refundable, with no prorated refund on cancellation. [V, 2026-10-11] |
| Whether pricing requires contacting sales | No for the three plans, which are priced publicly with self-serve sign-up. Yes for add-ons (listed "starting from" with Contact Us), extra participant slots, device discounts, short-term studies and retroactive Garmin Connect extraction. [V, 2026-10-11] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | **Advanced plan:** Garmin device-direct data through the Labfront Companion app: beat-to-beat intervals, actigraphy and 3-axis accelerometer (25 to 100 Hz). Movesense Medical, HR2 or Flash (recordings started by the participant in a task, not continuous in the background): ECG waveform, 9-axis IMU, RR interval. Dexcom CGM after Dexcom approves the study (about 2 months, including a data use agreement). Current pages list Garmin, Movesense and Dexcom only. [V, 2026-10-11]<br>**Basic plan:** No raw sensor streams. Standard Garmin Connect data only, from one device integration (Garmin Connect or Dexcom); no beat-to-beat interval, actigraphy, accelerometer or Movesense data. The free Tester plan, by contrast, gets beat-to-beat intervals and 25 Hz accelerometry. [V, 2026-10-11] |
| Derived or processed metrics available to researchers | Garmin Connect post-processed metrics (daily and activity summaries, sleep, stress, respiration, SpO2, heart rate, steps); sleep requires the Garmin Connect source. Paid Labfront Analytics reports add HRV time and frequency domain, non-linear HRV (DFA, MSE), actigraphy sleep, and sleep regularity and timing indices. [V, 2026-10-11] |
| Documented sampling rates or temporal resolution | Advanced: heart rate 1 s to 60 min; respiration, SpO2 and stress 10 s to 60 min; steps 1 or 15 min; BBI every beat; actigraphy 10 s to 1 min; accelerometer 25, 50 or 100 Hz; Movesense IMU 12.5 to 208 Hz, ECG 125, 250 or 500 Hz, recordings up to 12 h. Basic: heart rate 1 min; respiration, SpO2 and stress 3 min; steps 15 min; no BBI, actigraphy or accelerometer. Tester: accelerometer 25 Hz, Movesense IMU 12.5 Hz and ECG 125 Hz, recordings up to 15 min. [V, 2026-10-11] |
| How far back data can be retrieved | Tester downloads are limited to the last 30 days (older data is kept and unlocked on upgrade); paid plans have unlimited history for project data and list "Retroactive Garmin Data Access". A separately quoted service (announced 2022) extracts participants' existing Garmin Connect data up to two years back and requires their Garmin Connect login details. [V, 2026-10-11] |
| Export, API, SDK or file routes | Dashboard download: one ZIP of CSV files per request, filtered by participant and date range. Developer Access add-on (Beta): an S3 bucket refreshed every 6 hours (Garmin Connect, Garmin device-direct, tasks and questionnaires). No public API or SDK. Participants can download a copy of their own data. [V, 2026-10-11] |
| API rate limits | n/a |
| Terms on retaining, storing or deleting data | Research data is typically kept for 3 years after study completion (the 2022 Security Statement says at least 3 years, longer on request where local law requires), with NIH DMS Policy compliance stated. Researchers can request full deletion at any time. The Terms say that terminating all services deletes the account's data. [V, 2026-10-11] |
| Terms on using data to train AI or ML models | The Privacy Policy (updated 2025-12-30) covers study participants' Experiment Data, including wearable data, and says Labfront uses data to train and improve its machine learning models and may share de-identified data with third parties. The trust page and FAQ say researchers own the data and Labfront does not access project data. No opt-out from model training is described. (conflict) [U, 2026-10-11] |
| Announced shutdowns, deprecations or migrations, with dates | Not public [2026-10-11] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-11] |
| Whether a data processing agreement is offered | Labfront says it can provide a Data Processing Agreement to specific customers on request, and a Data Use Agreement template on request; most institutions, it says, need neither beyond the Terms and policies. It describes itself as primarily a data processor. No DPA text is published. [C, 2026-10-11] |
| Published HIPAA statement | Labfront claims HIPAA alignment (trust page) and HIPAA compliance (data-storage page, grants FAQ). No BAA, audit or attestation is published. [C, 2026-10-11] |
| Published GDPR statement | Labfront states GDPR adherence and describes itself as primarily a processor for research teams. Hosting is US only (see data_residency). [C, 2026-10-11]<br>**Data Privacy Framework certification:** Kiipo Co. (display name Labfront, Sharon, MA) is listed Active on the Commerce Department's Data Privacy Framework registry under the EU-U.S. DPF, the Swiss-U.S. DPF and the UK Extension, for non-HR data. Certified 2026-01-05, next certification due 2027-01-05, no inactive periods. Verification method: self-assessment. Dispute resolution: JAMS. [V, 2026-10-11] |
| ISO/IEC 27001 status and evidence | Unclear |
| SOC 2 status and evidence | Unclear |
| FDA clearances, from the FDA database | Not public [2026-10-11] |
| Where data is stored, and residency options | US only (AWS), with EU servers planned but undated. Pages disagree on the primary region: the current FAQ and trust page say Virginia; the Security Statement (last updated 2022-08-25) says primarily Ohio, with backups across US AWS locations. (conflict) [C, 2026-10-11] |

<!-- facts:end -->

### Fitrockr

<!-- facts:begin fitrockr -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | Garmin Health x Fitrockr research grants, run as regional or themed rounds (EMEA 2023, Americas 2023, India 2024, Biomarkers 2024, Australia and New Zealand 2025, Asia 2026). The Asia 2026 award was 5 Garmin vivoactive 5 watches, 6 months of unrestricted Fitrockr platform access for up to 50 participants, and a possible feature in Garmin Health communications; earlier rounds gave 3 months of access for up to 50 users. There is no standing academic program. [C, 2026-10-21] |
| Who can join the research program | Set per round, usually by region. Asia 2026 was open to academic researchers, post-docs and graduate students in Asia doing health or sports science studies with Garmin wearables, with projects starting within 2026. Americas 2023 was open to researchers in any North or South American country. [C, 2026-10-21] |
| How to apply, and any approval or review step | Applicants apply through the round's official grant page before a fixed deadline; between rounds Fitrockr points people to its newsletter. Selection criteria and the review process are not published. [C, 2026-10-21] |
| Whether the program is active, paused, renamed or closed | Between rounds. The Asia 2026 call closed on 31 March 2026 and its winners are listed; the next round is "to be announced". No open call on the 2026-07-13 capture or in researcher B's live reading of 2026-10-21. [R, 2026-10-21] |
| Whether the general developer or API program is open to new applicants | No public developer program. Paying customers get the REST data API (all synced data) and a separate live-data API (needs the Live add-on) on request to support; API access is a priced add-on (+20% on licence). API documentation is not public. [R, 2026-10-21] |
| Participant or user limits before approval or by tier | No participant cap on the published plans: the pricing page bills by connected device (5 device licences included, more bought per device) with unlimited users, and a 2026 news post says licences moved from user accounts to devices. The pricing help article still says pricing is based on user numbers. Free trial: up to 5 device connections for 2 weeks. Grants cover up to 50 participants. (conflict) [R, 2026-10-21] |
| How academic access differs from commercial or consumer access | No separate academic price list or terms. One "Research & Clinical Trials" price list covers universities, hospitals and companies; teams with limited research funds are asked to request a custom quote. The grants are the only academic-specific route. [R, 2026-10-21] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | n/a |
| Consumer subscription or membership price | n/a |
| Research or academic pricing or discount | No published academic price or discount. Teams with limited research funds are asked to contact Fitrockr for a custom quote. [R, 2026-10-21] |
| Fees for API, SDK, platform or data access | Research & Clinical Trials plans per month, as researcher B read them on 2026-10-21: Basic from EUR 50 (USD 55), Pro from EUR 150 (USD 165), each with 5 device licences; extra device licences EUR 1 to 7.5 (Basic) or EUR 1 to 15 (Pro) per month. Add-ons: API access +20% on licence; accelerometer and gyroscope collection +25%; live streaming +20%; surveys +20%; on-premise hosting EUR 5,000 + 20%; Data Vault EUR 250 per month after the project; historic Garmin Connect import EUR 500 setup. Germany cloud hosting, support and admin accounts included. [R, 2026-10-21] |
| Minimum order, term or commitment | 3-month minimum contract, with renewals in 3-month terms, on Basic and Pro. The terms say subscriptions do not renew automatically unless agreed. [R, 2026-10-21] |
| Whether pricing requires contacting sales | Partly. "Starting at" plan and add-on prices are published, but contracts (fixed price per project or pay-as-you-go) are set in a Fitrockr quote, and some items (country-of-choice hosting, custom work) are priced on effort. [R, 2026-10-21] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | Through the Fitrockr app's direct device sync (not Garmin Connect): raw and enhanced beat-to-beat intervals (every beat), accelerometer (fixed 25 Hz) and gyroscope (fixed 32 Hz) as a paid add-on, actigraphy, zero crossing and skin temperature, plus heart rate, stress, SpO2 and respiration at configurable epochs. Syncing through Garmin Connect "supports less data". GPS can be switched off per study. Garmin is the main source; other brands (Apple, Google, Withings, Oura, Polar and others) are supported. [R, 2026-10-21] |
| Derived or processed metrics available to researchers | Device metrics passed through (Garmin stress, Body Battery, sleep, steps, intensity minutes, respiration, SpO2) plus metrics Fitrockr computes itself, including HRV indices (RMSSD, SDNN, LF/HF) from beat-to-beat data and MET, and report types (HRV, sleep, 6-minute walk test and others). [R, 2026-10-21] |
| Documented sampling rates or temporal resolution | Accelerometer fixed at 25 Hz and gyroscope at 32 Hz on Garmin (not adjustable); beat-to-beat intervals every beat; other streams configurable (Fitrockr lists 1 s, 60 s, 90 s and so on). Via Garmin Connect sync, HRV is limited to RMSSD in 5-minute intervals during the sleep window. [R, 2026-10-21] |
| How far back data can be retrieved | For Garmin Connect-linked users, up to 2 years of history can be imported (a paid add-on, EUR 500 setup per researcher B's reading of the pricing page). For direct Fitrockr app sync, history is limited to what is still on the watch; when storage is full, default data overwrites the oldest files. [R, 2026-10-21] |
| Export, API, SDK or file routes | On-demand dashboard exports (41 export options) in Excel, CSV or JSON (CSV or JSON for large data); REST data API for all synced data and a live-data API for live streams (both add-ons); a full database dump in BSON on request for long-term storage. [R, 2026-10-21] |
| API rate limits | Not public [2026-10-21] |
| Terms on retaining, storing or deleting data | Each research project runs on its own server instance, deleted with all data at the end of the study. Under the 2026-09-19 terms (researcher B's reading), Fitrockr deletes or returns customer data after a post-termination retrieval period, unless law or a written agreement says otherwise. Read-only access after the project is the paid Data Vault add-on; a free BSON database dump is the self-storage route. [R, 2026-10-21] |
| Terms on using data to train AI or ML models | Under the 2026-09-19 terms and privacy policy (researcher B's reading), Fitrockr will not use identifiable customer or participant health data to train general-purpose AI models unrelated to the customer's project. It may create and use aggregated or irreversibly anonymised data, which is not excluded from training. [R, 2026-10-21] |
| Announced shutdowns, deprecations or migrations, with dates | Garmin sync technology change by 7 September 2025: for projects syncing with the Fitrockr app, Garmin no longer provides sleep data for 13 older models (vivosmart 4, vivofit 4, vivomove 3/Style, vivomove Sport, vivoactive 4, Venu Sq, Venu, Lily, Instinct, Instinct Solar, Forerunner 245, 45, 55); Garmin Connect sync is unaffected. The old iOS participant app (id1553631734) no longer has an App Store page; the current app is Fitrockr Sync. The 2026-09-19 terms say third-party integrations are not guaranteed to stay available. [R, 2026-10-21] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Offered where Fitrockr handles protected health information for a HIPAA covered entity; the 2026-09-19 privacy policy says Fitrockr may then act as a Business Associate under a BAA (researcher B's reading). The BAA text is not published. [R, 2026-10-21] |
| Whether a data processing agreement is offered | Yes, where required. Fitrockr acts as processor for customer data, and a separate Data Processing Agreement governs the processing. The DPA text is not published. [R, 2026-10-21] |
| Published HIPAA statement | Fitrockr says it complies with HIPAA and markets itself as "HIPAA certified"; a 2023 news post says it "received the certification" but names no certifier (HHS issues no HIPAA certification). The 2026-09-19 privacy policy adds that processing health data does not by itself make every service subject to HIPAA. [R, 2026-10-21] |
| Published GDPR statement | Fitrockr (Digital Rebels GmbH, Berlin) says it complies with GDPR, acts as data processor for customer data under German law, and (2026-09-19 privacy policy) uses Chapter V transfer mechanisms for data leaving the EEA. [R, 2026-10-21] |
| ISO/IEC 27001 status and evidence | Claimed for the cloud hosting centre only, not for Fitrockr itself; the hosting provider and certificate are not named, and no certificate naming Fitrockr or Digital Rebels GmbH was found. Fitrockr separately claims Google CASA certification, with no letter of validation published. [R, 2026-10-21] |
| SOC 2 status and evidence | Not public [2026-10-21] |
| FDA clearances, from the FDA database | Not public [2026-10-21] |
| Where data is stored, and residency options | Default hosting in an ISO-certified data centre in Germany (included); the security help page says Germany or Switzerland. Hosting in a country of the customer's choice (for example the US), on-premise self-hosting and military on-premise hosting in a closed network are add-ons. [R, 2026-10-21] |

<!-- facts:end -->

### Terra

<!-- facts:begin terra -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | No academic or research-access programme for outside researchers. The nearest route is the Terra Startup Accelerator (up to $100,000 in API credits over up to six months), whose FAQ says research projects are eligible if Terra is credited. "Terra Research" is Terra's in-house team publishing its own analyses of pooled end-user data, not an access programme. [C, 2026-10-21] |
| Who can join the research program | **Startup Accelerator:** Pre-revenue or early-revenue teams that cannot yet afford paid API access, with health data central to the product. Research projects qualify if health data is central to the work and Terra is credited in resulting publications and datasets. [V, 2026-10-21] |
| How to apply, and any approval or review step | **Startup Accelerator:** Short-answer online form (about 20 to 30 minutes), rolling admission, decision within 10 business days, about 0.8% of applications accepted. A card is required to activate the credits. [V, 2026-10-21] |
| Whether the program is active, paused, renamed or closed | **Startup Accelerator:** Open, rolling admission (2026-10-21). [V, 2026-10-21] |
| Whether the general developer or API program is open to new applicants | Open and self-serve. Sign up on the dashboard, choose a plan and get API keys; there is no separate gating step for production. The Terms add compliance reviews (questionnaires, information requests) that Terra may run for development or production access. [V, 2026-10-21]<br>**Garmin through Terra:** Terra's Garmin integration page now says the customer supplies its own Garmin app credentials and applies at developerportal.garmin.com. Until at least 2026-10-14 the same page said Terra manages the Garmin credentials. With Garmin's own programme taking no new applications, a new Terra customer may have no Garmin route. [V, 2026-10-21]<br>**Google Health and Fitbit through Terra:** Terra's docs say Terra manages the credentials for its Google Health connection (the Google Health API replacement for the Fitbit Web API), so the customer registers no Google app; each user re-consents once. Its Fitbit (legacy Fitbit Web API) page says the same for Fitbit. Google Health became generally available in Terra connections in August 2026. [V, 2026-10-21]<br>**WHOOP, Strava, Dexcom, Huawei (bring your own credentials):** The customer supplies its own provider credentials for WHOOP, Strava, Dexcom and Huawei, so the study needs its own developer approval from each of these providers. [V, 2026-10-21] |
| Participant or user limits before approval or by tier | Testing and staging environments are capped at 50 connected users each; production has no user cap and is billed per active authentication. The Streaming add-on's included credits cover 20 active streaming users a month. [V, 2026-10-21] |
| How academic access differs from commercial or consumer access | No academic tier or academic terms; universities buy the same plans. Three terms matter for research use: free development accounts are for internal evaluation only (no pilot study on a sandbox); the customer Terms bar publicly disseminating information on the performance of the Services or Output (clause 1.2(v)), which reaches methods papers that report on Terra data quality or delivery; and accelerator credits require crediting Terra in publications and datasets. [V, 2026-10-21] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | n/a |
| Consumer subscription or membership price | n/a |
| Research or academic pricing or discount | Not public [2026-10-21] |
| Fees for API, SDK, platform or data access | Quick Start: $399/month billed annually or $499/month billed monthly, with 100,000 credits a month. An active authentication (one connected source for one end user) costs 200 credits a month; the first 400 events per authentication are free, then 0.5 credits per event. Credits beyond 100,000 cost $0.005 (to 1,000,000) and $0.003 above. Streaming API add-on $99/month (20,000 credits, about 20 active streaming users). Graph API from $50 for 2 graphs a month. Enterprise is custom. [V, 2026-10-21] |
| Minimum order, term or commitment | Monthly, or annual paid upfront. Annual renewals need at least 60 days' notice to cancel; monthly can be cancelled any time in the current period, but the customer stays liable for that period. 30-day money-back guarantee. [V, 2026-10-21] |
| Whether pricing requires contacting sales | No for Quick Start and the published add-ons. Yes for Enterprise (custom plans, signed BAA, dedicated server, data storage) and for any non-profit or special pricing. [V, 2026-10-21] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | Unified API passes through what each provider exposes, unsmoothed: sample arrays such as heart rate, RR interval, HRV, SpO2, glucose, position and raw ECG voltage where the provider supplies them; no raw PPG, no raw uncalibrated CGM. The Streaming API add-on carries roughly per-second heart rate, HRV, RR interval, ECG, acceleration and gyroscope from BLE/ANT+ devices, Wear OS, Apple Watch and phone sensors. [V, 2026-10-21] |
| Derived or processed metrics available to researchers | Provider summaries (daily, activity, sleep, body, nutrition, menstruation) normalised to Terra's schema, plus Terra's own Health Scores (recovery, strain, stress, immunity and others) and Models. Smart Fill (August 2026, called "health context" in the product blog) imputes missing sleep, daily and activity values, with a confidence value on every estimated cell. Terra does not compute derived metrics such as speed from position samples. [V, 2026-10-21] |
| Documented sampling rates or temporal resolution | Set by each device and provider, passed through unchanged (for example Huawei heart rate about once a minute). Cloud integrations are event-driven or polled by Terra every 5 to 10 minutes. Streaming API events arrive roughly once per second per stream. [V, 2026-10-21] |
| How far back data can be retrieved | By default data flows only from connection onward. Historical pulls depend on the provider: Garmin up to 5 years, Google Health up to the last 12 months on connect (returned by REST, not pushed), Polar and Health Connect 30 days and never before the user granted permission. A single request may span at most 1,825 days. [V, 2026-10-21] |
| Export, API, SDK or file routes | Event-based push to a configured destination: webhooks, Postgres/MySQL, Supabase, S3, GCS, Azure Blob, SQS, Kafka, MongoDB, Firestore. REST endpoints for historical backfill. Mobile SDKs for Apple Health, Samsung Health and Health Connect (on-device sources have no cloud route). Output in Terra format, FIT or FHIR. Streaming websocket as an add-on. [V, 2026-10-21] |
| API rate limits | The Rate Limits reference sets two per-user rules on data-read endpoints (at most 1,825 days per request; at most 6,000 requested days per user per hour, HTTP 429, raisable per dev_id). The environments page says Terra imposes no rate limits on the REST API. Webhook delivery is not rate-limited; provider limits apply and are shared across all of a customer's users. (conflict) [U, 2026-10-21] |
| Terms on retaining, storing or deleting data | End User Privacy Policy (updated 2026-09-24): end-user data is usually kept two days after collection, in rare cases up to six months, and never more than six months, with exceptions (an active connection, legal duty, separate user permission, misuse investigation). Aggregated or de-identified derivatives may be kept longer for research, analytics and service improvement. DPA: personal data deleted or returned within 90 days of termination. Storage is an Enterprise feature. [V, 2026-10-21] |
| Terms on using data to train AI or ML models | No clause names AI or model training for end-user data. The End User Privacy Policy lets Terra use collected data for product development and to conduct "statistical, scientific, or market research" and publish aggregated or de-identified results, and to keep de-identified derivatives without a stated limit. The research wording was added between 2025-10-16 and 2026-02-24. Terra's Integration Onboarding Terms (updated 2026-10-12) let Terra use de-identified data from partner integrations for any lawful purpose. Anthropic and OpenAI are subprocessors for AI-assisted support on anonymised end-user data, with a customer opt-out. [V, 2026-10-21] |
| Announced shutdowns, deprecations or migrations, with dates | Fitbit connection runs on the legacy Fitbit Web API (Google sunset September 2026); move users to the Google Health connection, which needs every user to sign in again and gets a new user_id. July 2026: provider fitbit_v2 renamed google_health, old name rejected; Biostrap deprecated. Web Google connection (Google Fit REST) must move to Google Health before Google ends Fit API support at the end of 2026; the Health Connect SDK route is unaffected. Peloton and Technogym removed. Legacy JavaScript SDK no longer updated. Phased move to the access.tryterra.co/api/v2 base URL. [V, 2026-10-21] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | A signed BAA is listed on the Enterprise plan only, not on Quick Start. [C, 2026-10-21] |
| Whether a data processing agreement is offered | A Data Processing Addendum (updated 2026-09-24, with EU SCCs and the UK addendum) forms part of the Terms and is accepted with them. Subprocessor changes are posted at least 10 days ahead. [C, 2026-10-21] |
| Published HIPAA statement | Terra says it is HIPAA compliant and adheres to HIPAA standards. Self-declared. [C, 2026-10-21] |
| Published GDPR statement | Terra says it is GDPR compliant; its GDPR page (updated 2026-03-01) offers a downloadable GDPR assessment via a Vanta trust centre. The DPA covers EU SCCs and the UK transfer addendum. [C, 2026-10-21] |
| ISO/IEC 27001 status and evidence | Not public [2026-10-21] |
| SOC 2 status and evidence | Terra says it is SOC 2 Type II certified, with an annual SOC 2 Type II audit (Security, Confidentiality, Availability). No report or auditor seen. [C, 2026-10-21] |
| FDA clearances, from the FDA database | Not public [2026-10-11] |
| Where data is stored, and residency options | Primary processing in the United Kingdom and the Netherlands, with transfers to the US possible. End-user data hosting subprocessors (AWS, Google Cloud, ClickHouse Cloud) are listed in the US, UK and EU; support tools (Zendesk, HyperDX, Anthropic, OpenAI) in the US. Enterprise offers a dedicated instance in a chosen region; no region choice is documented for Quick Start. [V, 2026-10-21] |

<!-- facts:end -->

### Thryve

<!-- facts:begin thryve -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | **Thryve Research Partners:** Research Partners route ("Become a Partner"): describe the study, then get Thryve's research infrastructure, documentation and compliance materials and study setup support. Sold alongside a Multimodal Clinical Trial Platform built on the white-label Pulsatio participant app. It is the commercial platform with onboarding support, not a separate academic data-access program. [V, 2026-10-21]<br>**Terve Research:** Terve Research: a European research platform for academic and medical institutions, announced 31 August 2026, funded by Huawei and run by Thryve (mHealth Pioneers GmbH) on its white-label platform. Closed studies recruit their own participants; open studies can enrol Huawei wearable users across Europe. Researchers get joint-controllership and ethics-committee templates; selected studies may receive sponsored devices and implementation support. [C, 2026-10-21] |
| Who can join the research program | **Thryve Research Partners:** Unclear<br>**Terve Research:** Aimed at European academic and medical institutions; participants need a compatible Huawei device at launch. No selection criteria for researchers or sponsored studies are published. [C, 2026-10-21] |
| How to apply, and any approval or review step | **Thryve Research Partners:** "Become a Partner" contact route: describe the research, then configure participant flows, device connections and data collection with Thryve support. No review criteria or timeline published. Self-serve alternative: the 14-day trial or Start Up plan via Stripe checkout. [V, 2026-10-21] |
| Whether the program is active, paused, renamed or closed | **Thryve Research Partners:** Active: research partner and research organization pages live as of 2026-10-21. [V, 2026-10-21]<br>**Terve Research:** Not live as of 2026-10-21. The 31 August 2026 announcement says two clinical studies launch in September, but terveresearch.com still says "launching soon" and collects early-access emails, and no Terve app from mHealth Pioneers appears in the Apple App Store (DE, GB, FI storefronts, 2026-10-21). (conflict) [U, 2026-10-21] |
| Whether the general developer or API program is open to new applicants | Open and self-serve: 14-day free trial (25 users) through Stripe checkout, card and business email required, converting automatically to the Start Up plan at EUR 499 per month unless cancelled. Personal email addresses are refused. [V, 2026-10-21] |
| Participant or user limits before approval or by tier | **Thryve plans:** End users included: Free Trial 25, Start Up 500 (extra users EUR 0.50 each), Scale Up 5,000 (extra EUR 999 per 10,000 users), Enterprise flexible. [V, 2026-10-21]<br>**Google Health API route (own OAuth client):** A study connecting Google Health through Thryve uses its own Google OAuth client and is capped by Google at 100 users until OAuth verification and the CASA assessment are complete. The on-device route (Apple Health or Health Connect) has no such cap. [V, 2026-10-21] |
| How academic access differs from commercial or consumer access | Not public [2026-10-21] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | n/a |
| Consumer subscription or membership price | n/a |
| Research or academic pricing or discount | Not public [2026-10-21] |
| Fees for API, SDK, platform or data access | **Thryve plans:** Start Up from EUR 499 per month (500 users, 1 app, EUR 0.50 per extra user); Scale Up from EUR 1,000 per month (5,000 users, EUR 999 per extra 10,000; only for startups founded less than 10 years ago); Enterprise bespoke. Foundational analytics included at no extra charge; further analytics upon request. [V, 2026-10-21]<br>**Google Health API route (own OAuth client):** Third-party cost on top of Thryve fees: a CASA security assessment for restricted health scopes, paid to a Google-authorised assessor and renewed annually. Google states $500 to $4,500 by app complexity; Thryve says it typically starts around EUR 1,000 and upwards. The on-device route avoids CASA. [C, 2026-10-21] |
| Minimum order, term or commitment | **Start Up plan:** Start Up is monthly and cancellable at any time; the trial needs a card and converts to Start Up after 14 days. Scale Up and Enterprise terms not published. [V, 2026-10-21] |
| Whether pricing requires contacting sales | Start Up is self-serve with a public price; Scale Up is "Contact Us"; Enterprise is bespoke through sales. [V, 2026-10-21] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | No sensor-level raw signals (accelerometer, PPG) from web sources: Thryve passes on the manufacturer-processed values each source exposes, at the source's finest granularity, without pre-aggregating. Through the Apple Health SDK module it reads heartbeat series and ECG; ThryveBLE (beta) connects Bluetooth heart rate and glucose monitors directly. [V, 2026-10-21]<br>**Garmin Companion module (SDK 5.3.0):** Real-time Bluetooth streaming from paired Garmin devices into the app and Thryve's warehouse: heart rate, beat-to-beat intervals (BBI), SpO2, respiration, stress, steps, calories, floors, Body Battery and intensity minutes. Needs Garmin Connect on the phone and a Garmin Companion licence string, which Garmin issues per application ID on request through Thryve support. [V, 2026-10-21]<br>**Google Health on-device route:** The Google Health app writes Fitbit and Pixel data into Apple Health or Health Connect and Thryve reads it with its SDK, with no Google OAuth client, verification or CASA. On Health Connect this includes heart rate, resting heart rate, HRV, skin temperature, respiratory rate and blood glucose. [C, 2026-10-21] |
| Derived or processed metrics available to researchers | 250+ harmonized data types (source-provided daily and epoch values); Foundational Analytics (standardized data and derived definitions such as a main-sleep period) included for all clients since December 2025; sleep, health status and health risk analytics upon request. [V, 2026-10-21] |
| Documented sampling rates or temporal resolution | Set by each source: epoch values to second precision where provided, but Polar hourly and Fitbit intraday mostly only during recorded activities and sleep. Retrieval latency: bulk sources polled at most every 15 minutes, including Google Health direct (scheduled, up to 15 minutes delay). Garmin Companion streams in real time over Bluetooth. [V, 2026-10-21] |
| How far back data can be retrieved | Default backfill of 14 days before user creation (configurable down to 0); Start Up and Scale Up up to 14 days, Enterprise flexible. Per source: Polar none; Health Connect beyond 30 days needs an extra user permission; Google Health lookback not defined by Google. Per API call: 30 days epoch, 364 days daily. [V, 2026-10-21] |
| Export, API, SDK or file routes | REST Wearable API v5 (epoch and daily endpoints) by pull, or webhooks (notifications and data push); native SDKs for iOS and Android plus Flutter and React Native for on-device sources; Thryve dashboard. [V, 2026-10-21]<br>**Google Health:** Two routes. (A) Direct: the customer brings its own OAuth client tied to its own Google Cloud project and verified app, passes Google OAuth verification and an annual CASA assessment, and is capped at 100 users until both are done; Thryve then retrieves data as a web bulk source with no shared client. (B) On-device: Thryve's SDK reads what the Google Health app writes into Apple Health or Health Connect, avoiding Google credentials, verification and CASA. [V, 2026-10-21] |
| API rate limits | Not public [2026-10-21] |
| Terms on retaining, storing or deleting data | Thryve keeps data for the plan's storage window: 1 day (trial), 2 weeks (Start Up), 1 month (Scale Up), flexible (Enterprise), so studies must pull or receive data continuously. Stored data types are configurable. Users are deleted by API asynchronously from midnight UTC after the deletion date (default seven days ahead). [V, 2026-10-21] |
| Terms on using data to train AI or ML models | Unclear |
| Announced shutdowns, deprecations or migrations, with dates | **Fitbit Web API source:** Thryve's Fitbit source ends with Google's Fitbit Web API shutdown. Dates disagree: Thryve's docs table said 29 October 2026 until late October and now marks Fitbit "Deprecated" with no date, next to a new Google Health source (ID 49); Thryve's blog (updated 29 September 2026) says Google extended the cut-off to 30 October, while older paragraphs of the same post still say 30 September and that no extension was communicated; Google's own docs now say 2 November 2026. Within 24 hours of the shutdown Thryve disconnects all Fitbit connections; already-ingested data stays. Every user must re-authorize through Google Health (route A or B, see export_routes). (conflict) [C, 2026-10-30]<br>**Google Health integration status:** Thryve's Google Health page still says the integration is available on fast-track request ahead of full public release, while its blog says connection flows were released 20 July 2026 and full integration with scheduled retrieval on 15 August 2026. (conflict) [U, 2026-10-21]<br>**Samsung Health SDK module:** Old Samsung Health module (shealth) deprecated 16 April 2026 and removed in Thryve SDK 5.3.0; the replacement uses Samsung's Health Data SDK, and users must reconnect because Samsung does not support migrating connections. [V, 2026-10-21]<br>**Google Fit sources:** GoogleFitREST and GoogleFitNative are end of life; closed to new apps since 1 May 2024, existing integrations working until 2026. [V, 2026-10-21] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Thryve says a BAA is standard on every plan, not only Enterprise. No signed agreement seen. [C, 2026-10-21] |
| Whether a data processing agreement is offered | DPA standard on every plan; Thryve acts as data processor for the customer. Terve Research instead offers joint-controllership templates. [C, 2026-10-21] |
| Published HIPAA statement | Self-declared HIPAA compliant; raw data tokenized at ingestion. [C, 2026-10-21] |
| Published GDPR statement | Self-declared GDPR compliant; data pseudonymized behind a Thryve user token and hosted in Germany. [C, 2026-10-21] |
| ISO/IEC 27001 status and evidence | Claims ISO/IEC 27001 and ISO 9001 certification, recertified in 2025. Certificates only through a request form, so certifier, scope and expiry are not public. [C, 2026-10-21] |
| SOC 2 status and evidence | Not public [2026-10-21] |
| FDA clearances, from the FDA database | Not public [2026-10-21] |
| Where data is stored, and residency options | All data processed and stored in Germany; no other region option published. Terve Research is hosted on T Cloud Public, Germany. [V, 2026-10-21] |

<!-- facts:end -->

## Key Links

- Fitabase: https://www.fitabase.com/ · pricing: https://www.fitabase.com/how-it-works/pricing/
- Fitabase API knowledge base: https://www.fitabase.com/resources/knowledge-base/fitabase-api/what-is-the-fitabase-api/
- Fitabase Google Health API migration (key dates, dataset availability): https://www.fitabase.com/resources/knowledge-base/google-health-api-migration/key-dates/ · https://www.fitabase.com/resources/knowledge-base/google-health-api-migration/dataset-availability/
- Fitrockr pricing (moved from /research/pricing/; site blocks automated access): https://www.fitrockr.com/pricing/
- Terra: https://tryterra.co/integrations/garmin · pricing: https://tryterra.co/pricing · docs: https://docs.tryterra.co/
- Terra Startup Accelerator: https://tryterra.co/startup-accelerator
- Thryve pricing: https://www.thryve.health/pricing · research partners: https://www.thryve.health/research-partners · compliance: https://www.thryve.health/certifications-compliance
- Thryve Fitbit migration options (updated 29 September 2026): https://www.thryve.health/blog/fitbit-shutdown-september-2026-migration-options
- Validic Fitbit→Google transition guide: https://help.validic.com/space/VCS/5513478151/Fitbit+to+Google+Health+API+Developer+Transition+Guide
- Thryve: https://www.thryve.health/blog/fitbit-api-deprecation
- Rook: https://docs.tryrook.io/data-sources/garmin/
- Sahha: https://sahha.ai/blog/fitbit-api-sunset-migration/
- Open Wearables: https://openwearables.io/
- MyDataHelps Apple HealthKit ECG export format: https://support.mydatahelps.org/apple-healthkitv2-electrocardiogram-export-format
- All of Us Fitbit resources: https://support.researchallofus.org/hc/en-us/articles/20281023493908-Resources-for-Using-Fitbit-Data
- All of Us data types: https://support.researchallofus.org/hc/en-us/articles/4619151535508-Data-Types-and-Organization

## Sources

See `../sources.md` entries S-INT-01 through S-INT-08.

Added 2026-10-10 (all accessed 2026-10-10; rows proposed for `../sources.md`):

1. Fitabase homepage, pricing page, Engage page, FAQ, privacy notice and terms. https://www.fitabase.com/ ; https://www.fitabase.com/how-it-works/pricing/ ; https://www.fitabase.com/engage/ ; https://www.fitabase.com/resources/faq/ ; https://www.fitabase.com/privacy/ ; https://www.fitabase.com/terms/
2. Fitabase research library. https://www.fitabase.com/research-library/ . 1,650 publications, last updated 5 October 2026.
3. Labfront pricing. https://www.labfront.com/pricing . Tiers, analytics add-ons from $3,000 plus $50 per participant, Developer Access from $4,000, Data Audit from $500.
4. Fitrockr research pricing, research grants and compatible devices. https://www.fitrockr.com/research/pricing ; https://www.fitrockr.com/research/research-grants/ ; https://www.fitrockr.com/compatible-devices/
5. Terra pricing. https://tryterra.co/pricing . Quick Start $499 per month or $399 billed annually, 100,000 credits; BAA on Enterprise.
6. Thryve pricing. https://www.thryve.health/pricing . Start Up from €499 per month (500 users), Scale Up from €1,000 per month (5,000 users), storage windows, compliance FAQ.

Added 2026-10-22, vendor fact records (every quote and retrieval date is in the record file; the main source URLs are listed here):

7. Fitabase fact record, `../../facts/fitabase.yaml` (judged 2026-10-21). Sources include https://www.fitabase.com/how-it-works/customers/ ; https://www.fitabase.com/resources/knowledge-base/learn-about-fitbit-data/data-resolutions/ ; https://www.fitabase.com/resources/knowledge-base/learn-about-garmin-data/garmin-datasets/ ; https://www.fitabase.com/resources/knowledge-base/learn-about-garmin-data/collecting-enhanced-beat-to-beat-interval-data-using-garmin-devices/ ; https://www.fitabase.com/blog/post/garmin-cirqa-screenless-device-for-research/ ; https://www.fitabase.com/blog/post/relaunch-of-fitabase-engage/ ; https://www.fitabase.com/blog/post/webhooks/ ; https://www.fitabase.com/blog/post/google-health-api-fitbit-project-extensions/ ; https://www.fitabase.com/resources/knowledge-base/google-health-api-migration/dataset-availability/ ; https://www.fitabase.com/resources/knowledge-base/working-with-the-irb/data-security-privacy/ ; https://www.fitabase.com/resources/knowledge-base/working-with-the-irb/example-irb-text/ ; https://apps.apple.com/us/app/fitabase-engage/id6496601338 ; Data Privacy Framework registry https://www.dataprivacyframework.gov/list (participant 7900).
8. Labfront fact record, `../../facts/labfront.yaml` (judged 2026-10-11). Sources include https://www.labfront.com/pricing ; https://help.labfront.com/pricing-plans-and-payment-1 ; https://help.labfront.com/terms-of-service ; https://help.labfront.com/developer-access ; https://help.labfront.com/movesense-overview ; https://help.labfront.com/dexcom-overview ; https://www.labfront.com/collaborator ; https://www.labfront.com/grant ; https://help.labfront.com/privacy-policy ; https://help.labfront.com/security-statement ; https://help.labfront.com/privacy-and-security-faqs ; https://www.labfront.com/trust-security ; https://www.labfront.com/blog/retroactively-collect-garmin-data ; Data Privacy Framework registry (participant 9072).
9. Fitrockr fact record, `../../facts/fitrockr.yaml` (judged 2026-10-21; mostly Reported, site blocks scripts). Sources include https://www.fitrockr.com/pricing/ (live reading 2026-10-21) and Wayback captures of https://www.fitrockr.com/research/pricing/ ; https://www.fitrockr.com/help-center/data-dictionary/ ; https://www.fitrockr.com/research/help-center/hrv-via-garmin-connect-sync/ ; https://www.fitrockr.com/research/help-center/important-update-upcoming-transition-to-new-garmin-sync-technology/ ; https://www.fitrockr.com/health-solutions/terms-of-use/ ; https://www.fitrockr.com/health-solutions/privacy-policy/ ; https://www.fitrockr.com/features/ ; https://www.fitrockr.com/help-center/pricing-plans-payment/ ; Garmin's release https://www.garmin.com/en-PH/newsroom/press-release/news-2026-mar-fitrockr/ .
10. Terra fact record, `../../facts/terra.yaml` (judged 2026-10-21). Sources include https://tryterra.co/pricing ; https://docs.tryterra.co/unified-api/pricing ; https://tryterra.co/terms-of-service ; https://tryterra.co/startup-accelerator ; https://tryterra.co/integrations/garmin ; https://docs.tryterra.co/help-center/help-topics/data-api-sdk/account-config-environments-and-going-live/fitbit-to-google-migration ; https://docs.tryterra.co/reference/health-and-fitness-api/rate-limits ; https://tryterra.co/end-user-privacy ; https://tryterra.co/integration-partner-terms ; https://tryterra.co/dpa ; https://tryterra.co/privacy/subprocessors ; https://docs.tryterra.co/changelog/2026/august-update-2026 .
11. Thryve fact record, `../../facts/thryve.yaml` (judged 2026-10-21). Sources include https://www.thryve.health/pricing ; https://www.thryve.health/free-trial ; https://www.thryve.health/research-partners ; https://terveresearch.com ; https://www.thryve.health/news/thryve-huawei-terve-research-partnership ; https://www.thryve.health/blog/fitbit-shutdown-september-2026-migration-options ; https://docs.thryve.health/thryve-data-sources/garmin-health-companion ; https://docs.thryve.health/thryve-data-sources/overview ; https://www.thryve.health/certifications-compliance ; https://developers.google.com/health/app-verification .
