import math
import numpy as np

f = lambda t, y: (y ** 2) / (1 + t)
df = lambda t, y: ((y ** 2) * (2 * y - 1)) / ((1 + t) ** 2)
df2 = lambda t, y: (2 * (y ** 2) * (1 - 3 * y + 3 * (y ** 2))) / ((1 + t) ** 3)
df3 = lambda t, y: (2 * (y ** 2) * (-3 + 11 * y - 18 * (y ** 2) + 12 * (y ** 3))) / ((1 + t) ** 4)

answer = np.zeros((11, 2))
answer[0][0] = 0
answer[0][1] = -(1/(math.log(2)))


def taylor():
    for i in range(1, 11):
        t1 = 1 + 0.1 * (i-1)
        answer[i][0] = i
        w = answer[i - 1][1]
        answer[i][1] = w + 0.1 * (
                f(t1, w) + (0.1 / 2) * df(t1, w) + ((0.1**2) / 6) * df2(t1, w) + ((0.1 ** 3) / 24) * df3(t1, w))
    print(answer)


taylor()
