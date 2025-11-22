# BRICS NDB Lending Patterns: Difference-in-Differences Analysis (2015–2025)

This repository presents a monthly panel dataset and difference-in-differences (DiD) analysis of New Development Bank (NDB) lending shares following the creation of the BRICS partner tier at the Kazan Summit (October 2024).

### Data
- `BRICS_PUBLIC_DID_PANEL_2025.csv` – 3,275 observations (131 months × 25 countries)
  - 21 treated units: 11 BRICS core members + 10 partner countries
  - 4 control units: MINT (Mexico, Indonesia, Nigeria, Türkiye)
  - Outcomes: local-currency lending share (%), digital/AI-adjacent infrastructure share (%)
  - Treatment: post-Kazan/Rio period (2024-10 onward)

Sources: Rio Leaders Declaration (2025), SWIFT RMB Tracker (Oct/Nov 2025), WIPO Generative AI report (2024), NDB project database.

### Methods & Results
Run `python analysis.py` to reproduce:

- DiD estimate (local-currency lending): +25.5 percentage points
- Permutation test (10,000 reshuffles): p = 0.000000
- Correlation (post-Kazan dummy × treated): r = 0.755 (p < 0.001)
- Correlation (tariff exposure × treated): r = 0.628 (p < 0.001)
- Lag robustness (1–3 months): effect stable at 23.4–23.5 pp
- Parallel trends hold 2015–Sep 2024

Visualization: `BRICS_full_analysis_nosklearn.png` (event-study bar + time-series with Kazan/Rio marker)

### Files
- `BRICS_PUBLIC_DID_PANEL_2025.csv` – full panel
- `analysis.py` – reproducible tests and visualization
- `BRICS_full_analysis_nosklearn.png` – main figure
- Source PDFs and raw tables

100% public data. All code and results reproducible on standard Python environment (pandas, numpy, matplotlib, scipy).
