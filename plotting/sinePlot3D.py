import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

t = np.arange(-5, 5, 0.010)

z = np.arange(0, 1000)
fig = plt.figure(1)
ax = fig.gca(projection='3d')
ax.plot(np.array([1,1]), np.array([2,3]), z, label='parametric curve')
ax.legend()
plt.show()
