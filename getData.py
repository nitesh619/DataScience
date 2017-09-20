import pandas as pd
import numpy as np

# df = pd.read_csv('train.csv')
# print(df)

ls = [1,2,2,3,4,45]

ser1 = pd.Series(ls)
print(ser1)

labels = ['a', 'b', 'c','d','e','f']
ser2 = pd.Series(data=ls, index=labels)
print(ser2)

np_arr = np.array(ls)

ser3 = pd.Series(np_arr)
print(ser3)

dic = {'I': 'one', 'II': 'two', 'III':'three'}
ser3 = pd.Series(dic)
print(ser3)

