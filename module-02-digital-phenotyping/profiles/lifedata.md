# LifeData (RealLife Exp / "LifeData+")

## Quick Facts

| Field | Details |
|---|---|
| Organization | LifeData, LLC — 1800 N Wabash Rd, Suite 300, Marion, Indiana 46952, USA |
| Category | Commercial EMA / ESM / eDiary / ePRO / eCOA platform. **Not a passive-sensing digital phenotyping platform** — see the scope note below |
| Current status | **Active.** Two live product generations in parallel: the original platform (participant app **RealLife Exp**, researcher console `server.lifedatacorp.com`) and a successor platform marketed as **LifeData+** (participant app **LifeData**, console `app.lifedatacorp.com`) |
| Platforms/devices | Native iOS and Android participant apps (four store listings total, two per generation); web researcher console |
| Open source | **No.** No GitHub organization, no public repositories, no SDK found (Verified — `api.github.com/orgs/lifedatacorp` returns 404; a GitHub code/repo search for the product names returns zero results) |
| Hosting/deployment | Vendor SaaS only. Servers **located in the United States**; onward hosting via **Microsoft / Microsoft Azure**, named in the vendor's own privacy policy. No self-hosting option identified |
| Pricing model | Commercial subscription, **entirely non-public** — priced on number of researchers × subscription duration × number of participants; five named tiers (Individual, Team, Enterprise, Clinical, Monitoring) with no rate figures; graduate-student discount stated to exist; every tier's call-to-action is "Schedule Consultation" |
| Last verified | 2026-09-02 (first research pass) |

## Naming — resolve before searching the literature

Three names are in circulation and they are easy to conflate. Recording rather than silently resolving, per CLAUDE.md:

- **LifeData, LLC** is the company (site `lifedatacorp.com`; papers sometimes cite it as "LifeDataCorp LLC" or "the Lifedatacorp platform").
- **RealLife Exp** is the vendor's actual, current name for the original participant-facing app (App Store bundle `com.lifedata.reallife-exp`, Play package `com.lifedata.reallife_exp`). Study protocols in this generation are called **"LifePaks"** in the vendor's own app-store copy.
- **"Realtime EXP"** is **not** a vendor product name. It appears in the literature as a mis-rendering of *RealLife Exp* — Europe PMC full-text search returns **exactly one** hit for `"Realtime EXP"` (Ball et al. 2025, which writes "Realtime EXP by LifeData") against **74** for `"RealLife Exp"`. Anyone searching this knowledge base or the literature for "Realtime EXP" should read it as RealLife Exp.

Practical consequence: a literature search for this platform needs at least `"RealLife Exp"`, `LifeData`, and `LifeDataCorp` as separate queries, and bare `LifeData` is a noisy term (162 Europe PMC hits for `"LifeData" AND "ecological momentary"`, many of them false positives on unrelated phrases).

## Scope note — is this a digital phenotyping platform?

**No, on the definition this module uses — and this is the single most decision-relevant fact in the profile.** Across the vendor's entire public site (home, `/features/`, `/solutions-research/`, the ESM/EMA/eDiary/ePRO/eCOA product pages, and the "Who We Serve" pages), the **only** device-sensor stream LifeData documents is **GPS geolocation**, and it is described consistently and specifically as being captured *with a response*:

- "**Geolocation** — Gather GPS coordinates with each user response." (`/solutions-research/`, `/experience-sampling-app-2/`, `/ecological-momentary-assessment-app-2/`, three separate pages, identical wording)
- "**Location Data (GPS)** — Capture location data with participant responses for deeper insights." (`/features/`, the platform's full feature list)
- "**GPS Data** — Collect participants' geolocation when they respond, if needed." (`/who-we-serve-psychological-science/`)
- "All responses are timestamped and geolocation reporting is standard." (`/solutions-research/`)

There is **no mention anywhere on the public site** of accelerometer, gyroscope, magnetometer, barometer, ambient light, proximity, screen state, device/app usage, battery, network/Wi-Fi, Bluetooth, call or SMS metadata, keyboard data, microphone/audio features, notifications, or continuous background location. Nor is there any mention of wearable integration, HealthKit, Health Connect, or FHIR/EHR integration. Google Play's Data safety declarations for both apps are consistent with this narrow footprint (RealLife Exp: "Location, Personal info and 3 others"; LifeData: "Location, Personal info and 4 others").

This is a **Corroborated negative finding**, not merely an unverified gap: it is the consistent picture across five independent vendor pages, the two app-store descriptions, and both Play Data-safety declarations. It is not fully Verified only because the researcher-facing documentation is login-gated (see below), so a non-public sensor option cannot be strictly excluded.

**Treat LifeData as belonging to the EMA/ePRO end of this module's spectrum** — closest in kind to MetricWire and to Avicenna Research's survey/eCOA side, and materially narrower than Beiwe, RADAR-base, AWARE, mindLAMP, or CARP on passive sensing. What it collects that a plain survey tool does not is **fine-grained response metadata** (millisecond-precision notification-delivery, response-timing and engagement timestamps) plus **response-linked GPS** — which is why suicide-risk-prediction work such as Nock et al. 2026 can speak of "passively collected survey meta-data" while using no phone sensors at all.

## Products / Platform Architecture

Two generations run in parallel, and the vendor's own site presents them as a live choice rather than a completed migration — a switcher in the site footer offers "LifeData / **Original** → Go to LifeData" and "LifeData+ / Released in 2026 → Go to LifeData+":

| | Original platform | LifeData+ |
|---|---|---|
| Participant app | **RealLife Exp** | **LifeData** |
| iOS listing | `id939951918`, first released **2015-01-03**, v2.8.14 (**2026-04-06**), min iOS 13.0 | `id6443996884`, first released **2025-05-28**, v1.0.16 (**2026-08-27**), min iOS 18.0 |
| Android listing | `com.lifedata.reallife_exp`, released **2015-01-11**, updated **2026-04-08** | `com.lifedata.lifedata`, released **2025-11-27**, updated **2026-07-18** |
| Researcher console | `https://server.lifedatacorp.com/server-frontend/index.html` | `https://app.lifedatacorp.com/` |
| Protocol terminology | "LifePaks" | "Studies" |

**Recorded conflict, not resolved:** the website says LifeData+ was "Released in 2026"; the App Store first-release date for the new app is **2025-05-28** and its own store description says "the new LifeData platform released in **2025**". Both are vendor-controlled sources. Most plausible reading is a 2025 soft/limited release and a 2026 general-availability marketing launch, but that is inference and is labelled as such.

**Consequence for study planning and for reading the literature:** every published study to date used the *original* RealLife Exp platform. LifeData+ (`min iOS 18.0`, 1 App Store rating) has **no published deployment record whatsoever** as of this pass. A team choosing LifeData now is choosing between a platform with a decade-long publication trail on an app the vendor labels "Original," and a successor with essentially no external evidence base. That is a genuine and unusual tradeoff, and neither the vendor's site nor any third-party source states an end-of-support date for the original platform. **Unresolved — requires vendor contact.**

## Active Data Collection

This is the platform's core competence and the area where its public documentation is most specific.

- **Notification (signal-contingent) sessions** — questions pushed by notification; participant taps to answer immediately.
- **Check-in / eDiary sessions** — participant-initiated responding on their own time, for event-contingent reporting, daily diaries, or always-available intervention material (i.e. EMI, not just EMA).
- **Scheduling**: fixed times, random times within specified windows with a configurable minimum inter-prompt interval (the vendor's own example: "three random times between 8am and 5pm, at least 90 minutes apart"), triggered, and event-based. Multiple question/schedule combinations per study.
- **Branching** (immediate within-survey follow-up on a response) and **Triggering** — the vendor distinguishes two trigger types: one that sends follow-up questions at a later point (e.g. 90 minutes later), and one that **activates a whole new schedule** (e.g. once per day for a week). This second form is a genuine EMI/JITAI-adjacent capability and is more specifically documented than MetricWire's comparable "contextualized trigger-based survey deployment" claim.
- **13 question types**, per `/features/`, including multiple choice, scales, free text, **media uploads**, and web; `/solutions-research/` additionally names sliding scale, Likert, **image capture**, and **in-app consent**.
- **Smart logic**: display logic, piped text, and computed **scores**; "Adaptive Study Automation" that adapts assessment/intervention based on responses, scores, engagement, and study events.
- **Study alerts**: real-time alerts to the research team triggered by participant responses, scores, or study events — relevant to risk-monitoring designs (and consistent with its heavy use in suicide-risk EMA research).
- **Offline collection**: the study protocol is downloaded to the phone and "all data collection can be handled offline," with automatic upload on reconnection. Verified (vendor-stated) on two separate pages.
- **Multiple languages**, "including right-to-left languages" (vendor-stated).

## Researcher and Study Management Features

- Web study builder + management console; study **templates** (eDiary page).
- **Remote onboarding** in "under a minute" via emailed secure link, **QR code**, access code, or App Store search (vendor-stated). A live demo protocol is offered at `https://lifedatacorp.page.link/jgPjLQNpbRKch1nTA`.
- **Research teams with roles**: "assign roles with varying levels of system and data access"; Enterprise tier adds "institutional master subscriptions" and "department sub-accounts"; Clinical tier adds **multi-site support**.
- **Monitoring**: real-time engagement/response-rate/activity tracking; customizable dashboards for individuals and groups; smart reminders.
- **Researcher-assigned IDs** — explicitly framed as a way to "link LifeData data with external datasets without storing personal information," which is the mechanism behind the platform's anonymous mode.
- **Audit trails**: offered as a *paid service* ("LifeData **can develop** customized reports to track the research team's system interactions"), not as a standard shipped feature. Worth noting for anyone who assumed audit logging is built in — the wording implies bespoke work.

## Data Access and Export

- **CSV** download is the primary path ("Export clean .csv files"), with "multiple data formats available for various types of analyses, including multilevel modeling" — i.e. both long and wide/nested layouts, though the vendor does not enumerate them.
- Data files carry **detailed timestamps and participant IDs**, described as "formatted for easy analysis in Python, R, SPSS, Stata, and more."
- **Millisecond-precision** timestamps for notification delivery, response timing and engagement (`/features/`) — the metadata layer that makes engagement/compliance modelling possible.
- **Media file export** alongside response data.
- Real-time dashboards as an alternative to export.
- "Participant study downloads (varies by subscription)" — the FAQ implies an export/participant-volume element that differs by tier, unexplained publicly. **Unclear.**
- **No API, no SDK, no webhook, no direct database access is mentioned anywhere on the public site**, and there is no developer portal. `api.lifedatacorp.com` resolves in DNS but returns HTTP 404 at `/`, `/docs`, `/swagger`, `/v1`, `/api-docs` and `/health` — consistent with an internal application backend, not a documented researcher-facing API. Programmatic/streaming access should be assumed **absent** until the vendor says otherwise.

## APIs, SDKs, and Extensibility

Nothing public. No GitHub organization (`lifedatacorp` → 404), no repositories, no client library (official or unofficial — unlike MetricWire, where a third-party Python client at least evidences a private API), no plugin architecture, no custom-sensor mechanism, no white-label offering named (contrast Avicenna Research, which advertises white-labelling). Extensibility is effectively limited to what the study builder exposes plus LifeData's own paid **custom services** (protocol building, dashboard development, custom audit-trail reports).

## Deployment and Infrastructure

Vendor SaaS only; zero researcher-side infrastructure. **Data stored on servers located in the United States** (privacy policy, verbatim), with onward transfer to "a secure data hosting company such as **Microsoft Azure**" — the most specific hosting disclosure of any commercial platform in this module. There is **no EU/UK data-residency option documented**; the vendor's answer to EU data flows is the Data Privacy Framework certification below, not in-region hosting. For a European study under an institutional policy requiring EU-resident storage, this is likely disqualifying, and should be raised with the vendor before anything else.

## Participant Experience

- Native iOS/Android apps, ~1 min onboarding via link/QR, offline-capable, anonymous mode available.
- App-store signal is thin but real: RealLife Exp holds **4.3 (19 ratings)** on the App Store and **3.6** on Google Play. Play reviews visible in this pass include a participant complaint about **notifications behaving as though they had timed out when they had not**, and one about an update making the app "immediately…" (truncated). This is anecdotal, n-of-few, and **Reported** only — but it points at exactly the failure mode that matters most for a signal-contingent EMA study (missed/expired prompts recorded as non-response), and is worth checking against a pilot.
- Battery/data-usage impact is not documented and, given that there is no continuous background sensing, is likely low relative to true phenotyping platforms — that is inference, not a vendor claim.
- No participant-facing dashboard is documented; support is routed through the study team ("Payment for participation is the responsibility of the study coordinator," per the vendor's own Play Store reply).

## Privacy, Security, and Compliance

**Read this section carefully: the marketing pages and the legal documents do not say the same thing.**

**What is Verified from primary legal documentation (`/lifedata-privacy-policy/`, `/lifedata-terms-of-use/`):**

- **EU–U.S. Data Privacy Framework, the UK Extension, and the Swiss–U.S. DPF** — LifeData states it has **certified to the U.S. Department of Commerce** under all three, subjects EU/UK/Swiss personal data to the DPF Principles, commits to DPA/ICO/FDPIC cooperation and to binding arbitration, and recognises **FTC** enforcement jurisdiction. This is a specific, named, externally-registerable status and the strongest single compliance artefact LifeData has. *(Independent confirmation on `dataprivacyframework.gov` was attempted this pass and the site's search API returned errors to automated requests — the certification is therefore **Corroborated (specific, self-declared, externally checkable)** rather than **Verified**; a human should confirm the listing directly.)*
- **GDPR role: LifeData is a Processor**, the study creator is the Controller — stated explicitly and consistently, including that consent is obtained by Controllers and data-subject access requests route through them. Deletion requests originating with a Controller are completed **within 30 days**.
- **Data retention and deletion, with actual numbers**: data is **permanently deleted 180 days** after account cancellation or subscription lapse (retrievable before then by request to `support@lifedatacorp.com`); researcher-initiated deletion of a study through the web app is **permanent after no more than 30 days**; accounts inactive **over 12 months** may be terminated and their content deleted, after an emailed warning. These are the most concrete retention figures of any commercial platform in this module.
- **Data ownership**: "Your data is owned by you… We don't sell it… we don't use the responses you collect for our own purposes" except under legal compulsion. The Terms nonetheless take a broad "worldwide, royalty free license" to study content for the limited purpose of providing the service, surviving termination — standard SaaS language, but worth an institutional contracts review.
- **Named security safeguards** (Privacy Policy §5): authentication/access management, "encryption to prevent unauthorized access," firewalls and malware detection, and backup/restore procedures, based on a stated periodic risk assessment. **Encryption at rest is not distinguished from encryption in transit and no cipher or key-management detail is given.** Google Play declares "Data is encrypted in transit" for both apps.
- **No IP addresses are collected from the mobile device** (explicitly stated), though web server logs do record them for the researcher console.
- Governing law: **State of Indiana**.

**What is claimed only in marketing, and is NOT supported by anything in the legal documentation:**

- "**HIPAA & GDPR Compliance**" / "LifeData's ePRO Data Collection is HIPAA and GDPR compliant" / "Securely and anonymously collect and store data on a HIPAA compliant platform" (four+ separate marketing pages). **The privacy policy and terms of use contain the word HIPAA zero times.** There is **no mention of a Business Associate Agreement**, no Privacy Rule or Security Rule language, no covered-entity/business-associate framing. One page ( `/clinical-research/`) even misspells it "HIPPA." Per CLAUDE.md, compliance is **not** inferred from a general company claim: **treat HIPAA status as Unclear and BAA availability as unconfirmed.** The home page's own framing — "Gather data without Personally Identifiable Information (PII) / Comply with IRB/HIPAA requirements" — suggests the intended posture is *compliance by de-identification* (run the study in anonymous mode so PHI never enters the platform), which is a legitimate design but is **not** the same thing as a HIPAA-compliant service under a BAA. A team handling identifiable PHI must get this in writing.
- **SOC 2: not mentioned anywhere.** **ISO 27001: not mentioned anywhere.** **21 CFR Part 11: not mentioned anywhere** — notable given that the vendor sells a "Clinical" tier with "Real-time eCOA" and multi-site support into regulated clinical trials, where Part 11 / Annex 11 validation is normally a threshold question. **No trust centre, no security whitepaper, no DPA template is published.**
- No penetration-test, sub-processor list (beyond the generic "Microsoft"), or breach-notification commitment is published.

**Net assessment:** on *documented data-protection posture* LifeData sits mid-pack in this module — better than MetricWire (whose compliance documentation could not be located at all across two passes) and better than the academic open-source platforms on retention/deletion specificity, but clearly behind **Avicenna Research**, which holds a dated, third-party-audited ISO 27001:2022 certification. LifeData's DPF certification is a real, externally verifiable status; its HIPAA claim is marketing text with no legal-document backing.

## Pricing

**Non-public. Every route ends at "Schedule Consultation."** The site has no `/pricing` page (HTTP 404), and third-party directories (SoftwareSuggest, ZoomInfo) list it as quote-only.

What *is* publicly stated about the pricing **model** is unusually clear even though no figures are given, and is worth recording because it differs structurally from competitors:

- Pricing is **not feature-gated and not per-project**: "subscription pricing is not feature or project-based… Pilot future projects while running a current project or enjoy the benefits of running multiple projects at no extra cost." Every subscription includes all study-builder features, both native apps, technical support, "easy and unlimited data access," and the visualization/engagement dashboards.
- The three variables are: **number of researchers × subscription duration × number of participants over that duration**.
- **Half-year and annual** subscription terms; separate **academic and commercial** pricing.
- Five tiers: **Individual**, **Team** (up to 9 users, lower cost per researcher), **Enterprise** (10+ users, institutional master subscription with department sub-accounts), **Clinical** (real-time eCOA, multi-site, consulting), **Monitoring** (ePRO, clinician dashboards, site/staff training).
- A **graduate-student discount** exists for qualifying students (vendor-stated).
- A substantial **paid professional-services menu** sits alongside the subscription: protocol consultation, protocol review, protocol building, sponsor/site training, methodological consultation, user-acceptance testing, data monitoring/reporting, dashboard development, custom audit-trail reports, and data-analysis consultation. **None is priced publicly**, and several (audit trails in particular) cover ground a research team might reasonably have assumed was included.

No free tier or public free trial is advertised — a difference from Avicenna Research, whose free trial is at least third-party-reported. All figures require vendor contact.

## Support and Services

- Technical support is included in every subscription (vendor-stated), delivered through a **help centre at `support.lifedatacorp.com` / `help.lifedatacorp.com` that is entirely login-gated** — bare fetches return HTTP 403 behind a challenge, and the Zendesk help-centre API returns `"Couldn't authenticate you"`. The contact page confirms the design: "If you are in need of technical support, please log into your account and submit a request through the help center."
- **This is the profile's largest evidence limitation and it is a structural one.** There is **no public researcher documentation of any kind** — no data dictionary, no export schema, no sensor/permission reference, no scheduling semantics reference. Everything in the sections above comes from marketing pages, legal documents, app-store metadata, or published papers. A prospective adopter cannot evaluate the platform's actual capabilities without first entering a sales conversation. Contrast Avicenna Research (`avicennaresearch.dev` feature docs), m-Path (public pricing and docs), and every open-source platform in this module.
- Extensive paid services (see Pricing) including IRB-adjacent methodological consultation and site training — a heavier services layer than most of this module.
- Marketing/blog content is **stale**: the WordPress post sitemap's most recent `lastmod` is **2024-07-30**, and much of the blog is 2018–2019 literature roundups. This is a stale-content signal, not an abandonment signal — see below.

## Evidence of Use

Active and substantial, and this is the platform's strongest suit:

- **Vendor-stated scale** (`/features/`, `/` counters, Reported): "more than 600 studies, 90,000 participants, nearly 1 billion responses, and deployments in 65 countries," 14 years of operation, 225+ customer publications, 750M+ data points.
- **Independently checkable**: the vendor's own `/customer-publications/` page lists roughly **260 publications spanning 2016–2026**, including **26 dated 2026** — the list is genuinely maintained, not a frozen artefact. Institutional logos on the home page link to Harvard, Stanford, Yale, Penn, Columbia, Michigan, Berkeley, UCSF, Cambridge, HKU, UBC, Mass General, Boston Children's, CHOP, Mayo, MD Anderson, Cedars-Sinai and others.
- **Europe PMC full-text counts (accessed 2026-09-02)**: 74 hits for `"RealLife Exp"`; 6 for `"lifedatacorp"`; 162 for `"LifeData" AND "ecological momentary"` (noisy, do not use as a count). Per CLAUDE.md, these are breadth signals, not quality proxies.
- Domains skew to psychology/psychiatry: suicidal thoughts and behaviours, mindfulness, binge eating and food addiction, smoking/vaping, functional neurological disorder, autism and neurodevelopmental conditions, sleep, chronic pain, audiology, caregiving.
- Examples reachable this pass: Nock et al. 2026 (*J Psychopathol Clin Sci*, N=619); Ball et al. 2025 (*Behav Ther*, PMC13289574); Speyer et al. 2023 (*Int J Methods Psychiatr Res*, PMC10698810 — z-proso EMA adherence sub-study, "delivered via an application provided by LifeDataCorp LLC"); a 2026 *Sci Rep* HRV/affect study (PMC12864953) naming "the RealLife Exp application (associated to the Lifedatacorp platform)".

**Maintenance-status verdict: Active, with a stale-marketing caveat.** Evidence for: four app-store listings updated between **April and August 2026**; a website rebuilt in **2026** (Elementor asset timestamps, © 2026); a **new platform generation shipped in 2025–2026**; a staffed team page listing five engineers, a principal designer and a CEO; a publications list carrying 26 entries from 2026. Evidence against: a **blog dead since July 2024** and a **broken internal link** — the footer "Products" link points at `?page_id=23768`, which returns the site's 404 page. The broken link and stale blog are cosmetic-website neglect, not product abandonment; the product-side signals are unambiguous.

## Module 3 candidates — two deployments identified

Both were verified from full text this pass and are recorded here so Module 3's platform-must-be-profiled rule is now satisfied. **These are pointers only; Module 3 owns their profiles.** Note that both are suicide-risk EMA studies from the same Harvard/Boston research programme, so they are not independent replications of each other.

1. **Nock MK et al. 2026** — "Using smartphone surveys to predict next-week suicide attempts," *Journal of Psychopathology and Clinical Science*. DOI `10.1037/abn0001117`; PMID 42149475; **PMC13308188 (not open access — full text retrieved via NCBI efetch this pass; no OA PDF available for the literature library)**. N=619 (313 adults from a psychiatric emergency service, 306 adolescents from a psychiatric inpatient unit, two Boston-area hospitals), 6 surveys/day of 20 items for 3 months. Verified verbatim: participants "installed an app on their smartphone (**LifeData**)." Operational findings: **502 of 619 consented participants (81.1%) provided data in at least one survey**, together starting **79,448 surveys**; **rolling median and mean survey initialization rates were <50% across the three-month period and decreased over time**. The predictive models used survey responses plus "passively collected survey **meta-data**" (e.g. time since last submission) — **response metadata, not phone sensor data**, consistent with the scope note above. The largest LifeData deployment identified anywhere in this pass.

2. **Ball MI et al. 2025** — "Engagement in Ecological Momentary Assessment of Suicidal Thoughts and Behaviors: A Mixed Methods Study," *Behavior Therapy*. DOI `10.1016/j.beth.2025.05.007`; PMID 41139109; PMC13289574 (open access via Europe PMC full-text XML; **the PDF could not be retrieved — Europe PMC's `fullTextPDF` endpoint returns 404 for this record and PMC's PDF routes return an HTML challenge to automated requests**, so no PDF was added to `literature/`). Verified verbatim from full text: "**Due to platform changes during the study, 90% (n = 90) received EMA through the smartphone application (app) Realtime EXP by LifeData, and 10% (n = 10) received EMA through the smartphone app Catalyst by MetricWire.**" Design detail also verified: morning and nighttime surveys at participant-selected fixed times, daytime surveys random with a ≥90-minute minimum spacing, each survey open for two hours; $1/survey with a $4 daily bonus for 5–6 surveys, up to $350; inpatient period plus 28 days post-discharge.

Ball et al. is additionally the **only published head-to-head LifeData/MetricWire deployment** located in this pass — a mid-study platform switch within one cohort — and is therefore unusually relevant to both profiles. It also independently confirms MetricWire's backend product name **"Catalyst,"** which `profiles/metricwire.md` currently records only on the strength of an unofficial third-party Python client. That is a genuine upgrade in evidence for MetricWire and is flagged here for whoever integrates this profile; **`metricwire.md` was not edited by this pass.**

## Strengths

- **Deep, specific, and unusually well-documented EMA/ESM scheduling and adaptive-logic engine**: fixed/random/triggered/event-based schedules with configurable minimum inter-prompt spacing, branching, two distinct trigger types (delayed follow-up *and* activation of an entire new schedule), display logic, piped text, computed scores, and response-driven adaptive automation. The schedule-activating trigger in particular supports EMI/JITAI designs and is more precisely documented than any comparable commercial claim in this module.
- **The longest continuous operating history and largest publication trail of any commercial platform in this module** — participant apps shipping since **January 2015**, ~14 years of company operation, ~260 vendor-listed publications through 2026 across a broad institutional base. On evidence-of-use, it clearly exceeds MetricWire (where no publication list was located) and is at least comparable to Avicenna/Ethica.
- **Fully offline-capable collection** with automatic sync — protocol lives on the device, so connectivity gaps do not stop data capture. Relevant for rural, low-connectivity, and international deployments.
- **Concrete, numeric retention and deletion terms** (180 days / 30 days / 12-month inactivity) — more specific than any other commercial platform profiled here.
- **DPF-certified with the U.S. Department of Commerce** (EU, UK Extension, Swiss), with named FTC jurisdiction and arbitration commitments — a specific, externally checkable status.
- **Anonymous mode plus researcher-assigned IDs** designed to keep PII out of the platform entirely while still linking to external datasets — a genuinely useful design for IRB-constrained studies.
- Real-time study **alerts on responses/scores/events**, well matched to risk-monitoring designs (and demonstrably used that way in the suicide-research literature).
- All-features-included, multi-project subscription model: pilots and parallel studies at no extra cost, which is friendlier to exploratory academic work than per-study pricing.

## Limitations

- **Not a passive-sensing platform.** Response-linked GPS is the only sensor stream documented. No accelerometer, screen/app usage, communication metadata, Bluetooth, audio, or any other phenotyping stream; no wearable, HealthKit, Health Connect, or EHR/FHIR integration. If a study needs passive behavioural sensing, LifeData is the wrong tool and no configuration will fix that.
- **No public researcher documentation at all** — the help centre is entirely login-gated. No data dictionary, export schema, permission model, or scheduling reference can be read before entering a sales conversation. This is the most severe documentation opacity of any platform in this module, worse than MetricWire's (whose site is bot-blocked but at least has public feature pages of comparable depth).
- **No API, SDK, GitHub presence, plugin architecture, or white-labelling.** Data access is dashboard-and-CSV only. Unlike MetricWire, not even an unofficial third-party client exists to evidence a private API.
- **Pricing entirely non-public**, with no advertised free tier or trial, and a large paid-services menu (including **audit trails**, which read as bespoke work rather than a shipped feature) whose costs are also unpublished.
- **The HIPAA claim is marketing-only.** Four-plus pages assert HIPAA compliance; the privacy policy and terms of use never mention HIPAA, a BAA, or the Security/Privacy Rules. **SOC 2, ISO 27001, and 21 CFR Part 11 appear nowhere**, despite an explicitly marketed "Clinical" eCOA tier for regulated multi-site trials. No trust centre, security whitepaper, DPA template, or sub-processor list.
- **US-only data residency**, with no documented EU/UK in-region option — likely disqualifying under some European institutional data-governance policies regardless of the DPF certification.
- **Two live platform generations with no published migration or end-of-support guidance.** The entire evidence base attaches to the "Original" app; LifeData+ has no published deployments, one App Store rating, and a **minimum iOS 18.0** requirement that will exclude older participant devices — a real recruitment consideration for populations with ageing phones.
- **iOS/Android parity is not independently verified** (per CLAUDE.md, not assumed). Nothing suggests a gap — the feature set is survey-centric, where parity is far more achievable than for background sensing — but it has not been confirmed stream-by-stream.
- **Stale marketing surface**: blog dead since July 2024, and a broken internal link (footer "Products" → 404) on the vendor's own freshly rebuilt site. Cosmetic rather than substantive, but it undercuts the site as a reliable current-state reference.
- Participant-side app-store ratings are thin (19 iOS ratings; 3.6 on Play) and include a **notification-timeout complaint** — anecdotal, but pointed at the exact mechanism a signal-contingent design depends on.

## Best-Fit Use Cases

- **Intensive longitudinal self-report studies** — ESM/EMA, daily diary, event-contingent reporting — where the science lives in the questions and the sampling design, not in phone sensors. This is squarely the platform's home ground and the reason for its publication record.
- **Complex adaptive protocols**: multi-schedule designs, response-triggered follow-ups, computed scores driving branching, and trigger-activated new schedules (EMI/JITAI-adjacent designs).
- **Risk-monitoring designs** needing real-time alerts on participant responses — clinical psychology, suicide research, substance use.
- **Fully remote, no-infrastructure deployments** where the team has no DevOps capacity and wants QR/link onboarding in minutes.
- **Low-connectivity or international field settings**, given genuinely offline-capable collection and multi-language (including RTL) support.
- **IRB-sensitive studies that can run de-identified**, using anonymous mode plus researcher-assigned IDs to keep PII off the vendor's servers entirely.
- Teams who value a **decade-plus publication trail and a well-worn methodological support offering** over technical openness.

## Poor-Fit Use Cases

- **Any study requiring passive smartphone sensing or digital phenotyping** — mobility/GPS traces, accelerometry, screen or app usage, communication metadata, audio features. Use Beiwe, RADAR-base, AWARE, mindLAMP, or CARP instead.
- **Studies needing wearable, HealthKit, Health Connect, or EHR/FHIR integration** — none documented.
- Teams needing **programmatic/API access, streaming or near-real-time pipelines, or direct database access**.
- Teams requiring **self-hosting, data custody, or source-code auditability**.
- **Studies bound by EU/UK data-residency requirements**, absent a vendor-confirmed in-region option.
- **Regulated clinical trials with a hard 21 CFR Part 11 / computer-system-validation gate**, or any study handling identifiable PHI that needs a signed BAA — neither is publicly evidenced, despite the Clinical tier's marketing.
- Teams that must **evaluate technical capability from public documentation before contacting sales**, or that need firm pricing up front.
- Studies recruiting participants on **older iOS devices** if deploying on LifeData+ (min iOS 18.0).

## Open Questions

*(Directed to: LifeData, LLC — `contact@lifedatacorp.com`, `support@lifedatacorp.com`, consultation booking at https://www.lifedatacorp.com/schedule-consultation/. Note that the login-gated help centre means **most of these can only be answered by the vendor** — this platform has a higher vendor-contact dependency than any other in this module.)*

1. **Is there any passive/background data collection at all** beyond response-linked GPS — including continuous or geofenced location — on either platform generation? (Public materials say no; the gated documentation cannot rule it out.)
2. **Is background/continuous location supported on iOS**, and how do iOS background-execution limits affect notification delivery and location capture relative to Android? Is there any documented iOS/Android feature gap?
3. **HIPAA specifically: will LifeData execute a Business Associate Agreement?** Under what tier and at what cost? What is the basis for the site-wide "HIPAA compliant" claim given that the legal documents never mention it?
4. **SOC 2, ISO 27001, and 21 CFR Part 11 / computer-system validation** — does any documentation, certification, or validation package exist, particularly for the "Clinical" eCOA tier? Is a security whitepaper or trust centre available under NDA?
5. **Is encryption at rest implemented**, and with what cipher/key management? (The privacy policy says only "encryption," undifferentiated.)
6. **Is EU/UK data residency available**, or is US-only storage plus DPF certification the sole option? Is a DPA template available?
7. **Actual pricing** for each tier — the researcher/duration/participant formula in real numbers, the size of the graduate-student discount, service-menu rates (especially **audit trails**), and whether any free trial or pilot tier exists.
8. **Is there any API, webhook, or programmatic export**, official or partner-only? What does `api.lifedatacorp.com` serve?
9. **LifeData+ vs the Original platform**: is there an end-of-support date for RealLife Exp? What is the migration path for an in-flight study? What capabilities differ between the two? Which does the vendor recommend for a new academic study today?
10. **What is the exact discrepancy** behind "Released in 2026" (website) vs a 2025-05-28 App Store first release and "released in 2025" (app description)?
11. **Export schema specifics**: what exactly are the "multiple data formats… including multilevel modeling," and what does "participant study downloads (varies by subscription)" limit?
12. **Data-flow latency** — how quickly do uploaded responses become available for export/dashboard? (Not documented; Avicenna Research publishes a "minutes after upload" figure for comparison.)
13. **Are audit trails a standard feature or bespoke paid work**, and can they meet regulated-trial audit requirements?
14. Participant-side **notification reliability** — is the timeout behaviour reported in Play Store reviews a known issue, and was it resolved?

## Key Links

- Official site: https://www.lifedatacorp.com/
- Features (full list): https://www.lifedatacorp.com/features/
- Products and tiers, services menu, pricing FAQ: https://www.lifedatacorp.com/products-2/
- Solutions — Research: https://www.lifedatacorp.com/solutions-research/
- ESM app page: https://www.lifedatacorp.com/experience-sampling-app-2/
- EMA app page: https://www.lifedatacorp.com/ecological-momentary-assessment-app-2/
- eDiary: https://www.lifedatacorp.com/ediary-app/ · ePRO: https://www.lifedatacorp.com/epro/ · eCOA: https://www.lifedatacorp.com/ecoa/
- Clinical research: https://www.lifedatacorp.com/clinical-research/ · Remote patient monitoring: https://www.lifedatacorp.com/remote-patient-monitoring/
- The Science of ESM/EMA: https://www.lifedatacorp.com/the-science-2/
- **Customer publications list (~260 entries, 2016–2026)**: https://www.lifedatacorp.com/customer-publications/
- Team: https://www.lifedatacorp.com/the-team/
- Privacy Policy (**DPF, GDPR-processor role, retention/deletion, Azure, security safeguards**): https://www.lifedatacorp.com/lifedata-privacy-policy/
- Terms of Use: https://www.lifedatacorp.com/lifedata-terms-of-use/
- Contact / consultation: https://www.lifedatacorp.com/contact-us/ · https://www.lifedatacorp.com/schedule-consultation/
- Researcher console — Original platform: https://server.lifedatacorp.com/server-frontend/index.html
- Researcher console — LifeData+: https://app.lifedatacorp.com/
- Help centre (**login-gated; HTTP 403 to anonymous fetch**): https://support.lifedatacorp.com/hc/en-us
- RealLife Exp — App Store: https://apps.apple.com/us/app/reallife-exp/id939951918
- RealLife Exp — Google Play: https://play.google.com/store/apps/details?id=com.lifedata.reallife_exp
- LifeData (LifeData+) — App Store: https://apps.apple.com/us/app/lifedata/id6443996884
- LifeData (LifeData+) — Google Play: https://play.google.com/store/apps/details?id=com.lifedata.lifedata
- Demo protocol / rapid-onboarding link: https://lifedatacorp.page.link/jgPjLQNpbRKch1nTA
- Data Privacy Framework registry (to confirm the certification): https://www.dataprivacyframework.gov/
- No GitHub organization exists (`https://api.github.com/orgs/lifedatacorp` → HTTP 404)
- **No pricing page** — `https://www.lifedatacorp.com/pricing/` returns HTTP 404
- **Known broken vendor link**: footer "Products" → `https://www.lifedatacorp.com/?page_id=23768` → the site's 404 page

## Sources

1. LifeData — homepage. https://www.lifedatacorp.com/ (**direct fetch**, accessed 2026-09-02). **Primary/Verified (vendor-stated).** Feature highlights (experience sampling, eDiary, random/fixed schedules, branching/triggering, offline collection, anonymous mode, remote onboarding, research teams/roles), the "How it works" three-step flow, CSV export and real-time dashboards, the "Easy HIPAA/GDPR compliance" marketing block, and the vendor's scale counters (600+ customers, 65 countries, 225+ customer publications, 90,000+ participants, 750M+ data points — read directly from the counter widgets' `data-to-value` attributes). Also the "LifeData Original / LifeData+ (Released in 2026)" platform switcher and the two console URLs.
2. LifeData — Features. https://www.lifedatacorp.com/features/ (**direct fetch**, 2026-09-02). **Primary.** The full current feature list, framed as LifeData+ "built on 14 years of experience… more than 600 studies, 90,000 participants, nearly 1 billion responses, 65 countries." Establishes 13 question types, smart logic/piped text/scores, adaptive study automation, study alerts, millisecond timestamps, **"Location Data (GPS) — capture location data with participant responses"** as the sole sensor entry, multi-language incl. RTL, and the "HIPAA & GDPR Compliance" claim.
3. LifeData — Products. https://www.lifedatacorp.com/products-2/ (**direct fetch**, 2026-09-02). **Primary.** Five tiers (Individual/Team/Enterprise/Clinical/Monitoring), the ten-item paid services menu (including **Audit Trails** as a bespoke service), and the pricing FAQ — what a subscription includes, the graduate-student discount, and the researcher × duration × participants pricing formula with no figures.
4. LifeData — Solutions: Research. https://www.lifedatacorp.com/solutions-research/ (**direct fetch**, 2026-09-02). **Primary.** "Gather GPS coordinates with each user response"; question types incl. image capture and consent; "All responses are timestamped and geolocation reporting is standard"; CSV export with "multiple data formats… including multilevel modeling."
5. LifeData — ESM and EMA app pages. https://www.lifedatacorp.com/experience-sampling-app-2/ , https://www.lifedatacorp.com/ecological-momentary-assessment-app-2/ (**direct fetches**, 2026-09-02). **Primary.** Independently repeat the response-linked-geolocation wording, corroborating the sensor-scope finding across pages.
6. LifeData — Who We Serve: Psychological Science / Clinical Trials / Healthcare Research; Clinical Research; eDiary; ePRO; eCOA; Remote Patient Monitoring. (**direct fetches**, 2026-09-02). **Primary.** "Collect participants' geolocation when they respond, if needed"; offline collection; multi-site support; export "formatted for easy analysis in Python, R, SPSS, Stata"; and the repeated unsupported HIPAA/GDPR-compliance marketing claims (incl. the "HIPPA" misspelling on `/clinical-research/`).
7. LifeData — Privacy Policy. https://www.lifedatacorp.com/lifedata-privacy-policy/ (**direct fetch**, 2026-09-02). **Primary/Verified.** EU-U.S. DPF + UK Extension + Swiss-U.S. DPF self-certification to the U.S. Department of Commerce; FTC jurisdiction; DPA/ICO/FDPIC cooperation and binding arbitration; GDPR **processor** role; **US server location**; onward transfer to **Microsoft / Microsoft Azure**; §5 security safeguards (authentication, encryption, firewalls/malware detection, backup/restore, periodic risk assessment); deletion timelines (**180 days** post-cancellation, **30 days** post-request); no mobile-device IP collection; opt-in geolocation only. **Contains no reference to HIPAA, SOC 2, ISO 27001, or 21 CFR Part 11.**
8. LifeData — Terms of Use. https://www.lifedatacorp.com/lifedata-terms-of-use/ (**direct fetch**, 2026-09-02). **Primary/Verified.** Content licence terms, 180-day deletion, **12-month inactivity termination**, Indiana governing law, no-minors clause. Also contains no HIPAA reference.
9. LifeData — Contact Us; The Team. https://www.lifedatacorp.com/contact-us/ , https://www.lifedatacorp.com/the-team/ (**direct fetches**, 2026-09-02). **Primary.** Confirms support is routed exclusively through the login-gated help centre; team roster (CEO Kevin Eklund; co-founders Tim Steenbergh PhD and Jason Runyan DPhil; five named engineers and a principal designer) as an active-staffing signal.
10. LifeData — Customer Publications. https://www.lifedatacorp.com/customer-publications/ (**direct fetch**, 2026-09-02). **Primary.** ~260 listed publications, 2016–2026, including 26 dated 2026 — evidence the list is actively maintained.
11. LifeData help centre. https://support.lifedatacorp.com/hc/en-us (**direct fetch attempted**, 2026-09-02). **Primary/negative result.** HTTP 403 behind a challenge page; the Zendesk help-centre API returns `{"error":"Couldn't authenticate you"}`. Establishes that researcher documentation is login-gated — an access barrier confirmed by attempt, not an unattempted gap.
12. Apple App Store lookups via the iTunes API (**direct fetch**, 2026-09-02). https://apps.apple.com/us/app/reallife-exp/id939951918 and https://apps.apple.com/us/app/lifedata/id6443996884 . **Primary/Verified.** RealLife Exp: seller LIFEDATA LLC, bundle `com.lifedata.reallife-exp`, first release **2015-01-03**, v2.8.14 of **2026-04-06**, min iOS 13.0, rating 4.3/19; description establishes the **"LifePak"** terminology. LifeData: bundle `com.lifedata.LifeData`, first release **2025-05-28**, v1.0.16 of **2026-08-27**, min **iOS 18.0**, 1 rating; description says "the new LifeData platform released in **2025**" — the source of the release-year conflict recorded above.
13. Google Play listings (**direct fetches**, 2026-09-02). https://play.google.com/store/apps/details?id=com.lifedata.reallife_exp and `?id=com.lifedata.lifedata`. **Primary/Verified.** RealLife Exp released **2015-01-11**, updated **2026-04-08**, rating 3.6; LifeData released **2025-11-27**, updated **2026-07-18**. Data safety: RealLife Exp collects "Location, Personal info and 3 others" and may share app info/performance with third parties; LifeData collects "Location, Personal info and 4 others" and shares no data with third parties; both "encrypted in transit," both support deletion requests. Also the participant review reporting notification-timeout behaviour, and LifeData's own reply routing payment questions to the study coordinator.
14. LifeData WordPress sitemaps (**direct fetch**, 2026-09-02). https://www.lifedatacorp.com/sitemap_index.xml , `/page-sitemap.xml` , `/post-sitemap.xml`. **Primary.** Complete public page inventory (confirming no pricing, API, or documentation page exists) and the blog's most recent `lastmod` of **2024-07-30** — the stale-content finding.
15. Negative technical probes (**direct**, 2026-09-02). `https://api.github.com/orgs/lifedatacorp` → HTTP 404; GitHub repository search for the product names → 0 results; `https://www.lifedatacorp.com/pricing/` → HTTP 404; `api.lifedatacorp.com` at `/`, `/docs`, `/swagger`, `/v1`, `/api-docs`, `/health` → HTTP 404; footer "Products" link `?page_id=23768` → site 404 page. **Verified negatives** supporting the closed-source, no-public-API, no-public-pricing, and broken-link findings.
16. Ball MI, et al. (2025). "Engagement in Ecological Momentary Assessment of Suicidal Thoughts and Behaviors: A Mixed Methods Study." *Behavior Therapy*. DOI 10.1016/j.beth.2025.05.007; PMID 41139109; PMC13289574. **Full text retrieved and read via Europe PMC `fullTextXML` (2026-09-02) — Verified verbatim**, not from an abstract: the 90% LifeData / 10% MetricWire Catalyst platform split due to a mid-study platform change, the schedule design, and the incentive structure. OA PDF could not be downloaded (Europe PMC `fullTextPDF` → 404; PMC PDF routes → HTML challenge).
17. Nock MK, et al. (2026). "Using smartphone surveys to predict next-week suicide attempts." *Journal of Psychopathology and Clinical Science*. DOI 10.1037/abn0001117; PMID 42149475; PMC13308188. **Full text retrieved and read via NCBI efetch (2026-09-02) — Verified verbatim**: "installed an app on their smartphone (LifeData)"; N=619 across two Boston-area hospitals; 502/619 (81.1%) provided any data; 79,448 surveys started; rolling median and mean initialization rates <50% and declining over three months; predictors included "passively collected survey **meta-data**." **Not open access** — no PDF stored.
18. Speyer LG, Murray AL, et al. (2023). "Respondent characteristics associated with adherence in a general population ecological momentary assessment study." *Int J Methods Psychiatr Res*; PMC10698810. **Full text via Europe PMC (2026-09-02).** Independent third-party confirmation of research use: the z-proso EMA sub-study was "delivered via an application provided by **LifeDataCorp LLC**," 4 surveys/day for 2 weeks on a quasi-random within-window schedule, mean response latency 25 minutes.
19. *Scientific Reports* (2026), "Interplay between resting heart rate variability, daily affective dynamics and mental health"; PMC12864953. **Full text via Europe PMC (2026-09-02).** Independent naming: "the **RealLife Exp** application (associated to the **Lifedatacorp** platform)," semi-random signal-contingent sampling with eight notifications per day. Corroborates the RealLife-Exp-vs-Realtime-EXP naming point.
20. Europe PMC REST search API (2026-09-02). https://www.ebi.ac.uk/europepmc/webservices/rest/search . **Bibliometric breadth only, not a quality measure.** `"RealLife Exp"` → 74 hits; `"Realtime EXP"` → **1** hit (Ball et al. 2025); `"lifedatacorp"` → 6; `"LifeData" AND "ecological momentary"` → 162 (noisy).
21. Third-party directory/company listings — SoftwareSuggest, ZoomInfo, LinkedIn (search summaries, 2026-09-02). **Reported.** Corroborate quote-only pricing; no rate figures located anywhere.
