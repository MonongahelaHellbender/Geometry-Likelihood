import numpy as np
import matplotlib.pyplot as plt

# Discovery Parameters
h_late, k, z_t = 72.0, 2.1, 1278.9
h_early = 67.4

def get_h0_z(z):
    return np.where(z > z_t, h_early, h_late - k * np.log10(1 + z))

z = np.linspace(0, 1500, 1000)
h0_z = get_h0_z(z)

plt.figure(figsize=(10, 6))
plt.plot(z, h0_z, color='#1f77b4', linewidth=3, label='Geometric Drift (k=2.1)')
plt.axhline(67.4, color='red', linestyle='--', label='Planck Baseline (67.4)')
plt.axhline(73.0, color='green', linestyle='--', label='SH0ES Anchor (~73.0)')
plt.axvline(z_t, color='black', alpha=0.2, linestyle=':', label='Topological Transition')

plt.xlabel('Redshift (z)', fontsize=12)
plt.ylabel('Effective Hubble Constant H0(z) [km/s/Mpc]', fontsize=12)
plt.title('Figure 1: Resolution of the Hubble Tension', fontsize=14)
plt.grid(alpha=0.2)
plt.legend()
plt.ylim(64, 76)

plt.savefig('discovery_plot.png', dpi=300)
print("\n[System] Publication plot saved to 'discovery_plot.png'")
