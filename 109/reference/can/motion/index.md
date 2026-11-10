# Motion

The commands that move the motor and the frames that come back.

### Send_data_pack_1

<div class="cmd-facts" markdown><span class="fact">ID 2</span><span class="fact">host → driver</span><span class="fact">2 or 5 or 8 bytes</span><span class="fact">Python: `Send_data_pack_1()`</span></div>

The motion command. Its length decides the control mode the driver enters: 8 bytes command a position with a speed and a current feedforward, 5 bytes a speed with a current feedforward, 2 bytes a current. Send 0 for a feedforward you do not use. A frame of any other length is ignored (the driver flags it as a wrong data length) but still answered.

**8 bytes** — position setpoint with speed and current feedforward (position mode)

| Byte | Bit | Field | Type | Meaning |
|---|---|---|---|---|
| 0-2 |  | Position setpoint | signed 24-bit | encoder ticks |
| 3-5 |  | Speed feedforward | signed 24-bit | encoder ticks/s |
| 6-7 |  | Current feedforward | signed 16-bit | mA |

**5 bytes** — speed setpoint with current feedforward (velocity mode)

| Byte | Bit | Field | Type | Meaning |
|---|---|---|---|---|
| 0-2 |  | Speed setpoint | signed 24-bit | encoder ticks/s |
| 3-4 |  | Current feedforward | signed 16-bit | mA |

**2 bytes** — current setpoint (current mode)

| Byte | Bit | Field | Type | Meaning |
|---|---|---|---|---|
| 0-1 |  | Current setpoint | signed 16-bit | mA |

The driver answers with **Respond_data_pack_1**.

Every form resets the watchdog. With `Rstint` set, the integral accumulators are cleared on each new setpoint. From firmware 109 a position or speed frame that follows another mode (idle, current, PD, a watchdog trip) starts the velocity integral from zero, so a release from a wound-up mode does not kick; one that follows position or velocity mode keeps it. The new setpoint and the mode change reach the control loop together.

---

### Send_data_pack_PD

<div class="cmd-facts" markdown><span class="fact">ID 4</span><span class="fact">host → driver</span><span class="fact">8 bytes</span><span class="fact">Python: `Send_data_pack_PD()`</span></div>

Puts the driver in impedance (PD) mode and sets the position, speed and current feedforward of the PD loop, whose gains are KP and KD (Send_PD_Gains).

**8 bytes**

| Byte | Bit | Field | Type | Meaning |
|---|---|---|---|---|
| 0-2 |  | Position setpoint | signed 24-bit | encoder ticks |
| 3-5 |  | Speed setpoint | signed 24-bit | encoder ticks/s |
| 6-7 |  | Current feedforward | signed 16-bit | mA |

The driver answers with **Respond_data_pack_1**.

Firmware 106 and older wrote the speed into the feedforward instead of the PD loop's speed setpoint, so the speed term had no effect; 107 fixed it.

---

### Send_data_pack_HALL

<div class="cmd-facts" markdown><span class="fact">ID 31</span><span class="fact">host → driver</span><span class="fact">4 bytes</span><span class="fact">Python: `Send_data_pack_HALL()`</span></div>

Homing against a sensor: the driver spins at the given speed until the input on the ADDITIONAL2 pin shows the trigger condition, then latches the position it reached as its position setpoint and holds it. With a level trigger (0 or 1) it holds only while the pin stays at that level: when the pin changes back, the driver spins on again until the level returns. The edge trigger (2) holds after the first edge. Sending the command again while the driver is already in HALL mode does not re-arm it; leave the mode first.

**4 bytes**

| Byte | Bit | Field | Type | Meaning |
|---|---|---|---|---|
| 0-2 |  | Speed | signed 24-bit | encoder ticks/s; the sign gives the direction |
| 3 |  | Trigger | unsigned 8-bit | 0 = trigger when the pin is low, 1 = when it is high, 2 = on any edge |

The driver answers with **Respond_data_hall**.

Firmware 103 read only bit 7 of byte 3 (0 or 1); the edge trigger (2) came later.

---

### Respond_data_pack_1

<div class="cmd-facts" markdown><span class="fact">ID 3</span><span class="fact">driver → host</span><span class="fact">8 bytes</span></div>

The driver's answer to Send_data_pack_1 and Send_data_pack_PD: where the motor is, how fast it turns and the current it draws. The Python library stores them as `position`, `speed` and `current`.

**The frame** (8 bytes)

| Byte | Bit | Field | Type | Meaning |
|---|---|---|---|---|
| 0-2 |  | position | signed 24-bit | encoder ticks |
| 3-5 |  | speed | signed 24-bit | encoder ticks/s |
| 6-7 |  | current | signed 16-bit | Iq in mA |

---

### Respond_data_hall

<div class="cmd-facts" markdown><span class="fact">ID 32</span><span class="fact">driver → host</span><span class="fact">4 bytes</span></div>

The driver's answer to Send_data_pack_HALL: the position and the state of the sensor input. Python attributes: `position`, `HALL_trigger`, `additional_pin2`, `hall_index`.

**The frame** (4 bytes)

| Byte | Bit | Field | Type | Meaning |
|---|---|---|---|---|
| 0-2 |  | position | signed 24-bit | encoder ticks |
| 3 | 7 | HALL_trigger | bit | 1 while the driver waits for the trigger (with a level trigger, also again after the pin left the level), 0 while it holds |
| 3 | 6 | additional_pin2 | bit | the raw level of the ADDITIONAL2 pin |
| 3 | 5 | hall_index | bit | 1 once the trigger has been seen (latched) |

---

### Send_data_pack_2

<div class="cmd-facts" markdown><span class="fact">ID 6</span><span class="fact">host → driver</span><span class="fact">not implemented</span></div>

Reserved. The firmware has no handler for this ID and the Python library's call does nothing.

---

### Send_data_pack_3

<div class="cmd-facts" markdown><span class="fact">ID 8</span><span class="fact">host → driver</span><span class="fact">not implemented</span></div>

Reserved. The firmware has no handler for this ID and the Python library's call does nothing.

---

### Respond_data_pack_2

<div class="cmd-facts" markdown><span class="fact">ID 5</span><span class="fact">driver → host</span><span class="fact">0 bytes</span></div>

Reserved; the driver never sends it.

---

### Respond_data_pack_3

<div class="cmd-facts" markdown><span class="fact">ID 7</span><span class="fact">driver → host</span><span class="fact">0 bytes</span></div>

Reserved; the driver never sends it.

---

### Send_Iq

<div class="cmd-facts" markdown><span class="fact">ID 21</span><span class="fact">host → driver</span><span class="fact">not implemented</span></div>

Reserved; the firmware has no handler for this ID. Use the 2-byte form of Send_data_pack_1 for a current setpoint.

---
