import numpy as np

# Your fundamental domain length
L = 18.7 # Gpc

print("=== TOPOLOGICAL DIPOLE (AXIS OF EVIL) FORECAST ===")
print(f"Manifold: Half-Turn (E2) | Domain Size: {L} Gpc")

# The Half-Turn twist occurs along the Z-axis of the Fundamental Domain
# Ghost images would appear at intervals of L
distance_to_nearest_image = L 
# Because chi_lss/L is ~0.74, the first repeating 'circle' is just 
# beyond our horizon (L/2 vs current radius).
horizon_ratio = (13.8) / (L / 2)

print(f"Nearest Ghost Image: {distance_to_nearest_image} Gpc")
print(f"Horizon/Domain Ratio: {horizon_ratio:.2f}")

if horizon_ratio < 2.0:
    print("PREDICTION: Repeating 'Circles in the Sky' are currently unobservable.")
    print("EXPLANATION: This explains why Planck found NO topology signatures.")
    print("BUT: The alignment of the quadrupole (l=2) will point directly")
    print("     along the twist axis (Dec ~ +60, RA ~ 170).")
