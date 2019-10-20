import numpy as np

n = int(input("how many data points do you have: "))
xp = float(eval(input("Your evaluation point is: ")))
x1 = []
y1 = []
for i in range(n):
    x1 += [float(input("Your next x is: "))]
for j in range(n):
    y1 += [float(input("Your corresponding y is: "))]

Dy = np.zeros((n, n))
Dy[:, 0] = y1
for k in range(1, n):
    for l in range(n - k):
        Dy[l][k] = Dy[l + 1][k - 1] - Dy[l][k - 1]

print(Dy)

h = (x1[-1] - x1[0]) / (n - 1)


def combup(n, r):
    demo = n
    i = 1
    while i < r:
        demo *= (n-i)
        i += 1
    else:
        return demo


def factor(x):
    a = 1
    if x!= 1:
        i = 2
        while i <= x:
            a *= i
            i += 1
        else:
            return a
    else:
        return a


def forward(u):
    s = (u - x1[0]) / h
    sum = Dy[0][0]
    for i in range(1, n):
        sum = sum + combup(s, i) * Dy[0][i] / factor(i)
        print(sum)
    return print("The final evaluation is %.8f" % sum)


forward(xp)
