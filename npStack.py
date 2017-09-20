import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1])

v = np.vstack([x, y])
h = np.hstack([x, y])
d = np.dstack([x, y])

print(v)
print(h)
print(d)

print(np.array([2, 4, 5, 4]).reshape(2, 2))

c = np.linspace(1,10,10)

print(c)