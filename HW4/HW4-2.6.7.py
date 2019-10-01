f = lambda x: float(600) * (x ** float(4)) - float(550) * (x ** float(3)) + float(200) * (x ** float(2)) - float(
    20) * x - float(1)

x0 = float(0.1)
x1 = float(0)
x2 = float(1)
x3 = float(0.55)
Maxi = float(100)
Tolerance = float(10 ** (-4))
degree = float(4)


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
            return print("Secant p = %s with iteration %d" % (str(b), i))
            break
        else:
            p0 = p1
            q0 = q1
            p1 = p
            q1 = fn(p)
        i += 1
    return print("Method failed after N0 iterations, N0 = ", "%.4f" % maxi)


# Falsi method
def failpo(fn, p0, p1, TOL, N0):
    i = 2
    q0 = fn(p0)
    q1 = fn(p1)
    b = []
    while i <= N0:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        b += [p]
        if abs(p - p1) < TOL:
            return print("Falsi p = %s with iteration %d" % (b, i))
            break
        else:
            q = fn(p)
            if q * q1 < 0:
                p0 = p1
                q0 = q1
            p1 = p
            q1 = q
        i += 1
    return print("Method failed after N0 iterations, N0 = ", "%.4f" % N0)


# Bisection Method
def bisectest(fn, p0, p1, tol, N0):
    i = 1
    FA = fn(p0)
    result = []
    while i <= N0:
        p = p0 + (p1 - p0) / 2
        FP = fn(p)
        result += [p]
        if FP == 0:
            print("Bisection p = %s with iteration %d" % (str(result), i))
            break
        elif ((p1 - p0) / 2) < tol:
            print("Bisection p = %s with iteration %d" % (str(result), i))
            break
        else:
            if FA * FP > 0:
                p0 = p
                FA = FP
            else:
                p1 = p
        i += 1
    else:
        return print("No result after %d th iteration" % N0)


def newtfinal():

    # Newton's Method
    def horner(x):
        y = poly[len(poly) - 1]
        z = poly[len(poly) - 1]
        for j in range(len(poly) - 2, 0, -1):
            y = x * y + poly[j]
            z = x * z + y
        y = x * y + poly[0]
        b = [y, z]
        return b

    def deflate(a, x):
        n = len(a) - 1
        b = [float(0)] * n
        b[n - 1] = a[n]
        for i in range(n - 2, -1, -1):
            b[i] = float(a[i + 1]) + float(x) * float(b[i + 1])
        return b

    def newt(p0, tol, N0):
        s = 1
        b = []
        a = p0
        while s <= N0:
            result = [horner(p0)[0], horner(p0)[1]]
            p = p0 - (result[0] / result[1])
            b += [p]
            if abs(p - p0) < tol:
                print("P are the following result with %d iterations and p0 = %d" % (s, a))
                print(b)
                return p
                break
            else:
                p0 = p
            s += 1
        else:
            return "None"

    poly = [float(-1), float(-20), float(200), float(-550), float(600)]
    finalresult = []
    for k in range(int(degree)):
        u = newt(x1, Tolerance, Maxi)
        if u == "None":
            break
        finalresult += [u]
        poly = deflate(poly, u)
    print("Newton Zeros are %s" % str(finalresult))
    print("For p0 = %.2f , P(p0) = %.6f, P'(p0) = %.6f " % (x0, horner(x0)[0], horner(x0)[1]))


# Muller's Method
def muller(p0, p1, p2, tol, N0):
    h1 = p1 - p0
    h2 = p2 - p1
    g1 = (f(p1) - f(p0)) / h1
    g2 = (f(p2) - f(p1)) / h2
    d = (g2 - g1) / (h2 + h1)
    i = 3
    result = []
    while i <= N0:
        b = g2 + h2 * d
        D = (b ** 2 - 4 * f(p2) * d) ** (1 / 2)
        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D
        h = (-2) * f(p2) / E
        p = p2 + h
        result += [p]
        if abs(h) < tol:
            return print("The Muller result is %s with %d th iteration" % (str(result), i))
            break
        else:
            p0 = p1
            p1 = p2
            p2 = p
            h1 = p1 - p0
            h2 = p2 - p1
            g1 = (f(p1) - f(p0)) / h1
            g2 = (f(p2) - f(p1)) / h2
            d = (g2 - g1) / (h2 + h1)
            i += 1
    else:
        return print("No result after %d th iteration" % N0)


newtfinal()
secant(f, x0, x2, Tolerance, Maxi)
failpo(f, x0, x3, Tolerance, Maxi)
bisectest(f, x0, x2, Tolerance, Maxi)
muller(x1, x0, x2, Tolerance, Maxi)