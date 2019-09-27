from scipy.misc import derivative
from math import cos
from math import sin

x = [-100, -50, -25, 25, 50, 100]
TOL = float(10 ** (-5))
N1 = float(100)
f = lambda x: x ** float(2) - float(10) * cos(x)
f1 = lambda x: float(2) * x + float(10) * sin(x)


# Newton's Method 1
def newt1(fn, p3, TOL, N0):
    i = 1
    a = p3
    b = []
    while i <= N0:
        p = p3 - fn(p3) / (derivative(fn, p3, dx=1e-6))
        b += [p]
        if abs(p - p3) < TOL:
            return print("Newton's method with scipy is %s for p0 = %d" % (str(b), a))
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
    b = []
    while i <= N0:
        p = p3 - fn(p3) / fn2(p3)
        b += [p]
        if abs(p - p3) < TOL:
            return print("Newton's method with written f' is %s for p0 = %d" % (str(b), a))
            break
        else:
            p3 = p
        i += 1
    else:
        return print("Newton's Method failed after N0 iterations, N0 = ", "%.4f" % maxi)


for i in x:
    newt1(f, float(i), TOL, N1)
    newt2(f, f1, float(i), TOL, N1)
