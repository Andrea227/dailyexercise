import numpy as np
import math

a = 0
b = 1
m = 3
h = 0.1
N = int((b - a) / h)
f1 = lambda t, x, y, z: y - z + t
f2 = lambda t, x, y, z: 3 * (t ** 2)
f3 = lambda t, x, y, z: y + math.exp(-t)
f = [f1, f2, f3]

####Start#####
t0 = a
alpha = [1, 1, -1]
w = [0] * m
for k in range(0, ):
    w[k] = alpha[k]
print(t0, w)
k = np.zeros((4, m))


###algorithm##
def rks():
    t1 = a
    for i in range(0, N):
        for j in range(0, m):
            k[0][j] = h * f[j](t1, w[0], w[1], w[2])
        for j in range(0, m):
            k[1][j] = h * f[j](t1 + (h / 2), w[0] + (0.5 * k[0][0]), w[1] + (0.5 * k[0][1]), w[2] + (0.5 * k[0][2]))
        for j in range(0, m):
            k[2][j] = h * f[j](t1 + (h / 2), w[0] + (0.5 * k[1][0]), w[1] + (0.5 * k[1][1]), w[2] + (0.5 * k[1][2]))
        for j in range(0, m):
            k[3][j] = h * f[j](t1 + (h / 2), w[0] + (0.5 * k[2][0]), w[1] + (0.5 * k[2][1]), w[2] + (0.5 * k[2][2]))
        for j in range(0, m):
            w[j] = w[j] + (1 / 6) * (k[0][j] + 2 * k[1][j] + 2 * k[2][j] + k[3][j])
        t1 = a + (i+1) * h
        print(t1, w)
    return print("finish")


rks()
