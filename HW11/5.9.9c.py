import numpy as np
import math

# Input
a = 0
b = 2
m = 3
h = 0.5
N = int((b - a) / h)
alpha = [1, 0, 1]
f1 = lambda t, x, y, z: y
f2 = lambda t, x, y, z: -x - 2 * math.exp(t) + 1
f3 = lambda t, x, y, z: -x - math.exp(t) + 1
f = [f1, f2, f3]
t = [0] * (N + 1)
t[0] = a

# Algorithm part 1
print("This is the prediction")
k = np.zeros((4, m))
w = np.zeros((N + 1, m))
for j in range(0, m):
    w[0][j] = alpha[j]
for i in range(1, 4):
    for j in range(0, m):
        k[0][j] = h * f[j](t[i - 1], w[i - 1][0], w[i - 1][1], w[i - 1][2])
    for j in range(0, m):
        k[1][j] = h * f[j](t[i - 1] + (h / 2), w[i - 1][0] + (0.5 * k[0][0]), w[i - 1][1] + (0.5 * k[0][1]),
                           w[i - 1][2] + (0.5 * k[0][2]))
    for j in range(0, m):
        k[2][j] = h * f[j](t[i - 1] + (h / 2), w[i - 1][0] + (0.5 * k[1][0]), w[i - 1][1] + (0.5 * k[1][1]),
                           w[i - 1][2] + (0.5 * k[1][2]))
    for j in range(0, m):
        k[3][j] = h * f[j](t[i - 1] + h, w[i - 1][0] + k[2][0], w[i - 1][1] + k[2][1], w[i - 1][2] + k[2][2])
    for j in range(0, m):
        w[i][j] = w[i - 1][j] + (1 / 6) * (k[0][j] + 2 * k[1][j] + 2 * k[2][j] + k[3][j])
    t[i] = round(a + i * h, 2)
    print(t[i], w[i][0], w[i][1], w[i][2])

# Prep for prediction
w2 = np.zeros((N + 1, m))
for p in range(0, N + 1):
    for q in range(0, m):
        w2[p][q] = w[p][q]

# algorithm part 2
for i in range(4, N + 1):
    t[i] = a + i * h
    for j in range(0, m):
        w2[i][j] = w[i - 1][j] + (h / 24) * (
                55 * f[j](t[i - 1], w[i - 1][0], w[i - 1][1], w[i - 1][2]) - 59 * f[j](t[i - 2], w[i - 2][0],
                                                                                       w[i - 2][1], w[i - 2][2])
                + 37 * f[j](t[i - 3], w[i - 3][0], w[i - 3][1], w[i - 3][2]) - 9 * f[j](t[i - 4], w[i - 4][0],
                                                                                        w[i - 4][1], w[i - 4][2]))
    for j in range(0, m):
        w[i][j] = w[i - 1][j] + (h / 24) * (
                9 * f[j](t[i], w2[i][0], w2[i][1], w2[i][2]) + 19 * f[j](t[i - 1], w[i - 1][0], w[i - 1][1],
                                                                         w[i - 1][2])
                - 5 * f[j](t[i - 2], w[i - 2][0], w[i - 2][1], w[i - 2][2]) + f[j](t[i - 3], w[i - 3][0], w[i - 3][1],
                                                                                   w[i - 3][2]))
    print(t[i], w[i][0], w[i][1], w[i][2])

# real value and error
u1 = lambda t: math.cos(t) + math.sin(t) - math.exp(t) + 1
u2 = lambda t: -math.sin(t) + math.cos(t) - math.exp(t)
u3 = lambda t: -math.sin(t) + math.cos(t)
u = [u1, u2, u3]
real = np.zeros((N + 1, m))
print("This is real value")
for j in range(0, m):
    real[0][j] = alpha[j]
for i in range(1, N + 1):
    real[i][0] = u1(t[i])
    real[i][1] = u2(t[i])
    real[i][2] = u3(t[i])
for k in range(0, N + 1):
    print(t[k], real[k][0], real[k][1], real[k][2])
