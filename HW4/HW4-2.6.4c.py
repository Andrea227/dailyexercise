f = lambda x: (x ** (float(4))) + (x ** float(3)) + float(3) * x ** float(2) + float(2) * x + 2
x0 = float(eval(input("Your approximation zero is: ")))
x1 = float(eval(input("Your second approximation zero is: ")))
x2 = float(eval(input("Your third approximation zero is: ")))
Maxi = float(input("The maximum iteration is: "))
Tolerance = float(eval(input("The tolerance is: ")))


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
            return print("The result is %s with %d th iteration" % (str(result), i))
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


muller(x0, x1, x2, Tolerance, Maxi)