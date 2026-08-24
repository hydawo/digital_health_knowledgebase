# mindLAMP (LAMP Platform)

## Quick Facts

| Field | Details |
|---|---|
| Organization | BIDMC Division of Digital Psychiatry (Beth Israel Deaconess Medical Center / Harvard Medical School), led by John Torous |
| Category | Open-source digital phenotyping and mobile-intervention platform, mental-health oriented |
| Current status | Active, with some component repositories explicitly marked deprecated (see below) |
| Platforms/devices | iOS and Android apps; web dashboard/portal |
| Open source | Yes — code hosted publicly under the BIDMCDigitalPsychiatry GitHub organization |
| Hosting/deployment | Self-hostable (server component); mindLAMP's own documentation advertises "flexible hosting and complete data access," implying a managed-hosting option exists alongside self-hosting, but the site did not state whether it is offered to outside teams or under what terms this session |
| Pricing model | Free/open source (software); no pricing figures found for any managed-hosting arrangement |
| Last verified | 2026-08-24 (second-pass direct-source re-verification) |

## Summary

mindLAMP (Learn, Assess, Manage, Prevent), built on the "LAMP Platform," is an open-source digital phenotyping and mobile-intervention tool from Harvard-affiliated BIDMC's Division of Digital Psychiatry. It is explicitly positioned to support both **research and clinical use** of patient-generated health data — a dual orientation that distinguishes it from research-only platforms like Beiwe or RADAR-base. It combines active data collection (surveys, cognitive/behavioral tasks) with passive smartphone sensing, and is used by clinical research teams internationally (the search evidence names teams in Canada and Australia running adapted versions of the platform).

**Status note — resolved in second pass (2026-08-24, Verified via direct GitHub fetch, resolves unresolved-question #87):** `LAMP-portal` and `LAMP-app` are not just labeled deprecated in their descriptions — **both were formally archived by their owner on Nov 17, 2020**, and GitHub reports each as "read-only." Direct inspection of the BIDMCDigitalPsychiatry organization's current (non-archived) repository listing shows the successor architecture clearly:

| Deprecated (archived 2020-11-17) | Current successor |
|---|---|
| `LAMP-portal` | `LAMP-dashboard` (the mindLAMP researcher/clinician web dashboard; TypeScript, actively updated as recently as Aug 21, 2026) |
| `LAMP-app` | `LAMP-core-android` (Kotlin) and `LAMP-core-ios` (Swift) — described as "core scaffolding for digital phenotyping apps," rather than a single monolithic app repo |

Other current, actively updated repositories confirmed in the same fetch: `LAMP-server` (backend, updated Aug 20, 2026), `LAMP-platform` (docs/issues), `LAMP-activities` (cognitive tests, updated Aug 19, 2026), `LAMP-app-gateway` (push/logging gateway), `LAMP-js` and `LAMP-py` (API clients, BSD-3-Clause licensed), `LAMP-cortex` and its successor `LAMP-toolkit` (analytics, MIT licensed). The organization hosts 32 repositories total; only the 10 most-starred/most-relevant were enumerated directly. **A prospective adopter should build on `LAMP-dashboard`, `LAMP-server`, and `LAMP-core-android`/`LAMP-core-ios`, not `LAMP-portal` or `LAMP-app`.**

## Products / Platform Architecture

- **mindLAMP app** (iOS/Android) — participant-facing app for surveys, cognitive/behavioral tasks, and passive sensing.
- **mindLAMP dashboard** — researcher/clinician-facing web portal for study configuration and data review.
- **LAMP-server** — backend server component (TypeScript), actively updated (Aug 2026).
- **LAMP-dashboard** — researcher/clinician web dashboard (TypeScript), successor to the archived `LAMP-portal`.
- **LAMP-core-android** / **LAMP-core-ios** — mobile app scaffolding (Kotlin/Swift), successors to the archived `LAMP-app`.
- **LAMP-activities** — cognitive-test library.
- **LAMP-app-gateway** — push notification/logging gateway server.
- **LAMP-js** / **LAMP-py** — official JavaScript and Python API clients (BSD-3-Clause).
- **LAMP-cortex** (legacy) / **LAMP-toolkit** (current successor, MIT licensed) — analytics pipeline.
- Legacy/archived: `LAMP-portal`, `LAMP-app` — both formally archived by the owner on 2020-11-17 (Verified, direct GitHub fetch, second pass).

## Sensors and Data Streams

**Second-pass update (2026-08-24, Corroborated — direct fetch of docs.lamp.digital's landing content):** the documentation names passive streams including **GPS, accelerometer, screen time, calls, heart rate, steps, sleep, and gyroscope**, stated to flow into "one consistent format, enabling comparison across projects." This upgrades the general claim from Unclear to Corroborated, but the fetch was of general marketing/landing content rather than a full sensor-by-sensor reference page (unlike the AWARE second-pass result), so **exact iOS-vs-Android parity for each stream remains not independently verified** — still an open question, and one that matters given the platform's clinical-use orientation where data completeness has direct care implications.

## Active Data Collection

Surveys, cognitive tests, and behavioral tasks are core to the platform's stated "Assess" and "Manage" functions (per the LAMP name itself: Learn, Assess, Manage, Prevent). This is a materially more clinically-oriented active-assessment design than Beiwe's simpler survey model, per the platform's own framing, though exact EMA scheduling/branching sophistication was not independently benchmarked this session.

## Researcher and Study Management Features

A dashboard/portal component exists for study and participant management, per the platform's own architecture description; specific features (multi-study support, role-based access, adherence monitoring) were not independently verified against current documentation this session.

## Data Access and Export

Not independently verified against current documentation this session — flagged as an open question. The platform's dual research/clinical orientation implies data governance considerations (e.g., a clinician using the same platform for patient care) that are distinct from a research-only tool, and this distinction should be confirmed with the maintaining team before use in any protocol involving clinical decision-making.

## APIs, SDKs, and Extensibility

Fully open source under the BIDMCDigitalPsychiatry GitHub organization, permitting institutional forking and modification. **Second-pass update (2026-08-24, Verified via direct fetch):** licence terms are **not uniform across the codebase** — `LAMP-js` and `LAMP-py` (the official API clients) are **BSD-3-Clause**, and `LAMP-toolkit` (the analytics successor to `LAMP-cortex`) is **MIT**. The licence covering the core `LAMP-server`/`LAMP-dashboard`/`LAMP-core-android`/`LAMP-core-ios` repositories specifically was not confirmed (GitHub's org-level repository list did not surface it in this pass) — narrower open item than before, since the client-library and toolkit licences are now settled. An `/api` section is referenced in docs.lamp.digital's navigation, consistent with `LAMP-js`/`LAMP-py` wrapping a documented REST API, though the API reference content itself was not fetched this session.

## Deployment and Infrastructure

Self-hostable server component (`LAMP-server`, confirmed current and actively maintained — Verified). **Second-pass update (2026-08-24):** docs.lamp.digital's own content advertises "flexible hosting and complete data access" as a platform capability, which is suggestive of a managed-hosting option beyond pure self-hosting, but the fetched content did not state whether this is a service offered to outside research/clinical teams, under what terms, or at what cost — **the managed-hosting question is upgraded from Unclear to Reported, not fully resolved; still requires direct BIDMC contact.** The earlier "clinical research teams in Canada and Australia" framing remains Reported only, not independently traced to a specific citation this session. Infrastructure requirements for self-hosting were not independently benchmarked.

## Privacy, Security, and Compliance

Not independently verified this session. Given the platform's explicit clinical-use positioning (not just research), HIPAA and comparable clinical-data-handling documentation would be a first-order question for any team considering clinical deployment — and CLAUDE.md's instruction not to infer compliance from institutional affiliation (Harvard/BIDMC) applies here as directly as anywhere in this module.

## Pricing

Free and open source; no licence fee identified. As with Beiwe and RADAR-base, actual cost is a function of self-hosting infrastructure and staff time, or reliance on whatever hosted-instance arrangement the maintaining team currently offers to outside teams — not independently confirmed this session.

## Research Evidence and Validation

mindLAMP has a substantial published research record centered on mental-health digital phenotyping, including the platform-description paper "Enabling Research and Clinical Use of Patient-Generated Health Data (the mindLAMP Platform): Digital Phenotyping Study" (Vaidyam, Halamka, Torous; *JMIR mHealth and uHealth*, Jan 2022) and subsequent studies on digital-phenotyping correlations in larger mental-health samples, EMA validation in schizophrenia populations, and COVID-related neuropsychiatric sequelae research in college students. This is a strong, mental-health-domain-specific published record, though this session did not attempt an exhaustive publication count.

## Strengths

- Explicit dual research/clinical orientation, distinguishing it from research-only competitors — potentially valuable for teams bridging digital phenotyping research into actual care pathways.
- Strong, mental-health-specific published research record from an established academic digital-psychiatry group.
- Fully open source, permitting institutional self-hosting and modification.
- Combines active clinical assessment tools (cognitive/behavioral tasks) more deeply than some passive-sensing-first competitors.

## Limitations

- ~~Some component repositories are explicitly marked deprecated... this session could not fully map which components are current successors~~ **Resolved 2026-08-24** — `LAMP-portal` and `LAMP-app` are formally archived (2020-11-17); successors are `LAMP-dashboard` and `LAMP-core-android`/`LAMP-core-ios` respectively (Verified, direct GitHub fetch).
- Exact per-stream iOS/Android sensor parity, full data-export mechanics, the licence covering the core server/dashboard/app repositories specifically (as opposed to the now-confirmed BSD-3-Clause/MIT client-and-toolkit licences), and compliance posture remain not independently verified against current documentation, even after this second pass — docs.lamp.digital's full reference documentation (as opposed to its landing content) is the next direct-fetch target for a third pass.
- The clinical-use positioning raises data-governance questions (patient-care data vs. research data) that a purely research-oriented platform doesn't have to answer, and this session did not establish how mindLAMP handles that distinction.

## Best-Fit Use Cases

- Mental-health-focused digital phenotyping research, especially where active cognitive/behavioral assessment matters alongside passive sensing.
- Teams wanting to bridge research findings into a clinical-facing tool built on the same underlying platform.

## Poor-Fit Use Cases

- Teams needing airtight, independently-verified compliance documentation without further due diligence — this session could not establish that documentation.
- Studies where component-level maintenance status is safety-critical and cannot tolerate the ambiguity flagged above around deprecated repositories.

## Open Questions

*(Directed to: BIDMC Division of Digital Psychiatry / John Torous lab — via https://github.com/BIDMCDigitalPsychiatry or https://www.digitalpsych.org)*

- ~~Which specific mindLAMP repositories are current/production, and which are the successors to the repositories explicitly marked deprecated (`LAMP-portal`, `LAMP-app`)?~~ **Resolved 2026-08-24** — see the repository table above (Verified, direct GitHub fetch).
- What open-source licence governs the core `LAMP-server`/`LAMP-dashboard`/`LAMP-core-android`/`LAMP-core-ios` repositories specifically? (`LAMP-js`/`LAMP-py` = BSD-3-Clause and `LAMP-toolkit` = MIT are now confirmed, narrowing this question.)
- What is the exact per-stream iOS-vs-Android sensor parity? (The general passive-sensor list — GPS, accelerometer, screen time, calls, heart rate, steps, sleep, gyroscope — is now Corroborated, but not broken out by platform.)
- What HIPAA/GDPR/compliance documentation exists, particularly for the clinical-use pathway as distinct from pure research use?
- Is the "flexible hosting" mentioned in the platform's own documentation a managed-hosting service available to outside teams, and under what terms/cost? (Existence of the phrase is now Corroborated; terms remain unconfirmed.)

## Key Links

- Digital Psych (lab site): https://www.digitalpsych.org/mindlamp1.html
- Documentation: https://docs.lamp.digital/
- GitHub organization: https://github.com/BIDMCDigitalPsychiatry
- LAMP-server repository: https://github.com/BIDMCDigitalPsychiatry/LAMP-server
- LAMP-dashboard repository: https://github.com/BIDMCDigitalPsychiatry/LAMP-dashboard
- Publications: https://docs.lamp.digital/about/publications/ (site returned an error on direct fetch this session — see Sources)

## Sources

1. BIDMCDigitalPsychiatry GitHub organization. https://github.com/BIDMCDigitalPsychiatry (accessed 2026-08-24, direct fetch — first and second pass). **Primary/Verified.** Repository inventory; second pass directly confirmed `LAMP-portal` and `LAMP-app` were archived by the owner on 2020-11-17 (read-only), identified current successor repositories (`LAMP-dashboard`, `LAMP-core-android`, `LAMP-core-ios`, `LAMP-server`, `LAMP-activities`, `LAMP-app-gateway`, `LAMP-js`, `LAMP-py`, `LAMP-toolkit`), and confirmed BSD-3-Clause (`LAMP-js`, `LAMP-py`) and MIT (`LAMP-toolkit`) licences.
2. Digital Psych — mindLAMP lab page. https://www.digitalpsych.org/mindlamp1.html (accessed 2026-08-24, search summary). Platform framing (Learn, Assess, Manage, Prevent), research/clinical dual orientation.
3. docs.lamp.digital — documentation landing page (**direct fetch, second pass**). https://docs.lamp.digital/ (accessed 2026-08-24). **Corroborated** (landing/marketing content, not a full reference page). Passive-sensor list (GPS, accelerometer, screen time, calls, heart rate, steps, sleep, gyroscope), "flexible hosting and complete data access" framing, `/api` navigation reference.
4. Vaidyam A, Halamka J, Torous J. "Enabling Research and Clinical Use of Patient-Generated Health Data (the mindLAMP Platform): Digital Phenotyping Study." *JMIR mHealth and uHealth* 2022;10(1). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8783287/ (accessed 2026-08-24, search summary). Platform-description peer-reviewed paper.
5. mindLAMP publications listing. https://docs.lamp.digital/about/publications/ — **fetch attempted, returned HTTP 404 both sessions**; existence and framing corroborated via search summary only. Still flagged as a documentation-access gap.
6. International/adapted-deployment claim (Canada, Australia) — search-summary corroboration only, not independently traced to a specific named study or primary source in either session. **Reported**, not Verified.
