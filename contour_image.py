import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
	#the height function
	return (1 - x / 2 + x ** 5 + y ** 5)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n);
y = np.linspace(-3,3,n);
X,Y = np.meshgrid(x,y)

#plot contourf  color	12 -> 对等高线的分段数目
plt.contourf(X,Y,f(X,Y),6,alpha = 0.75,cmap = plt.cm.hot)

#add contour lines
C = plt.contour(X,Y,f(X,Y),6,colors = 'black',linewidth=0.5)

plt.clabel(C,inline = True, fontsize=10)
plt.xticks(())
plt.yticks(())
plt.show()