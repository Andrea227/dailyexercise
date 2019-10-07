from scipy.interpolate import lagrange
from math import cos

xp = float(input("What's your approximation point: "))
degree = input("What's the degree of approximation poly?: ")
xlist = [float(eval(input('The first x0 is: ')))]
b = 1
while b <= int(degree):
    xlist += [float(eval(input("The next x is:")))]
    b += 1
f = lambda x: cos(x)
y = []
for a in xlist:
    y += [f(a)]
poly = lagrange(xlist, y)

acterror = abs(f(xp)-poly(xp))

from numpy.polynomial.polynomial import Polynomial

print("The coeffients are %s" % str(Polynomial(poly).coef))
print("The final approximation formula is")
print(poly)
print("The approxiamation at %.4f is %.6f " % (xp, poly(xp)))
print("The actual error is %.6f " % acterror)
