# Defaults

The settings of the firmware at the release this site describes: their start values in `common.h`, and what
`EEPROM.cpp` does with each.

- **Start value**: the value in `common.h`. A setting the EEPROM does not keep starts from it at every power-up. A
  kept setting is replaced at power-up by the value in the EEPROM, so its start value is only seen before that.
- **After `#Default`**: what `#Default` writes to the EEPROM and loads; — means `#Default` does not change it.
- **Kept by `#Save`**: whether `#Save` (Send_Save_config) stores it, so that it survives a power cycle.

Internal state (error flags, counters, calibration steps, scratch variables) is left out; the error flags are in
[Errors and LED states](errors.md).

<!-- defaults-table -->
