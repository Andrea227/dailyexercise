import sys
import math

p0 = 1 / 2
TOL = 10 ** (-4)
N0 = 50


# illustrate all the input


def y1(a):
    y = (1 / 2) * ((a ** 3) + 1)
    return y


def y2(a):
    y = (2 / a) - (1 / (a ** 2))
    return y


def y3(a):
    y = (2 - (1 / a)) ** (1 / 2)
    return y


def y4(a):
    y = -(1 - 2 * a) ** (1 / 3)
    return y


# define the function we would like to find the root

i = 1
p1 = p0
while i <= N0:
    p = y1(p1)
    if abs(p - p1) < TOL:
        print("p1 =", "%.6f" % p)
        break
    # If we find the root directly or the error is under tolerance, we output the outcome and exit the system
    else:
        p1 = p
    i += 1
    # otherwise, we continue the loop until the method fails or find an answer

i = 1
p2 = p0
while i <= N0:
    if p2 == 0:
        print("2nd Method failed since divergence")
        break
    else:
        p = y2(p2)
        if abs(p - p2) < TOL:
            print(print("p2 =", "%.6f" % p))
            break
        # If we find the root directly or the error is under tolerance, we output the outcome and exit the system
        else:
            p2 = p
    i += 1
    # otherwise, we continue the loop until the method fails or find an answer

i = 1
p3 = p0
while i <= N0:
    if p3 == 0:
        print("2nd Method failed since divergence")
        break
    else:
        p = y3(p3)
        if abs(p - p3) < TOL:
            print(print("p3 =", "%.6f" % p))
            break
        # If we find the root directly or the error is under tolerance, we output the outcome and exit the system
        else:
            p3 = p
    i += 1
    # otherwise, we continue the loop until the method fails or find an answer

i = 1
p4 = p0
while i <= N0:
    p = y4(p4)
    if abs(p - p4) < TOL:
        print(print("p4 =", "%.6f" % p))
        sys.exit()
    # If we find the root directly or the error is under tolerance, we output the outcome and exit the system
    else:
        p4 = p
    i += 1
    # otherwise, we continue the loop until the method fails or find an answer

sys.exit()
