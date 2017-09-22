import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 50, 50)
print(x)
y = np.linspace(1, 50, 50)
z = 50
m = 0
x, y = np.meshgrid(x, y)
print(x)

plt.figure()
ax = plt.gca(projection='3d')
ax.plot_surface(x, y, z, cmap=plt.get_cmap("jet"))
ax.plot_surface(x, y, m, cmap=plt.get_cmap("jet"))

plt.show()
