# Gripper

| Command | Kind | Argument | What it does | Response |
|---|---|---|---|---|
| `#Gripper` | Set/Get | int: 0 or 1 | Whether this driver is a gripper. Save it; `#Default` clears it. | the flag |
| `#Gripcal` | Action |  | Starts the gripper calibration: the jaws find their end stops at 500 mA. It prints nothing when it ends; after about 24 s without both end stops it gives up, uncalibrated. Gripinfo shows the result. Enters **gripper calibration** mode. | `Gripper calibration!` |
| `#Gripinfo` | Get |  | Prints the gripper state: calibrated, activated, end stops, position, current. | the report |
| `#Gripstop` | Set/Get | int: 0 or 1 | The gripper E-stop bit. While it is 1 the driver raises the gripper E-stop error on every control cycle: set it to 0, then Clear. | the bit |
| `#Gripact` | Set/Get | int: 0 or 1 | The activate bit. | the bit |
| `#Gripcur` | Set/Get | int: current in mA | The current limit of gripper moves, 400 mA at power-up. The firmware does not clamp it, not even to the driver's 2800 mA; see the gripper manual for the safe range. | the setpoint |
| `#Gripvel` | Set/Get | int: 0 to 255 | The speed setpoint of gripper moves, 50 at power-up. | the setpoint |
| `#Grippos` | Set/Get | int: 0 (open) to 255 (closed) | The position setpoint; also activates the gripper, sets the action bit and goes to gripper mode. Enters **gripper** mode. | the current position |
