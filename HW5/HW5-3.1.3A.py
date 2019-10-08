import scipy.optimize as opt
import scipy
from numpy import *
from numpy import sin, cos, exp, pi
import math

xp = float(eval(input("What's your approximation point: ")))
degree = int(input("What's the degree of approximation poly?: "))
xlist = [float(eval(input('The first x0 is: ')))]
b = 1
while b <= int(degree):
    xlist += [float(eval(input("The next x is:")))]
    b += 1
max_x = opt.fminbound(lambda x: -abs((exp(-2 * x)) * (46 * sin(3 * x) + 9 * cos(3 * x))), xlist[0], xlist[degree])
max_x1 = opt.fminbound(lambda x: -abs(x * (x - (pi / 6)) * (x - (pi / 4))), xlist[0], xlist[degree])

print("The maximum of %d th derivative is %.2f " % (degree + 1, max_x))

error_bound = (abs((exp(-2 * max_x)) * (46 * sin(3 * max_x) + 9 * cos(3 * max_x)))) / (math.factorial(degree + 1))
for a in xlist:
    error_bound *= (max_x1 - a)

print("The error bound is equal to or smaller than %.5f" % abs(error_bound))
