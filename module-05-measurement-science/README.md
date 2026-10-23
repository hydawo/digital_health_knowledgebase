# Module 5: Measurement Science by Domain

**Status:** created 2026-10-22. Two domains: [Sleep](sleep/) and [Cardiac](cardiac/). Sleep was seeded the same day with 58 papers (17 PDFs on disk, 5 free to read but not redistributable, 28 free but needing a hand download, 8 paywalled) and a hub linking 49 tagged papers and profiles in Modules 1 to 4. Cardiac was seeded the same day with 68 papers (18 PDFs on disk, 23 free to read but not redistributable, 17 needing a hand download, 10 paywalled) and a hub linking 62 tagged papers and profiles. Physical activity and fitness, and
possibly mental health, follow one at a time.

## What this module is

Modules 1 and 2 describe technologies, Module 3 describes deployments and Module 4 holds methods and
reviews about digital health research in general. This module holds the science of measuring one
physiological domain with wearables and phones, regardless of device:

- consensus statements, position papers and guidelines for that domain;
- standard metrics and how they are defined (for sleep: total sleep time, sleep efficiency, wake
  after sleep onset, regularity indices);
- validation methods and performance-evaluation frameworks specific to the domain;
- algorithms that are not tied to one vendor (for sleep: Cole-Kripke, Sadeh, GGIR's sleep detection);
- reviews and meta-analyses that pool many devices, and papers on the physiological limits of what a
  sensor can infer (for sleep: staging from wrist PPG and motion versus PSG).

## Scope boundaries

| Paper type | Goes to |
|---|---|
| One device validated against a reference | Module 1, next to the device |
| One platform's own analytics | Module 2, next to the platform |
| A deployment reporting how it went | Module 3 |
| Research practice in general, not one domain (adherence, missing data, ethics) | Module 4 |
| Measurement science for one domain, across devices | **This module** |

A paper can still be relevant to a domain without living here. Those are found through the domain
hub page instead of being copied (see below).

## Layout

| Path | What it holds |
|---|---|
| `literature-library-index.json` | One dedup ledger for the whole module, ids prefixed `doi:`, `pmid:` or `arxiv:` |
| `<domain>/literature-library.md` | The domain catalogue, one row per paper |
| `<domain>/literature/` | Open-access PDFs |
| `<domain>/_hand-download.md` | Free papers the publishers block to scripts, to fetch by hand |
| `<domain>/_seed/` | Search logs and agent output from the seeding pass, kept for provenance |
| `<domain>/hub.md` | Generated page listing every paper and profile in Modules 1 to 5 tagged with the domain |
| `../shared/domain-tags.json` | Domain tags for papers and profiles in Modules 1 to 4, keyed by DOI or profile path |

## Why one module and not one per domain

Most sleep papers are also device or deployment papers, so separate modules would give them two
homes. One module with a section per domain, plus tags on the papers that already live elsewhere,
keeps one home per paper. Decision recorded in `ROADMAP.md`, item 6.

## Domains

| Domain | Status | Catalogue |
|---|---|---|
| Sleep | Seeded 2026-10-22: 58 papers in 7 sections; [hub](sleep/hub.md) | [`sleep/literature-library.md`](sleep/literature-library.md) |
| Cardiac | Seeded 2026-10-22: 68 papers in 7 sections; [hub](cardiac/hub.md) | [`cardiac/literature-library.md`](cardiac/literature-library.md) |
| Physical activity and fitness | Not started | |
| Mental health | Not decided | |
