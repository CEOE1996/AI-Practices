from random import *
import math
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x * math.exp(-x ** 2 - y ** 2)
    #return (x-2) ** 2 + (y-2) ** 2;

D = 2
G = 100
c = 0.817
n = 0
Sigma = 1

xl = np.array([-2, -2])
xu = np.array([2, 2])

x_p = xl + (xu - xl) * np.random.rand(D)

Resultados = []

for i in range(G):
    r = np.random.normal(0, Sigma ** 2, 2)
    x_h = x_p + r
    
    print(x_h)
    print("xp:", x_p)
    print("r:", r)

    if f(x_h[0], x_h[1]) < f(x_p[0], x_p[1]):
        x_p = x_h
        n += 1

    phi = n / (i + 1)
    
    if phi < 1/5:
        Sigma = c ** 2 * Sigma
    else:
        Sigma = Sigma / c ** 2;    

    print("f(x):", f(x_p[0], x_p[1]), "x:", x_p[0], "y:", x_p[1])
    Resultados.append(f(x_p[0], x_p[1]))


#Graficar Resultados
plt.plot(Resultados)
plt.ylabel('F(x, y)')
plt.xlabel('Generaciones')
plt.show()