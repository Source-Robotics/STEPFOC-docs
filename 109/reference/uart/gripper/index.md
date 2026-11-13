# Gripper

<div class="cmd-index" markdown>[`#Gripper`](#gripper) [`#Gripcal`](#gripcal) [`#Grippos`](#grippos) [`#Gripvel`](#gripvel) [`#Gripcur`](#gripcur) [`#Gripact`](#gripact) [`#Gripstop`](#gripstop) [`#Gripinfo`](#gripinfo)</div>

### `#Gripper` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: 0 or 1</span></div>

Whether this driver is a gripper. Save it; `#Default` clears it.

**Response:** the flag

---

### `#Gripcal` 

<div class="cmd-facts" markdown><span class="fact">Action</span><span class="fact">Enters **gripper calibration** mode</span></div>

Starts the gripper calibration: the jaws find their end stops at 500 mA. It prints nothing when it ends; after about 24 s without both end stops it gives up, uncalibrated. Gripinfo shows the result.

**Response:** `Gripper calibration!`

---

### `#Grippos` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: 0 (open) to 255 (closed)</span><span class="fact">Enters **gripper** mode</span></div>

The position setpoint; also activates the gripper, sets the action bit and goes to gripper mode.

**Response:** the current position

---

### `#Gripvel` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: 0 to 255</span></div>

The speed setpoint of gripper moves, 50 at power-up.

**Response:** the setpoint

---

### `#Gripcur` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: current in mA</span></div>

The current limit of gripper moves, 400 mA at power-up. From firmware 109 a move uses its magnitude, at most the driver's 2800 mA (108 and older used it as sent); see the gripper manual for the safe range.

**Response:** the setpoint

---

### `#Gripact` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: 0 or 1</span></div>

The activate bit.

**Response:** the bit

---

### `#Gripstop` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: 0 or 1</span></div>

The gripper E-stop bit. While it is 1 the driver raises the gripper E-stop error on every control cycle: set it to 0, then Clear.

**Response:** the bit

---

### `#Gripinfo` 

<div class="cmd-facts" markdown><span class="fact">Get</span></div>

Prints the gripper state: calibrated, activated, end stops, position, current.

**Response:** the report

---
