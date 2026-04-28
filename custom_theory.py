from cobaya.theory import Theory
import numpy as np

class LogDriftProvider(Theory):
    # Cobaya requires params as a dictionary
    params = {"k_drift": None, "H0_late": None}
    z_transition = 1278.9
    H_baseline = 67.4 

    def initialize(self):
        print("[System] LogDriftProvider: Handshake established.")

    def must_provide(self, **requirements):
        # We provide Hubble for any component (like CAMB) that needs background
        reqs = {}
        if "Hubble" in requirements:
            reqs["Hubble"] = {"z": requirements["Hubble"]["z"]}
        if "H" in requirements:
            reqs["H"] = {"z": requirements["H"]["z"]}
        return reqs

    def calculate(self, state, want_derived=True, **params_values_dict):
        pass

    def get_Hubble(self, z):
        h0 = self.provider.get_param("H0_late")
        k = self.provider.get_param("k_drift")
        return np.where(z > self.z_transition, 
                        self.H_baseline, 
                        h0 - k * np.log10(1 + z))

    def get_H(self, z):
        return self.get_Hubble(z)
