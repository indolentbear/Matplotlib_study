import matplotlib.pyplot as plt
import numpy as np

x = np.arange(12);
y1 = (1 - x/float(12)) * np.random.uniform(0.5,1.0,12);
y2 = (1 - x/float(12)) * np.random.uniform(0.5,1.0,12);

plt.bar(x,+y1,facecolor = '#9900ff',edgecolor = 'blue')
plt.bar(x,-y1,facecolor = '#ff9999',edgecolor = 'red')

for x0,y0 in zip(x,y1):				#ha: horizontal alignment
	plt.text(x0,y0+0.05,'%.2f'%y0,ha = 'center',va = 'bottom')
for x0,y0 in zip(x,y2):
	plt.text(x0,-y0-0.05,'-%.2f'%y0,ha = 'center',va = 'top')

plt.xlim(-.5,12)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())

plt.show()