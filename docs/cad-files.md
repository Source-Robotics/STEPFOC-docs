# Downloads and files

Everything to download for STEPFOC, at the versions these pages describe. The versions come from one file,
`versions.yml`, so this page changes with them; which versions work together is in
[Versions and compatibility](appendix/compatibility.md).

## Firmware and software

| What | Version | Download | How to install |
|---|---|---|---|
| Firmware image (`stepfoc-firmware-V<number>.bin`), its manifest `firmware.json` and the release notes | <!-- version-link: firmware --> | [the GitHub release](<!-- version-release: firmware -->) | [Updating through the bootloader](07-firmware/update.md) |
| Firmware source, a PlatformIO project | the same release | [the firmware folder at the tag](<!-- version-url: firmware -->/STEPFOC%20firmware) | [Building from source](07-firmware/building.md) |
| The bootloader binary, for a board without one | <!-- version-link: software.bootloader --> | [bin](<!-- version-url: software.bootloader -->/bin) | [Installing the bootloader on an older board](07-firmware/bootloader.md) |
| The bootloader's host tool `bl_flash.py` | the same release | [host_tools](<!-- version-url: software.bootloader -->/host_tools) | [Updating through the bootloader](07-firmware/update.md) |
| Python library (`Spectral-BLDC`) | <!-- version-link: software.python_library --> | `pip install Spectral-BLDC`; the source and examples on GitHub, [at that version](<!-- version-url: software.python_library -->) | [With Python](06-operation/python.md) |
| Motor GUI | runs in the browser, always the latest | [motorgui.com](https://motorgui.com/) | [Motor GUI](05-setup/motor-gui.md) |
| CAN definitions for this release: JSON, and DBC files for the motion layouts | this site's release | [CAN frame tool and downloads](reference/can-tools.md) | |
| ST-LINK USB driver, for the programming adapter on Windows | | [STSW-LINK009](https://www.st.com/en/development-tools/stsw-link009.html) | [Installing the bootloader on an older board](07-firmware/bootloader.md) |
| STM32CubeProgrammer, for the programming adapter | | [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) | [Installing the bootloader on an older board](07-firmware/bootloader.md) |

The version links open the files at exactly that release; the dates are those of the releases on GitHub, and on
PyPI for the Python library.
Motor GUI has no versions to choose: the page is always the current one. Known faults of the firmware are on
[Known issues](08-troubleshooting/known-issues.md).

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
