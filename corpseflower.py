import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
from pylab import plotfile, show, gca

data1 = np.genfromtxt('corpse.csv', delimiter=',', skip_header=1, names=['a','b','c','d'])

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(data1['a'], data1['c'], color='r', linewidth=5, label='Spike')
ax1.plot(data1['a'], data1['d'], color='b', linewidth=5, label='StinkyDGB')

#plt.axis([0,13,0,100])

plt.legend(loc=2)
plt.xlabel('Day')
plt.ylabel('Height')

plt.title('Comparison of Spike and StinkyDGB, ending with StinkyDGB Bloom')

show()