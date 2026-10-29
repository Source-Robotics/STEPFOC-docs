<!-- One shared glossary, included by the Glossary page. Keep entries alphabetical. -->

**Activated**
:   A flag the driver keeps (`#Activate`, `Send_gripper_data_pack`). In gripper mode a move is only carried out while
    the gripper is activated.

**Bootloader**
:   The small program in the first 12 KB of the driver's flash (boards shipped with firmware 104 or newer). It
    loads the firmware over UART or CAN, so the firmware can be updated without a programming adapter. See
    [Firmware](07-firmware/index.md).

**Calibration**
:   The routine (`#Cal`) that checks the magnet and the supply, takes the motor's resistance, inductance and pole
    pairs, spins the motor in open loop to check the phase wiring, and finds the angle offset and the motor
    constants. Its result is kept with `#Save`.

**CAN ID**
:   The node address of the driver on the CAN bus, 0 to 15. It occupies bits 10 to 7 of the 11-bit CAN frame ID;
    the command ID occupies bits 6 to 1 and the error bit is bit 0.

**Command ID**
:   The number, 0 to 63, that says which message a CAN frame carries. The Reference lists every command ID.

**Control mode**
:   What the driver is doing with the motor: idle, position, velocity, current, PD (impedance), open loop, voltage
    torque, gripper, HALL. A command that carries a setpoint puts the driver in the matching mode.

**Daisy chain**
:   Several drivers on one CAN bus and one power line, each driver's second connector feeding the next one.

**Encoder ticks**
:   The unit of position: the 14-bit magnetic encoder gives 16384 ticks per revolution of the motor shaft, counted
    over as many revolutions as the motor makes. Speed is in ticks per second.

**Error bit**
:   Bit 0 of every CAN frame ID the driver sends: 1 while any error is active.

**Firmware release**
:   One build of the firmware, numbered 103, 104, 105, ... and tagged `V103`, `V104`, ... in the firmware
    repository. `#Info` prints the release a driver runs. This documentation describes one release; the version
    selector switches between them.

**Heartbeat**
:   A frame (`Respond_Heartbeat`) the driver sends at a set interval so the host knows it is alive. Off by default.

**Iq, Id**
:   The two components of the motor current in the rotor frame: Iq produces torque, Id is normally held at 0.

**Impedance (PD) mode**
:   The control mode in which the driver behaves like a spring and damper around a position setpoint, with the
    gains `KP` and `KD`.

**Kt, KV**
:   The motor's torque constant and velocity constant, found by calibration and used to estimate torque.

**Open loop**
:   Driving the motor as a plain stepper, without the encoder in the loop (`#Openloop`, `#gosteps`, and one step of
    the calibration).

**Phase order**
:   Which way the stepper's two coils are connected to A+/A− and B+/B−. Firmware 105 and newer detects a reversed
    coil during calibration and compensates it; older firmware asks you to swap the wires.

**Pole pairs**
:   The number of electrical cycles per mechanical revolution: 50 for a 1.8° stepper, 100 for a 0.9° stepper. Set
    with `#PP` before calibration.

**Termination**
:   The 120 Ω resistor the first and the last node of a CAN bus need. The switch on the driver turns it on.

**Theta offset**
:   The angle between the encoder's zero and the motor's electrical zero, found by calibration.

**Watchdog**
:   A timer the driver resets with every valid CAN frame it receives. When it is set (`Send_Watchdog`) and runs out,
    the driver reports a watchdog error and stops.
