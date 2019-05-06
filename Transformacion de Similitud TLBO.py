from random import *
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.lines as mlines

def f(dx, dy, s, o):
    ax, ay = Trans(xi[0, 0], xi[0, 1], dx, dy, s, o)
    bx, by = Trans(xi[1, 0], xi[1, 1], dx, dy, s, o)
    cx, cy = Trans(xi[2, 0], xi[2, 1], dx, dy, s, o)

    return DifEuclides(xf[0, 0], xf[0, 1], ax, ay) + DifEuclides(xf[1, 0], xf[1, 1], bx, by) + DifEuclides(xf[2, 0], xf[2, 1], cx, cy)

def fp(x, xl, xu, D):
    return f(x[0], x[1], x[2], x[3]) + 1000 * penalizacion(x, xl, xu, D) 

def penalizacion(x, xl, xu, D):
    z = 0
    for i in range(D):
        if xl[i] > x[i]:
            z = z + 1
        elif xu[i] < x[i]:
            z = z + 1

    return z

def DifEuclides(x, y, xi, yi):
    return math.sqrt((x - xi) ** 2 + (y - yi) ** 2)


def Trans(ax, ay, dx, dy, s, o):
    xp = ax * s * math.cos(o) - ay * s * math.sin(o) + dx
    yp = ax * s * math.sin(o) + ay * s * math.cos(o) + dy
    return xp, yp

xi = np.array([[1, 1], [2, 4], [3, 1]])
xf = np.array([[-3.121320, 2], [-7.363961, -0.121320], [-5.242641, 4.121320]])


D = 4
G = 100
N = 100

xl = np.array([-10, -10, -math.pi, 0])
xu = np.array([10, 10, math.pi, 5])

Aptitud = np.zeros(N).tolist()
x = np.zeros((D, N))

for i in range(N):
    x[:, i] = xl + (xu - xl) * random()
    Aptitud[i] = f(x[0, i], x[1, i], x[2, i], x[3, i])

Resultados = []

LastF = LastDX = LastDY = LastO = LastS = 0

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

    print(a, "- f(x):", min(Aptitud), "dx:", x[0, ind], "dy:", x[1, ind], "s:", x[2, ind], "o:", x[3, ind])
    LastF, LastDX, LastDY, LastS, LastO = min(Aptitud), x[0, ind], x[1, ind], x[2, ind], x[3, ind]
    Resultados.append(min(Aptitud))

#Graficar Fitness
plt.plot(Resultados)
plt.ylabel('F(x, y)')
plt.xlabel('Generaciones')
plt.show()

plt.plot(xi[:, 0], xi[:, 1], 'go-')
plt.plot(xf[:, 0], xf[:, 1], 'ro-')

ax, ay = Trans(xi[0, 0], xi[0, 1], LastDX, LastDY, LastS, LastO)
bx, by = Trans(xi[1, 0], xi[1, 1], LastDX, LastDY, LastS, LastO)
cx, cy = Trans(xi[2, 0], xi[2, 1], LastDX, LastDY, LastS, LastO)

plt.plot([ax, bx, cx], [ay, by, cy], 'b^-')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Transformacion de Similitud')

green_line = mlines.Line2D([], [], color='green', marker='o', markersize=10, label='Origen')
red_line = mlines.Line2D([], [], color='red', marker='o', markersize=10, label='Destino')
blue_line = mlines.Line2D([], [], color='blue', marker='^', markersize=10, label='Solucion')
plt.legend(handles=[green_line, red_line, blue_line])

plt.axis([-10, 10, -10, 10])
plt.show()
