import math
import sys

# definition of the input
p0 = float(eval(input("Enter p0: ")))
p1 = float(eval(input("Enter p1: ")))
TOL = float(eval(input("Enter TOL: ")))
maxi = float(input("Enter Iteration: "))

# f = lambda x: math.exp(x) + 2 ** (-x) + 2 * math.cos(x) - 6
# f = lambda x: math.log(x-1) + math.cos(x-1)
# f = lambda x: 2 * x * math.cos(2 * x) - ((x - 2) ** 2)
# f = lambda x: ((x - 2) ** 2) - math.log(x)
# f = lambda x: math.exp(x) - 3 * (x**2)
f = lambda x: math.sin(x) - math.exp(-x)


# secant algorithm
def secant(fn, p0, p1, TOL, maxi):
    i = 2
    q0 = fn(p0)
    q1 = fn(p1)
    while i <= maxi:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        if abs(p - p1) < TOL:
            return print("p =", "%.7f" % p)
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
