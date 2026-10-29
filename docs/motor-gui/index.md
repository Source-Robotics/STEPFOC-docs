---
hide:
  - toc
---

# Motor GUI Guide

![Motor GUI](../assets/placeholder-hero.png){ .hero }

<!-- doc-meta: motor-gui -->

[Motor GUI](https://motorgui.com/) is Source Robotics' tool for the STEPFOC and Spectral Micro drivers, in the
browser: it connects to a driver over the serial adapter or to a bus of drivers over the CANvas adapter, shows the
state, moves the motor, runs the calibration, tunes the loops with live plots, records telemetry and updates the
firmware. Everything it does, the driver also does from a terminal or from Python; the GUI reads and writes the
same settings.

!!! note "This guide is being written"
    Motor GUI is in development. The chapters below say what each part does today; screenshots and the details
    follow as the tool is finished. For the first setup, the [Quick start](../quick-start.md) already goes through
    Motor GUI step by step.

<div class="grid cards" markdown>

-   :material-connection:{ .lg .middle } **[Getting started](01-getting-started.md)**

    ---

    The browser, the serial or CAN adapter, opening the port.

-   :material-tune:{ .lg .middle } **[Setup and calibration](03-setup-and-calibration.md)**

    ---

    Motor parameters, the calibration run and its log, limits, saving.

-   :material-chart-line:{ .lg .middle } **[Tuning](04-tuning.md)** and **[Telemetry](05-telemetry.md)**

    ---

    Gains and presets with the response on the plots; the telemetry stream and recordings.

-   :material-update:{ .lg .middle } **[Firmware updates](06-firmware-updates.md)**

    ---

    Flash a release from GitHub through the bootloader.

</div>
