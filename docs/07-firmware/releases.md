# Releases and versions

A firmware release is a number: 103, 104, 105, … Every release is a tag `V<number>` in the
[firmware repository](https://github.com/Source-Robotics/STEPFOC-stepper-controller) and a GitHub release that
carries the image `stepfoc-firmware-V<number>.bin`, a manifest `firmware.json` with the image's size, SHA-256 and
the commit it was built from, and the release notes. The notes are the firmware's changelog; the
[appendix](../appendix/firmware-release-notes.md) collects them.

## Which release does my driver run?

```
#Info
```

prints `Software version: <number>` among the rest. Over CAN, Send_Respond_Device_Info returns it as the third
byte. From firmware 105 the number is the build's own version; before that it was read from the EEPROM and could
be stale after an update until `#Default`.

## Which release does this site describe?

The one in the version box on the [landing page](../index.md) and in the version selector in the header. When a
newer release changes what a page says, a new version of the site is published and the previous one stays
reachable from the selector. The [compatibility table](../appendix/compatibility.md) says which releases go with
which bootloader, Python library and PAR6 runtime.

## The Spectral Micro counterpart

Each STEPFOC release has a Spectral Micro release with the same changes; the numbers differ by one. The
compatibility table lists the pairs.

## The two branches

Releases from 104 on are built from the `bootloader-version` branch of the repository, whose firmware is linked
to run above the bootloader. The `main` branch holds the firmware of release 103 and earlier, linked to run
without a bootloader, and is not updated. A board running 103 is documented by version `103` of this site; to
move it to a current release, see [Installing the bootloader on an older board](bootloader.md).
