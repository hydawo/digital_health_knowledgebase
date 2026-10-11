# MetricWire: judgement (baseline fact run)

Judge run, 2026-10-11. Inputs: `A.yaml`, `B.yaml`, `gaps.md`. Output: `facts/metricwire.yaml`.

Final record: 38 entries (34 fields; `program_eligibility` and `academic_pricing` split by scope, `app_availability`
split three ways). Status: 21 stated, 11 not_public, 4 unclear, 2 not_applicable. Every quote re-probed "exact" on
2026-10-11. `validate.py --file`: 0 errors, 0 unresearched. `weekly.py --only metricwire --no-state`: 29 pages, 0
quotes missing, 0 dead links.

## The SwaggerHub API (coordinator point 1)

Verified directly. `https://api.swaggerhub.com/apis/MetricWire/ConsumerAPI` lists six versions (1.0.0, 1.0.0-oas3,
2.0.0, 3.0.0, 4.0.0, 4.0.0-oas3), every one `X-Private: false` and owned by MetricWire. All are also
`X-Published: false`, which in SwaggerHub means "not marked as a published release". It does not mean hidden; the
definitions download without sign-in. Default 3.0.0 (created 2023-06-29, modified 2025-05-21). Host
`consumer-api.metricwire.com`, OAuth2 `application` (client credentials) flow, token URL `/oauth/token`. 4.0.0 drops
eight operations against 3.0.0 (bulk trigger and intervention creation, cognitive-task triggers, `SyncStudy`) and adds
none; the gap hunter said seven. Fetch URL used throughout: `https://api.swaggerhub.com/apis/MetricWire/ConsumerAPI/3.0.0`.
The spec documents no rate limit and no sampling rate. Sensor and cognitive-task operation IDs end in "Enterprise".

Decisions:
- `export_routes`: stated, Corroborated (not Verified, because which licence tiers get API credentials is not
  published). Portal exports plus the Consumer API.
- `raw_streams`: stated, Corroborated, now built on the API's enumerated stream types (31 phone, 19 Fitbit, Polar
  endpoints) plus the privacy policy and app store sources. Per-OS availability and raw-versus-summary still undocumented.
- `sampling_rates`: kept not_public; the spec is added to the checked sources.
- `developer_program_status`: unclear. There is no developer programme to apply to; the API is a customer feature with
  undocumented tier access. Both researchers had not_public on the strength of `api.metricwire.com` returning `{}`, which
  is the wrong host.
- `rate_limits`, `history_depth`, `api_platform_fees`: not_public, with the spec added as a checked source.

## Fields where A and B disagreed

| Field | A | B | Decision and reason |
|---|---|---|---|
| research_program | stated, Verified | stated, Corroborated | Verified. The vendor's own page establishing its own programme is the authoritative source; no self-claim cap applies to this field. |
| program_application | unclear | not_public | not_public, Corroborated. No process is published (site licence page and contact page read); the legacy Play listing's "send us an e-mail" quote kept as context. |
| developer_program_status | not_public | not_public | Both agreed but both were overturned by the SwaggerHub spec; now unclear (see above). |
| academic_vs_commercial | Corroborated | Reported | Reported. No price comparison exists to corroborate a difference. |
| academic_pricing | Corroborated, merged | Reported, merged | Split by scope: Academic Site Licence (Corroborated, vendor page) and Penn State SRC (Reported, secondary). |
| derived_metrics | stated, Reported | not_public | stated, Reported. HealthKit metrics on the App Store listing, plus Fitbit and Polar summary types and "mobility" stream names in the API. Derivation of the mobility types undocumented. |
| ai_training_terms | unclear | not_public | unclear. A secondary source (Onix) says participant data feed a Gemini scheduling agent; policy silent on AI. See point 4. |
| deprecations | not_public, Reported | unclear | not_public, Corroborated. Nothing is announced; the stagnant legacy app, 404 knowledge base, archived m2c2kit guide and API 4.0.0 removals go in the note. |
| app_availability | split by scope, Verified | single entry, Verified | Split into three scopes (Catalyst, legacy app, study-branded apps). See point 2. |
| data_residency | Verified | Corroborated | Verified. Not a self-claim-capped field, and the vendor's own security summary is the primary source for where it stores data. |
| retention_terms | Verified | Corroborated | Verified, same reasoning (the vendor's own legal terms). Added the archival-copy exception. |
| fda_clearances | Verified, api.fda.gov as url | Corroborated, accessdata url + fetch_url | Verified, using B's README-compliant form (accessdata.fda.gov url, openFDA fetch_url) with `expect_absent`, matching the Polar record. |
| gdpr_statement | PIPEDA quote | site-licence quote | Both kept. |

No field ended as `conflict`: no two sources contradicted each other once read.

## Coordinator points 2 to 7

2. **App change.** Confirmed via the iTunes lookup: Catalyst 6.9.0 released 2026-10-07T21:19:54Z, minimum iOS 15.0;
   legacy MetricWire 4.9.9 released 2022-04-06, minimum iOS 12.0. Play: Catalyst updated Oct 7, 2026; legacy updated
   Jul 30, 2024. Study-branded apps recorded as a third scope from the App Store "More by MetricWire Inc." list
   (ARTEMIS, Rhythms In Daily Life, SOAR, MAP ARC, PLAD TRACE, TRACC MH, TREAT), Corroborated.
3. **Compliance.** HIPAA, GDPR, ISO 27001 and SOC 2 all Corroborated (vendor statements only; no certificate, registry
   or confirmation). "The only EMA platform that complies" quoted and flagged as marketing. `dpa` unclear: the DPA
   sentence concerns MetricWire's own service providers. `baa` not_public.
4. **AI training.** Onix case study recorded as secondary in `ai_training_terms`, labelled "at most Reported" in the
   note. Quotes used: the BigQuery "participant data, survey responses..." sentence and the Vertex AI/Gemini sentence.
   The participant policy's "no commercial interest" sentence kept verbatim.
5. **Penn State SRC.** Recorded as scoped entries in `program_eligibility` and `academic_pricing` (secondary,
   Reported), and pointed to from `research_program`'s note. Scoped explicitly as a third-party sub-licence.
6. **Play data safety.** Exact: "App interactions App functionality, Analytics, Advertising or marketing,
   Personalization" under "Data shared". Recorded as a source and note in `retention_terms`, the nearest data-use
   field in the schema.
7. **Retention.** Recorded as stated, Verified, with the archival-copy exception and the note that deletion depends on
   the research team.

## Gap-hunter findings

| Finding | Accepted? | Where |
|---|---|---|
| A1 SwaggerHub Consumer API | Accepted, verified from the registry JSON | export_routes, raw_streams, developer_program_status, rate_limits |
| A2 zeolite built on official spec | Accepted ("API documentation is available on Swaggerhub" exact) | export_routes, developer_program_status |
| A3 HealthKit, Fitbit, Polar, Health Connect | Accepted | raw_streams, derived_metrics |
| A4 31 sensor types | Accepted; "default is 100000" used in rate_limits as page size, not a limit | raw_streams, derived_metrics |
| B1 Penn State SRC | Accepted, scoped as secondary | program_eligibility, academic_pricing |
| C1 retention and archival copy | Accepted | retention_terms |
| C2 DPA with providers, HIPAA servers | Accepted | dpa, data_residency, retention_terms |
| C3 Play data safety | Accepted (exact) | retention_terms |
| C4 background ambient noise | Accepted | raw_streams |
| C5 cognitive tasks, interventions | Accepted only through the API endpoints; homepage quotes not needed | export_routes |
| C6 m2c2kit guide archived | Accepted | deprecations |
| C7 Atlassian knowledge base gone | Accepted (expect_absent source) | deprecations, export_routes note |
| C8 Europe PMC 351 / ClinicalTrials.gov 12 | Rejected for the record (no schema field; counts are not quotes). Worth adding to the profile's evidence section | none |
| C9 Ontario law, non-refundable fees | Accepted as note only | minimum_commitment |
| Sensors as add-on in v4.0 (search snippet) | Rejected: not quotable, page 404 | none |
| apis.io "no public spec" | Rejected: contradicted by A1 | none |

## Profile and matrix statements the record contradicts

| File | Line | Says | Record says |
|---|---|---|---|
| module-02-digital-phenotyping/profiles/metricwire.md | 22 | Participant app is the "MetricWire app (iOS/Android)" | Current app is Catalyst By MetricWire; the generic app is stale (iOS 2022-04-06). Line 10 already has this right. |
| same | 33-51 | Every stream except GPS "Unclear" | The API enumerates accelerometer, gyroscope, magnetometer, light, battery, Bluetooth, screen events, calls, messages, app usage, noise (level only), device information and more, with separate iOS types. Per-OS columns still cannot be filled from it. |
| same | 61 | Derived metrics "Not verified in any pass to date" | Fitbit, Polar and HealthKit summaries plus API "mobility" stream types. |
| same | 73 | "Export formats and API mechanics are not described on the public pages" | API mechanics are documented on SwaggerHub (JSON, OAuth2 client credentials). Portal export formats still undocumented. |
| same | 77 | "No official, MetricWire-published API documentation was located"; zeolite reflects a reverse-engineered or "private/partner-only" API | Official spec published on SwaggerHub by MetricWire; zeolite links to it. |
| same | 122, 134, 144 | API "not publicly documented for general researcher self-service"; poor fit for teams needing "a documented public API"; open question on an official channel | Documented; open question narrows to which licence tiers get credentials. |
| same | 145 | Data retention open | Research team deletes at study end; MetricWire keeps no copies beyond a possible legal archival copy. |
| same | 160-161 (sources 3, 4) | m2c2kit guide cited as live; zeolite as evidence of no official docs | Guide archived 2026-08-12; zeolite links the official docs. |
| same | 101, Pricing | No mention of Penn State SRC | Penn State SRC enterprise sub-licence, reduced cost, free for pilot and thesis work (secondary). |
| same | 93-97 | Compliance section omits the DPA scope | DPA statement covers MetricWire's service providers only. |
| module-02-digital-phenotyping/comparison-matrix.md | 116 | Sensors: "'Passive Sensors' named without a list; the rest Unclear"; wearables: "Not established" | API stream list; Fitbit, Polar, HealthKit and Health Connect integrations documented. |
| same | 135 | Academic access: Academic Site Licence only | Add Penn State SRC route (secondary). |
| shared/unresolved-questions.md | 294 (#90) | "MetricWire's API still Unclear" | Answered: a documented Consumer API exists; tier access remains open. |

Not a contradiction, but missing from the profile: the Play data-safety "Advertising or marketing" sharing declaration,
and the Onix case study on a Gemini scheduling agent using participant data.
