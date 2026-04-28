import matplotlib.pyplot as plt
import numpy as np

# Parameters
L = 18.7  # Fundamental Domain (The Box)
R_hor = 14.4  # Observable Horizon (The Sphere)

fig, ax = plt.subplots(figsize=(8, 8))

# 1. Draw the Observable Universe (The Sphere)
circle = plt.Circle((0, 0), R_hor, color='blue', alpha=0.1, label='Observable Horizon (What we see)')
ax.add_artist(circle)
ax.plot(0, 0, 'go', markersize=10, label='Earth (The Original)')

# 2. Draw the Fundamental Domain (The Box)
rect = plt.Rectangle((-L/2, -L/2), L, L, fill=False, color='purple', linewidth=3, label='Fundamental Domain (The Real Box)')
ax.add_artist(rect)

# 3. Calculate and Plot Ghost Images
# In an E2 manifold, images repeat at L intervals
ghosts = [
    (L, 0), (-L, 0), (0, L), (0, -L),  # Nearest neighbors
    (L, L), (-L, -L), (L, -L), (-L, L) # Diagonal neighbors
]

for i, (gx, gy) in enumerate(ghosts):
    ax.plot(gx, gy, 'ro', markersize=8, alpha=0.6)
    if i == 0:
        ax.plot(gx, gy, 'ro', markersize=8, alpha=0.6, label='Ghost Images (The "You" on the other side)')

# Formatting
ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)
ax.set_aspect('equal')
ax.axhline(0, color='black', alpha=0.2)
ax.axvline(0, color='black', alpha=0.2)
ax.set_title(f'Dembeck-Ellison Topology: The Ghost Map\nDomain L={L} Gpc vs Horizon R={R_hor} Gpc', fontsize=12)
ax.set_xlabel('Gpc')
ax.set_ylabel('Gpc')
ax.legend(loc='upper right', fontsize=8)

plt.savefig('ghost_map.png', dpi=300)
print("\n[System] Ghost Map visualization saved to 'ghost_map.png'")
print("OBSERVATION: Notice the red dots are OUTSIDE the blue circle.")
print("This is why we see the tension (the drift) but not the repeating images yet.")
