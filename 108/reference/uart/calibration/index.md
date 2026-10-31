# Calibration and motor parameters

| Command | Kind | Argument | What it does | Response |
|---|---|---|---|---|
| `#R` | Set/Get | float: resistance in Ω | The phase resistance of the motor (one coil). STEPFOC does not measure it; enter the datasheet value before Cal. | the current value |
| `#L` | Set/Get | float: inductance in H | The phase inductance of the motor (one coil); enter the datasheet value before Cal. | the current value |
| `#Kt` | Set/Get | float: Nm/A | The torque constant, found by calibration. | the current value |
| `#KV` | Set/Get | float: rpm/V | The velocity constant, found by calibration. | the current value |
| `#Flux` | Set/Get | float: Wb | The flux linkage, found by calibration. Not reachable over UART: the parser accepts `#flux` (lowercase) but the handler expects `Flux`, so neither spelling works. | the current value |
| `#Cal` | Action |  | Runs the calibration routine (see Motor parameters and calibration). Enter R, L and PP first. | the calibration log |
| `#Calangle` | Action |  | Runs only the angle-offset step of the calibration. Enters **angle-offset calibration** mode. | `Idle` when done |
| `#Offset` | Set/Get | float: angle in rad | The angle offset between encoder zero and electrical zero, found by calibration. | the current value |
| `#Iqoffset` | Set/Get | int: current in mA | The current used by the angle-offset search. | the current value |
| `#Magnet` | Get |  | Reads the encoder's magnet status. | `Magnet Good` or `Magnet Bad` |
| `#Dir` | Set/Get | int: 0 or 1 | The counting direction of the encoder (1 is the default). | the current value |
| `#Phase` | Get |  | Prints the phase order found by calibration. | `Phase order is: N` |
| `#Resv` | Set/Get | int: voltage in mV | The voltage calibration starts the resistance test at (not used by STEPFOC, which does not measure resistance). | the current value |
| `#Calpwr` | Set/Get | float: power in W | The power calibration may dissipate in the resistance and inductance tests (not used by STEPFOC). | the current value |
| `#Openv` | Set/Get | int: voltage in mV | The voltage of the open-loop spin, in calibration and with Openloop. | the current value |
| `#Opens` | Set/Get | float: electrical speed in rad/s | The speed of the open-loop spin in calibration. | the current value |
| `#Vp` | Set/Get | int: voltage in mV | The voltage of the phase-order search in calibration. | the current value |
| `#Calibrated` | Set/Get | int: 0 or 1 | The calibrated flag. `#Calibrated 1` clears a calibration error without calibrating; the motor may still be uncalibrated. | the flag |
| `#PP` | Set/Get | int: pole pairs | The motor's pole pairs: 50 for a 1.8° stepper, 75 for 1.2°, 100 for 0.9°, 125 for 0.72°. Calibration accepts only these values. | the current value |
