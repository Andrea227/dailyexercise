import numpy as np

num = int(input("how many data points do you have: "))
n = int(num - 1)
x1 = []
a1 = []
for k in range(num):
    x1 += [float(input("Your next x is: "))]
for l in range(num):
    a1 += [float(input("Your corresponding y is: "))]

h = [1] * num
alf = [1] * num
mu = [1] * num
L = [1] * num
z = [1] * num
c = [1] * num
b = [1] * num
d = [1] * num

for i in range(0, n):
    h[i] = x1[i + 1] - x1[i]

for j in range(0, n):
    alf[j] = (3*(a1[j+1]-a1[j])/h[j]) - 3*(a1[j]-a1[j-1])/h[j-1]

L[0] = 1
mu[0] = 0
z[0] = 0

for t in range(1, n):
    L[t] = 2*(x1[t+1]-x1[t-1])-h[t-1]*mu[t-1]

for w in range(1, n):
    mu[w] = h[w]/L[w]
    z[w] = (alf[w]-h[w-1]*z[w-1])/L[w]

L[n] = 1
z[n] = 0
c[n] = 0
s = 0

for r in range(n-1, -1, -1):
    c[r] = z[r]-mu[r]*c[r+1]
    b[r] = ((a1[r+1]-a1[r])/h[r]) - h[r]*(c[r+1]+2*c[r])/3
    d[r] = (c[r+1]-c[r])/(3*h[r])

print(str(a1[:2]))
print(str(b[:2]))
print(str(c[:2]))
print(str(d[:2]))



