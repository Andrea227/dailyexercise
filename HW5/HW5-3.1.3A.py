import scipy.optimize as opt
import scipy
from numpy import *
from numpy import sin, cos, exp, pi, log
import math

xp = float(eval(input("What's your approximation point: ")))
degree = int(input("What's the degree of approximation poly?: "))
xlist = [float(eval(input('The first x0 is: ')))]
b = 1
while b <= int(degree):
    xlist += [float(eval(input("The next x is:")))]
    b += 1
max_x = opt.fminbound(lambda x: -abs(2/((x**3)*(log(10)))), xlist[0], xlist[degree])
max_x1 = opt.fminbound(lambda x: -abs((x-3.0)*(x-3.2)*(x-3.5)), xlist[0], xlist[degree])

print("The maximum of %d th derivative is %.2f " % (degree + 1, max_x))

error_bound = (abs(2/((max_x**3)*(log(10))))) / (math.factorial(degree + 1))
for a in xlist:
    error_bound *= (max_x1 - a)

print("The error bound is equal to or smaller than %.9f" % abs(error_bound))
