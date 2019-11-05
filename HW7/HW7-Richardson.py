import math
import numpy as np

# Since it is a continuation of the book example, as they are using
# forward difference formula, we will continue using forward formula

n1 = 3
xp = float(eval(input("What's your approximation point: ")))
hp = float(eval(input("What's your step size: ")))
f1 = lambda x: (2 ** x) * (math.sin(x))


def richard3(x, f, h, n):
    Dh = np.zeros((n, n))
    for i in range(0, n):
        h1 = h / (2 ** i)
        Dh[i][0] = (1 / h1) * (f(x + h1) - f(x))
    for j in range(1, n):
        Dh[j][1] = Dh[j][0] + (1 / 3) * (Dh[j][0] - Dh[j - 1][0])
    Dh[2][2] = Dh[2][1] + (1 / 15) * (Dh[2][1] - Dh[1][1])
    return print(Dh)


print("As the book example doing, we will use forward difference")
print("The extrapolation table is")
richard3(xp, f1, hp, n1)
