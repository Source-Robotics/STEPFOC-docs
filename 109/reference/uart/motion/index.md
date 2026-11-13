# Motion

<div class="cmd-index" markdown>[`#Iq`](#iq) [`#Id`](#id) [`#V`](#v) [`#P`](#p) [`#PD`](#pd) [`#PDV`](#pdv) [`#PDI`](#pdi) [`#Uq`](#uq) [`#Ud`](#ud) [`#Openloop`](#openloop) [`#gosteps`](#gosteps) [`#stepinterval`](#stepinterval) [`#microstep`](#microstep) [`#HALL`](#hall) [`#Idle`](#idle) [`#Brake`](#brake) [`#Coast`](#coast) [`#Close`](#close)</div>

### `#Iq` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: current setpoint in mA</span><span class="fact">Enters **current** mode</span></div>

Current (torque) control with the given Iq setpoint.

**Response:** the measured Iq in mA

---

### `#Id` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: current setpoint in mA</span></div>

Sets the Id setpoint; normally left at 0. Also parameter 58.

**Response:** the measured Id in mA

---

### `#V` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: speed setpoint in encoder ticks/s</span><span class="fact">Enters **velocity** mode</span></div>

Velocity control with the given speed.

**Response:** the measured speed in ticks/s

---

### `#P` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: position setpoint in encoder ticks</span><span class="fact">Enters **position** mode</span></div>

Position control to the given position.

**Response:** the measured position in ticks

---

### `#PD` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: position setpoint in encoder ticks</span><span class="fact">Enters **PD** mode</span></div>

Impedance (PD) control around the given position with the gains KP and KD.

**Response:** the measured position in ticks

---

### `#PDV` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: speed setpoint in encoder ticks/s</span></div>

The speed setpoint of the PD loop.

**Response:** the PD speed setpoint

---

### `#PDI` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: current feedforward in mA</span></div>

The current feedforward of the PD loop.

**Response:** the PD current feedforward

---

### `#Uq` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: voltage in mV</span><span class="fact">Enters **voltage torque** mode</span></div>

Voltage-torque mode with the given q-axis voltage (no current loop).

**Response:** the Uq setpoint in mV

---

### `#Ud` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: voltage in mV</span></div>

The d-axis voltage used in voltage-torque mode; does not change the mode.

**Response:** the Ud setpoint in mV

---

### `#Openloop` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> float: electrical speed in rad/s</span><span class="fact">Enters **open loop** mode</span></div>

Spins the motor open loop, as a plain stepper, with the voltage set by Openv. The voltage is not current-controlled and Ilim does not apply: see Open-loop stepping on Control modes.

**Response:** the open-loop speed

---

### `#gosteps` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: number of microsteps (sign = direction)</span><span class="fact">Enters **open-loop steps** mode</span></div>

Moves the given number of microsteps open loop, one every stepinterval, at the voltage set by Openv, then goes to idle. With microstep 16, 16 steps are one electrical cycle: four full steps, 7.2° on a 1.8° motor.

**Response:** `Moving for N steps`

---

### `#stepinterval` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: step time in µs</span></div>

The time between two microsteps of gosteps, 1000 µs by default. It is rounded down to whole control cycles of 160 µs, and is 160 µs at the least.

**Response:** the step interval

---

### `#microstep` 

<div class="cmd-facts" markdown><span class="fact">Set/Get</span><span class="fact"><span class="k">Argument</span> int: microsteps per electrical cycle</span></div>

The microsteps gosteps makes per electrical cycle (four full steps), 16 by default.

**Response:** the microstep setting

---

### `#HALL` 

<div class="cmd-facts" markdown><span class="fact">Action</span><span class="fact">Enters **HALL** mode</span></div>

Homing against the sensor on ADDITIONAL2 at 3000 ticks/s, triggered when the pin is low. It holds while the pin stays low and spins on when the pin goes high again (see Send_data_pack_HALL for the CAN form with a chosen speed and trigger).

**Response:** `HALL`

---

### `#Idle` 

<div class="cmd-facts" markdown><span class="fact">Get</span></div>

Goes to idle; the motor coasts or brakes as set by Brake / Coast.

**Response:** `Idle`

---

### `#Brake` 

<div class="cmd-facts" markdown><span class="fact">Action</span><span class="fact">Enters **idle** mode</span></div>

Goes to idle with the motor braking (phases shorted); also the idle behaviour from then on. Not kept by Save: the driver brakes at every power-up.

**Response:** `Brake 1`

---

### `#Coast` 

<div class="cmd-facts" markdown><span class="fact">Action</span><span class="fact">Enters **idle** mode</span></div>

Goes to idle with the motor coasting (phases open); also the idle behaviour until the next power-up, which brakes again. Not kept by Save.

**Response:** `Coast 0`

---

### `#Close` 

<div class="cmd-facts" markdown><span class="fact">Action</span><span class="fact">Enters **idle** mode</span></div>

Leaves open loop and goes back to closed-loop idle.

**Response:** nothing

---
