# Getting started

## Where to buy

You can buy a [STEPFOC starter kit](https://source-robotics.com/products/STEPFOC-starter-kit) or a [single STEPFOC driver](https://source-robotics.com/products/STEPFOC-stepper-controller) in the Source Robotics shop.

## Recommended hardware

1. [Diametrically magnetized magnet](https://source-robotics.com/products/6x2-5mm-diametrical-neodymium-magnet)
2. Stepper motor; see the [tested motors](tested_motors.md)
3. [Programming adapter](https://source-robotics.com/products/jtag-programming-adapter-1-27-pitch)
4. [Serial adapter](https://source-robotics.com/products/usb-to-serial-adapter)
5. [CAN adapter](https://source-robotics.com/products/canvas-usb-to-can-adapter) 
6. [Thermistor](https://source-robotics.com/products/100k-ntc-thermistor)
7. [CAN wires](https://source-robotics.com/products/spectral-micro-can-cable) and [power wires](https://source-robotics.com/products/spectral-micro-power-cable)

## Hardware setup

### Mounting PCB to Motor

Some hardware considerations:

* Distance between motor encoder and magnet should be around 1 mm.
* Hole spacing of STEPFOC is 31 mm (NEMA 17)

<p align="left"> <img src="../assets/STEPFOC_MAGNET.png" alt="STEPFOC MAGNET" width="800"/> <br /> </p>

## Electrical connections
!!! danger "Reversing the polarity on DC+ and DC- will destroy the board."

<p align="left"> <img src="../assets/STEPFOC_CONN.png" alt="STEPFOC CONN" width="1200"/> <br /> </p>

1. Solder the motor phases to **A+, A-, B+, B-**: one coil of the stepper to A+ and A-, the other coil to B+ and B-. Find the two coils with a multimeter (the two wires of a coil have a few ohms between them, the two coils have no connection). Keep the wires long enough to swap them: if calibration reports a wrong phase order, swap A+ and A-, which reverses the direction of that coil.
2. Connect motor power to one of the **Power connectors** terminals
3. If you are using UART comms. Connect Uart adapter to **UART connector**
4. If you are using thermistor, connect it to **Thermistor connector**
5. If you are using CAN comms. Connect CAN adapter to one of **CAN connectors**
6. When uploading code connect JTAG adapter to **JTAG connector**

!!! danger "Cable orientation"
    **ALL cables used for daisy chain (CAN and power) need to to follow orientation as shown on the image below! Failing to follow that will destroy your motor controller! All correct cables can be bought here: https://source-robotics.com/pages/connectors-and-cables** <br />

<p align="left"> <img src="../assets/Orientation.png" alt="Orientation" width="700"/> <br /> </p> 

## Connecting multiple motors (daisy chaining)

Multiple STEPFOC stepper drivers or Spectral BLDC drivers and nodes can be connected to single CAN bus using daisy-chaining. First and last nodes on can bus should have termination resistors. **You can flip the CAN switch to "ON" position to enable termination resistor.**

!!! tip "Power connectors can handle max 4 A DC. It is recommended to have at most 6 motor controllers (STEPFOC or Spectral micro) in one daisy chain."

<p align="left"> <img src="../assets/Daisy_chain-Photoroom.png" alt="Daisy chain" width="700"/> <br /> </p> 

## Thermistor connection

Solder the thermistor like shown in the image. 
!!! tip "Thermistor is disabled by default. To enable it use command #Term 1"

<p align="left"> <img src="../assets/STEPFOC_THERMISTOR-Photoroom.png" alt="STEPFOC THERMISTOR" width="600"/> <br /> </p> 

Thermistor needs to be placed on the housing of the stepper motor. Another option is remove one of the 4 stepper screws on the bottom and place thermistor inside that hole. Apply thermal cement on the thermistor to secure it in place and improve thermal conductivity. 

## Status

Normal operation | Calibration | Error mode 
---- | ---- | ----
3 short flashed and a pause <p align="left"> <img src="../assets/Normal.gif" alt="Normal" width="180"/> <br /> </p> | Flashing every 0.5 seconds <p align="left"> <img src="../assets/Calib.gif" alt="Calib" width="180"/> <br /> </p> | Solid LED, no flashing. <p align="left"> <img src="../assets/Error2.PNG" alt="Error2" width="180"/> <br /> </p>

If you have [STEPFOC firmware](https://github.com/Source-Robotics/STEPFOC-stepper-controller/tree/main/STEPFOC%20firmware) uploaded on your STEPFOC, LEDs will be in one of 3 states.

!!! note "STEPFOC controllers come PRELOADED with STEPFOC firmware"

* **Normal operation** is when motor controller has no active errors and is calibrated
* **Error mode** is active if any error on the motor driver is active. List of possible errors:
    1. Temperature error
    2. Drv error
    3. Encoder error
    4. Vbus error
    5. Velocity error
    6. Current error
    7. Not calibrated 
    8. Received ESTOP
    9. Watchdog error
* **Calibration** will flash when in calibration routine

## What next?

* **Optional** - > Flash the [latest firmware](https://github.com/Source-Robotics/STEPFOC-stepper-controller/tree/main/STEPFOC%20firmware) to your driver (Note that drivers arrive with preflashed firmware)
* You will need to [calibrate your motor](calibration.md)
* [Tune your PID loops](PID_tuning.md)
* Follow one of the guides or examples to start using your STEPFOC driver
