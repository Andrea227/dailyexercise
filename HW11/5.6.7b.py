# input
a = 2
b = 3
N = 5
alpha = 1
f = lambda t, y: 1 + (t - y) ** 2

# start
print("The following are approximations")
h = (b - a) / N
t = [0] * (N + 1)
t[0] = a
w = [0] * 4
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
for i in range(4, N + 1):
    t1 = a + i * h
    w0 = w[3] + (h / 24) * (55 * f(t[3], w[3]) - 59 * f(t[2], w[2]) + 37 * f(t[1], w[1]) - 9 * f(t[0], w[0]))
    w1 = w[3] + (h / 24) * (9 * f(t1, w0) + 19 * f(t[3], w[3]) - 5 * f(t[2], w[2]) + f(t[1], w[1]))
    print(t1, w1)
    for j in range(0, 3):
        t[j] = t[j + 1]
        w[j] = w[j + 1]
    t[3] = t1
    w[3] = w1

# real value and error
u1 = lambda t: t + 1 / (1 - t)
real = [0] * (N + 1)
print("This is real value")
real[0] = alpha
print(a, real[0])
for i in range(1, N + 1):
    t2 = a + i * h
    real[i] = u1(t2)
    print(t2, real[i])
