from random import *
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

X = np.array([0.0690, 0.2760, 0.3866, 0.6546, 0.8422, 0.5708])
Y = np.array([0.4500, 0.7600, 0.9500, 1.4000, 1.7300, 1.2300])

def f(x, y):
    r = 0
    for i in range(len(Y)):
        r += 0.5 * (Y[i] - (x * X[i] + y)) ** 2 
    return r

D = 2
G = 100
L = 20
N = 100

xl = np.array([-5, -5])
xu = np.array([5, 5])

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



# plt.plot(X,Y,'b*','LineWidth',2,'MarkerSize',10)
# plt.plot(x,y,'g-','LineWidth',2,'MarkerSize',10)
# plt.ylabel('y')
# plt.xlabel('x')
# plt.show()
