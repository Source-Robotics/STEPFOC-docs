# Guides

Worked examples with code, from a first Python program to a leg, a gravity-compensated arm and two motors coupled
over a network. They were written with the Spectral Micro BLDC driver and run unchanged on STEPFOC: the CAN
commands and the Python library are the same.

- [Python](python.md): read a driver's position and speed over CAN
- [Quadruped leg](quadruped.md): the kinematics and control of a two-motor leg
- [Gravity compensation](gravity-compensation.md): hold a link against gravity with a current feedforward
- [Bilateral teleoperation](bilateral-teleoperation.md): two motors that follow each other, with force feedback

More examples, including a mobile robot and the SimpleFOC firmware, are in the
[Spectral-BLDC-Python examples](https://github.com/Source-Robotics/Spectral-BLDC-Python/tree/main/examples) and in
the [Spectral Micro documentation](https://docs.source-robotics.com/Spectral-BLDC-docs/).
