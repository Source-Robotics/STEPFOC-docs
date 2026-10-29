# About this manual

## Scope and audience

The STEPFOC Manual covers the STEPFOC stepper driver from unpacking to a tuned motor on a CAN bus: what the driver
is, how to mount it on a motor and wire it, the first setup over the serial terminal, calibration and tuning, how
the driver is controlled over UART and CAN or from Python, and how its firmware is updated. The Reference lists
every CAN message and UART command of the firmware release named on the landing page. The Guides are worked
examples.

It is written for someone who builds a robot or a machine with STEPFOC: a maker, a student or an engineer who can
solder four motor wires and open a serial terminal. It does not assume any knowledge of field-oriented control; the
Theory corner in the appendix explains the concepts the control modes rely on.

Read the Safety chapter before you power anything. The other chapters are in the order you need them.

## Finding your way

--8<-- "navigation.md"

## Warnings and notes

Three kinds of highlighted text appear in this documentation. Read every Danger and Notice before you act on the
step it belongs to.

--8<-- "symbols.md"

## Related documents

<!-- documents-table -->

The Spectral Micro BLDC driver shares its hardware and firmware with STEPFOC; its documentation is at
[docs.source-robotics.com/Spectral-BLDC-docs](https://docs.source-robotics.com/Spectral-BLDC-docs/). The grippers
driven by STEPFOC electronics are documented at
[docs.source-robotics.com/MSG-gripper-docs](https://docs.source-robotics.com/MSG-gripper-docs/).

## Document history

The STEPFOC Manual describes one firmware release; one revision is kept per release, and the version selector in
the header switches between them. The earlier version of this site, for firmware 103, is kept as version `103`.

| Revision | Date | Changes |
|---|---|---|
| 2026.A (draft) | — | First version in this form: the manual chapters, the generated CAN and UART reference, firmware 108 |
