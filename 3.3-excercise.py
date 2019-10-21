import numpy as np

q = np.zeros((4, 4))

i = 0
for i in range(0, 4):
    for j in range(0, 4):
        q[i][j] = 4 * i - j

print(q)

z = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def hermite(x):
    result = q[0][0]
    for p in range(1, 2 * 2):
        a = 1
        for r in range(0, p):
            a *= (x-z[r])
        result = result + q[p][p] * a
    return result


b = hermite(7)

print(b)
