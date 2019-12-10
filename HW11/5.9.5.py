import numpy as np
import math

a = 0
b = 4
m = 2
h = 0.1
N = int((b - a) / h)
f1 = lambda t, x, y: 3*x - 0.002*x*y
f2 = lambda t, x, y: 0.0006*x*y-0.5*y
f = [f1, f2]

####Start#####
t0 = a
alpha = [1000, 500]
w = alpha
print(t0, w)
k = np.zeros((4, m))


###algorithm for approximation##
t1 = a
print("Here's the approximation, real value and error for each m = 1, 2, 3")
for i in range(0, N):
    for j in range(0, m):
        k[0][j] = h * f[j](t1, w[0], w[1])
    for j in range(0, m):
        k[1][j] = h * f[j](t1 + (h / 2), w[0] + (0.5 * k[0][0]), w[1] + (0.5 * k[0][1]))
    for j in range(0, m):
        k[2][j] = h * f[j](t1 + (h / 2), w[0] + (0.5 * k[1][0]), w[1] + (0.5 * k[1][1]))
    for j in range(0, m):
        k[3][j] = h * f[j](t1 + h, w[0] + k[2][0], w[1] + k[2][1])
    for j in range(0, m):
        w[j] = round(w[j] + (1 / 6) * (k[0][j] + 2 * k[1][j] + 2 * k[2][j] + k[3][j]), 8)
    t1 = round(a + (i + 1) * h, 1)
    print(t1, w)
