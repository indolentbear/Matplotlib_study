import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec

#method 1: subplot
plt.figure()

x = np.linspace(-3,3,50);
y = 2*x + 1;
x1 = np.linspace(-3,3,50);
y1 = x**2 + 1;

plt.subplot(1,2,1)
plt.plot(x,y,color = 'red',linewidth = 0.5,linestyle = '-.',label = 'y = x*2+1')

plt.subplot(122)
plt.plot(x1,y1,color = 'red',linewidth = 0.5,linestyle = '-.',label = 'y = x**2+1')

plt.show()

#method 2: subplot2grid
plt.figure()
ax1 = plt.subplot2grid((3,3),(0,0),colspan = 3,rowspan = 1)
									#col / rowspan 代指图像的长、高
ax1.plot([1,2],[1,2])
ax1.set_title('ax1_title')

#method 3:gridspec
plt.figure()
gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,:2])
ax3 = plt.subplot(gs[1:,3])

#method 4:easy to define structure
f,((ax11,ax12),(ax21,ax22)) = plt.subplots(3,3,sharex = True, sharey = True)
ax11.scatter([1,2][1,2])



plt.show()