import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'X': [1, 2, 4, 3, 5], 'Y': [1, 3, 3, 2, 5]})

df['x-mean'] = df['X'] - np.mean(df['X'])
df['y-mean'] = df['Y'] - np.mean(df['Y'])

df['mul'] = df['x-mean']*df['y-mean']
df['xsquare'] = df['x-mean']**2

sumCov = np.sum(df['mul'])
sumXsqr = np.sum(df['xsquare'])

slope = sumCov/sumXsqr
bias = np.mean(df['Y']) - np.mean(df['X']) * slope

df['Ypredicted'] = df['X'] * slope + bias

df['error'] = df['Ypredicted'] - df['Y']
df['error2'] = df['error'] ** 2
print('RMSE: ', np.sqrt(np.mean(df['error2'])))

plt.scatter(df['X'], df['Y'])
plt.plot(df['X'], df['Ypredicted'])
plt.show()
print(slope)
print(bias)
print(df)
