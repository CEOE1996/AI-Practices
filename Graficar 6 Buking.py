from random import *
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

xl, xu, yl, yu = -15,  -5, -3, 3

x, y = np.meshgrid(np.arange(xl, xu, 0.1), np.arange(yl, yu, 0.1))

z = (100 * np.sqrt(np.absolute(y - 0.01*x ** 2))) + (0.01 * np.absolute(x+10))

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, z, cmap=cm.PuOr,linewidth=0, antialiased=False)
fig.colorbar(surf)
plt.title('Buking')
plt.show()


