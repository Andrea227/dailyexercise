import numpy as np

num = int(input("how many data points do you have: "))
n = num - 1
xp = float(eval(input("Your evaluation point is: ")))
x1 = []
y0 = []
y1 = []
for i in range(num):
    x1 += [float(input("Your next x is: "))]
for j in range(num):
    y0 += [float(input("Your corresponding y is: "))]
for k in range(num):
    y1 += [float(input("Your corresponding y1 is: "))]

z = [0]*(2*num)
q = np.zeros((2*num, 2*num))
i = 0
while n >= i >= 0:
    z[2*i] = x1[i]
    z[2*i+1] = x1[i]
    q[2*i+1][0] = y0[i]
    q[2*i][0] = y0[i]
    q[2*i+1][1] = y1[i]
    if i != 0:
        q[2*i][1] = (q[2*i][0] - q[2*i-1][0])/(z[2*i] - z[2*i-1])
    i += 1

k = 2
while 2*n+1 >= k >= 2:
    j = 2
    while k >= j >= 2:
        q[k][j] = (q[k][j-1] - q[k-1][j-1])/(z[k] - z[k-j])
        j += 1
    k += 1

print(x1)
print(y0)
print(y1)
print(z)
print(q)
