import sys
import math

p0 = 1
TOL = 10 ** (-2)
N0 = 50


# illustrate all the input


def y1(a):
    y = (3 + 3 * (a ** 2)) ** (1 / 4)
    return y


# define the function we would like to find the root

i = 1
while i <= N0:
    p = y1(p0)
    if abs(p - p0) < TOL:
        print("p =", "%.6f" % p)
        sys.exit()
    # If we find the root directly or the error is under tolerance, we output the outcome and exit the system
    else:
        p0 = p
    i += 1
    # otherwise, we continue the loop until the method fails or find an answer

print("Method failed after N0 iterations, N0 = " % N0)
sys.exit()
# if the method fails, we print no answer and exit the file
