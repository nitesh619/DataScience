import numpy as np
import pandas as pd

np.random.seed(101)
out=['G1','G1','G1','G2','G2','G2']
ins=[1,2,3,1,2,3]
#print(np.random.randn(5,4))
df=pd.DataFrame(np.random.randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
#print(df)
hier_index= list(zip(out,ins))
print(hier_index)
hier_index=pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
df= pd.DataFrame(np.random.rand(6,2),hier_index,['A','B'])
print(df)
df.index.names=['Group','num']
print(df)
print(df.loc['G2'])
print(df.loc['G2'].loc[2]['B'])
print('cross section')
#cross section
print(df.xs('G1'))
print(df.xs(1,level='num'))