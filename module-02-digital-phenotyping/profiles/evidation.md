# Evidation

## Quick Facts

| Field | Details |
|---|---|
| Organization | Evidation Health, Inc., San Mateo, California, USA. Founded 2012. The consumer app has been branded Achievement, MyEvidation and now Evidation |
| Category | Commercial participant-network and real-world-data platform. **Not a passive phone-sensing platform**, see the scope note in the Summary. Collects wearable data through connected consumer accounts, plus surveys, and links it to claims, EHR and biosample data for sponsors |
| Current status | **Active.** Vendor pages fetched 2026-09-03 describe 20 or more live condition cohorts, a dermatology cohort launched in 2026 and a new chief executive and chief medical officer appointed in 2026 |
| Platforms/devices | Consumer app on iOS and Android (Corroborated, the privacy notice names both operating systems; store listings not fetched). Wearable data arrives through 20 or more connected apps and devices, including Fitbit, Apple Health, Garmin and Oura |
| Open source | **No.** No public repositories, SDK or self-hosting route found |
| Hosting/deployment | Vendor SaaS only. Sponsors commission studies that run on Evidation's platform and member base; no researcher-run instance exists |
| Pricing model | **Non-public.** Every sponsor-facing page ends in a contact form. Members are paid in points redeemable for cash or charity donations |
| Last verified | 2026-09-03 (first research pass) |

## Summary

- Evidation is a company that maintains a consented member base and sells access to studies run on it. The vendor states 5 million members across 97 percent of United States ZIP codes, more than 140 studies supported and more than 100 peer-reviewed publications (Reported, vendor figures).
- It belongs in this module because it is a route to wearable plus survey data at a scale no self-run platform reaches, and because the two largest engagement analyses in this knowledge base ran on it. It sits at the edge of scope because the sponsor never operates the software. A team does not configure sensors, host servers or own the app.
- The data model is a direct connection to individuals rather than a study app. Members connect an existing wearable account, answer daily or weekly survey cards and earn points. Sponsors receive longitudinal, patient-level data from cohorts built by therapeutic area and demographics.
- The strongest published evidence is about engagement rather than sensing. Six participant-centric studies on the platform retained a median 77.2 percent of participants, and an Evidation cohort of 89,479 people completed more than two million daily surveys in five months (Verified from the two papers, see Research Evidence).
- Closest comparators in this knowledge base are the data intermediaries in Module 1, which move wearable data but do not hold a member base, and the commercial platforms in this module, which a team configures itself.

## Products / Platform Architecture

- **Evidation app (members).** Connects health apps and devices, delivers survey and reading cards, pays points for health actions such as walking and sleeping. The vendor lists condition programmes including Heart Health with the American College of Cardiology, Flu Smart and MigraineSmart (Reported).
- **Sponsor platform (life sciences).** Cohort building by therapeutic area and demographics, near real-time wearable measures correlated with events, patient-reported outcomes and linkage to clinical, claims, demographic and molecular data (Reported, vendor pages).
- **Condition cohorts.** Cardiometabolic, autoimmune and dermatology cohorts are named, with a total of 20 or more (Reported).
- **Study platform for external consortia.** The vendor states it provided data collection, processing and storage for the BUMP pregnancy study with 4YouandMe, and integrated Medicare claims, HealthKit and ePRO data for the Heartline study with Apple Watch (Reported; both are confirmed by the papers below).
- **Temporal proteomics platform.** Announced in 2026 for autoimmune biosample collection (Reported, no technical documentation fetched).

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
| Device motion / activity recognition | Unclear | Unclear | Derived | No | Step counts come from connected apps, including phone-based Apple Health and Google Fit sources. |
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

**Verification.** "No" rows record that the vendor pages fetched on 2026-09-03 (home, research, how-it-works, about, privacy) do not document the stream; the app's privacy notice was not fetched separately and could change a row. Treat the table as Reported.

### Connected-device streams

| Stream | Source devices named | Resolution reaching sponsors | Notes |
|---|---|---|---|
| Steps and activity | Fitbit, Apple Health, Garmin, Oura, and others among the 20 or more connectable apps | Daily and intraday minute-level, per the six-cohort paper | The vendor cites 951 billion member steps in 2021 (Reported). |
| Sleep | Fitbit, Oura, Apple Watch, Garmin | Nightly summaries | Used in the influenza and COVID detection papers. |
| Heart rate and resting heart rate | Fitbit, Oura, Apple Watch, Garmin | Daily and intraday, device dependent | Basis of the vaccination-response and infection-detection work. |
| Skin temperature | Oura | Nightly | Named in the healthcare-worker stress and recovery study. |
| ECG and irregular rhythm notifications | Apple Watch, Heartline study only | Event level | Combined with Medicare claims. |
| Surveys and patient-reported outcomes | Evidation app cards | Daily, weekly or event-triggered | The core active stream. |

## Derived Metrics / Analytics

- Vendor pages describe digital measures developed in-house, disease event and prevention modelling, patient segmentation and near real-time correlation of wearable data to events (Reported, no method documentation fetched).
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
- No public dashboard, role model, audit log or adherence-monitoring documentation was found.

## Data Access and Export

- Sponsors receive de-identified, patient-level longitudinal datasets. Format, delivery mechanism and latency are not documented publicly (Unclear).
- Members can see and control what they share, with whom and for how long, and consent to each data request (Reported, vendor pages).
- The American Life in Realtime dataset, collected on the platform with provisioned Fitbit Inspire 2 devices, is described as publicly available benchmark data (Reported from the paper abstract; access terms not checked).
- No public API, bulk export tool or self-service data download for researchers was found.

## APIs, SDKs, and Extensibility

- No public API, SDK or developer portal found (Verified by absence on the fetched pages; no developer domain located).
- Integration is inbound only, through the 20 or more consumer health apps and devices members can connect.

## Deployment and Infrastructure

- Vendor-hosted SaaS in the United States. Sponsors deploy nothing.
- Studies run on Evidation's existing member base or on cohorts recruited into it. External consortia have used the platform as their data collection and storage layer (BUMP, Heartline).
- Hardware provisioning has been done for specific studies, for example the Fitbit Inspire 2 in American Life in Realtime (Verified, Angrisani et al. 2025).

## Participant Experience

- Members install one consumer app, connect an existing wearable account and answer cards. Rewards are points redeemable for cash or charity (Reported).
- The vendor states that members give consent every time their data is requested (Reported).
- Retention across six participant-centric studies stayed above 80 percent in the first month and above 50 percent for each study's full active period, with a median of 77.2 percent retained (Verified, Goodday et al. 2024).
- Adherence was population dependent. Median adherence for Oura, Garmin and Apple Watch tasks exceeded 80 to 90 percent except in severely ill cancer and postpartum populations, where physical, mental and situational barriers dominated (Verified, Goodday et al. 2024).
- Underrepresented populations retained at lower rates than White participants across recruitment channels in BUMP (Verified, Harry et al. 2025).

## Privacy, Security, and Compliance

- The corporate privacy notice fetched on 2026-09-03 describes identifiers, device information, geolocation and usage data, sharing with service providers and affiliates, disclosure of de-identified information, and a CCPA opt-out for sales or sharing. It states the company does not knowingly sell or share personal information of minors under 16 (Verified from the notice).
- A separate privacy notice governs the consumer app. It was not fetched, so app-specific handling of health data is Unclear.
- No SOC 2, ISO 27001, HIPAA or GDPR statement appears on the pages fetched. Compliance status is Unclear, not absent.
- Consent is described as per-request and revocable (Reported).

## Pricing

- Non-public. Sponsor pricing requires contact through the vendor's form.
- Member-side costs are zero; members are paid in points.
- No academic pricing, per-participant fee or minimum commitment was found.

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
- United States centred membership; international availability is Unclear.
- The vendor's own publication and study counts differ between pages (140 or more studies and 100 or more publications on the home page; 175 or more studies and 70 or more publications on the about page). Recorded as conflicting, not reconciled.

## Best-Fit Use Cases

- Large observational cohorts needing thousands of wearable-connected participants quickly.
- Real-world evidence for life-sciences sponsors, especially where claims or EHR linkage is needed.
- Studies of engagement and retention at population scale.
- Nationally representative person-generated health data with provisioned devices, as in American Life in Realtime.

## Poor-Fit Use Cases

- Any study requiring raw phone sensor streams, custom sampling schedules or researcher-hosted data.
- Small academic studies without sponsor budgets.
- Studies outside the United States.
- Work needing an auditable, self-service study console.

## Open Questions

- What does a sponsor actually receive, in what format and at what latency?
- Which security certifications, if any, does the platform hold?
- Does the app read any phone sensors itself, or only connected accounts?
- Is there any academic or non-commercial access route?
- What are the access terms for the American Life in Realtime benchmark dataset?

These are logged as Q125 in `shared/unresolved-questions.md`.

## Key Links

- Official site: https://evidation.com/
- Research page: https://evidation.com/research
- How it works (members): https://evidation.com/how-it-works
- About: https://evidation.com/about
- Privacy notice: https://evidation.com/privacy
- Contact/sales: linked from every page as "Contact Us" (URL not fetched)
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
