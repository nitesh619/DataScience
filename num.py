import numpy as np
#np.set_printoptions(threshold='nan')
#check version
c = np.arange(1000).reshape(100, 10)
c = np.zeros_like(c)


for i in range(len(c)):
    for j in range(len(c[i])):
        c[i][j] += np.random.randint(1, 10)


for i in range(len(c)):
    for j in range(len(c[i])):
        c[i][j] += np.random.randint(1, 10)

print(c)
