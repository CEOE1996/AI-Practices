import math

def af(x):
    return 4 * (x ** 3) + 15 * (x ** 2) + 8 * x - 4

def af1(x):
    return 12 * (x ** 2) + 30 * x + 8

def bf(x):
    return (x - 5) ** 2

def bf1(x):
    return 2 * (x - 5)

def cf(x):
    return math.sin(2 * x)

def cf1(x):
    return math.cos(2 * x) * 2

x0 = float(input('Introduce el valor inicial: '))
print('\nfunción: 4x^3 + 15x^2 + 8x - 4')
x1 = x0
for i in range(20):
    x1 = x1 - af(x1) / af1(x1)
    print(i, ': ', x1)

print('\nfunción: (x - 5)^2')
x1 = x0

for i in range(20):
    x1 = x1 - bf(x1) / bf1(x1)
    print(i, ': ', x1)

print('\nfunción: sin(2x)')
x1 = x0

for i in range(20):
    x1 = x1 - cf(x1) / cf1(x1)
    print(i, ': ', x1)
