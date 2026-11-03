# Errors and LED states

## The LED

| Pattern | State |
|---|---|
| three short flashes, a pause | normal operation: calibrated, no error |
| fast flashing, about ten times a second | calibration running |
| a few flashes, then blinking for about 2 s after power-up | the bootloader waits for a host before it starts the firmware; it keeps blinking when there is no valid firmware |
| on, steady | error mode, or not calibrated |
| off | no power, or `#LED 0` |

| Normal operation | Calibration | Error mode |
|---|---|---|
| ![Three short flashes and a pause](https://docs.source-robotics.com/STEPFOC-docs/108/assets/Normal.webp){ width="180" } | ![Fast flashing during calibration](https://docs.source-robotics.com/STEPFOC-docs/108/assets/Calib.webp){ width="180" } | ![On, steady](https://docs.source-robotics.com/STEPFOC-docs/108/assets/Error2.webp){ width="180" } |

## The error flags

The flags as the firmware keeps them, the line `#Error` prints for each, and where each sits in the two bytes of
Send_Respond_State_of_Errors (bits numbered from the most significant).

| Flag | `#Error` prints | Byte, bit | Raised when |
|---|---|---|---|
| `Error` | `In error state!` | 0, 7 | any of the flags below is set (also the error bit of every CAN identifier) |
| `temperature_error` | `Temp error` | 0, 6 | the thermistor reads above `#Tlim` (with `#Term 1`) |
| `encoder_error` | `Encoder error` | 0, 5 | the encoder reports no magnet (too weak a field) |
| `Vbus_error` | `Vbus error` | 0, 4 | the supply is below 9 V or above `#Vmax` (29000 mV after `#Default`) |
| `Driver_error` | `Driver error (undervoltage, thermal shutdown, or overcurrent)` | 0, 3 | never in this firmware; reserved (STEPFOC reads no fault output of its driver stage) |
| `Velocity_error` | `Velocity error` | 0, 2 | the speed exceeds 30,000,000 ticks/s, a fixed threshold (`Velocity_limit_error`), not `#Vlimit` |
| `Current_error` | `Current error` | 0, 1 | never in this firmware; reserved |
| `ESTOP_error` | `Received ESTOP command` | 0, 0 | Send_ESTOP was received |
| `Calibrated` (0) | `Not calibrated` | 1, 7 (1 = calibrated) | the motor has not been calibrated |
| `Activated` | — | 1, 6 | the activated flag, not an error |
| `Watchdog_error` | `Watchdog error` | 1, 5 | the watchdog time passed without a motion frame or a status request |

Gripper mode has its own flags in Respond_Gripper_data_pack: a temperature error (a copy of the thermistor error),
a timeout error (a copy of the CAN watchdog error, not a move timeout) and an E-stop error, which stays while the
E-stop bit is 1; see the [Gripper](https://docs.source-robotics.com/STEPFOC-docs/108/reference/can/gripper/) reference.

## Clearing

`#Clear` and Send_Clear_Error clear every flag except `Calibrated` and go to idle; a flag whose cause persists is
set again at once. The watchdog, E-stop and velocity errors clear and stay clear; the Vbus, encoder and
temperature errors come back until the cause is gone, and so does a gripper E-stop while its E-stop bit is 1.
Calibration clears the calibration error.
