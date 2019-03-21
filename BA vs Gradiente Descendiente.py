import random
import math

def f(x, y):
    return x * math.exp(-x ** 2 - y ** 2)

def dpx(x):
    return math.exp(-x ** 2 - y ** 2) - 2 * math.exp(-x ** 2 - y ** 2) * x ** 2

def dpy(x):
    return -2 * math.exp(-x ** 2 - y ** 2) * x * y

fbest = 999999
xbest = xbest = fval = x = y = 0
xl = yl = -2
xu = yu = 2

print('\nBusqueda Aleatoria 2')
for i in range(10000):
    x = xl + (xu - xl) * round(random.random(), 4)
    y = yl + (yu - yl) * round(random.random(), 4)
    fval = f(x, y)
    if(fval < fbest):
        fbest = fval
        xbest = x
        ybest = y

print('fbest:', fbest) 
print('xbest', xbest) 
print('ybest', ybest)

x = 0.5
y = 0
h = 0.1

print('\nGradiente Descendiente')
for i in range(10000):
    x = x - h * dpx(x)
    y = y - h * dpy(y)

print('f:', f(x, y))
print('x:', x)
print('y:', y)
