import numpy as np
import math

a = 1
b = 2
m = 3
h = 0.1
N = int((b - a) / h)
f1 = lambda t, x, y, z: y
f2 = lambda t, x, y, z: z
f3 = lambda t, x, y, z: 5 * math.log(t) + 9 + (1 / t) * z - (3 / (t ** 2)) * y + (4 / (t ** 3)) * x
f = [f1, f2, f3]

####Start#####
t0 = a
alpha = [0, 1, 3]
w = alpha
print(t0, w)
k = np.zeros((4, m))
u1 = lambda t: -(t ** 2) + t * math.cos(math.log(t)) + t * math.sin(math.log(t)) + (t ** 3) * math.log(t)

###algorithm for approximation##
t1 = a
print("Here's the approximation")
for i in range(0, N):
    for j in range(0, m):
        k[0][j] = h * f[j](t1, w[0], w[1], w[2])
    for j in range(0, m):
        k[1][j] = h * f[j](t1 + (h / 2), w[0] + (0.5 * k[0][0]), w[1] + (0.5 * k[0][1]), w[2] + (0.5 * k[0][2]))
    for j in range(0, m):
        k[2][j] = h * f[j](t1 + (h / 2), w[0] + (0.5 * k[1][0]), w[1] + (0.5 * k[1][1]), w[2] + (0.5 * k[1][2]))
    for j in range(0, m):
        k[3][j] = h * f[j](t1 + h, w[0] + k[2][0], w[1] + k[2][1], w[2] + k[2][2])
    for j in range(0, m):
        w[j] = round(w[j] + (1 / 6) * (k[0][j] + 2 * k[1][j] + 2 * k[2][j] + k[3][j]), 8)
    t1 = round(a + (i + 1) * h, 1)
    print(t1, w)
