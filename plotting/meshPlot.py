import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-1.5, 1.5, 301)
print(x)
y = np.linspace(-1.5, 1.5, 301)
z = x**2 + y

x, y =np.meshgrid(x, y)
print(x)


plt.figure()
ax = plt.gca(projection='3d')
ax.plot_surface(x,y,z, cmap=plt.get_cmap("jet"))

plt.show()