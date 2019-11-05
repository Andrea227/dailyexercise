import math
import numpy as np

# Since it is a continuation of the book example, as they are using
# forward difference formula, we will continue using forward formula

n1 = 3
xp = float(eval(input("What's your approximation point: ")))
hp = float(eval(input("What's your step size: ")))
f1 = lambda x: (2 ** x) * (math.sin(x))
f2 = lambda x: (x ** 3) * (math.cos(x))


def richard3(x, f, h, n):
    Dh = np.zeros((n, n))
    for i in range(0, n):
        h1 = h / (2 ** i)
        Dh[i][0] = round((1 / h1) * (round(f(x + h1), ndigits=4) - round(f(x), ndigits=4)), ndigits=4)
    for j in range(1, n):
        Dh[j][1] = round(Dh[j][0] + round((1 / 3) * (round(Dh[j][0] - Dh[j - 1][0], ndigits=4)), ndigits=4), ndigits=4)
    Dh[2][2] = round(Dh[2][1] + round((1 / 15) * round((Dh[2][1] - Dh[1][1]), ndigits=4), ndigits=4), ndigits=4)
    return print(Dh)


np.set_printoptions(precision=4, suppress=True, floatmode='fixed')
print("As the book example doing, we will use forward difference")
print("The extrapolation table is")
richard3(xp, f2, hp, n1)
