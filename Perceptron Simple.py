import numpy as np
import matplotlib.pyplot as plt

o = 1.5
w1 = w2 = 1

def funAct(x):
    return x[0] * w1 + x[1] * w2 - o > 0

def getY(x):
    a = o / w2
    m = -w1 / w2
    return a + m * x

x = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

c = []

for i in x:
    c.append('g' if funAct(i) else 'r')

lx = np.arange(-1, 3)
ly = getY(lx)

plt.scatter(x[:,0], x[:,1], c = c)
plt.plot(lx, ly)

plt.show()