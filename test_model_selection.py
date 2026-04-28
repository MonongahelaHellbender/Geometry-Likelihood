import numpy as np

# Data from our Supernova Fit
chi2_drift = 48.33
chi2_lcdm = 57.53
N_data = 8  # Number of data points in our binned Pantheon+ sample
k_drift_params = 3 # H0, Om_m, k
k_lcdm_params = 2  # H0, Om_m

def calculate_ic(chi2, k_params, n_data):
    aic = chi2 + 2 * k_params
    bic = chi2 + k_params * np.log(n_data)
    return aic, bic

aic_drift, bic_drift = calculate_ic(chi2_drift, k_drift_params, N_data)
aic_lcdm, bic_lcdm = calculate_ic(chi2_lcdm, k_lcdm_params, N_data)

print("=== PROFESSIONAL MODEL SELECTION ===")
print(f"Dembeck-Ellison AIC: {aic_drift:.2f} | BIC: {bic_drift:.2f}")
print(f"Standard LCDM AIC:   {aic_lcdm:.2f} | BIC: {bic_lcdm:.2f}")
print("-" * 35)
print(f"Delta AIC: {aic_lcdm - aic_drift:.2f}")
print(f"Delta BIC: {bic_lcdm - bic_drift:.2f}")

if aic_lcdm - aic_drift > 2:
    print("STATUS: Positive Evidence for the Drift Model.")
if aic_lcdm - aic_drift > 6:
    print("STATUS: STRONG Evidence. This model is statistically preferred.")
