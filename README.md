# Empirical Falsification of an E2 Manifold Cosmological Drift

**Author:** Melissa Dawn Dembeck-Ellison
**Status:** Concluded (Null Result)

## Current calibrated center

The current source-calibrated center for this repo is the stored unbinned
Pantheon+ falsification chain, packaged in:

- `outputs/null_result_center/geometry_likelihood_null_center_packet_v1.json`
- `outputs/null_result_center/geometry_likelihood_null_center_packet_v1.md`

Current center id: `e2_drift_null_result`

## Overview
This repository investigated whether modeling the global topology as a finite Half-Turn ($E_2$) Manifold introduced a Logarithmic Expansion Drift $H(z) = H_{late} - k \log_{10}(1+z)$ capable of reducing the $H_0$ and $S_8$ tensions. 

While preliminary prototype testing against heavily binned data suggested a statistically viable parameter space ($k \approx 2.1$), formal integration with the unbinned Pantheon+ covariance matrix conclusively falsified the model.

## Final Results (Formal MCMC)
A full Markov Chain Monte Carlo analysis using the `cobaya` framework against
the complete Pantheon+ sample (1700+ SNIa) collapsed the original high-drift
prototype into a low-drift posterior that no longer supports the claimed
tension-resolution story.

The stored chain-level readout is:

- **$k_{drift}$ mean:** $\approx 0.158 \pm 0.138$
- **$k_{drift}$ 97.5th percentile:** $\approx 0.522$
- **$\chi^2_{SN}$:** $\approx 2061.7 \pm 1.6$
- **Final convergence surface:** $R-1 \approx 0.0408$

**Conclusion:** The unbinned observational data does not support the original
prototype drift near $k \approx 2.1$. The proposed topological drift framework
fails as a primary resolution to the Hubble tension and is best preserved as a
formal falsification result.

## Repository Value
This codebase is preserved as an open-source demonstration of rapid hypothesis testing, symbolic integration, and formal Bayesian falsification pipelines.

## Useful current files

If you need the formal falsification surface rather than the early exploratory
phase, start with:

- `custom_theory.py`
  - Cobaya theory hook for the tested drift model
- `reproduce.py`
  - formal Pantheon+ MCMC entry point
- `plot_real_corner.py`
  - renders the actual posterior corner plot from saved chains
- `true_parameter_confidence.png`
  - current posterior visualization

## Historical caution

Earlier positive-looking prototype scripts have been quarantined under:

- `archive/pre_falsification_prototypes/`

Those files are kept for provenance only and should not override the null-result
conclusion above.

Two additional top-level files should also be treated as historical,
pre-falsification surfaces rather than as current truth:

- `PHASE_2_FINAL_REPORT.md`
- `manuscript.tex`
