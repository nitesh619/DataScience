import numpy as np
import pandas as pd
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

sales = {'account': ['Jones LLC', 'Alpha Co', 'Blue Inc'],
         'Jan': [150, 200, 50],
         'Feb': [200, 210, 90],
         'Mar': [140, 215, 95]}
df = pd.DataFrame.from_dict(sales)
print df