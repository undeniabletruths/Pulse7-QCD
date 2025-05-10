
# Göbekli Tepe YP7 Pulse Analysis

This repository contains source data and scripts used in the analysis presented in the study:
**"The Göbekli Tepe Harmonic Interface: Pulse 7 Encoding and Temporal Synchronization in Megalithic Architecture"**

## Contents

- `/data/glyph_coordinates_gt.csv`: Coordinates and sequence indices of glyphs on Pillar 43.
- `/data/pillar_spacing_gt.csv`: Measured distances between central pillars.
- `/scripts/*.py`: Scripts for loading data, performing pulse scans, and calculating Z-scores.

## Requirements

- Python 3.10+
- NumPy
- SciPy

## Reproduction Steps

1. Load glyph data using `symbol_vector_loader.py`
2. Run pulse detection using `pulse_scan_engine.py`
3. Perform statistical validation via `montecarlo_test_runner.py`
4. Output Z-scores and visuals using `zscore_reporter.py`

Expected Z-scores:
- Pulse 7: > +4.0σ
- Pulse 12: ~ +3.5σ
- Pulse 144: > +4.8σ

MIT License. Contributions welcome.
