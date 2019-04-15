from random import *
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def f(x, y):
    # return (2 * x ** 2) + (-1.05 * x ** 4) + (x ** 6 / 6) + (x * y) + (y ** 2) 
    # return ((1.5 - x + x*y)**2) + ((2.25 - x + x*y**2)**2) + ((2.625 - x + x*y**3)**2)
    return (100 * np.sqrt(np.absolute(y - 0.01*x ** 2))) + (0.01 * np.absolute(x+10))

D = 2
G = 100
L = 20
N = 100

# #Three-Hump Camel 
# xl = np.array([-5, -5])
# xu = np.array([5, 5])

#Beale
# xl = np.array([-4.5, -4.5])
# xu = np.array([4.5, 4.5])

#Buking
xl = np.array([-15, -3])
xu = np.array([-5, 3])

Aptitud = np.zeros(N).tolist()
x = np.zeros((D, N))
v = np.zeros((D, N))

for i in range(N):
    x[:, i] = xl + (xu - xl) * random()
    Aptitud[i] = f(x[0, i], x[1, i])

Resultados = []

LastF = LastX = LastY = 0

for a in range(G):    
    for i in range(N):
        k = i

        while k == i:
            k = randint(0, N - 1)
        
        j = randint(0, D - 1)

        o = uniform(-1, 1)

        v[j, i] =  x[j, i] + o * (x[j, i] - x[j, k])
        
        AptitudV = f(v[0, i], v[1, i]) 
        if(AptitudV < Aptitud[i]):
            x[:, i] = v[:, i]
            Aptitud[i] = AptitudV

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

        FitC = f(c[0], c[1])

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

#Three-Hump Camel 
# xl = np.array([-5, 5])
# xu = np.array([-5, 5])

#Beale
# xl = np.array([-4.5, 4.5])
# xu = np.array([-4.5, 4.5])

#Buking
xl = np.array([-15, -5])
xu = np.array([-3, 3])

x, y = np.meshgrid(np.arange(xl[0], xl[1], 0.1), np.arange(xu[0], xu[1], 0.1))

z = f(x, y)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(x, y, z, cmap=cm.PuOr,linewidth=0, antialiased=False)
ax.scatter(LastX, LastY, LastF, c='g')

plt.show()
