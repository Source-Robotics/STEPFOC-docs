# STEPFOC and Spectral Micro

STEPFOC is built on the same board and the same firmware as the
[Spectral Micro BLDC driver](https://docs.source-robotics.com/Spectral-BLDC-docs/). The Spectral Micro drives
three-phase brushless motors; STEPFOC drives two-phase stepper motors. Everything else is shared: the
microcontroller, the encoder, the connectors, the CAN and UART interfaces, the Python library, Motor GUI and the
bootloader.

What this means in practice:

- **The commands are the same.** Every CAN message and UART command in the Reference exists on both drivers, with
  the same IDs, names and layouts. A program written for one runs on the other.
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
