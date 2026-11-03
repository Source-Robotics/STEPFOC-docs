# Motion

| Command | Kind | Argument | What it does | Response |
|---|---|---|---|---|
| `#Iq` | Set/Get | float: current setpoint in mA | Current (torque) control with the given Iq setpoint. Enters **current** mode. | the measured Iq in mA |
| `#Id` | Set/Get | float: current setpoint in mA | Sets the Id setpoint; normally left at 0. | the measured Id in mA |
| `#V` | Set/Get | int: speed setpoint in encoder ticks/s | Velocity control with the given speed. Enters **velocity** mode. | the measured speed in ticks/s |
| `#Uq` | Set/Get | int: voltage in mV | Voltage-torque mode with the given q-axis voltage (no current loop). Enters **voltage torque** mode. | the Uq setpoint in mV |
| `#Ud` | Set/Get | int: voltage in mV | The d-axis voltage used in voltage-torque mode; does not change the mode. | the Ud setpoint in mV |
| `#Brake` | Action |  | Goes to idle with the motor braking (phases shorted); also the idle behaviour from then on. Not kept by Save: the driver brakes at every power-up. Enters **idle** mode. | `Brake 1` |
| `#HALL` | Action |  | Homing against the sensor on ADDITIONAL2 at 3000 ticks/s, triggered when the pin is low. It holds while the pin stays low and spins on when the pin goes high again (see Send_data_pack_HALL for the CAN form with a chosen speed and trigger). Enters **HALL** mode. | `HALL` |
| `#Coast` | Action |  | Goes to idle with the motor coasting (phases open); also the idle behaviour until the next power-up, which brakes again. Not kept by Save. Enters **idle** mode. | `Coast 0` |
| `#P` | Set/Get | int: position setpoint in encoder ticks | Position control to the given position. Enters **position** mode. | the measured position in ticks |
| `#PD` | Set/Get | int: position setpoint in encoder ticks | Impedance (PD) control around the given position with the gains KP and KD. Enters **PD** mode. | the measured position in ticks |
| `#PDV` | Set/Get | int: speed setpoint in encoder ticks/s | The speed setpoint of the PD loop. | the PD speed setpoint |
| `#PDI` | Set/Get | int: current feedforward in mA | The current feedforward of the PD loop. | the PD current feedforward |
| `#Idle` | Action |  | Goes to idle; the motor coasts or brakes as set by Brake / Coast. Enters **idle** mode. | `Idle` |
| `#Close` | Action |  | Leaves open loop and goes back to closed-loop idle. Enters **idle** mode. | nothing |
| `#microstep` | Set/Get | int: microsteps per electrical cycle | The microsteps gosteps makes per electrical cycle (four full steps), 16 by default. | the microstep setting |
| `#stepinterval` | Set/Get | int: step time in µs | The time between two microsteps of gosteps, 1000 µs by default. It is rounded down to whole control cycles of 160 µs, and is 160 µs at the least. | the step interval |
| `#gosteps` | Set/Get | int: number of microsteps (sign = direction) | Moves the given number of microsteps open loop, one every stepinterval, at the voltage set by Openv, then goes to idle. With microstep 16, 16 steps are one electrical cycle: four full steps, 7.2° on a 1.8° motor. Enters **open-loop steps** mode. | `Moving for N steps` |
| `#Openloop` | Set/Get | float: electrical speed in rad/s | Spins the motor open loop, as a plain stepper, with the voltage set by Openv. The voltage is not current-controlled and Ilim does not apply: see Open-loop stepping on Control modes. Enters **open loop** mode. | the open-loop speed |
