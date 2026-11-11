# Methodology — Multi-Resonant Triangular Antenna – Design 04

## 1. Geometry preparation
Create the antenna geometry in HFSS using the dimensions and materials recorded from the native project.

## 2. Material assignment
Record substrate permittivity, loss tangent, conductor material and thickness. Do not infer them from screenshots.

## 3. Excitation and boundaries
Document the feed/port type, reference impedance, radiation boundary or airbox, and all boundary assignments.

## 4. Solution and sweep
Record solution type, adaptive solution frequency, convergence settings, sweep range, sweep type and frequency resolution.

## 5. S-parameter evaluation
Plot dB(S(1,1)) over frequency. Use −10 dB as a commonly used impedance-matching threshold, while reporting the actual criterion used.

## 6. Radiation evaluation
Document the exact HFSS quantity plotted (GainTotal, RealizedGainTotal or Directivity), frequency, coordinate system, and units. Add 2D principal-plane cuts when available.

## 7. Reproducibility
Retain the native `.aedt` file where licensing and sharing permissions allow, plus CSV exports and solver settings.
