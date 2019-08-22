import numpy as np

def expM(f, n):
    if n == 1:
        return f
    elif n % 2 == 0:
        return expM(np.dot(f, f), n//2)
    else: 
        return np.dot(f, expM(np.dot(f, f), (n - 1) // 2))

def fibo(n = 10):
    if n <= 1:
        return n
    else:
        f = np.array([[1, 1],[1, 0]], dtype = np.int64)
        fexp = expM(f, n-1)
        return fexp[0, 0]