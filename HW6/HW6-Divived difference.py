import numpy as np

n = int(input("how many data points do you have: "))
xp = float(eval(input("Your evaluation point is: ")))
x1 = []
y1 = []
for i in range(n):
    x1 += [float(input("Your next x is: "))]
for j in range(n):
    y1 += [float(input("Your corresponding y is: "))]

Dy = np.zeros((n, n))
Dy[:, 0] = y1
for k in range(1, n):
    for l in range(1, k + 1):
        Dy[k][l] = (Dy[k][l - 1] - Dy[k - 1][l - 1]) / (x1[k] - x1[k - l])

np.set_printoptions(precision=8, suppress=True, floatmode='fixed')
print(Dy)


def diff(u):
    sum = Dy[0][0]
    for i in range(1, n):
        a = 1
        j = 0
        while i-1>=j>=0:
            a *= (u - x1[j])
            j += 1
        sum = sum + Dy[i][i] * a
    return sum


print(diff(xp))
