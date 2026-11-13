# Mounting on the motor

The board has the NEMA 17 hole pattern (31 mm), so it mounts on the back of the motor with the motor's own four
rear screws, with a spacer between the motor and the board that sets the magnet height.

1. Remove the four rear screws of the motor. They hold the motor's end cap; it does not come apart when you remove
   them one at a time and put the spacer and the board on at once.
2. Put the spacer on the motor. The firmware repository has printable spacers for common motor lengths in
   [Stepper motor accessories](https://github.com/Source-Robotics/STEPFOC-stepper-controller/tree/main/STEP%20files/Stepper%20motor%20accessories)
   (NEMA 17, a 21.5 mm NEMA 17 version, NEMA 23); for another motor, make a spacer that leaves 1 mm between the magnet and the encoder chip.
3. Put the board on the spacer, encoder chip towards the magnet, and fit longer screws of the same thread (M3 on a
   NEMA 17). Tighten them evenly; the board must be parallel to the magnet.
4. Check the gap between the magnet and the encoder chip: about 1 mm, the magnet not touching it.

!!! success "Check"
    The board sits parallel to the back of the motor, with about 1 mm between the magnet and the encoder chip, and
    the shaft turns by hand without the magnet touching the chip. If the gap is wrong: [The encoder magnet](https://docs.source-robotics.com/STEPFOC-docs/109/04-mounting/magnet/).

A NEMA 23 motor takes the NEMA 23 spacer from the same folder. A smaller frame, such as NEMA 14, needs an adapter
plate you make yourself: the repository has none.

!!! warning "The board is bare"
    Nothing on the back of the board may touch the motor's housing. Make sure the spacer keeps the board clear of
    the end cap, and keep metal swarf and screws away from the board while you work. Touch earthed metal before you pick the
    board up and hold it by its edges: static electricity damages its chips.
