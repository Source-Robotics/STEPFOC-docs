---
status: draft
---

# Firmware updates

Motor GUI updates a driver through its bootloader, over the serial adapter or over CAN: it lists the firmware
releases from the firmware repository on GitHub, downloads the image and its manifest, verifies the size and the
SHA-256, resets the driver into its bootloader and streams the image.

1. Park the mechanism: the motor has no torque during the update.
2. Open *Firmware update*, choose the release (the newest is first) and start it. On a CAN bus, *Scan bootloaders*
   finds the boards and you pick the node.
3. Wait for *Flash complete*. The driver restarts with the new firmware; check the version it reports.
4. If the release notes say the update clears the calibration: parameters, calibration, limits, Save.

A cancelled or failed update is not a brick: the driver stays in its bootloader and the update can be run again.
What the bootloader is and does: [The bootloader](../07-firmware/the-bootloader.md); the other ways to update:
[Updating through the bootloader](../07-firmware/update.md).

<!-- screenshots to follow -->
