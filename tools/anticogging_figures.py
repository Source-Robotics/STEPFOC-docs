"""The figures of the page Encoder table and anti-cogging (docs/05-setup/anti-cogging.md), a light and a dark version.

    python tools/anticogging_figures.py      # writes docs/assets/anti-cogging/<name>.svg and <name>_dark.svg

Needs matplotlib and numpy, which the site build does not (they are not in requirements.txt): run it with a Python
that has them, after a change to the data or the look, and commit the SVGs.

The numbers are in tools/anticogging_data/, copied from runs on the bench NEMA 17 (a free 50-pole-pair stepper on a
STEPFOC, the motor the page's bench values come from):

  encoder_table.csv          the encoder table the drive measured (#Encal), read back as buffer kind 4: 128 entries,
                             entry i the error at raw count 128 i, in 1/16 count (0.61 deg peak to peak)
  anticogging_bins.csv       the histogram of the current the velocity loop asks for (signal 15) over the electrical
                             angle at 1500 ticks/s, 256 bins, forward and back averaged, each without its mean: with
                             anti-cogging off, and with the harmonics found from it on. Measured before the encoder
                             table and the zero trim existed, so its 1st harmonic is large
  anticogging_harmonics.csv  the 8 largest of the harmonics 1-32 found from the "off" bins, a cos(h t) + b sin(h t) mA
  speed_6000.csv             the speed minus its mean while turning forward at 6000 ticks/s, anti-cogging off and on
                             (the same run as the bins)
  zero_trim_sets.csv         the anti-cogging set the drive identified (#Cogcal) with the current-sense zeros as
                             measured, and again with the zeros corrected by hand by -2 and +5 counts, as the trim does

The first figure, encoder_measurement, is an illustration, not a measurement: the bench table with a friction lag
and a detent pull made up for the picture, put through the drive's steps (128 bins, forward and back averaged,
harmonics 1-16). The table and the anti-cogging sets follow the firmware's arithmetic (encal.cpp, cogcal.cpp).
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "tools" / "anticogging_data"
OUT = ROOT / "docs" / "assets" / "anti-cogging"

CPR = 16384          # encoder counts per shaft turn
POLE_PAIRS = 50      # the bench NEMA 17
TO_DEG = 360.0 / 16.0 / CPR   # table units (1/16 count) -> degrees of the shaft
GREEN = "#19c37d"
THEMES = {
    # dark text and axes on the light page, light ones on the dark (slate) page; each on its page's colour, so the
    # file also reads when it is opened on its own
    "light": {"suffix": "", "page": "#ffffff", "fg": "#292B37", "muted": "#5F6270", "grid": "#E1E2E6",
              "grey": "#8C8F9B", "faint": "#C4C6CD", "green": GREEN},
    "dark": {"suffix": "_dark", "page": "#1e2029", "fg": "#E4E4E4", "muted": "#B4B6BE", "grid": "#383B47",
             "grey": "#9EA1AC", "faint": "#5A5D69", "green": GREEN},
}
WIDTH = 8.0          # inches; the page scales the SVG to its text width

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Roboto", "Segoe UI", "Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 11,
    "svg.fonttype": "none",      # text stays text: the reader's Roboto, or the next font in the list
    "svg.hashsalt": "anti-cogging",
    "axes.linewidth": 0.8,
    "lines.solid_capstyle": "round",
})


def read(name: str) -> list[dict]:
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return [{k: float(v) for k, v in row.items()} for row in csv.DictReader(f)]


def harmonics_at(terms, angle_rad):
    """a cos(h t) + b sin(h t), summed over the terms (h, a, b)."""
    return sum(a * np.cos(h * angle_rad) + b * np.sin(h * angle_rad) for h, a, b in terms)


def fit_harmonics(values, centres_rad, hs, sinc=True):
    """The firmware's fit: a = 2/N sum v cos(h t), b = 2/N sum v sin(h t) at the bin centres, each divided by the
    bin average's sinc (encal.cpp en_fit, cogcal.cpp cc_fit); sinc=False for values that are not bin averages."""
    n = len(values)
    v = np.asarray(values) - np.mean(values)
    out = []
    for h in hs:
        g = math.sin(math.pi * h / n) / (math.pi * h / n) if sinc else 1.0
        a = 2.0 / n * np.sum(v * np.cos(h * centres_rad)) / g
        b = 2.0 / n * np.sum(v * np.sin(h * centres_rad)) / g
        out.append((h, a, b))
    return out


def style(ax, t, xlabel=None, ylabel=None):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(t["muted"])
    ax.tick_params(colors=t["fg"], labelcolor=t["fg"], length=3, width=0.8)
    ax.grid(True, axis="y", color=t["grid"], linewidth=0.8)
    ax.set_axisbelow(True)
    ax.set_facecolor(t["page"])
    if xlabel:
        ax.set_xlabel(xlabel, color=t["fg"])
    if ylabel:
        ax.set_ylabel(ylabel, color=t["fg"])


def angle_axis(ax):
    ax.set_xlim(0, 360)
    ax.set_xticks(range(0, 361, 45))
    ax.set_xticklabels([f"{d}°" for d in range(0, 361, 45)])


def legend(ax, t, ncol, **kw):
    """Above the plot, left-aligned: it never covers a curve."""
    kw.setdefault("loc", "lower left")
    kw.setdefault("bbox_to_anchor", (0.0, 1.0))
    return ax.legend(frameon=False, labelcolor=t["fg"], handlelength=2.2, ncol=ncol, fontsize=10,
                     borderaxespad=0.2, columnspacing=1.6, **kw)


def save(fig, name, t):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{name}{t['suffix']}.svg"
    fig.savefig(path, format="svg", facecolor=t["page"], bbox_inches="tight", pad_inches=0.08,
                metadata={"Date": None, "Creator": None})
    plt.close(fig)
    # the page colour as a background rect, so the file reads when it is opened on its own (house rule)
    svg = path.read_text(encoding="utf-8")
    rect = f'<rect width="100%" height="100%" fill="{t["page"]}"/>'
    svg = svg.replace('<g id="figure_1">', rect + '\n <g id="figure_1">', 1)
    path.write_text(svg, encoding="utf-8", newline="\n")
    return path


# ---------- the figures ----------

def encoder_table_deg():
    rows = read("encoder_table.csv")
    return np.array([r["raw_count"] for r in rows]), np.array([r["error_sixteenth_count"] for r in rows]) * TO_DEG


def encoder_measurement(t):
    """Illustration: how the drive gets from two open-loop passes to the table."""
    raw, table = encoder_table_deg()
    fine = np.arange(0, CPR, 8)                                     # 2048 points per turn
    true = np.interp(fine, np.append(raw, CPR), np.append(table, table[0]))
    shaft = 2 * np.pi * fine / CPR
    detent = 0.045 * np.sin(50 * shaft + 0.6) + 0.015 * np.sin(200 * shaft + 1.9)   # made up
    lag = 0.12                                                       # made up: friction, degrees of the shaft
    fwd, bwd = true - lag + detent, true + lag + detent
    # the drive's steps: the mean per 1/128 of a turn, forward and back averaged, harmonics 1-16, mean removed
    bins = fine >> 7
    avg = np.array([(fwd[bins == b].mean() + bwd[bins == b].mean()) / 2 for b in range(128)])
    terms = fit_harmonics(avg, 2 * np.pi * (128 * np.arange(128) + 64) / CPR, range(1, 17))
    fitted = harmonics_at(terms, 2 * np.pi * raw / CPR)

    fig, ax = plt.subplots(figsize=(WIDTH, 3.4))
    deg = fine * 360.0 / CPR
    ax.plot(deg, bwd, color=t["grey"], linewidth=0.7, label="backward pass")
    ax.plot(deg, fwd, color=t["grey"], linewidth=0.7, linestyle=(0, (4, 1.5)), label="forward pass")
    ax.plot(np.append(raw, CPR) * 360.0 / CPR, np.append(fitted, fitted[0]), color=t["green"], linewidth=2.2,
            label="the table: their average, harmonics 1 to 16")
    style(ax, t, "shaft angle", "error, degrees of the shaft")
    angle_axis(ax)
    ax.set_ylim(-0.62, 0.5)
    ax.text(0.995, 0.03, "ILLUSTRATION", transform=ax.transAxes, ha="right", va="bottom", color=t["muted"],
            fontsize=9.5, fontweight="bold")
    legend(ax, t, 3)
    return save(fig, "encoder_measurement", t)


def encoder_table(t):
    raw, table = encoder_table_deg()
    deg = raw * 360.0 / CPR
    # en_results (parameter 55): the 1st harmonic of the entries themselves
    once = fit_harmonics(table, 2 * np.pi * raw / CPR, [1], sinc=False)
    once_curve = harmonics_at(once, np.linspace(0, 2 * np.pi, 361))

    fig, ax = plt.subplots(figsize=(WIDTH, 3.4))
    ax.plot(np.linspace(0, 360, 361), once_curve, color=t["grey"], linewidth=1.3, linestyle=(0, (5, 3)),
            label="its once-per-turn part")
    ax.plot(np.append(deg, 360), np.append(table, table[0]), color=t["green"], linewidth=2.0,
            marker="o", markersize=2.6, label="the encoder table, 128 entries")
    hi, lo = table.max(), table.min()
    for y in (hi, lo):
        ax.axhline(y, color=t["faint"], linewidth=0.8, linestyle=(0, (1, 2)))
    ax.annotate("", xy=(352, hi), xytext=(352, lo),
                arrowprops={"arrowstyle": "<->", "color": t["muted"], "linewidth": 0.9, "shrinkA": 0, "shrinkB": 0})
    ax.text(347, (hi + lo) / 2, f"{hi - lo:.2f}° peak to peak\n≈ {(hi - lo) * POLE_PAIRS:.0f}° electrical",
            ha="right", va="center", color=t["fg"], fontsize=10)
    style(ax, t, "shaft angle", "error, degrees of the shaft")
    angle_axis(ax)
    ax.set_ylim(-0.42, 0.32)
    right = ax.secondary_yaxis("right", functions=(lambda d: d * POLE_PAIRS, lambda e: e / POLE_PAIRS))
    right.set_ylabel("electrical degrees (× 50 pole pairs)", color=t["fg"])
    right.tick_params(colors=t["fg"], labelcolor=t["fg"], length=3, width=0.8)
    right.spines["right"].set_color(t["muted"])
    legend(ax, t, 2)
    return save(fig, "encoder_table", t)


def anticogging(t):
    rows = read("anticogging_bins.csv")
    off = np.array([r["off_mA"] for r in rows])
    on = np.array([r["harmonics_on_mA"] for r in rows])
    centres = (np.arange(256) + 0.5) * 360.0 / 256
    terms = [(int(r["harmonic"]), r["a_mA"], r["b_mA"]) for r in read("anticogging_harmonics.csv")]
    check = fit_harmonics(off, np.radians(centres), [h for h, _, _ in terms])
    assert all(abs(a - a2) < 0.01 and abs(b - b2) < 0.01 for (_, a, b), (_, a2, b2) in zip(terms, check))
    table = (np.roll(off, 1) + off) / 2           # cogcal.cpp: entry i at angle 64 i, between bins i-1 and i
    table_deg = np.arange(256) * 360.0 / 256
    fine = np.linspace(0, 360, 721)
    harm = harmonics_at(terms, np.radians(fine))

    def rms(x):
        return float(np.sqrt(np.mean(x ** 2)))

    fig, (top, bottom) = plt.subplots(2, 1, figsize=(WIDTH, 5.8), sharex=True, gridspec_kw={"hspace": 0.42})
    top.plot(np.append(table_deg, 360), np.append(table, table[0]), color=t["grey"], linewidth=1.4,
             label="table: 256 values")
    top.plot(fine, harm, color=t["green"], linewidth=2.2, label="harmonics: the 8 largest")
    style(top, t, None, "mA")
    top.text(0.995, 0.97, "the correction found, anti-cogging off", transform=top.transAxes, ha="right", va="top",
             color=t["muted"], fontsize=10)
    legend(top, t, 2)

    bottom.plot(centres, off, color=t["grey"], linewidth=1.4, label=f"anti-cogging off: {rms(off):.1f} mA rms")
    bottom.plot(centres, on, color=t["green"], linewidth=2.2, label=f"on (harmonics): {rms(on):.1f} mA rms")
    style(bottom, t, "electrical angle", "mA")
    bottom.text(0.995, 0.97, "what the velocity loop asks for", transform=bottom.transAxes, ha="right", va="top",
                color=t["muted"], fontsize=10)
    legend(bottom, t, 2)
    angle_axis(bottom)
    for ax in (top, bottom):
        ax.set_ylim(-25, 30)
        ax.set_yticks(range(-20, 21, 10))
    return save(fig, "anticogging", t)


def repeating(ms, values, f_e, harmonics=range(1, 9)):
    """The part of a trace that repeats with the electrical angle: least squares of harmonics 1-8 of f_e in time."""
    w = 2 * np.pi * f_e * ms / 1000.0
    cols = [np.ones_like(w)] + [f(h * w) for h in harmonics for f in (np.cos, np.sin)]
    a = np.column_stack(cols)
    coef, *_ = np.linalg.lstsq(a, values, rcond=None)
    return a[:, 1:] @ coef[1:]


def speed(t):
    rows = read("speed_6000.csv")
    ms = np.array([r["time_ms"] for r in rows])
    f_e = 6000.0 * POLE_PAIRS / CPR                 # electrical turns per second at 6000 ticks/s
    keep = ms <= 250
    fig, axes = plt.subplots(2, 1, figsize=(WIDTH, 4.6), sharex=True, sharey=True, gridspec_kw={"hspace": 0.42})
    for ax, key, colour, name in ((axes[0], "off_ticks_per_s", t["grey"], "anti-cogging off"),
                                  (axes[1], "harmonics_on_ticks_per_s", t["green"], "anti-cogging on")):
        v = np.array([r[key] for r in rows])
        v = v - v.mean()
        rep = repeating(ms, v, f_e)
        ax.plot(ms[keep], v[keep], color=t["faint"], linewidth=0.9, drawstyle="steps-mid",
                label=f"{name}, as measured")
        ax.plot(ms[keep], rep[keep], color=colour, linewidth=2.2,
                label=f"repeating with the angle: {float(np.sqrt(np.mean(rep ** 2))):.0f} ticks/s rms")
        style(ax, t, None, "ticks/s")
        legend(ax, t, 2)
    axes[1].set_xlabel("time, ms", color=t["fg"])
    axes[1].set_xlim(0, 250)
    axes[1].set_ylim(-2400, 2400)
    return save(fig, "anticogging_speed", t)


def zero_trim(t):
    rows = read("zero_trim_sets.csv")
    hs = [int(r["harmonic"]) for r in rows]
    before = [math.hypot(r["a_as_measured_mA"], r["b_as_measured_mA"]) for r in rows]
    after = [math.hypot(r["a_zeros_corrected_mA"], r["b_zeros_corrected_mA"]) for r in rows]
    x = np.arange(1, 13)
    b = np.array([before[hs.index(h)] if h in hs else 0.0 for h in x])
    a = np.array([after[hs.index(h)] if h in hs else 0.0 for h in x])
    fig, ax = plt.subplots(figsize=(WIDTH, 3.0))
    ax.bar(x - 0.19, b, width=0.36, color=t["grey"], label="zeros as measured")
    ax.bar(x + 0.19, a, width=0.36, color=t["green"], label="zeros corrected")
    for xs, ys in ((x - 0.19, b), (x + 0.19, a)):
        for xi, yi in zip(xs, ys):
            if yi >= 2:
                ax.text(xi, yi + 0.25, f"{yi:.1f}", ha="center", va="bottom", color=t["fg"], fontsize=9.5)
    style(ax, t, "harmonic of the electrical angle", "amplitude, mA")
    ax.set_xticks(x)
    ax.set_xlim(0.4, 12.6)
    ax.set_ylim(0, 11)
    legend(ax, t, 2)
    return save(fig, "zero_trim", t)


def main():
    for t in THEMES.values():
        for make in (encoder_measurement, encoder_table, anticogging, speed, zero_trim):
            print(make(t).relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
