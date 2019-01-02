import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('POP_TOTAL_DS2_en_v2.csv')
#df.interpolate(inplace=True)

df1 = df[(df['Country Code'] == 'ALB')]
df1 = df1.T
df1 = df1[4:]
print(df1)
plt.plot(df1)
plt.show()