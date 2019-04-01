from random import *
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

A = np.array([[2, 1, 0], [4, 3, 5], [1, 0, 2], [3, 1, 10]])
b = np.array([8, 25, 4, 20])

def f(x):
    return np.linalg.norm(b - np.matmul(A, x), 2)

D = 3
G = 100
L = 20
N = 100

Pf = 50
Po = N - Pf

xl = np.array([-10, -10, -10])
xu = np.array([10, 10, 10])

Aptitud = np.zeros(Pf).tolist()
li = np.zeros(Pf).tolist()
x = np.zeros((D, Pf))
v = np.zeros((D, N))

for i in range(Pf):
    x[:, i] = xl + (xu - xl) * random()
    Aptitud[i] = f(x[:, i])

for a in range(G):    
    #Abejas Empleadas
    for i in range(Pf):

        k = i

        while k == i:
            k = randint(0, Pf - 1)
        
        j = randint(0, D - 1)

        o = uniform(-1, 1)

        v[j, i] =  x[j, i] + o * (x[j, i] - x[j, k])
        
        AptitudV = f(v[:, i]) 
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
        
        AptitudV = f(v[:, m])
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
            Aptitud[i] = f(x[:, i])
            li[i] = 0

    ind = Aptitud.index(min(Aptitud))

    print(a, "- f(x):", min(Aptitud), "x:", x[0, ind], "y:", x[1, ind], "y:", x[2, ind], )
