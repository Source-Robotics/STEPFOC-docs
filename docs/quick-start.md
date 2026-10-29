# Quick start

From the box to a calibrated motor that follows commands, on one page. Every step links to the chapter that
explains it; follow the link when a step is not clear or something fails.

!!! danger "Read first"
    Reversed supply polarity, a daisy-chain cable the wrong way round, or 5 V on the UART port destroys the driver.
    The motor turns during calibration. The [Safety](02-safety.md) chapter is two minutes long.

## 1. What you need

- A STEPFOC driver, a bipolar (4-wire) stepper motor with a rear shaft — NEMA 17, 1 to 5 Ω per coil, 3 A or less;
  the [tested motors](03-technical-data/tested-motors.md) are safe choices.
- The 6 × 2.5 mm **diametrically** magnetised magnet, a spacer for your motor length, four longer M3 screws.
- A 12 to 29 V supply, 24 V recommended, with a current limit if it has one.
- The 3.3 V USB-to-serial adapter and its cable; for CAN later, the CANvas adapter.
- A serial terminal on the PC: PuTTY (the CR LF build), the PlatformIO monitor, or the Arduino serial monitor.

The starter kit has all of it except the motor and the supply. Details and shop links:
[What you need](01-overview/what-you-need.md).

## 2. Fit the magnet

Press the magnet onto the rear shaft, centred, and glue it. It must end up about **1 mm** above the encoder chip
in the middle of the board, and it must not be able to turn on the shaft. A magnet that slips is the usual cause of
a calibration that "succeeds" and a motor that then runs badly. [The encoder magnet](04-mounting/magnet.md).

## 3. Mount the board

Remove the motor's four rear screws, put the spacer on, the board on the spacer with the encoder chip towards the
magnet, and the longer screws in. Check the gap: 1 mm, not touching. [Mounting on the motor](04-mounting/mounting.md).

## 4. Wire the motor

Find the two coils with a multimeter (the two wires of a coil show a few ohms; wires of different coils show
nothing). Solder one coil to **A+ and A−**, the other to **B+ and B−**. Which coil is which, and which way round,
does not matter: calibration detects it. [Wiring the stepper](04-mounting/wiring.md).

## 5. Connect power and the terminal

1. The supply to a power connector: **DC+ to positive, DC− to negative**. Check twice.
2. The serial adapter to the UART connector: TX to RX, RX to TX, 3.3 V only.
3. Power on. The LED turns on steadily: the driver is not calibrated yet, which is an error state.
4. Open the terminal on the adapter's port, 256000 baud, line ending CR+LF, and type:

```
#Info
```

The driver prints its hardware and firmware version and the state of everything. If nothing comes back:
[The serial terminal](05-setup/terminal.md).

[Power and the CAN daisy chain](04-mounting/power-and-can.md) · [Connectors and pinout](03-technical-data/connectors.md)

## 6. Enter the motor parameters

From the motor's datasheet, for **one coil**:

```
#PP 50          pole pairs: 50 for a 1.8° motor, 100 for 0.9°
#R 1.1          phase resistance in ohms
#L 0.0026       phase inductance in henries (2.6 mH = 0.0026)
```

STEPFOC does not measure these; calibration fails on a value left at 0.
[Motor parameters and calibration](05-setup/calibration.md).

## 7. Calibrate

Fix the motor to the bench, nothing on the shaft, 24 V on the supply, then:

```
#Cal
```

The LED flashes, the motor turns in both directions, and the driver prints each step: the pole pairs, the magnet,
the supply, the parameters you entered, the open-loop spin, the angle offset, the motor constants, and finally

```
Calibration success!
Save config with #Save
Going to idle!
```

A failed step names itself. `Magnet test: Failed` is the magnet; `Open loop: Failed` or `Phase order is wrong!`
means the motor did not turn or did not respond: check the four wires, the supply, and that the magnet does not
slip. The whole log and every message: [Motor parameters and calibration](05-setup/calibration.md).

## 8. Set the current limit and save

```
#Ilim 1500      the motor's rated phase current in mA
#Save
```

Without `#Save` the calibration is gone at the next power cycle. The LED now shows three short flashes and a pause:
normal operation. [Current limit and loop tuning](05-setup/tuning.md) · [Saving the configuration](05-setup/saving.md).

## 9. Move it

```
#V 16384        one revolution per second
#V 0
#P 0            back to where it started
#P 16384        one revolution forward
#Idle
```

Position is in encoder ticks, 16384 per revolution; speed in ticks per second; current in mA. If the motor hums
or whines, lower `#Ilim` or tune the loops: [Current limit and loop tuning](05-setup/tuning.md). What the modes
are: [Control modes](06-operation/modes.md).

## 10. Where to go next

| You want to | Read |
|---|---|
| control it from a program over CAN | [Over CAN](06-operation/can.md), then [With Python](06-operation/python.md) |
| put several drivers on one bus | give each a node ID (`#CANID 1`, `#Save`), terminate the ends: [Power and the CAN daisy chain](04-mounting/power-and-can.md) |
| tune it with plots in the browser | [With Motor GUI](06-operation/motor-gui.md) |
| protect the motor from overheating | [Thermistor](04-mounting/thermistor.md) |
| update the firmware | [Firmware](07-firmware/index.md) |
| look up a command | [Protocol reference](reference/index.md) |
| understand why it does not work | [Errors and recovery](06-operation/errors.md), [Troubleshooting](08-troubleshooting.md) |
