"""
WARNING: PROTOTYPE DEMO SCRIPT
This script generates MOCK random samples for visualization purposes.
It is NOT the output of a converged, formal MCMC chain.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Generate 1000 "Possible Universes" clustered around your discovery
np.random.seed(42)
h0_samples = np.random.normal(72.0, 0.5, 1000)
k_samples = np.random.normal(2.1, 0.15, 1000)
# Add a slight correlation (the 'Degeneracy' professionals look for)
k_samples = k_samples + (h0_samples - 72.0) * 0.1

df = pd.DataFrame({'H0 (Local)': h0_samples, 'Drift Coefficient (k)': k_samples})

g = sns.JointGrid(data=df, x='H0 (Local)', y='Drift Coefficient (k)', space=0)
g.plot_joint(sns.kdeplot, fill=True, cmap='Purples', thresh=0, levels=10)
g.plot_marginals(sns.histplot, color='purple', alpha=0.3, kde=True)

plt.suptitle('Parameter Confidence Intervals (The Corner Plot)', y=1.02)
plt.savefig('parameter_confidence.png', dpi=300)
print("[System] Corner Plot generated as 'parameter_confidence.png'")
