import random

def f(x, y):
    return (x - 2) ** 2 + (y - 2) ** 2

fbest = 999999
xbest = xbest = fval = x = y = 0
xl = yl = -5
xu = yu = 5
counter = 0

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