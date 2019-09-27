import math
import sys

# definition of the input
p0 = float(eval(input("Enter p0: ")))
p1 = float(eval(input("Enter p1: ")))
TOL = float(eval(input("Enter TOL: ")))
maxi = float(input("Enter Iteration: "))

# f = lambda x: (x ** 3) - 2 * (x ** 2) - 5
# f = lambda x: (x ** 3) + 3 * (x ** 2) - 1
# f = lambda x: x - math.cos(x)
f = lambda x: x - 0.8 - 0.2 * math.sin(x)


# secant algorithm
def secant(fn, p0, p1, TOL, maxi):
    i = 2
    q0 = fn(p0)
    q1 = fn(p1)
    b = []
    while i <= maxi:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        b += [p]
        if abs(p - p1) < TOL:
            return print("p = %s with iteration %d" % (str(b), i))
            sys.exit()
        else:
            p0 = p1
            q0 = q1
            p1 = p
            q1 = fn(p)
        i += 1
    return print("Method failed after N0 iterations, N0 = ", "%.4f" % maxi)
    sys.exit()


secant(f, p0, p1, TOL, maxi)
