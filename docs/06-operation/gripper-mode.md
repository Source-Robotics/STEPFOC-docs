# Gripper mode

A driver can run a gripper instead of a joint: the same board, with a state machine that moves a jaw to a
position between open and closed, at a speed, with a current limit that becomes the grip force, and that reports
when it holds something. The [MSG gripper](https://docs.source-robotics.com/MSG-gripper-docs/) is built on
STEPFOC this way.

## Turning it on

```
#Gripper 1
#Save
```

`#Default` clears the flag again. A driver in gripper mode still answers every other command; the gripper
commands only work with the flag set.

## Calibrating the gripper

After every power-up the gripper has to find its end stops: `#Gripcal` or Send_gripper_calibrate. The jaws open
until they stop, then close until they stop, slowly and at 500 mA; the positions become 0 (open) and 255 (closed).
The driver prints nothing when it is done. If it has not found both end stops within about 24 s it gives up, and
the gripper stays uncalibrated. Check the result with `#Gripinfo` (`Gripper calibrated is: 1`) or the
`gripper_calibrated` bit of Respond_Gripper_data_pack: a move is carried out only once the gripper is calibrated.
The motor itself must be calibrated (`#Cal`) and saved before that, once.

## Moving

Over UART:

```
#Gripvel 100       speed, 0 to 255
#Gripcur 400       current limit of the move in mA, the grip force
#Grippos 200       go to position 200 (0 open, 255 closed); also activates the gripper
```

Over CAN, Send_gripper_data_pack carries position, speed and current in one frame with the activate and action
bits; the driver answers with Respond_Gripper_data_pack: the position, the measured current, whether it is moving,
and the object detection:

| Object detection | Meaning |
|---|---|
| 0 | moving |
| 1 | an object was detected while closing: the jaws stopped on it and hold it with the current limit |
| 2 | an object was detected while opening |
| 3 | the position was reached |

An empty Send_gripper_data_pack (0 bytes) only asks for the state. Send_gripper_data_pack's E-stop bit raises the
gripper E-stop error; `#Gripstop 1` does the same over UART. The error stays: while the E-stop bit is 1 the driver
raises it again on every control cycle, and `#Error` prints only `In error state!`. To recover, clear the bit
(`#Gripstop 0`, or a Send_gripper_data_pack with the bit 0), then `#Clear` or Send_Clear_Error.

!!! warning "Current"
    The firmware does not limit the current you give a gripper move. The safe range depends on the gripper's
    mechanics and motor; the gripper's manual gives it. The driver is rated for 2.8 A, but nothing enforces that
    here: a gripper move uses the current as sent.

## Where the details are

The bytes of the two gripper frames are in the [CAN reference](../reference/can/gripper.md), the UART commands in
the [UART reference](../reference/uart/gripper.md).
