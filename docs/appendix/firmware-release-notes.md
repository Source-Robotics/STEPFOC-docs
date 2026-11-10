# Firmware release notes

What changed in each firmware release, from the release notes in the firmware repository, up to the release this site describes.

!!! note "Release 109, not published yet"
    Its notes on GitHub come with the release; until then, a summary of what it brings over 108, each item with
    the page that describes it:

    - Settings in blocks with their own checksums; a reset keeps the CAN ID; flashing never touches them
      ([Saving the configuration](../05-setup/saving.md)).
    - Parameters: any setting by number over CAN (36-38) or `#Par`; identity (39) and telemetry (40); captures,
      a histogram and buffers (41-43) ([Parameters and buffers](../reference/can/parameters.md),
      [Status and diagnostics](../06-operation/diagnostics.md)).
    - The watchdog's actions: hold, brake, coast, descend ([The watchdog](../06-operation/watchdog.md)).
    - The current loop from R, L and one bandwidth, 160 Hz; a choice of speed estimates; commutation delay
      compensation; the position input filter and the velocity-integral deadband
      ([Current limit and loop tuning](../05-setup/tuning.md)).
    - The encoder table and anti-cogging measured on the drive ([Encoder table and anti-cogging](../05-setup/anti-cogging.md)).
    - Calibration puts the current limit back when it ends; `#Cal` goes on to the encoder table and anti-cogging, `#Calonly` is the calibration alone
      ([Motor parameters and calibration](../05-setup/calibration.md)).
    - The product lock, the current-sense zero measured at start-up, no undervoltage error while the supply ramps up.
    - Sound through the motor: tones, a queue, samples; CAN 44 and 45, `#Tone` ([Sound](../06-operation/sound.md)).
    - `#Info` prints the build, the board ID and the calibration ID; parameters 84 to 87 hold them
      ([Status and diagnostics](../06-operation/diagnostics.md)).

    Fixes and smaller changes in 109:

    - Gripper: a gripper poll (the empty gripper frame) sent right after a new move command could cancel it as
      new, and so could a repeat of the same command: the move then ran from the previous move's "at position",
      and the gripper reported object detection 3 (at position) while it pressed on an object. Now only a new
      command marks itself, and the gripper reports contact as intended. The same in every release before 109.
    - Current-sense zero: a driver started on USB before its motor supply measured the zero without the supply,
      about 60 counts (100 mA) off, and nothing said so. It now waits for the supply, uses 2048 until it comes, says
      so in `#Info`, and measures the zero by itself once the supply is there.
    - Calibration: the angle alignment locks the rotor with the calibration current through the coil's
      resistance (it used a fixed 0.5 V, too weak for small motors with a high coil resistance). `#Cal` started
      while the motor moves switches the bridge off first. A failed calibration switches the bridge off at once.
      An E-stop ends a calibration, and `#Cal` is not started while one is latched (`#Clear` first). `#Calangle` is refused while the driver is in error.
    - Limits: `#Ilim` and `#Vlimit` take the magnitude of a negative number. Send_Limits ignores a negative value
      or one that is not a number, and stops the current limit at 2800 mA. The current of a gripper move stays
      within 0 to 2800 mA. Send_PD_Gains, Send_Current_Gains, Send_Velocity_Gains, Send_Position_Gains and
      Send_Kt ignore a negative value or one that is not a number. Send_Voltage_Limit takes 0 to 60000 mV, as
      parameter 17 does, and ignores anything else. `#PP` takes 1 to 200 pole pairs only while idle, as
      parameter 78 does.
    - Watchdog: setting the time starts a fresh window, so switching it on again no longer trips it at once. A
      negative time means off. A save over CAN no longer counts as silence
      ([The watchdog](../06-operation/watchdog.md)).
    - After `#Cal`: if a host takes the driver within 3 s, the encoder-table and anti-cogging runs are dropped
      (they used to wait and start at the next idle). `#Encal` and `#Cogcal` start a run only with no argument,
      or with `save`, `all` (`#Encal`) or `trim` (`#Cogcal`); any other word only prints the state. `#Cogcal
      stop`, parameter 43 = 0 and parameter 52 = 0 stop a combined run in either of its parts. While a run turns
      the motor, a capture is not armed and the histogram's source cannot be changed. The anti-cogging run's
      speed stays within the velocity limit. The hold after an encoder-table run starts from a clean velocity
      integral ([Encoder table and anti-cogging](../05-setup/anti-cogging.md)).
    - Storage: a block whose check fails is read up to three times before its defaults are used. `#Info` and the
      status flags say the anti-cogging is saved only while what is in RAM equals what is stored.
    - CAN: a frame with a length code above 8 is treated as 8 bytes. Extended (29-bit) frames are ignored.
    - Control: the current-loop integrals are cleared whenever the bridge brakes or coasts. PWM duties stay
      between 0 and 100 %. The watchdog's hold and descend no longer use the delay compensation of the last
      moving loop.
    - Sound: the note queue and the sample buffer no longer replay old content after a stop. A pitch the driver
      cannot play answers `Tone: not played`.
    - Python library, release after 1.20: `Send_Parameter` packs the float parameters (8 to 16 and 20) itself. A
      position or speed beyond 24 bits, or a current beyond 16 bits, raises `ValueError` (it used to wrap).
      `UnpackData` ignores other nodes' frames, remote frames and extended frames. Node IDs must be 0 to 15.
      Parameters 79, 80 and 84 to 87 read as unsigned. A failed send returns False and is logged once
      ([Python library](../reference/python.md)).

    [Upgrading from older firmware](../07-firmware/upgrading.md) says what a driver keeps and what to run.

--8<-- "generated/firmware_release_notes.md"
