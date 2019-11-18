import numpy as np
import math

x0 = float(eval(input("What's your a point?: ")))
x1 = float(eval(input("What's your b point?: ")))
num = int(input("How many integers do you have: ?"))
f1 = lambda x: (x ** 2) * math.log(x)


def rom(a, b, n, f):
    h = b - a
    R = np.zeros((n, n))
    R[0][0] = (h / 2) * (f(a) + f(b))
    print(R[0][0])
    for i in range(1, n):
        g = 0
        z = int((2 ** (i + 1 - 2)) + 1)
        for k in range(1, z):
            g = g + f(a + (k - 0.5) * h)
        R[1][0] = (1 / 2) * R[0][0] + (1 / 2) * h * g
        mid = [R[1][0]]
        j = 1
        while 1 <= j <= i:
            R[1][j] = R[1][j - 1] + (R[1][j - 1] - R[0][j - 1]) / ((4 ** (j + 1 - 1)) - 1)
            mid += [R[1][j]]
            j += 1
        print(mid)
        h = h / 2
        p = 0
        while 0 <= p <= i:
            R[0][p] = R[1][p]
            p += 1
    return print(R)


rom(x0, x1, num, f1)
