---
status: draft
---

# Troubleshooting

| Symptom | Check |
|---|---|
| the browser offers no port | a Chromium-based browser (Chrome, Edge, Brave, Opera); Firefox and Safari have no Web Serial |
| the port is listed but will not open | another program holds it: a terminal, PlatformIO's monitor, the Arduino serial monitor |
| the port opens, nothing appears | the driver's power; TX and RX crossed on a non-Source adapter; the baud rate on a non-Source adapter (256000) |
| *No connection* on CAN | the CANvas adapter's port; the bus termination; the node ID of the driver; 1 Mbit/s |
| the calibration does not start | calibration runs over the serial connection only, not over CAN |
| *Unsaved changes* after a power cycle | the settings were not saved to the driver; Save writes them |
| the firmware update finds no bootloader | a driver with firmware 103 has no bootloader: [Installing the bootloader on an older board](../07-firmware/bootloader.md) |

The driver's own errors and what clears them: [Errors and recovery](../06-operation/errors.md).
