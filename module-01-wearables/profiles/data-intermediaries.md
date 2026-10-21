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

**Last verified:** 2026-08-21; Fitabase, Labfront, Fitrockr, Terra and Thryve pricing and access terms re-verified 2026-10-10.

**Dated context, 2026-10-10.** Two vendor routes these platforms sit on top of are closed to new direct applicants: Google is "not onboarding new projects" on the Google Health API and turns the legacy Fitbit Web API off on 30 October 2026 (`fitbit-google.md`), and Garmin has paused new Connect Developer Program access requests since spring 2026 (Corroborated; `garmin.md`). For a new study, an intermediary that already holds access is currently the main way to reach Garmin data. For Fitbit, unified APIs (Thryve, Validic) require each customer's own Google Cloud project, verified app and CASA (Corroborated). The Google Health app's writes to Apple Health and Health Connect give an on-device route with no Google Health API project (Corroborated; `../../facts/fitbit-google.yaml`, 2026-10-11). **Update 2026-10-21.** Google's notice was removed by 2026-10-19, so the Google Health API is apparently open to new projects again (Corroborated, no announcement). A study can apparently open its own project, with Google's restricted-scope review and, above 100 users, verification and CASA. The Garmin pause is unchanged.

---

## Category 1, Research operations platforms

These supply participant management, adherence monitoring, and de-identified export. They are what
a research team buys because Fitbit and Garmin do not provide it.

### Fitabase, **the incumbent for Fitbit/Garmin research**

| Field | Detail | Confidence |
|---|---|---|
| Supports | Fitbit and Garmin; study-controlled or participant-owned devices | **Verified** |
| Granularity | Daily, hourly, **minute-level**; CSV export | **Verified** |
| Study tooling | Monitoring dashboards, device battery and sync status, participant tagging, de-identified profiles, customizable data capture windows, unlimited batch exports | **Verified** |
| API | Aggregate Data API for programmatic export in JSON/CSV | **Verified** |
| Coming | "Fitabase Engage": the Mobile App and Engage Wrist App are labelled "Preview · Summer 2026" on the Engage page (re-read 2026-10-10); SMS messaging is listed without a status. No Engage price is published | **Verified** (vendor-stated) |
| Track record | Homepage: used in "over 1,100 research studies"; research library: "1650 publications have used Fitabase", last updated 5 October 2026 (both read 2026-10-10) | **Reported** (vendor claims; counting methods not stated) |
| Pricing | **Not public.** "Custom Pricing for Every Study"; Premium Add-Ons (SMS Messages & Reminders; Aggregate Data API) also unpriced; contact hello@fitabase.com | **Verified** that it is non-public (re-read 2026-10-10) |
| Compliance | FAQ: "the option to run your project completely de-identified" and "robust industry standards". The FAQ, privacy notice and terms pages contain no HIPAA, BAA or PHI wording (text search, 2026-10-10) | **Verified** that nothing is published |

Fitabase is the single most important non-device entity in Module 1. If a study is using Fitbit and
does not have engineering capacity, Fitabase is effectively the default, and its (unpublished) cost
should be budgeted from the start. Note that Fitabase's Engage roadmap moves it toward the survey/
EMA territory of the Module 2 platforms, a convergence worth tracking.

Open question: does Fitabase execute a HIPAA BAA as standard? Its de-identification framing suggests
a deliberate strategy of staying outside PHI, which is a different compliance posture from a BAA.
**Unclear, ask directly.**

### Labfront, published pricing

**Added 2026-08-21 second pass.** Labfront was missing from the first draft. It is one of two
research-operations platforms in this file that publish their prices (Fitrockr, below, is the other;
corrected 2026-10-10, the 2026-08-21 text called Labfront the only one).

| Field | Detail | Confidence |
|---|---|---|
| Devices supported | **Garmin** (vívosmart 5, vívoactive 5, Index BPM, Index S2 scale), **Movesense Medical, HR2 and Flash** (participants start each Movesense recording manually; updated 2026-10-11 from `../../facts/movesense.yaml`), **Dexcom G7 CGM** | **Verified** |
| Garmin data | **Beat-to-Beat Interval**, steps, heart rate, oxygen saturation, respiration, accelerometer, naps, wheelchair activities | **Verified** |
| Movesense data | **RR-interval, ECG, IMU, accelerometer, gyroscope, magnetometer** | **Verified** |
| **Higher resolution than stock** | Labfront has a Garmin partnership letting it **configure devices via the Garmin Health SDKs to increase sensor resolution**, capturing higher-resolution data than Garmin normally collects, explicitly including beat-to-beat/interbeat intervals for HRV | **Corroborated** |
| Included in all tiers | Physiological data collection, **survey tools (EMA)**, event tracking | **Verified** |

#### Published pricing, **Verified** (labfront.com/pricing, re-read 2026-10-10)

| Tier | Price | Participants | Notes |
|---|---|---|---|
| **Tester** | **Free** | 5 | 30-day data access window; limited sampling rates on some devices; all settings enabled so you can confirm a protocol works |
| **Basic** | **$500 / year** | 20 included, **$10** each additional | Unlimited data history; **one** device integration (Garmin *or* Dexcom); standard sampling rates |
| **Advanced** | **$1,250 / year** | 20 included, **$25** each additional | Unlimited data history; **all** integrations (Garmin, Dexcom, Movesense); **customisable sampling rates, "from 100 Hz accelerometry down to beat-to-beat intervals for HRV"** |
| Analytics packages | from **$3,000** plus **$50 per participant** (HRV linear from $4,000; HRV non-linear from $6,000; sleep actigraphy from $3,000; sleep regularity and timing from $5,000) | | Optional add-ons; require Advanced. Developer Access from $4,000; Data Audit from $500. (The 2026-08-21 figure of $2,000 is superseded.) |

Labfront also runs a **grants programme** providing subsidised platform access, analytics packages
and devices to researchers at every career stage on a rolling basis, plus hardware discounts through
its Garmin and Movesense partnerships. Named examples include a Sleep Research Society Foundation
sleep grant and an ACSM-linked award. **Corroborated.**

#### Why this changes the picture

A 40-participant Garmin study with high-resolution BBI and EMA costs **$1,250 + 20 × $25 = $1,750
per year** in platform fees, plus devices. That is a fully specified, publicly quotable budget line, which only Labfront and Fitrockr permit among the research platforms here.

It also **removes the Garmin SDK licence question from the critical path** for many studies: rather
than negotiating a Garmin Health SDK licence, a team can buy Labfront Advanced and inherit Labfront's
partnership-derived ability to raise sampling resolution.

**Labfront vs Fitabase, briefly:**

| | Labfront | Fitabase |
|---|---|---|
| Devices | Garmin, Movesense, Dexcom | **Fitbit**, Garmin |
| Pricing | **Published** | Custom quote only |
| EMA/surveys | **Included in all tiers** | "Engage" suite, Summer 2026 |
| Free tier | **Yes, 5 participants** | No |
| Track record | Smaller; grant-driven academic focus | **1,100+ studies** (homepage) and **1,650 publications** (research library, updated 5 October 2026), vendor figures |
| Fitbit support | **No** | Yes |

If your study is Fitbit-based, Fitabase remains the main research-operations option (Fitrockr also lists Google/Fitbit). If it is Garmin-based,
Labfront is cheaper, transparent, includes EMA, and adds Movesense and CGM; Fitrockr is the other published-price option.

Links: https://www.labfront.com/ · https://www.labfront.com/pricing · https://www.labfront.com/compatible-devices · https://www.labfront.com/grant · https://help.labfront.com/garmin-overview

### Fitrockr, published pricing and Garmin research grants (added 2026-10-10)

| Field | Detail | Confidence |
|---|---|---|
| Organization | Fitrockr (Berlin) | **Reported** |
| Devices | Claims "700+ wearables"; the compatible-devices page lists Garmin, Apple, Google, Fitbit, Samsung, Withings, Polar, WHOOP, Oura, Dexcom and others, via direct integrations and Apple Health / Health Connect | **Reported** (vendor) |
| Study tooling | Participant compliance and adherence tracking, tasks and scheduled push notifications, multi-language participant apps, dashboards, raw data downloads; surveys and notifications are a paid add-on (+20% on licence) | **Reported** (vendor) |
| Pricing, research and clinical trials | Trial free for 2 weeks, up to 5 device connections. **Basic** from €50 or $55 per month (standard wearable data); **Pro** from €150 or $165 per month ("enhanced" wearable data, additional data types, higher sampling rates). Both: 5 device licences included, unlimited users, 3-month minimum contract and renewals; additional device licences €1 to €7.50 per month on Basic and €1 to €15 on Pro. Add-ons include raw accelerometer (25 Hz) and gyroscope (32 Hz) at +25% on licence, API access +20%, on-premise hosting €5,000 + 20%, and a Data Vault at €150 per month for post-project access | **Verified** (fitrockr.com/research/pricing, 2026-10-10) |
| Hosting and compliance | Germany cloud included; country-of-choice cloud, local or on-premise hosting as add-ons. States "HIPAA-, CASA- and ISO-certified. GDPR-compliant." with no certificate linked | Hosting **Verified** (pricing page); compliance **Reported** (vendor claim) |
| Grants | Fitrockr's grants page: "Fitrockr and Garmin support innovative research through grant programs". The Garmin Health x Fitrockr Health Solutions Research Grant Asia 2026 (five vívoactive 5 units) closed on 31 March 2026; an earlier Fitrockr and Garmin Health grant for projects up to 50 participants closed 31 August 2025; no current grant is listed | **Verified** (fitrockr.com, 2026-10-10) |

Pricing is per connected device licence rather than per participant, so devices reused across
sequential participants are licensed once (inference from the licence model; confirm with Fitrockr).

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
| **Terra API** | Unified API across many wearable brands; widely referenced as the default for multi-brand integration | Reported |
| **Validic** | Long-established health data connectivity vendor; publishes a Fitbit → Google Health API developer transition guide, indicating active maintenance through the 2026 migration | Reported |
| **Thryve** | EU-based health data API; publishes analysis of the Fitbit API deprecation | Reported |
| **Rook** | Wearable/health data API with documented Garmin data-source mapping | Reported |
| **Sahha** | Health data platform; publishes migration guidance for the Fitbit shutdown | Reported |
| **Open Wearables** | **Open-source** wearable API project; has integrated Oura, WHOOP and others as of 2026, and ships an MCP server exposing wearable data to LLM assistants | Reported |

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
  has obvious implications for routing WHOOP data through an intermediary).
- Cost is usage-based. Entry prices are public for some vendors (Verified 2026-10-10): **Terra** Quick Start from $499 per month billed monthly, or $399 per month billed annually, with 100,000 credits per month; a signed BAA is listed only on the custom-priced Enterprise plan. **Thryve** Start Up from €499 per month for up to 500 users (€0.50 per additional user), Scale Up from €1,000 per month for up to 5,000 users, Enterprise bespoke; Thryve's plan table lists data storage of 1 day (free trial), 2 weeks (Start Up) and 1 month (Scale Up), and a "Data processing / Business association agreement" row. Neither publishes academic pricing. Thryve's FAQ calls itself "100% GDPR and HIPAA compliant" (vendor claim, **Reported**).

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
shutoff on 30 October 2026 or to Google's closure of Google Health API onboarding.

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
| Need nocturnal beat-to-beat intervals for HRV | **Garmin Enhanced BBI** via Fitabase or Labfront, no custom app needed |
| Need raw signal | Direct: Polar BLE SDK (cheapest), Movesense (highest rates), Samsung Health Sensor SDK (incl. raw EDA on Galaxy Watch8), Garmin Health SDK, Empatica (EDA), Ultrahuman (ring PPG), Axivity/ActiGraph |
| BYOD, wearable is an intervention not an instrument | Unified API (Terra/Validic/Rook/Thryve) |
| Question can be answered from existing data | All of Us Researcher Workbench or UK Biobank |
| Study uses Fitbit after 30 October 2026 | Fitabase (holds its own project; new-study capacity not stated), or on-device collection via Apple Health or Health Connect. Unified APIs need the customer's own Google Cloud project, verified app and CASA (Corroborated). The study's own Google Health API project is apparently possible again (Corroborated 2026-10-21; Google was not onboarding new projects on 2026-10-10), with restricted-scope review and, above 100 users, verification and CASA |

## Key Links

- Fitabase: https://www.fitabase.com/ · pricing: https://www.fitabase.com/how-it-works/pricing/
- Fitabase API knowledge base: https://www.fitabase.com/resources/knowledge-base/fitabase-api/what-is-the-fitabase-api/
- Terra: https://tryterra.co/integrations/garmin
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
