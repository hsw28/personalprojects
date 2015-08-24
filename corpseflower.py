import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
from pylab import plotfile, show, gca

data1 = np.genfromtxt('corpseflower.csv', delimiter=',', skip_header=1, names=['a','b','c','d', 'e', 'f'])

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(data1['a'], data1['c'], color='r', linewidth=3, label='Spike')
ax1.plot(data1['a'], data1['d'], color='b', linewidth=3, label='StinkyDGB')
ax1.plot(data1['a'], data1['e'], color='g', linewidth=3, label='Huntington 2014')
ax1.plot(data1['a'], data1['f'], color='indigo', linewidth=3, label='Gustavus 2007 (first bloom)')

#plt.axis([0,13,0,100])

plt.legend(loc=2)
plt.xlabel('Day')
plt.ylabel('Height')

plt.title('Comparison of Spike and StinkyDGB, ending with StinkyDGB Bloom')

show()