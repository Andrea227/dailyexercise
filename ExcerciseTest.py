from scipy.misc import derivative


x = float(1)
TOL = float(10 ** (-4))
N1 = float(50)
f = lambda x: x ** float(3) - float(2) * (x ** float(2)) - float(5)
f1 = lambda x: float(3) * (x ** float(2)) - float(4) * x


# Newton's Method 1
def newt1(fn, p3, TOL, N0):
    i = 1
    b = [p3]
    while i <= N0:
        p = p3 - fn(p3) / (derivative(fn, p3, dx=1e-6))
        b += [p]
        p3 = p
        i += 1
    else:
        return print(b)


# Newton's Method 2
def newt2(fn, fn2, p3, TOL, N0):
    i = 1
    b = [p3]
    while i <= N0:
        p = p3 - fn(p3) / fn2(p3)
        b += [p]
        p3 = p
        i += 1
    else:
        return print(b)

newt1(f, x, TOL, N1)
newt2(f, f1, x, TOL, N1)





