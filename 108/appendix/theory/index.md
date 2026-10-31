# Theory corner

The control concepts behind the driver's modes, for readers who want to know why a setting does what it does.
Nothing here is needed to use the driver; the chapters say what to type.

## Field-oriented control of a stepper

A hybrid stepper is a two-phase synchronous motor with many pole pairs: 50 for a 1.8° motor, so one mechanical
revolution is 50 electrical cycles. A conventional stepper driver drives it blindly: it advances the current
pattern one step at a time and relies on the rotor following. The torque the rotor receives depends on the angle
between the stator field and the rotor, the *load angle*; it is largest a quarter of an electrical cycle ahead of
the rotor and zero when the two are aligned. Because the driver does not know where the rotor is, it keeps full
current in the coils at all times, so that even a badly placed field produces enough torque, and it still loses
steps when the load angle exceeds 90° electrical.

Field-oriented control (FOC) closes that gap with a measurement of the rotor angle. The encoder on the motor shaft
gives the mechanical angle $\theta$; with the pole pairs $p$ and the angle offset $\theta_0$ found by calibration,
the electrical angle is $\theta_e = p\,\theta + \theta_0$. The two coil currents $I_A$ and $I_B$ are transformed
into the rotor's frame of reference (the Park transform):

$$
I_d = I_A \cos\theta_e + I_B \sin\theta_e,\qquad
I_q = -I_A \sin\theta_e + I_B \cos\theta_e
$$

$I_q$, the *quadrature* current, is the part of the current that stands at right angles to the rotor field and
produces torque: $\tau = K_t\, I_q$. $I_d$, the *direct* current, is aligned with the field and produces none. Two
PI controllers regulate $I_q$ to the torque demand and $I_d$ to zero by choosing the voltages $U_q$ and $U_d$;
the inverse transform turns those into the two coil voltages, applied by PWM at 25 kHz. The loop runs at 6250 Hz.

The consequences are what makes a FOC stepper behave like a servo: the current is only what the torque needs, so
the motor runs cool and quiet; the field is always placed where it produces the most torque per ampere; and a
step is never lost, because the controller knows the rotor position at every instant and works from the error,
not from a count of pulses.

Calibration supplies the constants this needs. The pole pairs come from the step angle. The current loop gains
follow from the coil's resistance $R$ and inductance $L$ and the chosen bandwidth $\omega_c = 2\pi f_c$ (`#Cbw`):
$K_p = L\,\omega_c$ and $K_i = R\,\omega_c$ cancel the coil's electrical time constant and give a first-order
response at $f_c$. The angle offset is found by driving a current along the $d$ axis and reading where the rotor
settles. The velocity constant $K_V$ comes from the back-EMF the spinning motor generates, and the torque
constant follows from it: in SI units $K_t = 1/K_V$ (with $K_V$ in rpm/V, $K_t \approx 9.55/K_V$ Nm/A).

## The cascade of loops

Position, velocity and current are controlled by three loops nested inside one another:

$$
\text{position loop: } \omega_d = K_{pp}\,(\theta_d - \theta)
\qquad
\text{velocity loop: } I_{q,d} = K_{pv}\,(\omega_d - \omega) + K_{iv}\!\int(\omega_d - \omega)\,dt
\qquad
\text{current loop: } U_q = \text{PI}(I_{q,d} - I_q)
$$

The position loop is proportional: its output is a speed demand, limited by the velocity limit. The velocity loop
is a PI controller: its output is a current demand, limited by the current limit; the integral term removes the
steady-state error a load would otherwise leave. The current loop is the innermost and fastest. Each loop must be
slower than the one inside it, by a factor of five to ten, for the inner loop to look like an ideal actuator to the
outer one; that is why the loops are tuned from the inside out, and why a current loop bandwidth of 500 Hz leaves
room for a velocity loop of a few tens of hertz and a position loop below that.

A command picks where the cascade is entered: a current setpoint uses the current loop alone, a speed setpoint
the two inner loops, a position setpoint all three. The *feedforward* terms the CAN motion frames carry are added
to the demands rather than computed from an error: a speed feedforward is added to the position loop's output, a
current feedforward to the velocity loop's output. A host that knows the trajectory can command it directly and
leave the loops to correct what is left, which gives a faster, smoother response than letting the loops produce
the whole demand from the error.

An integrator accumulates error over time, and keeps accumulating while the output is at its limit; the overshoot
this causes when the limit is released is *windup*. The velocity loop's integrator is clamped to the velocity
limit, and `#Rstint` resets the integrators on every new setpoint, which suits a host that sends one setpoint
after another in large steps.

## Impedance control

Impedance control does not prescribe a motion or a force. It prescribes the *relation* between the two: how much
force the motor produces when it is displaced from its setpoint and how fast. The driver's PD mode implements a
spring and a damper around the setpoint:

$$
\tau = K_P\,(\theta_d - \theta) + K_D\,(\dot\theta_d - \dot\theta) + K_t\, I_{ff}
$$

with the stiffness $K_P$ in Nm/rad, the damping $K_D$ in Nm·s/rad, and a current feedforward $I_{ff}$ for a known
load such as gravity. The torque is produced by the current loop ($I_q = \tau / K_t$), which is what makes FOC a
prerequisite: a stepper driven blindly cannot produce a commanded torque.

Pushed off its setpoint by an external force $F$, the motor yields by $\Delta\theta = \tau_{ext}/K_P$ and pushes
back with that force; let go, it returns, with the damper settling the motion. A small $K_P$ makes a soft joint,
a large one a stiff joint; $K_D$ without $K_P$ is a pure damper. The setpoint can move, in which case the virtual
spring drags the rotor along a trajectory with a bounded force — the property legged robots, hand-guided arms and
anything that touches people or an uncertain environment need. The impedance loop is also what a position loop
is *not*: the position loop's integral action removes any steady-state deflection and so makes the joint as stiff
as the current limit allows, which is the right thing for a machine tool and the wrong thing for a leg.

The full impedance model includes an inertia term, $M\ddot\theta$; the driver, like most joint controllers, leaves
it out, so the apparent inertia is the motor's own.

## Admittance control

Admittance is the inverse relation: the controller measures the force and commands a motion,

$$
\dot\theta_d = \frac{\tau_{ext} - K\,(\theta - \theta_0)}{B}
$$

on top of a stiff position controller. It is the natural form for a machine that has a force sensor and a position
loop that cannot be made soft, such as an industrial arm; impedance control is the natural form for a machine whose
actuator is a torque source, such as a FOC motor. The driver has no force sensor and implements impedance; a host
that wants admittance behaviour can estimate the external torque from $K_t I_q$ minus the known load and command
positions accordingly, with the limits of that estimate (friction, cogging, the current loop's accuracy).

## Compliance and stiffness

Stiffness $K$ is the force per unit of displacement; compliance is its inverse, $C = 1/K$, the displacement per
unit of force. *Passive* compliance is in the mechanism — a spring, a flexible finger, a belt; *active* compliance
is in the controller — the impedance loop above. The driver offers three points on that scale: the position mode,
stiff up to the current limit; the PD mode, as stiff as $K_P$; and the current mode, which is no stiffness at all,
a torque source the host shapes as it likes.

The current limit `#Ilim` is a force limit in every mode: the largest torque the motor will produce before it
yields, whatever the loops ask. Set it for the motor's rating, and for the mechanism's.

## Which mode

| Mode | Behaviour under an external force | Use |
|---|---|---|
| Position | holds the position up to the current limit, then yields | positioning, machines, anything that must not deflect |
| Velocity | holds the speed up to the current limit | conveyors, wheels, spindles |
| PD (impedance) | deflects in proportion to the force, returns when released | legs, arms that touch things or people, hand guiding, teleoperation |
| Current (torque) | produces the commanded torque, moves as the load dictates | a host that closes its own loop, gravity compensation, force-limited pressing |
