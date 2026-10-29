---
status: draft
---

# Setup and calibration

The first setup of a driver from Motor GUI, over the serial adapter. The same steps with terminal commands are in
[First setup](../05-setup/index.md).

## Motor parameters

STEPFOC takes the motor's pole pairs, phase resistance and phase inductance from you, for one coil, from the
motor's datasheet. Enter them in the motor settings and apply them before calibrating; calibration fails on a value
left at 0. The current loop bandwidth is next to them (500 Hz by default).

## Calibration

Fix the motor, nothing on the shaft, 24 V on the supply. Start the calibration: the driver enters *Calibration
mode*, the motor turns in both directions, and the log shows each step as the driver reports it — magnet test,
supply test, the parameters, the open-loop spin, the angle offset, the motor constants, then `Calibration
success!`. A failed step is named in the log; [Motor parameters and calibration](../05-setup/calibration.md) says
what each message means.

After a successful calibration the GUI shows the phase order and direction the driver found, Kt, KV and the flux
linkage.

## Limits

The current limit is the first thing to set after calibration: the motor's rated phase current. The velocity limit
and the voltage limit are next to it. [Current limit and loop tuning](../05-setup/tuning.md).

## Saving

Nothing survives a power cycle until it is saved to the driver's EEPROM. The GUI marks *Unsaved changes* until you
**Save**. *Default* restores the factory values, including the serial number and the gripper flag; note what the
driver reports before you use it.

<!-- screenshots to follow -->
