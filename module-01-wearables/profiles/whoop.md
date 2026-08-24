# WHOOP

## Quick Facts

| Field | Details |
|---|---|
| Organization | WHOOP, Inc. (US) |
| Category | Subscription-first screenless wearable focused on strain, recovery, and sleep |
| Current status | Active |
| Platforms/devices | WHOOP band (4.0, WHOOP 5.0/MG generation); worn on wrist or via WHOOP Body apparel; iOS and Android |
| Open source | No |
| Hosting/deployment | Vendor cloud; REST API v2 |
| Pricing model | **Subscription-only** — the hardware is bundled into a recurring membership |
| Last verified | 2026-08-21 |

## Summary

WHOOP is architecturally the most closed of the major consumer platforms. It is screenless (so it cannot display anything to a participant, which is either a reactivity advantage or a feedback limitation depending on the design), and its business model is a **subscription that includes the hardware** — you do not buy a WHOOP, you rent access to one.

For research the defining characteristic is that the **API returns only WHOOP's proprietary aggregated scores and summaries. There is no raw heart rate time series and no inter-beat-interval data through the documented endpoints.** A recovery score, an RMSSD value for the night, a strain figure, a sleep stage summary — these are the unit of analysis. A researcher who wants the underlying physiology cannot get it.

Against that, WHOOP performed best of six wrist devices in the strongest recent *independent* sleep-staging validation, which is a meaningful point in its favour and one that is often overlooked because the device is less common in academic settings than Fitbit.

## Products / Platform Architecture

- **WHOOP band** — screenless, worn continuously (24/7 is the intended use, including during sleep and exercise). Battery pack slides onto the band so the device can be charged **without removing it** — a genuinely distinctive feature that eliminates the charging gap that affects every other wrist wearable.
- **WHOOP app** (iOS/Android) — the entire user interface.
- **WHOOP Developer Platform** — REST API v2, OAuth 2.0, webhooks.
- WHOOP has a clinical research function internally (it recruits for roles such as Lead Clinical Research Scientist) and has run partnerships with clinical institutions, but a published, self-serve research programme with defined terms is **not established**.

## Sensors and Data Streams

| Sensor | Present | Researcher access to underlying signal |
|---|---|---|
| PPG (multi-wavelength) | Yes | **No raw PPG, no raw HR time series, no IBI/RR series via the API.** Only session/period aggregates. |
| Accelerometer | Yes | **Not exposed.** No raw accelerometry, no step time series in the documented API. |
| Skin temperature | Yes (4.0+) | Exposed only as `skin_temp_celsius` within the recovery score object. |
| SpO2 (pulse oximetry) | Yes (4.0+) | Exposed only as `spo2_percentage` within the recovery score object. |
| ECG | WHOOP MG generation (reported) | Not documented as available via the API. |
| GPS | **No** | n/a — no onboard GPS. |
| EDA | No | n/a |

## Derived Metrics / Analytics

WHOOP API v2 endpoints and their returned score fields:

| Endpoint | Key returned fields |
|---|---|
| `GET /v2/cycle`, `GET /v2/cycle/{cycleId}` | id, user_id, timestamps, timezone_offset, score_state; score: `strain`, `kilojoule`, `average_heart_rate`, `max_heart_rate` |
| `GET /v2/recovery`, `GET /v2/cycle/{cycleId}/recovery` | cycle_id, sleep_id, user_id, timestamps, score_state; score: `recovery_score`, `resting_heart_rate`, `hrv_rmssd_milli`, `spo2_percentage`, `skin_temp_celsius` |
| `GET /v2/activity/sleep`, `GET /v2/activity/sleep/{sleepId}` | id, cycle_id, user_id, timestamps, nap flag, score_state; score: `stage_summary`, `sleep_needed` breakdown, `respiratory_rate`, `sleep_performance_percentage`, `sleep_consistency_percentage`, `sleep_efficiency_percentage` |
| `GET /v2/activity/workout`, `GET /v2/activity/workout/{workoutId}` | id, user_id, sport, timestamps, score_state; score: `strain`, `average_heart_rate`, `max_heart_rate`, `kilojoule`, `distance_meter`, altitude metrics, `zone_durations` |
| `GET /v2/user/measurement/body` | `height_meter`, `weight_kilogram`, `max_heart_rate` |
| `GET /v2/user/profile/basic` | user_id, email, first_name, last_name |

OAuth scopes (six member-data scopes): `read:recovery`, `read:cycles`, `read:workout`, `read:sleep`, `read:profile`, `read:body_measurement`.

Two things stand out. **`hrv_rmssd_milli` is a genuinely useful, well-defined field** — a nightly RMSSD in milliseconds, measured during slow-wave sleep, which is a more methodologically defensible HRV quantity than several competitors expose. And the **"cycle"** concept is WHOOP-specific: WHOOP organises the day around sleep-to-sleep physiological cycles rather than calendar days, which is arguably better aligned to circadian reality but requires care when merging with calendar-day data from other sources.

`score_state` is important operationally — it signals whether a score is `SCORED`, `PENDING_SCORE`, or `UNSCORABLE`. Studies must handle unscorable periods explicitly rather than treating them as missing at random.

## Active Data Collection

The WHOOP app includes a Journal feature where members log daily behaviours (alcohol, caffeine, sleep environment, etc.), which WHOOP correlates against recovery. **Journal data is not listed among the v2 API endpoints retrieved**, so it appears not to be exportable — a notable loss, since it is the closest thing WHOOP has to structured self-report. Treat as unavailable unless confirmed otherwise.

No survey/EMA scheduling, no branching logic, no notifications a researcher can control.

## Researcher and Study Management Features

None documented. No study console, no participant roster, no adherence dashboard, no bulk provisioning path in the public developer platform. A study must build its own OAuth enrolment flow and monitor adherence by inspecting returned data.

**App approval is required** before an integration launches — WHOOP documents design guidelines and an app approval process. This is an additional gate and timeline item.

## Data Access and Export

- **API v2**, OAuth 2.0, REST, JSON. Webhooks supported (v1 webhooks have been removed; v2 ids differ from v1 and a mapping lookup is documented).
- **Rate limits:** default **100 requests per minute and 10,000 requests per day per client**. Response headers carry `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`. WHOOP states it can increase limits on request with justification.
  - The daily cap is the binding constraint at scale: 10,000 requests/day across all users of the application. A 500-participant study pulling several endpoints daily with pagination will approach this. **Request a limit increase before enrolling, not after.**
- **Historical depth:** not established.
- **Participant self-export:** WHOOP has offered member data downloads; not verified in this session.
- **Terms restrictions** (from the API Terms of Use, partially retrieved): the developer is responsible for all use under its credentials and **may not sell, rent, lease, redistribute, or syndicate access to the services through the APIs, nor market, sell, license, or lease data transferred or accessed through the API to any third party.** Further prohibitions cover reverse-engineering WHOOP algorithms, processing export-controlled data, altering WHOOP terms, competing with WHOOP, and disparaging WHOOP.
  - **This matters directly for open science.** A blanket prohibition on transferring API-obtained data to third parties raises real questions about depositing WHOOP-derived data in a public repository or sharing it with collaborating institutions. No explicit research carve-out was found. **This should be resolved with WHOOP in writing before a study commits**, particularly for funders with open-data mandates.
- No explicit prohibition on academic or clinical research use was found in the terms language retrieved — but neither was an explicit permission. The full terms document was not retrieved in this session.

## APIs, SDKs, and Extensibility

- REST v2 + OAuth 2.0 + webhooks. No device SDK; the band is not programmable.
- No raw-data escape hatch of any kind.

## Deployment and Infrastructure

Vendor cloud only. No self-hosting, no on-premises option.

## Participant Experience

- **Best-in-class continuous wear.** Screenless, light, and — critically — chargeable *on the wrist* via a slide-on battery pack. Alone among wrist wearables, WHOOP has no structural charging gap, which is why its 24/7 data completeness can exceed Apple Watch and Fitbit in practice.
- Can be worn as a band or in WHOOP Body apparel (bicep sleeves, etc.), useful where wrist wear is impractical.
- Screenless means **no participant-facing feedback on the device** — this reduces reactivity (the participant is not glancing at step counts and changing behaviour), which is scientifically attractive for observational designs. It also means the device cannot be used as an intervention delivery mechanism.
- Requires the app for any feedback and for syncing.
- iOS and Android.
- The subscription model means a participant who drops out or whose membership lapses takes the hardware access with them — device recovery and membership management are study logistics.

## Privacy, Security, and Compliance

Not established. HIPAA/BAA, SOC 2, ISO certification, GDPR DPA, data residency, and deletion mechanics were not verified in this session. Given the restrictive data-transfer terms noted above, the compliance and data-governance conversation with WHOOP is a prerequisite, not a formality.

## Pricing

- **Subscription includes hardware.** Reported 2026 tiers: WHOOP ONE from ~$199/year, PEAK ~$239/year, LIFE ~$359/year, depending on tier and device. Roughly $16.58–$29.92/month equivalent. *Status: Reported* — secondary sources, not verified against WHOOP's pricing page.
- **This is the most expensive per-participant recurring cost in this module** — roughly 3–5× Oura's membership and far above Garmin's zero. For a 100-person 12-month study, WHOOP membership alone is on the order of $20,000–$36,000.
- No published academic or research pricing. Whether WHOOP offers research discounts or bulk study provisioning is an open question.
- No API fee documented.

## Research Evidence and Validation

**This section was materially wrong in the first draft of this knowledge base and has been
corrected after reading Schyvens et al. 2025 in full.** See `../validation-evidence.md`.

**Schyvens et al., *SLEEP Advances* 2025**, N=62, six devices vs PSG, independently funded (VLAIO),
no author conflicts:

| Metric | Whoop 4.0 | Rank of 6 |
|---|---|---|
| **Cohen's kappa (overall agreement)** | **0.37 — "fair"** | **4th of 6** |
| Sleep/wake sensitivity | 93.58% | 5th |
| Sleep/wake specificity | 40.13% | 4th |
| Wake accuracy | 40.13% | 4th |
| Light sleep accuracy | 61.99% | 4th |
| **Deep sleep accuracy** | **69.63%** | **1st** |
| REM accuracy | 61.99% | 3rd |
| TST bias | **+24.46 min (p=0.010)** | — |
| SE bias | +4.10% (p=0.006) | — |
| WASO bias | −19.15 min (p=0.007) | — |
| SOL bias | **−10.95 min (p=0.006)** | — |

**The correct reading.** WHOOP had the best *deep-sleep classification accuracy* of the six devices
tested — and the second-worst *overall* agreement, behind Apple Watch (κ=0.53) and both Fitbits
(0.42, 0.41). Those two facts are compatible: a device that over-assigns deep sleep will catch most
true deep epochs while misclassifying a great deal else. **Quoting WHOOP's 69.6% deep-sleep number
without its κ=0.37 is misleading.**

WHOOP also significantly overestimated total sleep time (+24 min), overestimated sleep efficiency,
underestimated WASO by 19 minutes, and was one of only two devices with a significant sleep-onset
latency bias.

**No independent study has ever compared WHOOP and Oura under the same protocol.** Robbins 2024
(Oura's strongest evidence) excluded WHOOP; Schyvens 2025 excluded Oura. A bridged estimate using
Apple Watch as the shared anchor across both studies suggests Oura's four-stage agreement is
probably meaningfully better than WHOOP's — see `../validation-evidence.md` §3 — but that is a
labelled inference, not a result.

Further caveats: the tested device was **WHOOP 4.0**, not the current 5.0/MG generation. WHOOP has
an active internal research programme and publishes vendor-authored validation, which should be
weighted as **Reported**. WHOOP MG's ECG and Blood Pressure Insights carry regulatory clearances per
WHOOP's claims; the specific clearance scope was not verified. **Unclear.**

## Strengths

- **No charging gap** — the only wrist wearable here that can be charged while worn, giving the best structural 24/7 completeness.
- Best independent sleep-staging performance among wrist devices in the strongest recent comparison.
- Screenless design minimises measurement reactivity — genuinely useful for observational research.
- Well-defined nocturnal RMSSD field.
- Clean, small, easily consumed REST API with webhooks; simple to integrate.
- Alternative wear positions via WHOOP Body apparel.
- iOS and Android.

## Limitations

- **No raw data of any kind.** No HR time series, no IBI/RR, no accelerometry, no PPG. The API exposes only WHOOP's own scores and summaries. This is the most restrictive data model of any platform in this module.
- **Highest recurring per-participant cost** by a wide margin.
- **Restrictive API terms prohibiting transfer of API data to third parties**, with no located research carve-out — a potential conflict with open-data and data-sharing mandates.
- Proprietary black-box composites (Strain, Recovery) with no published algorithms and no researcher control over version changes.
- No GPS, no step time series.
- Journal (self-report) data appears not to be exportable.
- Default rate limits are low (10,000 requests/day per client) and require proactive negotiation at cohort scale.
- No study management tooling; app approval adds a gate.
- Thinner academic literature than Fitbit.
- Compliance posture unverified.

## Best-Fit Use Cases

- Studies where **continuous 24/7 wear and sleep-data completeness** are the binding constraint and the budget can absorb the subscription.
- Sleep timing/duration and sleep-continuity outcomes where the independent validation result is decisive.
- Observational designs where minimising participant reactivity to feedback is scientifically important.
- Recovery/autonomic research using nightly RMSSD, provided the vendor-derived nature of the value is acknowledged.
- Athletic, military, and occupational performance research — WHOOP's established user base.

## Poor-Fit Use Cases

- Any study needing raw or high-resolution physiological signals.
- Studies with open-data or data-deposition requirements, until the terms question is resolved.
- Large cohorts on a tight budget.
- Location, mobility, or step-based endpoints.
- Studies needing participant-facing device feedback as part of an intervention.
- Studies requiring transparent, publishable metric definitions for primary endpoints.

## Open Questions

*(Directed to WHOOP: developer support via https://developer.whoop.com/docs/developing/support/ , and WHOOP business/partnerships.)*

- **Do WHOOP's API Terms of Use permit depositing derived data in public research repositories or sharing it with collaborating institutions?** This is the single most important question for any funded academic study.
- Is there any research/academic programme, research pricing, bulk membership provisioning, or study-management offering?
- Is any raw or higher-resolution data (HR time series, IBI) obtainable under a separate research agreement, outside the public API?
- Is WHOOP Journal data exportable via API or any other route?
- What historical depth is retrievable for a newly authorised member?
- What rate-limit increases are realistically granted, and on what evidence?
- Is ECG data from the WHOOP MG generation available via API?
- HIPAA/BAA, SOC 2, ISO 27001, GDPR DPA, data residency, and participant deletion mechanics.
- Independent validation of WHOOP HRV against ECG.
- Current, vendor-confirmed membership pricing and tier definitions.

## Key Links

- Official site: https://www.whoop.com/
- Developer platform: https://developer.whoop.com/
- Developer introduction: https://developer.whoop.com/docs/introduction/
- API reference: https://developer.whoop.com/api/
- Rate limiting: https://developer.whoop.com/docs/developing/rate-limiting/
- Getting started: https://developer.whoop.com/docs/developing/getting-started/
- App approval: https://developer.whoop.com/docs/developing/app-approval/
- API Terms of Use: https://developer.whoop.com/api-terms-of-use/
- Support: https://developer.whoop.com/docs/developing/support/
- Consumer terms: https://www.whoop.com/termsofuse/

## Sources

1. WHOOP API documentation. https://developer.whoop.com/api/ (accessed 2026-08-21). **Primary.** Establishes the v2 endpoint inventory and every returned score field listed above, and that no raw HR or IBI endpoint is documented.
2. WHOOP Developer Platform introduction. https://developer.whoop.com/docs/introduction/ (accessed 2026-08-21). Establishes v2 status, v1 webhook removal, and the app-approval requirement.
3. WHOOP API rate limiting. https://developer.whoop.com/docs/developing/rate-limiting/ (accessed 2026-08-21). Establishes 100 req/min and 10,000 req/day per client, the rate-limit headers, and that increases are available on request.
4. WHOOP OAuth scopes (corroborated across developer documentation and integration guides). https://developer.whoop.com/docs/developing/getting-started/ ; https://openwearables.io/docs/providers/whoop-api-integration (accessed 2026-08-21).
5. WHOOP API Terms of Use. https://developer.whoop.com/api-terms-of-use/ (accessed 2026-08-21 — **partially retrieved via search index, not fetched in full**). Source of the prohibition on selling/renting/redistributing API access and on marketing, selling, licensing, or leasing API-accessed data to third parties. **Re-read in full before relying on this summary.**
6. Schyvens A.-M. et al. — "A performance validation of six commercial wrist-worn wearable sleep-tracking devices for sleep stage scoring compared to polysomnography." *SLEEP Advances* 2025;6(2):zpaf021. https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472 — independent, n=62; WHOOP 4.0 best of six at ~69.6%.
7. WHOOP membership pricing (secondary, unverified against vendor page): https://lifestack.ai/blog/how-much-is-whoop-membership ; https://www.droid-life.com/2026/04/22/is-a-fitbit-air-at-99-plus-a-monthly-subscription-appealing/ (accessed 2026-08-21).
