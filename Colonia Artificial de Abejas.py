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

Pf = 50
Po = N - Pf

#Three-Hump Camel 
# xl = np.array([-5, -5])
# xu = np.array([5, 5])

#Beale
# xl = np.array([-4.5, -4.5])
# xu = np.array([4.5, 4.5])

#Buking
xl = np.array([-15, -3])
xu = np.array([-5, 3])

Aptitud = np.zeros(Pf).tolist()
li = np.zeros(Pf).tolist()
x = np.zeros((D, Pf))
v = np.zeros((D, N))

for i in range(Pf):
    x[:, i] = xl + (xu - xl) * random()
    Aptitud[i] = f(x[0, i], x[1, i])

Resultados = []

LastF = LastX = LastY = 0

for a in range(G):    
    #Abejas Empleadas
    for i in range(Pf):

        k = i

        while k == i:
            k = randint(0, Pf - 1)
        
        j = randint(0, D - 1)

        o = uniform(-1, 1)

        v[j, i] =  x[j, i] + o * (x[j, i] - x[j, k])
        
        AptitudV = f(v[0, i], v[1, i]) 
        if(AptitudV < Aptitud[i]):
            x[:, i] = v[:, i]
            Aptitud[i] = AptitudV
            li[i] = 0
        else:
            li[i] += 1

    #Abejas Observadoras
    for i in range(Po):
        m = randint(0, Pf - 1)

        k = m

        while k == m:
            k = randint(0, Pf - 1)
        
        j = randint(0, D - 1)

        o = uniform(-1, 1)

        v[j, m] =  x[j, m] + o * (x[j, m] - x[j, k])
        
        AptitudV = f(v[0, m], v[1, m])
        if(AptitudV < Aptitud[m]):
            x[:, m] = v[:, m]
            Aptitud[m] = AptitudV
            li[m] = 0
        else:
            li[m] += 1

    #Abejas Exploradoras
    for i in range(Pf):
        if(li[i] > L):
            x[:, i] = xl + (xu - xl) * random()
            Aptitud[i] = f(x[0, i], x[1, i])
            li[i] = 0

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
