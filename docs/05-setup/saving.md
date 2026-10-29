# Saving the configuration

Nothing you set with a command survives a power cycle until you save it.

```
#Save
```

writes the whole configuration to the EEPROM: the motor parameters and the calibration, every gain and limit, the
CAN node ID, the heartbeat and watchdog settings, the thermistor and LED settings and the gripper flag. Over CAN,
Send_Save_config does the same. Save after calibration, after tuning, and after changing the node ID.

## The defaults

```
#Default
```

writes the factory defaults to the EEPROM and reloads them. It also resets the serial number, the hardware version
and the batch date that the driver reports, and it clears the gripper flag, the heartbeat rate and the watchdog;
note the values `#Info` prints before you use it. The defaults are listed in the [Defaults](../reference/defaults.md)
reference.

Use it after a firmware update when the driver behaves oddly, or when `#Info` shows nonsense values (a `-1` where
a number should be): the EEPROM then holds a layout the firmware does not expect.

## What `#Info` shows

`#Info` prints what is in the EEPROM and what the driver measures: hardware and firmware version, serial number,
calibration state, resistance, inductance, pole pairs, Kt and KV, the gains and limits, the CAN ID, and the active
errors. It is the first thing to look at when something is off, and the thing to copy into a bug report.
