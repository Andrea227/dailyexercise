from scipy.misc import derivative

# definition of the input
p0 = float(eval(input("Enter p0: ")))
p1 = float(eval(input("Enter p1: ")))
TOL = float(10**(-6))
maxi = float(100)
p2 = float((p0 + p1) / 2)

f = lambda x: 230 * (x ** 4) + 18 * (x ** 3) + 9 * (x ** 2) - 221 * x - 9
f1 = lambda x: 230 * 4 * (x ** 3) + 18 * 3 * (x ** 2) + 9 * 2 * x - 221


# secant method
def secant(fn, p0, p1, TOL, N0):
    i = 2
    q0 = fn(p0)
    q1 = fn(p1)
    b = []
    while i <= N0:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        b += [p]
        if abs(p - p1) < TOL:
            return print("Secant method gave us %s as iteration %d" % (b, i))
            break
        else:
            p0 = p1
            q0 = q1
            p1 = p
            q1 = fn(p)
        i += 1
    else:
        return print("Secant Method failed after N0 iterations, N0 = ", "%.4f" % maxi)


# False Point Method
def failpo(fn, p0, p1, TOL, N0):
    i = 2
    q0 = fn(p0)
    q1 = fn(p1)
    b = []
    while i <= N0:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        b += [p]
        if abs(p - p1) < TOL:
            return print("Falsi method gave us %s as iteration %d" % (b, i))
            break
        else:
            q = fn(p)
            if q * q1 < 0:
                p0 = p1
                q0 = q1
            p1 = p
            q1 = q
        i += 1
    else:
        return print("FP Method failed after N0 iterations, N0 = ", "%.4f" % maxi)


# Newton's Method 1
def newt1(fn, p3, TOL, N0):
    i = 1
    b = []
    while i <= N0:
        p = p3 - fn(p3) / (derivative(fn, p3))
        b += [p]
        if abs(p - p3) < TOL:
            return print("Newt method with scipy gave us %s as iteration %d" % (b, i))
            break
        else:
            p3 = p
        i += 1
    else:
        return print("Newton's Method failed after N0 iterations, N0 = ", "%.4f" % maxi)


# Newton's Method 2
def newt2(fn, fn2, p3, TOL, N0):
    i = 1
    b = []
    while i <= N0:
        p = p3 - (fn(p3) / fn2(p3))
        b += [p]
        if abs(p - p3) < TOL:
            return print("Newt method with writen f' gave us %s as iteration %d" % (b, i))
            break
        else:
            p3 = p
        i += 1
    else:
        return print("Newton's Method failed after N0 iterations, N0 = ", "%.4f" % maxi)


failpo(f, p0, p1, TOL, maxi)
secant(f, p0, p1, TOL, maxi)
newt1(f, p2, TOL, maxi)
newt2(f, f1, p2, TOL, maxi)
