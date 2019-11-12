import numpy as np


# In this way we are going to compute the monte carlo approximation directly to the analytical definite integration
# result
def f(x):
    return 1 - 4 * (x ** 2)


# Number of the points we use
n = 1000000

# The endpoints of the range and image
x_min, x_max = -0.5, 0.5
y_min, y_max = 0.0, 1.0

# Uniformly random points
x = np.random.uniform(x_min, x_max, n)  # 均匀分布
y = np.random.uniform(y_min, y_max, n)

# Calculate the number of points falls under the function curve
res = sum(np.where(y < f(x), 1, 0))

# Calculate the approximation to the definite integral
integral = res / n

print('The Monte Carlo approximation of definite integral is : ', integral)
