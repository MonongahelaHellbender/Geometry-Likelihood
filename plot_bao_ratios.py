import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Dembeck-Ellison (DE) Parameters
h0_de = 72.0
k_drift = 2.100
om_m = 0.315
c = 299792.458 # km/s
r_s = 147.09 # Sound horizon from Planck (Mpc)

# Standard LCDM for comparison (H0 = 67.4)
h0_planck = 67.4

def get_h(z, model='de'):
    if model == 'de':
        h0_z = h0_de - k_drift * np.log10(1 + z)
        return h0_z * np.sqrt(om_m * (1+z)**3 + (1 - om_m))
    else:
        return h0_planck * np.sqrt(om_m * (1+z)**3 + (1 - om_m))

def dm_over_rs(z, model='de'):
    inv_h = lambda zp: 1.0 / get_h(zp, model)
    dm, _ = quad(inv_h, 0, z)
    return (c * dm) / r_s

# BOSS/eBOSS Gold Dataset (z, DM/rs, error)
# Reference: Alam et al. 2021 (Consensus values)
bao_z = np.array([0.15, 0.38, 0.51, 0.70, 0.85, 1.48, 2.33])
bao_dm = np.array([4.51, 10.23, 13.33, 17.86, 18.20, 30.21, 37.50])
bao_err = np.array([0.11, 0.17, 0.22, 0.33, 0.40, 0.75, 1.10])

z_range = np.linspace(0.1, 2.5, 100)
de_ratios = [dm_over_rs(z, 'de') for z in z_range]
lcdm_ratios = [dm_over_rs(z, 'planck') for z in z_range]

plt.figure(figsize=(10, 6))
plt.errorbar(bao_z, bao_dm, yerr=bao_err, fmt='ko', label='BOSS/eBOSS Data')
plt.plot(z_range, de_ratios, color='purple', linewidth=2, label=f'Dembeck-Ellison (k={k_drift})')
plt.plot(z_range, lcdm_ratios, color='red', linestyle='--', label='Standard LCDM (H0=67.4)')

plt.title('Professional Validation: BAO Distance Ratios DM(z)/rs', fontsize=14)
plt.xlabel('Redshift (z)', fontsize=12)
plt.ylabel('DM(z) / rs', fontsize=12)
plt.legend()
plt.grid(alpha=0.2)
plt.savefig('bao_validation.png', dpi=300)
print("[System] BAO Validation Plot saved to 'bao_validation.png'")
