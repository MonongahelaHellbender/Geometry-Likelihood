import numpy as np
import matplotlib.pyplot as plt

# Dembeck-Ellison Parameters
h0_late = 72.0
k_drift = 2.100
om_m = 0.315

def get_h_ratio(z):
    h0_z = h0_late - k_drift * np.log10(1 + z)
    # H(z)/H0_local
    lcdm_factor = np.sqrt(om_m * (1+z)**3 + (1 - om_m))
    return (h0_z / h0_late) * lcdm_factor

def growth_factor_approx(z):
    """
    Approximates the growth rate of structure f(z).
    f(z) ~ Om_m(z)^0.55
    """
    h_z = get_h_ratio(z)
    # Evolving matter density fraction
    om_m_z = (om_m * (1+z)**3) / (h_z**2)
    return om_m_z**0.55

z_range = np.linspace(0, 2.0, 50)
f_drift = [growth_factor_approx(z) for z in z_range]
# Standard LCDM (No drift, H0=67.4)
f_lcdm = [(om_m * (1+z)**3 / (np.sqrt(om_m*(1+z)**3 + (1-om_m)))**2)**0.55 for z in z_range]

plt.figure(figsize=(10, 6))
plt.plot(z_range, f_drift, color='blue', linewidth=2, label='Dembeck-Ellison Growth (Faster Expansion)')
plt.plot(z_range, f_lcdm, color='red', linestyle='--', label='Standard LCDM Growth')

plt.title('Objective 6.1: Growth of Structure (S8 Tension Resolution)', fontsize=14)
plt.xlabel('Redshift (z)', fontsize=12)
plt.ylabel('Growth Rate f(z)', fontsize=12)
plt.legend()
plt.grid(alpha=0.2)
plt.savefig('growth_tension_resolution.png', dpi=300)

reduction = (1 - (f_drift[0] / f_lcdm[0])) * 100
print(f"=== GROWTH TENSION ANALYSIS ===")
print(f"Local Growth Suppression: {reduction:.2f}%")
print("RESULT: If suppression > 2%, the model resolves the S8 tension alongside Hubble.")
