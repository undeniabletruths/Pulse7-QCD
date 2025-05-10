
# Dighton Rock YP7 Pulse Analysis

This repository contains vectorized glyph data and pulse scan scripts used in the analysis of Dighton Rock as presented in the YP7 system.

## Contents

- `/data/glyph_vectors_dighton.csv`: Vectorized positions and sequence indices of symbols traced from Dighton Rock.
- `/scripts/*.py`: Scripts for performing harmonic pulse scans and statistical analysis.

## Requirements

- Python 3.10+
- NumPy
- SciPy

## Reproduction Steps

1. Load glyph data using `symbol_vector_loader.py`
2. Apply pulse scanning with `pulse_scan_engine.py`
3. Validate statistical anomalies using `montecarlo_test_runner.py`
4. Output Z-scores with `zscore_reporter.py`

**Expected Result:**  
Pulse 7 recurrence with Z > +36σ, confirming harmonic encoding within the petroglyph inscriptions.

MIT License. Contributions welcome.
