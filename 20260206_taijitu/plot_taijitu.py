"""Taitu"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.axis('off')  # Désactive les axes

# Dessin du cercle principal (Taijitu)
R = 1
circle = plt.Circle((0., 0.), R, color='black', fill=False, zorder=2)
ax.add_patch(circle)

# Demi-cercle noir
theta1 = np.linspace(1/2*np.pi, 3/2*np.pi, 100)
x = R * np.cos(theta1)
y = R * np.sin(theta1)
ax.fill(x, y, 'black', zorder=-1)

# cercles blanc et noir
ax.add_patch(plt.Circle((0., -0.5), R/2 * 0.99, color='black', fill=True))
ax.add_patch(plt.Circle((0., 0.5), R/2 * 0.99, color='white', fill=True))

# Dessin des deux petits cercles (Yin dans Yang et Yang dans Yin)
ax.add_patch(plt.Circle((0., 0.5), R/6, color='black', fill=True))
ax.add_patch(plt.Circle((0., -0.5), R/6, color='white', fill=True))

# Affichage
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.savefig('taijitu.png')
plt.show()
