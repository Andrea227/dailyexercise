import math

###start###
a = 0
b = 1
h = 0.01
N = int((b - a) / h)
w = [0] * 101
w[0] = 0
w[1] = 1 - math.exp(-0.01)

f = lambda t, y: 1 - y
u1 = lambda t: 1 - math.exp(-t)
u = [0] * 101
u[0] = u1(0)
u[1] = u1(0.01)

t1 = a
print("The following are approximation and real value")
print(0, w[0], u[0])
print(0.1, w[1], u[1])
for i in range(2, N+1):
    w[i] = 4 * w[i - 1] - 3 * w[i - 2] - 2 * h * f(t1, w[i - 2])
    t1 = round(a + i * h, 2)
    u[i] = u1(t1)
    print(t1, w[i], u[i])




