# Quick start

From the box to a calibrated motor that follows commands, on one page. The quickest way through is
[Motor GUI](https://motorgui.com/) in the browser; every step also shows the terminal commands, and ends with a
link to the chapter that explains it. Follow the link when a step is not clear or something fails.

!!! danger "Read first"
    Reversed supply polarity, a daisy-chain cable the wrong way round, or 5 V on the UART port destroys the driver.
    The motor turns during calibration. The [Safety](02-safety.md) chapter is two minutes long.

## 1. What you need

| | Where to get it |
|---|---|
| **STEPFOC driver** | [single driver](https://source-robotics.com/products/STEPFOC-stepper-controller) or the [starter kit](https://source-robotics.com/products/STEPFOC-starter-kit), which has everything below except the motor and the supply |
| **A bipolar stepper motor** with a rear shaft: NEMA 17, 1 to 5 Ω per coil, 3 A or less | the [tested motors](03-technical-data/tested-motors.md) are safe choices |
| **The encoder magnet**, diametrically magnetised; the stock one is 6 × 2.5 mm, another thickness is fine if it gives the 1 mm gap | [magnet](https://source-robotics.com/products/6x2-5mm-diametrical-neodymium-magnet) |
| **A spacer** for your motor length and four longer M3 screws | printable spacers in [Stepper motor accessories](https://github.com/Source-Robotics/STEPFOC-stepper-controller/tree/main/STEP%20files/Stepper%20motor%20accessories) |
| **USB-to-serial adapter**, 3.3 V, and its cable | [serial adapter](https://source-robotics.com/products/usb-to-serial-adapter), [UART cable](https://source-robotics.com/products/uart-cable) |
| **Power cable** | [power cable](https://source-robotics.com/products/spectral-micro-power-cable) |
| **A 12 to 29 V supply**, 24 V recommended | a bench supply with a current limit is the safest start |
| For CAN later: **CANvas USB-to-CAN adapter** and a **CAN cable** | [CAN adapter](https://source-robotics.com/products/canvas-usb-to-can-adapter), [CAN cable](https://source-robotics.com/products/spectral-micro-can-cable) |
| Optional: **100 kΩ NTC thermistor** for motor temperature protection | [thermistor](https://source-robotics.com/products/100k-ntc-thermistor) |
| **Software**: Motor GUI in Chrome or Edge, or a serial terminal | [motorgui.com](https://motorgui.com/); PuTTY, the PlatformIO monitor or the Arduino serial monitor |

Read in more detail: [What you need](01-overview/what-you-need.md).

## 2. Fit the magnet

Press the magnet onto the rear shaft, centred, and glue it. It must end up about **1 mm** above the encoder chip
in the middle of the board, and it must not be able to turn on the shaft. A magnet that slips is the usual cause of
a calibration that "succeeds" and a motor that then runs badly.

Read in more detail: [The encoder magnet](04-mounting/magnet.md).

## 3. Mount the board

Remove the motor's four rear screws, put the spacer on, the board on the spacer with the encoder chip towards the
magnet, and the longer screws in. Check the gap: 1 mm, not touching.

Read in more detail: [Mounting on the motor](04-mounting/mounting.md).

## 4. Wire the motor

Find the two coils with a multimeter (the two wires of a coil show a few ohms; wires of different coils show
nothing). Solder one coil to **A+ and A−**, the other to **B+ and B−**. Which coil is which, and which way round,
does not matter: calibration detects it.

Read in more detail: [Wiring the stepper](04-mounting/wiring.md).

## 5. Connect power and the PC

1. The supply to a power connector: **DC+ to positive, DC− to negative**. Check twice.
2. The serial adapter to the UART connector with the UART cable (TX to RX, RX to TX; 3.3 V only).
3. Power on. The LED turns on steadily: the driver is not calibrated yet, which it reports as an error state.

=== "Motor GUI"
    Open [motorgui.com](https://motorgui.com/) in Chrome or Edge, choose the serial connection and **Open port** on
    the adapter's port. The driver's identity and state appear: hardware and firmware version, serial number,
    *Not calibrated*, *No errors*. If nothing connects: the port, the cable's TX/RX, the browser (Web Serial needs
    a Chromium browser).

    Read in more detail: [Motor GUI](05-setup/motor-gui.md).

=== "Terminal"
    Open a terminal on the adapter's port, 256000 baud, line ending CR+LF, and type `#Info`. The driver prints its
    hardware and firmware version and the state of everything.

    Read in more detail: [The serial terminal](05-setup/terminal.md).

Read in more detail: [Power and the CAN daisy chain](04-mounting/power-and-can.md) ·
[Connectors and pinout](03-technical-data/connectors.md).

## 6. Enter the motor parameters

From the motor's datasheet, for **one coil**: the pole pairs (50 for a 1.8° motor, 100 for 0.9°), the phase
resistance in ohms, the phase inductance in henries (2.6 mH = 0.0026). STEPFOC does not measure these; calibration
fails on a value left at 0.

=== "Motor GUI"
    Enter *Pole pairs*, *Resistance* and *Inductance* in the motor settings and apply them.

=== "Terminal"
    ```
    #PP 50
    #R 1.1
    #L 0.0026
    ```

Read in more detail: [Motor parameters and calibration](05-setup/calibration.md).

## 7. Calibrate

Fix the motor to the bench, nothing on the shaft, 24 V on the supply.

=== "Motor GUI"
    Start the calibration. The GUI switches to *Calibration mode* and shows the driver's log step by step.

=== "Terminal"
    ```
    #Cal
    ```

The LED flashes, the motor turns in both directions, and the driver reports each step: the pole pairs, the magnet,
the supply, the parameters you entered, the open-loop spin, the angle offset, the motor constants, and finally

```
Calibration success!
Save config with #Save
Going to idle!
```

A failed step names itself. `Magnet test: Failed` is the magnet; `Open loop: Failed` or `Phase order is wrong!`
means the motor did not turn or did not respond: check the four wires, the supply, and that the magnet does not
slip.

Read in more detail: [Motor parameters and calibration](05-setup/calibration.md), with the whole log and every
message.

## 8. Set the current limit and save

The current limit is the motor's rated phase current in mA; the firmware's default is higher than a small motor's
rating.

=== "Motor GUI"
    Set the current limit in the limits, then **Save** (the GUI warns about unsaved changes until you do).

=== "Terminal"
    ```
    #Ilim 1500
    #Save
    ```

Without saving, the calibration is gone at the next power cycle. The LED now shows three short flashes and a
pause: normal operation.

Read in more detail: [Current limit and loop tuning](05-setup/tuning.md) ·
[Saving the configuration](05-setup/saving.md).

## 9. Move it

=== "Motor GUI"
    Use the jog controls: *Jog velocity* turns the motor at a speed, *Jog position* moves it to a position, *Jog
    current* applies a torque; *Send setpoint* sends a value in the current control mode. The plots show position,
    speed and current while it moves.

=== "Terminal"
    ```
    #V 16384        one revolution per second
    #V 0
    #P 0            back to where it started
    #P 16384        one revolution forward
    #Idle
    ```

Position is in encoder ticks, 16384 per revolution; speed in ticks per second; current in mA. If the motor hums
or whines, lower the current limit or tune the loops.

Read in more detail: [Control modes](06-operation/modes.md) · [Current limit and loop tuning](05-setup/tuning.md).

## 10. Where to go next

| You want to | Read |
|---|---|
| get to know Motor GUI: the screen, the plots, recordings, several motors | [Motor GUI](05-setup/motor-gui.md), [Working in Motor GUI](06-operation/motor-gui.md) |
| control the driver from a program over CAN | [Over CAN](06-operation/can.md), then [With Python](06-operation/python.md) |
| put several drivers on one bus | give each a node ID and terminate the ends: [Power and the CAN daisy chain](04-mounting/power-and-can.md) |
| protect the motor from overheating | [Thermistor](04-mounting/thermistor.md) |
| update the firmware | [Firmware](07-firmware/index.md) |
| look up a message or a command | [API reference](reference/index.md) |
| understand why it does not work | [Errors and recovery](06-operation/errors.md), [Troubleshooting](08-troubleshooting.md) |
