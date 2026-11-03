# Status and utility

| Command | Kind | Argument | What it does | Response |
|---|---|---|---|---|
| `#Vmax` | Set/Get | int: voltage in mV | The supply voltage above which a Vbus error is raised, 29000 mV after #Default. | `Vmax in mV: N` |
| `#Save` | Action |  | Writes the configuration to the EEPROM, and the CAN ID into the bootloader's board ID. Do it after calibration and after tuning. It also writes the serial number held in RAM (1 after a power-up, unless SERNUM set it) over the stored one. | `Save` |
| `#Reset` | Action |  | Resets the driver. From firmware 105 the reset lands in the bootloader, which waits 2 s for a flashing host and then starts the firmware again. | nothing |
| `#Tlim` | Set/Get | int: temperature in °C | The temperature at which the temperature error is raised; 75 by default. | `Temp limit N` |
| `#Default` | Action |  | Writes the factory defaults to the EEPROM and loads them: the serial number, hardware version and batch date; the CAN ID (0); the gripper flag, heartbeat, watchdog and thermistor (off); the motor parameters and the calibration (cleared); every gain and limit. See Defaults. | `Loaded default config!` |
| `#Temp` | Get |  | Prints the thermistor temperature. | °C, or `Temp Off` while the thermistor is disabled |
| `#Term` | Set/Get | int: 0 or 1 | Enables the thermistor measurement and the temperature error (off by default). | the setting |
| `#Mode` | Get |  | Prints the control mode. The voltage-torque mode prints `Gripper mode`; HALL, the angle-offset search, open-loop steps (gosteps) and gripper mode print nothing. | `Idle mode`, `Position control`, `Speed control`, `Current control`, `PD control`, `Open loop`, `Gripper mode`, `Gripper calib mode` |
| `#Vbus` | Get |  | Prints the supply voltage. | mV |
| `#Error` | Get |  | Prints which errors are active. | `No errors!` or `In error state!` followed by one line per active error |
| `#Clear` | Action |  | Clears the errors and goes to idle. An error whose cause is still present comes straight back; a calibration error is cleared only by calibrating (or `#Calibrated 1`). Enters **idle** mode. | `Clear errors` |
| `#Iabc` | Get |  | Prints the phase currents. | `Ia`, `Ib` in mA |
| `#PWM` | Get |  | Prints the PWM duty values. | the duties |
| `#Help` | Action |  | Prints a short command reference. Added in firmware 106. | the reference |
| `#Info` | Get |  | Prints the hardware version, batch date and firmware version, the control loop's execution time, the CAN ID, the calibration state, the thermistor and the supply voltage, the phase direction, phase order and commutation direction, and the motor parameters (pole pairs, angle offset, R, L, Kt, KV). Not the serial number (SERNUM), the gains (Param) or the errors (Error). | the report |
| `#Param` | Get |  | Prints every gain of every loop. | the gains |
| `#Cyc` | Set/Get | int: interval in ms (0 = off) | Sends position, speed and Iq on its own every interval: `$ <position> <speed> <Iq>`; for BetterSerialPlotter. | `Cyclic disabled` when turned off |
| `#Cyca` | Set/Get | int: interval in ms (0 = off) | Like Cyc, in the Arduino plotter format `Position:x,Speed:y,Iq:z`. | `Cyclic disabled` when turned off |
| `#CANID` | Set/Get | int: 0 to 13 | The CAN node ID. Use 0 to 13: the firmware accepts 14 and 15, but the bootloader reserves them and a driver on one of those cannot be updated over CAN. Kept over a power cycle after Save, which also writes it into the bootloader's board ID. | the ID, or `Invalid CAN ID` |
| `#SERNUM` | Set/Get | int: number | The serial number. This firmware does not read it back from the EEPROM at power-up: it reports 1 until set, and Save writes the value in RAM over the stored one. | `Serial number is: N` |
| `#Activate` | Action |  | Sets the activated flag. | `Controller activated` |
| `#Pullconfig` | Get |  | Prints the whole configuration on one line, for Motor GUI. | the configuration |
| `#LED` | Set/Get | int: 0 or 1 | Turns the status LED on or off. | the LED state |
