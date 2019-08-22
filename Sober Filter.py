import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

I = mpimg.imread('3.jpg')

plt.imshow(I)
plt.show()

h, w, l = I.shape

ig = np.zeros((h, w))

for i in range(h):
    for j in range(w):
        ig[i, j] = (int(I[i, j, 0]) + int(I[i, j, 1]) + int(I[i, j, 2])) / 3

plt.imshow(ig)
plt.show()

s = np.array([[-1, 0, 1], [-2, 0, 2], [-3, 0, 3]])
ib = np.zeros((h - 2, w - 2))

If = np.zeros((h - 2, w - 2))

for i in range(1, h - 1):
    for j in range(1, w - 1):
        itemp = ig[i - 1 : i + 2, j - 1 : j + 2]
        temp = np.abs((s * itemp).sum())

        ib[i - 1, j - 1] = temp

        if temp > 24:
            If[i - 1, j - 1] = True
        else:
            If[i - 1, j - 1] = False

plt.imshow(ib)
plt.show()

plt.imshow(If)
plt.show()