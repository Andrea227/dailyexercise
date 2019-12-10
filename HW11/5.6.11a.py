import numpy as np
import math

# input
a = 1
b = 2
N = 10
alpha = 1
f = lambda t, y: (y / t) - ((y / t) ** 2)

# start
print("The following are approximations")
h = (b - a) / N
t = [0] * (N + 1)
t[0] = a
w = [0] * (N + 1)
w[0] = alpha
print(t[0], w[0])

# Part 1
for i in range(1, 4):
    k1 = h * f(t[i - 1], w[i - 1])
    k2 = h * f(t[i - 1] + (h / 2), w[i - 1] + (k1 / 2))
    k3 = h * f(t[i - 1] + (h / 2), w[i - 1] + (k2 / 2))
    k4 = h * f(t[i - 1] + h, w[i - 1] + k3)
    w[i] = w[i - 1] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    t[i] = a + i * h
    print(t[i], w[i])

# Part 2
for i in range(3, N):
    t[i] = round(a + i * h, 2)
    t[i + 1] = round(a + (i + 1) * h, 2)
    w0 = w[i - 3] + ((4 * h) / 3) * (2 * f(t[i], w[i]) - f(t[i - 1], w[i - 1]) + 2 * f(t[i - 2], w[i - 2]))
    w[i + 1] = w[i - 1] + (h / 3) * (f(t[i + 1], w0) + 4 * f(t[i], w[i]) + f(t[i - 1], w[i - 1]))
    print(t[i + 1], w[i + 1])

# real value and error
u1 = lambda t: t / (1 + math.log(t))
real = [0] * (N + 1)
print("This is real value")
real[0] = alpha
print(a, real[0])
for i in range(1, N + 1):
    t2 = a + i * h
    real[i] = u1(t2)
    print(t2, real[i])
