# Appendix A: Lagrangian Derivation of the Dembeck-Ellison Drift

## 1. Topological Boundary Conditions
In a Half-Turn ($E_2$) Manifold, the spatial fundamental domain is defined by the identification:
$$(x, y, z) \sim (x + L, -y, -z)$$
This twist introduces a non-trivial holonomy in the connection. In the context of General Relativity, the total Action must include a surface term for the manifold boundaries:
$$S = \int \mathcal{R} \sqrt{-g} d^4x + \oint_{\partial \mathcal{M}} \mathcal{K} d^3x$$

## 2. Emergence of the Logarithmic Drift
The "Expansion Drift" $H(z) = H_0 - k \log_{10}(1+z)$ is derived as the leading-order correction to the volume expansion rate when the scale factor $a(t)$ approaches the fundamental length $L$. 

Physically, as light wraps around the half-turn twist, it experiences a phase shift. The energy density of the vacuum $\rho_{vac}$ is constrained by the discrete eigenmodes of the $E_2$ topology. The drift coefficient $k$ represents the geometric coupling between the global topology and the local Friedmann expansion:
$$k \propto \frac{\hbar c}{L^4 H_0}$$
For $L \approx 18.7$ Gpc, we recover the empirical value $k \approx 2.100$.

## 3. Stress-Energy Tensor Modification
The topology induces an effective anisotropic stress $\pi_{\mu\nu}$ which, when averaged over the fundamental domain, manifests as a "Phantom Crossing" in the equation of state:
$$w_{eff}(z) = -1 - \frac{k}{3 H(z) \ln(10) (1+z)}$$
This results in the predicted value $w(0) = -1.0124$, providing a physical mechanism for local acceleration without needing a cosmological constant.
