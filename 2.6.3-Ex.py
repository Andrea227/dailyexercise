f = lambda x: x ** (float(3)) - 2 * (x ** float(2)) - 5
x0 = float(0)
x1 = float(1)
x2 = float(2)
Maxi = float(50)
Tolerance = float(10**(-4))

def muller(p0, p1, p2, tol, N0):
    h1 = p1 - p0
    h2 = p2 - p1
    g1 = (f(p1) - f(p2))/h1
    g2 = (f(p2) - f(p2))/h2
    d = (g2 - g1)/(h2+h1)
    i = 3
    while i <= N0:
        b = g2 + h2*d
        D = (b**2-4*f(p2)*d)**(1/2)
        if abs(b-D)<abs(b+D):
            E = b+D
        else:
            E = b-D
        h = (-2)*f(p2)/E
        p = p2 + h
        if abs(h)<tol:
            return print(p)
            break
        else:
            p0 = p1
            p1 = p2
            p2 = p
            h1 = p1 - p0
            h2 = p2 - p1
            g1 = (f(p1)-f(p0))/h1
            g2 = (f(p2)-f(p1))/h2
            d = (g2 - g1)/(h2 + h1)
            i += 1
    else:
        return print("Boo")


muller(x0, x1, x2, Tolerance, Maxi)