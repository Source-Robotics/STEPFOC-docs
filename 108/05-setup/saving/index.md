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
settings and the gripper flag. Over CAN, Send_Save_config does the same. Save after calibration, after tuning, and
after changing the node ID.

Some settings are not kept and start from their defaults at every power-up: the current loop bandwidth (`#Cbw`,
500 Hz), the idle behaviour (`#Brake` / `#Coast` or Send_Settings: brake), and the open-loop and calibration
settings (`#Openv`, `#Opens`, `#Vp`, `#Iqoffset`, `#microstep`, `#stepinterval`). The
[Defaults](https://docs.source-robotics.com/STEPFOC-docs/108/reference/defaults/) reference marks each setting.

!!! warning "A saved watchdog runs from power-up"
    With a watchdog saved (Send_Watchdog), the driver starts its count at power-up. A host that sends no motion
    frame or status request within the watchdog time finds the driver in watchdog error, and clears it with
    Send_Clear_Error. See [Over CAN](https://docs.source-robotics.com/STEPFOC-docs/108/06-operation/can/#a-control-loop).

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

Restoring the defaults writes the factory values to the EEPROM and reloads them. It also sets the CAN node ID to
0 and the thermistor to off, resets the serial number, the hardware version and the batch date stored in the
EEPROM, and clears the gripper flag, the heartbeat rate and the watchdog. Note the hardware version and batch date
`#Info` prints before you use it, and give the driver its node ID again afterwards. The defaults are listed in the
[Defaults](https://docs.source-robotics.com/STEPFOC-docs/108/reference/defaults/) reference.

Use it before the first calibration of a motor, after a firmware update when the driver behaves oddly, and when
the state shows nonsense values (a `-1` where a number should be). With firmware 106 and newer that should not
happen: the driver checks the stored configuration at power-up and replaces a damaged block with the defaults by
itself.

## What the driver reports

The state Motor GUI shows is what is in the EEPROM and what the driver measures. In a terminal it takes three
commands: `#Info` prints the hardware and firmware version, the CAN ID, the calibration state and the motor
parameters (pole pairs, resistance, inductance, Kt and KV); `#Param` prints the gains and limits; `#Error` the
active errors. They are the first thing to look at when something is off, and the thing to copy into a bug
report.
