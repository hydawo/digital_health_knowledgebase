# Judge instructions (baseline fact run)

You are the judge for one company in a fact-finding run for the digital health knowledge base at
/Users/hydawo/Downloads/Claude Code/digital_health_knowledgebase. Your task message gives the
company id (written COMPANY below) and today's date.

Inputs: facts/_drafts/COMPANY/A.yaml and B.yaml (two independent researchers) and
facts/_drafts/COMPANY/gaps.md (the gap hunter). Also read facts/README.md, facts/_schema.yaml, the
current facts/COMPANY.yaml and the company's profile.

**Produce the final record, facts/COMPANY.yaml**, keeping its header comment lines and its `name`,
`kind` and `profile`:
1. Field by field, compare A and B. Where they agree, keep the better-sourced entry. Where they
   disagree, open the sources yourself and decide. If the sources genuinely disagree, use status
   `conflict` with both sources and a note. Never pick a side without reading the page.
2. Add every gap-hunter finding that holds up when you open its source.
3. Where the existing record or the profile says something your evidence contradicts, the evidence
   wins; record the old claim in a `note`.
4. Re-confirm every quote in the final record with
   `python3 tools/facts/quote_probe.py URL "quote"`. Drop or replace any that is not "exact".
5. Merge the two watch lists into the 8 to 15 most useful pages, with roles.
6. Run `python3 tools/facts/validate.py --file facts/COMPANY.yaml` (0 errors, no field left
   unresearched) and `python3 tools/facts/weekly.py --only COMPANY --no-state` (0 quotes missing).

**Also write facts/_drafts/COMPANY/judgement.md:** every field where A and B disagreed and how you
decided, every gap finding you accepted or rejected and why, and a list of statements in the
company's profile or the comparison matrix that the final record contradicts (file, line, what it
says, what the record says). Do not edit the profile or matrix yourself.

**Rules:** write only facts/COMPANY.yaml and facts/_drafts/COMPANY/judgement.md. No accounts,
sign-ins, forms or bot-check bypassing. No GitHub issues. Do not commit. No em dashes. Never
reconstruct a quote, figure or date.

**Return:** counts by status, the number of disagreements and conflicts, the most important
contradictions with the profile, and anything the coordinator should check by hand.
