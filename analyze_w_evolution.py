import numpy as np
import matplotlib.pyplot as plt

# Discovered Parameters
h0_late = 72.0
k_drift = 2.100
om_m = 0.315 # Planck 2018 Matter Density

def get_h_ratio(z):
    # H(z)/H0 = (h0_z/h0_late) * sqrt(om_m*(1+z)^3 + (1-om_m))
    h0_z = h0_late - k_drift * np.log10(1 + z)
    lcdm_factor = np.sqrt(om_m * (1+z)**3 + (1 - om_m))
    return (h0_z / h0_late) * lcdm_factor

def derive_w(z):
    # Numerical derivative of the expansion history to find w(z)
    dz = 0.001
    h_plus = get_h_ratio(z + dz)
    h_minus = get_h_ratio(z - dz)
    
    # Standard formula: w(z) = [-1 + (2/3)*(1+z)/H * dH/dz] / [1 - (om_m(1+z)^3 / H^2)]
    h_val = get_h_ratio(z)
    dh_dz = (h_plus - h_minus) / (2 * dz)
    
    numerator = -1 + (2/3) * (1 + z) * (dh_dz / h_val)
    denominator = 1 - (om_m * (1 + z)**3) / (h_val**2)
    return numerator / denominator

z_range = np.linspace(0.01, 2.0, 100)
w_vals = [derive_w(z) for z in z_range]

plt.figure(figsize=(10, 6))
plt.plot(z_range, w_vals, color='purple', linewidth=2.5, label='Effective w(z) from Drift (k=2.1)')
plt.axhline(-1, color='black', linestyle='--', label='Lambda (-1.0)')
plt.fill_between(z_range, -1.1, -0.9, color='gray', alpha=0.1, label='DESI/Planck Tension Zone')

plt.title('Theoretical Objective 4.1: Dark Energy Evolution w(z)', fontsize=14)
plt.xlabel('Redshift (z)', fontsize=12)
plt.ylabel('Equation of State w(z)', fontsize=12)
plt.grid(alpha=0.2)
plt.legend()
plt.ylim(-1.4, -0.6)

plt.savefig('w_evolution_discovery.png', dpi=300)
print("\n[System] Equation of State analysis saved to 'w_evolution_discovery.png'")

# Calculate w at z=0 (Local Today)
w_today = derive_w(0.001)
print(f"Predicted w(0): {w_today:.4f}")
