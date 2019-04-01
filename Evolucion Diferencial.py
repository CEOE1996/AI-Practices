from random import *
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def f(x, y):
    # return (2 * x ** 2) + (-1.05 * x ** 4) + (x ** 6 / 6) + (x * y) + (y ** 2) 
    return ((1.5 - x + x*y)**2) + ((2.25 - x + x*y**2)**2) + ((2.625 - x + x*y**3)**2)
    # return (100 * np.sqrt(np.absolute(y - 0.01*x ** 2))) + (0.01 * np.absolute(x+10))

D = 2
G = 100
N = 50

C = 0.6
F = 0.8

#Three-Hump Camel 
#xl = np.array([-5, -5])
#xu = np.array([5, 5])

#Beale
xl = np.array([-4.5, -4.5])
xu = np.array([4.5, 4.5])

#Buking
# xl = np.array([-15, -3])
# xu = np.array([-5, 3])

Fitness = np.zeros(N).tolist()
x = np.zeros((D, N))
v = np.zeros((D, N))

for i in range(N):
    x[:, i] = xl + (xu - xl) * random()
    Fitness[i] = f(x[0, i], x[1, i])

Resultados = []

LastF = LastX = LastY = 0

for i in range(G):
    for j in range(N):

        r1 = r2 = r3 = j

        while r1 == r2 or r2 == r3 or r3 == r1:
            r1 = randint(0, N - 1)
            r2 = randint(0, N - 1)
            r3 = randint(0, N - 1)
        
        v[:, j] =  x[:, r1] + F * (x[:, r2] - x[:, r3])
        

        u = np.zeros(D)

        for k in range(D):
            r = random()
            
            if(r <= C):
                u[k] = v[k, j]
            else :
                u[k] = x[k, j]

        new = f(u[0], u[1])
        
        #print('new:', new, 'Fit:', Fitness[j])

        if new < Fitness[j]:
            x[:, j] = u
            Fitness[j] = new
            


    ind = Fitness.index(min(Fitness))

    print(i, "- f(x):", min(Fitness), "x:", x[0, ind], "y:", x[1, ind])
    LastF, LastX, LastY = min(Fitness), x[0, ind], x[1, ind]
    Resultados.append(min(Fitness))


#Graficar Resultados
plt.plot(Resultados)
plt.ylabel('F(x, y)')
plt.xlabel('Generaciones')
plt.show()

xl = np.array([-4.5, 4.5])
xu = np.array([-4.5, 4.5])

x, y = np.meshgrid(np.arange(xl[0], xl[1], 0.1), np.arange(xu[0], xu[1], 0.1))

z = f(x, y)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(x, y, z, cmap=cm.PuOr,linewidth=0, antialiased=False)
ax.scatter(LastX, LastY, LastF, c='g')

plt.show()
