import math

x0 = float(eval(input("What's your a point?: ")))
x2 = float(eval(input("What's your b point?: ")))
h1 = float((x0 + x2) / 2)
x1 = x0 + h1

f1 = lambda x: (x ** 2) * math.exp(-x)


def simpson(a, b, c, h, f):
    h1 = h / 2
    result1 = (h / 3) * (f(a) + 4 * f(c) + f(b))
    result2 = (h1 / 3) * (f(a) + 4 * f(c - h1) + f(a + h))
    result3 = (h1 / 3) * (f(a + h) + 4 * f(c + h1) + f(b))
    result = [result1, result2, result3]
    return result


ans = simpson(x0, x2, x1, h1, f1)
eerror = (1 / 15) * abs(ans[0] - ans[1] - ans[2])
aans = -math.exp(-1) * ((-1) ** 2) + math.exp(-0) * (0 ** 2) - 2 * 1 * math.exp(-1) - 2 * math.exp(-1) + 2 * math.exp(-0)
aerr = abs(aans - ans[1] - ans[2])

print("Integrating f use simpson's rule is %s" % str(ans))
print("Estimate of the error is %.8f" % eerror)
print("The actual value of integration is %.8f" % aans)
print("Actual error of integrating f use simpson's rule is %.8f" % aerr)
if eerror < aerr:
    print("This closely approximates")
else:
    print("This does not closely approximate")
