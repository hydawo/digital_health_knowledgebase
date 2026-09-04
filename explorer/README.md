# Knowledge Base Explorer

Single-page guide to the three modules with every write-up listed and searchable.

Source: `kb-explorer.html`. Published artifact: https://claude.ai/code/artifact/441c6054-9e49-4cde-ae49-5e25d8f6a9b3

When a profile is added or removed in any module, update the matching array in the page (M1, M2, M3), the counts in the header, module card, panel intro, search placeholder and footer, then republish to the same URL.

## Filters (added 2026-09-03)

Modules 1, 2 and 3 each have a filter bar. Groups combine with AND, one value per group.

- **Form factor** and **operating system** for Module 1, and **disease area** and study **operating system** for Module 3, are hand-kept in `tags.json`. Every new Module 3 profile needs a row there or the build prints a warning.
- **Data streams** are derived at build time. Module 1 reads the sensor table and tags a sensor as present when the Present column names any device or says yes. Module 2 reads the stream table and tags a stream when either the Android or the iOS column says yes; operating system comes from the same columns. Module 3 scans the wording of each profile's Instrumentation section for stream names.
- Disease areas use the fixed list in `tags.json` under `_areas` so the chips stay comparable across studies.
