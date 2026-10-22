# **STEPFOC datasheet**

!!! Note annotate "**Spectral micro BLDC driver and STEPFOC driver**" 
    **STEPFOC stepper driver is built on the same hardware and software foundation as the Spectral Micro BLDC driver. As a result, some references or images in this documentation may still show the Spectral Micro, since both drivers share about 99% of their features. They also use the same CAN and UART command sets, with only minor differences in UART-based calibration and setup procedures.** <br />


!!! Note annotate "" 
**STEPFOC** is a FOC based stepper motor controller designed to deliver affordable, high-performance hardware paired with powerful open-source software. Its mission is to transform low-cost stepper motors into high-performance robotic servos, enabling advanced robotics applications without the high price tag.

The controller features a 14-bit magnetic encoder, inline current sensing, CAN and UART interfaces, and supports position, velocity, torque, and impedance control modes — everything you need to build precise and capable robotic systems.

Optimized for NEMA17 stepper motors, STEPFOC provides a complete solution for robotics development.


   |   |   Features
    ---- | ---- 
    <p align="left"> <img src="../assets/STEPFOC.png" alt="drawing" width="600"/> <br /> </p> | **Electrical specs**  <br /> - Stepper motor FOC controller <br />  - Voltage input: 12 - 29V   <br />  - Max continuous phase current: 2.8A <br />  - Max phase current: 2.8A (with good colling) <br />  - Inline current sensing <br />  - PWM switching rate: 25 kHz <br />  - Max power: 80W <br />   - Idle power: 0.3W <br />  - Control loop frequency: 6250Hz   <br />  - Max electrical frequency: 460 Hz <br />    <br /> **Mechanical specs** <br />   - Mass: 8 g   <br />  - Dimensions: 39mm x 39mm <br />  - Nema 17 compatible mounting hole distances<br />  <br />  **Features** <br />- STM32f103c microcontroller <br />- 14 bit encoder <br />  - CAN and UART communication <br /> -  Daisy chain CAN and power connector  <br />  - EEPROM memory 16 Kbit <br />  -  Hardware overcurrent, over-under voltage and temperature protection  <br />  - Fully open source firmware and support for SimpleFOC <br />  - One additional pin for hall sennsor <br />  - Temperature sensor connector <br /> -  Torque, velocity, position, and Impedance control modes <br /> -  Auto calibration features <br /> -  Connector for step / dir interface
  

!!! Tip annotate "Each STEPFOC Stepper controller is Fully end of line tested." 

!!! Note annotate "" 

## **Absolute maximum ratings**

* Supply voltage -> min 12V, typ 24V, max 29V
* Phase current -> typ 1.5A, max 2.5A with good cooling and in small bursts
* Operating Temperature -> min -20°C, typ 25°C, max 130°C

!!! Note annotate "" 

## **Connectors**

Connector | Cable assembly | Connector datasheet
---- | ---- | ----
UART| [Link](https://source-robotics.com/products/uart-cable) | [JST SH series](https://www.digikey.com/en/product-highlight/j/jst/sh-and-sr-series-connectors)
Power| [Link](https://source-robotics.com/products/spectral-micro-power-cable) | [JST XH series](https://www.digikey.com/en/product-highlight/j/jst/xh-series-connectors)
CAN| [Link](https://source-robotics.com/products/spectral-micro-can-cable?variant=47694678655324) | [JST ZH series](https://www.digikey.com/en/products/detail/jst-sales-america-inc/ZHR-2/566476)
JTAG| [Link](https://source-robotics.com/products/jtag-programming-adapter-1-27-pitch?variant=47293352903004) | 1.27 pitch pin header

!!! Note annotate "" 

## **Pinout**

!!! Tip annotate "REVERSING POLARITIY ON DC+- WILL DESTROY YOUR BOARD." 

Motor phases are conneceted to U,V and W. Power is connected to DC+ and DC-
<p align="left"> <img src="../assets/STEPFOC_CONN.png" alt="drawing" width="1200"/> <br /> </p>

!!! Note annotate "Note!" 

    * thermistor pin is using pulldown of 54.9 kilo ohms. 
    * UART is 3v3 only. Using 5V will destroy the board.
    * "ADDITIONAL2" can be used as analog input or general purpose input/output

!!! Note annotate "" 

## **CAD and dimensions**

[You can download Spectral micro STEP files here!](https://github.com/Source-Robotics/STEPFOC-stepper-controller/tree/main/STEP%20files)
<p align="left"> <img src="../assets/STEPFOC_STEP.png" alt="drawing" width="600"/> <br /> </p>

STEPFOC uses same hole spacing as NEMA17 format motors.
!!! Note annotate "Magnetic encoder is located exactly at the middle of the board!" 
<p align="left"> <img src="../assets/micro_dimensions.PNG" alt="drawing" width="600"/> <br /> </p>

!!! Note annotate "" 

## **CAN termination**

To use CAN termination make sure to place the switch in **ON** position!
<p align="left"> <img src="../assets/STEPFOC_CAN.png" alt="drawing" width="600"/> <br /> </p>



!!! Note annotate "" 

## **Pre loaded firmware**

!!! Note annotate "" 
    **STEPFOC comes preloaded with  STEPFOC firmware. You can check what release by using UART interface and calling the command: #Info**

Default settings that come prelaoded are:

- LED indication: 1  
- Calibrated: 0
- Using thermistor: 0
- Watchdog active: 0
- Heartbeat active: 0
- UART baud rate: 256000
- CAN baud rate: 1000000
- Default CAN node ID: 0
- I AM GRIPPER: 0

- Pole pair: 0
- Resistance: 0
- Inductance: 0
