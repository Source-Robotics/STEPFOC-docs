# Mounting on the motor

The board has the NEMA 17 hole pattern (31 mm), so it mounts on the back of the motor with the motor's own four
rear screws, with a spacer between the motor and the board that sets the magnet height.

1. Remove the four rear screws of the motor. They hold the motor's end cap; it does not come apart when you remove
   them one at a time and put the spacer and the board on at once.
2. Put the spacer on the motor. The firmware repository has printable spacers for common motor lengths in
   [Stepper motor accessories](https://github.com/Source-Robotics/STEPFOC-stepper-controller/tree/main/STEP%20files/Stepper%20motor%20accessories)
   (NEMA 17, a 21.5 mm NEMA 17 version, NEMA 23); for another motor, make a spacer that puts the board 1 mm above
   the magnet.
3. Put the board on the spacer, encoder chip towards the magnet, and fit longer screws of the same thread (M3 on a
   NEMA 17). Tighten them evenly; the board must be parallel to the magnet.
4. Check the gap: about 1 mm, the magnet not touching the chip.

A NEMA 14 or NEMA 23 motor needs an adapter plate between the motor and the board; the NEMA 23 spacer is in the
same folder.

!!! warning "The board is bare"
    Nothing on the back of the board may touch the motor's housing. Make sure the spacer keeps the board clear of
    the end cap, and keep metal swarf and screws away from the board while you work.
