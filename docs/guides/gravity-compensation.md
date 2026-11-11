# Gravity compensation

!!! note "Written with the Spectral Micro"
    This guide was written with the Spectral Micro BLDC driver. STEPFOC uses the same CAN commands and the same Python library, so the same code runs on STEPFOC: where the guide says "Spectral Micro BLDC", read "STEPFOC".

<iframe width="560" height="315" src="https://www.youtube.com/embed/ax6jpcH3168?si=d5UKeyYru_Y35xdS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## What is Gravity Compensation?

Gravity compensation is a fundamental concept in robotic control that helps counteract the effects of gravity on a robot's joints and links. By applying the necessary motor current to balance this torque, the robotic joint can remain stationary at any position without additional external forces.

## Why is it so important?

In robotics, a significant portion of motor power is consumed just fighting against gravity. Gravity compensation algorithms are standard in all industrial robots and collaborative robot arms because they provide: improved position accuracy and control, smoother motion planning, and more precise force control applications.

The gravity compensation algorithm works as a feedforward component to the motor PID control loops, reducing their computational load and improving overall performance.

## The Approach

In this example, we use the Robotics Toolbox for Python to model a "robotic arm" with a single revolute joint. We compute the required torque using the Recursive Newton-Euler Algorithm (RNEA) and convert this torque into a motor current/torque that the motor controller will command the motor.

The full write-up is the blog post [Gravity compensation in robotics](https://source-robotics.com/blogs/blog/gravity-compensation-in-robotics).
The example code is in [Gravity compensation](https://github.com/Source-Robotics/Spectral-BLDC-Python/tree/main/examples/Advanced/Gravity%20compensation)
in the Python library's examples, with its [bill of materials](https://github.com/Source-Robotics/Spectral-BLDC-Python/blob/main/examples/Advanced/Gravity%20compensation/BOM.md).