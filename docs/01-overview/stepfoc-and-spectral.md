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
- **The firmware releases go in step, and from 109 share their numbers.** A change that applies to both drivers
  comes to both. From release 109 they are released together under the same version number; the Spectral Micro
  went from 107 straight to 109, so there is no Spectral Micro 108. Before, the numbers did not always match
  (STEPFOC 108 went with Spectral Micro 107); the [compatibility table](../appendix/compatibility.md) lists the
  pairs.
- **Calibration differs.** A BLDC driver measures the motor's resistance and inductance and finds its pole pairs;
  STEPFOC cannot, so you enter the three values from the motor's datasheet before calibrating. See
  [Motor parameters and calibration](../05-setup/calibration.md). From firmware 109 a STEPFOC calibration is
  followed by the encoder table and the anti-cogging; on the Spectral Micro 109 they are there but do not run by
  themselves yet.
- **Some defaults differ.** The speed estimate, the commutation delay compensation and the velocity gains of
  STEPFOC 109 were tuned on its bench; the Spectral Micro keeps its own until it is measured the same way.
- **The motor terminals differ.** A+, A−, B+, B− for the two stepper coils instead of U, V, W.
- **Some images on this site show a Spectral Micro.** Where a photo or a screenshot shows the BLDC board, the
  procedure is the same for STEPFOC.

The guides under the Guides tab were written with the Spectral Micro; the code in them runs unchanged on STEPFOC.
