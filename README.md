# Empirical Falsification of an E2 Manifold Cosmological Drift

**Author:** Melissa Dawn Dembeck-Ellison
**Status:** Concluded (Null Result)

## Overview
This repository investigated whether modeling the global topology as a finite Half-Turn ($E_2$) Manifold introduced a Logarithmic Expansion Drift $H(z) = H_{late} - k \log_{10}(1+z)$ capable of reducing the $H_0$ and $S_8$ tensions. 

While preliminary prototype testing against heavily binned data suggested a statistically viable parameter space ($k \approx 2.1$), formal integration with the unbinned Pantheon+ covariance matrix conclusively falsified the model.

## Final Results (Formal MCMC)
A full Markov Chain Monte Carlo analysis using the `cobaya` framework against the complete Pantheon+ sample (1700+ SNIa) yielded the following constraints:

* **$k_{drift}$:** $< 0.190$ (Strongly preferring 0.0)
* **$\chi^2_{SN}$:** $2061.7 \pm 1.6$

**Conclusion:** The unbinned observational data does not support a logarithmic expansion drift. When exposed to the full covariance matrix, the likelihood engine aggressively drives the drift coefficient to zero, effectively returning the expansion history to a standard $\Lambda$CDM geometry. The proposed topological framework is formally ruled out as a primary resolution to the $H_0$ tension.

## Repository Value
This codebase is preserved as an open-source demonstration of rapid hypothesis testing, symbolic integration, and formal Bayesian falsification pipelines.
