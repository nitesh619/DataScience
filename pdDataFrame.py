import pandas as pd
import numpy as np
from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'T', 'R'])

print(df)
print(df['W'])
print(df[['W', 'X']])

df['new'] = df['W'] + df['X']
df.drop('new', axis=1)
print(df)

df.drop('new', axis=1, inplace=True)
print(df)

df.drop('E', axis=0, inplace=True)
print(df)

print(df.shape)
print(df.loc['C'])
print(df.iloc[1])
print(df.loc['B'])
