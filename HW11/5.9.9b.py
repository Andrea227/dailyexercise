import numpy as np
import math

# Input
a = 0
b = 2
m = 2
h = 0.1
N = int((b - a) / h)
alpha = [0, -1]
f1 = lambda t, x, y: -4 * x - 2 * y + math.cos(t) + 4 * math.sin(t)
f2 = lambda t, x, y: 3 * x + y - 3 * math.sin(t)
f = [f1, f2]
t = [0] * (N + 1)
t[0] = a

# Algorithm part 1
print("This is the prediction")
k = np.zeros((4, m))
w = np.zeros((N + 1, m + 2))
for j in range(0, m):
    w[0][j] = alpha[j]
for i in range(1, 4):
    for j in range(0, m):
        k[0][j] = h * f[j](t[i - 1], w[i - 1][0], w[i - 1][1])
    for j in range(0, m):
        k[1][j] = h * f[j](t[i - 1] + (h / 2), w[i - 1][0] + (0.5 * k[0][0]), w[i - 1][1] + (0.5 * k[0][1]))
    for j in range(0, m):
        k[2][j] = h * f[j](t[i - 1] + (h / 2), w[i - 1][0] + (0.5 * k[1][0]), w[i - 1][1] + (0.5 * k[1][1]))
    for j in range(0, m):
        k[3][j] = h * f[j](t[i - 1] + h, w[i - 1][0] + k[2][0], w[i - 1][1] + k[2][1])
    for j in range(0, m):
        w[i][j] = w[i - 1][j] + (1 / 6) * (k[0][j] + 2 * k[1][j] + 2 * k[2][j] + k[3][j])
    t[i] = round(a + i * h, 2)
    print(t[i], w[i][0], w[i][1])

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
                55 * f[j](t[i - 1], w[i - 1][0], w[i - 1][1]) - 59 * f[j](t[i - 2], w[i - 2][0], w[i - 2][1])
                + 37 * f[j](t[i - 3], w[i - 3][0], w[i - 3][1]) - 9 * f[j](t[i - 4], w[i - 4][0], w[i - 4][1]))
    for j in range(0, m):
        w[i][j] = w[i - 1][j] + (h / 24) * (
                9 * f[j](t[i], w2[i][0], w2[i][1]) + 19 * f[j](t[i - 1], w[i - 1][0], w[i - 1][1])
                - 5 * f[j](t[i - 2], w[i - 2][0], w[i - 2][1]) + f[j](t[i - 3], w[i - 3][0], w[i - 3][1]))
    print(t[i], w[i][0], w[i][1])

# real value and error
u1 = lambda t: 2 * math.exp(-t) - 2 * math.exp(-2 * t) + math.sin(t)
u2 = lambda t: (-3) * math.exp(-t) + 2 * math.exp(-2 * t)
u = [u1, u2]
real = np.zeros((N + 1, m))
print("This is real value")
for j in range(0, m):
    real[0][j] = alpha[j]
for i in range(1, N + 1):
    real[i][0] = u1(t[i])
    real[i][1] = u2(t[i])
for k in range(0, N + 1):
    print(t[k], real[k][0], real[k][1])
