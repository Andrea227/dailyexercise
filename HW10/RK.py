import math
import numpy as np

f = lambda t, x: (6.22 * (10 ** (-19))) * ((2000 - (x / 2)) ** 2) * ((2000 - (x / 2)) ** 2) * ((3000 - (3 * x / 4)) ** 3)
h = 0.01

answer = np.zeros((21, 2))
answer[0][0] = 0
answer[0][1] = 0


def rk():
    t = 0
    w = 0
    print(t, w)
    for i in range(1, 21):
        k1 = h*f(t, w)
        k2 = h*f(t+(h/2), w + (k1/2))
        k3 = h*f(t+(h/2), w + (k2/2))
        k4 = h * f(t + h, w + k3)
        w = w + (k1 + 2*k2 + 2*k3 + k4)/6
        t = 0 + i*0.01
        print(t, w)
    return print("The answer is the last list")

np.set_printoptions(suppress=True, floatmode='fixed')
rk()
