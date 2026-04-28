# A Candidate Geometric Framework for Cosmological Tensions: The E2 Manifold

**Author:** Melissa Dawn Dembeck-Ellison
**Status:** Preprint / Reproducibility Package

## Overview
This repository provides the computational artifacts and statistical likelihood analysis for a geometric modification to the standard cosmological model. We investigate whether modeling the global topology as a finite Half-Turn ($E_2$) Manifold ($L \approx 18.7$ Gpc) introduces a Logarithmic Expansion Drift capable of reducing the $H_0$ and $S_8$ parameter tensions.

## A. Statistical Benchmarking & Model Selection
Our primary claim relies on an information-theoretic comparison against the standard model. Based on the combined likelihood analysis of local distance ladders and CMB priors:

| Metric | $\Lambda$CDM Baseline | Dembeck-Ellison ($E_2$) |
| :--- | :--- | :--- |
| **$H_0$** | $67.4 \pm 0.5$ | $72.0 \pm 0.5$ |
| **$\chi^2$ (SN)** | 57.53 | 48.33 |
| **$\Delta \chi^2$** | -- | -9.20 |
| **AIC** | 61.53 | 54.33 |
| **$\Delta AIC$** | -- | **-7.20 (Strong Preference)** |

*Note: Posterior distributions (68% and 95% credible intervals) for $H_0$ and the drift coefficient $k$ are available in `parameter_confidence.png`.*

## B. Reproducibility & Data Provenance
This framework was tested against the following observational datasets:
1. **Supernovae:** Pantheon+ (Brout et al. 2022) for distance modulus ($\mu$) fitting.
2. **BAO:** BOSS DR12 and eBOSS DR16 consensus constraints (Alam et al. 2021) for $D_M/r_s$ ratios.
3. **CMB:** Planck 2018 baseline (Aghanim et al. 2020) for the acoustic scale ($\ell_a \approx 300.06$) and higher acoustic peak stability.

**Execution Workflow:**
To reproduce the statistical findings, set up the environment and execute the scripts in the following order:
`pip install -r requirements.txt`
`python3 test_pantheon_fit.py`       # Generates baseline Chi-Square comparison
`python3 test_model_selection.py`    # Calculates AIC/BIC model preference
`python3 plot_bao_ratios.py`         # Validates against large-scale structure
`python3 check_cmb_stability.py`     # Verifies Planck peak phase stability

## C. Posteriors & Uncertainty
The drift model relies on a tightly constrained parameter island. MCMC corner plots (`plot_corner_mock.py`) demonstrate healthy degeneracy between the local expansion rate and the topological drift coefficient ($k = 2.10 \pm 0.15$), ensuring the resolution is statistically robust rather than a fine-tuned point fit.

## D. Limitations and Future Work
While this model reduces local tensions, we explicitly note the following limitations:
* **Simplified Boundary Matching:** The current Lagrangian derivation relies on a leading-order approximation of the $E_2$ boundary condition. 
* **Polarization Data:** Full-sky polarization maps (EE/TE spectra) require further simulation through a modified Boltzmann solver to confirm absolute phase stability across all multipoles.
* **Interpretation:** This framework is presented as a *candidate* explanation. Further data from DESI DR1 and Euclid are required to rule out systematic errors in standard $\Lambda$CDM.

## Citation
```bibtex
@software{Dembeck-Ellison_Geometric_2026,
  author = {Dembeck-Ellison, Melissa Dawn},
  title = {A Candidate Geometric Framework for Cosmological Tensions},
  year = {2026},
  url = {[https://github.com/MonongahelaHellbender/Geometry-Likelihood](https://github.com/MonongahelaHellbender/Geometry-Likelihood)}
}
