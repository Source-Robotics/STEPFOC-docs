<!-- One shared glossary, included by the Glossary page. Keep entries alphabetical. -->

**Activated**
:   A flag the driver keeps (`#Activate`, Send_gripper_data_pack). In gripper mode a move is carried out only while
    the gripper is activated.

**ADDITIONAL2**
:   A spare pin of the driver, usable as an analog input or a digital input/output. HALL mode homes the motor
    against a sensor wired to it.

**Angle offset** (theta offset)
:   The angle between the encoder's zero and the motor's electrical zero, found by calibration and stored. The
    driver needs it to place the current vector relative to the rotor.

**Back-EMF**
:   The voltage a turning motor generates in its own coils, proportional to speed. It opposes the supply, limits the
    top speed at a given voltage, and is what calibration measures to find KV, Kt and the flux linkage.

**Board ID**
:   The bootloader's own address, 0 to 13, stored in its configuration page. The firmware keeps it equal to the CAN
    node ID.

**Bootloader**
:   The program in the first 12 KB of the driver's flash on boards shipped with firmware 104 or newer. It starts the
    firmware, and loads a new firmware over UART or CAN. See [The bootloader](07-firmware/the-bootloader.md).

**Calibration**
:   The routine (`#Cal`) that checks the magnet and the supply, takes the motor's resistance, inductance and pole
    pairs, computes the current loop gains, spins the motor in open loop to learn the wiring, finds the angle offset
    and measures Kt, KV and the flux linkage. Its result is kept with `#Save`.

**CAN ID** (node ID)
:   The address of the driver on the CAN bus, 0 to 15. It occupies bits 10 to 7 of the 11-bit CAN frame identifier;
    the command ID occupies bits 6 to 1 and the error bit is bit 0.

**CANvas**
:   Source Robotics' USB-to-CAN adapter. It appears as a serial port and speaks slcan, which `python-can` and Motor
    GUI use.

**Command ID**
:   The number, 0 to 63, in bits 6 to 1 of a CAN frame identifier that says which message the frame carries. The
    Protocol reference lists every command ID.

**Commutation**
:   Placing the stator current so that it produces torque at the rotor's present angle. FOC does it continuously
    from the encoder angle and the angle offset; a conventional stepper driver does it blindly, step by step.

**Control mode**
:   What the driver is doing with the motor: idle, position, velocity, current, PD (impedance), voltage torque, open
    loop, HALL, gripper, or calibration. A command that carries a setpoint puts the driver in the matching mode.

**Current loop bandwidth** (`#Cbw`)
:   How fast the current loop follows a change of its setpoint, in Hz. Calibration computes the current loop gains
    from it and the motor's resistance and inductance; 500 Hz by default.

**Daisy chain**
:   Several drivers on one CAN bus and one supply, each driver's second CAN and power connector feeding the next.

**d-q frame**
:   The rotating frame of reference FOC works in: the q axis is at right angles to the rotor field and the current on
    it (Iq) produces torque; the d axis is along the field and its current (Id) produces none, so it is held at 0.

**Diametrical magnet**
:   A disc magnet whose poles are across its diameter, so the field turns with the shaft. The encoder needs this
    kind; an axially magnetised disc looks the same and does not work.

**EEPROM**
:   The non-volatile memory on the driver that holds the configuration and the calibration. `#Save` writes it,
    `#Default` restores the factory values.

**Encoder ticks**
:   The unit of position: the 14-bit magnetic encoder gives 16384 ticks per revolution of the motor shaft, counted
    over as many revolutions as the motor makes. Speed is in ticks per second.

**Error bit**
:   Bit 0 of every CAN frame identifier the driver sends: 1 while any error is active.

**Feedforward**
:   A term added to a loop's output from what is known in advance rather than from the error: the motion frames
    carry a speed and a current feedforward so a host that knows the trajectory can command it directly, leaving
    the loops to correct the rest.

**Field-oriented control** (FOC)
:   Controlling a motor by regulating the stator current as a vector in the rotor's frame, from a measurement of the
    rotor angle. On a stepper it replaces the fixed step currents with sinusoidal currents that follow the rotor,
    which gives smooth, quiet, efficient motion with no lost steps and a known position.

**Firmware release**
:   One build of the firmware, numbered 103, 104, 105, … and tagged `V103`, `V104`, … in the firmware repository.
    `#Info` prints the release a driver runs. This documentation describes one release; the version selector
    switches between them.

**Flux linkage**
:   The rotor's magnetic flux as seen by a coil, in weber; found by calibration from the back-EMF, together with
    KV and Kt.

**Gripper mode**
:   The driver running a gripper (`#Gripper 1`): jaw positions from 0 (open) to 255 (closed), a speed, a current
    limit that becomes the grip force, and object detection.

**HALL mode**
:   Homing against a sensor on ADDITIONAL2: the motor turns at a set speed until the sensor triggers, then holds
    the position reached.

**Heartbeat**
:   A frame (Respond_Heartbeat) the driver sends at a set interval so the host knows it is alive. Off by default.

**Iq, Id**
:   The two components of the motor current in the d-q frame: Iq produces torque, Id is normally held at 0. The
    current mode's setpoint and limit are Iq values.

**Impedance (PD) mode**
:   The control mode in which the driver behaves like a spring and a damper around a position setpoint, with the
    stiffness `KP` and the damping `KD`, plus a current feedforward.

**Kt, KV**
:   The motor's torque constant (torque per ampere) and velocity constant (speed per volt), found by calibration.
    Kt turns a current into an estimated torque; KV gives the top speed at a supply voltage.

**Microstepping**
:   Driving a stepper with intermediate current levels between full steps. Only the open-loop commands
    (`#gosteps`, `#microstep`) use it; under FOC the current follows the rotor continuously.

**Motor GUI**
:   Source Robotics' browser tool for the driver: tuning, plots and firmware updates over a serial or CAN adapter.

**Open loop**
:   Driving the motor as a plain stepper, without the encoder in the loop: `#Openloop`, `#gosteps`, and the
    open-loop spin of the calibration.

**Phase order**
:   How the stepper's two coils are connected to A+/A− and B+/B−. Firmware 105 and newer learns the wiring during
    calibration and compensates it; firmware 103 asks for the wires to be swapped when it is reversed.

**Pole pairs**
:   The number of electrical cycles per mechanical revolution: 50 for a 1.8° stepper, 100 for a 0.9° stepper. Set
    with `#PP` before calibration.

**Remote frame**
:   A CAN frame with the RTR bit set and no data: a request. The host asks for data with a remote frame under a
    command ID, and the driver answers with a data frame under the same ID.

**Spectral Micro**
:   Source Robotics' BLDC driver, on which STEPFOC is built: the same board, firmware and commands, for
    three-phase brushless motors.

**Step angle**
:   The angle of one full step of a stepper: 1.8° for the common 200-step motor, 0.9° for a 400-step motor. It
    sets the pole pairs: 360 ÷ (4 × step angle).

**Termination**
:   The 120 Ω resistor the first and the last node of a CAN bus need. The switch on the driver turns it on.

**Vbus**
:   The supply voltage at the driver, measured and printed in mV. Outside the limits the driver raises a Vbus
    error.

**Watchdog**
:   A timer the driver resets with every valid CAN frame it receives. When it is set (Send_Watchdog) and runs out,
    the driver reports a watchdog error and stops.
