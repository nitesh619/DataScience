import numpy as np
import pandas as pd

# df = pd.read_csv('train.csv')
# print(df)

ls = [1,2,2,3,4,45]

ser1 = pd.Series(ls)
print(ser1)

labels = ['a', 'b', 'c','d','e','f']
ser2 = pd.Series(data=ls, index=labels)
print(ser2)
ser2 = ser2.add_prefix('XXXXXXXXXXXXXXXXXXX')
print ser2
np_arr = np.array(ls)

ser3 = pd.Series(np_arr)
print(ser3)

dic = {'I': 'one', 'II': 'two', 'III':'three'}
ser3 = pd.Series(dic)
print(ser3)

search_leads = pd.DataFrame([], [], ['Name', 'Handle', 'Verified', 'Bio', 'Profile_Link'])
ll = pd.DataFrame([], [], ['Name', 'Handle', 'Verified', 'Bio', 'Profile_Link'])

search_leads['Name'] = pd.Series(['aaa', 'aaa', 'gfg', 'gf', 'rer'])
ll['Name'] = pd.Series(['cc', '45tre', 'cxvc', '12sa', 'csd'])
search_leads['Profile_Link'] = search_leads['Name'] + "cdc"
search_leads.drop_duplicates(subset=['Name'],keep=False, inplace=True)
search_leads.reset_index(drop=True,inplace=True)
print search_leads
print ll
search_leads = pd.concat([search_leads, ll])
print search_leads