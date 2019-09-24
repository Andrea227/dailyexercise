from scipy.misc import derivative
import math

x = -0.5
TOL = 10 ** (-5)
N1 = 100
f = lambda x: math.exp(6 * x) + 3 * ((math.log(2)) ** 2) * (math.exp(2 * x)) - (math.log(8)) * (math.exp(4 * x)) - (
        math.log(2) ** 3)
f1 = lambda x: 6 * math.exp(6 * x) + 6 * ((math.log(2)) ** 2) * (math.exp(2 * x)) - 4 * (math.log(8)) * (
    math.exp(4 * x))
f2 = lambda x: 36 * math.exp(6 * x) + 12 * ((math.log(2)) ** 2) * (math.exp(2 * x)) - 16 * (math.log(8)) * (
    math.exp(4 * x))


# Newton's Method 1
def newt1(fn, fn1, p3, TOL, N0):
    i = 1
    a = p3
    while i <= N0:
        p = p3 - (fn(p3) * fn1(p3)) / (fn1(p3) ** 2 - fn(p3) * derivative(fn1, p3, dx=1e-6))
        if abs(p - p3) < TOL:
            return print("p1 = %.8f for p0 = %d and iteration = %d" % (p, a, i))
            break
        else:
            p3 = p
        i += 1
    else:
        return print("Newton's Method failed after N0 iterations, N0 = ", "%.4f" % N0)


# Newton's Method 2
def newt2(fn, fn2, fn3, p3, TOL, N0):
    i = 1
    a = p3
    while i <= N0:
        p = p3 - ((fn(p3) * fn2(p3)) / ((fn2(p3)) ** 2 - (fn(p3) * fn3(p3))))
        if abs(p - p3) < TOL:
            return print("p2 = %.8f for p0 = %d and iteration = %d" % (p, a, i))
            break
        else:
            p3 = p
        i += 1
    else:
        return print("Newton's Method failed after N0 iterations, N0 = ", "%.4f" % N0)


newt1(f, f1, x, TOL, N1)
newt2(f, f1, f2, x, TOL, N1)
