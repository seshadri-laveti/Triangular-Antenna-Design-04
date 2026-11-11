#!/usr/bin/env python3
"""Analyze HFSS-exported S11 CSV data.

Required CSV headers: freq_GHz,s11_dB
Usage: python analysis/analyze_s11.py data/s11_export.csv
Uses only the Python standard library.
"""
import csv
import sys
from pathlib import Path

THRESHOLD_DB = -10.0

def load_csv(path):
    rows = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or not {"freq_GHz", "s11_dB"}.issubset(reader.fieldnames):
            raise ValueError("CSV must contain columns freq_GHz and s11_dB")
        for row in reader:
            try:
                rows.append((float(row["freq_GHz"]), float(row["s11_dB"])))
            except (TypeError, ValueError):
                continue
    rows.sort()
    if len(rows) < 3:
        raise ValueError("At least three valid data rows are required")
    return rows

def crossing(x1, y1, x2, y2, threshold):
    if y2 == y1:
        return (x1 + x2) / 2
    return x1 + (threshold-y1)*(x2-x1)/(y2-y1)

def find_bands(rows, threshold):
    bands = []
    inside = rows[0][1] <= threshold
    start = rows[0][0] if inside else None
    for (x1,y1),(x2,y2) in zip(rows, rows[1:]):
        next_inside = y2 <= threshold
        if not inside and next_inside:
            start = crossing(x1,y1,x2,y2,threshold)
        elif inside and not next_inside:
            end = crossing(x1,y1,x2,y2,threshold)
            bands.append((start,end,end-start))
            start = None
        inside = next_inside
    if inside:
        bands.append((start,rows[-1][0],rows[-1][0]-start))
    return bands

def minima(rows):
    found = [(rows[i][0],rows[i][1]) for i in range(1,len(rows)-1)
             if rows[i][1] <= rows[i-1][1] and rows[i][1] < rows[i+1][1]]
    return found or [min(rows,key=lambda p:p[1])]

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python analysis/analyze_s11.py data/s11_export.csv")
    rows = load_csv(Path(sys.argv[1]))
    print(f"Samples: {len(rows)}")
    print(f"Frequency range: {rows[0][0]:.6f} to {rows[-1][0]:.6f} GHz")
    print("\nLocal S11 minima:")
    for f, s in minima(rows):
        print(f"  {f:.6f} GHz : {s:.3f} dB")
    print(f"\nContinuous S11 <= {THRESHOLD_DB:.1f} dB bands:")
    bands = find_bands(rows, THRESHOLD_DB)
    if not bands:
        print("  No band found")
    for i,(lo,hi,bw) in enumerate(bands,1):
        center = (lo+hi)/2
        fbw = 100*bw/center if center else 0
        print(f"  Band {i}: {lo:.6f}–{hi:.6f} GHz; BW={bw:.6f} GHz; FBW={fbw:.2f}%")

if __name__ == "__main__":
    main()
