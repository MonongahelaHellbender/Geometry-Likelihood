import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Define the "Box" (Fundamental Domain)
L = 18.7 # Side length in Gpc
r = [0, L]
X, Y = np.meshgrid(r, r)

# Draw the 6 faces of the manifold domain
ax.plot_surface(X, Y, np.full_like(X, 0), alpha=0.1, color='blue') # Floor
ax.plot_surface(X, Y, np.full_like(X, L), alpha=0.1, color='blue') # Ceiling
ax.plot_surface(X, np.full_like(X, 0), Y, alpha=0.3, color='cyan') # Back Face (Anchor)
ax.plot_surface(X, np.full_like(X, L), Y, alpha=0.3, color='magenta') # Front Face (Twist)

# Draw a "Light Path" showing the Half-Turn identification
# A ray starts at (L/4, 0, L/2) and exits at (3L/4, L, L/2) due to the half-twist
path_x = [L/4, L/2, 3*L/4]
path_y = [0, L/2, L]
path_z = [L/2, L/2, L/2]
ax.plot(path_x, path_y, path_z, color='yellow', linewidth=4, label='Light wrapping with 180° twist')
ax.scatter([L/4], [0], [L/2], color='green', s=100, label='Entry Point')
ax.scatter([3*L/4], [L], [L/2], color='red', s=100, label='Half-Turn Exit')

ax.set_title('Half-Turn (E2) Topology: Fundamental Domain', fontsize=14)
ax.set_xlabel('X (Gpc)')
ax.set_ylabel('Y (Gpc)')
ax.set_zlabel('Z (Gpc)')
ax.legend()

plt.savefig('manifold_visualization.png', dpi=300)
print("\n[System] 3D Manifold visualization saved to 'manifold_visualization.png'")
