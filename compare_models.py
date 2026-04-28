import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Model Parameters
h0_late = 72.0
k_drift = 2.100
h0_lcdm = 67.4
om_m = 0.315
c = 299792.458

def get_h_drift(z):
    h0_z = h0_late - k_drift * np.log10(1 + z)
    return h0_z * np.sqrt(om_m * (1+z)**3 + (1 - om_m))

def get_h_lcdm(z):
    return h0_lcdm * np.sqrt(om_m * (1+z)**3 + (1 - om_m))

def comoving_distance(z, model='drift'):
    func = lambda zp: c / (get_h_drift(zp) if model=='drift' else get_h_lcdm(zp))
    dist, _ = quad(func, 0, z)
    return dist

z_range = np.linspace(0.01, 2.0, 50)
dist_drift = [comoving_distance(z, 'drift') for z in z_range]
dist_lcdm = [comoving_distance(z, 'lcdm') for z in z_range]
percent_diff = (np.array(dist_drift) - np.array(dist_lcdm)) / np.array(dist_lcdm) * 100

plt.figure(figsize=(10, 6))
plt.plot(z_range, percent_diff, color='red', linewidth=2.5, label='Drift vs Standard LCDM')
plt.axhline(0, color='black', linestyle='--')
plt.title('Percentage Deviation in Comoving Distance', fontsize=14)
plt.xlabel('Redshift (z)', fontsize=12)
plt.ylabel('Deviation (%)', fontsize=12)
plt.grid(alpha=0.2)
plt.legend()
plt.savefig('distance_deviation.png', dpi=300)

print("=== STATISTICAL GAP ANALYSIS ===")
print(f"At z=1.10 (Euclid Range):")
print(f"Standard LCDM Distance: {comoving_distance(1.1, 'lcdm'):.2f} Mpc")
print(f"Ellison Drift Distance: {comoving_distance(1.1, 'drift'):.2f} Mpc")
print(f"Theoretical Deviation:  {percent_diff[-1]:.2f}%")
