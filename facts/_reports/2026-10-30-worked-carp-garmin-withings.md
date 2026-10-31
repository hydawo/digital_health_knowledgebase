# CARP, Garmin and Withings worked, 2026-10-30

Fact keeper pass on the 2026-10-26 report (`facts/_reports/2026-10-26.md`), limited to CARP, Garmin
and Withings: their Quotes missing items and their Dead links. Every quote written today was copied
from the live page (or a Wayback capture where the live page is gone) and re-probed as exact: 85
quotes in carp.yaml and garmin.yaml, 14 in withings.yaml. `python3 tools/facts/validate.py`: 35
companies, 1340/1340 facts, 0 errors. `python3 tools/facts/generate.py` run.

All three vendors reorganised or removed documentation:

- **CARP** rebuilt docs.carp.dk (now under `/docs/`, built from `carp-dk/carp-docs-fumadocs`). Every old
  page 404s. All content was found at new URLs except the "Go live" page and carp.dk/join.
- **Garmin** relaunched the Connect Developer Program. The pause recorded since spring 2026 has ended.
  The API pages moved under `/gc-developer-program/enterprise/`, and a Personal API was added.
- **Withings** removed both public Advanced Research API pages. They now 302 to the portal home.

## Items

### Quotes missing

| Company | Field | What I found | What I changed | Confidence |
|---|---|---|---|---|
| carp | developer_program_status | docs.carp.dk home no longer has the MIT line. The rebuilt docs say it in other words | Re-cited at `docs/introduction` ("free, open-source toolkit") and `testing-and-publishing` ("the CARP packages use the MIT license"). clientId quote moved to `docs/data-storage/caws` | Verified (unchanged) |
| garmin | developer_program_status [Connect Developer Program] | "Stay tuned" is gone. The overview now offers Starter Access ("Apply ... create an app with Starter Access") and Enterprise Access. The FAQ says Starter developers "can gain immediate access". Open Wearables and the5krunner date the reopening to 21 October 2026 | **Value changed from "Paused to new applicants" to "Open again"**, with the tiers described. Pause sources moved into the note as history | **Corroborated to Verified** for open status (Garmin's own pages). The reopening date is Corroborated |
| garmin | derived_metrics | The "over 30 activity types" line is gone. The Health API metric list now marks Enhanced BBI as Enterprise only | Re-cited at `enterprise/health-api`, `enterprise/activity-api` and `enterprise/womens-health-api`. Value now says Enhanced BBI is Enterprise only | Verified (unchanged) |
| garmin | program_eligibility [Health SDKs and Connect Developer Program] | The Open Wearables wording changed. Garmin's "only for business use" FAQ line is gone | Value rewritten: business tiers serve organisations, and the Personal API covers only a person's own data. New Garmin and Open Wearables quotes | Verified (unchanged); the entity list is Reported |
| withings | program_eligibility, program_application, raw_streams [Advanced Research API] (2), sampling_rates [ScanWatch raw] (2), research_program, program_status | Not client-side rendering. Both `research-apis` and `raw-data` 302 to developer.withings.com and are out of the sitemap. openapi.yaml still lists the Rawdata v2 services and links to the removed guide | Old quotes kept and probed exact against Wayback captures (`fetch_url`: research-apis 2026-10-13, raw-data 2026-05-21), each with a note. Removed pages dropped from `watch` | Unchanged except program_status |
| withings | program_status | Removal not announced. API reference and "Trusted by 100+ research labs" still live | **Status changed from stated "Active" to unclear** | **Corroborated to Unclear** |

### Dead links

| Company | Source | What I found | What I changed | Confidence |
|---|---|---|---|---|
| carp | 8 docs.carp.dk pages | All found in the rebuilt docs: `data-storage/caws`, `mobile-sensing/measure-types`, `domain-model`, `data-managers`, `privacy-and-formats`, `sampling-configurations`, `health/collecting-data`, `apps/app-usage`, `communication/calls-and-messages` | Re-cited 13 facts' sources with fresh quotes. `watch` URLs replaced. history_depth value updated: Health first read defaults to 1 day, getHealthMeasure() sets 30 days, and the unlocked-phone rule is now iOS only. raw_streams note: Wi-Fi is now listed for iOS too, and Bluetooth is foreground-only on iOS | Verified (unchanged) |
| carp | `start/run-your-study/go-live/` | Content gone from the rebuilt docs (not in the old Starlight repo either) | program_application: "accounts by invitation" and "test server first" dropped from the value; CAWS-page quotes added (incl. `dev.carp.dk` while testing). export_routes: go-live source dropped | Verified (unchanged) |
| carp | `carp.dk/join/` | 404; TestFlight/China text found on no current CARP page | app_availability: TestFlight claim removed from value, noted as historical | Verified (unchanged) |
| garmin | `activity-api/`, `health-api/`, `program-faq/` | Moved to `/gc-developer-program/enterprise/...`. Fee lines ("no licensing or maintenance fees", "Commercial use requires a license fee payment", minimum device order) and "two business days" are gone | Re-cited 14 facts. user_cap changed from not_public to stated (Starter limited, Enterprise unlimited; 1,000 Reported). history_depth changed from unclear to stated (Starter none, Enterprise "1 month +"). api_platform_fees, minimum_commitment, quote_required, academic_vs_commercial, program_application, export_routes, rate_limits and deprecations rewritten to the relaunched pages | user_cap stays Verified. history_depth goes from Unclear to Verified. Others unchanged |

## Prose fixed

- `module-02-digital-phenotyping/profiles/carp-mobile-sensing.md`: Wi-Fi and Bluetooth rows,
  verification note, Health unlocked rule, account process, TestFlight line, Android-only list,
  references 24, 28 and 35.
- `module-01-wearables/profiles/garmin.md`: status, pricing, summary, eligibility, backfill,
  approval, fees, limitations, open questions, key links, sources 1, 3, 10 and 33. New sources 39
  and 40 added.
- Garmin lines in `module-01-wearables/comparison-matrix.md` (6), `README.md` (7) and
  `profiles/data-intermediaries.md` (4).
- `shared/unresolved-questions.md`: question 127 answered, plus status notes on questions 5, 14 and 28
  and on the gating paragraph.
- `module-01-wearables/profiles/withings.md`: research API status, how to apply, the open question,
  key links and sources 1 and 2.

## Not done, for the coordinator

- Withings lines outside its profile still say the Advanced Research API pages are live. These need
  the "unclear" status: `module-01-wearables/comparison-matrix.md`, `README.md`, and
  `shared/unresolved-questions.md` questions 10 and 43. They were outside this pass's edit scope.
- Ask Withings whether the Advanced Research API is still offered. Ask Garmin how universities are
  treated under Starter and Enterprise, and what Enterprise costs.
- The Garmin Starter request form was not opened or submitted, so approval speed after the
  reopening is unobserved.
- The Wearable Data Atlas, KB Explorer and KB Map artifacts carry the Garmin pause and need a resync.
