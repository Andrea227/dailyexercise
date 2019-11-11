x0 = float(eval(input("What's your a point?: ")))
x2 = float(eval(input("What's your b point?: ")))
h1 = float((x0 + x2) / 2)
x1 = x0 + h1

f1 = lambda x: 2 / (x - 4)


def simpson(a, b, c, h, f):
    result = (h / 3) * (f(a) + 4 * f(c) + f(b))
    return result


ans = simpson(x0, x2, x1, h1, f1)

print("Integrating f use simpson's rule is %.8f" % ans)

