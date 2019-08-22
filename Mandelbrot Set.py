import numpy as np 
import matplotlib.pyplot as plt 

MaxIter = 80
Res = 300

def iterate(c):
    z = complex(0, 0)
    n = 0

    while abs(z) < 2 and n < MaxIter:
        z = z * z + c
        n += 1
    
    return n

def Mandelbrot():
    I = np.zeros((Res, Res))

    for i, x in enumerate(np.linspace(-2, 2, Res)):
        for j, y in enumerate(np.linspace(-2, 2, Res)):
            c = complex(x, y)
            n = iterate(c)

            if n == MaxIter:
                I[j, i] = 0
            else:
                I[j, i] = int(255 / MaxIter) * n
    
    plt.imshow(I)
    plt.title('Conjunto de Mandelbrot')
    plt.show()
    plt.imsave('Mandelbrot.jpg', I)

Mandelbrot()