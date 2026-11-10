# Defaults

The settings of the firmware at the release this site describes: their start values in `common.h`, and what
`EEPROM.cpp` does with each.

- **Start value**: the value in `common.h`. A setting the EEPROM does not keep starts from it at every power-up. A
  kept setting is replaced at power-up by the value in the EEPROM, so its start value is only seen before that.
- **After `#Default`**: what `#Default` writes to the EEPROM and loads; — means `#Default` does not change it.
- **Kept by `#Save`**: whether `#Save` (Send_Save_config) stores it, so that it survives a power cycle.

Internal state (error flags, counters, calibration steps, scratch variables) is left out; the error flags are in
[Errors and LED states](https://docs.source-robotics.com/STEPFOC-docs/109/reference/errors/). A name after a value, such as `160 (CURRENT_BANDWIDTH_DEFAULT)`, is the
constant in `constants.h` the value comes from. `existing_id` for the CAN ID means that `#Default` keeps a valid
stored ID (0 when none is stored). The settings of firmware 109 that are parameters, the anti-cogging and the
encoder table among them, are in the [parameter table](https://docs.source-robotics.com/STEPFOC-docs/109/reference/can/parameters/#every-parameter) with their defaults.

| Variable | Start value | After `#Default` | Kept by `#Save` | Firmware comment |
|---|---|---|---|---|
| `SERIAL_NUMBER` | 1 | 111 in the EEPROM, not read back | written, not read back |  |
| `HARDWARE_VERSION` | 1 | 1 | yes | Version of the Spectral BLDC driver PCB |
| `BATCH_DATE` | 1 | 125 | yes | Date the batch was produced |
| `SOFTWARE_VERSION` | 1 | 109 | no: set by the firmware | Software release |
| `I_AM_GRIPPER` | 1 | 0 | yes | Is motor controller gripper (1) or not (0) |
| `LED_ON_OFF` | 1 | 1 | yes | Use LED for status indication |
| `theta_offset` | 0.0f | 0 | yes | will be determined at calibration |
| `pole_pairs` | 50 | 0 | yes | Number of pole pairs of your Stepper motor |
| `current_control_bandwidth` | 160 (CURRENT_BANDWIDTH_DEFAULT) | — | no | Hz: the current PI gains come from R, L |
| `DIR_` | 1 | 0 | yes | When looking at the magnetic encoder counter-clockwise is POSITIVE rotation. |
| `Phase_order` | 2 | 0 | yes |  |
| `commutation_dir` | 1 | 1 | yes | +1 or -1, auto-detected at calibration so +Iq/+velocity/+rotation map to +encoder rotation |
| `Thermistor_on_off` | 0 | 0 | yes | Are we taking termistor mesurements? 0 is off, 1 is on |
| `Resistance` | 0 | 0 | yes | Resistance of SINGLE PHASE of your BLDC motor |
| `Total_Resistance` | 0 | 0 | yes | = 2 * Resistance + 2 * R_sense + 2 *Rdson |
| `Inductance` | 0 | 0 | yes | Inductance of SINGLE PHASE of your BLDC motor |
| `Kt` | 0 | 0 | yes | Torque constant of your BLDC motor |
| `flux_linkage` | 0 | 0 | yes | Flux linkage of your BLDC motor |
| `KV` | 0 | 0 | yes |  |
| `Max_temperature` | 75 | 75 | yes | Max temperature in degrees |
| `Min_temperature` | -20 | — | no | Min temperature in degrees |
| `Max_Vbus` | 29500 | 29000 | yes | Max vbus voltage in mV |
| `Min_Vbus` | 9000 | — | no | Min vbus voltage in mV |
| `watchdog_time_ms` | 0 | 0 | yes |  |
| `watchdog_action` | 0 | 0 | yes | 0 legacy, 1 hold, 2 brake, 3 coast, 4 descend (watchdog_action.h) |
| `wd_fallback_time_ms` | 2000 | 2000 | yes | how long hold/descend may run before the after-action |
| `wd_fallback_current` | 0 | 0 | yes | mA, descend: the current applied (signed) |
| `wd_fallback_speed` | 1000 | 1000 | yes | ticks/s, descend: the speed cap in either direction |
| `wd_after_action` | 0 | 0 (WD_ACTION_LEGACY) | yes | after hold/descend: 0 legacy, 2 brake, 3 coast |
| `calibration_id` | 0 | 0 in the EEPROM, not read back | written, not read back | parameter 87: new at every successful calibration |
| `tool_id` | 0 | 0 | yes | what the drive is built into: 0 none, 1 SSG-48, 11-33 MSG, 200-254 custom |
| `board_product` | 0 | 0 | yes | product lock stamp in block 2: 1 STEPFOC, 2 Spectral, 0 none |
| `sense1_offset` | 0 | — | no | current-sense zero of channel 1, ADC counts from 2048 (start-up) |
| `sense2_offset` | 0 | — | no | current-sense zero of channel 2 |
| `comm_delay_us` | 166 (COMM_DELAY_DEFAULT_US) | — | no | parameter 64: commutation delay compensation, us |
| `input_filter_hz` | 0 | — | no | parameter 74: the position input filter, Hz (0 = off) |
| `vel_int_deadband` | 0 | — | no | parameter 75: the velocity integral's deadband, ticks (0 = off) |
| `sound_limit_mv` | 2000 (SOUND_LIMIT_DEFAULT_MV) | — | no | parameter 81: the sound's voltage at most (batch 22) |
| `sound_axis` | 1 | — | no | parameter 82: 1 the q axis (default: much louder on the bench), 0 the d axis |
| `fast_trig` | 0 | — | no | parameter 65: 1 the transforms' sin/cos from the integer table (it was |
| `speed_estimator` | 2 (SPEED_ESTIMATOR_DEFAULT) | — | no | parameter 50 |
| `speed_pll_bandwidth` | 60 (SPEED_PLL_BANDWIDTH_DEFAULT) | — | no | parameter 51, Hz |
| `Heartbeat_rate_ms` | 0 | 0 | yes | Motor controller will send data every Heartbeat_rate_ms |
| `Calibrated` | 1 | 0 | yes | 0 if motor is not calibrated, 1 if it is calibrated |
| `Resistance_calc_voltage` | 1000 | — | no | Voltage used to calculate resistance //1000 |
| `Calibration_power` | 12 | — | no | Max power that can dissipate during inductance test. |
| `Open_loop_voltage` | 5000 | — | no | Voltage to use when spinning the motor open loop. In mV |
| `Open_loop_speed` | 20.0 | — | no | Speed to be used when spinning the motor open loop. In RAD/s |
| `Phase_voltage` | 5000 | — | no | Max voltage to be used during Kv calculation |
| `cyclic_period` | 0 | — | no | We send messages every cyclic_period |
| `CAN_ID` | 0 | existing_id | yes | CAN id of THIS motor driver! No 2 motor drivers can share the same ID. |
| `brake_coast` | 1 | — | no | 1 is brake 0 is coast |
| `trigger_value` | 0 | — | no | 0=low level, 1=high level, 2=any edge |
| `calibration_offset_current` | 500 | — | no |  |
| `microstep` | 16 | — | no |  |
| `gosteps` | 0 | — | no |  |
| `step_interval` | 1000 | — | no | step interval in microseconds |
| `Voltage_limit` | 6000 | 6000 | yes | Voltage limit for Ud and Uq voltages. If 0 value of controller.VBUS_mV will be used |
| `Reset_integral_accumulator` | 0 | 0 | yes |  |
| `Kp_p` | 5 | 5 | yes |  |
| `Position_setpoint` | 0 | — | no |  |
| `Kp_v` | 0.02 | 0.02 | yes | bench 2026-11-08: a bare NEMA 17 vibrates at 0.056 (speed PLL) or 0.04 |
| `Ki_v` | 0.001 | 0.001 | yes | bench 2026-11-08 (kiv_sweep.py, KPV 0.02): rings at 0.004; 0.001 halves the |
| `Velocity_setpoint` | 0 | — | no | -1.5 |
| `Velocity_limit` | 800000 | 800000 | yes | Clamp integrals to this  [TICKS/s] |
| `Velocity_limit_error` | 30000000 | — | no | [TICKS/s] ; Velocity when we will report error / For stepper speed runout is around 250 nfo000 |
| `Kp_id` | 7 | 7 | yes | motor1 |
| `Ki_id` | 3 | 3 | yes | motor1 |
| `Id_setpoint` | 0 | — | no |  |
| `Kp_iq` | 3 | 3 | yes | motor1 |
| `Ki_iq` | 0.3 | 0.3 | yes | motor1 |
| `Iq_current_limit` | 1700 | 1700 | yes |  |
| `Id_current_limit` | 0 | 0 | yes |  |
| `Feedforward_current` | 0 | — | no |  |
| `KD` | 0.0028 | 0.0028 | yes | [Nm*s/rad] |
| `KP` | 0.1400 | 0.1400 | yes | [Nm/rad] |
| `Uq_setpoint` | 0 | — | no |  |
| `Ud_setpoint` | 0 | — | no |  |
| `position_setpoint` | 0 | — | no |  |
| `speed_setpoint` | 50 | — | no |  |
| `current_setpoint` | 400 | — | no |  |
| `action_status` | 0 | — | no | -0 Stopped(or performing activation /automatic release). |
| `activated` | 0 | — | no |  |
| `release_direction` | 0 | — | no |  |
| `estop_status` | 0 | — | no |  |
