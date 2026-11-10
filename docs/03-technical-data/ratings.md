# Ratings and limits

## Electrical

| | Value |
|---|---|
| Supply voltage | 12 to 29 V DC, 24 V typical |
| Vbus error limits (firmware) | below 9 V or above 29 V (`#Vmax`, 29000 mV after `#Default`) |
| Phase current, continuous | 1.5 A typical |
| Phase current, maximum | 2.8 A; needs good cooling and short bursts. `#Ilim` is clamped to 2800 mA, and from firmware 109 so is Send_Limits over CAN |
| Current limit, default | 1700 mA after `#Default`; calibration uses 1600 mA for its steps and, from firmware 109, puts the limit back |
| Power, maximum | 80 W |
| Power, idle | 0.3 W |
| PWM frequency | 25 kHz |
| Control loop frequency | 6250 Hz |
| Electrical frequency, maximum | 600 Hz |
| Current sensing | inline, both phases |
| Encoder | 14-bit magnetic, 16384 ticks per revolution, diametrical magnet 1 mm above the chip |
| UART | 3.3 V, 256000 baud by default (1 000 000 tested) |
| CAN | CAN 2.0, 1 Mbit/s, 11-bit identifiers, node IDs 0 to 13 (the bootloader reserves 14 and 15), 120 Ω termination by switch |
| Thermistor input | 100 kΩ NTC, 54.9 kΩ pull-down |
| ADDITIONAL2 | analog input or general-purpose input/output, 3.3 V |
| Driver stage protection | not monitored: the firmware reads no fault output of the driver stage, and its driver error flag stays 0 |

!!! warning "Polarity"
    Reversing the polarity on DC+ and DC− destroys the board.

## Thermal and environmental

| | Value |
|---|---|
| Operating temperature of the board | −20 to 130 °C |
| Motor temperature limit (firmware, with the thermistor) | 75 °C by default (`#Tlim`), −20 °C minimum |

## Mechanical

| | Value |
|---|---|
| Dimensions | 39 × 39 mm |
| Mass | 8 g |
| Mounting | the NEMA 17 pattern, 31 mm hole spacing; NEMA 23 motors with the NEMA 23 spacer, other frames with an adapter you make |

## Firmware limits

| | Value |
|---|---|
| Position | signed 24-bit over CAN (±8.4 million ticks, ±512 revolutions), 32-bit internally |
| Speed | signed 24-bit over CAN, encoder ticks per second |
| Current setpoint | signed 16-bit over CAN, mA |
| Pole pairs accepted by calibration | 50, 75, 100 or 125 |
| Configuration | kept in the EEPROM with `#Save` / `Send_Save_config` |

The defaults of every setting are listed in the [Defaults](../reference/defaults.md) reference.
