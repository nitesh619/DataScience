import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.patheffects as path_effects
x = np.linspace(-1.5, 1.5, 301)
print(x)
y = np.linspace(-1.5, 1.5, 301)
z = 9
n =10

x, y =np.meshgrid(x, y)
print(x)


plt.figure()
ax = plt.gca(projection='3d')
ax.set_path_effects(path_effects=[path_effects.Stroke(linewidth=5, foreground='#ffffff'),
                       path_effects.Normal()])

ax.plot_surface(x,y,z, color='r')
plt.show()