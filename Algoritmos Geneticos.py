from random import *
import math
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    #return x * math.exp(-x ** 2 - y ** 2)
    return (x-2) ** 2 + (y-2) ** 2;

def Seleccion(Aptitud):
    AptitudLen = len(Aptitud)
    AptitudTotal = sum(Aptitud)
    P = np.zeros(AptitudLen).tolist()
    R = random()
    Psum = 0

    for i in range(AptitudLen):
        P[i] = Aptitud[i] / AptitudTotal

    for i in range(AptitudLen):
        Psum += P[i]
        if(Psum >= R):
            return i

    return AptitudLen

N = 100
D = 2
pm = 0.01
G = 150

xl = np.array([-2, -2])
xu = np.array([2, 2])

Aptitud = np.zeros(N).tolist()
Padres = np.zeros((2, N))

for i in range(N):
    MR = np.array([random(), random()])
    Padres[:, i] = xl + (xu - xl) * MR

Resultados = []

for i in range(G):
    for j in range(N):
        fx = f(Padres[0, j], Padres[1, j])

        if(fx >= 0):
            Aptitud[j] = 1 / (1 + fx)
        else:
            Aptitud[j] = 1 + abs(fx)

    A = Aptitud.index(max(Aptitud))
    Resultados.append((f(Padres[0, A], Padres[1, A]), Padres[0, A], Padres[1, A]))

    Hijos = np.zeros((2, N))

    for j in range(int(N / 2)):
        Padre = Seleccion(Aptitud)
        Madre = Padre

        while(Padre != Madre):
            Madre = Seleccion(Aptitud)

        P = Padres[:, Padre]
        M = Padres[:, Madre]

        H1 = Padres[:, Padre]
        H2 = Padres[:, Madre]

        Cruce = randint(0, D - 1)
        H1[Cruce : D - 1] = M[Cruce : D - 1]
        H2[Cruce : D - 1] = P[Cruce : D - 1]

        Hijos[:, j * 2 - 1] = H1
        Hijos[:, j * 2] = H2

    for j in range(N):
        for k in range(D):
            if random() <= pm:
                Hijos[k, j] = xl[k] + (xu[k] - xl[k]) * random()
    
    Padres = Hijos


#print(Padres)
R = []
for i in Resultados:
    print("fx:", i[0], "xg:", i[1], "yg:", i[2])
    R.append(i[0])

#Graficar Resultados
plt.plot(R)
plt.ylabel('F(x, y)')
plt.xlabel('Generaciones')
plt.show()
