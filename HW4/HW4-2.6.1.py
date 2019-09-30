degree = float(eval(input("The degree is: ")))
i = 1
poly = [float(eval(input('The first coefficient is: ')))]
while i <= degree:
    poly += [float(eval(input("The next coefficient is:")))]
    i += 1
x0 = float(eval(input("Your approximation zero is: ")))
Maxi = float(input("The maximum iteration is: "))
Tolerance = float(eval(input("The tolerance is: ")))

def horner(x):
    y = poly[len(poly)-1]
    z = poly[len(poly)-1]
    for j in range(len(poly)-2, 0, -1):
        y = x * y + poly[j]
        z = x * z + y
    y = x * y + poly[0]
    b = [y, z]
    return b

def newt(p0, tol, N0):
    i = 1
    b = []
    a = p0
    while i <= N0:
        result = [horner(p0)[0], horner(p0)[1]]
        p = p0 - (result[0] / result[1])
        b += [p]
        if abs(p - p0) < tol:
            return print("With %d th iteration, Newton's method is %s with p0 = %.2f " % (i, str(b), a))
            break
        else:
            p0 = p
        i += 1
    else:
        return print("Newton's Method failed after N0 iterations, N0 = ", "%.4f" % N0)


newt(x0, Tolerance, Maxi)
print("For p0 = %.2f , P(p0) = %.6f, P'(p0) = %.6f " % (x0, horner(x0)[0], horner(x0)[1]))