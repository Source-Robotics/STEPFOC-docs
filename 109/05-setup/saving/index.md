# Saving the configuration

Nothing you set survives a power cycle until you save it.

=== "Motor GUI"
    **Save**. The GUI marks *Unsaved changes* until you do.

=== "Terminal"
    ```
    #Save
    ```

Saving writes the configuration to the EEPROM: the motor parameters and the calibration, every gain and limit,
the CAN node ID (and the bootloader's board ID with it), the heartbeat and watchdog settings, the thermistor and LED
settings and the gripper flag. From firmware 109 also the tool id and the watchdog fallback, the anti-cogging set
with its mode and scale, and the encoder table with its on/off switch, parameter 56 and the current-sense zero
trims. Over CAN, Send_Save_config does the same. Save after calibration, after tuning, and after changing the node
ID. The runs after a calibration save by themselves when they succeed.

Some settings are not kept and start from their defaults at every power-up: the current loop bandwidth (`#Cbw`,
160 Hz; the gains it computed are kept), the idle behaviour (`#Brake` / `#Coast` or Send_Settings: brake), the
open-loop and calibration settings (`#Openv`, `#Opens`, `#Vp`, `#Iqoffset`, `#microstep`, `#stepinterval`), and
the parameters of firmware 109 that tune the loops: the speed estimate (direct PLL at 60 Hz), the commutation delay
compensation (166 µs), the fast reading and PWM paths (on), the sin/cos table (off), the position input filter and
the velocity-integral deadband (off), the anti-cogging identification speed, the d-axis current, and the capture
and histogram settings. The [Defaults](https://docs.source-robotics.com/STEPFOC-docs/109/reference/defaults/) reference marks each setting, and the
[parameter table](https://docs.source-robotics.com/STEPFOC-docs/109/reference/can/parameters/#every-parameter) says for every parameter whether it is kept.

!!! warning "A saved watchdog runs from power-up"
    With a watchdog saved (Send_Watchdog), the driver starts its count at power-up. A host that sends no motion
    frame or status request within the watchdog time finds the driver in watchdog error, and clears it with
    Send_Clear_Error. See [Over CAN](https://docs.source-robotics.com/STEPFOC-docs/109/06-operation/can/#a-control-loop).

!!! note "The serial number"
    This firmware does not read the serial number back from the EEPROM at power-up: `#SERNUM` reports 1 until it
    is set, and every save writes the value held in RAM over the stored one.

## The defaults

=== "Motor GUI"
    *Default* in the settings.

=== "Terminal"
    ```
    #Default
    ```

Restoring the defaults writes the factory values to the EEPROM and reloads them. It also sets the thermistor to
off, resets the serial number, the hardware version and the batch date stored in the EEPROM, and clears the
gripper flag, the heartbeat rate and the watchdog; from firmware 109 also the tool id, the watchdog fallback, the
anti-cogging set, the encoder table and its zero trims, and sets parameter 56 back to its default. The CAN node ID
is kept from firmware 109 (it is 0 only when no valid ID is stored); firmware 108 and older set it to 0. Note the
hardware version and batch date `#Info` prints before you use it. The defaults are listed in the
[Defaults](https://docs.source-robotics.com/STEPFOC-docs/109/reference/defaults/) reference.

Use it before the first calibration of a motor, after a firmware update when the driver behaves oddly, and when
the state shows nonsense values (a `-1` where a number should be). With firmware 106 and newer that should not
happen: the driver checks the stored configuration at power-up and replaces a damaged block with the defaults by
itself.

## Where it is kept: the EEPROM

The configuration lives in an EEPROM chip on the board (a 24C16, 2 KB), apart from the firmware: flashing a new
firmware never touches it, and only the firmware's check at power-up decides to reset a part of it. Since
firmware 106 the configuration is in blocks, each with its own checksum; firmware 109 adds three:

| Block | Bytes | Checksum at | Holds |
|---|---|---|---|
| calibration | 60-188, reserved 212-236 | 208 | pole pairs, R, L, Kt, KV, flux linkage, angle offset, phase order, commutation direction, the current gains |
| settings 1 | 44-180 | 192 | CAN ID, limits, the other gains, watchdog, heartbeat, thermistor, LED, gripper flag |
| settings 2 (109) | 260-312 | 256 | tool id, watchdog fallback, the product stamp, the calibration ID; reserved slots |
| anti-cogging (109) | 324-879 | 320 | the harmonics, the table, mode and scale |
| encoder table (109) | 884-1147 | 880 | the table, its on/off switch, parameter 56, the current-sense zero trims |

At power-up a block whose checksum does not match is read again, up to three times. If it still does not match,
it gets its defaults, alone, and the others stay; a settings
reset keeps a valid CAN ID. A board saved by firmware 101 to 105, from before the checksums, is trusted when the
first 109 start finds anything it ever saved, and sealed with checksums then. The new blocks need the chip's upper
banks; on a smaller chip they keep their defaults in RAM and are not saved, which `#Info` says
(`Settings block 2: not available`, `block 3 not available`) and the identity frame's flag bit 3 shows. Going back
to an older firmware is safe: the first two blocks are unchanged, and older firmware ignores everything from byte
256 on. [Upgrading from older firmware](https://docs.source-robotics.com/STEPFOC-docs/109/07-firmware/upgrading/) says what changes when you update.

## What the driver reports

The state Motor GUI shows is what is in the EEPROM and what the driver measures. In a terminal it takes three
commands: `#Info` prints the hardware and firmware version, the CAN ID, the calibration state and the motor
parameters (pole pairs, resistance, inductance, Kt and KV), and from firmware 109 the build, the board ID and the
calibration ID, the tool id, the watchdog, the EEPROM blocks and, at its end, what is in force;
`#Param` prints the gains and limits; `#Error` the active errors.
They are the first thing to look at when something is off, and the thing to copy into a bug report.
[Status and diagnostics](https://docs.source-robotics.com/STEPFOC-docs/109/06-operation/diagnostics/) explains the new lines.
