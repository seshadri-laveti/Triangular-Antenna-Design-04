# Technical Report Template — Triangular Antenna Design 04

## Title
Design and HFSS Simulation of Triangular Antenna Design 04

## Author
Laveti Seshadri, Electronics and Communication Engineering (ECE)

## Abstract
Summarize geometry, target operating bands, simulation method and verified numerical results. Do not use unverified screenshot estimates as final measurements.

## 1. Introduction
Explain the application, motivation, operating-frequency objectives and design goals.

## 2. Antenna Geometry and Design
Insert `../Images/01_antenna_geometry.png`. Record all geometry dimensions, feed arrangement, substrate material, thickness, relative permittivity, loss tangent and ground dimensions from the HFSS model.

## 3. Simulation Setup
Record HFSS version, solution type, solution frequency, sweep type/range/step, adaptive passes, mesh/convergence settings, radiation boundary or airbox, and excitation definition.

## 4. S-Parameter Results
Insert `../Images/02_s11_parameter.png`. Use exported CSV data to report every local resonance, minimum S11, continuous -10 dB band edges, absolute bandwidth and fractional bandwidth.

Formulas:
- BW = f_H - f_L
- f_c = (f_H + f_L) / 2
- FBW (%) = [BW / f_c] x 100

## 5. Radiation and Gain Results
Insert `../Images/03_3d_gain_pattern.png`. Confirm whether the plotted quantity is gain, realized gain or directivity, and state units (usually dBi). Add peak gain, radiation efficiency, directivity and E-plane/H-plane cuts where available.

## 6. Discussion
Discuss impedance matching, usable bands, radiation-pattern shape, limitations and comparison against design objectives.

## 7. Conclusion
Summarize only values verified from HFSS exports and simulation reports.

## 8. Reproducibility and Data Availability
List native `.aedt` project availability, exported CSV files, solver settings and analysis scripts. Share native files only if permitted.

## Completion checklist
- [ ] Geometry dimensions and materials recorded
- [ ] HFSS setup and boundary conditions documented
- [ ] S11 CSV exported
- [ ] Resonant frequencies calculated
- [ ] -10 dB band edges and bandwidths calculated
- [ ] Gain quantity and units confirmed
- [ ] Efficiency and directivity exported
- [ ] Radiation-pattern cuts included
- [ ] Plots have readable axes, units and captions
