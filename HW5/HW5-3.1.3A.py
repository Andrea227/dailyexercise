import scipy.optimize as opt
import scipy
from numpy import *
from numpy import sin, cos
import math

xp = float(input("What's your approximation point: "))
degree = int(input("What's the degree of approximation poly?: "))
xlist = [float(input('The first x0 is: '))]
b = 1
while b <= int(degree):
    xlist += [float(eval(input("The next x is:")))]
    b += 1
max_x = round(opt.fminbound(lambda x: -sin(x), xlist[0], xlist[degree]), 2) # abs(cos(x)) if degree is 1

print("The maximum of %d th derivative is %.2f " % (degree+1, max_x))

error_bound = (sin(max_x))/(math.factorial(degree+1)) # abs(cos(x)) if degree is 1
for a in xlist:
    error_bound *= (xp-a)

print("The error bound is equal to or smaller than %.5f" % abs(error_bound))