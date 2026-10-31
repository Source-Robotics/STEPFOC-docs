# Control modes

The driver is always in one control mode. A command that carries a setpoint switches to the mode that uses it;
`#Idle` or Send_Idle switches back to idle. The driver refuses the closed-loop modes while it is not calibrated or
while an error is active.

```mermaid
stateDiagram-v2
    [*] --> NotCalibrated: power-up, no saved calibration
    [*] --> Idle: power-up, saved calibration
    NotCalibrated --> Calibration: #Cal
    Calibration --> Idle: success, #Save
    Calibration --> NotCalibrated: a test fails
    Idle --> ControlMode: a setpoint
    ControlMode --> Idle: #Idle, Send_Idle
    ControlMode --> Error: a fault
    Idle --> Error: a fault
    Error --> Idle: #Clear, cause gone
```

A setpoint is `#P`, `#V`, `#Iq`, `#PD` or a CAN motion frame, and a new setpoint switches the mode without
passing through idle; a fault is any of the errors on [Errors and recovery](https://docs.source-robotics.com/STEPFOC-docs/108/06-operation/errors/).

| ControlMode | What the motor does | Entered by | Setpoint unit |
|---|---|---|---|
| Idle | nothing: coasts (phases open) or brakes (phases shorted), as set by `#Brake` / `#Coast` or Send_Settings | `#Idle`, Send_Idle, `#Clear`, errors | — |
| Position | holds and moves to a position with the cascade of position, velocity and current loops | `#P`, Send_data_pack_1 (8 bytes) | encoder ticks |
| Velocity | turns at a speed with the velocity and current loops | `#V`, Send_data_pack_1 (5 bytes) | encoder ticks/s |
| Current (torque) | applies a current, so a torque, with the current loop alone | `#Iq`, Send_data_pack_1 (2 bytes) | mA |
| PD (impedance) | behaves like a spring and a damper around a position, with `KP` and `KD` | `#PD`, Send_data_pack_PD | encoder ticks |
| Voltage torque | applies a voltage on the q axis directly, without the current loop | `#Uq` | mV |
| Open loop | steps the motor like a plain stepper driver, without the encoder | `#Openloop` (continuous), `#gosteps` (a number of steps) | electrical speed; steps |
| HALL | spins until a sensor on ADDITIONAL2 triggers, then holds the position reached | `#HALL`, Send_data_pack_HALL | encoder ticks/s |
| Gripper | runs the gripper state machine: move to a jaw position with a speed and a current limit | `#Grippos`, Send_gripper_data_pack (with `#Gripper 1`) | 0 to 255 |
| Calibration | the calibration routine, and the angle-offset step alone | `#Cal`, `#Calangle`, `#Gripcal` | — |

## Units

- **Position** is in encoder ticks: 16384 per revolution of the motor shaft, counting up without limit over
  several revolutions. Positive is counter-clockwise seen from the magnet (the back of the motor).
- **Speed** is in encoder ticks per second: 16384 is one revolution per second, 60 rpm.
- **Current** is in mA. Torque is current times the motor's Kt, which calibration finds.
- **Feedforward**: the 8-byte motion frame carries a speed and a current feedforward beside the position, the
  5-byte one a current feedforward beside the speed. They are added after the loops, so a host that knows the
  trajectory can command it directly and leave the loops to correct the rest. Send 0 when you do not use them.

## Try it

<div class="calc" data-ticks-per-rev="16384" data-max-electrical-hz="600" markdown="0">
  <div class="calc__row calc__row--inline">
    <label for="uc-ticks">Ticks (a position, or a speed per second)</label>
    <input id="uc-ticks" type="number" name="ticks" step="1" value="16384">
    <label for="uc-pp">Pole pairs</label>
    <select id="uc-pp" name="pp">
      <option value="50" selected>50 (1.8° stepper)</option>
      <option value="75">75 (1.2°)</option>
      <option value="100">100 (0.9°)</option>
      <option value="125">125 (0.72°)</option>
    </select>
  </div>
  <p class="calc__result">As a position: <strong data-out="turns">1.000</strong> turns, <strong data-out="deg">360.0°</strong> · as a speed: <strong data-out="rpm">60</strong> rpm · the practical maximum for <span data-out="ppout">50</span> pole pairs is about <strong data-out="maxrpm">720</strong> rpm</p>
  <div class="calc__row calc__row--inline">
    <label for="uc-kt">Kt in Nm/A (what #Kt prints)</label>
    <input id="uc-kt" type="number" name="kt" step="0.01" min="0" value="0.21">
    <label for="uc-ma">Current in mA</label>
    <input id="uc-ma" type="number" name="ma" step="10" value="1000">
  </div>
  <p class="calc__result">Torque: <strong data-out="nm">0.21 Nm</strong>, <strong data-out="ncm">21 N·cm</strong></p>
</div>

The units of this page, with your numbers: 16384 encoder ticks per turn, the practical speed limit from the
electrical frequency the control loop can follow ([Ratings and limits](https://docs.source-robotics.com/STEPFOC-docs/108/03-technical-data/ratings/)), and
the torque as Kt times the current.

## Positive rotation

<figure markdown="span">
  ![Positive rotation](https://docs.source-robotics.com/STEPFOC-docs/108/assets/STEPFOC_ORIENTATION.webp){ width="700" }
  <figcaption>Figure 15: Positive rotation is counter-clockwise looking at the encoder magnet. A positive current turns the motor that way, a positive speed too, and the position grows.</figcaption>
</figure>

## Which mode am I in?

`#Mode` prints the mode. Its text for the voltage-torque mode reads `Gripper mode` in this firmware release (a
leftover label); `#Info` and the behaviour of the motor are the reliable check.
