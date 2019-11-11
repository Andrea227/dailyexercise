import math

a = float(eval(input("What's your a point?: ")))
b = float(eval(input("What's your b point?: ")))
h = float(input("What's your h: "))

n = int((b - a) / h)
f1 = lambda x: (x ** 2) * (math.exp(-(x ** 2)))


def csimpson(num, f, x0, x1):
    y0 = f(x0) + f(x1)
    y1 = 0  # summation of f(x2i-1)
    y2 = 0  # summation of f(x2i)
    intform = []
    for i in range(1, num):
        r = x0 + i * h
        intform += [f(r)]
        if i % 2 == 0:
            y2 = y2 + f(r)
        else:
            y1 = y1 + f(r)
    result = (h / 3) * (y0 + 2 * y2 + 4 * y1)
    return result, intform


def ctrap(num, f, x0, x1):
    y0 = f(x0) + f(x1)
    y1 = 0  # summation of f(xi)
    intform = []
    for i in range(1, num):
        r = x0 + i * h
        intform += [f(r)]
        y1 = y1 + f(r)
    result = (h / 2) * (y0 + 2 * y1)
    return result, intform


def cmid(f, h1, x0):
    num = int((b - a - 2 * h1) / h1)
    y1 = 0
    intform = []
    for j in range(0, int((num/2)+1), 1):
        r = x0 + (2*j + 1) * h1
        intform += [f(r)]
        y1 = y1 + f(r)
    result = (h1 * 2) * y1
    return result, intform


rel1 = ctrap(n, f1, a, b)
p1 = rel1[1]
int1 = rel1[0]
rel2 = csimpson(n, f1, a, b)
p2 = rel2[1]
int2 = rel2[0]
rel3 = cmid(f1, h, a)
p3 = rel3[1]
int3 = rel3[0]
print("The integration using composite Trapezoidal's rule is %.8f the f(xi) are %s" % (int1, p1))
print("The integration using composite Simpson's rule is %.8f the f(xi) process are %s" % (int2, p2))
print("The integration using composite Midpoint's rule is %.8f the f(x2i) process are %s" % (int3, p3))


