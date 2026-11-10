# Releases and versions

A firmware release is a number: 103, 105, 106, … Every release is a tag `V<number>` in the
[firmware repository](https://github.com/Source-Robotics/STEPFOC-stepper-controller) and a GitHub release that
carries the image `stepfoc-firmware-V<number>.bin`, a manifest `firmware.json` with the image's size, SHA-256 and
the commit it was built from, and the release notes. The notes are the firmware's changelog; the
[appendix](https://docs.source-robotics.com/STEPFOC-docs/109/appendix/firmware-release-notes/) collects them.

## Which release does my driver run?

```
#Info
```

prints `Software version: <number>` among the rest; Motor GUI shows the same number in the driver's identity, and
over CAN Send_Respond_Device_Info returns it as the third byte. From firmware 109 Send_Respond_Identity returns it
too, as a 16-bit number, with the product it was built for. From firmware 105 the number is the build's own
version. Before that it was read from the EEPROM, where the last `#Default` wrote it, so it names the firmware
that last restored the defaults, not necessarily the one running: 101 and 102 write 101, 103 writes 103.

### Drivers that report 103

A driver that reports 103 runs either release 103 from the `main` branch, without a bootloader, or an early build
of the `bootloader-version` branch, which also writes 103 and runs above the bootloader. Some drivers were shipped
with the bootloader before release 105. Which image those carry was not recorded: most likely 103, built for
the bootloader.

To tell whether yours has the bootloader:

- Watch the LED as you switch the driver on: with the bootloader it blinks for about two seconds before the
  firmware starts.
- Or power it up while `bl_flash.py list` or Motor GUI's *Scan bootloaders* is polling: a driver with the
  bootloader answers in its first two seconds.

With the bootloader, update it to the current release as in [Updating through the bootloader](https://docs.source-robotics.com/STEPFOC-docs/109/07-firmware/update/); the
release it ran before does not matter then. Without one, install it first:
[Installing the bootloader on an older board](https://docs.source-robotics.com/STEPFOC-docs/109/07-firmware/bootloader/).

## Which release does this site describe?

The one in the version box on the [landing page](https://docs.source-robotics.com/STEPFOC-docs/109/) and in the version selector in the header. When a
newer release changes what a page says, a new version of the site is published and the previous one stays
reachable from the selector. The [compatibility table](https://docs.source-robotics.com/STEPFOC-docs/109/appendix/compatibility/) says which releases go with
which bootloader, Python library and PAR6 runtime.

## The Spectral Micro counterpart

A change that applies to both drivers comes to the Spectral Micro too. From release 109 the two drivers share
their version numbers and are released together (the Spectral Micro went from 107 straight to 109; there is no
Spectral Micro 108). Before, the numbers did not always match: STEPFOC 108 went with Spectral Micro 107. The
compatibility table lists the pairs.

## The two branches

Releases from 105 on are built from the `bootloader-version` branch of the repository, whose firmware is linked
to run above the bootloader. The `main` branch holds the firmware of release 103 and earlier, linked to run
without a bootloader, and is not updated. A board running 103 is documented by version `103` of this site; to
move it to a current release, see [Installing the bootloader on an older board](https://docs.source-robotics.com/STEPFOC-docs/109/07-firmware/bootloader/).
