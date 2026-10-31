# Group D worked, 2026-10-31

Fact keeper pass for Avicenna, mindLAMP, RADAR-base, LifeData, AWARE, Beiwe, CARP and m-Path. It covers
the 47 facts from these companies that fall due by 2026-11-10 and that the automatic extension could not
confirm (not_public, unclear, conflict, not_applicable, or a moved quote), plus this group's items in
`facts/_reports/2026-10-31.md`. Those items were one Quotes missing (carp derived_metrics) and one Check by
hand (the LifeData help centre). None of these companies had Quotes reworded or Dead links. Every source
cited by a re-checked fact was read live today, through `tools/facts/common.py` fetch, raw GitHub files or
the GitHub API. Every quote kept or written was probed with `quote_probe.py` and came back exact.
`python3 tools/facts/validate.py`: 35 companies, 1340/1340 facts, 0 errors. `generate.py` was not run, as
instructed.

Nothing material changed. No fact in this group changed status or confidence. One quote was replaced
(carp-dsp), and several notes now record what the 2026-10-31 read found.

- **Avicenna:** the six not_public facts that cited the `/legal` index now cite the actual documents,
  `/legal/terms-of-use/` and `/legal/privacy-policy/`. Neither document publishes academic pricing,
  minimum terms, hosting prices or AI-training terms. `/pricing` still returns 404.
- **RADAR-base:** PR #92 (Google Health push ingest) has **not** merged or been released. Detail below.
- **Fixed in passing:** the RADAR-base `deprecations [Fitbit route]` fact had two `sources:` keys. YAML
  kept only the second one, so the REST-Connector v0.7.6 source was silently dropped from the record. The
  two lists are now merged. A scan of all 35 records found no other duplicate keys.

## Items

### Quotes missing

| Company | Field | What I found | What I changed | Confidence |
|---|---|---|---|---|
| carp | derived_metrics | The carp-dsp description and README were rewritten (pushed 2026-10-30). The "Kotlin Multiplatform framework" line is gone. The repo now describes a workflow framework for reproducible pipelines, MIT licence | Quote replaced with the README's "CARP-DSP is a workflow framework for mobile and wearable sensing analytics, built on the CARP study platform." The carp-dsp clause in the value now reads: a workflow framework (MIT) that checks a workflow against the protocol's data before it runs. The other four quotes re-probed exact. Note added | Verified (unchanged) |

### Check by hand

| Company | Source | What I found | What I changed | Confidence |
|---|---|---|---|---|
| lifedata | help.lifedatacorp.com/hc/en-us (developer_program_status) | Still 403 to scripts, and support.lifedatacorp.com is 403 too. The other three sources (features, products, terms) were re-read and still show no API, SDK or developer program. api.lifedatacorp.com still returns 404 at its root. A GitHub account named LifeDataLLC (created 2025-06-23) holds one "Jira-Reports" repository and has no link to lifedatacorp.com, so I could not tie it to the company | Re-read sources got today's retrieved date. The note now records the account and that the help centre was still 403. **recheck_by left at 2026-11-10** | Corroborated (unchanged) |

### Due re-checks (status cannot be auto-confirmed)

recheck_by is now 2026-11-30 (the 30-day interval) on every row except LifeData developer_program_status.

| Company | Facts | What I found | What I changed |
|---|---|---|---|
| avicenna | academic_vs_commercial, academic_pricing, minimum_commitment, hosting_price, rate_limits, ai_training_terms (not_public); device_price, subscription_price (not_applicable) | `/legal` is only an index with links to terms-of-use, privacy-policy and cookies-policy. The terms have a fees section with per-study billing, and the privacy policy defines researchers as academically affiliated, but neither publishes prices, a minimum or AI terms. The FAQ still offers only Trial versus Licensed. The Raw Data page still gives export size limits (about 5 GB per export) and no request rate limit. Forum t/1295 still describes the AI survey chatbot as an early feature. The rebuilt white-label page no longer has the "the project budget" line, and it has no price wording | The `/legal` sources were replaced by the specific documents: terms-of-use for academic_pricing, minimum_commitment and hosting_price, and both documents for academic_vs_commercial and ai_training_terms. The hosting_price note now records that the "project budget" line is gone |
| mindlamp | user_cap, academic_vs_commercial, academic_pricing, minimum_commitment, hosting_price [BIDMC Core], ai_training_terms (not_public); retention_terms, licence (conflict) | Pricing is still "tailored proposal" only: the get-started FAQ says pricing depends on participants, sites, duration and custom work. The BIDMC services page still requires a business agreement after Phase 1. PR 939 (the deletion-claims fix) is still open and unmerged, and its draft-branch quotes are still exact. Issue 943 (licence) still has 0 comments. The GitHub API still reports no licence for LAMP-server, -core-ios, -core-android, -activities or -worker. All privacy-page quotes are exact, and so is the Play label "Data can't be deleted" | Dates only. The licence value now records the 2026-10-31 API check and that issue 943 still has no reply |
| radar-base | academic_pricing, minimum_commitment [The Hyve], hosting_price, rate_limits, ai_training_terms (not_public); device_price, subscription_price (not_applicable) | The Hyve pages still give no price, term or academic rate. "Subscription model" and "initial service period" are both still there. The REST-Connector README still sets `fitbit.user.poll.interval` to 150 s. The demo privacy policy still says "Anonymised data may be preserved indefinitely" | Dates only |
| radar-base | deprecations [Fitbit route], due 2026-11-15 but re-checked because of the PR #92 question | GitHub API: **PR #92 is open and not merged** (updated 2026-10-20, base `dev`). The newest PushEndpoint release is still v0.4.0 (2025-06-19). Eight follow-on Google Health PRs (#95, #99 to #102, #106, #107, #109) are chained onto the PR #92 branch, all open, the latest updated 2026-10-30. REST-Connector PRs #199, #201, #202 and #215 merged on 2026-10-19 to 23 and shipped in v0.7.6. Google still sets the turn-off for 2026-11-02, while dev.fitbit.com still says 2026-10-30. All 8 quotes are exact | The duplicate `sources:` key was merged (the v0.7.6 source is back in the record). The value now says PR #92 was still unmerged on 2026-10-31 and that eight follow-on PRs are open. A note line records the API check. recheck_by is 2026-11-30 |
| lifedata | device_price (not_applicable); subscription_price, hosting_price, rate_limits (not_public); deprecations (conflict) | No /pricing page (404). Products still says pricing is "not feature or project-based". The terms still have only the "abusive or excessive usage" clause. All four deprecation quotes are exact. iTunes lookup still gives releaseDate 2025-05-28 (now version 1.0.18, updated 2026-10-17) against the website's "Released in 2026" | Dates only |
| aware | user_cap, academic_pricing, minimum_commitment, hosting_price, ai_training_terms (not_public) | The support page still offers paid support and University of Melbourne hosting with no price ("Contact Dr Simon D'Alfonso"). Open Collective still has $5 and $100 tiers and nothing on study pricing. The privacy page and use-aware have no AI terms. The micro-server quote is exact | Dates only |
| beiwe | user_cap, minimum_commitment, rate_limits, ai_training_terms (not_public); app_availability [Google Play] (unclear) | Neither BSC page publishes a cap, a minimum or AI terms. use-beiwe still carries the FY26 pricing ($2,640 a month plus $8.40 per APM, smallest example $8,760). The wiki pages and gunicorn_conf.py still show no rate limit (Tableau 60 s timeout only). The Play listing still returns 404 (expect_absent confirmed). build.gradle still sets targetSdk 33 and version 3.6.0, and the only commit since 2024-06 is a Gradle update on 2026-02-10. The other three quotes are exact | Dates only. The app_availability note now records today's re-check |
| carp | minimum_commitment, ai_training_terms (not_public); retention_terms (conflict) | Hosting still requires an active research partnership, and invoicing still "typically takes place once per year". The privacy policies still allow use "to improve our Applications and Services" and say nothing on AI. All six retention quotes are exact, including both Play data-safety lines and the CAWS `EXPORTS_RETENTION_DAYS:7` default | Dates only |
| m-path | device_price (not_applicable); rate_limits (not_public); ai_training_terms (unclear) | Pricing and billing still list the API as a EUR 5,000 add-on with no documentation or limits (billing page updated 2026-10-26). The sitemap lists no API page. All four terms and DPA quotes are exact, and the terms, DPA and privacy pages have no AI or training clause | Dates only |

## Prose fixed

- `module-02-digital-phenotyping/profiles/carp-mobile-sensing.md`: the server-side derived-metrics bullet
  (carp-dsp described as a workflow framework, MIT) and reference 30 (carp-dsp re-read 2026-10-31). The
  generated facts block (line 250) is not hand-edited. It picks up the new value when `generate.py` runs.
- `module-02-digital-phenotyping/profiles/radar-base.md`: the Fitbit route bullet (Verified 2026-10-31,
  PR #92 still unmerged, eight follow-on PRs open, no new PushEndpoint release) and reference 19 (re-check
  date added).

## Shared-file edits needed

- `explorer/kb-explorer.html` (`PROFILES` array): it embeds the old RADAR-base Fitbit bullet ("The push
  ingest, RADAR-PushEndpoint PR #92, is still open (last updated 2026-10-20), and the README...") and the old
  CARP carp-dsp line ("the `carp-dsp` repository provides a data-science pipeline framework [30]"). Fix:
  rebuild with `explorer/build.py` after `generate.py`. No hand edit is needed.
- `ROADMAP.md` line 56: "One more look after 2 November (410 responses, RADAR-base PR #92)." This is still
  accurate. Optional replacement: "One more look after 2 November (410 responses, RADAR-base PR #92, still
  unmerged on 2026-10-31 with eight follow-on PRs open)."
- No comparison matrix, README, sources.md or unresolved-questions line contradicts today's findings.
  Every status is unchanged, and the open "when will PR #92 ship" question in the RADAR-base profile and
  explorer is still open.

## Needs a browser or vendor

- **Browser:** help.lifedatacorp.com/hc/en-us and support.lifedatacorp.com (both 403 behind a bot check).
  Look for any API, SDK or developer documentation in the LifeData help centre. LifeData
  developer_program_status was left at recheck_by 2026-11-10 for this.
- **Vendor questions, unchanged from earlier passes:**
  - mindLAMP: written licence terms for the five repositories, and which deletion behaviour applies on
    BIDMC servers.
  - m-Path: how terms clause 11.7 and the DPA apply to participant data.
  - LifeData: which generation (Original or LifeData+) a new study uses.
  - Avicenna: academic versus commercial terms, and on-premises pricing.
  - RADAR-base: when PR #92 will ship.
- **For the coordinator:**
  - Avicenna `soc2` (not in this pass, due 2027-01-09) and the `watch` list still cite the `/legal`
    index. The index is a fine page to watch, but the soc2 source could move to `/legal/privacy-policy/`
    at its next re-check.
  - `tools/facts/validate.py` does not catch duplicate YAML keys, which is how the RADAR-base source went
    missing. A duplicate-key check in the loader would stop it happening again.
