# 3. Calibrate

The driver learns your motor: you give it three values from the datasheet, and calibration measures the rest.

## 1. Restore the defaults

First the factory defaults, so that calibration does not start from another motor's values or from junk in the
EEPROM.

=== "Motor GUI"

    Press *Default* in the settings.

=== "Terminal"

    ```
    #Default
    ```

??? info "What else #Default resets"
    It also resets the serial number, hardware version and batch date stored in the EEPROM; from firmware 109 it
    keeps the CAN node ID.

## 2. Enter the motor parameters

From the motor's datasheet, for **one coil**:

- the pole pairs: 50 for a 1.8° motor, 100 for 0.9°;
- the phase resistance, in ohms;
- the phase inductance, in henries (2.6 mH = 0.0026).

![The three values on a typical datasheet, here for the 17HS16-2004S1: 1.8°, 1.1 Ω, 2.6 mH.](https://docs.source-robotics.com/STEPFOC-docs/109/assets/Motor_specs.webp){ width="700" }

STEPFOC does not measure these; calibration fails on a value left at 0.

!!! tip "We recommend a Motor GUI preset"
    In Motor GUI's **Presets** tab, a preset enters these values for you, with safe limits and gains. For a Source
    Robotics product, pick its preset. For any other stepper, pick *Generic motor* and type the pole pairs, the
    resistance and the inductance from the datasheet: the preset writes them with a low current limit and soft
    loops, so the motor calibrates safely. More: [Motor GUI](https://docs.source-robotics.com/STEPFOC-docs/109/05-setup/motor-gui/).

=== "Motor GUI"

    Enter *Pole pairs*, *Resistance* and *Inductance* in the motor settings and apply them.

=== "Terminal"

    ```
    #PP 50
    #R 1.1
    #L 0.0026
    ```

!!! success "Check"
    `#Info` prints the values you entered as `Number of pole pairs`, `Single phase resistance` and `Single
    phase Inductance` (Motor GUI shows them in the motor settings). None of them may be 0.

More: [Motor parameters and calibration](https://docs.source-robotics.com/STEPFOC-docs/109/05-setup/calibration/).

## 3. Calibrate

1. Fix the motor to the bench, with nothing on the shaft.
2. Set the supply to 24 V.
3. Start the calibration:

    === "Motor GUI"

        Start the calibration. The GUI switches to *Calibration mode* and shows the driver's log step by step.

    === "Terminal"

        ```
        #Cal
        ```

4. Keep the shaft free until the end, about a minute more after the log below.

The LED flashes, the motor turns in both directions, and the driver reports each step: the pole pairs, the magnet,
the supply, the parameters you entered, the open-loop spin, the angle offset, the motor constants, and finally

```
Calibration success!
Next, by itself: the encoder table, then anti-cogging (about a minute; keep the shaft free). Everything is saved when they finish (#Encal state, #Cogcal state)
Going to idle!
```

The driver then goes on to measure the encoder table and the anti-cogging, and saves everything when they succeed.

A failed step names itself, and the log ends with `Calibration failed!`. `Magnet test: Failed` is the magnet;
`Phase order is wrong!` means the motor did not turn or did not respond: check the four wires, the supply, and
that the magnet does not slip.

!!! success "Check"
    The calibration log ends with `Calibration success!`. If it does not, use the failed step in
    [Calibration troubleshooting](https://docs.source-robotics.com/STEPFOC-docs/109/05-setup/calibration/#troubleshooting); do not treat a stopped motor as
    success.

More: [Motor parameters and calibration](https://docs.source-robotics.com/STEPFOC-docs/109/05-setup/calibration/), with the whole log and every message.

## 4. Set the current limit and save

The current limit is the motor's rated phase current in mA. It is 1700 mA after `#Default`, more than a small
motor's rating.

Calibration uses its own 1600 mA for its steps and puts the limit back when it ends, and the encoder table after it
runs at 80 % of the limit, so on a small motor set it before you calibrate (step 3); set it now in any case.

=== "Motor GUI"

    Set the current limit in the limits, then **Save** (the GUI warns about unsaved changes until you do).

=== "Terminal"

    ```
    #Ilim 1500
    #Save
    ```

Without saving, the calibration is gone at the next power cycle. The LED now shows three short flashes and a
pause: normal operation.

![Three short flashes and a pause](https://docs.source-robotics.com/STEPFOC-docs/109/assets/Normal.webp){ width="180" }

!!! success "Check"
    After **Save**, Motor GUI no longer marks unsaved changes, and after a power cycle `#Info` prints
    `Calibrated`. [Saving](https://docs.source-robotics.com/STEPFOC-docs/109/05-setup/saving/) explains which settings are kept.

More: [Current limit and loop tuning](https://docs.source-robotics.com/STEPFOC-docs/109/05-setup/tuning/) · [Saving the configuration](https://docs.source-robotics.com/STEPFOC-docs/109/05-setup/saving/).
