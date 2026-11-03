# Versions and compatibility

Which firmware release works with which bootloader, Python library, PAR6 runtime and board revision. One row per firmware release, newest first.

| Firmware | Released | Bootloader | Spectral Micro equivalent | Python library (Spectral-BLDC) | PAR6 runtime | STEPFOC PCB | Docs |
|---|---|---|---|---|---|---|---|
| 108 | 2026-08-26 | required (installed on boards shipped with 105 or newer) | 107 | 1.20 or newer | 0.9 or newer | v1 | 108 |
| 107 | 2026-08-24 | required | 107, without its calibration fix (which came with STEPFOC 108) | 1.20 or newer | 0.9 or newer | v1 | not published |
| 106 | 2026-07-05 | required | 106 | 1.19 or newer | 0.9 or newer | v1 | not published |
| 105 | 2026-07-04 | required (the first release that needs it) | 105 | 1.19 or newer | 0.9 or newer | v1 | not published |
| 103 | 2025-12-28 | none (flashed with a programming adapter) | 101 | 1.17 or newer | 0.9 or newer | v1 | 103 |

`#Info` prints the firmware release a driver runs; `Send_Respond_Device_Info` returns it over CAN.
