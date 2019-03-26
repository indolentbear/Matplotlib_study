import matplotlib.pyplot as plt
import numpy as np

a = np.array([[0.3125648,0.5264648,0.3182618],
			 [0.1235629,0.7563252,0.2222222],
			 [0.5236412,0.9333333,0.8256432]]);

plt.imshow(a,interpolation='NONE',cmap='bone',origin='upper')
plt.colorbar()

plt.yticks(())
plt.xticks(())
plt.show()