import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50);
y = 2*x + 1;
x1 = np.linspace(-3,3,50);
y1 = x**2 + 1;

l,b,w,h = 0.1,0.1,0.8,0.8
fig = plt.figure()
ax1 = fig.add_axes([l,b,w,h])
ax1.plot(x,y,'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

l,b,w,h = 0.2,0.6,0.25,0.25
ax2 = fig.add_axes([l,b,w,h])
ax2 = ax1.twinx
ax2.plot(x1,y1,'r')
# ax2.set_xlabel('x')
# ax2.set_ylabel('y')
# ax2.set_title('title')

plt.show()