---
status: draft
---

# Tuning

The loop gains of the driver — the position, velocity and current loops and the impedance (PD) loop — with the
response visible on the plots while you change them.

- **Presets**: a starting set of gains for a kind of motor, applied with *Apply preset*.
- **Gains**: the fields for Kpp, Kpv, Kiv, Kpiq, Kiiq, KP and KD; *Apply gains* sends them to the driver, Save keeps
  them.
- **Jog and plot**: command a speed or a position and watch the motor follow it on the plot; overshoot,
  oscillation and lag show at once. *Live stream while dragging* updates the setpoint as you move the slider.

The procedure — current loop first, then velocity, then position, each from the inside out — is in
[Current limit and loop tuning](../05-setup/tuning.md), and the theory behind it in the
[theory corner](../appendix/theory.md).

<!-- screenshots to follow -->
