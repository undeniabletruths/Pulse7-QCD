# Pulse7-QCD Anomaly Detection

This repository contains the Python scripts and configuration files used to identify the Pulse 7 numeric resonance in CMS Open Data.

## Contents
- `pulse_detector.py` — pulse matching and interval analysis
- `simulate_montecarlo.py` — 100k-run Monte Carlo engine
- `data_loader.py` — handles CMS ROOT file loading and filtering

## Requirements
- Python 3.10+
- NumPy, pandas, uproot

## Run Example
```bash
python simulate_montecarlo.py --pulse 7 --events 100000p
