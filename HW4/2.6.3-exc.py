f = lambda x: x ** (float(3)) - 2 * (x ** float(2)) - 5
x0 = float(0)
x1 = float(1)
x2 = float(2)
Maxi = float(100)
Tolerance = float(10 ** (-4))
poly = [-5, 0, -2, 1]


def muller(p0, p1, p2, tol, N0):
    h1 = p1 - p0
    h2 = p2 - p1
    g1 = (f(p1) - f(p2)) / h1
    g2 = (f(p2) - f(p2)) / h2
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
            return p
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
        return "None"


def deflate(a, x):
    n = len(a) - 1
    b = [float(0)] * n
    b[n - 1] = a[n]
    for i in range(n - 2, -1, -1):
        b[i] = float(a[i + 1]) + float(x) * float(b[i + 1])
    return b


finalresult = []
for k in range(int(3)):
    u = muller(x0, x1, x2, Tolerance, Maxi)
    if u == "None":
        break
    finalresult += [u]
    poly = deflate(poly, u)

print("Zeros are %s" % str(finalresult))
