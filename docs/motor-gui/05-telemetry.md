---
status: draft
---

# Telemetry and recordings

Motor GUI reads position, speed and current from the driver continuously (the driver's cyclic output over serial,
or the motion replies over CAN) and plots them. The plots pan and zoom; hovering shows the value.

A **recording** keeps the stream to a file for a test: *New recording*, run the move, *Stop recording*. Use it to
compare two sets of gains, to document a motor, or to attach to a bug report.

<!-- screenshots to follow -->
