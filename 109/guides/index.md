# Guides

Worked examples with code, from a first Python program to a leg, a gravity-compensated arm and two motors coupled
over a network. They were written with the Spectral Micro BLDC driver and run unchanged on STEPFOC: the CAN
commands and the Python library are the same.

- [Python](https://docs.source-robotics.com/STEPFOC-docs/109/guides/python/): read a driver's position and speed over CAN
- [Quadruped leg](https://docs.source-robotics.com/STEPFOC-docs/109/guides/quadruped/): the kinematics and control of a two-motor leg
- [Gravity compensation](https://docs.source-robotics.com/STEPFOC-docs/109/guides/gravity-compensation/): hold a link against gravity with a current feedforward
- [Bilateral teleoperation](https://docs.source-robotics.com/STEPFOC-docs/109/guides/bilateral-teleoperation/): two motors that follow each other, with force feedback

More examples, including a mobile robot and the SimpleFOC firmware, are in the
[Spectral-BLDC-Python examples](https://github.com/Source-Robotics/Spectral-BLDC-Python/tree/main/examples) and in
the [Spectral Micro documentation](https://docs.source-robotics.com/Spectral-BLDC-docs/).
