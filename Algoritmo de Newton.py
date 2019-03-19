import math

def af1(x):
    return 4 * (x ** 3) + 15 * (x ** 2) + 8 * x - 4

def af2(x):
    return 12 * (x ** 2) + 30 * x + 8

def bf1(x):
    return math.cos(2 * x) * 2

def bf2(x):
    return -4 * math.sin(2 * x)

def cf1(x):
    return 2 * math.cos(x) - x * math.sin(x)

def cf2(x):
    return -3 * math.sin(x) - x * math.cos(x)

print('\nfunción: x^4 + 5x^3 + 4x^2 - 4x + 1')
x0 = float(input('Introduce el valor inicial: '))
print('Valor Inicial: ', x0)
x1 = x0

for i in range(20):
    x1 = x1 - af1(x1) / af2(x1)
    print(i, ': ', x1)

print('\nfunción: sin(2x)')
x0 = float(input('Introduce el valor inicial: '))
print('Valor Inicial: ', x0)
x1 = x0

for i in range(20):
    x1 = x1 - bf1(x1) / bf2(x1)
    print(i, ': ', x1)

print('\nfunción: sin(x + xcos(x))')
x0 = float(input('Introduce el valor inicial: '))
print('Valor Inicial: ', x0)
x1 = x0

for i in range(20):
    x1 = x1 - cf1(x1) / cf2(x1)
    print(i, ': ', x1)
