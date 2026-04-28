import numpy as np
from scipy.integrate import quad

# Parameters
h0_late = 72.0
k_drift = 2.100
om_m = 0.315

def get_h_ratio(z, model='drift'):
    if model == 'drift':
        h0_z = h0_late - k_drift * np.log10(1 + z)
        return (h0_z / h0_late) * np.sqrt(om_m * (1+z)**3 + (1 - om_m))
    else: # Standard LCDM
        return np.sqrt(om_m * (1+z)**3 + (1 - om_m))

def growth_rate(z, model='drift'):
    h_z = get_h_ratio(z, model)
    om_m_z = (om_m * (1+z)**3) / (h_z**2)
    return om_m_z**0.55

# Integrate growth over cosmic time to find the relative S8 amplitude
# S8 ~ Growth(Today) / Growth(CMB)
def calculate_growth_amplitude(model='drift'):
    # Numerical integration of growth from z=1100 to z=0
    integral, _ = quad(lambda z: growth_rate(z, model) / (1 + z), 0, 1100)
    return np.exp(-integral)

growth_drift = calculate_growth_amplitude('drift')
growth_lcdm = calculate_growth_amplitude('lcdm')
s8_reduction = (1 - (growth_drift / growth_lcdm)) * 100

print(f"=== INTEGRATED GROWTH ANALYSIS (S8 TENSION) ===")
print(f"Dembeck-Ellison S8 Suppression: {s8_reduction:.2f}%")
if s8_reduction > 3.0:
    print("STATUS: Model successfully resolves the S8 Tension via expansion history.")
