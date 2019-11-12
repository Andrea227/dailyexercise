import numpy as np

# Number of selected points
n = 1000000

# Choose the point uniformly randomly in the cubic of 1
xrand = np.random.uniform(0, 1, n)
yrand = np.random.uniform(0, 1, n)
zrand = np.random.uniform(0, 1, n)

# Fulfill the restraint of the real volume we want
sumv = 0
for i in range(n):
    a = (xrand[i] - 0.5) ** 2 + (zrand[i] - 0.5) ** 2
    b = (yrand[i] - 0.5) ** 2 + (zrand[i] - 0.5) ** 2
    c = (xrand[i] - 0.5) ** 2 + (yrand[i] - 0.5) ** 2
    if a < 0.25 and b < 0.25 and c < 0.25:
        sumv += 1
    else:
        pass

# Calculate the monte carlo approximation of volume
integral = sumv / n

# print('Double  cylinder intersection is: ', integral)
print('Triple cylinder intersection is: ', integral)
