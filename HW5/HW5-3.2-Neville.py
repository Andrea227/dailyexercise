import numpy as np
import mathpy
import math

xp = 1+math.sqrt(10)
degree = int(input("How many data points do you have: "))

xlist = np.zeros(degree)
ylist = np.zeros(degree)
h = 10/(degree-1)
f = lambda x: (1+x**2)**(-1)
xlist[0] = -5
b = 1
while b < int(degree):
    xlist[b] = -5 + b*h
    b += 1
a = 0
while a < int(degree):
    ylist[a] = f(xlist[a])
    a += 1


def neville(x, y, x0):
    n = x.size
    q = np.zeros((n, n - 1))
    # Insert 'y' in the first column of the matrix 'q'
    q = np.concatenate((y[:, None], q), axis=1)

    for i in range(1, n):
        for j in range(1, i + 1):
            q[i, j] = ((x0 - x[i - j]) * q[i, j - 1] - (x0 - x[i]) * q[i - 1, j - 1]) / (x[i] - x[i - j])
    yp = q[n - 1, n - 1]
    return [yp, q]


print(neville(xlist, ylist, xp))
print(mathpy.numerical.neville(xlist, ylist, xp))

