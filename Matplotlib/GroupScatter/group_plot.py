import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd

#Load Files
filename='raw.xlsx'
book=xlrd.open_workbook(filename)
print('Source file: '+filename+' loaded!')

#Extraction
nsheets=book.nsheets

sheet_names=book.sheet_names()
nrows=book.sheet_by_name('Sheet1').nrows

header=book.sheet_by_name('Sheet1').row_values(0)
data=[book.sheet_by_name('Sheet1').row_values(i) for i in range(1, nrows)]
df=pd.DataFrame(data, columns=header)
df=df.replace('', np.nan)

#Grouping
group=[]
for i in range(0, nrows-1):
    if df.ix[i]['ID'][0:16]=='Elite Controller':
        group.append(df.ix[i]['ID'][0:16])
    
    if df.ix[i]['ID'][0:14]=='HIV-1 negative':
        group.append(df.ix[i]['ID'][0:14])
        
    if df.ix[i]['ID'][0:13]=='HAART treated':
        group.append(df.ix[i]['ID'][0:13])

s=pd.Series(group)

df=pd.concat([df, s], axis=1)
column_list=list(df.columns)
column_list[-1]='Group'
df.columns=column_list

#Triming Data Frame
df=df[[1896.0,'DUSP6','Group']]
groups=df.groupby('Group')

#Plotting
fig, ax = plt.subplots()
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
for name, group in groups:
    ax.plot(group[1896.0], group['DUSP6'], marker='o', linestyle='', ms=8, label=name)
ax.legend()
plt.show()
