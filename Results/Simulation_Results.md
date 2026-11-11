# Simulation Results — Multi-Resonant Triangular Antenna – Design 04

## Original HFSS screenshots

- Geometry: `../Images/01_antenna_geometry.png`
- S11 plot: `../Images/02_s11_parameter.png`
- 3D gain pattern: `../Images/03_3d_gain_pattern.png`

## Visual interpretation of the supplied S11 graph

Visible marker labels include 3.64 GHz (−14.858 dB), 4.35 GHz (−10.705 dB), 7.52 GHz (−19.681 dB) and 9.20 GHz (−15.069 dB).

| Visual feature | Frequency (GHz) | S11 (dB) |
|---|---:|---:|
| 1 | 3.640 | -14.858 |
| 2 | 4.350 | -10.705 |
| 3 | 5.720 | -12.000 |
| 4 | 7.520 | -19.681 |
| 5 | 9.200 | -15.069 |

**Caution:** values in this table are transcribed or estimated from the screenshot labels/visual curve. They are not a substitute for the original HFSS exported sweep. For designs without visible numeric markers, treat all values as approximate.

## Gain plot legend

- Maximum displayed legend value: 6.05
- Minimum displayed legend value: -21.75

Confirm whether the plotted quantity is gain, realized gain or directivity and confirm the units in HFSS before reporting a peak gain in dBi.

## Illustrative data

`../data/illustrative_s11_dataset.csv` and `../figures/illustrative_s11_curve.png` are **synthetic illustrative examples** created to demonstrate data organization and plotting. They are not measured, simulated, digitized or exported HFSS results and must not be cited as actual antenna performance.

## Exact calculations required from HFSS export

Export frequency and dB(S(1,1)) to CSV and calculate:
- Resonant frequency at each local minimum.
- Lower and upper −10 dB crossings for each continuous band.
- Absolute bandwidth: BW = f_H − f_L.
- Center frequency: fc = (f_H + f_L)/2.
- Fractional bandwidth: FBW (%) = 100 × BW/fc.
- VSWR, if needed: VSWR = (1 + |Γ|)/(1 − |Γ|), where |Γ| = 10^(S11_dB/20).

A -10 dB threshold corresponds to |Γ| ≈ 0.316 and VSWR ≈ 1.925.
