---
hide:
  - toc
---

# STEPFOC Manual

![STEPFOC driver](assets/STEPFOC.png){ .hero }

<!-- doc-meta: stepfoc -->

[Quick start](quick-start.md){ .md-button .md-button--primary } [About this manual](about.md){ .md-button }

Source Robotics d.o.o. publishes this document for the STEPFOC stepper driver. It is revised as the product and
its firmware change; the document number, firmware version, revision and date above identify the version you are
reading, and the document history on the About page says what changed. Take care that the firmware version named
under *Applies to* matches what `#Info` reports on your driver: the version selector in the header switches
between firmware releases. The text and the images are licensed CC BY-SA 4.0, the code examples MIT.

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } **Quick start**

    ---

    [One page](quick-start.md) from the box to a calibrated motor that follows commands, with a link into the
    manual at every step.

-   :material-book-open-variant:{ .lg .middle } **The manual**

    ---

    [Safety](02-safety.md), [Technical data](03-technical-data/index.md), [Mounting and wiring](04-mounting/index.md),
    [First setup](05-setup/index.md), [Operation](06-operation/index.md), [Firmware](07-firmware/index.md),
    [Troubleshooting](08-troubleshooting.md).

-   :material-code-braces:{ .lg .middle } **Protocol reference**

    ---

    Every [CAN message](reference/can/index.md) and [UART command](reference/uart/index.md), the
    [defaults](reference/defaults.md), the [errors](reference/errors.md) and the [Python library](reference/python.md),
    read from the firmware.

-   :material-school:{ .lg .middle } **Learn**

    ---

    [Guides](guides/index.md) with code, the [bootloader](07-firmware/the-bootloader.md), and the
    [theory corner](appendix/theory.md) on FOC, the cascade and impedance control.

</div>
