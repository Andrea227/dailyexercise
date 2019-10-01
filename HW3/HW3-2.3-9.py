import sys
import math


# definition of the input
p0 = float(eval(input("Enter p0: ")))
p1 = float(eval(input("Enter p1: ")))
TOL = float(10**(-4))
maxi = float(100)


# f = lambda x: (x ** 3) - 2 * (x ** 2) - 5
# f = lambda x: (x ** 3) + 3 * (x ** 2) - 1
# f = lambda x: x - math.cos(x)
# f = lambda x: x - 0.8 - 0.2 * math.sin(x)
f = lambda x: float(600) * (x ** float(4)) - float(550) * (x ** float(3)) + float(200) * (x ** float(2)) - float(
    20) * x - float(1)


def failpo(fn, p0, p1, TOL, N0):
    i = 2
    q0 = fn(p0)
    q1 = fn(p1)
    b = []
    while i <= N0:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        b += [p]
        if abs(p - p1) < TOL:
            return print("p = %s with iteration %d" % (b, i))
            sys.exit()
        else:
            q = fn(p)
            if q * q1 < 0:
                p0 = p1
                q0 = q1
            p1 = p
            q1 = q
        i += 1
    return print("Method failed after N0 iterations, N0 = ", "%.4f" % maxi)
    sys.exit()


failpo(f, p0, p1, TOL, maxi)
