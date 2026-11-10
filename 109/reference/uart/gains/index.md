# Gains and limits

| Command | Kind | Argument | What it does | Response |
|---|---|---|---|---|
| `#Vlimit` | Set/Get | int: speed in encoder ticks/s | The speed limit: it clamps the speed setpoint of the velocity loop, and in position mode the speed the position loop asks for. The velocity integrator is clamped to the current limit (Ilim), not to this. From firmware 109 a negative number counts as its magnitude. | the current limit |
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
| `#Ilim` | Set/Get | int: current in mA | The Iq current limit, 1700 mA after #Default. Set it to the rated phase current of your motor; this command clamps it to 2800 mA and takes the magnitude of a negative number (from firmware 109 Send_Limits over CAN stops at 2800 mA too). Calibration uses 1600 mA for its steps and, from firmware 109, puts it back when it ends. | the current limit |
| `#Cbw` | Set/Get | float: bandwidth in Hz, 10 to 625 | The current loop bandwidth. From firmware 109 setting it computes Kpiq and Kiiq at once from R and L, the way calibration does, and prints them (the same as parameter 49); a value outside 10-625, or with R or L at 0, changes nothing. Not kept by Save: 160 Hz at every power-up, but the gains it set are kept. | the bandwidth, then `Kp_iq = …, Ki_iq = …` |
| `#Rstint` | Set/Get | int: 0 or 1 | Whether the integral accumulators are reset on every new setpoint. | the setting |
