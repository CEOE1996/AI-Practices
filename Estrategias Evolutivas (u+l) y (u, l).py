from random import *
import math
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    #return x * math.exp(-x ** 2 - y ** 2)
    return (x-2) ** 2 + (y-2) ** 2;

mu = 100
D = 2
G = 100
lamda = 150 #100 para (u + l)-ES, 150 para (u, l)-ES
xl = np.array([-2, -2])
xu = np.array([2, 2])

Fitness = np.zeros(mu + lamda).tolist()
Sigma = np.zeros((2, mu + lamda))
x = np.zeros((2, mu + lamda))

for i in range(mu):
    x[:, i] = xl + (xu - xl) * np.random.rand(D)
    Sigma[:, i] = np.random.rand(D)

Resultados = []

for i in range(G):
    for j in range(lamda):

        r1 = randint(0, mu - 1)
        r2 = r1

        while(r1 == r2):
            r2 = randint(0, mu - 1)

        x[:, mu + j] = (x[:, r1] + x[:, r2]) / 2
        Sigma[:,mu + j] = (Sigma[:, r1] + Sigma[:, r2]) / 2

        r = np.random.normal(0, Sigma[:, mu + j])
        x[:, mu + j] = x[:, mu + j] + r
        
    for j in range(mu + lamda):
        Fitness[j] = f(x[0, j], x[1, j])

    ind = np.argsort(Fitness)
    
    Fitness.sort()

    x = x[:, ind]
    Sigma = Sigma[:, ind]    

    print(i, "- f(x):", Fitness[0], "x:", x[0, 0], "y:", x[1, 0])
    Resultados.append(Fitness[0])

#Graficar Resultados
plt.plot(Resultados)
plt.ylabel('F(x, y)')
plt.xlabel('Generaciones')
plt.show()