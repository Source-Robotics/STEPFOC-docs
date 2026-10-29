---
status: draft
---

# Getting started

Motor GUI runs in the browser and talks to the hardware through the browser's serial port access (Web Serial),
so it needs a Chromium-based browser: Chrome, Edge, Brave or Opera. Nothing is installed.

## Two ways to connect

- **One driver over the serial adapter.** The 3.3 V USB-to-serial adapter on the driver's UART connector, 256000
  baud. This is the connection for the first setup and for calibration, which only runs over UART.
- **A bus of drivers over the CANvas adapter.** The CANvas USB-to-CAN adapter appears as a serial port and speaks
  slcan; Motor GUI talks to every node on the bus through it, each by its node ID.

## Opening the port

1. Plug in the adapter and power the driver.
2. Open [motorgui.com](https://motorgui.com/), choose the connection kind, and **Open port**. The browser asks
   which port; pick the adapter's.
3. The driver's identity appears: hardware version, firmware version, serial number, batch date, whether it is
   calibrated and activated, and the active errors.

If the port is not offered, the browser is not Chromium-based or another program holds the port (a terminal left
open). If the port opens and nothing appears: TX and RX crossed, the driver unpowered, or the wrong baud rate on
another adapter.

## What is on the screen

The state of the driver and the control mode it is in; the jog controls (position, velocity, current) and a
setpoint field; the plots of position, speed and current; the settings for the motor, the limits and the gains;
calibration; the errors with a **Clear errors** button; the firmware update; a console for typing commands by hand.
*Keyboard shortcuts* lists the keys.

<!-- screenshots to follow -->
