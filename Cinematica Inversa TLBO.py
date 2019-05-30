from random import *
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.lines as mlines

def f(q):
    p = getP(q)

    return np.linalg.norm(p_final - p, 2) 

def fp(x, xl, xu, D):
    return f(x) + 1000 * penalizacion(x, xl, xu, D) 

def penalizacion(x, xl, xu, D):
    z = 0
    for i in range(D):
        if xl[i] > x[i]:
            z = z + 1
        elif xu[i] < x[i]:
            z = z + 1

    return z

def getP(q):
    p = np.array([0.0, 0.0, 0.0])
    p[0] = -math.sin(q[0] - math.pi / 2) * (l1 * math.cos(q[1]) + l2 * math.cos(q[1] + q[2]))
    p[1] = math.cos(q[0] - math.pi/2) * (l1 * math.cos(q[1]) + l2 * math.cos(q[1] + q[2]))
    p[2] = l1 * math.sin(q[1]) + l2 * math.sin(q[1] + q[2])
    return p

def getT(theta,a,d,alpha):
    return np.array([
                        [math.cos(theta), -math.sin(theta) * math.cos(alpha), math.sin(theta) * math.sin(alpha), a * math.cos(theta)],
                        [math.sin(theta), math.cos(theta) * math.cos(alpha), -math.cos(theta) * math.sin(alpha), a * math.sin(theta)],
                        [0, math.sin(alpha), math.cos(alpha), d],
                        [0, 0, 0, 1]
                    ])

def getF(p):
    T1 = getT(p[0], 0.0, 0.0, math.pi/2)
    T2 = getT(p[1], l1, 0.0, 0.0)
    T3 = getT(p[2], l2, 0.0, 0.0)
    
    T12 = np.multiply(T1, T2)
    T13 = np.multiply(T12, T3)

    # print(T1)
    # print(T12)
    # print(T13)

    f1 = T1[0:3, 3]
    f2 = T12[0:3, 3]
    f3 = T13[0:3, 3]

    return f1, f2, f3


p_final = np.array([0.5, 0.1, 0.3])

l1 = 0.5
l2 = 0.5

D = 3
G = 100
N = 100

xl = np.array([-160, -150, -135]) * (math.pi / 180)
xu = np.array([160, 150, 135]) * (math.pi / 180)

Aptitud = np.zeros(N).tolist()
x = np.zeros((D, N))

for i in range(N):
    x[:, i] = xl + (xu - xl) * random()
    Aptitud[i] = f(x[:, i])

Resultados = []

LastF = LastQ1 = LastQ2 = LastQ3 = 0

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

    print(a, "- f(x):", min(Aptitud), "q1:", x[0, ind], "q2:", x[1, ind], "q3:", x[2, ind])
    LastF, LastQ1, LastQ2, LastQ3 = min(Aptitud), x[0, ind], x[1, ind], x[2, ind]
    Resultados.append(min(Aptitud))

#Graficar Fitness
plt.plot(Resultados)
plt.ylabel('F(x, y)')
plt.xlabel('Generaciones')
plt.show()

# p = getP([LastQ1, LastQ2, LastQ3])

f1, f2, f3 = getF([LastQ1, LastQ2, LastQ3])

# print("p1:", p[0])
# print("p2:", p[1])
# print("p3:", p[2])
print("f1:", f1[0], f1[1], f1[2])
print("f2:", f2[0], f2[1], f2[2])
print("f3:", f3[0], f3[1], f3[2])

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(p_final[0], p_final[1], p_final[2], c='g', marker="x")

plt.show()
