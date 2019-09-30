import math

# We give the value of inputs, including initial approximation, tolerance and maximum iterations
x = float(eval(input("The initial approximation is: ")))
tolerance = float(eval(input("The tolerance is: ")))
maxii = float(input("The maximum iteration is: "))

# Here we have the function that we need to find the zero
f = lambda x: float(0.5) * (float(math.sin(x) + float(math.cos(x))))


# Here's the Steffensen's Method
def steff(fn, p0, tol, N):
    i = 1
    result = []
    while i <= N:
        p1 = fn(p0)
        p2 = fn(p1)
        p = p0 - ((p1 - p0) ** 2) / (p2 - 2 * p1 + p0)
        result += [p]
        if abs(p - p0) < tol:
            return print("The result is %s with iteration %d th" % (result, i))
            break
        else:
            p0 = p
        i += 1
    else:
        return print("Method failed after %d th iterations" % N)


# Now we run the algorithm with inputs.
steff(f, x, tolerance, maxii)
