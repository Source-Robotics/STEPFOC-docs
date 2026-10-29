---
status: draft
---

# Several motors

Over the CANvas adapter, Motor GUI sees every driver on the bus and addresses each by its node ID. Before you put
drivers on one bus, give each its own ID over the serial adapter (the CAN ID in the settings, then Save), and
terminate the first and the last node. [Power and the CAN daisy chain](../04-mounting/power-and-can.md).

The watchdog (*Watchdog ms*) makes a driver stop by itself when the GUI stops talking to it; set it on a bus that
drives something that must not run away.

<!-- screenshots to follow -->
