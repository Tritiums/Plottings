import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import xlrd
import sys

ratio=0.438510336




fig=plt.figure()

plt.axis([0,160,0,90])

#Subplot ax
ax0=fig.add_subplot(1,1,1)

#currentAxis = plt.gca()

ax0.add_patch(Rectangle((60, 50), 20, 20, linewidth=0, facecolor="#7F7F7F"))

ax0.add_patch(Rectangle((10, 10), 20, 20, linewidth=0, facecolor="#4F81BD"))
ax0.add_patch(Rectangle((10, 10), ratio*20, 20, linewidth=0, facecolor="#C00000"))


plt.subplots_adjust(left=0.03, right=0.99,
                    bottom=0.04, top=0.99)

plt.show()
