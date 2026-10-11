# Evidation

## Quick Facts

| Field | Details |
|---|---|
| Organization | Evidation Health, Inc., San Mateo, California, USA. Founded 2012. The consumer app has been branded Achievement, MyEvidation and now Evidation |
| Category | Commercial participant-network and real-world-data platform. **Not a passive phone-sensing platform**, see the scope note in the Summary. Collects wearable data through connected consumer accounts, plus surveys, and links it to claims, EHR and biosample data for sponsors |
| Current status | **Active.** Sponsor services live. An autoimmune temporal proteomics cohort launched in January 2026 and a GLP-1 insights release followed in July 2026 [28, 22]. Chief executive Leslie Oley Wilberforce was appointed 2025-03-06 and chief medical officer Dr. Ghazanfar Khan 2025-12-02 [17]. The three studies on the public join-research page (heart health, migraines, diabetes) all show enrollment closed (2026-10-11) [26]. Vendor pages fetched 2026-09-03 also describe 20 or more condition cohorts and a 2026 dermatology cohort (Reported; the dermatology cohort was not on the newsroom on 2026-10-11) |
| Platforms/devices | Consumer app "Evidation" on the App Store (seller Evidation Health, Inc., v7.4.0, 2026-10-02, iPhone only, iOS 16.4 or later) and Google Play (`com.achievemint.android`, updated 2026-10-04, 1M+ downloads) (Verified 2026-10-11) [12]. Wearable data arrives only through members' connected third-party apps, not from the devices directly; the help centre lists 12 (Apple Health, Dexcom, Fitbit, Garmin, Google Fit, MyFitnessPal, Oura, Qardio, RunKeeper, Samsung Health, Strava, Withings), while 2026-09-03 vendor pages said 20 or more [23]. Licensed-platform customers get their own branded apps, built and run by Evidation (Corroborated) [15] |
| Open source | **No.** No public repositories, SDK or self-hosting route found |
| Hosting/deployment | Evidation-managed only. Sponsors either commission studies that run on Evidation's member base or license the Research & Engagement Platform, which Evidation runs for them (Our Future Health, UK, chose it in November 2023; 2026 status unconfirmed) [14, 16]. No self-hosting or on-premises option is documented (Corroborated) |
| Pricing model | **Non-public.** Sponsors buy through the contact form or partner@evidation.com; no fee is published for any offering [13, 22]. No separate academic tier, terms or price: academic institutions are grouped with non-profit customers (Corroborated) [14]. The member app is free and members are paid in points, with a $10 reward at 10,000 points [12, 23]. Academics can reach the Evidation-built American Life in Realtime data through USC's Understanding America Study Data Use Agreement (see Data Access) |
| Last verified | 2026-10-11 (vendor fact record). ALiR access terms and the Everyone Registry abstract last checked 2026-10-10 |

## Summary

- Evidation is a company that maintains a consented member base and sells access to studies run on it. The vendor states 5 million members across 97 percent of United States ZIP codes, more than 140 studies supported and more than 100 peer-reviewed publications (Reported, vendor figures).
- It belongs in this module because it is a route to wearable plus survey data at a scale no self-run platform reaches, and because the two largest engagement analyses in this knowledge base ran on it. It sits at the edge of scope because the sponsor never operates the software. A team does not configure sensors or host servers, and even on the licensed platform Evidation runs the app and infrastructure.
- The data model is a direct connection to individuals rather than a study app. Members connect an existing wearable account, answer daily or weekly survey cards and earn points. Sponsors receive longitudinal, patient-level data from cohorts built by therapeutic area and demographics.
- The strongest published evidence is about engagement rather than sensing. Six participant-centric studies on the platform retained a median 77.2 percent of participants, and an Evidation cohort of 89,479 people completed more than two million daily surveys in five months (Verified from the two papers, see Research Evidence).
- Closest comparators in this knowledge base are the data intermediaries in Module 1, which move wearable data but do not hold a member base, and the commercial platforms in this module, which a team configures itself.

## Products / Platform Architecture

- **Evidation app (members).** Connects health apps and devices, delivers survey and reading cards, pays points for health actions such as walking and sleeping. The vendor lists condition programmes including Heart Health with the American College of Cardiology, Flu Smart and MigraineSmart (Reported).
- **Sponsor platform (life sciences).** Cohort building by therapeutic area and demographics, near real-time wearable measures correlated with events, patient-reported outcomes and linkage to clinical, claims, demographic and molecular data (Reported, vendor pages).
- **Condition cohorts.** Cardiometabolic, autoimmune and dermatology cohorts are named, with a total of 20 or more (Reported).
- **Study platform for external consortia.** The vendor states it provided data collection, processing and storage for the BUMP pregnancy study with 4YouandMe, and integrated Medicare claims, HealthKit and ePRO data for the Heartline study with Apple Watch (Reported; both are confirmed by the papers below).
- **Licensed Research & Engagement Platform.** Sponsors can license the participant platform instead of using Evidation's member base; Evidation runs it, including a sponsor-branded participant app and infrastructure. Our Future Health (UK) selected it in November 2023; whether it still runs on Evidation in 2026 is unconfirmed (Verified for the offering, Corroborated for the branded apps) [15, 16].
- **Temporal proteomics platform.** Launched January 2026 with an initial autoimmune cohort that includes proteomics sampling and continuous wearable capture; data are analysed with Evidation's proprietary AI foundation models (Verified, press release; no technical documentation) [28].
- **Cohort data and insights.** A July 2026 release offers data, on-demand analyses and population-level insights from a GLP-1 cohort of more than 165,000 people through partner@evidation.com [22].

## Sensors and Data Streams

- Every Module 2 profile uses the same table so platforms can be compared row by row. Rows are the passive streams named in `CLAUDE.md`. "Yes" and "No" are used only where a primary source says so; "Unclear" means the vendor documentation fetched does not say.
- Evidation's documented inputs are connected wearable accounts and survey cards. No vendor page fetched lists any phone sensor the app reads itself. The privacy notice states that geolocation may be collected depending on device and app settings, but that notice covers the websites as well as the app.

| Stream | Android | iOS | Raw or derived | Sampling configurable | Notes |
|---|---|---|---|---|---|
| GPS / location | Unclear | Unclear | Unclear | No | Privacy notice mentions geolocation; no research use documented. |
| Accelerometer | No | No | Not applicable | No | Not documented as a phone stream. Activity arrives from connected wearables. |
| Gyroscope | No | No | Not applicable | No | Not documented. |
| Magnetometer | No | No | Not applicable | No | Not documented. |
| Barometer | No | No | Not applicable | No | Not documented. |
| Ambient light | No | No | Not applicable | No | Not documented. |
| Proximity | No | No | Not applicable | No | Not documented. |
| Device motion / activity recognition | Unclear | Unclear | Derived | No | Step counts come from connected apps, including phone-based Apple Health. Google Fit connections were withdrawn on iOS and the website (help article updated 2026-04-07); Android status not stated [23]. |
| Screen state | No | No | Not applicable | No | Not documented. |
| App usage | No | No | Not applicable | No | Not documented. |
| Battery / charging | No | No | Not applicable | No | Not documented. |
| Network / connectivity | No | No | Not applicable | No | Not documented. |
| Wi-Fi | No | No | Not applicable | No | Not documented. |
| Bluetooth | No | No | Not applicable | No | Not documented. |
| Calls (metadata) | No | No | Not applicable | No | Not documented. |
| SMS (metadata) | No | No | Not applicable | No | Not documented. |
| Keyboard | No | No | Not applicable | No | Not documented. |
| Audio / microphone | No | No | Not applicable | No | Not documented. |
| Notifications | No | No | Not applicable | No | Not documented. |
| Device information | Yes | Yes | Event | No | Privacy notice: device identifiers, advertising identifiers and IP address are collected. |

**Verification.** "No" rows record that the vendor pages fetched on 2026-09-03 (home, research, how-it-works, about, privacy) do not document the stream. The Member Privacy Notice (last updated 2026-07-13) was read for the vendor fact record on 2026-10-11 for retention, residency and AI terms, not re-checked row by row against this table. Treat the table as Reported.

### Connected-device streams

| Stream | Source devices named | Resolution reaching sponsors | Notes |
|---|---|---|---|
| Steps and activity | Fitbit, Apple Health, Garmin, Oura, and others among the connectable apps | Not documented by the vendor. The six-cohort paper and ALiR report daily and intraday minute-level data for those studies, which is not a delivery standard [6, 10, 24] | The vendor cites 951 billion member steps in 2021 (Reported). |
| Sleep | Fitbit, Oura, Apple Watch, Garmin | Nightly summaries | Used in the influenza and COVID detection papers. |
| Heart rate and resting heart rate | Fitbit, Oura, Apple Watch, Garmin | Daily and intraday, device dependent | Basis of the vaccination-response and infection-detection work. |
| Skin temperature | Oura | Nightly | Named in the healthcare-worker stress and recovery study. |
| ECG and irregular rhythm notifications | Apple Watch, Heartline study only | Event level | Combined with Medicare claims. |
| Surveys and patient-reported outcomes | Evidation app cards | Daily, weekly or event-triggered | The core active stream. |
| Health records | EHR via 1upHealth Patient Connect (FHIR), integrated October 2024 | Not documented | Members permission their own records [27]. |

- Device data reaches Evidation only through the member's connected third-party app account, not from the wearable directly. Whether sponsors receive raw, intraday or daily-summary data is not documented (Verified) [23, 24].
- Member data syncs every 4 to 6 hours per the website FAQ and every 4 to 5 hours per the help centre; both say up to 24 hours to appear. No temporal resolution for delivered device data is published [23].
- On connection, Evidation may pull up to 30 days of data the third-party app recorded before the connection [18].

## Derived Metrics / Analytics

- Vendor pages describe digital measures developed in-house, disease event and prevention modelling, patient segmentation and near real-time correlation of wearable data to events (Reported, no method documentation fetched).
- Named processed measures from connected apps are activity, steps, sleep, heart rate and HRV, alongside program-level analytics, executive-ready reports and member characterisation. No metric list or definitions are published (Corroborated) [15, 28].
- Published analytics run on the platform include influenza detection from wearable data and symptoms, COVID-19 test-resource optimisation, vaccination-effect detection in wearable metrics and stress heterogeneity from multimodal sensors (see Research Evidence).
- No participant-facing metric catalogue was fetched. Members receive personalised insights, a monthly migraine report and health tips (Reported).

## Active Data Collection

- Survey cards delivered in the app, answered for points. Daily surveys ran for five months in the 2020 influenza and COVID cohort and daily or weekly surveys for up to 15 months in comparable studies (Verified, Cho et al. 2025).
- Reading cards, health tips and programme content are delivered through the same feed.
- Patient-reported outcomes and event reports, including symptom, treatment and flare logging, are the basis of the condition cohorts (Reported).
- No documentation fetched on branching, randomised timing, cognitive tasks or audio diaries. Treat these as Unclear.

## Researcher and Study Management Features

- Sponsors work with Evidation staff rather than a self-service console. The public material describes cohort building, recontact of members, precision recruitment of high-risk participants and multi-source data linkage (Reported).
- Recruitment reach is the distinctive feature. The BUMP study enrolled 524 pregnant women through a patient portal, paid and unpaid social media and a community health partner, with a 23.6 percent enrolment rate from interest forms over 25 weeks (Verified, Harry et al. 2025).
- Sponsors start through the contact page or partner@evidation.com. No application form, review step or timeline is published. Evidation prepares recruitment content to fit the sponsor's IRB submission [13, 28].
- Members must be US residents aged 18 or over. Each study sets its own criteria through a screener, and members opt in per study from in-app or email invitations; a new Research tab in the app gathers these opportunities [19, 23].
- No public dashboard, role model, audit log or adherence-monitoring documentation was found.

## Data Access and Export

- Sponsors receive de-identified, individual-level datasets as a one-time extract or by subscription with recurring updates, plus structured analysis-ready study datasets, executive-ready reports and on-demand analyses of existing cohorts (Verified) [24, 22]. Format, schema, transfer mechanism and latency are not published (Unclear). The depth of history in sponsor datasets is not published either.
- Members can see and control what they share, with whom and for how long, and consent to each data request (Reported, vendor pages).
- The American Life in Realtime (ALiR) dataset, collected with a study app that Evidation helped design and build ("designing and building the study app", acknowledgments) and provisioned Fitbit Inspire 2 devices, is distributed through USC's Understanding America Study (UAS). The Data Availability statement says UAS "makes deidentified study data available to registered researchers (who sign the Data Use Agreement)", with ALiR data to follow curation of one full year for the whole panel (anticipated late 2025). ALiR Fitbit data "include both minute-level sensor data and Fitbit's aggregated metrics". Funded by the National Library of Medicine (R01LM013237). **Verified 2026-10-10** from the full text (Angrisani et al. 2025, *PNAS Nexus*, PMC12501968). Whether the full ALiR wearable files are already downloadable could not be confirmed without a UAS login. This is the one documented route by which academics can obtain Evidation-collected data without sponsoring a study.
- **Evidation Everyone Registry** (Reported, ISPOR 2026 poster abstract by Evidation staff: Martin, Ramirez, Khan): "a longitudinal, person-centered data resource" combining wearable data, patient-reported outcomes and optional EHR linkage, launched 2025-12-22 to a selected sample of 5,800 members, with over 3,800 consented by 2026-01-08; 75% of consenters opted to include EHR data and 97% of participants have connected at least one wearable. The abstract does not say whether outside researchers can access it. Evidation's registry page (2025-12-18) says member data are coded before being shared with "research partners", with no criteria or terms for who qualifies (Verified) [20].
- **WAVE study** (NCT06207929; sponsor Evidation Health, collaborator BARDA; 18,157 enrolled; 2024-01-21 to 2024-08-07). The protocol and consent allow sharing coded data with approved external research partners, but individual-data sharing is marked undecided and the process not finalised (Verified, ClinicalTrials.gov) [21].
- **GLP-1 cohort.** Data and on-demand analyses from more than 165,000 people are offered through partner@evidation.com, a commercial route [22].
- None of these is an open academic route to existing Evidation data.
- No public API, bulk export tool or self-service data download for researchers was found.
- Members can request a .json export of their Evidation data by email from account settings; it covers only the last year. Data from a sponsored program is requested through support and routed to the study team or sponsor [25].

## APIs, SDKs, and Extensibility

- No public developer program, API documentation or SDK (not public, Verified). developer.evidation.com, api.evidation.com and docs.evidation.com did not resolve and the evidation-health GitHub organisation has no public repositories (2026-10-11). The member and website terms mention "our API documentation", but that is boilerplate also present in the November 2021 terms and does not show an open program [19].
- Integration is inbound only, through the 20 or more consumer health apps and devices members can connect.

## Deployment and Infrastructure

- Evidation-managed only. Member data are stored primarily in US data centres (Corroborated, vendor notices) [18]. Sponsors deploy nothing themselves: Evidation either runs the study on its member base or runs a licensed Research & Engagement Platform for the sponsor, with a branded app and infrastructure [14, 15].
- The licensed platform has one documented non-US deployment: Our Future Health (UK) chose it in November 2023. Its 2026 status, and any residency or data processing terms for it, are not published [16].
- Studies run on Evidation's existing member base or on cohorts recruited into it. External consortia have used the platform as their data collection and storage layer (BUMP, Heartline).
- Hardware provisioning has been done for specific studies, for example the Fitbit Inspire 2 in American Life in Realtime (Verified, Angrisani et al. 2025).

## Participant Experience

- Members install one consumer app, connect an existing wearable account and answer cards. Rewards are points redeemable for cash or charity; 10,000 points gives a $10 digital reward (Verified) [23]. Where a study needs a device, Evidation ships it to the participant at no cost [26].
- The vendor states that members give consent every time their data is requested (Reported).
- Retention across six participant-centric studies stayed above 80 percent in the first month and above 50 percent for each study's full active period, with a median of 77.2 percent retained (Verified, Goodday et al. 2024).
- Adherence was population dependent. Median adherence for Oura, Garmin and Apple Watch tasks exceeded 80 to 90 percent except in severely ill cancer and postpartum populations, where physical, mental and situational barriers dominated (Verified, Goodday et al. 2024).
- Underrepresented populations retained at lower rates than White participants across recruitment channels in BUMP (Verified, Harry et al. 2025).

## Privacy, Security, and Compliance

- The corporate privacy notice fetched on 2026-09-03 describes identifiers, device information, geolocation and usage data, sharing with service providers and affiliates, disclosure of de-identified information, and a CCPA opt-out for sales or sharing. It states the company does not knowingly sell or share personal information of minors under 16 (Verified from the notice).
- The Member Privacy Notice (last updated 2026-07-13) governs the app [18]. It states US data centres (primarily), up to 30 days of earlier data pulled when a third-party app is connected, use of member personal information in machine learning and other AI methods for certain services, and retention for as long as reasonably necessary, with research-program retention set by each study's informed consent. Member terms bar members from using the services or data for AI purposes. No terms on sponsors training models on licensed data are published [18, 19].
- Archived study data are not deleted on request, at least under the RESHAPE consent; account deletion is irreversible. Retention terms binding sponsors are not published [29].
- No SOC 2, ISO 27001, HIPAA or GDPR statement appears in text. The our-solutions page shows badge images only, with alt texts for HIPAA, GDPR, "FDA 21 CFR Part 1" (probably Part 11, electronic records), BARR, Cyber Essentials Plus and CCPA/CPRA [13]. A badge gives no scope, so HIPAA and GDPR are Unclear; SOC 2 and ISO 27001 are not public (the BARR badge names no framework). evidation.com/security and /trust return HTTP 404. evidation.com publishes a security.txt naming vuln@evidation.com, a disclosure contact rather than certification evidence.
- No BAA or data processing agreement is published [13, 18].
- No FDA 510(k), PMA or establishment registration matches Evidation or Achievemint in openFDA (2026-10-11) [30].
- Consent is described as per-request and revocable (Reported).

## Pricing

- Non-public. Sponsors buy through the contact form or partner@evidation.com, which also offers existing cohort data and on-demand analyses; a quote is required in practice, inferred from no price being published (Corroborated) [13, 22].
- The pricing models are published (datasets per extract or by subscription, a licensed platform, cohort data and analyses by arrangement) but no fee for any of them. Hosting for the licensed platform is bundled into a licence whose price is not published. No minimum commitment is published [15, 24].
- Member-side costs are zero; members are paid in points.
- No academic pricing, per-participant fee or minimum commitment was found. Academic institutions are offered the same solutions as other non-profits, with no separate tier (Corroborated) [14]. The academic data route that does exist is ALiR via the UAS Data Use Agreement, which involves no payment to Evidation (see Data Access and Export).

## Research Evidence and Validation

The papers stored in [`../literature/evidation/`](../literature/evidation/) are the deployment-relevant subset of a much larger Evidation-affiliated literature. A Europe PMC search on 2026-09-03 returned 142 hits for the company name with wearable and digital-health terms.

- **Goodday et al. 2024, *JMIR*, six-cohort engagement analysis.** Frontline healthcare workers, pregnancy, cancer and other populations; median retention 77.2 percent, interquartile range 72.6 to 88 percent; barriers were task burden, physical or situational inability and low perceived benefit. Verified from full text, and a Module 3 candidate.
- **Cho et al. 2025, *Lancet Digital Health*, adherence and retention factors.** Secondary analysis of a Duke study and an Evidation study; the Evidation arm had 89,479 participants with demographic data completing 2,080,992 daily surveys over five months, mean 23 surveys per participant. Verified from full text, and a Module 3 candidate.
- **Harry et al. 2025, *JMIR Formative Research*, BUMP recruitment.** 524 women aged 18 to 40; social media recruitment reached underrepresented groups, community partnership enrolled 5 of 57 engaged. Verified from full text.
- **Angrisani et al. 2025, *PNAS Nexus*, American Life in Realtime.** Probability-sampled cohort drawn from the Understanding America Study, provisioned Fitbit Inspire 2, at least one year of data per person, positioned as benchmark data for equity in precision health. Verified from full text.
- Further platform-based papers found but not stored: influenza detection from wearables and symptoms (2024), COVID-19 testing optimisation with wearables (2024), vaccination effects in wearable metrics (2023), machine-learning COVID detection from wearables (2023), stress heterogeneity from multimodal sensors (2023). All are Evidation-affiliated and open access.

## Strengths

- Recruitment scale and reach that no self-run platform matches, with recontactable members across conditions.
- Existing linkage to claims, EHR and biosamples alongside wearable and survey data.
- Published, quantified engagement evidence from its own studies, including honest reporting of low-adherence populations.
- Device-agnostic wearable intake through consumer account connections.

## Limitations

- The sponsor operates nothing. Sensor configuration, hosting, raw data access and export format are all in the vendor's hands.
- No phone sensing beyond what connected apps supply. Not a substitute for a Beiwe or AWARE deployment where GPS, screen or communication streams matter.
- Pricing, security certification and data delivery mechanics are undocumented publicly.
- Evidation's own member base is US-only (members must be US residents aged 18 or over) [19]. The only documented non-US route is the licensed platform, chosen by Our Future Health in the UK in 2023, with 2026 status unconfirmed [16].
- Google Fit connections were withdrawn on iOS and the website in 2026, while the store listings and help-centre list still name it [23, 12].
- The Member Privacy Notice permits machine learning and AI use of member data for certain services; terms for sponsor AI use of licensed data are not published [18].
- The vendor's own publication and study counts differ between pages (140 or more studies and 100 or more publications on the home page; 175 or more studies and 70 or more publications on the about page). Recorded as conflicting, not reconciled.

## Best-Fit Use Cases

- Large observational cohorts needing thousands of wearable-connected participants quickly.
- Real-world evidence for life-sciences sponsors, especially where claims or EHR linkage is needed.
- Studies of engagement and retention at population scale.
- Nationally representative person-generated health data with provisioned devices, as in American Life in Realtime.

## Poor-Fit Use Cases

- Any study requiring raw phone sensor streams, custom sampling schedules or researcher-hosted data.
- Small academic studies without sponsor budgets (secondary analysis of ALiR data via UAS is the exception).
- Studies outside the United States that need Evidation's member base. The licensed platform is the only documented non-US route (Our Future Health, 2026 status unconfirmed).
- Work needing an auditable, self-service study console.

## Open Questions

- What does a sponsor actually receive, in what format and at what latency?
- Which security certifications, if any, does the platform hold? (Still open 2026-10-11: no security or trust page exists; the our-solutions page shows HIPAA, GDPR, BARR and Cyber Essentials Plus badges with no statement or scope.)
- Does the app read any phone sensors itself, or only connected accounts?
- ~~Is there any academic or non-commercial access route?~~ Partly answered 2026-10-10: no academic program on Evidation's pages, but ALiR data reach academics through USC's UAS Data Use Agreement. Partly answered 2026-10-11: the Evidation Everyone Registry shares coded data with "research partners", but who qualifies is not stated; WAVE data sharing is undecided.
- Does Our Future Health still run on Evidation's licensed platform in 2026, and under what residency and data processing terms?
- Are Google Fit connections still available on Android?
- ~~What are the access terms for the American Life in Realtime benchmark dataset?~~ Answered 2026-10-10: UAS registration plus Data Use Agreement (see Data Access and Export).

These are logged as Q125 in `shared/unresolved-questions.md`.

## Vendor Fact Record

<!-- facts:begin -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | **Sponsors:** No academic or self-serve research program and no data API. Evidation sells sponsor services built on its US member community: data offerings (licensed real-world datasets, patient insights, prospective studies) and activation offerings (recruitment, activation), as one-time engagements or ongoing subscriptions, plus a licensable Research & Engagement Platform that Evidation runs for the sponsor. [V, 2026-10-11]<br>**Outside researchers seeking existing Evidation data:** No open-access route to existing Evidation data. Three published routes each stop short of one: (1) the Evidation Everyone Research Registry codes member data before sharing it with "research partners", with no criteria or terms for who counts as a partner; (2) the WAVE study (NCT06207929, sponsor Evidation Health, collaborator BARDA, 18,157 enrolled, 2024-01-21 to 2024-08-07) plans to share coded data with approved external research partners, but its individual-data sharing is marked undecided and the process not finalized; (3) a July 2026 release offers data, on-demand analyses and population-level insights from a GLP-1 cohort of more than 165,000 people through partner@evidation.com, which is a commercial route. [V, 2026-10-11] |
| Who can join the research program | **Sponsors:** Sponsors are organisations (biopharma, consumer health, technology, non-profit, government). No eligibility criteria for sponsors are published. [V, 2026-10-11]<br>**Members (Evidation app):** Members must be US residents aged 18 or over; each study sets its own criteria through a screener. [V, 2026-10-11] |
| How to apply, and any approval or review step | **Sponsors:** Sponsors start through the "working with us" contact route or partner@evidation.com. No application form, review step or timeline is published. Evidation prepares recruitment content to fit the sponsor's IRB submission. [V, 2026-10-11]<br>**Members (Evidation app):** Members see study invitations in the app or by email, complete a screener and are told whether they qualify; each study is opt-in. [V, 2026-10-11] |
| Whether the program is active, paused, renamed or closed | Sponsor services active. An autoimmune temporal proteomics cohort launched in January 2026 and a GLP-1 insights release followed in July 2026; the member app's new Research tab gathers programs and research opportunities. On the public join-research page the three listed studies (heart health, migraines, diabetes) all show enrollment closed. [V, 2026-10-11] |
| Whether the general developer or API program is open to new applicants | Not public [2026-10-11] |
| Participant or user limits before approval or by tier | Not public [2026-10-11] |
| How academic access differs from commercial or consumer access | No separate academic tier, terms or price. Academic institutions are grouped with non-profit customers and offered the same solutions (recruitment, patient insights, real-world studies, licensing the Research & Engagement Platform, or having Evidation run the study). Members get the app free and are paid in points; they are participants, not data customers. [C, 2026-10-11] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | n/a |
| Consumer subscription or membership price | **Members (Evidation app):** The Evidation member app is free; members are paid in points, with a $10 reward at 10,000 points. [V, 2026-10-11] |
| Research or academic pricing or discount | Not public [2026-10-11] |
| Fees for API, SDK, platform or data access | Not public [2026-10-11] |
| Minimum order, term or commitment | Not public [2026-10-11] |
| Whether pricing requires contacting sales | **Sponsors:** Yes in practice. No price is published for any sponsor offering, and the only published routes to buy are the contact form and partner@evidation.com. [C, 2026-10-11] |
| Price of managed hosting | **Licensed Research & Engagement Platform:** Not public [2026-10-11]<br>**Data licensing, insights and recruitment engagements:** n/a |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | Device data reaches Evidation only through members' connected third-party apps (Apple Health, Dexcom, Fitbit, Garmin, Google Fit, MyFitnessPal, Oura, Qardio, RunKeeper, Samsung Health, Strava, Withings), not from the wearables directly, plus surveys and EHR records linked through 1upHealth's Patient Connect. Sponsors receive it in licensed de-identified individual-level datasets (PROs and surveys, behavioural and functional measures, connected device and wearable data, clinical data, molecular data where available). Whether wearable data is delivered at raw, intraday or daily-summary level is not documented. [V, 2026-10-11] |
| Derived or processed metrics available to researchers | Vendor-processed measures from connected apps (activity, steps, sleep, heart rate, HRV), digital measures from wearables, program-level analytics, executive-ready reports and member characterization. No metric list or definitions are published. [C, 2026-10-11] |
| Documented sampling rates or temporal resolution | Not public [2026-10-11] |
| How far back data can be retrieved | **Connected third-party apps:** On connection, Evidation may pull data the third-party app recorded up to 30 days before the member connected it; after that, data accrues for as long as the member stays connected. [V, 2026-10-11]<br>**Member self-export:** A member's detailed data export covers only the last year. [V, 2026-10-11]<br>**Sponsor datasets:** Not public [2026-10-11] |
| Export, API, SDK or file routes | Sponsors: licensed de-identified individual-level datasets (one-time extract or subscription), structured analysis-ready study datasets, reports, and on-demand analyses of existing cohorts. No public API or SDK. Members: a .json export of their own Evidation data by email from account settings; data from a sponsored program is requested through support and routed to the study team or sponsor. [V, 2026-10-11] |
| API rate limits | n/a |
| Terms on retaining, storing or deleting data | **Member and research-participant data:** Member data is kept as long as reasonably necessary for the service, legal obligations and other legitimate business purposes. Retention for research-program data is set by each program's informed consent, and study data already archived into a study dataset is not deleted on request. Account deletion is irreversible. Retention terms binding sponsors that receive data are not published. [V, 2026-10-11] |
| Terms on using data to train AI or ML models | The Member Privacy Notice (last updated 2026-07-13) lets Evidation use member personal information in machine learning and other AI methods for certain services, and Evidation analyses cohort data with its own AI foundation models. Members themselves are barred from using the services or related data for AI purposes. No terms on sponsors training models on licensed data are published. [V, 2026-10-11] |
| Announced shutdowns, deprecations or migrations, with dates | Google Fit connections were withdrawn on iOS and the Evidation website after a Google change (help article updated 2026-04-07; no withdrawal date given). Members are told to switch to Apple Health or another source. [V, 2026-10-11] |
| Software licence of the platform's components | **Licensed Research & Engagement Platform:** Proprietary. The participant platform is licensed commercially and run by Evidation (Our Future Health in the UK chose it in November 2023). No open-source components; the evidation-health GitHub organisation has no public repositories. [V, 2026-10-11]<br>**Data licensing, insights and recruitment engagements:** n/a |
| Self-hosting and managed-hosting options | **Licensed Research & Engagement Platform:** Evidation-managed only. Sponsors either license the Research & Engagement Platform, which Evidation runs (including the participant-facing app and infrastructure, as for Our Future Health), or have Evidation manage the study end to end. No self-hosting or on-premises option is documented. [C, 2026-10-11]<br>**Data licensing, insights and recruitment engagements:** n/a |
| App store availability on iOS and Android | **Evidation member app:** Evidation member app on the App Store (iPhone only, iOS 16.4 or later) and on Google Play (1M+ downloads), published by Evidation Health, Inc. (iOS id 793039965, Android package com.achievemint.android). This is the app participants use in data, recruitment and Evidation-run engagements. [V, 2026-10-11]<br>**Sponsor-branded apps on the licensed platform:** Licensed-platform customers get their own branded apps, which Evidation builds and runs (for example the Our Future Health participant app, accessible by app or browser). These are listed under the customer's name, not Evidation's. [C, 2026-10-11] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-11] |
| Whether a data processing agreement is offered | Not public [2026-10-11] |
| Published HIPAA statement | Unclear |
| Published GDPR statement | Unclear |
| ISO/IEC 27001 status and evidence | Not public [2026-10-11] |
| SOC 2 status and evidence | Not public [2026-10-11] |
| FDA clearances, from the FDA database | Not public [2026-10-11] |
| Where data is stored, and residency options | Member data is stored primarily in US data centres. No residency options are published for sponsors or for licensed deployments outside the US. [C, 2026-10-11] |

<!-- facts:end -->

## Key Links

- Official site: https://evidation.com/
- Sponsor solutions: https://evidation.com/for-customers/our-solutions
- Licensed platform: https://evidation.com/for-customers/our-platform
- Datasets: https://evidation.com/for-customers/datasets
- Non-profit and academic: https://evidation.com/for-customers/non-profit
- Member Privacy Notice: https://evidation.com/members-privacy
- Member terms: https://evidation.com/members-terms
- Help centre: https://help.evidation.com/
- Research page: https://evidation.com/research
- How it works (members): https://evidation.com/how-it-works
- About: https://evidation.com/about
- Privacy notice: https://evidation.com/privacy
- Evidation app: https://apps.apple.com/us/app/evidation-earn-health-rewards/id793039965 ; https://play.google.com/store/apps/details?id=com.achievemint.android
- Understanding America Study data portal (ALiR access): https://uasdata.usc.edu/
- Contact/sales: https://evidation.com/contact ; partner@evidation.com
- Developer/API documentation: none found
- GitHub: none found
- Pricing: not public

## Sources

1. Evidation home page, https://evidation.com/, fetched 2026-09-03. Member, study and publication counts, cohort list, news items.
2. Evidation research page, https://evidation.com/research, fetched 2026-09-03. Case-study framing and research areas.
3. Evidation how-it-works page, https://evidation.com/how-it-works, fetched 2026-09-03. Member experience, connected apps, programmes.
4. Evidation about page, https://evidation.com/about, fetched 2026-09-03. Founding year, study counts, Heartline, BUMP and American Life in Realtime descriptions.
5. Evidation privacy notice, https://evidation.com/privacy, fetched 2026-09-03. Data categories, sharing, CCPA opt-out.
6. Goodday SM, et al. Value of Engagement in Digital Health Technology Research: Evidence Across 6 Unique Cohort Studies. *J Med Internet Res* 2024;26:e57827. doi:10.2196/57827. PDF stored.
7. Cho PJ, Olaye IM, Shandhi MMH, Daza EJ, Foschini L, Dunn JP. Identification of key factors related to digital health observational study adherence and retention by data-driven approaches. *Lancet Digit Health* 2025;7(1). doi:10.1016/s2589-7500(24)00219-x. Full-text XML stored; PDF render failed.
8. Harry ML, et al. Using Social Media to Engage and Enroll Underrepresented Populations: Longitudinal Digital Health Research. *JMIR Form Res* 2025;9:e68093. doi:10.2196/68093. PDF stored.
9. Angrisani M, et al. American Life in Realtime: Benchmark, publicly available person-generated health data for equity in precision health. *PNAS Nexus* 2025;4(10):pgaf295. doi:10.1093/pnasnexus/pgaf295. PDF stored.
10. Angrisani et al. 2025, *PNAS Nexus*, full text XML via Europe PMC (PMC12501968), Data Availability, Methods and Acknowledgments sections (accessed 2026-10-10). **Primary/Verified.** UAS Data Use Agreement route, minute-level Fitbit data, Evidation's role in the study app, NLM funding.
11. ISPOR 2026 poster abstract, "Inclusive Health Research in the Palm of Your Hand: The Evidation Everyone Registry." https://www.ispor.org/heor-resources/presentations-database/presentation-cti/ispor-2026/poster-session-4-3/inclusive-health-research-in-the-palm-of-your-hand-the-evidation-everyone-registry (accessed 2026-10-10). **Reported** (vendor-authored abstract).
12. App Store (id 793039965) and Google Play (`com.achievemint.android`) listings, and HTTP checks of evidation.com/security and /trust (404), 2026-10-10; listings rechecked 2026-10-11 (iPhone only, iOS 16.4 or later, 1M+ downloads, free). https://apps.apple.com/us/app/evidation-earn-health-rewards/id793039965 ; https://play.google.com/store/apps/details?id=com.achievemint.android. **Primary/Verified.**
13. Evidation our-solutions and contact pages, https://evidation.com/for-customers/our-solutions ; https://evidation.com/contact, 2026-10-11. Sponsor offerings, sponsor types, contact route, compliance badge images. **Primary/Verified.**
14. Evidation non-profit page, https://evidation.com/for-customers/non-profit, 2026-10-11. Academic institutions grouped with non-profits; licensing or end-to-end management. **Primary.**
15. Evidation platform page, https://evidation.com/for-customers/our-platform, 2026-10-11. Licensed Research & Engagement Platform, customer apps, analytics. **Primary.**
16. "Evidation Selected by Our Future Health as Participant Platform for UK's Largest Health Research Program", https://evidation.com/resources/evidation-selected-by-our-future-health-as-participant-platform-for-uks-largest-health-research-program (dateline 2023-11-16), 2026-10-11. **Primary.** 2026 status unconfirmed.
17. Evidation press releases on leadership, https://evidation.com/resources/evidation-appoints-leslie-oley-wilberforce-as-ceo (2025-03-06) and https://evidation.com/resources/evidation-appoints-dr-ghazanfar-khan-as-chief-medical-officer (2025-12-02), 2026-10-11. **Primary/Verified.**
18. Evidation Member Privacy Notice (last updated 2026-07-13), https://evidation.com/members-privacy, and Consumer Health Data Privacy Notice, https://evidation.com/consumer-health-data-privacy-notice, 2026-10-11. Retention, 30-day lookback, AI use, US data centres. **Primary/Verified.**
19. Evidation member terms, https://evidation.com/members-terms, and website terms, https://evidation.com/terms, 2026-10-11. US residents 18+, AI-purpose ban, API boilerplate. **Primary/Verified.**
20. Evidation Everyone Research Registry page, https://evidation.com/blog/shape-the-future-of-health-research (2025-12-18), 2026-10-11. Coded data shared with research partners. **Primary/Verified.**
21. ClinicalTrials.gov NCT06207929 (WAVE), https://clinicaltrials.gov/study/NCT06207929, read via the v2 API, 2026-10-11. **Primary/Verified.**
22. "Growth Potential and Uneven Adoption in the GLP-1 Market", https://evidation.com/resources/growth-potential-and-uneven-adoption-in-the-glp-1-market (July 2026), and newsroom, https://evidation.com/newsroom, 2026-10-11. **Primary/Verified.**
23. Evidation help centre: currently available apps (https://help.evidation.com/hc/en-us/articles/360008060493-Currently-available-apps), data syncing (https://help.evidation.com/hc/en-us/articles/360012493253-Data-syncing-101), Google Fit changes (https://help.evidation.com/hc/en-us/articles/50630998040211-How-to-Earn-Activity-Points-After-Google-Fit-Connection-Changes, updated 2026-04-07), getting started, research participation and what's new articles; website sync FAQ (https://evidation.com/frequently-asked-questions/how-long-does-it-take-to-sync-my-data), 2026-10-11. **Primary/Verified.**
24. Evidation datasets page, https://evidation.com/for-customers/datasets, 2026-10-11. Extract or subscription licensing, data categories. **Primary/Verified.**
25. Evidation data download FAQ, https://evidation.com/frequently-asked-questions/how-do-i-download-my-data, and help article on collected data (last-year export), 2026-10-11. **Primary/Verified.**
26. Evidation join-research page, https://evidation.com/join-research, 2026-10-11. Studies listed as enrollment closed; devices shipped at no cost. **Primary/Verified.**
27. "Evidation Partners with 1upHealth", https://evidation.com/resources/evidation-partners-with-1uphealth-to-integrate-diverse-sources-of-permissioned-real-world-health-data-for-research, 2026-10-11. **Primary.**
28. "Evidation Launches Temporal Proteomics Platform and Autoimmune Cohort", https://evidation.com/resources/evidation-launches-temporal-proteomics-platform-and-autoimmune-cohort (January 2026), and recruit page, https://evidation.com/for-customers/recruit, 2026-10-11. **Primary/Verified.**
29. RESHAPE Study Informed Consent Form (help centre) and data deletion FAQ, https://evidation.com/frequently-asked-questions/how-do-i-delete-my-data, 2026-10-11. **Primary/Verified.**
30. openFDA 510(k), PMA and registration queries for Evidation and Achievemint, e.g. https://api.fda.gov/device/510k.json?search=applicant:evidation, 2026-10-11 (no matches). **Primary/Verified.**
