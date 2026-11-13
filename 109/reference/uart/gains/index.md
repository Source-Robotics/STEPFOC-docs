# Gains and limits

<div class="cmd-index" markdown>[`#Kpp`](#kpp) [`#Kpv`](#kpv) [`#Kiv`](#kiv) [`#Kpiq`](#kpiq) [`#Kiiq`](#kiiq) [`#Kpid`](#kpid) [`#Kiid`](#kiid) [`#KP`](#kp) [`#KD`](#kd) [`#Vlimit`](#vlimit) [`#Ilim`](#ilim) [`#Vlim`](#vlim) [`#Rstint`](#rstint) [`#Cbw`](#cbw)</div>

### `#Kpp` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: gain</span></div>

Kp of the position loop.

**Response:** the current value

---

### `#Kpv` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: gain</span></div>

Kp of the velocity loop.

**Response:** the current value

---

### `#Kiv` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: gain</span></div>

Ki of the velocity loop.

**Response:** the current value

---

### `#Kpiq` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: gain</span></div>

Kp of the Iq current loop; also sets Kpid.

**Response:** the current value

---

### `#Kiiq` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: gain</span></div>

Ki of the Iq current loop; also sets Kiid.

**Response:** the current value

---

### `#Kpid` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: gain</span></div>

Kp of the Id current loop.

**Response:** the current value

---

### `#Kiid` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: gain</span></div>

Ki of the Id current loop.

**Response:** the current value

---

### `#KP` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: gain</span></div>

KP of the impedance (PD) loop.

**Response:** the current value

---

### `#KD` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: gain</span></div>

KD of the impedance (PD) loop.

**Response:** the current value

---

### `#Vlimit` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: speed in encoder ticks/s</span></div>

The speed limit: it clamps the speed setpoint of the velocity loop, and in position mode the speed the position loop asks for. The velocity integrator is clamped to the current limit (Ilim), not to this. From firmware 109 a negative number counts as its magnitude.

**Response:** the current limit

---

### `#Ilim` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: current in mA</span></div>

The Iq current limit, 1700 mA after #Default. Set it to the rated phase current of your motor; this command clamps it to 2800 mA and takes the magnitude of a negative number (from firmware 109 Send_Limits over CAN stops at 2800 mA too). Calibration uses 1600 mA for its steps and, from firmware 109, puts it back when it ends.

**Response:** the current limit

---

### `#Vlim` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: voltage in mV</span></div>

The voltage limit of the current loops (Ud and Uq), 6000 mV by default. It keeps the loops of low-resistance steppers stable, and it also caps the top speed. 0, or a value above the supply voltage, means the supply voltage.

**Response:** the current limit in mV

---

### `#Rstint` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: 0 or 1</span></div>

Whether the integral accumulators are reset on every new setpoint.

**Response:** the setting

---

### `#Cbw` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: bandwidth in Hz, 10 to 625</span></div>

The current loop bandwidth. From firmware 109 setting it computes Kpiq and Kiiq at once from R and L, the way calibration does, and prints them (the same as parameter 49); a value outside 10-625, or with R or L at 0, changes nothing. Not kept by Save: 160 Hz at every power-up, but the gains it set are kept.

**Response:** the bandwidth, then `Kp_iq = …, Ki_iq = …`

---
