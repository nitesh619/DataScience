import numpy as np

x = np.arange(36).reshape(6, 6)

print(x)

print('------------------------------')

print(x[1:4])
print('------1st to 3rd row in 1st to 2nd row ------')
print(x[1:4][1:3])
print('----------cols 1,2,3------------')
print(x[0:, [1, 2, 3]])
print('--------rows 1, 2, 3------------')
print(x[[1, 2, 3]])
print('--------1st to 3rd row and 2nd to 4th col------------')
print(x[1:4, 2:5])