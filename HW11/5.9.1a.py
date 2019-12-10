import numpy as np
import math

a = 0
b = 1
m = 2
h = 0.2
N = int((b - a) / h)
f1 = lambda t, x, y: 3 * x + 2 * y - (2 * (t ** 2) + 1) * math.exp(2 * t)
f2 = lambda t, x, y: 4 * x + y + ((t ** 2) + 2 * t - 4) * math.exp(2 * t)
f = [f1, f2]

####Start#####
t0 = a
alpha = [1, 1]
w = alpha
print(t0, w)
k = np.zeros((4, m))
u1 = lambda t: (1 / 3) * math.exp(5 * t) - (1 / 3) * math.exp(-t) + math.exp(2 * t)
u2 = lambda t: (1 / 3) * math.exp(5 * t) + (2 / 3) * math.exp(-t) + (t ** 2) * math.exp(2 * t)
u = [u1, u2]

###algorithm for approximation##
t1 = a
real = [1, 1]
error = [0, 0]
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
    for j in range(0, m):
        real[j] = round(u[j](t1), 8)
        error[j] = round(abs(w[j] - real[j]), 8)
    print(t1, w, real, error)
