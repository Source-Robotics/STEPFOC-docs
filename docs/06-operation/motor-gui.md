# With Motor GUI

[Motor GUI](https://motorgui.com/) is Source Robotics' tool for the driver in the browser: it connects to a driver
over the serial adapter (Web Serial, so a Chromium-based browser) or to a bus of drivers over the CANvas adapter,
shows the state, plots position, speed and current, lets you set the gains and limits and save them, and updates
the firmware through the bootloader from the GitHub releases.

Use it when you want to see what the motor does while you tune it, or to flash a driver without installing
anything. Everything it does can also be done from the terminal or from Python; it reads and writes the same
settings.

## Connecting

1. Open [motorgui.com](https://motorgui.com/) in Chrome or Edge.
2. Plug in the serial adapter (for one driver) or the CANvas adapter (for a bus), power the driver.
3. Choose the connection in the GUI and pick the port the browser offers.

The driver must run firmware 104 or newer for the firmware-update function; the rest works with any release.

## Updating firmware from Motor GUI

Motor GUI reads the manifest (`firmware.json`) of the chosen release from the firmware repository's GitHub
releases, verifies the image, reboots the driver into its bootloader and streams the image. See
[Updating through the bootloader](../07-firmware/update.md) for what happens and what to do when it fails.
