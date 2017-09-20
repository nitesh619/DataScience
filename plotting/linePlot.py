import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10)
print(x)

y = (2+3*x)
print(y)

plt.plot(x, y)
plt.show()