# Calibration and motor parameters

<div class="cmd-index" markdown>[`#Cal`](#cal) [`#Calonly`](#calonly) [`#Calangle`](#calangle) [`#Encal`](#encal) [`#Cogcal`](#cogcal) [`#R`](#r) [`#L`](#l) [`#PP`](#pp) [`#Kt`](#kt) [`#KV`](#kv) [`#Flux`](#flux) [`#Offset`](#offset) [`#Iqoffset`](#iqoffset) [`#Magnet`](#magnet) [`#Dir`](#dir) [`#Phase`](#phase) [`#Resv`](#resv) [`#Calpwr`](#calpwr) [`#Openv`](#openv) [`#Opens`](#opens) [`#Vp`](#vp) [`#Calibrated`](#calibrated)</div>

### `#Cal` 

<div class="cmd-facts" markdown><span class="fact">Action</span><span class="fact">Enters **idle** mode</span></div>

Runs the calibration routine (see Motor parameters and calibration), over the serial port only. Enter R, L and PP first, and the current limit for the motor: it uses its own 1600 mA for its steps and puts the limit back when it ends (firmware 108 and older left 1600 mA). From firmware 109, when it succeeds, the encoder table and then the anti-cogging with the current-sense trim follow by themselves, and everything is saved (about a minute; keep the shaft free).

**Response:** the calibration log

---

### `#Calonly` 

<div class="cmd-facts" markdown><span class="fact">Action</span><span class="fact">Enters **idle** mode</span></div>

The calibration alone: like Cal, but nothing follows it. Save afterwards with Save. Added in firmware 109.

**Response:** the calibration log

---

### `#Calangle` 

<div class="cmd-facts" markdown><span class="fact">Action</span><span class="fact">Enters **angle-offset calibration** mode</span></div>

Runs only an angle-offset search. It uses an older routine than the one in Cal, which gives up after about two minutes and keeps the offset it reached. Prints `Idle` at once, before the search starts. From firmware 109, when parameter 56 is not 0, the anti-cogging is identified again afterwards (with the current-sense trim) and everything is saved: the anti-cogging depends on the offset. After a timeout nothing follows and nothing is saved. From firmware 109 it is refused while the driver is in error.

**Response:** `Idle`, at once; `Calangle: not started, the drive is in error (#Error, #Clear)` when it is refused

---

### `#Encal` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> nothing, or save, all, stop, on, off, state</span></div>

The encoder table (see Encoder table and anti-cogging). Alone it measures the table and uses it: the field turns the rotor open loop one shaft turn each way at 2048 ticks/s, about 20 s, with the shaft free. `save` also saves; `all` then identifies the anti-cogging and saves both; `stop` aborts; `on` and `off` switch the correction (on only with a measured table, and neither while a run turns the motor); `state`, or any other word, only prints. The same as parameters 52 and 53. Added in firmware 109.

**Response:** `Encoder table: <state>`, then the table's error in degrees

---

### `#Cogcal` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> nothing, or save, trim, stop, state</span></div>

The anti-cogging identification on the drive (see Encoder table and anti-cogging): one motor turn forward and one back in velocity mode at parameter 44's speed (1500 ticks/s, about 22 s), the shaft free to turn. `save` also saves; `trim` first corrects the current-sense zeros from the result and identifies again (not saved: parameter 43 = 5 trims and saves); `stop` aborts, also the encoder part of a combined run; `state`, or any other word, only prints. States 10 and 11 print their own text; 7 and 8, the encoder part of a combined run, show only in parameter 43. Added in firmware 109.

**Response:** `Anti-cogging identification: <state>`, the speed and the identified cogging in mA rms, and the harmonics when done

---

### `#R` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: resistance in Ω</span></div>

The phase resistance of the motor (one coil). STEPFOC does not measure it; enter the datasheet value before Cal. Also parameter 76, in mΩ.

**Response:** the current value

---

### `#L` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: inductance in H</span></div>

The phase inductance of the motor (one coil); enter the datasheet value before Cal. Also parameter 77, in µH.

**Response:** the current value

---

### `#PP` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: pole pairs</span></div>

The motor's pole pairs: 50 for a 1.8° stepper, 75 for 1.2°, 100 for 0.9°, 125 for 0.72°. Calibration accepts only these values. Also parameter 78: 1-200, only while idle; from 109 `#PP` answers `PP: not taken (1-200, and only while idle)` otherwise.

**Response:** the current value

---

### `#Kt` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: Nm/A</span></div>

The torque constant, found by calibration.

**Response:** the current value

---

### `#KV` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: rpm/V</span></div>

The velocity constant, found by calibration.

**Response:** the current value

---

### `#Flux` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: Wb</span></div>

The flux linkage, found by calibration. Works over UART from firmware 109; the parser of 108 and older accepted only the lowercase `#flux`, which had no handler.

**Response:** the current value

---

### `#Offset` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: angle in rad</span></div>

The angle offset between encoder zero and electrical zero, found by calibration.

**Response:** the current value

---

### `#Iqoffset` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: current in mA</span></div>

The current used by the angle-offset search.

**Response:** the current value

---

### `#Magnet` 

<div class="cmd-facts" markdown><span class="fact">Get</span></div>

Reads the encoder's magnet status.

**Response:** `Magnet Good` or `Magnet Bad`

---

### `#Dir` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: 0 or 1</span></div>

A stored flag that Info prints as `Phase direction`. The control code does not use it in this release; #Default writes 0.

**Response:** the current value

---

### `#Phase` 

<div class="cmd-facts" markdown><span class="fact">Get</span></div>

Prints the phase order found by calibration.

**Response:** `Phase order is: N`

---

### `#Resv` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: voltage in mV</span></div>

The voltage calibration starts the resistance test at (not used by STEPFOC, which does not measure resistance).

**Response:** the current value

---

### `#Calpwr` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: power in W</span></div>

The power calibration may dissipate in the resistance and inductance tests (not used by STEPFOC).

**Response:** the current value

---

### `#Openv` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: voltage in mV</span></div>

The voltage of the open-loop modes (Openloop, gosteps), 5000 mV at power-up. Calibration does not use it: its open-loop spin has a fixed 5000 mV. Not kept by Save.

**Response:** the current value

---

### `#Opens` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: electrical speed in rad/s</span></div>

The electrical speed of Openloop, the same value Openloop sets. Calibration does not use it.

**Response:** the current value

---

### `#Vp` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: voltage in mV</span></div>

Stored, but not used by this firmware: the phase-order check of calibration uses a fixed 3000 mV.

**Response:** the current value

---

### `#Calibrated` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: 0 or 1</span></div>

The calibrated flag. `#Calibrated 1` clears a calibration error without calibrating; the motor may still be uncalibrated.

**Response:** the flag

---
