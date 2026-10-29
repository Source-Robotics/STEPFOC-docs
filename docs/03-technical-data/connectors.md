# Connectors and pinout

<figure markdown="span">
  ![The connectors of the STEPFOC driver](../assets/STEPFOC_CONN.png){ width="900" }
  <figcaption>Figure 2: The connectors. The motor coils go to A+, A−, B+, B−; the supply to DC+ and DC−.</figcaption>
</figure>

| Connector | Pins | Type | Cable |
|---|---|---|---|
| Motor | A+, A−, B+, B− | solder pads | the motor's own leads, see [Wiring the stepper](../04-mounting/wiring.md) |
| Power, two of them | DC+, DC− | JST XH, 2 pins | [Power cable](https://source-robotics.com/products/spectral-micro-power-cable); the second connector feeds the next driver |
| CAN, two of them | CAN H, CAN L | JST ZH, 2 pins | [CAN cable](https://source-robotics.com/products/spectral-micro-can-cable); the second connector feeds the next driver |
| UART | 3.3 V, TX, RX, GND | JST SH, 4 pins | [UART cable](https://source-robotics.com/products/uart-cable) |
| Thermistor | NTC, NTC | JST SH, 2 pins | the 100 kΩ NTC from the shop or any 100 kΩ NTC |
| JTAG | 3.3 V, GND, SWDIO, SWCLK | 1.27 mm header | [Programming adapter](https://source-robotics.com/products/jtag-programming-adapter-1-27-pitch) |
| ADDITIONAL2 | signal, GND | pads | your sensor; the HALL homing mode reads this pin |
| STEP / DIR | STEP, DIR, GND, 24 V | header | hardware only: the firmware does not support a step/dir interface |

!!! danger "Polarity and orientation"
    DC+ to the positive supply, DC− to the negative; a cable the wrong way round destroys the driver. The daisy-chain
    cables have an orientation too: see [Power and the CAN daisy chain](../04-mounting/power-and-can.md).

!!! note
    - UART is TX to RX and RX to TX between the driver and the adapter.
    - The UART port and the ADDITIONAL2 pin are 3.3 V. 5 V on either destroys the board.
    - The thermistor pin has a 54.9 kΩ pull-down; the firmware's temperature table is for a 100 kΩ NTC.
    - The CAN termination switch is next to the CAN connectors; **ON** connects the 120 Ω resistor.
