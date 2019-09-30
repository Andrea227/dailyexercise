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
            print("P are the following result with %d iterations and p0 = %d" % (i, a))
            print(b)
            return p
            break
        else:
            p0 = p
        s += 1
    else:
        return "None"

finalresult=[]
for k in range(int(degree)):
    u = newt(x0, Tolerance, Maxi)
    if u == "None":
        break
    finalresult += [u]
    poly = deflate(poly, u)

print("Zeros are %s" % str(finalresult))
print("For p0 = %.2f , P(p0) = %.6f, P'(p0) = %.6f " % (x0, horner(x0)[0], horner(x0)[1]))