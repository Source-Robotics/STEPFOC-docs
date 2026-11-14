# Versions and compatibility

Which firmware release works with which bootloader, Python library, Motor GUI, PAR6 runtime and board revision. One row per firmware release, newest first.

<div class="ref-table compat" markdown>

| Firmware | Released | Bootloader | Spectral Micro equivalent | Python library (Spectral-BLDC) | Motor GUI | PAR6 runtime | STEPFOC PCB | Docs |
|---|---|---|---|---|---|---|---|---|
| 110 | 2026-11-13 | required | 110 | 1.22 or newer (names for parameters 90 to 93; 1.21 reads them by their numbers) | 0.7.0 or newer (STOP sends #Estop over UART, presets write parameters 90 to 92 over CAN) | 0.9 or newer (it sends watchdog action 0, the legacy response) | v1 | 110 |
| 109 | 2026-11-10 | required | 109 (from 109 the two share their version numbers; there is no Spectral Micro 108) | 1.21 or newer (the calls for the commands added in 109: parameters, identity, telemetry, buffers, the watchdog's coast and descend) | 0.5.0 or newer | 0.9 or newer (it sends watchdog action 0, the legacy response) | v1 | 109 |
| 108 | 2026-08-26 | required (installed on boards shipped with 105 or newer, and on some shipped before) | 107 | 1.20 or newer |  | 0.9 or newer | v1 | 108 |
| 107 | 2026-08-24 | required | 107, without its calibration fix (which came with STEPFOC 108) | 1.20 or newer |  | 0.9 or newer | v1 | not published |
| 106 | 2026-07-05 | required | 106 | 1.19 or newer |  | 0.9 or newer | v1 | not published |
| 105 | 2026-07-04 | required (the first release that needs it) | 105 | 1.19 or newer |  | 0.9 or newer | v1 | not published |
| 103 | 2025-12-28 | none (flashed with a programming adapter) | 101 | 1.17 or newer |  | 0.9 or newer | v1 | 103 |

</div>

`#Info` prints the firmware release a driver runs; `Send_Respond_Device_Info` returns it over CAN.
