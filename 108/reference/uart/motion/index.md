# Motion

| Command | Kind | Argument | What it does | Response |
|---|---|---|---|---|
| `#Iq` | Set/Get | float: current setpoint in mA | Current (torque) control with the given Iq setpoint. Enters **current** mode. | the measured Iq in mA |
| `#Id` | Set/Get | float: current setpoint in mA | Sets the Id setpoint; normally left at 0. | the measured Id in mA |
| `#V` | Set/Get | int: speed setpoint in encoder ticks/s | Velocity control with the given speed. Enters **velocity** mode. | the measured speed in ticks/s |
| `#Uq` | Set/Get | int: voltage in mV | Voltage-torque mode with the given q-axis voltage (no current loop). Enters **voltage torque** mode. | the Uq setpoint in mV |
| `#Ud` | Set/Get | int: voltage in mV | The d-axis voltage used in voltage-torque mode; does not change the mode. Enters **voltage torque** mode. | the Ud setpoint in mV |
| `#Brake` | Action |  | Goes to idle with the motor braking (phases shorted); also the idle behaviour from then on. Enters **idle** mode. | `Brake 1` |
| `#HALL` | Action |  | Homing against the sensor on ADDITIONAL2 at 3000 ticks/s (see Send_data_pack_HALL for the CAN form with a chosen speed and trigger). Enters **HALL** mode. | `HALL` |
| `#Coast` | Action |  | Goes to idle with the motor coasting (phases open); also the idle behaviour from then on. Enters **idle** mode. | `Coast 0` |
| `#P` | Set/Get | int: position setpoint in encoder ticks | Position control to the given position. Enters **position** mode. | the measured position in ticks |
| `#PD` | Set/Get | int: position setpoint in encoder ticks | Impedance (PD) control around the given position with the gains KP and KD. Enters **PD** mode. | the measured position in ticks |
| `#PDV` | Set/Get | int: speed setpoint in encoder ticks/s | The speed setpoint of the PD loop. | the PD speed setpoint |
| `#PDI` | Set/Get | int: current feedforward in mA | The current feedforward of the PD loop. | the PD current feedforward |
| `#Idle` | Action |  | Goes to idle; the motor coasts or brakes as set by Brake / Coast. Enters **idle** mode. | `Idle` |
| `#Close` | Action |  | Leaves open loop and goes back to closed-loop idle. Enters **idle** mode. | nothing |
| `#microstep` | Set/Get | int: microsteps per full step | The microstepping used by gosteps. | the microstep setting |
| `#stepinterval` | Set/Get | int: step time | The time between steps for gosteps. | the step interval |
| `#gosteps` | Set/Get | int: number of steps (sign = direction) | Moves the given number of steps open loop, with the timing of stepinterval and microstep. Enters **open-loop steps** mode. | `Moving for N steps` |
| `#Openloop` | Set/Get | float: electrical speed | Spins the motor open loop, as a plain stepper, with the voltage set by Openv. Enters **open loop** mode. | the open-loop speed |
