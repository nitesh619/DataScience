import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
stickercolors = ["#ffffff", "#00008f", "#ff6f00", "#ffcf00", "#009f0f", "#cf0000"]


def plot_cube(r):
    X, Y = np.meshgrid(r, r)
    ax.plot_surface(X, Y, 3, color=stickercolors[0], alpha=0.9)
    ax.plot_surface(X, Y, 0, color=stickercolors[1], alpha=0.9)
    ax.plot_surface(X, 0, Y, color=stickercolors[2], alpha=0.9)
    ax.plot_surface(X, 3, Y, color=stickercolors[3], alpha=0.9)
    ax.plot_surface(3, X, Y, color=stickercolors[4], alpha=0.9)
    ax.plot_surface(0, X, Y, color=stickercolors[5], alpha=0.9)


# plot_cube([0, 3])

def plot_edge(z):
    r = [0, 1]
    X, Y = np.meshgrid(r, r)
    ax.plot_surface(X, Y, z, alpha=0.8, color=stickercolors[0])
    ax.plot_surface(np.array([[1, 2], [1, 2]]), Y, z, alpha=0.8, color=stickercolors[0])
    ax.plot_surface(np.array([[2, 3], [2, 3]]), Y, z, alpha=0.8, color=stickercolors[0])
    r = [1, 2]
    X, Y = np.meshgrid(r, r)
    ax.plot_surface(X, Y, z, alpha=0.8, color=stickercolors[2])
    ax.plot_surface(np.array([[0, 1], [0, 1]]), Y, z, alpha=0.8, color=stickercolors[2])
    ax.plot_surface(np.array([[2, 3], [2, 3]]), Y, z, alpha=0.8, color=stickercolors[2])
    r = [2, 3]
    X, Y = np.meshgrid(r, r)
    ax.plot_surface(X, Y, z, alpha=0.8, color=stickercolors[4])
    ax.plot_surface(np.array([[0, 1], [0, 1]]), Y, z, alpha=0.8, color=stickercolors[4])
    ax.plot_surface(np.array([[1, 2], [1, 2]]), Y, z, alpha=0.8, color=stickercolors[4])


plot_edge(3)
plot_edge(0)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
