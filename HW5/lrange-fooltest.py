'''
Method: Lagrange Interpolation
Section: Interpolation and Curve Fitting
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_3_01.py
Date: Aug. 6, 2017
'''
from math import cos
x = [0, 0.6, 0.9]
y = [cos(0), cos(0.6), cos(0.9)]
m = len(x)
n = m-1
xp = float(input('Enter x : '))
yp = 0
for i in range(n+1):
    L = 1
    b = []
    for j in range(n+1):
        if j != i:
            L *= (xp - x[j])/(x[i] - x[j])
        print(L)
    yp += y[i]*L
print('For x = %.1f, y = %.1f' % (xp,yp))