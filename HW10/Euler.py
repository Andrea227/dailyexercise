import numpy as np
import math

f = lambda t, y: (2 * y / t) + (t ** 2) * math.exp(t)
h = 0.1


def rk():
    t = 1
    w = 0
    print(t, w)
    for i in range(1, 11):
        w = w + h * f(t, w)
        t = 1 + i * 0.1
        print(t, w)
    return print("The answer is the last list")


np.set_printoptions(suppress=True, floatmode='fixed')
rk()
