# Status and utility

<div class="cmd-index" markdown>[`#Save`](#save) [`#Reset`](#reset) [`#Default`](#default) [`#Pullconfig`](#pullconfig) [`#Info`](#info) [`#Tone`](#tone) [`#Par`](#par) [`#Tool`](#tool) [`#WdFb`](#wdfb) [`#Product`](#product) [`#Param`](#param) [`#Help`](#help) [`#Error`](#error) [`#Clear`](#clear) [`#Mode`](#mode) [`#Vbus`](#vbus) [`#Vmax`](#vmax) [`#Temp`](#temp) [`#Term`](#term) [`#Tlim`](#tlim) [`#Iabc`](#iabc) [`#PWM`](#pwm) [`#LED`](#led) [`#CANID`](#canid) [`#SERNUM`](#sernum) [`#Activate`](#activate) [`#Cyc`](#cyc) [`#Cyca`](#cyca)</div>

### `#Save` 

<div class="cmd-facts" markdown><span class="fact">Action</span></div>

Writes the configuration to the EEPROM, and the CAN ID into the bootloader's board ID. Do it after calibration and after tuning. It also writes the serial number held in RAM (1 after a power-up, unless SERNUM set it) over the stored one.

**Response:** `Save`

---

### `#Reset` 

<div class="cmd-facts" markdown><span class="fact">Action</span></div>

Resets the driver. From firmware 105 the reset lands in the bootloader, which waits 2 s for a flashing host and then starts the firmware again.

**Response:** nothing

---

### `#Default` 

<div class="cmd-facts" markdown><span class="fact">Action</span></div>

Writes the factory defaults to the EEPROM and loads them: the serial number, hardware version and batch date; the gripper flag, heartbeat, watchdog and thermistor (off); the motor parameters and the calibration (cleared); every gain and limit; from firmware 109 also the tool id (0), the watchdog fallback, the calibration ID (0), the anti-cogging set, the encoder table and its trims (cleared), and parameter 56 (back to 2). From firmware 109 the CAN ID is kept (0 only when no valid one is stored). See Defaults.

**Response:** `Loaded default config!`

---

### `#Pullconfig` 

<div class="cmd-facts" markdown><span class="fact">Get</span></div>

Prints the whole configuration on one line, for Motor GUI.

**Response:** the configuration

---

### `#Info` 

<div class="cmd-facts" markdown><span class="fact">Action</span></div>

Prints the hardware version, batch date and firmware version, the control loop's execution time, the CAN ID, the calibration state, the thermistor and the supply voltage, the phase direction, phase order and commutation direction, and the motor parameters (pole pairs, angle offset, R, L, Kt, KV). From firmware 109 also the build, the board ID and the calibration ID, the CAN receive overruns and dropped transmits, the product, the current-sense zeros, the tool id, the watchdog and its fallback, settings block 2, the anti-cogging, and at the end the `In force:` section (see Status and diagnostics). Not the serial number (SERNUM), the gains (Param) or the errors (Error).

**Response:** the report

---

### `#Tone` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> f,mA[,ms], or off</span><span class="fact">Enters **position** mode</span></div>

A tone through the motor (see Sound): `#Tone 440,250,1000` plays 440 Hz at a loudness of 250 mA for 1000 ms, on the axis parameter 82 picks. mA left out: 200; ms left out: 500; ms 0: until `#Tone off`. 20 Hz up to below 3125 Hz. It plays only while the driver holds or moves; from idle a calibrated driver first holds the position it is at (`#Idle` releases it). `#Tone` alone or `#Tone off` stops all sound. Added in firmware 109.

**Response:** `Tone 440 Hz, 250 mA, 1000 ms`; from idle first `Holding the position while it plays (#Idle releases it)`; `Tone: not played (…)` when it cannot; `Tone off`

---

### `#Par` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: n, or n,value</span></div>

Any parameter by its number (see Parameters and buffers): alone it lists every parameter, `#Par 56` reads one, `#Par 56,0` sets it (no spaces); a gain or limit (8-16, 20) takes a decimal, e.g. `#Par 9,0.02` sets Kpv. Added in firmware 109.

**Response:** `P<n> = <value>`; `refused: out of range, read only, not now, or unknown` when the driver did not take it; `P<n> unknown`

---

### `#Tool` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: 0 to 255</span></div>

The tool id: what the drive is built into, 0 none, 1 SSG-48, 11-33 MSG (tens = rail 1/2/3 = 100/150/200 mm, units = stepper 1/2/3 = 21.5/40/60 mm), 200-254 your own. The same as parameter 1. Kept by Save. Added in firmware 109.

**Response:** `Tool ID: N`, or `Invalid tool id (0-255)`

---

### `#WdFb` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int list: time_ms,current_mA,speed_ticks_s,after_action</span></div>

The watchdog fallback, four numbers at once without spaces, e.g. `#WdFb 2000,0,1000,2`: how long hold or descend runs, descend's current and speed cap, and what follows (0 legacy, 2 brake, 3 coast). The same as parameters 2 to 5, clamped the same way; fewer than four numbers change nothing. Kept by Save. Added in firmware 109.

**Response:** `Watchdog fallback: … ms, … mA, … ticks/s, then …`

---

### `#Product` 

<div class="cmd-facts" markdown><span class="fact">Action</span><span class="fact"><span class="k">Argument</span> nothing, or claim, clear</span></div>

The product lock: prints this firmware and the board's stamp. `claim` stamps the board as this product (a repaired board, a motor the stamp rule misjudges), `clear` removes the stamp; power-cycle after either. Over UART only. Added in firmware 109.

**Response:** `Firmware: STEPFOC; board stamp: …`

---

### `#Param` 

<div class="cmd-facts" markdown><span class="fact">Get</span></div>

Prints every gain of every loop.

**Response:** the gains

---

### `#Help` 

<div class="cmd-facts" markdown><span class="fact">Action</span></div>

Prints a short command reference. Added in firmware 106.

**Response:** the reference

---

### `#Error` 

<div class="cmd-facts" markdown><span class="fact">Get</span></div>

Prints which errors are active.

**Response:** `No errors!` or `In error state!` followed by one line per active error

---

### `#Clear` 

<div class="cmd-facts" markdown><span class="fact">Action</span><span class="fact">Enters **idle** mode</span></div>

Clears the errors and goes to idle. An error whose cause is still present comes straight back; a calibration error is cleared only by calibrating (or `#Calibrated 1`).

**Response:** `Clear errors`

---

### `#Mode` 

<div class="cmd-facts" markdown><span class="fact">Get</span></div>

Prints the control mode. The voltage-torque mode prints `Gripper mode`; HALL, the angle-offset search, open-loop steps (gosteps), gripper mode and the encoder-table run print nothing.

**Response:** `Idle mode`, `Position control`, `Speed control`, `Current control`, `PD control`, `Open loop`, `Gripper mode`, `Gripper calib mode`

---

### `#Vbus` 

<div class="cmd-facts" markdown><span class="fact">Get</span></div>

Prints the supply voltage.

**Response:** mV

---

### `#Vmax` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: voltage in mV</span></div>

The supply voltage above which a Vbus error is raised, 29000 mV after #Default.

**Response:** `Vmax in mV: N`

---

### `#Temp` 

<div class="cmd-facts" markdown><span class="fact">Get</span></div>

Prints the thermistor temperature.

**Response:** °C, or `Temp Off` while the thermistor is disabled

---

### `#Term` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: 0 or 1</span></div>

Enables the thermistor measurement and the temperature error (off by default).

**Response:** the setting

---

### `#Tlim` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: temperature in °C</span></div>

The temperature at which the temperature error is raised; 75 by default.

**Response:** `Temp limit N`

---

### `#Iabc` 

<div class="cmd-facts" markdown><span class="fact">Get</span></div>

Prints the phase currents.

**Response:** `Ia`, `Ib` in mA

---

### `#PWM` 

<div class="cmd-facts" markdown><span class="fact">Get</span></div>

Prints the PWM duty values.

**Response:** the duties

---

### `#LED` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: 0 or 1</span></div>

Turns the status LED on or off.

**Response:** the LED state

---

### `#CANID` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: 0 to 13</span></div>

The CAN node ID. Use 0 to 13: the firmware accepts 14 and 15, but the bootloader reserves them and a driver on one of those cannot be updated over CAN. Kept over a power cycle after Save, which also writes it into the bootloader's board ID; from firmware 109 Default and a settings reset keep it too.

**Response:** the ID, or `Invalid CAN ID`

---

### `#SERNUM` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: number</span></div>

The serial number. This firmware does not read it back from the EEPROM at power-up: it reports 1 until set, and Save writes the value in RAM over the stored one.

**Response:** `Serial number is: N`

---

### `#Activate` 

<div class="cmd-facts" markdown><span class="fact">Action</span></div>

Sets the activated flag.

**Response:** `Controller activated`

---

### `#Cyc` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: interval in ms (0 = off)</span></div>

Sends position, speed and Iq on its own every interval: `$ <position> <speed> <Iq>`; for BetterSerialPlotter.

**Response:** `Cyclic disabled` when turned off

---

### `#Cyca` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: interval in ms (0 = off)</span></div>

Like Cyc, in the Arduino plotter format `Position:x,Speed:y,Iq:z`.

**Response:** `Cyclic disabled` when turned off

---
