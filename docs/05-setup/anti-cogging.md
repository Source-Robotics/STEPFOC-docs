---
status: new
---

# Encoder table and anti-cogging

Firmware 109 measures two corrections on the drive itself, with nothing but the motor on the bench: the
**encoder table**, which corrects the small error of the encoder's angle reading, and the **anti-cogging**, a
current that cancels the motor's own torque ripple. After a calibration both run by themselves
([What follows the calibration](calibration.md#what-follows-the-calibration)); this page explains what they are,
how to run them again, and how to check them.

!!! danger "The motor turns"
    Each run turns the motor one revolution forward and one back, slowly. Keep the shaft free: nothing on it and
    nothing it could drive. A mechanism that cannot turn a whole revolution, a gripper's racks for example, has to
    come off first.

## The encoder table

The magnetic encoder reads the shaft angle with a small error that changes slowly around the turn: the magnet is
never exactly on the axis, and the chip itself is not perfectly linear. On the bench NEMA 17 it was 0.65° peak to
peak. The commutation multiplies it by the pole pairs, so on a 50-pole-pair stepper the field is up to 32
electrical degrees off at places, which costs torque and makes the current uneven around the turn.

To measure it, the driver turns the field open loop, one shaft revolution forward and one back at 2048 ticks/s
(about 20 s), with a current of 80 % of the current limit holding the rotor to the field. At each 1/128 of a turn
it records how far the encoder's angle is from the field's. Forward and backward are averaged, so friction, which
pulls the rotor behind the field in each direction, cancels; the stepper's own pull towards its detents is left
out by keeping only the harmonics 1 to 16 per turn. The result is a table of 128 corrections. From then on the
encoder reading is corrected with it, and the electrical offset is moved by the table's mean error, so the
commutation stays right.

A table over 4° peak to peak, or one that would move the offset by more than 60 electrical degrees, is rejected
as implausible: the magnet is loose or far off its place.

## Anti-cogging

A stepper pulls towards its detent positions, four times per electrical turn, and errors in the current
measurement add a ripple once and twice per electrical turn. At low speed both show as a ripple in the speed and
the position. Anti-cogging adds a current to the current setpoint that cancels it: a function of the electrical
angle, added in velocity and position modes.

To find it, the driver runs in velocity mode at 1500 ticks/s (parameter 44), records the current the velocity
loop asks for in 256 bins over the electrical angle for one motor revolution forward and one back, and averages
the two directions, each without its mean, so friction drops out. From that it keeps two forms of the same
correction:

- **harmonics** (parameter 37 = 1): the 8 largest of the harmonics 1 to 32 of the electrical angle, each
  a·cos(h·θ) + b·sin(h·θ) in mA;
- **table** (parameter 37 = 2): 256 values in mA over one electrical turn, interpolated between them.

The identification switches the harmonics on. On the bench both forms were equally good. Parameter 38 scales the
correction from 0 to 200 % for experiments; 100 % is as identified.

The angle here comes from the encoder alone, without the calibration's offset. The part of the correction that
comes from the current measurement is tied to the motor's electrical angle, though, which the offset defines:
that is why `#Calangle` identifies the anti-cogging again.

The identification records the current the loops ask for, so it depends a little on the gains. After a large
change of the current or velocity gains, identify it again.

### The current-sense zero trim

The once-per-electrical-turn part of the anti-cogging is mostly an error of the current-sense zero (on the bench
1.6 mA of ripple per ADC count of zero error). The identification **with the trim** reads both zero errors from it,
corrects the zeros, and identifies again on the corrected zeros. If the 1st harmonic did not drop by at least 30 %,
the zeros go back and the anti-cogging is identified once more without the trim; the state then reads 11, done
without the trim. A 1st harmonic under 1.5 mA is left alone, and one run moves a zero by at most 30 counts. The
trims (parameters 59 and 60, up to ±60 counts) are saved with the encoder table and added to the zero the driver
measures at every start-up. On the bench drive the trim took the 1st harmonic from 8.8 to 0.2 mA in one run.

## Running them

The driver must be calibrated and without an error. Both runs keep the CAN watchdog fed while they go, end by
holding the position the shaft reached, and stop at once when a host sends a command (a motion command, Idle) or
an error comes up; nothing is saved then.

| What | UART | CAN: Send_Parameter |
|---|---|---|
| the encoder table, used at once | `#Encal` | 52 = 1 |
| the encoder table, used and saved | `#Encal save` | 52 = 2 |
| the encoder table, then the anti-cogging with the trim, then save all | `#Encal all` | 52 = 3, or 43 = 3 |
| the anti-cogging, switched on | `#Cogcal` | 43 = 1 |
| the anti-cogging, switched on and saved | `#Cogcal save` | 43 = 2 |
| the anti-cogging with the trim | `#Cogcal trim` | 43 = 4 |
| the anti-cogging with the trim, saved | — | 43 = 5 |
| stop a run | `#Encal stop`, `#Cogcal stop` | 52 = 0, 43 = 0 |

A save from a run is the whole configuration, as `#Save` writes it. After a change of the motor, the magnet or
its position, run the encoder table and the anti-cogging again, in that order, or calibrate again.

Two guards keep a correction from running on the wrong data: parameter 37 refuses 1 or 2 while no set is stored
for that form, and an encoder table measured on its own (52 = 1 or 2) switches an anti-cogging set from before
off, because that set was found on the uncorrected encoder; the anti-cogging state then reads 10 until it is
identified again.

## Checking them

`#Info` ends with what is in force:

```
In force:
  encoder table: on, error 0.61 deg p-p
  anti-cogging: on (harmonics), saved
  current-sense zero trim: -1 / 5 counts
  delay compensation: 166 us
  speed estimate: direct PLL, 60 Hz
  fast reading / fast PWM: on / on
  input filter: off; integral deadband: off
  after a calibration (#Cal; #Calonly skips it): encoder table and anti-cogging, then save
```

(here with the values the bench drive measured). While a run goes, a line `running: encoder table` or
`running: anti-cogging identification` follows. `#Encal state` and `#Cogcal state` print one run's state without
starting it; after a finished identification (state 3, or 11 without the trim) it also lists the harmonics.

Over CAN the same is in the parameters (the [parameter table](../reference/can/parameters.md#every-parameter)):

| Parameter | What it tells | On the bench NEMA 17 |
|---|---|---|
| 52 | the encoder table's state: 3 done, 4 aborted, 5 error or not calibrated, 6 the rotor did not follow, 7 rejected | 3 |
| 54, 55 | the table's error peak to peak and its once-per-turn part, 0.01° of the shaft | 61-65 (0.61-0.65°); two runs within 0.021° |
| 57 | how far the last table moved the electrical offset, 0.1° electrical | −25, then −1 on a second run |
| 43 | the anti-cogging state: 3 done, 11 done without the trim, 6 the shaft did not turn | 3 |
| 45 | the cogging current found, 0.1 mA rms | 71 (7.1 mA) |
| 62, 63 | the 1st harmonic before and after the trim, 0.1 mA | 88, then 2 |
| 59, 60 | the zero trims, counts | −1, 5 |
| 79 | the bits of what is in force, see [What is in force](../reference/can/parameters.md#what-is-in-force-parameter-79) | |

With the anti-cogging on, the bench motor's speed ripple that repeats with the angle was 1.2 to 2 times smaller
at 1500 to 6000 ticks/s, and the position ripple 1.9 to 2.5 times smaller. A free motor gains little from the
encoder table in these numbers (its current varied 2.5 to 3 times less around the turn, but a free motor needs
little current); a loaded one gains more.

Send_Buffer_Read reads the corrections themselves: kind 4 the encoder table (128 values in 1/16 count), kind 2
the harmonics, kind 3 the anti-cogging table ([Respond_Buffer_Data](../reference/can/parameters.md#respond_buffer_data)).

When a run fails:

| State | Cause | What to do |
|---|---|---|
| 52 = 6, 43 = 6 | the rotor did not follow: the shaft is blocked, or the current is too low to turn it | free the shaft; for the encoder table raise the current limit (it uses 80 % of it) |
| 52 = 5, 43 = 5 | the driver was in error or is not calibrated | `#Error`, clear it, calibrate |
| 52 = 4, 43 = 4 | a command came first | run it again and send nothing meanwhile |
| 52 = 7 | the table is implausible | check the magnet: glued, centred, at the right distance ([The encoder magnet](../04-mounting/magnet.md)), then calibrate |
| 43 = 8 | the encoder table of a combined run failed | parameter 52 says why |

## Switching them off

| | UART | CAN: Send_Parameter |
|---|---|---|
| the encoder table off / on | `#Encal off`, `#Encal on` | 53 = 0, 53 = 1 |
| the anti-cogging off, harmonics, table | — | 37 = 0, 1, 2 |
| how much of the anti-cogging | — | 38 = 0 to 200 (%) |

`#Save` keeps the switches with the corrections. `#Default` clears both corrections and the trims.

!!! note "Spectral Micro"
    The Spectral Micro firmware 108 has the same encoder table and anti-cogging, but runs neither after a
    calibration until they are tested on its bench, and skips the zero trim. Its manual says more.
