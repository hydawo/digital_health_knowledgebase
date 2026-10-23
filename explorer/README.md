# Knowledge Base Explorer

The published pages that explain the knowledge base. All five modules appear in each.

| Page | Source | Published |
|---|---|---|
| Explorer: every write-up and paper, searchable, one tab per module | `kb-explorer.html` | https://claude.ai/artifact/9QpKQHQXsMtNFoaxiXacbk |
| Map: the system at a glance, the weekly robot, open questions, status | `kb-map.html` | https://claude.ai/artifact/9rScizou73axRp1eoyX13P |
| Architecture: how the agents work and how the repo is laid out | `kb-architecture.html` | https://claude.ai/artifact/AA8avrDsQmZYzwEQn4by1b |

The Wearable Data Atlas (Module 1 only) lives in `module-01-wearables/wearable-data-atlas.html`.

When a profile is added or removed in any module, update the matching array in the page (M1, M2, M3), the counts in the header, module card, panel intro, search placeholder and footer, then republish to the same URL.

Module 5 (added 2026-10-22) has one tab listing the stored PDFs of every domain. `build.py` reads each domain folder named in its `for dom in [...]` loop; the page script loops over the same list. A new domain needs adding in both places, plus a paragraph in the Module 5 panel and the paper count on its card. The hub pages themselves are built by `tools/domains/build_hubs.py`, not by this script. The map and architecture pages carry hand-written Module 5 counts; update them when a domain is added or seeded.

## Filters (added 2026-09-03)

Modules 1, 2 and 3 each have a filter bar. Groups combine with AND, one value per group.

- **Form factor** and **operating system** for Module 1, and **disease area** and study **operating system** for Module 3, are hand-kept in `tags.json`. Every new Module 3 profile needs a row there or the build prints a warning.
- **Data streams** are derived at build time. Module 1 reads the sensor table and tags a sensor as present when the Present column names any device or says yes. Module 2 reads the stream table and tags a stream when either the Android or the iOS column says yes; operating system comes from the same columns. Module 3 scans the wording of each profile's Instrumentation section for stream names.
- Disease areas use the fixed list in `tags.json` under `_areas` so the chips stay comparable across studies.
