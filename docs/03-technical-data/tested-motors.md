# Tested motors

STEPFOC works with bipolar (4-wire) stepper motors whose phase resistance is 1 to 5 Ω and whose rated current is
3 A or less. The motors below have been run on it; the resistance and inductance are the datasheet values of one
coil, which is what you enter with `#R` and `#L` before calibration.

| Motor | Frame | Pole pairs | Phase resistance | Phase inductance | Rated current | Mass | |
|---|---|---|---|---|---|---|---|
| 17HS08-1004S | NEMA 17, 20 mm | 50 | 3.7 Ω | 4.5 mH | 1.0 A | 140 g | [Stepperonline](https://www.omc-stepperonline.com/nema-17-bipolar-1-8deg-16ncm-22-6oz-in-1a-3-7v-42x42x20mm-4-wires-17hs08-1004s) |
| 17HS16-2004S1 | NEMA 17, 40 mm | 50 | 1.1 Ω | 2.6 mH | 2.0 A | 310 g | [Stepperonline](https://www.omc-stepperonline.com/nema-17-bipolar-45ncm-64oz-in-2a-42x42x40mm-4-wires-w-1m-cable-connector-17hs16-2004s1) |
| 17HS24-2104S | NEMA 17, 60 mm | 50 | 1.6 Ω | 3.0 mH | 2.1 A | 500 g | [Stepperonline](https://www.omc-stepperonline.com/nema-17-bipolar-1-8deg-65ncm-92oz-in-2-1a-3-36v-42x42x60mm-4-wires-17hs24-2104s) |
| 23HM22-2804S | NEMA 23, 56 mm, 0.9° | 100 | 1.16 Ω | 4.2 mH | 2.8 A | 700 g | [Stepperonline](https://www.omc-stepperonline.com/nema-23-bipolar-0-9deg-1-26nm-178-4oz-in-2-8a-2-5v-57x57x56mm-4-wires-23hm22-2804s) |

<div class="grid" markdown>
![17HS08-1004S](../assets/17HS08-1004S.jpg){ width="160" }
![17HS16-2004S1](../assets/17HS16-2004S1.jpg){ width="160" }
![17HS24-2104S](../assets/17HS24-2104S.jpg){ width="160" }
![23HM22-2804S](../assets/23HM22-2804S.jpg){ width="160" }
</div>

Before the first test, set the current limit to the motor's rated current with `#Ilim`; the firmware's default is
higher than the 17HS08's rating. See [Current limit and loop tuning](../05-setup/tuning.md).

!!! tip "Choosing a motor"
    A lower phase resistance and inductance give a higher speed at a given supply voltage; the velocity constant
    `KV` that calibration finds tells how fast the motor can turn: roughly 0.8 × Vbus × KV revolutions per minute.
    Motors with visibly uneven windings or a resistance that differs between the two coils calibrate badly.
