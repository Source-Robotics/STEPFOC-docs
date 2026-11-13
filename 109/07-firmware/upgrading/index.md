# Upgrading from older firmware

Firmware 109 changes how the driver measures and controls the motor more than any release before it. This page
says what a driver keeps when it is updated to 109, what works at once, what has to be run, and how to go back.
[Updating through the bootloader](https://docs.source-robotics.com/STEPFOC-docs/109/07-firmware/update/) is how to flash it.

## What is kept

Flashing never touches the EEPROM, where the configuration lives
([Where it is kept](https://docs.source-robotics.com/STEPFOC-docs/109/05-setup/saving/#where-it-is-kept-the-eeprom)). A driver updated from 106, 107 or 108
starts with everything it had:

- the calibration: pole pairs, R, L, the angle offset, Kt, KV, the phase order and direction;
- the CAN ID, the gains, the limits, the watchdog, the heartbeat, the thermistor and the gripper settings.

A driver from 101 to 105, saved before the configuration had checksums, is trusted and sealed at its first start
of 109 when it was ever saved; 108 reset a board saved but never calibrated, CAN ID included, and 109 keeps it.

Release 103 and older from the `main` branch have no bootloader: such a board needs the programming adapter once
([Installing the bootloader on an older board](https://docs.source-robotics.com/STEPFOC-docs/109/07-firmware/bootloader/)).

The new settings start from their defaults: tool id 0, the watchdog fallback 2000 ms / 0 mA / 1000 ticks/s / legacy,
parameter 56 = 2.

## What works at once

These need no measurement and are on from the first start of 109:

- the **direct PLL speed estimate** at 60 Hz ([The speed estimate](https://docs.source-robotics.com/STEPFOC-docs/109/05-setup/tuning/#the-speed-estimate));
- **commutation delay compensation**, 166 µs ([Commutation delay compensation](https://docs.source-robotics.com/STEPFOC-docs/109/05-setup/tuning/#commutation-delay-compensation));
- the **fast reading and PWM** paths of the control loop;
- the **current-sense zero**, measured at every start-up: a STEPFOC that read about 48 mA of current with nothing
  flowing reads under 1 mA;
- undervoltage is not checked for the first 500 ms after power-up, so a supply that ramps up slowly no longer
  leaves a Vbus error behind (overvoltage always is);
- the **watchdog actions**: the action byte the host already sends is acted on. Byte 0, what the Python library and
  the PAR6 runtime send, gives the legacy response, so an unchanged host sees no difference;
- `#Default` and a settings reset **keep the CAN ID**;
- the new CAN commands and parameters, the identity frame, telemetry, the capture, `#Info`'s `In force:`, and
  [sound through the motor](https://docs.source-robotics.com/STEPFOC-docs/109/06-operation/sound/).

## What has to be run

These are off after the update, because nothing is saved for them yet; the encoder table and the anti-cogging
cannot be switched on before they are measured:

- the **encoder table**;
- the **anti-cogging**;
- the **current-sense zero trim**.

A calibration runs all three ([What follows the calibration](https://docs.source-robotics.com/STEPFOC-docs/109/05-setup/calibration/#what-follows-the-calibration));
so does `#Encal all` without a calibration.

## What does not change by itself

- **The current gains.** The saved Kpiq and Kiiq stay as they are: on a driver calibrated before 109 they are the
  old gains divided by 7, a loop of about 70 Hz (parameter 49 reads about 71). A calibration computes them again
  at 160 Hz; so does `#Cbw 160` (or parameter 49 = 160), then `#Save`.
- **The velocity gains.** The saved Kpv and Kiv stay as they are, typically 0.007 and 0.0005. Firmware 109 was
  tuned with 0.02 and 0.001, the PLL speed estimate allowing the higher gain; set them yourself
  ([The velocity loop](https://docs.source-robotics.com/STEPFOC-docs/109/05-setup/tuning/#the-velocity-loop)).

## The whole upgrade

1. Flash 109 ([Updating through the bootloader](https://docs.source-robotics.com/STEPFOC-docs/109/07-firmware/update/)). `#Info` prints `Software version: 109` and ends with
   `In force:`.
2. Check that the current limit suits the motor (`#Ilim`), then calibrate, with the shaft free: `#Cal`. The
   encoder table (at 80 % of the current limit), the anti-cogging and the trim follow, and everything is saved
   (about two minutes in all).
3. Set the velocity gains, for example `#Kpv 0.02` and `#Kiv 0.001` (a 21.5 mm stepper overshot 95 % at these on
   the bench; its presets use `#Kpv 0.014` and `#Kiv 0.00014`), then `#Save`. (Calibration puts the
   current limit that was in force back when it ends; set `#Ilim` for your motor before step 2 if it is not.)

!!! success "Check"
    `#Info` prints `encoder table: on`, `anti-cogging: on (harmonics), saved`.

With Motor GUI's presets: apply the preset first, then calibrate, then set the velocity gains. On firmware 109 a
preset writes the current gains of a 160 Hz loop for its own R and L, the same a calibration computes from them,
and its own velocity gains.

On a robot whose joints cannot turn freely, neither the calibration nor the runs after it can be made in place.

There skip step 2: the drive keeps the calibration it has, the new speed estimate, the delay compensation and the
current-sense zero work at once, and `#Cbw 160` with `#Save` gives the new current gains. The encoder table and
the anti-cogging then stay off.

## Going back

Flashing 108 or older over 109 is safe for the configuration: the calibration and the first settings block are
unchanged, and older firmware ignores everything 109 saved from byte 256 on (tool id, fallback, anti-cogging,
encoder table). Flash 109 again and they are all still there.

!!! note "Not yet tested on the bench"
    The upgrade from 103 (programming adapter, then the bootloader, then 109) and a downgrade to 108 had not been
    tested on the bench when this page was written; the rest of what it says was, except where the pages it links
    say otherwise.
