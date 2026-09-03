# Profile table conventions

Fixed table layouts that every profile in a module uses, so readers can compare platforms and devices
row by row instead of reading a different shape on every page. Added 2026-09-03 after the Module 2
profiles were found to present the same section as prose on one page and a table on the next.

## Module 2, "Sensors and Data Streams"

One table, one row per passive stream in the order `CLAUDE.md` lists them, columns in this order.

| Column | Allowed values |
|---|---|
| Stream | GPS / location; Accelerometer; Gyroscope; Magnetometer; Barometer; Ambient light; Proximity; Device motion / activity recognition; Screen state; App usage; Battery / charging; Network / connectivity; Wi-Fi; Bluetooth; Calls (metadata); SMS (metadata); Keyboard; Audio / microphone; Notifications; Device information |
| Android, iOS | Yes; No; No (OS), meaning the operating system exposes nothing to third-party apps; Unclear; Conflicting documentation |
| Raw or derived | Raw, Derived, Event, Metadata, with the fields named where known; Not applicable |
| Sampling configurable | Yes with what is configurable; No; Unclear; Not applicable |
| Notes | Short, factual, sourced |

Rows are never dropped. A stream the platform does not have reads "No" with "Not a <platform> stream"
in the notes. A stream nobody verified reads "Unclear". A "Verification" paragraph under the table
names the source, the date and the confidence level, and any prose from earlier passes is kept under
"Notes from earlier verification passes" so provenance survives.

## Module 1, "Sensors and Data Streams"

Target layout, to be applied in a later pass. One table, columns: Sensor | Present | Researcher access
to underlying signal | Resolution or sampling | Notes. Sensor rows follow the `CLAUDE.md` list (PPG,
ECG, accelerometer, gyroscope, temperature, SpO2, GPS, barometer, EDA, other). As of 2026-09-03 the
profiles use five different layouts; Apple Watch, Fitbit, Oura and WHOOP already use a three-column
form of this table.
