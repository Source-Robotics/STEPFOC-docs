# Firmware

The driver's firmware is open source and released as numbered builds. A driver shipped with firmware 105 or newer
carries a bootloader and updates itself over UART or CAN, and so do some drivers shipped before 105, which report
103 ([Drivers that report 103](https://docs.source-robotics.com/STEPFOC-docs/109/07-firmware/releases/#drivers-that-report-103) says how to tell). A driver without the
bootloader needs it installed once with a programming adapter.

## In this chapter

- [Releases and versions](https://docs.source-robotics.com/STEPFOC-docs/109/07-firmware/releases/): how releases are numbered, how to see which one a driver runs, what the
  release notes contain
- [The bootloader](https://docs.source-robotics.com/STEPFOC-docs/109/07-firmware/the-bootloader/): what it is, how the driver boots, how it is entered, its protocol and tools
- [Updating through the bootloader](https://docs.source-robotics.com/STEPFOC-docs/109/07-firmware/update/): the normal update, with Motor GUI, the bootloader's command-line
  tool, or a PAR6 control box
- [Upgrading from older firmware](https://docs.source-robotics.com/STEPFOC-docs/109/07-firmware/upgrading/): what a driver keeps when it is updated to this release, what works
  at once and what has to be run
- [Installing the bootloader on an older board](https://docs.source-robotics.com/STEPFOC-docs/109/07-firmware/bootloader/): for a driver that runs firmware 103 or older
- [Building from source](https://docs.source-robotics.com/STEPFOC-docs/109/07-firmware/building/): PlatformIO, the memory layout, uploading with a programming adapter

The release notes of every release up to the one this site describes are in the appendix,
[Firmware release notes](https://docs.source-robotics.com/STEPFOC-docs/109/appendix/firmware-release-notes/).
