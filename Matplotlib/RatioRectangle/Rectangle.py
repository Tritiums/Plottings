import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.patches import Rectangle
import xlrd
import sys

#Import File
filename='ALL clinical sample CFP10 ESAT6.xlsx'
book=xlrd.open_workbook(filename)
print('Source file: '+sys.path[0]+filename+' loaded!')

#Extraction
nsheets=book.nsheets

sheet_names=book.sheet_names()
nrows=book.sheet_by_name('Panel 01').nrows

header=book.sheet_by_name('Panel 01').row_values(0)
data=[book.sheet_by_name('Panel 01').row_values(i) for i in range(1, nrows)]
df=pd.DataFrame(data, columns=header)

coords_x=list(df.x)
coords_y=list(df.y)
coords_z=list(df.z)
sides=list(df.ratio)

coordinator=[]
for i in range(len(coords_x)):
    coordinator.append((coords_x[i], coords_y[i], coords_z[i], sides[i]))

#Create the figure object
fig=plt.figure()

plt.axis([0,20,0,13])

#Subplot ax
ax0=fig.add_subplot(1,1,1)

#currentAxis = plt.gca()
for x, y, z, ratio in coordinator:
    if z==0.5:
        ax0.add_patch(Rectangle((x, y), 0.8, .02, linewidth=0, facecolor="#7F7F7F"))
    else:
        ax0.add_patch(Rectangle((x, y), 1.2, .02, linewidth=0, facecolor="#4F81BD"))
        ax0.add_patch(Rectangle((x, y), ratio*1.2, .02, linewidth=0, facecolor="#C00000"))
    
plt.subplots_adjust(left=0.03, right=0.99,
                    bottom=0.04, top=0.99)

plt.show()
