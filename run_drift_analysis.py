import numpy as np
from cobaya.theory import Theory
from cobaya.theories.camb import camb as CAMB_Theory_Class
from cobaya.model import get_model
import sys

class LogDriftProvider(Theory):
    # Parameters for the MCMC
    params = {"k_drift": None, "H0_late": None}
    
    # Constants to protect BBN and Recombination
    z_transition = 1278.9
    H_baseline = 67.4 

    def initialize(self):
        # Physical density anchors (Planck 2018)
        self.ombh2_val = 0.02237
        self.omch2_val = 0.1200
        self.omrh2_val = 4.18e-5 # Photons + Neutrinos
        print("[System] LogDriftProvider: Physical anchors set.")

    def must_provide(self, **requirements):
        # Explicit hook for Hubble provider required by CAMB
        if "Hubble" in requirements:
            return {"Hubble": {"z": requirements["Hubble"]["z"]}}
        return {}

    def get_Hubble(self, z):
        """
        Modified expansion engine.
        Combines standard matter/rad scaling with our logarithmic drift.
        """
        h_late = self.provider.get_param("H0_late")
        k = self.provider.get_param("k_drift")
        
        # 1. Extrapolated 'Hubble Constant' at redshift z
        h0_z = np.where(z > self.z_transition, 
                        self.H_baseline, 
                        h_late - k * np.log10(1 + z))
        
        # 2. Physical matter/radiation evolution (km/s/Mpc normalized)
        matter_rad = (self.ombh2_val + self.omch2_val) * (1 + z)**3 + self.omrh2_val * (1 + z)**4
        
        # 3. Calculate Lambda density to match the h0_z anchor
        rho_lambda = (h0_z / 100.0)**2 - (self.ombh2_val + self.omch2_val + self.omrh2_val)
        
        # 4. Return total physical H(z)
        return 100.0 * np.sqrt(np.maximum(matter_rad + rho_lambda, 1e-10))

# Configuration using direct class objects to bypass string-lookup bugs
info = {
    "packages_path": "./data",
    "theory": {
        "drift_module": LogDriftProvider,
        "camb_module": {
            "class": CAMB_Theory_Class,
            "external": True,
            "stop_at_error": True
        }
    },
    "likelihood": {
        "planck_2018_lowl.TT": None
    },
    "params": {
        "ombh2": 0.02237,
        "omch2": 0.1200,
        "tau": 0.0544,
        "As": 2.1e-9,
        "ns": 0.9649,
        "H0_late": 71.43,
        "k_drift": 1.297
    }
}

print("[System] Connecting to Planck 2018 Likelihood...")
try:
    model = get_model(info)
    # Use params defined in the 'info' dict
    loglike = model.loglikelihood({})
    print("-" * 40)
    print("SUCCESS: Full Boltzmann Integration complete.")
    print(f"Total Log-Likelihood: {loglike}")
    print("-" * 40)
except Exception as e:
    print(f"[System] FATAL ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
