# m-Path

## Quick Facts

| Field | Details |
|---|---|
| Organization | m-Path Software BV (Leuven), described on its about page as a 2024 spin-off of KU Leuven's Faculty of Psychology. The research page claims 1000+ researchers, 150+ institutions and 90000+ participants (vendor figures, read 2026-10-11) [22] |
| Category | ESM/EMA platform with an add-on passive-sensing module |
| Current status | Active |
| Platforms/devices | Mobile app (regular m-Path) plus "m-Path Sense" for passive sensing; web-based point-and-click study builder. Both apps are free on both stores from m-Path Software. App Store: "m-Path" (id6733243074, v1.3.4, 2026-10-05) and "m-Path Sense" (id6520394129, v1.2.0, 2026-09-08). Google Play: "m-Path" (io.m_Path.kuleuven, 50K+ downloads) and "m-Path Sense" (io.m_Path_Sense.kuleuven, 1K+ downloads) (Verified 2026-10-11) [12][28]. A white-label app is a paid add-on |
| Open source | No. Dashboard and apps are proprietary (personal, revocable access right; no object code). The companion R packages mpathr and mpathsenser are GPL (>= 3) on CRAN, and m-Path Sense builds on the open-source CARP framework [16][27] |
| Hosting/deployment | Managed SaaS, no self-hostable release. Survey data on Microsoft Azure in Germany (Frankfurt), per the manual, FAQ, sub-processor list and, since October 2026, the privacy statement. Continuous sensing, direct Garmin and media data go straight to the researcher's pCloud, OneDrive or SFTP server. Storing answer data on the customer's own servers is a custom-priced add-on with a development cost [20] |
| Pricing model | Published research plans: Free (€0, 50 participants/year), Essential, Standard and Comfort (€1,599 to €16,593 per year excl. VAT, 300 to 3,000 participant slots in steps of 100), plus priced add-ons from the Standard plan up; no separate academic or commercial rates; basic version free for individual practitioners (Verified 2026-10-11) [13] |
| Last verified | 2026-10-11 (vendor fact record) |

## Summary

- m-Path is a no-code, point-and-click ESM/EMA (Experience Sampling Method / Ecological Momentary Assessment) platform built for researchers and clinicians with limited programming skills, distinguishing itself from most other platforms in this module by leading with EMA/EMI (Ecological Momentary Intervention) design sophistication rather than passive sensing. Passive mobile sensing is offered as a **separate module, "m-Path sense,"** layered onto the core EMA product rather than being the platform's primary identity, an architecture worth noting explicitly, since it means a team choosing m-Path for its EMA strengths needs to confirm m-Path sense meets their passive-sensing needs as a distinct evaluation, not assume parity with dedicated sensing-first platforms.

- The platform is documented in a peer-reviewed methods paper (Frontiers in Digital Health, 2023) describing it as supporting "smartphone-based ESM/EMA studies with mobile sensing, wearable triggers, cognitive tasks, and integrated EMI/JITAI interventions", i.e., it explicitly supports **Just-In-Time Adaptive Intervention (JITAI)** designs, where sensed context can trigger an intervention rather than only a survey prompt. This is a distinctive, well-documented capability among the platforms in this module.

## Products / Platform Architecture

- **m-Path**, the core web-based ESM/EMA/EMI study-builder and app.
- **m-Path sense**, the passive mobile-sensing module (GPS, Bluetooth, pedometer, and other embedded smartphone sensors per the vendor's own description). **Updated 2026-08-25 (second pass, Verified via direct fetch of `m-path.io/pricing/`):** m-Path sense is not merely "an add-on module" in a loose sense, it is a **separately priced product line** with two tiers, "Sensing Lite" (€3,000) and "Sensing Full" (€10,000), confirming quantitatively that passive sensing sits entirely outside the base subscription tiers.
- Wearable-triggered assessment ("wearable triggers") is explicitly named, implying integration with external wearable signals to trigger EMA prompts, not independently verified in depth this session. A separate "Smartwatch Integration" add-on (€3,000) is also listed on the pricing page, suggesting wearable-trigger support itself may be gated behind this specific add-on rather than included by default, this is an inference from the pricing page's structure, not a directly confirmed statement, and is flagged as a new open question below.
- **Wearable routes (vendor fact record, Verified 2026-10-11) [24].** Three documented routes.
  - **Thryve** (Smartwatch integration add-on, €3,000) in the regular m-Path app: Garmin, Fitbit, Apple Health and Polar at lower resolution, with computed measures such as sleep scores, sleep stages and daily summaries. Oura costs €3,000 a year more.
  - **Direct Garmin** in m-Path Sense, which needs the Sensing full add-on: heart rate down to 1 s, all beat-to-beat intervals, raw accelerometer 25 Hz and gyroscope 32 Hz, plus SpO2, stress, respiration and skin temperature.
  - **Garmin Lite**, a separate add-on for Standard or Comfort plans with no published price.
  - Empatica, movisens and ActiGraph are not integrated.
- **m-Path Keyboard** collects keystroke and typing data and sends it directly to the researcher, bypassing m-Path's servers; it derives sentiment and typing behaviour without storing raw text [26].

## Sensors and Data Streams

- Every Module 2 profile uses the same table so platforms can be compared row by row. Rows are the passive streams named in `CLAUDE.md`. "Yes" and "No" are used only where a primary source says so; "Unclear" means nothing current was verified, and "No (OS)" means the operating system does not expose the stream to any third-party app. Confidence and sources are stated under the table. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Stream | Android | iOS | Raw or derived | Sampling configurable | Notes |
|---|---|---|---|---|---|
| GPS / location | Yes | Yes | Raw. Coordinates. | Unclear. Documented as every minute on Android and every 10 m moved on iOS (Sensing full); at questionnaire time only (Sensing lite) | Sensing full and Sensing lite. |
| Accelerometer | Yes | Yes | Derived. Window summary features (means, SDs, energy), not raw samples. | Yes. Period in seconds (periodic sensor) | Sensing full. Raw 25 Hz accelerometer is available only from a directly integrated Garmin watch. |
| Gyroscope | Unclear | Unclear | Unclear | Unclear | Listed on the vendor's full-vs-lite comparison page but not in the Sensing full sensor table. |
| Magnetometer | Unclear | Unclear | Unclear | Unclear | Not in the documented sensor lists (checked 2026-10-11). |
| Barometer | Unclear | Unclear | Unclear | Unclear | Not in the documented sensor lists (checked 2026-10-11). |
| Ambient light | Yes | No | Derived. Lux summaries. | Unclear | Sensing full; listed as Android only. |
| Proximity | Unclear | Unclear | Unclear | Unclear | Not in the documented sensor lists (checked 2026-10-11). |
| Device motion / activity recognition | Yes | Yes | Derived. Activity type with confidence; pedometer step count. | Unclear | Sensing full (activity, pedometer); Sensing lite reads step count since last boot at questionnaire time. |
| Screen state | Yes | No | Event | Unclear | Sensing full; listed as Android only. |
| App usage | Yes | No | Unclear | Unclear | Android only by default. iOS needs a new, study-specific app with Apple SensorKit. Sensing lite reads the last day's usage at questionnaire time. |
| Battery / charging | Yes | Yes | Unclear | Unclear | Sensing full. |
| Network / connectivity | Yes | Yes | Unclear | Unclear | Sensing full. |
| Wi-Fi | Yes | Yes | Unclear | Unclear | Sensing full. |
| Bluetooth | Yes | Yes | Event. Nearby devices at questionnaire time. | Not applicable | Sensing lite. Continuous Bluetooth is listed on the comparison page but not in the Sensing full sensor table. |
| Calls (metadata) | Unclear | Unclear | Metadata, cryptographically anonymised | Unclear | Listed on the comparison page only; platforms not stated. Niemeijer 2023 reports calls were left out of the Play Store build; current docs give no such caveat. |
| SMS (metadata) | Unclear | Unclear | Metadata, cryptographically anonymised | Unclear | As for calls. |
| Keyboard | Unclear | Unclear | Derived. Sentiment and typing behaviour (speed, errors, emoji use); no raw text stored. | Unclear | m-Path Keyboard; data go directly to the researcher. Platform support not stated. |
| Audio / microphone | Yes | Yes | Derived noise level at questionnaire time; audio recording as a question answer. | Not applicable | Sensing lite. Photo and video answers also supported. |
| Notifications | Unclear | Unclear | Unclear | Unclear | Not in the documented sensor lists (checked 2026-10-11). |
| Device information | Yes | Yes | Unclear | Unclear | Sensing full ("device"); memory is also listed, Android only. |

**Verification.** Rewritten 2026-10-11 from the vendor fact record, Verified against the m-Path manual's Mobile Sensing (full), Sensing lite and full-vs-lite comparison pages [8][23]. Sensing full (the m-Path Sense app, CARP-based) also lists weather and writes JSON files straight to the researcher's cloud. Periodic sensors use a researcher-set interval in seconds and others are event-based; because the OS pauses the app, real rates are lower than configured. Android and iOS columns follow the Sensing full sensor table, which marks screen, app usage, light and memory as Android only; per-stream parity for the other rows is not stated outright, and streams named only on the comparison page (gyroscope, continuous Bluetooth, calls and texts) are left Unclear. Niemeijer 2023 (Module 3) reports a 52 iOS and 52 Android performance study on the CARP-based m-Path Sense app.

### Notes from earlier verification passes

- Per the vendor's own materials, m-Path sense captures location, Bluetooth-based proximity/social-context signals, pedometer/activity data, and (per the general framing) noise/environmental context, used to "unobtrusively acquire objective information about participants' current surroundings... and behavior." Exact sampling configurability and iOS-vs-Android parity were **still not independently verified against current developer documentation** this session, a direct fetch of the manual's "Welcome to m-Path" landing page did not surface sensor-level or platform-parity detail; the specific sensor sub-pages of the manual were not reached this pass.

## Derived Metrics / Analytics

- Phone accelerometer arrives as window summary features (means, SDs, energy and so on), not raw samples; light as lux summaries; activity type with a confidence value (Verified 2026-10-11) [8].
- Thryve wearables add computed measures such as sleep scores, sleep stages and daily activity summaries [24].
- The m-Path Keyboard derives momentary sentiment and typing behaviour without storing raw text [26].
- Dashboard visualisations and compliance monitoring. The open R packages mpathr and mpathsenser process exported data [27].

## Active Data Collection

- This is m-Path's core strength: point-and-click design of "complex and highly adjustable EMA and EMI designs with advanced functionalities" without requiring programming skill, per the peer-reviewed methods paper describing the platform. Explicit support for JITAI (context-triggered intervention delivery, not just context-triggered surveys) is a distinctive, published capability.

## Researcher and Study Management Features

- Not independently verified in depth this session beyond the web-based, no-code study-builder interface described in the platform's own and peer-reviewed materials.
- **Access (vendor fact record, Verified 2026-10-11).** Self-service. Anyone can open a free dashboard account with email verification and buy Essential, Standard or Comfort by card; add-ons and other purchases go through a payment link, invoice or formal quote. There is no vendor review or approval step, and the Terms make ethics approval the researcher's responsibility [13][16][32].
- Legacy invitation codes will be phased out (no date given) [25].

## Data Access and Export

- **Export routes (vendor fact record, Verified 2026-10-11) [25].**
  - Dashboard: single-participant export in the Visualize tab on all plans; bulk semicolon-delimited .csv in the Export tab on paid plans only.
  - Wearable data exported from the dashboard as JSON (dynamic and daily data).
  - Sensing full, direct Garmin, Garmin Lite, keyboard and media data go straight to the researcher's pCloud, OneDrive or self-hosted SFTP server.
  - API as a paid add-on (see below). The R packages mpathr and mpathsenser read the exported files [27].
- **History (Corroborated).** No backfill of pre-enrolment history is documented. Survey data stays in the dashboard for the life of the account, including after a paid plan lapses, until deletion is requested. Thryve wearable access runs for a researcher-set expiration time after the participant connects; whether it backfills data recorded before connection is not stated. Garmin Lite syncs a configurable number of hours back, or from the last sync [15][24].
- **Sync timing.** Fitbit via Thryve syncs about every 15 minutes; Garmin and Apple Health via Thryve sync less often [24].

## APIs, SDKs, and Extensibility

- **Updated 2026-08-25 (second pass, Verified via direct fetch of `m-path.io/pricing/`).** A developer API is confirmed to exist, **"API Access" is a named, separately priced add-on (€5,000)** on m-Path's own pricing page. This resolves the prior "not independently verified" status to Verified-present, but with an important qualifier CLAUDE.md's evidence standard calls for: the API is not a free/included capability the way it is on some competitors, it is a specific, priced commercial add-on, and no API *documentation* (endpoints, auth model, data schema) was located or fetched this session. Whether it is a full researcher-facing REST API or a narrower integration hook was not established.
- **Vendor fact record, 2026-10-11 (Corroborated).** No open developer program and no public API documentation was found on the site, the manual or the web; this is an absence, not a vendor statement. The API add-on is available from the Standard plan up by contacting m-Path. Rate limits are not public. The R packages mpathr and mpathsenser read exported files, not a live API [13][27].

## Deployment and Infrastructure

- Managed SaaS; no self-hostable release. Hosting on m-Path's servers is included in every plan (Verified 2026-10-11) [14][20].
- **Where data goes.** Survey responses and logs are on Microsoft Azure in Frankfurt per the storage page, FAQ and sub-processor list (but see the residency conflict under Privacy). Sensing full, direct Garmin and media uploads bypass m-Path's servers and go to the researcher's pCloud, OneDrive or self-hosted SFTP server, which the researcher pays for [20][25].
- **External servers add-on (custom price).** Storing answer data on the customer's own servers is possible, at an additional development cost because m-Path works with the customer's IT staff. It is a data-storage arrangement, not a software install [20].

## Participant Experience

- Not verified in any pass to date.

### Background keepalive (added 2026-10-09)

- **Yes, researcher-configured.** The m-Path Sense app contacts the m-Path servers every 5 minutes. When a set period of "radio silence" passes, for example after the app has been closed, the server sends the participant a notification asking them to reopen the app. Researchers set the thresholds in a "Remind after app is closed (in minutes)" field; the manual's example is 30, 120, 360. The reminder title and text can be customised. The manual does not state a default. This is functionally the same design as Beiwe's KeepAlive.
- The 2023 m-Path Sense performance paper (Niemeijer et al.) described this mechanism as "currently being implemented", so it postdates that study's data.
- On iOS 26 or later, an optional Live Activity can keep sensing running in the background longer. The participant switches it on, and it can lapse if iOS ends it.
- Status: **Verified** from the m-Path manual (updated 2026-10-05), 2026-10-09. Sources 8 to 10.

## Privacy, Security, and Compliance

- **Vendor fact record, checked 2026-10-11.**
  - **DPA:** published. A GDPR Article 28 data processing agreement is Annex 1 of the Terms, with the researcher or practitioner as controller and m-Path as processor, a public sub-processor list, audits at the controller's cost (€125 per staff hour) and SCC Module 4 (Annex 2) for controllers outside the EEA. Services are provided only in the EU/EEA unless the controller is in a third country (Corroborated) [16][17][19].
  - **HIPAA:** the homepage, FAQ and research page claim GDPR and HIPAA compliance. No HIPAA policy, BAA or attestation is published, and the legal documents do not mention HIPAA. Ask m-Path before any US covered-entity study (Corroborated; BAA not public) [4][21][22].
  - **ISO 27001 and SOC 2:** cited only for Microsoft Azure, the hosting provider. Neither is held by m-Path itself as far as published (not public, Corroborated) [20].
  - **Data residency (Verified, 2026-10-21).** Survey data is on Microsoft Azure in Germany (Frankfurt), per the storage page, the FAQ, the sub-processor list and the privacy statement. Until an update between 2026-10-12 and 2026-10-19 the privacy statement named KU Leuven as server host, which was recorded as a conflict on 2026-10-11. Thryve wearable data passes through the manufacturer's servers and Thryve before reaching m-Path [18][19][20][24].
  - **Retention:** DPA clause 8.1 says m-Path deletes controller data as soon as services end, unless the controller asks in writing at least 5 days before for return as .csv. In practice a lapsed paid account falls back to the Free plan and keeps its data until the researcher asks for removal; the DPA does not say when services count as ended short of account removal. Participants can delete all their online data in the app, immediately and permanently. Database backups are daily and kept up to one month (Verified) [15][17][20][29].
  - **AI training and content licence: unclear.** No clause mentions AI or model training. Terms clause 11.7 gives m-Path a worldwide, irrevocable, royalty-free licence to use content users provide "for any purpose", and "User" includes participants; clause 10.3 lets m-Path process personal data for its own purposes such as improving the services. The DPA limits processing of personal data to the controller's instructions. Whether 11.7 reaches participant responses is not stated [16][17].
  - **Clinical use:** Terms clause 11.4 excludes using the services to provide clinical or medical services, and the Terms say the services are not a diagnostic tool, while m-Path markets a therapy product (/clinical/). The Terms do not define "clinical or medical services" [16][33].
  - **Participants aged 13 to 16** need a parent's or guardian's consent, subject to national law [16].
  - **FDA:** no 510(k), PMA or establishment registration for m-Path or m-Path Software (Verified, regulator databases) [30].
  - **Legal documents:** the Legal page still announces an update for November 1, 2025, with no changelog. The Terms reserve the right to discontinue services without notice [31].
- **Updated 2026-08-25 (second pass, Corroborated via direct fetch of `m-path.io`'s homepage plus a targeted search).** m-Path's own homepage states directly: "Secure data processing and storage, compliant with GDPR and HIPAA." This is a vendor self-declared compliance claim, not an independently audited certification (Avicenna Research's dated ISO 27001:2022 statement is at the same vendor-stated evidence tier, corrected 2026-10-10), per CLAUDE.md's instruction not to manufacture certainty, this is recorded as **Corroborated** (a specific, findable claim on the vendor's own primary page) rather than **Verified** (which would require third-party audit evidence, not located this session). Additional corroboration: m-Path is confirmed as "an original spin-off from KU Leuven's research group Quantitative Psychology and Individual Differences" (search-summary source), consistent with the platform's already-noted Belgium/KU Leuven academic origin, and search results at the time pointed to a `m-path.io/Privacy_Policy_m-Path_Sense.html` page for the sensing module. As of 2026-10-11 the current privacy statement (m-path.io/privacy-policy/) covers both the app and the dashboard; the Sense-specific URL was not rechecked. The DPA, SOC 2 and ISO 27001 status is now as stated in the bullets above.

## Pricing

- **Resolved 2026-08-25 (second pass, resolving unresolved-question #93's pricing component, Verified via direct fetch of `m-path.io/pricing/`).** Full published tier structure. Prices corrected 2026-10-11 from the manual's price table (vendor fact record, Verified) [13]; on the pricing page the participant labels on each card run in reverse order, so the manual's table is the reliable reading.

| Tier | Annual cost excl. VAT (300 / 1,000 / 3,000 slots) | Participants/year | Notable inclusions |
|---|---|---|---|
| Free | €0 | 50 | Basic data export, questionnaire editor, response visualization, client personalization, manual/community support |
| Essential | €1,599 / €4,441 / €9,043 | 300 to 3,000, in steps of 100 | Advanced data export, automatic scheduler, participant management |
| Standard | €2,099 / €5,829 / €11,380 | 300 to 3,000, in steps of 100 | + priority email support, unlimited projects/accounts, collaboration, add-on selection |
| Comfort | €3,099 / €8,607 / €16,593 | 300 to 3,000, in steps of 100 | + online-meeting support, advanced troubleshooting, yearly workshop, yearly study review |

- **Add-ons** (added by contacting the vendor; re-read 2026-10-10): Cognitive Tests (€4,500), Sensing Lite (€3,000, sensor data collected only when a participant completes a questionnaire), Sensing Full (€10,000, continuous sensing on Android and iOS via the m-Path Sense app), Intervention Editor (€6,000), Moodboard Editor (€6,000), Smartwatch Integration (€3,000, via Thryve; Garmin, Fitbit, Apple Health and Polar; Oura €3,000 a year more), White-Label App (€10,000 plus a €2,000 annual update fee), API (€5,000), First ESM study support package (€800), and custom-priced Development, Consulting and External servers. Sensing Full includes Sensing Lite and is required for the direct Garmin integration; Garmin Lite is a separate add-on with no published price.
- **Add-on terms (vendor fact record, Verified 2026-10-11) [13][24].** Add-ons can be selected from the Standard plan up, by contacting m-Path. They attach to the one-year subscription; prices hold up to 1,000 participant slots a year and scale above that. Only Oura and the white-label update fee are stated explicitly as per year.
- **Subscription terms (pricing FAQ, Verified 2026-10-10; manual, Verified 2026-10-11) [14][15]:** a subscription is one year of access; extra participant slots can be bought at any time. Paid subscriptions run at least one year and start at 300 slots (the smallest licence); extensions from 3 months. No automatic renewal; a lapsed account falls back to the Free plan. Extra blocks of 100 slots mid-term cost €535 (Essential) or €700 (Standard). Half of unused slots bought beyond the first 300 can be recovered, as can half of the slots used by participants who filled in one questionnaire or fewer. A formal quote is available on request, and m-Path is registered on SAM.gov for US institutions.
- **Hosting cost:** m-Path's managed hosting is included in every plan. External servers is custom-priced with a development cost. Cloud storage for sensing, Garmin and media data (pCloud, OneDrive or SFTP) is the researcher's own cost [14][20].
- **Enterprise (workplace) use** is by contact, with no public price [33]. The page offers only "research plans" (heading "Research & Academic Licenses") with no academic versus commercial split, and the basic version is free for individual practitioners, funded by research licences.

- This is now among the most transparent, itemized pricing structures in this module, more granular than Beiwe's BSC figures and far more so than Avicenna Research's or RADAR-base's still-nonpublic rates. It also materially reframes m-Path's earlier "no-code EMA platform with a passive-sensing add-on" description: sensing, API access, and smartwatch integration are all priced *well above* even the top Comfort subscription tier's base cost, meaning a full-featured deployment (EMA + sensing + API + wearable triggers) could plausibly cost more in add-ons than in the base subscription. That combination was not priced as a bundle by any source found this session.

## Research Evidence and Validation

- The core platform methodology is documented in a peer-reviewed, open-access methods paper: Mestdagh M, Verdonck S, Piot M, Niemeijer K, Kilani G, Tuerlinckx F, Kuppens P, Dejonckheere E, "m-Path: an easy-to-use and highly tailorable platform for ecological momentary assessment and intervention in behavioral research and clinical practice," *Frontiers in Digital Health* 2023;5:1182175 (CC BY, Verified open access, confirmed via the retrieved full-text PDF, see `../literature/m-path/2023-mestdagh-frontiersdigitalhealth-m-path-platform.pdf`), also indexed on PubMed. This is a stronger methods-paper foundation than several other commercial platforms in this module, which typically rely only on vendor marketing materials rather than a dedicated peer-reviewed platform-description paper.

## Strengths

- Dedicated peer-reviewed methods paper describing the platform's design and capabilities, a stronger evidentiary foundation than most commercial competitors in this module.
- No-code, point-and-click EMA/EMI study design, explicitly aimed at researchers/clinicians without programming background.
- Explicit, published support for JITAI (context-triggered intervention, not just context-triggered survey) designs.
- Wearable-triggered assessment is a named integration point, potentially useful for studies pairing this platform with a Module 1 wearable ecosystem.
- Reported use by 150+ institutions and 1000+ researchers (vendor claim on the research page, 2026-10-11, Reported, not independently verified) [22].

## Limitations

- Passive sensing (m-Path Sense) is a **separately priced** add-on (Sensing Lite €3,000, questionnaire-time snapshots only; Sensing Full €10,000, continuous), on top of the base subscription and available only from the Standard plan up (add-ons attach to the one-year subscription), not the platform's core identity or an included capability; its depth relative to dedicated sensing-first platforms (Beiwe, RADAR-base, AWARE) was not independently benchmarked this session.
- Closed-source and vendor-hosted; the only server-side alternative is the custom-priced "External servers" add-on, which stores answer data on the customer's servers at a development cost.
- ~~Pricing... were not independently established this session~~, **resolved 2026-08-25**: full tier and add-on pricing is now public (see Pricing above). Export routes are now documented (see Data Access and Export, 2026-10-11); API-endpoint-level documentation remains unpublished. Compliance is Corroborated (vendor's own GDPR/HIPAA claim) but not independently audited, no BAA is published, and the data host is in conflict across m-Path's own documents.
- API access, smartwatch/wearable-trigger integration, and full sensing are all **additional paid add-ons on top of even the top subscription tier**, a materially higher realistic cost than the base subscription price alone suggests for any study wanting the platform's full-featured combination.
- The user-base figure (now "Institutions 150+" on the research page; the earlier "250+ Universities" no longer appears) is a vendor claim not independently corroborated.
- Bulk export is paid-only; the Free plan has single-participant export only.

## Best-Fit Use Cases

- Studies whose primary design need is sophisticated, no-code EMA/EMI/JITAI logic, with passive sensing as a secondary/supporting data stream.
- Clinical or blended-care contexts where non-programmer clinicians need to design their own assessment/intervention protocols. Check first how this fits Terms clause 11.4, which excludes providing clinical or medical services [16].
- Studies pairing wearable-triggered prompts with EMA.

## Poor-Fit Use Cases

- Studies where passive sensing depth and breadth (not EMA sophistication) is the primary requirement, dedicated sensing platforms should be evaluated first.
- Teams needing full source-code control, or self-hosting of the software itself (the External servers add-on covers data storage on the customer's server only).
- US covered-entity studies that need a signed BAA, until m-Path confirms one is available.

## Open Questions

- *(Directed to: m-Path, via https://m-path.io)*

- What is m-Path sense's full current sensor catalog, and how does it compare in depth to dedicated passive-sensing platforms? **Largely answered 2026-10-11** (see the sensor table); still open: iOS and Android parity for streams named only on the comparison page (gyroscope, continuous Bluetooth, calls and texts).
- ~~What is the pricing model?~~ **Resolved 2026-08-25**, see Pricing above.
- ~~What compliance documentation (GDPR, HIPAA) exists?~~ **Largely resolved 2026-08-25**, vendor states GDPR + HIPAA compliance directly (Corroborated, not independently audited). **Updated 2026-10-11:** a DPA is published as Annex 1 of the Terms; ISO 27001 and SOC 2 are cited only for Azure; no BAA is published.
- ~~Is there a documented developer API?~~ **Resolved (existence) 2026-08-25**, "API" is a named €5,000 add-on (billing period not stated, corrected 2026-10-10). **New sub-question**: what does the API actually expose (endpoints, auth, data schema), and is documentation available before purchase?
- ~~What wearable devices are supported, and how do they relate to the Smartwatch Integration add-on?~~ **Answered 2026-10-11:** Thryve route (Garmin, Fitbit, Apple Health, Polar; Oura extra), direct Garmin via Sensing full, and Garmin Lite (see Products). Still open: whether "wearable triggers" for prompts work on every route, and the Garmin Lite price.
- Does the Free tier's "50 participants/year" cap reset annually? (A subscription is one year of access and extra participant slots can be bought at any time, per the pricing FAQ.) Academic pricing: answered 2026-10-10, the page lists only "research plans" with no academic/commercial split; the basic version is free for individual practitioners, funded by research licences.
- ~~What exactly does the "External servers" add-on provide?~~ **Answered 2026-10-11:** storage of answer data on the customer's own servers, built with the customer's IT at a development cost. Price still custom.
- ~~Which host is current for survey data, Azure Frankfurt or KU Leuven?~~ Answered 2026-10-21: the privacy statement now names Microsoft Azure in Germany.
- Does Terms clause 11.7's content licence apply to participant responses held under the DPA, and does it permit model training?
- How does the therapy product fit with Terms clause 11.4?
- Is data on a Free-plan account, after a paid study lapses, ever deleted without a request?
- Is a HIPAA BAA available for US covered entities?

## Vendor Fact Record

<!-- facts:begin -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | No separate research or academic program. Research use runs on the research licences themselves (Free, Essential, Standard, Comfort), sold on a page titled "Research & Academic Licenses", with paid add-ons, consulting and a first-ESM-study support package. The research page claims 1000+ researchers, 150+ institutions and 90000+ participants (vendor figures). [V, 2026-10-11] |
| Who can join the research program | Anyone can open a free dashboard account; paid subscriptions are optional and no eligibility criteria are published for them. Individual practitioners (therapy use) get the basic version free. Participants aged 13 to 16 need a parent's or guardian's consent, subject to national law. [V, 2026-10-11] |
| How to apply, and any approval or review step | Self-service. Sign up with email verification, then buy Essential, Standard or Comfort by card on the pricing page; add-ons and other purchases go through a payment link, invoice or formal quote from m-Path. No review or approval step. Ethics approval is the researcher's responsibility. [V, 2026-10-11] |
| Whether the program is active, paused, renamed or closed | Active. Plans and add-ons are on sale on the live pricing page, and the manual's billing and sensing pages were updated in October 2026. [V, 2026-10-30] |
| Whether the general developer or API program is open to new applicants | No open developer program and no public API documentation. API access is a paid add-on (EUR 5,000), available from the Standard plan up by contacting m-Path. The open R packages (mpathr, mpathsenser) read exported files, not a live API. [C, 2026-10-11] |
| Participant or user limits before approval or by tier | Free plan 50 participants a year. Paid plans 300 to 3,000 participant slots a year in steps of 100; 300 is the smallest paid licence. Extra blocks of 100 can be bought mid-year. Add-on prices hold up to 1,000 slots and scale above that. [V, 2026-10-11] |
| How academic access differs from commercial or consumer access | No separate academic tier; the research licences are the same for any researcher. Individual practitioners get the basic version free, funded by research licences, and the site markets m-Path for therapy and blended care. Enterprise (workplace) use is by contact, with no public price. The Terms, however, exclude using the services to provide clinical or medical services. [C, 2026-10-11] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | n/a |
| Consumer subscription or membership price | **Research plans:** Per year, excl. VAT. At 300 slots: Essential EUR 1,599, Standard EUR 2,099, Comfort EUR 3,099. At 1,000: EUR 4,441 / 5,829 / 8,607. At 3,000: EUR 9,043 / 11,380 / 16,593. Free plan EUR 0. Extra 100 slots mid-term EUR 535 (Essential) or EUR 700 (Standard). [V, 2026-10-11]<br>**Individual practitioners:** Free for individual practitioners (therapy use). [V, 2026-10-11] |
| Research or academic pricing or discount | No academic discount; the published research plans (page titled "Research & Academic Licenses") are the academic prices. Half of unused slots bought beyond the first 300 can be recovered, as can half of the slots used by participants who filled in one questionnaire or fewer. US institutions can buy through SAM.gov. [V, 2026-10-11] |
| Fees for API, SDK, platform or data access | Add-ons, excl. VAT, added to the one-year subscription from the Standard plan up; prices hold up to 1,000 participant slots a year and scale above that. API EUR 5,000; Sensing lite EUR 3,000; Sensing full EUR 10,000 (includes Sensing lite; required for the direct Garmin integration); Smartwatch integration via Thryve EUR 3,000, with Oura EUR 3,000 more; Cognitive tests EUR 4,500; Intervention editor EUR 6,000; Moodboard editor EUR 6,000; White-label app EUR 10,000 plus EUR 2,000 a year; External servers custom. Garmin Lite is a separate add-on with no published price. [V, 2026-10-11] |
| Minimum order, term or commitment | Paid subscriptions run at least one year and start at 300 participant slots; extensions from 3 months. No automatic renewal; a lapsed account falls back to the Free plan. [V, 2026-10-11] |
| Whether pricing requires contacting sales | No for the base plans, which are priced and bought online. Add-ons are priced but enabled by contacting m-Path; external servers, consulting and custom development are custom-priced. A formal quote is available on request. [V, 2026-10-11] |
| Price of managed hosting | Managed hosting on m-Path's Azure servers is included in every plan. Storing answer data on the customer's own servers ("External servers") is custom-priced with a development cost. Sensing-full, Garmin-direct and media data go to the researcher's own pCloud, OneDrive or SFTP storage, which the researcher pays for. [V, 2026-10-11] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | Phone, continuous (Sensing full, m-Path Sense app, CARP-based): location, device, weather, pedometer, activity, screen (Android), battery, app usage (Android), connectivity, Wi-Fi, periodic accelerometer features, light (Android), memory (Android); a vendor comparison page also lists gyroscope, Bluetooth and anonymised call and text data. JSON files go straight to the researcher's cloud. Phone, in-survey (Sensing lite): location, noise level, step count, app usage (Android; iOS only with a study-specific SensorKit app), nearby Bluetooth, audio, photo, video. m-Path Keyboard: keystroke and typing data sent to the researcher. Wearables: direct Garmin gives heart rate down to 1 s, all beat-to-beat intervals, raw accelerometer 25 Hz and gyroscope 32 Hz, plus SpO2, stress, respiration and skin temperature; Garmin, Fitbit, Apple Health and Polar via Thryve at lower resolution. Empatica, movisens and ActiGraph are not integrated. [V, 2026-10-11] |
| Derived or processed metrics available to researchers | Phone accelerometer comes as window summary features (means, SDs, energy and so on), not raw samples, and light as lux summaries; activity type with confidence. Thryve wearables include computed measures such as sleep scores, sleep stages and daily summaries. The m-Path keyboard derives sentiment and typing behaviour without storing raw text. Dashboard visualisations and compliance monitoring; R packages mpathr and mpathsenser for processing. [V, 2026-10-11] |
| Documented sampling rates or temporal resolution | m-Path Sense: periodic sensors use a researcher-set interval in seconds, others are event-based; location every minute on Android and every 10 m moved on iOS. The OS pausing the app makes real rates lower than configured. Direct Garmin: heart rate default 30 s (1 to 3600 s), stress and respiration default 10 s, SpO2 default 30 s, steps fixed at 60 s, all beat-to-beat intervals, accelerometer 25 Hz, gyroscope 32 Hz. Thryve wearables are lower resolution; Fitbit syncs about every 15 minutes, Garmin and Apple Health less often. [V, 2026-10-11] |
| How far back data can be retrieved | No backfill of pre-enrolment history is documented. Survey data stays in the dashboard for the life of the account, including after a plan lapses, until deletion is requested. Thryve wearable access runs for a researcher-set expiration time after the participant connects. Garmin Lite syncs a configurable number of hours back, or from the last sync. [C, 2026-10-11] |
| Export, API, SDK or file routes | Dashboard: single-participant export in the Visualize tab (all plans) and bulk semicolon-delimited .csv in the Export tab (paid plans only); wearable data exported from the dashboard as JSON. Sensing-full, Garmin-direct, Garmin Lite, keyboard and media data go straight to the researcher's pCloud, OneDrive or self-hosted SFTP. API as a paid add-on. R packages mpathr and mpathsenser read the exports. [V, 2026-10-11] |
| API rate limits | Not public [2026-10-11] |
| Terms on retaining, storing or deleting data | DPA clause 8.1: m-Path deletes controller data as soon as services end, unless the controller asks in writing at least 5 days before for return as .csv. In practice a lapsed paid account falls back to the Free plan and keeps its data until the researcher asks for removal. Participants can delete all their online data in the app, immediately and permanently. Database backups are daily and kept up to one month. [V, 2026-10-11] |
| Terms on using data to train AI or ML models | Unclear |
| Announced shutdowns, deprecations or migrations, with dates | No dated shutdowns. Legacy invitation codes will be phased out (no date). The Legal page still announces a legal-document update for November 1, 2025, with no changelog. The Terms reserve the right to discontinue services without notice. [C, 2026-10-11] |
| Software licence of the platform's components | Platform (dashboard, m-Path and m-Path Sense apps) is proprietary; users get a personal, revocable access right and no object code. The companion R packages mpathr and mpathsenser are GPL (>= 3) on CRAN. m-Path Sense builds on the open-source CARP mobile sensing framework. [V, 2026-10-11] |
| Self-hosting and managed-hosting options | Managed SaaS only by default, with survey data on Microsoft Azure in Frankfurt (but see data_residency). Continuous sensing, Garmin-direct and media data bypass m-Path's servers and go to the researcher's pCloud, OneDrive or self-hosted SFTP. Storing answer data on the customer's own servers is a custom-priced add-on built with the customer's IT. No self-hostable release. [V, 2026-10-11] |
| App store availability on iOS and Android | Two free apps from m-Path Software on both stores: m-Path (surveys, Sensing lite, Thryve wearables; Play id io.m_Path.kuleuven, 50K+ downloads; App Store id6733243074) and m-Path Sense (continuous sensing and direct Garmin, built on CARP; Play id io.m_Path_Sense.kuleuven, 1K+ downloads; App Store id6520394129). A white-label app is a paid add-on. [V, 2026-10-11] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-11] |
| Whether a data processing agreement is offered | Yes. A GDPR Article 28 data processing agreement is Annex 1 of the Terms (researcher or practitioner as controller, m-Path as processor), with a public sub-processor list, audits at the controller's cost (EUR 125 per staff hour) and SCC Module 4 (Annex 2) for controllers outside the EEA. [C, 2026-10-11] |
| Published HIPAA statement | The homepage, FAQ and research page claim GDPR and HIPAA compliance. No HIPAA policy, BAA or attestation is published, and the legal documents do not mention HIPAA. [C, 2026-10-11] |
| Published GDPR statement | Belgian company acting as GDPR processor under an Article 28 DPA; services provided only in the EU/EEA unless the controller is in a third country; privacy statements set out data subject rights; participants can delete their online data in the app. [C, 2026-10-11] |
| ISO/IEC 27001 status and evidence | Not public [2026-10-11] |
| SOC 2 status and evidence | Not public [2026-10-11] |
| FDA clearances, from the FDA database | Not public [2026-10-11] |
| Where data is stored, and residency options | EU. Survey data is on Microsoft Azure in Germany (Frankfurt), per the manual's storage page, the FAQ, the sub-processor list and, since an update between 2026-10-12 and 2026-10-19, the privacy statement, which earlier named KU Leuven as server host. The DPA keeps services in the EU/EEA unless the controller is outside it. Continuous sensing, Garmin-direct and media data go straight to the researcher's pCloud, OneDrive or SFTP server, wherever that is. Thryve wearable data passes through the manufacturer's servers and Thryve before reaching m-Path. [V, 2026-10-21] |

<!-- facts:end -->

## Key Links

- Official site: https://m-path.io/
- Manual/knowledge base: https://m-path.io/manual/knowledge-base/welcome-to-m-path/
- Research page: https://m-path.io/landing/research/
- Pricing: https://m-path.io/pricing/
- m-Path (App Store): https://apps.apple.com/us/app/m-path/id6733243074 ; m-Path Sense (App Store): https://apps.apple.com/us/app/m-path-sense/id6520394129
- m-Path (Google Play): https://play.google.com/store/apps/details?id=io.m_Path.kuleuven ; m-Path Sense (Google Play): https://play.google.com/store/apps/details?id=io.m_Path_Sense.kuleuven
- Terms and conditions: https://m-path.io/terms-and-conditions/ ; Data processing agreement: https://m-path.io/data-processing/ ; Sub-processors: https://m-path.io/subcontractors/
- Security/storage: https://m-path.io/manual/knowledge-base/storage/

## Sources

1. m-Path, official site. https://m-path.io/ (accessed 2026-08-24, search summary). **Primary.** Platform framing, m-Path sense module, JITAI/EMI support.
2. Mestdagh M, Verdonck S, Piot M, Niemeijer K, Kilani G, Tuerlinckx F, Kuppens P, Dejonckheere E. "m-Path: an easy-to-use and highly tailorable platform for ecological momentary assessment and intervention in behavioral research and clinical practice." *Frontiers in Digital Health* 2023;5:1182175. https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2023.1182175/full ; PMC mirror: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10619650/ ; full-text PDF retrieved and verified, CC BY (accessed 2026-08-24, Direct, see `../literature/m-path/2023-mestdagh-frontiersdigitalhealth-m-path-platform.pdf`). Peer-reviewed platform-description paper.
3. m-Path, Research page. https://m-path.io/landing/research/ (accessed 2026-08-24, search summary). "250+ Universities" user-base claim, Reported, not independently verified. No longer on the page as of 2026-10-11; see 22.
4. m-Path, homepage (second-pass direct fetch). https://m-path.io/ (accessed 2026-08-25). **Primary/Direct.** "Secure data processing and storage, compliant with GDPR and HIPAA" (vendor self-declared, Corroborated not Verified).
5. m-Path, Pricing. http://m-path.io/pricing/ (accessed 2026-08-25, second pass). **Primary/Verified.** Full tier structure (Free/Essential/Standard/Comfort) and add-on pricing (Sensing Lite/Full, API Access, Smartwatch Integration, Cognitive Tests, Intervention Editor, Moodboard Editor, White-Label App). Resolves unresolved-question #93's pricing component.
6. m-Path, "Welcome to m-Path" manual landing page (second-pass direct fetch). https://m-path.io/manual/knowledge-base/welcome-to-m-path/ (accessed 2026-08-25). **Primary/Direct, limited yield.** Confirmed no sensor-level or pricing/API detail present on this specific landing page, the manual's deeper sensor-specific sub-pages were not reached this pass.
7. Search-summary corroboration of m-Path's KU Leuven spin-off origin and GDPR-specific privacy commitments (accessed 2026-08-25, search summary, not a single direct-fetched primary page, synthesized from m-path.io and m-path.io/Privacy_Policy_m-Path_Sense.html search results).
8. m-Path manual, "Mobile Sensing (full)." https://m-path.io/manual/knowledge-base/mobile-sensing-full/ (accessed 2026-10-09). **Primary/Direct.** Five-minute server contact and reopen reminders.
9. m-Path manual, "Live Activity background sensing." https://m-path.io/manual/knowledge-base/live-activity-background-sensing/ (accessed 2026-10-09). **Primary/Direct.**
10. Niemeijer K. et al. 2023, *JMIR Formative Research*, doi 10.2196/43296 (full text via Europe PMC, PMC10031448; accessed 2026-10-09). **Verified.** m-Path Sense embeds CARP Mobile Sensing; keepalive then in development.
11. m-Path, Pricing, re-read. https://m-path.io/pricing/ (accessed 2026-10-10). **Primary/Verified.** Add-on descriptions (Sensing Lite vs Full, External servers, First ESM study support, white-label update fee), no add-on billing period, subscription FAQ, no academic/commercial split.
12. iTunes lookup/search for m-Path (id 6733243074) and m-Path Sense (id 6520394129), 2026-10-10. **Primary/Verified.**
13. m-Path manual, "Subscriptions and billing." https://m-path.io/manual/knowledge-base/subscriptions-and-billing/ (accessed 2026-10-11, vendor fact record). **Primary/Verified.** Price table at 300, 1,000 and 3,000 slots; add-on prices and terms; payment routes; quote on request; SAM.gov.
14. m-Path manual, "Buying participant slots." https://m-path.io/manual/knowledge-base/buying-participant-slots/ (accessed 2026-10-11, vendor fact record). **Primary/Verified.** 300-slot minimum licence, €535/€700 per extra 100 slots, slot recovery, hosting included.
15. m-Path manual, "Subscription length." https://m-path.io/manual/knowledge-base/subscription-length/ (accessed 2026-10-11, vendor fact record). **Primary/Verified.** One-year minimum, 3-month extensions, no auto-renewal, data kept after a lapse.
16. m-Path, Terms and conditions. https://m-path.io/terms-and-conditions/ (fetched via https://m-path.io/LegalPage/terms.html, accessed 2026-10-11, vendor fact record). **Primary/Verified.** Access right, clauses 10.3, 11.4 and 11.7, User definition, ethics responsibility, parental consent, SCC Module 4, not a diagnostic tool, right to discontinue.
17. m-Path, Data processing agreement. https://m-path.io/data-processing/ (fetched via https://m-path.io/LegalPage/dpa.html, accessed 2026-10-11, vendor fact record). **Primary/Verified.** Controller and processor roles, clause 8.1 deletion and .csv return, €125 per hour audits, EU/EEA provision.
18. m-Path, Privacy statement. https://m-path.io/privacy-policy/ (fetched via https://m-path.io/LegalPage/privacy.html, accessed 2026-10-11, vendor fact record). **Primary.** Named KU Leuven as server host on 2026-10-11; since an update between 2026-10-12 and 2026-10-19 it names Microsoft Azure servers in Germany (rechecked 2026-10-21).
19. m-Path, Sub-processors. https://m-path.io/subcontractors/ (fetched via https://m-path.io/LegalPage/subcontractors.html, accessed 2026-10-11, vendor fact record). **Primary.** Microsoft Azure, Frankfurt, as the main sub-processor.
20. m-Path manual, "Storage." https://m-path.io/manual/knowledge-base/storage/ (accessed 2026-10-11, vendor fact record). **Primary/Verified.** Azure Frankfurt, own-server option at development cost, daily backups kept up to a month, Azure ISO 27001 and SOC 2.
21. m-Path, FAQ. https://m-path.io/faq/ (accessed 2026-10-11, vendor fact record). **Primary.** GDPR and HIPAA claim; Azure Frankfurt.
22. m-Path, Research page, re-read. https://m-path.io/landing/research/ (accessed 2026-10-11, vendor fact record). **Primary.** "Institutions 150+", 1000+ researchers, 90000+ participants (vendor figures); HIPAA claim.
23. m-Path manual, "Full sensing vs sensing lite: which do you need?" https://m-path.io/manual/knowledge-base/full-sensing-vs-sensing-lite-which-do-you-need/ and "Mobile sensing lite version" https://m-path.io/manual/knowledge-base/mobile-sensing-lite-version/ (accessed 2026-10-11, vendor fact record). **Primary/Verified.** Lite stream list; gyroscope, Bluetooth and anonymised call and text data on the comparison page; iOS app usage via SensorKit only.
24. m-Path manual, wearables pages (accessed 2026-10-11, vendor fact record). **Primary/Verified.** https://m-path.io/manual/knowledge-base/wearables/ ; https://m-path.io/manual/knowledge-base/which-wearable-integration-is-right-for-my-project/ ; https://m-path.io/manual/knowledge-base/wearables-garmin-direct-integration/ ; https://m-path.io/manual/knowledge-base/wearables-garmin-lite/ . Thryve devices, Oura surcharge, direct Garmin resolutions, Garmin Lite, non-integrated devices, sync timing.
25. m-Path manual, "Export data" https://m-path.io/manual/knowledge-base/export-data/ and "Adding a cloud storage location" https://m-path.io/manual/knowledge-base/adding-a-cloud-storage-location-for-client-file-uploads/ (accessed 2026-10-11, vendor fact record). **Primary/Verified.** Single and bulk export, pCloud, OneDrive and SFTP, legacy invitation codes.
26. m-Path manual, "m-Path Keyboard" https://m-path.io/manual/knowledge-base/m-path-keyboard/ and Mobile sensing page https://m-path.io/mobile-sensing/ (accessed 2026-10-11, vendor fact record). **Primary.** Keyboard data sent directly to the researcher; sentiment and typing behaviour without raw text.
27. CRAN, mpathr https://cran.r-project.org/package=mpathr and mpathsenser https://cran.r-project.org/package=mpathsenser (accessed 2026-10-11, vendor fact record). **Primary/Verified.** GPL (>= 3).
28. Google Play, m-Path https://play.google.com/store/apps/details?id=io.m_Path.kuleuven and m-Path Sense https://play.google.com/store/apps/details?id=io.m_Path_Sense.kuleuven (accessed 2026-10-11, vendor fact record). **Primary/Verified.**
29. m-Path manual, "Delete online data." https://m-path.io/manual/knowledge-base/delete-online-data/ (accessed 2026-10-11, vendor fact record). **Primary/Verified.** Participants can delete all online data immediately.
30. FDA 510(k), PMA and establishment registration databases, searched for "m-Path" and "m-Path Software" via openFDA (accessed 2026-10-11, vendor fact record). https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm . **Verified absent.** The only "M-PATH" 510(k) (K946356) is an unrelated guidewire.
31. m-Path, Legal page. https://m-path.io/legal/ (accessed 2026-10-11, vendor fact record). **Primary.** Announced legal-document update for November 1, 2025, still posted.
32. m-Path manual, "Create an online dashboard account." https://m-path.io/manual/knowledge-base/create-an-online-dashboard-account/ (accessed 2026-10-11, vendor fact record). **Primary/Verified.** Free account for any researcher or practitioner; email verification.
33. m-Path, Clinical page https://m-path.io/clinical/ and Enterprise page https://m-path.io/enterprise/ (accessed 2026-10-11, vendor fact record). **Primary.** Therapy marketing; enterprise use by contact.
