# Flashing firmware

!!! note "You can check what is the latest firmware release in the github page of STEPFOC! To check what software release is on your driver use command #Info"

!!! tip "Note"
    This video guide is for **Spectral Micro BLDC** driver but the steps for **STEPFOC** are exactly the same. **You just need to use STEPFOC repository not SPECTRAL MICRO!**
    When flashing new firmware make sure you disconnect power connection and uart connection.

<iframe width="560" height="315" src="https://www.youtube.com/embed/fcvL_6R1Je4?si=I4g3wQzkeJV9rXRw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

   |   |   Needed hardware
    ---- | ---- 
    You can change all variables using UART and CAN so flashing firmware a lot is not necessary<br /> You will usually flash it when:<br />  1. New version of the STEPFOC firmware is available <br />2. You are doing custom code development <br /> 3. You are using SimpleFOC firmware | You will need the [programming adapter](https://source-robotics.com/products/jtag-programming-adapter-1-27-pitch?variant=47293352903004) <p align="left"> <img src="../assets/ADAPTER2.png" alt="ADAPTER2" width="600"/> <br /> </p>
    
## Connecting to PCB

=== "Using [Adapter](https://source-robotics.com/products/jtag-programming-adapter-1-27-pitch?variant=47293352903004) "

    Step 1 | Step 2
    ---- | ---- 
    Locate JTAG PINS | Press programming adapter like shown in the picture (apply small amount of pressure on the pins to get a good contact)
    <p align="left"> <img src="../assets/STEPFOC_JTAG.png" alt="STEPFOC JTAG" width="750"/> <br /> </p> | <p align="left"> <img src="../assets/FLASHING3.png" alt="FLASHING3" width="500"/> <br /> </p> 

## Flashing using visual studio code
Download [Visual Studio Code](https://code.visualstudio.com/download).<br />

1. Open [STEPFOC firmware](https://github.com/Source-Robotics/STEPFOC-stepper-controller/tree/main/STEPFOC%20firmware) folder in VS code. (You need to have platformio installed)
2. Press upload in VS code (Bottom left corner in VS code)
<p align="left"> <img src="../assets/VSUPLOAD.png" alt="VSUPLOAD" width="800"/> <br /> </p>

## Flashing using STM32 ST-LINK Utility
Download the [STM32 ST-LINK utility](https://www.st.com/en/development-tools/stsw-link004.html).

!!! note "HEX and binaries"
    Using STM32 ST-LINK Utility you can flash only Binary or HEX files. These can be obtained from compiling the source code of the STEPFOC firmware

**Open STM32 ST-LINK utility Drag and drop the [binary file](https://github.com/Source-Robotics/STEPFOC-stepper-controller/tree/main/Binaries) inside.**

<p align="left"> <img src="../assets/stlink2.PNG" alt="stlink2" width="700"/> <br /> </p>

**Go to Target/settings and make sure they look like this.**

<p align="left"> <img src="../assets/stlink1.PNG" alt="stlink1" width="700"/> <br /> </p>

**Go to Target/connect. In case you get a error try to install stlink drivers from [here!](https://www.st.com/en/development-tools/stsw-link009.html)**

<p align="left"> <img src="../assets/stlink_conn.png" alt="stlink conn" width="700"/> <br /> </p>

**Go to Target/program and verify. You should get pink output msg like below.**

<p align="left"> <img src="../assets/stlink_prog.png" alt="stlink prog" width="700"/> <br /> </p>
