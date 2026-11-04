# Downloads and files

Everything to download for STEPFOC, at the versions these pages describe. The versions come from one file,
`versions.yml`, so this page changes with them; which versions work together is in
[Versions and compatibility](https://docs.source-robotics.com/STEPFOC-docs/108/appendix/compatibility/).

## Firmware and software

| What | Version | Download | How to install |
|---|---|---|---|
| Firmware image (`stepfoc-firmware-V<number>.bin`), its manifest `firmware.json` and the release notes | [108](https://github.com/Source-Robotics/STEPFOC-stepper-controller/tree/V108) (2026-08-26) | [the GitHub release](https://github.com/Source-Robotics/STEPFOC-stepper-controller/releases/tag/V108) | [Updating through the bootloader](https://docs.source-robotics.com/STEPFOC-docs/108/07-firmware/update/) |
| Firmware source, a PlatformIO project | the same release | [the firmware folder at the tag](https://github.com/Source-Robotics/STEPFOC-stepper-controller/tree/V108/STEPFOC%20firmware) | [Building from source](https://docs.source-robotics.com/STEPFOC-docs/108/07-firmware/building/) |
| The bootloader binary, for a board without one | [0.1](https://github.com/Source-Robotics/stm32f103c-bootloader/tree/V0.1) (2026-06-05) | [bin](https://github.com/Source-Robotics/stm32f103c-bootloader/tree/V0.1/bin) | [Installing the bootloader on an older board](https://docs.source-robotics.com/STEPFOC-docs/108/07-firmware/bootloader/) |
| The bootloader's host tool `bl_flash.py` | the same release | [host_tools](https://github.com/Source-Robotics/stm32f103c-bootloader/tree/V0.1/host_tools) | [Updating through the bootloader](https://docs.source-robotics.com/STEPFOC-docs/108/07-firmware/update/) |
| Python library (`Spectral-BLDC`) | [1.20](https://github.com/Source-Robotics/Spectral-BLDC-Python/tree/ef30bbe4fdd1e9a93544f7f356bbaeedeaa3b459) (2026-06-19) | `pip install Spectral-BLDC`; the source and examples on GitHub, [at that version](https://github.com/Source-Robotics/Spectral-BLDC-Python/tree/ef30bbe4fdd1e9a93544f7f356bbaeedeaa3b459) | [With Python](https://docs.source-robotics.com/STEPFOC-docs/108/06-operation/python/) |
| Motor GUI | runs in the browser, always the latest | [motorgui.com](https://motorgui.com/) | [Motor GUI](https://docs.source-robotics.com/STEPFOC-docs/108/05-setup/motor-gui/) |
| CAN definitions for this release: JSON, and DBC files for the motion layouts | this site's release | [CAN frame tool and downloads](https://docs.source-robotics.com/STEPFOC-docs/108/reference/can-tools/) | |
| ST-LINK USB driver, for the programming adapter on Windows | | [STSW-LINK009](https://www.st.com/en/development-tools/stsw-link009.html) | [Installing the bootloader on an older board](https://docs.source-robotics.com/STEPFOC-docs/108/07-firmware/bootloader/) |
| STM32CubeProgrammer, for the programming adapter | | [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) | [Installing the bootloader on an older board](https://docs.source-robotics.com/STEPFOC-docs/108/07-firmware/bootloader/) |

The version links open the files at exactly that release; the dates are those of the releases on GitHub, and on
PyPI for the Python library.
Motor GUI has no versions to choose: the page is always the current one. Known faults of the firmware are on
[Known issues](https://docs.source-robotics.com/STEPFOC-docs/108/08-troubleshooting/known-issues/).

## CAD and hardware files

The latest files, on the main branch of the [firmware repository](https://github.com/Source-Robotics/STEPFOC-stepper-controller).

| What | Where |
|---|---|
| STEP model of the board | [STEP files](https://github.com/Source-Robotics/STEPFOC-stepper-controller/tree/main/STEP%20files) |
| Magnet spacers, NEMA 17 and NEMA 23 spacers | [Stepper motor accessories](https://github.com/Source-Robotics/STEPFOC-stepper-controller/tree/main/STEP%20files/Stepper%20motor%20accessories) |
| The magnet tool | [Tools](https://github.com/Source-Robotics/STEPFOC-stepper-controller/tree/main/STEP%20files/Tools) |

## More

| What | Where |
|---|---|
| Source Robotics Toolbox (joints from encoder ticks) | [Source-Robotics-Toolbox](https://github.com/Source-Robotics/Source-Robotics-Toolbox) |
| CANvas USB-to-CAN adapter | [CANvas-adapter](https://github.com/Source-Robotics/CANvas-adapter) |
| All firmware releases | [Releases](https://github.com/Source-Robotics/STEPFOC-stepper-controller/releases) |
| This documentation | [STEPFOC-docs](https://github.com/Source-Robotics/STEPFOC-docs) |
| Shop | [source-robotics.com](https://source-robotics.com/products/STEPFOC-stepper-controller) |
