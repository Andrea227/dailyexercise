import math

n2 = [[0.5773502692, 1.000000000], [-0.5773502692, 1.0000000000]]
n5 = [[0.9061798459, 0.2369268850], [0.5384693101, 0.4786286705], [0.0000000000, 0.5688888889],
      [-0.5384693101, 0.4786286705], [-0.9061798459, 0.2369268850]]

x0 = float(eval(input("What's your a point?: ")))
x1 = float(eval(input("What's your b point?: ")))
num = int(input("How many integers do you have: ?"))
f1 = lambda x: (x ** 2) * math.log(x)


# f1 = lambda x: (x ** 2) * math.exp(-x)
# f1 = lambda x: 2/((x**2)-4)
# f1 = lambda x: (x ** 2) * math.sin(x)
# f2 = lambda x: (math.cos(x))**2


def gaus(a, b, n, f):
    iresult = 0
    h = (b - a) / 2
    if n == 2:
        for i in range(0, n):
            c = n2[i][1]
            x = (1 / 2) * ((b - a) * (n2[i][0]) + (b + a))
            iresult = iresult + f(x) * c
        result = iresult * h
        return result
    if n == 5:
        for i in range(0, n):
            c = n5[i][1]
            x = (1 / 2) * ((b - a) * (n5[i][0]) + (b + a))
            iresult = iresult + f(x) * c
        result = iresult * h
        return result
    else:
        pass


ans = gaus(x0, x1, num, f1)
print("The result is of Gaussian quadrature is %.8f" % ans)
