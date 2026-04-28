# Empirical Falsification of an E2 Manifold Cosmological Drift

**Author:** Melissa Dawn Dembeck-Ellison
**Status:** Concluded (Null Result)

## Abstract
We investigated a candidate geometric framework proposing that the global topology of the universe—specifically a finite Half-Turn ($E_2$) Manifold—introduces a Logarithmic Expansion Drift $H(z) = H_{late} - k \log_{10}(1+z)$. While early prototype testing using highly binned Supernova data suggested a viable pathway to reducing the Hubble ($H_0$) tension ($k \approx 2.100$), formal empirical validation against the full Pantheon+ covariance matrix conclusively ruled out this late-time topological modification.

## 1. Methodology
To rigorously test the geometric hypothesis, we constructed a custom theoretical likelihood component within the `cobaya` framework, bypassing standard $\Lambda$CDM distance calculations to directly integrate the proposed logarithmic drift. We utilized a Markov Chain Monte Carlo (MCMC) sampler to test the parameter space ($H_0$, $k_{drift}$, $\Omega_m$) against the unbinned Pantheon+ dataset (1700+ SNIa).

## 2. Formal Results
The MCMC chains reached strict formal convergence (Gelman-Rubin $R-1 < 0.05$). The empirical data aggressively constrained the drift coefficient:
* **$k_{drift}$:** strongly constrained to $< 0.190$ (rejecting the proposed $k = 2.100$).
* **$\chi^2_{SN}$:** converged at $2061.7 \pm 1.6$, entirely consistent with a standard, zero-drift $\Lambda$CDM expansion history.

## 3. Conclusion
The unbinned late-universe observational data does not support a logarithmic expansion drift. The geometric "twist" proposed by the $E_2$ Manifold boundary condition is mathematically incompatible with the rigid covariance structure of the Pantheon+ Supernova sample. Consequently, this specific late-time topological framework is falsified as a primary resolution to the Hubble tension. 
