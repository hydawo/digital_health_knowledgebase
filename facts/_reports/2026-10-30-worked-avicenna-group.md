# Avicenna group worked, 2026-10-30

Fact keeper pass on the 2026-10-26 report (`facts/_reports/2026-10-26.md`), sections Quotes missing
and Quotes reworded, for avicenna, activinsights-geneactiv, ametris-actigraph and m-path only.

Every quote written today was copied from the live page and probes as exact with
`tools/facts/quote_probe.py`. `python3 tools/facts/validate.py`: 0 errors (the 15 overdue facts belong
to other companies). `python3 tools/facts/generate.py` run.

**Avicenna root cause.** One cause, not 17: avicennaresearch.com was redesigned by 2026-10-26. The
pages are still server-rendered (no JavaScript needed). `/legal` is now an index; the privacy policy
moved to `/legal/privacy-policy/` (updated 2026-08-22) and the terms to `/legal/terms-of-use/` (updated
2025-11-17), with the old wording intact. `/features/sensor-based-data` redirects to
`/features/sensor-data/`, and the homepage and white-label page were rewritten.

## Items

### Quotes missing (18)

| Company | Field | What I found | What I changed | Confidence |
|---|---|---|---|---|
| avicenna | program_eligibility (3 quotes) | Researcher definition now on privacy policy, age clause on terms of use; homepage hero no longer says "Patient-centric Clinical Trial", now "Design and run clinical, behavioral, and real-world studies" | URLs moved to the two new pages; homepage quote replaced; value and academic_vs_commercial note now say "clinical studies" | Corroborated (unchanged) |
| avicenna | raw_streams | Sensor page no longer says data is accessible "raw or processed ... in real-time" | Quote replaced with the new page's motion-data line; note records the removed claim | Verified (unchanged) |
| avicenna | derived_metrics | New page says "step counts and activity-related information", not "activity type" | Quote replaced; value now "step counts and other activity information". GPS mobility note left as Unclear, as set 2026-10-24 | Verified (unchanged) |
| avicenna | hosting_options (2 quotes) | White-label page reworded; "route all data ... to your own servers" gone; new line says in-house storage is the only arrangement giving researchers direct database access | Both quotes replaced; value reworded to match | Verified (unchanged) |
| avicenna | api_platform_fees, quote_required, licence | Same wording, now on terms of use | URL moved, retrieved 2026-10-30 | Verified (unchanged) |
| avicenna | retention_terms (2 quotes) | Two-year retention on terms of use; participant deletion on privacy policy | URLs moved | Verified (unchanged) |
| avicenna | dpa, hipaa_statement, iso27001 | Same wording, privacy policy | URLs moved | Corroborated (unchanged, self-claims) |
| avicenna | data_residency (3 quotes) | Same wording, privacy policy | URLs moved; "legal page" changed to "same policy" | Unclear (conflict, unchanged) |
| avicenna | baa (not flagged, same cause) | Both quotes on privacy policy | URLs moved so next week does not flag them | Unclear (unchanged) |
| activinsights-geneactiv | developer_program_status | GENEAcore 1.3.9 (2026-10-22) is now "GPL (≥ 3)", was "GPL-2 \| GPL-3" | Quote and value updated | Verified (unchanged) |

### Quotes reworded (4)

| Company | Field | What I found | What I changed | Confidence |
|---|---|---|---|---|
| avicenna | app_availability | Minimum Android is now 10.0+ (API 29+), was 9.0+ (API 28+) | Value and quote updated; profile updated | Verified (unchanged) |
| activinsights-geneactiv | program_status | Published date now 2026-10-22. CRAN archive shows 1.0.0 on 2025-04-01, so "first published April 2026" was wrong | Quote updated; archive source added; value corrected | Corroborated (unchanged) |
| ametris-actigraph | deprecations [ActiLife] | ActiLife current release now v7.3.3.0, 2026-08-03 | Value and quote updated; other two quotes re-read exact | Verified (unchanged) |
| m-path | program_status | Billing page now "Updated on October 26, 2026" | Quote updated | Verified (unchanged) |

## Left open

- Avicenna not_public facts (academic_vs_commercial, academic_pricing, minimum_commitment, hosting_price,
  ai_training_terms, soc2) still list `/legal` (now an index) as a page checked. They need a re-read of
  the two new policy pages for absence.
- Avicenna export_routes says direct database access is available "on request". The new white-label
  line limits it to in-house storage, which matches the older forum answer. Worth a look at the next re-read.
- `module-01-wearables/comparison-matrix.md` line 365 still dates the last ActiLife update to 2026-05-08.
  No cross-platform conclusion changes, so I left it alone.
