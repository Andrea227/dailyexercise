import numpy as np
import math

n = int(input("how many data points do you have: "))
xp = float(eval(input("Your evaluation point is: ")))
x1 = []
y1 = []
for i in range(n):
    x1 += [float(input("Your next x is: "))]
for j in range(n):
    y1 += [float(input("Your corresponding y is: "))]

h = (x1[-1] - x1[0]) / (n - 1)
Dy = np.zeros((n, n))
Dy[:, 0] = y1
for k in range(1, n):
    for l in range(n - k):
        Dy[l][k] = Dy[l + 1][k - 1] - Dy[l][k - 1]

print(Dy)

mid = math.ceil(n / 2)


def combup(n, r):
    if r % 2 != 0:
        z = r // 2
        demo = n
        i = 1
        while i <= z:
            demo *= ((n ** 2) - (i ** 2))
            i += 1
    else:
        z = r // 2
        demo = n ** 2
        i = 1
        while i < z:
            demo *= ((n ** 2) - (i ** 2))
            i += 1
    return demo


def factor(x):
    a = 1
    if x != 1:
        i = 2
        while i <= x:
            a *= i
            i += 1
        else:
            return a
    else:
        return a


def central(u):
    realpo = mid-1
    s = (u - x1[realpo]) / h
    sum = Dy[realpo][0]
    for i in range(1, n):
        if i % 2 != 0:
            z = i // 2
            sum = sum + combup(s, i) * 0.5 * (Dy[realpo - z][i] + Dy[realpo - z - 1][i]) / factor(i)
            print(sum)
        else:
            z = i // 2
            sum = sum + combup(s, i) * Dy[realpo - z][i] / factor(i)
            print(sum)
    return print("The final evaluation is %.8f" % sum)


central(xp)
