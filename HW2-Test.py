import sys

x1 = 0
x2 = 1
TOL1 = 10 ** (-2)
TOL2 = 10 ** (-6)
N0 = 30


# illustrate all the input


def y1(a):
    y = (a ** 3) - 7 * (a ** 2) + 14 * a - 6
    return y


# define the function we would like to find the root

i = 1
FA = y1(x1)
b = [x1]
while i <= N0:
    p = (x1 + x2) / 2
    FP = y1(p)
    b += [p]
    if FP == 0:
        print(b)
        print("the iteration end at %d th" % i)
        break
    elif (x2 - x1)/2 < TOL2:
        print(b)
        print("the iteration end at %d th" % i)
        break
    elif FA * FP > 0:
        x1 = p
    else:
        x2 = p
    i += 1

sys.exit()