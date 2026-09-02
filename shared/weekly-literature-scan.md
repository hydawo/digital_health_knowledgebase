# Weekly Literature Scan — routine specification

**Last updated: 2026-09-02.** Canonical, version-controlled copy of what the automated weekly
literature-scan routine does and how it is configured.

## Why this file exists

The routine is a **claude.ai/code Routine** — a cloud scheduled agent — **not** a locally-scheduled
task. Its prompt therefore lives only in the claude.ai Routines UI and is **invisible to anyone
working in this repository**, including future Claude sessions. That has already caused confusion
once (the 2026-08-31 session found the routine failing but could not inspect what it was supposed to
do).

**This file is the canonical copy. If the routine's prompt is edited in the UI, update this file in
the same change.** Nothing here executes; it is documentation plus a paste-ready prompt.

---

## Current configuration

| Setting | Value |
|---|---|
| Type | claude.ai/code Routine (cloud), fires weekly on **Monday** |
| Operating mode | **Fully unattended** — the prompt instructs "Do not ask for confirmation at any step" |
| Repo access | **Push access to this repo's GitHub remote (public)** |
| Environment | "Default", `env_01Yak4krG93fzRmR7cJXa2JY` |
| Network access | **Custom** allowlist — `eutils.ncbi.nlm.nih.gov`, `export.arxiv.org`, plus the default package-manager list |
| Connectors | Official Anthropic-hosted PubMed MCP (`https://pubmed.mcp.claude.com/mcp`) as a secondary PubMed path |
| Coverage before 2026-09-02 | Module 1 (wearables) and Module 2 (digital phenotyping platforms) |
| Coverage from 2026-09-02 | **+ Module 3 (applied studies)** — see below |

**Do not re-add the PubCrawl connector** without confirming who operates the specific hosted
instance. See `research-log.md` (2026-09-01) for the full reasoning — the short version is that an
unattended, no-confirmation, push-access routine has little margin for prompt injection arriving
through an MCP tool result from an unverified operator.

---

## Dedup ledgers

Each module keeps a JSON ledger so the routine never re-surfaces the same paper.

| Module | Ledger | Key fields |
|---|---|---|
| 1 | `module-01-wearables/research-library-index.json` | `pmids_seen`, `dois_seen`, `records`, `runs`, `last_run_date` |
| 2 | `module-02-digital-phenotyping/literature-library-index.json` | `ids_seen`, `records`, `runs`, `last_run_date` |
| **3** | **`module-03-applied-studies/literature-index.json`** | `dois_seen`, `pmcids_seen`, `records`, **`rejected`**, `runs`, `last_run_date` |

Module 3's ledger adds a **`rejected`** array. Module 3 rejects far more of what it screens than the
other two (reviews, protocol papers, validation studies, unobtainable full text, duplicate cohorts),
and without recording rejections with a reason the routine would re-litigate the same papers every
week. It was seeded on 2026-09-02 with all **55 already-profiled studies** (55 DOIs, 54 PMCIDs).

---

## Module 3 section — paste-ready prompt

Add this to the routine's existing prompt. **It is deliberately different in kind from the Module 1
and 2 sections: it does not write profiles.**

> ### Module 3 — Applied Wearables and Digital Phenotyping Studies
>
> **Your job for this module is triage, not authorship. Do not create or edit any file in
> `module-03-applied-studies/profiles/`.** Append candidates to a queue for a human-initiated session
> to build. Rationale: Module 3 profiles require full-text reading, and abstract-level screening has
> a measured platform-misattribution rate of roughly 3 in 12 in this project. An unattended run must
> not write unverified study claims into a public repository.
>
> **1. Load the ledger** `module-03-applied-studies/literature-index.json`. Skip anything whose DOI
> is in `dois_seen`, whose PMCID is in `pmcids_seen`, or that appears in `rejected`.
>
> **2. Search.** Use NCBI E-utilities (and the arXiv API for CS/engineering venues). Query each
> Module 1 device and Module 2 platform — the authoritative list is the `## What's covered` section
> of `module-03-applied-studies/README.md` — ANDed with this deployment-reality block:
>
> `(feasibility OR adherence OR retention OR compliance OR "wear time" OR deployment OR attrition OR
> "data completeness" OR "missing data" OR acceptability OR usability OR engagement OR longitudinal)`
>
> Use a trailing window from `last_run_date` (or 10 days if null). **Sort by date, not citation
> count** — a citation-sorted pass missed 62 of 64 recent candidates when this was tested.
>
> **3. Screen.** Keep a candidate only if it has: a digital-health context term; **at least two**
> distinct deployment-reality signals (retention / adherence / feasibility / completeness / technical
> failure); and an actual cohort. **Reject** reviews, meta-analyses, protocol papers with no results,
> pure device-validation studies, and platform-architecture papers — all are explicitly out of Module
> 3 scope per `CLAUDE.md`.
>
> **Known false-positive traps:** "Polar" (polar bears/regions), "Avicenna" (the historical
> physician), "AWARE" and "CARP" (ordinary words — and **Europe PMC does not honour phrase quoting**
> for these), "m-Path", "Oura", "Samsung". Require a co-occurring digital-health term.
>
> **4. Append**, do not overwrite. Add each surviving candidate to
> `module-03-applied-studies/_scan-queue.md` with: date found, DOI, PMCID, title, venue, year, which
> Module 1/2 technology it appears to use, which deployment signals it hit, OA status, and this
> line verbatim: `Platform attribution is Reported — verify from full text before profiling.`
>
> **5. Record rejections** in the ledger's `rejected` array with a one-word reason (`review`,
> `protocol`, `validation`, `architecture`, `no-cohort`), so they are not re-screened next week.
>
> **6. Update the ledger**: set `last_run_date`, append a `runs` entry with counts (searched /
> screened-in / queued / rejected).
>
> **7. Commit** with a message beginning `Module 3 weekly scan:`. **Never modify**
> `feasibility-matrix.md`, `README.md`, `sources.md`, or any profile — a human pass owns those.

---

## Design decisions worth preserving

1. **The routine triages Module 3; it does not write it.** Modules 1 and 2 catalogue *papers about a
   technology*, which is safely automatable from abstracts. Module 3 asserts *what happened in a
   deployment*, which is not — every figure in its 55 profiles came from full text, and the two
   discovery passes that screened on abstracts alone produced three wrong platform attributions.
2. **Date-sorted, never citation-sorted.** Established empirically: the original citation-sorted pass
   missed 62 of 64 recent candidates.
3. **Rejections are recorded, not just exclusions.** Otherwise the same out-of-scope paper is
   re-examined every Monday forever.
4. **The queue is a file in the repo, not a message.** It survives between runs, is reviewable in a
   diff, and gives a human-initiated session a clear starting point.

## Known limitations

- **Three structural discovery blind spots** apply to this routine exactly as they do to manual
  passes — ordinary-word platform names, framework-shaped platforms (CARP), and venue-shaped
  invisibility (AWARE's operational literature is in CSCW/IMWUT/UbiComp, which NCBI does not index).
  A periodic **OpenAlex citation-graph pass** is the known workaround and is **not** part of this
  routine; run it manually. See `module-03-applied-studies/_citation-graph-scan-2026-09.md`.
- The routine cannot obtain paywalled or ACM-DL full text, so some genuine candidates will be queued
  and then prove unbuildable.
