import pandas as pd
import numpy as np

df = pd.read_csv('train.csv')
df.interpolate(inplace=True)
print(df.describe())
print(df.describe(include=[object]))
print(df.columns)
print(df.head(5))
print(df['Credit_History'])

df['Gender'] = df['Gender'].replace(np.nan, 'Male', regex=True)
df['Married'] = df['Gender'].replace(np.nan, 'Male', regex=True)
df['Dependent'] = df['Gender'].replace(np.nan, 'Male', regex=True)
df['Self_Employed'] = df['Gender'].replace(np.nan, 'Male', regex=True)
df['LoanAmount'] = df['Gender'].replace(np.nan, 'Male', regex=True)
df['Gender'] = df['Gender'].replace(np.nan, 'Male', regex=True)
