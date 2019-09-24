import sys
import math

x1 = 0
x2 = 1
TOL = 10 ** (-2)
N0 = 50


# illustrate all the input


def y1(a):
    y = 12.4 - 10 * (0.5 * math.pi - math.asin(a) - a * ((1 - a ** 2) ** (1 / 2)))
    return y


# define the function we would like to find the root

i = 1
FA = y1(x1)
while i <= N0:
    p = x1 + (x2 - x1) / 2
    FP = y1(p)
    if FP == 0 or (x2 - x1) / 2 < TOL:
        print(p)
        sys.exit()
    # If we find the root directly or the error is under tolerance, we output the outcome and exit the system
    elif FA * FP > 0:
        x1 = p
        FA = FP
    else:
        x2 = p
    i += 1
    # otherwise, we continue the loop until the method fails or find an answer

print("Method failed after N0 iterations, N0 = ", "%.4f" % N0)
sys.exit()
# if the method fails, we print no answer and exit the file
