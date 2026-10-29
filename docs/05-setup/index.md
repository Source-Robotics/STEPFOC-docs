# First setup

From a mounted and wired driver to a calibrated, tuned motor. Everything here is done over the serial terminal:
the calibration can only be started there, and the terminal is the quickest way to try every setting.

1. [The serial terminal](terminal.md): connect the adapter, open a terminal, type `#Info`.
2. [Motor parameters and calibration](calibration.md): enter the motor's resistance, inductance and pole pairs,
   run `#Cal`.
3. [Current limit and loop tuning](tuning.md): set `#Ilim` to the motor's rated current, tune the loops if the
   defaults do not suit the motor.
4. [Saving the configuration](saving.md): `#Save`, and what `#Default` does.

A driver that has been through these four pages is ready for [Operation](../06-operation/index.md).
