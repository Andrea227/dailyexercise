from scipy.misc import derivative
import math

# definition of the input
p0 = float(0)
p1 = float(0.48)
maxi = float(10)
TOL = float(0.001)

f = lambda x: math.tan(math.pi * x) - 6


# secant method
def secanttest(fn, p0, p1, N0):
    i = 2
    q0 = fn(p0)
    q1 = fn(p1)
    result = [p0, p1]
    while i <= N0:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        result += [p]
        p0 = p1
        q0 = q1
        p1 = p
        q1 = fn(p)
        i += 1
    return result


# False Point Method
def failpotest(fn, p0, p1, N0):
    i = 2
    q0 = fn(p0)
    q1 = fn(p1)
    result = [p0, p1]
    while i <= N0:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        result += [p]
        q = fn(p)
        if q * q1 < 0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q
        i += 1
    return result


# Bisection Method
def bisectest(fn, p0, p1, N0):
    i = 1
    FA = fn(p0)
    result = [p0, p1]
    while i <= N0:
        p = p0 + (p1 - p0) / 2
        FP = fn(p)
        result += [p]
        if FP == 0:
            break
        else:
            if FA * FP > 0:
                p0 = p
                FA = FP
            else:
                p1 = p
        i += 1
    return result


a1 = bisectest(f, p0, p1, maxi)
a2 = failpotest(f, p0, p1, maxi)
a3 = secanttest(f, p0, p1, maxi)

print("The answer for bisec is %s" % str(a1))
print("The answer for falsi is %s" % str(a2))
print("The answer for secant is %s" % str(a3))
