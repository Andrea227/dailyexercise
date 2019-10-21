# This file is updated from the original algorithm I wrote for the question 3.4.1. The only difference is that for
# every element in q, it gets round to 5 digits. And the precision of the final output is 5.

import numpy as np

num = int(input("how many data points do you have: "))
xp = float(input("What's your approximation: "))
n = num - 1
x1 = []
y0 = []
y1 = []
for i in range(num):
    x1 += [float(input("Your next x is: "))]
for j in range(num):
    y0 += [float(input("Your corresponding y is: "))]
for k in range(num):
    y1 += [float(input("Your corresponding y1 is: "))]

z = [0] * (2 * num)
q = np.zeros((2 * num, 2 * num))
i = 0
while n >= i >= 0:
    z[2 * i] = round(x1[i], ndigits=5)
    z[2 * i + 1] = round(x1[i], ndigits=5)
    q[2 * i + 1][0] = round(y0[i], ndigits=5)
    q[2 * i][0] = round(y0[i], ndigits=5)
    q[2 * i + 1][1] = round(y1[i], ndigits=5)
    if i != 0:
        q[2 * i][1] = round((q[2 * i][0] - q[2 * i - 1][0]) / (z[2 * i] - z[2 * i - 1]), ndigits=5)
    i += 1

k = 2
while 2 * n + 1 >= k >= 2:
    j = 2
    while k >= j >= 2:
        q[k][j] = round((q[k][j - 1] - q[k - 1][j - 1]) / (z[k] - z[k - j]), ndigits=5)
        j += 1
    k += 1


def hermite(x):
    result = q[0][0]
    for p in range(1, 2 * num):
        b = 1
        for r in range(0, p):
            b *= (x - z[r])
        result = result + q[p][p] * b
    return result


a = hermite(xp)

np.set_printoptions(precision=5, suppress=True, floatmode='fixed')
print("The difference table is")
print(q)
print("The evaluation at %.5f is %.5f" % (xp, a))