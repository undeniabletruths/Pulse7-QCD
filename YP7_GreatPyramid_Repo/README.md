
# Great Pyramid YP7 Pulse Analysis

This repository contains vector geometry and pulse scan scripts used in the YP7 Framework study of the Great Pyramid of Giza.

## Contents

- `/data/chamber_vectors_gp.csv`: Vectorized grid data from King's Chamber and internal beam sequences.
- `/data/shaft_angles_gp.csv`: Shaft target angles in degrees for harmonic overlay comparison.
- `/scripts/*.py`: Scripts for performing harmonic pulse scans and statistical validation.

## Requirements

- Python 3.10+
- NumPy
- SciPy

## Reproduction Steps

1. Load grid vector data using `symbol_vector_loader.py`
2. Run fixed-interval pulse scans with `pulse_scan_engine.py`
3. Simulate random datasets via `montecarlo_test_runner.py`
4. Output and validate Z-scores using `zscore_reporter.py`

**Expected Z-scores** (from publication results):  
- Pulse 7: +3.98σ  
- Pulse 49: +4.21σ  
- Pulse 144: +2.76σ

MIT License. Open for reproduction and review.
