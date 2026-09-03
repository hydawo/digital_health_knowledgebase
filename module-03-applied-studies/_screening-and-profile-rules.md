# Module 3 screening and profile-writing rules

Durable copy of the rules used by the 2026-09-03 coverage pass, so that any session or agent screens papers and writes profiles the same way. Part A is the screening rubric, Part B the writing rules. Both defer to `CLAUDE.md` where they overlap.

---

## Part A: screening rubric


Repo: this repository.
Module 3 dir: module-03-applied-studies/ (read its README.md "Scope rules" section and CLAUDE.md's "Module 3" section first).
Existing Module 3 profiles: module-03-applied-studies/profiles/*.md (55). Ledger: module-03-applied-studies/literature-index.json.
READ THE WHOLE TEXT FILE. Never screen from the abstract alone.

## Scope (from CLAUDE.md, Module 3)
INCLUDE only if ALL of:
 a) a real research deployment with a cohort (not a review, meta-analysis, perspective, protocol-without-results, or methods/statistics paper whose cohort is only an illustration);
 b) the data-collection instrument is a device/platform already profiled in Module 1 (module-01-wearables/profiles: apple-watch-healthkit, oura, whoop, fitbit-google, garmin, samsung, polar, withings, empatica, ametris-actigraph, axivity-geneactiv, movesense) or Module 2 (module-02-digital-phenotyping/profiles: beiwe, radar-base, mindlamp, aware-framework, avicenna-research-ethica, metricwire, m-path, carp-mobile-sensing, lifedata) — verify from the METHODS which was actually deployed, not the filename/folder;
 c) it reports enough about HOW THE DEPLOYMENT WENT — recruitment funnel, retention/attrition, adherence/wear time, data completeness/missingness, technical failure modes — to be useful to a future study team. A paper whose only deployment content is "N enrolled, N analysed" with no completeness/adherence/technical content does NOT qualify.
REJECT with exactly one reason code: review | protocol | validation (device-accuracy vs reference — Module 1's territory) | architecture (platform/methods/statistics paper with no deployment cohort of its own) | no-cohort (perspective, or cohort too thin to report deployment reality) | duplicate-cohort (same deployment as an existing Module 3 profile AND adds no new deployment/operational figures — check the existing profile before using this; if it adds genuinely new operational numbers, INCLUDE and note the overlap) | unobtainable.
Borderline: mark "BORDERLINE-include" or "BORDERLINE-reject" and say why in two sentences.

## For EVERY paper report
- file; first author (from the PDF byline, not metadata); year; journal; DOI; PMCID (if printed in the PDF, else "not in PDF")
- Platform/device ACTUALLY deployed per Methods (quote the sentence). Say explicitly if this differs from what the folder/filename suggests.
- Verdict + reason code
- If an existing Module 3 profile covers the same cohort, name it.

## For every INCLUDE (or BORDERLINE-include) additionally extract, with page/section reference for each number, verbatim where possible
- design; funding/COI; population/setting/country; enrolled -> analysed with each attrition step; duration; deployment model (BYOD vs provisioned); any custom integration
- recruitment method; retention definition and rate; attrition reasons
- data completeness/missingness with the exact definition used; wear-time definition; any OS (iOS/Android) breakdown
- documented technical failure modes (device, sync, battery, app, connectivity, server, vendor policy)
- the authors' own feasibility conclusions and recommendations
- anything that is NOT reported that a study designer would want (so the profile can say "not reported")
Do not infer or estimate any figure. If a number is not in the text, say "not reported".

Write the screening report as a dated file under `module-03-applied-studies/_screening-reports/` so the extraction survives the session.

---

## Part B: profile-writing rules


Repo: this repository.
Template: the "Profile template (Module 3-specific)" in CLAUDE.md, Module 3 section. Use exactly those section headings, plus a "## Related profiles" section before "## Sources" as the existing profiles do.
Exemplars (match their shape, register and density):
  module-03-applied-studies/profiles/oura-tempredict-healthcare-worker-adherence.md
  module-03-applied-studies/profiles/apple-heart-movement-study-retention.md

Hard writing rules (workspace convention, no exceptions):
1. No em dashes or en dashes anywhere, including the H1 title. Use " - " (a plain hyphen with spaces) between the author-year and the description in the H1, e.g. "# Vidal Bustamante et al. 2022 - GENEActiv ...". Elsewhere use a period or comma.
2. Almost no colons. Never use a colon to introduce an explanation. Colons in table cells, URLs, ratios and citations are fine.
3. One assertion per sentence. Do not chain a fact, a qualifier and a consequence with "and", commas or "which". Split into short sentences.
4. Use bold sparingly (a handful of times per profile at most). Do not bold whole sentences. Do not use bolded-lead bullet lists.
5. No rule-of-three stacking, no "it's not X, it's Y", no signposting, no closing summary sentence. End sections on a concrete detail.
6. Curly quotes are fine only inside verbatim quotations copied from the paper. Use straight quotes otherwise.

Evidence rules (from CLAUDE.md):
7. Every number must come from the full text you read. If a figure is not in the paper, write "not reported". Never estimate, infer or back-calculate a figure and present it as the paper's.
8. Assign the evidence-confidence scale (Verified / Corroborated / Reported / Unclear) to the feasibility claims specifically, in the "## Evidence Confidence" section, and say what was read from where and on what date (2026-09-03).
9. State the platform or device actually deployed per the Methods. If the search or filename suggested something else, say so.
10. Verify the first author from the PDF byline. Give the full citation with DOI and PMCID in Quick Facts.
11. Cross-link to Module 1/2 profiles with relative links of the form ../../module-01-wearables/profiles/<file>.md or ../../module-02-digital-phenotyping/profiles/<file>.md, and to sibling Module 3 profiles as <file>.md. Only link to files that exist (check with ls). Do not duplicate Module 1/2 content.
12. Note any conflict of interest, and whether the compensation model and support model are reported.
13. Where the paper reports a Beiwe deployment, note that the collection window predates Beiwe's 2024 heartbeat feature if it does, as the other Beiwe profiles do.
14. Local PDF line in Key Links: reference the existing path under module-01-wearables/literature/ or module-02-digital-phenotyping/literature/ rather than copying the file.

After writing, run this check from the profiles directory and fix anything it prints:
  grep -nE '—|–' <file>; grep -oE '\]\(([^)#h][^)]*)\)' <file> | sed 's/](\(.*\))/\1/' | sort -u | while read l; do [ -e "$l" ] || echo "BROKEN: $l"; done
