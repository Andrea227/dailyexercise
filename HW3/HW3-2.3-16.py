from scipy.misc import derivative
from math import cos
from math import sin

x = [-100, -50, -25, 25, 50, 100]
TOL = 10 ** (-5)
N1 = 100
f = lambda x: x ** 2 - 10 * cos(x)
f1 = lambda x: 2 * x + 10 * sin(x)


# Newton's Method 1
def newt1(fn, p3, TOL, N0):
    i = 1
    a = p3
    while i <= N0:
        p = p3 - fn(p3) / (derivative(fn, p3))
        if abs(p - p3) < TOL:
            return print("p1 = %.6f for p0 = %d" % (p, a))
            break
        else:
            p3 = p
        i += 1
    else:
        return print("Newton's Method failed after N0 iterations, N0 = ", "%.4f" % maxi)


# Newton's Method 2
def newt2(fn, fn2, p3, TOL, N0):
    i = 1
    a = p3
    while i <= N0:
        p = p3 - fn(p3) / fn2(p3)
        if abs(p - p3) < TOL:
            return print("p2 = %.6f for p0 = %d" % (p, a))
            break
        else:
            p3 = p
        i += 1
    else:
        return print("Newton's Method failed after N0 iterations, N0 = ", "%.4f" % maxi)


for i in x:
    newt1(f, i, TOL, N1)
    newt2(f, f1, i, TOL, N1)
