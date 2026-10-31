# STEPFOC and Spectral Micro

STEPFOC and the [Spectral Micro BLDC driver](https://docs.source-robotics.com/Spectral-BLDC-docs/) are sister
drivers: similar hardware and similar firmware, each made for its kind of motor. The Spectral Micro drives
three-phase brushless motors; STEPFOC drives two-phase stepper motors. They are not the same board and do not run
the same firmware, but they are controlled and run practically the same way: the same CAN and UART commands, the
same Python library, Motor GUI and bootloader.

What this means in practice:

- **The commands are practically the same.** The CAN messages and UART commands of the Reference have the same
  IDs, names and layouts on both drivers; STEPFOC adds a few that only make sense on a stepper (homing against a
  sensor, open-loop stepping). A program written for one runs on the other.
- **The firmware releases go in step.** A STEPFOC release has a Spectral Micro counterpart with the same changes;
  the [compatibility table](../appendix/compatibility.md) lists the pairs. The numbers differ by one (STEPFOC 108
  is Spectral Micro 107).
- **Calibration differs.** A BLDC driver measures the motor's resistance and inductance and finds its pole pairs;
  STEPFOC cannot, so you enter the three values from the motor's datasheet before calibrating. See
  [Motor parameters and calibration](../05-setup/calibration.md).
- **The motor terminals differ.** A+, A−, B+, B− for the two stepper coils instead of U, V, W.
- **Some images on this site show a Spectral Micro.** Where a photo or a screenshot shows the BLDC board, the
  procedure is the same for STEPFOC.

The guides under the Guides tab were written with the Spectral Micro; the code in them runs unchanged on STEPFOC.
