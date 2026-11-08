# Defaults

The settings of the firmware at the release this site describes: their start values in `common.h`, and what
`EEPROM.cpp` does with each.

- **Start value**: the value in `common.h`. A setting the EEPROM does not keep starts from it at every power-up. A
  kept setting is replaced at power-up by the value in the EEPROM, so its start value is only seen before that.
- **After `#Default`**: what `#Default` writes to the EEPROM and loads; — means `#Default` does not change it.
- **Kept by `#Save`**: whether `#Save` (Send_Save_config) stores it, so that it survives a power cycle.

Internal state (error flags, counters, calibration steps, scratch variables) is left out; the error flags are in
[Errors and LED states](errors.md). A name after a value, such as `160 (CURRENT_BANDWIDTH_DEFAULT)`, is the
constant in `constants.h` the value comes from. `existing_id` for the CAN ID means that `#Default` keeps a valid
stored ID (0 when none is stored). The settings of firmware 109 that are parameters, the anti-cogging and the
encoder table among them, are in the [parameter table](can/parameters.md#every-parameter) with their defaults.

<!-- defaults-table -->
