import math

# 4.1.1
h1 = 0.2
f1 = (0.74140 - 0) / h1  # forward
f2 = (1.3718 - 0.74140) / h1  # forward
f3 = (1.3718 - 0.74140) / h1  # backward
a = (f1, f2, f3)
print("Answer for 4.1.1b is %s" % str(a))

# 4.1.3
f = lambda x: math.exp(x) - 4 * x + 3
act1 = abs(f1 - f(0.0))
act2 = abs(f2 - f(0.2))
act3 = abs(f3 - f(0.4))
b = (act1, act2, act3)
print("Answer for 4.1.3b, the actual error for 0.0, 0.2, 0.4 is %s" % str(b))

# 4.1.13
c = (1 / 12) * (2.4142 - 8 * 2.6734 + 8 * 3.0976 - 3.2804)
print("Answer for 4.1.13, the 1st derivative approximation for 3 is %.6f" % c)

# 4.1.20
h2 = 0.1
h3 = 0.01
fd2 = lambda x: 3 * (x + 2) * math.exp(x) + math.cos(x)
act13 = fd2(1.3)
fd21 = (1 / (h2 ** 2)) * (11.59006 - 2 * 14.04276 + 16.86187)
fd22 = (1 / (h3 ** 2)) * (13.78176 - 2 * 14.04276 + 14.30741)
error1 = abs(fd21 - act13)
error2 = abs(fd22 - act13)
print("For h = %.2f, the approximation is %.5f" % (h2, fd21))
print("For h = %.2f, the approximation is %.5f" % (h3, fd22))
print("For h = %.2f, the actual error compared to the actual value is %.5f" % (h2, error1))
print("For h = %.2f, the actual error compared to the actual value is %.5f" % (h3, error2))
