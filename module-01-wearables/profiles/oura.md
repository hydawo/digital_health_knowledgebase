# Oura

## Quick Facts

| Field | Details |
|---|---|
| Organization | Oura Health Oy (Ōura), Finland |
| Category | Consumer smart ring; sleep, recovery, and temperature focus |
| Current status | Active |
| Platforms/devices | Oura Ring (Gen3, Oura Ring 4 and later); iOS and Android app |
| Open source | No |
| Hosting/deployment | Vendor cloud (Oura Cloud), REST API v2 |
| Pricing model | Ring purchase + **mandatory membership subscription for API data access on Gen3 and later** |
| Last verified | 2026-08-21 |

## Summary

Oura is the strongest consumer device for **sleep and nocturnal physiology**. Its form factor — a ring — puts the PPG sensor on the finger, where perfusion is better and motion artefact during sleep is lower than at the wrist, and it removes the screen-and-notifications distraction that makes wrist wearables uncomfortable to sleep in. In head-to-head PSG validation it has repeatedly been the best-performing consumer sleep-staging device.

For research there are two decisive practical facts:

1. **The API is clean and comprehensive** — a well-structured REST v2 with roughly 19 documented data routes, OAuth 2.0, generous rate limits (5,000 requests per 5 minutes), and date-ranged list endpoints.
2. **Data access is gated behind an active paid membership.** Oura's own support documentation states that Gen3-and-later users without an active Oura Membership cannot access their data through the Oura API, and neither can partner applications integrated with it. For a study, that means the subscription is not optional — it is a per-participant, per-month line item for the entire study duration, on top of the ring.

That second fact is the single most important cost driver and is easy to miss when scoping a study.

## Products / Platform Architecture

- **Oura Ring** — titanium ring, worn on a finger (Oura recommends index finger; sizing kit required before ordering, which adds lead time to participant onboarding).
- **Oura app** (iOS/Android) — sync and participant-facing insights.
- **Oura Cloud / API v2** — REST, OAuth 2.0.
- **Oura for Business / Oura for Organizations** — enterprise offering aimed at employers, healthcare, academic and clinical research, and military. Oura reports 200+ customers across those segments including US Air Force, US Navy, US Army, NASA, and universities. The specifics of what a research customer receives beyond the consumer API (bulk provisioning? cohort-level export? a study console?) are **not established** from public pages and are an open question.

## Sensors and Data Streams

| Sensor | Present | Researcher access to underlying signal |
|---|---|---|
| PPG (multi-wavelength: green/red/IR on Gen3+) | Yes | **No raw PPG.** Derived HR at ~5-minute resolution while stationary, continuous during sleep. |
| Accelerometer | Yes | **No raw accelerometry.** Derived activity/MET/steps only. |
| Gyroscope | Not documented as user-accessible | n/a |
| Temperature (NTC skin temperature sensors) | Yes | Derived nightly temperature *deviation* from personal baseline, not absolute raw trace. This is Oura's most distinctive research signal. |
| SpO2 | Gen3+ | Nightly average SpO2 and breathing regularity. |
| GPS | **No** | n/a — the ring has no GPS, no altimeter, no barometer. |
| EDA | No | n/a |

Note the deliberate design trade: the ring omits GPS, screen, and altimeter to achieve size and battery life. It is a physiology device, not a mobility device.

## Derived Metrics / Analytics

Oura API v2 routes (19 documented, grouped):

**Personal & configuration** — Personal Info (age, weight, height, biological sex, email); Ring Configuration (colour, design, firmware, hardware type, setup date); Ring Battery Level.

**Daily summaries** — Daily Sleep (score + contributors: deep sleep, efficiency, latency, REM, restfulness, timing); Daily Activity (score, calories, MET minutes, steps, activity distribution); Daily Readiness (score + contributors: HRV balance, body temperature, sleep balance); Daily Resilience (sleep recovery, daytime recovery, stress indicators); Daily SpO2; Daily Stress (stress/recovery time with day summary).

**Health metrics** — Heart Rate (timestamped BPM with source labelling); VO2 Max; Cardiovascular Age (vascular age, pulse wave velocity).

**Sleep & sessions** — Sleep Periods (detailed stage data — deep/light/REM — with heart rate and HRV variation traces); Sleep Time (optimal bedtime recommendation, efficiency status); Sessions (guided breathing/meditation with biometrics); Rest Mode Period.

**Activity & tags** — Workouts (activity type, calories, distance, intensity, timestamps); Enhanced Tags; Tags.

The **Sleep Periods** route is the research workhorse: it returns per-night stage hypnograms alongside within-night heart rate and HRV time series, which is unusually rich for a consumer API.

Oura's HRV is RMSSD-based and measured continuously through the night — a substantively different (and for most research purposes better) quantity than Apple's opportunistic SDNN. Cross-platform HRV comparisons must account for this.

## Active Data Collection

Minimal. Tags and Enhanced Tags let participants annotate timestamped events with free text/comments, which can serve as a lightweight event-marking mechanism (e.g. medication taken, symptom onset) but is not a survey/EMA system. No scheduled prompts, no branching logic.

## Researcher and Study Management Features

No first-party research console is documented in the public API. Oura for Business exists and explicitly names academic and clinical research as a customer segment, but its research-specific functionality is unverified.

In practice, academic Oura studies typically either (a) enrol participants through a custom OAuth app and pull per-participant data, or (b) use middleware. Provisioning is meaningfully harder than for wrist wearables because of **ring sizing** — each participant needs a sizing kit and a correct size before the actual device ships, adding weeks to onboarding and creating a real risk of mis-sized rings mid-study (finger size changes with temperature, hydration, pregnancy, and weight change).

## Data Access and Export

- **API v2**: OAuth 2.0. **Personal Access Tokens were deprecated for new integrations in December 2025** — new integrations must use OAuth 2.0 only. (*Status: Reported* — from secondary sources; confirm against Oura's developer portal, as this materially changes the effort of a small study that previously could have used per-participant PATs.)
- **Rate limits**: 5,000 requests per 5-minute period, enforced at two layers — per access token, and per application in aggregate across all its end-user tokens. The aggregate application-level cap is the one that constrains large cohorts; model it before scaling.
- **List endpoints** accept `start_date` / `end_date`; single documents fetchable by id. Historical depth available via API is not explicitly established.
- **Participant self-export**: all Oura users — including those without an active membership — can download data files through the Membership Hub, which Oura describes as GDPR-compliant. This is a useful fallback for participants whose membership lapses, and for studies that want a participant-mediated export path.
- **Membership gate**: Gen3 and later users without an active Oura Membership cannot access data through the API, and neither can partner apps for those users.
- **App version dependency**: users must have updated to a recent version of the Oura app for new data types to appear via API v2 — meaning participant app-update behaviour can silently break a data stream.

## APIs, SDKs, and Extensibility

- REST v2, OAuth 2.0, JSON. Documentation at `cloud.ouraring.com/v2/docs` and `api.ouraring.com/v2/docs` (both JavaScript-rendered; an OpenAPI document is referenced by community clients).
- Mature community client libraries exist in Python, Dart/Flutter, Deno/TypeScript, and others.
- No SDK for on-device code; the ring is not programmable.
- Webhooks: Oura has offered webhook subscriptions; not verified in this session.

## Deployment and Infrastructure

Vendor cloud only. No self-hosting. Research team needs an OAuth app registration and its own storage.

## Participant Experience

- **Highest sleep-wear acceptability** of any device in this module. A ring is comfortable to sleep in, silent, screen-free, and socially unobtrusive.
- Battery roughly 4–7 days depending on generation and use; charging takes ~20–80 minutes on a small dock. Low burden, but the dock is a losable item in remote studies.
- **Sizing is the operational weak point.** Sizing kits, lead times, and finger-size drift over a long study are real sources of attrition and data loss.
- Not suitable for participants who cannot wear rings for occupational or safety reasons (healthcare workers with hand-hygiene protocols, machine operators, some athletes).
- Data syncs via the phone app; sync lapses cause gaps.
- iOS and Android.

## Privacy, Security, and Compliance

- Oura provides a GDPR-oriented user data download through the Membership Hub.
- HIPAA posture, BAA availability, SOC 2 / ISO certifications, DPA terms, and data residency were **not verified** in this session. Oura's enterprise/government customer list (US military branches, NASA) implies some security maturity, but **do not infer compliance from a customer list** — obtain it in writing.

## Pricing

- **Ring:** retail purchase, priced in the several-hundred-dollar range depending on model and finish. Verify current pricing at ouraring.com.
- **Membership:** reported at **$5.99/month or $69.99/year**. *Status: Reported* — from secondary sources, not verified against Oura's pricing page.
- **Total cost of ownership is the key number for research.** For a 100-participant, 12-month study, membership alone is roughly $7,000 on top of ring hardware — and it is **mandatory**, because without it the API returns nothing for Gen3+ users. Compare this to Garmin, where core metrics carry no subscription at all.
- Whether Oura for Business offers research/academic pricing, bulk membership, or waived membership for study rings is **not established** and is the highest-value question to put to Oura.

## Research Evidence and Validation

Full extraction in `../validation-evidence.md`.

### Robbins et al. 2024, *Sensors* 24(20):6532 — Oura's strongest evidence, with a caveat

N=35 healthy adults (ages 20–50), single night, concurrent PSG at Brigham and Women's Hospital,
Oura Ring **Gen3** on the non-dominant index finger.

| Measure | Oura Gen3 | Apple Watch S8 | Fitbit Sense 2 |
|---|---|---|---|
| **Four-stage Cohen's kappa** | **0.65** | 0.60 | 0.55 |
| Sleep–wake kappa | 0.60 | 0.60 | 0.52 |
| Deep sleep sensitivity | **79.5%** | 50.5% | 61.7% |
| REM sensitivity | 76.0% | 82.6% | 67.3% |
| Light sleep sensitivity | 78.2% | 86.1% | 78.0% |
| TST bias | +9 min (ns) | — | — |
| SE / WASO vs PSG | **no significant difference** | WASO −10 min (p=0.02) | — |
| Device failures | **0 / 35** | 6 / 35 | 2 / 35 |

Oura was the only device of the three with **no data loss**, and the only one whose sleep efficiency
and WASO did not differ significantly from PSG. Both are genuinely strong results.

> ### ⚠️ Declared interest
> **The study was funded by Oura Ring Inc. The lead author serves on Oura's Medical Advisory Board
> and receives consulting fees from Oura.** **Verified** from the paper's own disclosures.
>
> The protocol is sound and the paper is peer-reviewed, so this is **Corroborated with a declared
> interest** — not independent evidence. Never cite the κ=0.65 figure without this attached.

### The ICC problem — applies to Oura as much as anyone

The same paper reports intraclass correlation coefficients, which are widely ignored in favour of
the kappa headline:

| Measure | Oura ICC | Interpretation |
|---|---|---|
| Total Sleep Time | 0.74 | Good |
| Sleep Efficiency | 0.74 | Good |
| Light Sleep | 0.40 | Fair |
| **Deep Sleep** | **0.32** | **Poor** |
| **REM Sleep** | **0.27** | **Poor** |

Even the best-performing consumer sleep tracker has *poor* between-person reliability for deep sleep
and REM stage summaries. **A study using nightly deep-sleep or REM minutes from Oura as an outcome is
substantially measuring device noise.** TST and SE are the defensible stage-derived endpoints.

### What is missing

- **Oura has never been tested against WHOOP under the same protocol.** Robbins excluded WHOOP;
  Schyvens et al. 2025 (six devices, independently funded) excluded Oura. A bridged estimate through
  Apple Watch suggests Oura is meaningfully ahead of WHOOP on overall agreement — see
  `../validation-evidence.md` §3 — but that is inference, not evidence.
- The tested hardware was **Gen3**. Ring 4 and Ring 5 are untested in independent PSG work.
- Temperature-based illness-onset detection (UCSF/TemPredict and related COVID-era work) remains
  Oura's strongest non-sleep literature. **Reported** — not re-verified this session.
- Health Radar, Blood Pressure Signals, and GLP-1 insights have **no located independent validation.**
- Finger skin temperature is peripheral, not core; interpret accordingly.

## Strengths

- Best-validated consumer sleep staging, and by a clear margin the most comfortable device to actually sleep in — which means better nocturnal data completeness in practice, not just better algorithms.
- Continuous nocturnal RMSSD HRV and nightly temperature deviation — two research-grade-adjacent signals that most wrist competitors handle worse or not at all.
- Clean, well-documented REST API with rich per-night detail (stage hypnograms plus within-night HR/HRV traces).
- Generous rate limits.
- iOS and Android.
- Participant self-export available even without membership, as a GDPR-backed fallback.
- Strong enterprise/government adoption suggests procurement paths exist for larger studies.

## Limitations

- **Mandatory paid membership for API access** on Gen3+ — a recurring per-participant cost with no documented academic waiver.
- **No raw PPG, no raw accelerometry.** Everything is vendor-processed.
- **No GPS, altimeter, or barometer** — the ring cannot support mobility or location research at all.
- Ring sizing adds weeks to onboarding and creates mid-study fit failures.
- Not wearable by some occupational populations.
- Personal Access Token deprecation (reported) raises the engineering floor for small studies.
- Application-level aggregate rate limiting constrains very large cohorts.
- Participant app-version dependence can silently break data types.
- Step counting is weaker than wrist devices.
- Compliance posture unverified.
- Vendor algorithm updates change metric definitions over time without researcher control — a known problem for Oura's readiness/score family specifically, which has been revised across generations.

## Best-Fit Use Cases

- Sleep research where staging quality and nocturnal wear compliance matter most (short of PSG).
- Circadian, menstrual cycle, ovulation, and fertility research using nightly temperature deviation.
- Illness-onset / infection-detection studies (temperature + HR + HRV + respiratory rate).
- Recovery, stress, and autonomic research needing continuous nocturnal RMSSD.
- Studies where an unobtrusive, screen-free device improves adherence or reduces reactivity (the device shows nothing on the wrist, so it is less likely to change behaviour).

## Poor-Fit Use Cases

- Any location, GPS, or mobility research.
- Step count or physical activity as a primary endpoint.
- Studies with no budget line for per-participant subscriptions.
- Raw signal research.
- Populations that cannot wear rings, or where finger size is unstable (pregnancy studies need particular care here).
- Rapid-deployment studies — sizing logistics prevent fast enrolment.

## Open Questions

*(Directed to Oura: https://ouraring.com/business , developer portal support.)*

- Does Oura for Business offer academic/research pricing, bulk or waived memberships for study-provisioned rings, or a research-specific data path?
- Is there a cohort-level/bulk export or a study-management console for research customers, distinct from per-user OAuth?
- Confirm the December 2025 Personal Access Token deprecation and what it means for existing small-scale research integrations.
- Historical data depth retrievable via API for a newly authorised participant.
- Webhook availability and reliability.
- HIPAA/BAA, SOC 2, ISO 27001, GDPR DPA, and data residency (Oura is EU-headquartered, which may be advantageous for EU studies — but confirm where data actually resides).
- What happens to a participant's already-collected data if their membership lapses mid-study — is it retrievable later, or permanently inaccessible via API?
- Current ring and membership pricing, verified against the vendor's own page.

## Key Links

- Official site: https://ouraring.com/
- Oura for Business / Organizations: https://ouraring.com/business
- API documentation (v2): https://cloud.ouraring.com/v2/docs and https://api.ouraring.com/v2/docs
- Developer portal: https://cloud.ouraring.com/
- API error handling / rate limits: https://cloud.ouraring.com/docs/error-handling
- Oura support — The Oura API: https://support.ouraring.com/hc/en-us/articles/4415266939155-The-Oura-API
- Community Python client (useful endpoint reference): https://github.com/hedgertronic/oura-ring

## Sources

1. Oura Member Care — "The Oura API." https://support.ouraring.com/hc/en-us/articles/4415266939155-The-Oura-API (accessed 2026-08-21). **Primary.** Establishes the membership requirement for Gen3+ API access (for both users and partner apps), the Membership Hub GDPR download available to all users, and the app-version dependency for new data types.
2. Oura API v2 documentation. https://cloud.ouraring.com/v2/docs (accessed 2026-08-21 — JavaScript-rendered, content not directly extractable in this session).
3. hedgertronic/oura-ring client README. https://github.com/hedgertronic/oura-ring (accessed 2026-08-21). Used as the endpoint inventory: 19 routes and their returned fields.
4. Oura API rate limiting and authentication (secondary, corroborated across sources): https://cloud.ouraring.com/docs/error-handling ; https://www.aifitnessapi.com/integrate/oura-api (accessed 2026-08-21). Establishes 5,000 requests / 5 minutes, two-layer limiting, OAuth 2.0, and the reported December 2025 PAT deprecation.
5. Oura for Organizations. https://ouraring.com/business (accessed 2026-08-21). Establishes the enterprise segment and named customer categories.
6. Oura blog — 2024 validation study announcement. https://ouraring.com/blog/2024-sensors-oura-ring-validation-study/ (accessed 2026-08-21). Vendor framing of the *Sensors* study; note funding.
7. *Sensors* 2024;24(20):6532 — "Accuracy of Three Commercial Wearable Devices for Sleep Tracking in Healthy Adults." https://www.mdpi.com/1424-8220/24/20/6532
8. Schyvens A.-M. et al. *SLEEP Advances* 2025;6(2):zpaf021. https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472 — noted as **not** including Oura.
9. Oura membership pricing (secondary, unverified against vendor page): https://www.bettervitals.com/learn/oura-ring-subscription-worth-it-2026 (accessed 2026-08-21).
