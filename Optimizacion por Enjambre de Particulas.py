from random import *
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def f(x, y):
    #return (2 * x ** 2) + (-1.05 * x ** 4) + (x ** 6 / 6) + (x * y) + (y ** 2) 
    #return ((1.5 - x + x*y)**2) + ((2.25 - x + x*y**2)**2) + ((2.625 - x + x*y**3)**2)
    return (100 * np.sqrt(np.absolute(y - 0.01*x ** 2))) + (0.01 * np.absolute(x+10))

D = 2
G = 100
N = 50
w = 0.6
c1 = c2 = 2

#Three-Hump Camel 
#xl = np.array([-5, 5])
#xu = np.array([-5, 5])

#Beale
# xl = np.array([-4.5, 4.5])
# xu = np.array([-4.5, 4.5])

#Buking
xl = np.array([-15, -5])
xu = np.array([-3, 3])

Fitness = np.zeros(N).tolist()
x = np.zeros((D, N))
v = np.zeros((D, N))
best = np.zeros((D, N))

for i in range(N):
    x[:, i] = xl + (xu - xl) * np.random.rand(D)
    v[:, i] = np.ones(D) + 2 * np.random.rand(D)
    best[:, i] = x[:, i]
    
    Fitness[i] = f(x[0, i], x[1, i])

Resultados = []

LastF = LastX = LastY = 0

for i in range(G):
    for j in range(N):

        new = f(x[0, j], x[1, j])

        if new < Fitness[j]:
            Fitness[j] = new
            best[:, j] = x[:, j]

    ind = Fitness.index(min(Fitness))

    for j in range(N):
        v[:, j] = w * v[:, j] + random() * c1 * (best[:, j] - x[:, j]) + random() * c2 * (x[:, ind] - x[:, j])
        x[:, j] = x[:, j] + v[:, j]

    print(i, "- f(x):", min(Fitness), "x:", x[0, ind], "y:", x[1, ind])
    LastF, LastX, LastY = min(Fitness), x[0, ind], x[1, ind]
    Resultados.append(min(Fitness))


#Graficar Resultados
plt.plot(Resultados)
plt.ylabel('F(x, y)')
plt.xlabel('Generaciones')
plt.show()

x, y = np.meshgrid(np.arange(xl[0], xl[1], 0.1), np.arange(xu[0], xu[1], 0.1))

z = f(x, y)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(x, y, z, cmap=cm.PuOr,linewidth=0, antialiased=False)
ax.scatter(LastX, LastY, LastF, c='g')

plt.show()
