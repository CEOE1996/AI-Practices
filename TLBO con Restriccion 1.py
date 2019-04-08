from random import *
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def f(x, y):
    return np.sin(x + y) + ((x - y) ** 2) + (-1.5 * x) + (2.5 * y) + 1

def fp(x, xl, xu, D):
    return f(x[0], x[1]) + 1000 * penalizacion(x, xl, xu, D) 

def penalizacion(x, xl, xu, D):
    z = 0
    for i in range(D):
        if xl[i] > x[i]:
            z = z + 1
        elif xu[i] < x[i]:
            z = z + 1

    return z

D = 2
G = 100
L = 20
N = 100

xl = np.array([-1.4, -3])
xu = np.array([4, 4])

Aptitud = np.zeros(N).tolist()
x = np.zeros((D, N))

for i in range(N):
    x[:, i] = xl + (xu - xl) * random()
    Aptitud[i] = f(x[0, i], x[1, i])

Resultados = []

LastF = LastX = LastY = 0

for a in range(G):    
    for i in range(N):
        #Fase de Ensenanza
        t = Aptitud.index(min(Aptitud))
        Tf = randint(1, 2)
        
        c = np.zeros(D)

        for j in range(D):
            avg = np.mean(x[j])
            c[j] = x[j, i] + random() * (x[j, t] - Tf * avg)

        FitC = fp(c, xl, xu, D)

        if FitC < Aptitud[i]:
            x[:, i] = c
            Aptitud[i] = FitC

        #Fase de Aprendizaje
        k = i

        while k == i:
            k = randint(0, N - 1)
        
        c = np.zeros(D)

        if Aptitud[i] < Aptitud[k]:
            for j in range(D):
                c[j] = x[j, i] + random() * (x[j, i] - x[j, k])
        else:
            for j in range(D):
                c[j] = x[j, i] + random() * (x[j, k] - x[j, i])

        FitC = fp(c, xl, xu, D)

        if FitC < Aptitud[i]:
            x[:, i] = c
            Aptitud[i] = FitC
        
    ind = Aptitud.index(min(Aptitud))

    print(a, "- f(x):", min(Aptitud), "x:", x[0, ind], "y:", x[1, ind])
    LastF, LastX, LastY = min(Aptitud), x[0, ind], x[1, ind]
    Resultados.append(min(Aptitud))


#Graficar Fitness
plt.plot(Resultados)
plt.ylabel('F(x, y)')
plt.xlabel('Generaciones')
plt.show()

xl = np.array([-1.5, 4])
xu = np.array([-3, 4])

x, y = np.meshgrid(np.arange(xl[0], xl[1], 0.1), np.arange(xu[0], xu[1], 0.1))

z = f(x, y)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(x, y, z, cmap=cm.PuOr,linewidth=0, antialiased=False)
ax.scatter(LastX, LastY, LastF, c='g')

plt.show()
