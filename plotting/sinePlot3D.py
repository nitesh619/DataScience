import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

t = np.arange(-5, 5, 0.010)

z = np.arange(0, 1000)
fig = plt.figure(1)
ax = fig.gca(projection='3d')
ax.plot(np.sin(2 * np.pi * t), np.cos(2 * np.pi * t) + t / 5, z, label='parametric curve')
ax.legend()
plt.show()
