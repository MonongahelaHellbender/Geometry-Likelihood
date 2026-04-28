# A Candidate Geometric Framework for Cosmological Tensions: The E2 Manifold

**Author:** Melissa Dawn Dembeck-Ellison
**Status:** Theoretical Prototype / Proof-of-Concept

## Overview
This repository provides the *theoretical scaffolding and simplified prototype scripts* for a geometric modification to the standard cosmological model. We investigate whether modeling the global topology as a finite Half-Turn (E2) Manifold introduces a Logarithmic Expansion Drift. 

**Current Status:** This is a candidate drift model that reduces selected H0/S8 discrepancies under *simplified validation tests*. It is not yet a fully reproducible likelihood pipeline.

## 1. Current Prototype Evidence
The scripts provided currently use binned, representative, or mocked data to demonstrate the mathematical viability of the framework:
* demo_pantheon_binned_fit.py: Demonstrates the shift using a highly binned subset of Pantheon+ data.
* plot_bao_ratios.py: Plots the theoretical curve against published BOSS/eBOSS data points.
* demo_corner_mock.py: Generates a mock MCMC posterior to demonstrate the expected parameter degeneracy between H0 and the drift coefficient k.
* custom_theory.py: The structural shell for the eventual Cobaya/CAMB integration.

## 2. Next Steps: Full Reproducibility Pipeline
To transition from a mathematical prototype to a formal cosmological validation, the next phase of this project will build reproduce.py, which will include:
1. Full integration of the unbinned Pantheon+ covariance matrix.
2. A complete calculate() method in Cobaya to formally modify the CAMB background expansion.
3. A real MCMC run generating true Bayesian evidence and posteriors.

## Citation
Dembeck-Ellison, Melissa Dawn (2026). A Candidate Geometric Framework for Cosmological Tensions (Prototype).
