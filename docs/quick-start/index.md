# Quick start

From the box to a calibrated motor that follows commands, in four parts. The quickest way through is
[Motor GUI](https://motorgui.com/) in the browser; every step also shows the terminal commands.

!!! danger "Read first"
    Reversed supply polarity, a daisy-chain cable the wrong way round, or 5 V on the UART port destroys the driver.
    The motor turns during calibration. The [Safety](../02-safety.md) chapter is two minutes long.

## Before you start

You start from the box: a driver, a motor and the parts below. The wiring needs a multimeter and a soldering iron.

Nothing else is assumed: no experience with motor drivers, a terminal or a program.

## The four parts

| Part | What you do | What you end with |
|---|---|---|
| [1. Fit the motor](1-motor.md) | Fit the magnet, mount the board on the motor, solder the coils | A driver on its motor, wired |
| [2. Connect](2-connect.md) | Connect the supply and the PC, open Motor GUI or a terminal | A driver that talks to your PC |
| [3. Calibrate](3-calibrate.md) | Restore the defaults, enter the motor's values, calibrate, set the current limit, save | A calibrated driver that keeps its settings |
| [4. First moves](4-first-moves.md) | Turn the motor at a speed, move it to a position, stop it | A motor that follows commands |

Each step links the page that explains it. Follow the link when a step is not clear or something fails.

## What you need

| | Where to get it |
|---|---|
| **STEPFOC driver** | [single driver](https://source-robotics.com/products/STEPFOC-stepper-controller) or the [starter kit](https://source-robotics.com/products/STEPFOC-starter-kit), which has everything below except the motor and the supply |
| **A bipolar stepper motor** with a rear shaft: NEMA 17, 1 to 5 Ω per coil, 3 A or less | the [tested motors](../03-technical-data/tested-motors.md) are safe choices |
| **The encoder magnet**, diametrically magnetised; the stock one is 6 × 2.5 mm, another thickness is fine if it gives the 1 mm gap | [magnet](https://source-robotics.com/products/6x2-5mm-diametrical-neodymium-magnet) |
| **A spacer** for your motor length and four longer M3 screws | printable spacers in [Stepper motor accessories](https://github.com/Source-Robotics/STEPFOC-stepper-controller/tree/main/STEP%20files/Stepper%20motor%20accessories) |
| **USB-to-serial adapter**, 3.3 V, and its cable | [serial adapter](https://source-robotics.com/products/usb-to-serial-adapter), [UART cable](https://source-robotics.com/products/uart-cable) |
| **Power cable** | [power cable](https://source-robotics.com/products/spectral-micro-power-cable) |
| **A 12 to 29 V supply**, 24 V recommended | a bench supply with a current limit is the safest start |
| For CAN later: **CANvas USB-to-CAN adapter** and a **CAN cable** | [CAN adapter](https://source-robotics.com/products/canvas-usb-to-can-adapter), [CAN cable](https://source-robotics.com/products/spectral-micro-can-cable) |
| Optional: **100 kΩ NTC thermistor** for motor temperature protection | [thermistor](https://source-robotics.com/products/100k-ntc-thermistor) |
| **Software**: Motor GUI in Chrome or Edge, or a serial terminal | [motorgui.com](https://motorgui.com/); PuTTY, the PlatformIO monitor or the Arduino serial monitor |

More: [What you need](../01-overview/what-you-need.md).
