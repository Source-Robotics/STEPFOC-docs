# Gains and limits

| Command | Kind | Argument | What it does | Response |
|---|---|---|---|---|
| `#Vlimit` | Set/Get | int: speed in encoder ticks/s | The speed limit: it clamps the speed setpoint of the velocity loop, and in position mode the speed the position loop asks for. The velocity integrator is clamped to the current limit (Ilim), not to this. | the current limit |
| `#Vlim` | Set/Get | int: voltage in mV | The voltage limit of the current loops (Ud and Uq), 6000 mV by default. It keeps the loops of low-resistance steppers stable, and it also caps the top speed. 0, or a value above the supply voltage, means the supply voltage. | the current limit in mV |
| `#Kpp` | Set/Get | float: gain | Kp of the position loop. | the current value |
| `#KP` | Set/Get | float: gain | KP of the impedance (PD) loop. | the current value |
| `#KD` | Set/Get | float: gain | KD of the impedance (PD) loop. | the current value |
| `#Kpv` | Set/Get | float: gain | Kp of the velocity loop. | the current value |
| `#Kpiq` | Set/Get | float: gain | Kp of the Iq current loop; also sets Kpid. | the current value |
| `#Kpid` | Set/Get | float: gain | Kp of the Id current loop. | the current value |
| `#Kiv` | Set/Get | float: gain | Ki of the velocity loop. | the current value |
| `#Kiiq` | Set/Get | float: gain | Ki of the Iq current loop; also sets Kiid. | the current value |
| `#Kiid` | Set/Get | float: gain | Ki of the Id current loop. | the current value |
| `#Ilim` | Set/Get | int: current in mA | The Iq current limit, 1700 mA after #Default. Set it to the rated phase current of your motor; this command clamps it to 2800 mA (Send_Limits over CAN does not). Calibration sets it to 1600 mA: set it again after Cal. | the current limit |
| `#Cbw` | Set/Get | float: bandwidth in Hz | The current loop bandwidth calibration uses to compute Kpiq and Kiiq. Not kept by Save: 500 Hz at every power-up, so set it just before Cal. | the bandwidth |
| `#Rstint` | Set/Get | int: 0 or 1 | Whether the integral accumulators are reset on every new setpoint. | the setting |
