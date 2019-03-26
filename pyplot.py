import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50);
y = 2*x + 1;
y1 = x**2 + 1;

plt.figure(num = 3,figsize = (8,5))
l1 = plt.plot(x,y,label = 'y = 2x+1')
plt.plot(x,y1,color = 'red',linewidth = 5.0,linestyle = '-.',label = 'y = x^2+1')
plt.legend(handles = l1,loc = 'upper right')
#plt.legend()
plt.xlim((-2,1))
plt.ylim((-2,3))
plt.xlabel('xxxxlabel')
plt.ylabel('yyyylabel')

x_ticks = np.linspace(-1,2,5)
plt.xticks(x_ticks)
plt.yticks([0,1,2],['a','b',r'$c\ \alpha$'])

#gca = get current axis
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',-1))
ax.spines['left'].set_position(('data',0))


x0 = 1;
y0 = 2*x0 + 1;
plt.scatter(x0,y0,s = 50,color = 'b')
plt.plot([x0,x0],[y0,0],'k--',lw = 2.5)
plt.plot([x0,0],[y0,y0],'k--',lw = 2.5)

for label in ax.get_xticklabels() + ax.get_yticklabels() :
	label.set_bbox(dict(facecolor = 'blue',edgecolor = 'NONE',alpha = 0.7))

plt.show()
