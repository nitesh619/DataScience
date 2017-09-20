import numpy as np
import matplotlib.pyplot as plt

population_ages = [22,34,54,66,23,778,34,112,76,112,123,11,9,4,13,45,67,78,88,63]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('graph hai ye')
plt.legend()
plt.show()