from random import *
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

xl, xu, yl, yu = -5, 5, -5, 5

x, y = np.meshgrid(np.arange(xl, xu, 0.1), np.arange(yl, yu, 0.1))

z = (2 * x ** 2) + (-1.05 * x ** 4) + (x ** 6 / 6) + (x * y) + (y ** 2) 

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, z, cmap=cm.PuOr,linewidth=0, antialiased=False)
fig.colorbar(surf)
plt.title('Three-Hump Camel')
plt.show()
