# Hardware revisions

What changed in each revision of the STEPFOC board, and which firmware and which revision of this manual go with
it. The board reports its hardware revision in `#Info` (`Hardware version`) and in Send_Respond_Device_Info.

| Revision | Since | Changes | Firmware | Manual |
|---|---|---|---|---|
| v1 | first production | — | 101 and newer; 105 and newer ship with the bootloader, and so did some boards before 105, most likely with 103 | this manual |

Boards with release 103 or older from the `main` branch have no bootloader;
[Installing the bootloader on an older board](https://docs.source-robotics.com/STEPFOC-docs/108/07-firmware/bootloader/) brings them to the current firmware.
[Drivers that report 103](https://docs.source-robotics.com/STEPFOC-docs/108/07-firmware/releases/#drivers-that-report-103) says how to tell which kind you have.
