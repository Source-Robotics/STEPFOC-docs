# Troubleshooting

By symptom. The error flags and what clears them are in [Errors and recovery](06-operation/errors.md).

## The driver does not answer

| Symptom | Check |
|---|---|
| No LED | the supply, DC+ and DC−, the power cable's orientation. If the cable was the wrong way round the driver is destroyed |
| LED on, nothing on the terminal | 256000 baud; TX to RX and RX to TX; the adapter's port; 3.3 V adapter; the line ending CR+LF |
| LED on, nothing on CAN | the node ID; 1 Mbit/s on the adapter; termination (about 60 Ω across CAN H and CAN L with everything unpowered); the CAN cable's orientation |
| `Unknown command` | the name's spelling and case: `#Kpiq`, not `#kpiq` |
| the LED is off and nothing works after a firmware update | the bootloader has no valid firmware: flash again, see [Updating through the bootloader](07-firmware/update.md) |

## Calibration

The messages and their causes are in [Motor parameters and calibration](05-setup/calibration.md). The ones that
come back most:

| Symptom | Cause |
|---|---|
| `Magnet test: Failed` | magnet too far, axially magnetised, or missing |
| the motor wobbles left and right during calibration | one coil is not connected |
| `Open loop: Failed` | the motor did not turn: a coil open, the open-loop voltage (`#Openv`) too low |
| `Phase order is wrong!` | the motor did not respond to the commutation check; wiring, current limit, magnet |
| calibration succeeds, the motor then runs badly or in the wrong direction | the magnet slipped on the shaft; glue it and calibrate again |
| calibration succeeds but the LED stays on and `#Error` shows nothing | `#Info` shows `-1`: `#Default`, parameters, calibrate again |

## The motor

| Symptom | Cause |
|---|---|
| crunching or whining at speed | the current limit or the current loop gains too high; lower `#Ilim`, lower `#Cbw` and calibrate again, or lower `#Kpiq` |
| humming, oscillating at rest | `#Kpv` or `#Kpp` too high; see [Current limit and loop tuning](05-setup/tuning.md) |
| weak torque | `#Ilim` low; the supply's current limit; the wrong `#R`/`#L` (the computed current gains are off) |
| the motor is hot | normal for a stepper at its rated current; lower `#Ilim`, enable the thermistor |
| it stops with a Vbus error when decelerating | the supply cannot absorb the returned energy; a different supply, or a brake resistor |
| it stops with a velocity error | the speed limit `#Vlimit`, or a load that lets the motor overrun |
| it loses position with a load | that is a torque limit: a stepper under FOC does not lose steps, it falls behind; raise `#Ilim` within the motor's rating, or more motor |
| it holds position with a sawtooth noise | the position loop gain; the magnet distance |

## Low-quality motors

Motors with visibly bad windings, an uneven back-EMF or a resistance that differs between the two coils calibrate
poorly and run rough. The [tested motors](03-technical-data/tested-motors.md) are known good.

## The magnet and the encoder

- The distance is 1 mm. "Magnet Good" from the magnet test does not mean the distance is right, only that the
  field is strong enough.
- A magnet touching the chip can destroy the microcontroller; a magnet too far gives a noisy, wrong position.
- The magnet must be diametrically magnetised and centred on the shaft.

## The driver gets hot or shuts down

The MOSFET driver stage shuts down on its own overtemperature or overcurrent and reports a driver error. Lower
the current limit, give the board airflow, check the motor leads for a short. Near 2.8 A the driver needs
cooling.

## After a firmware update

`#Info` shows the new release. If the values look wrong or the LED stays on: `#Default`, enter the motor
parameters, `#Cal`, `#Save`. A release note says when an update clears the calibration.

## Getting help

[Support](support/index.md) says where to ask and what to include; `#Info`'s output is the first thing.
