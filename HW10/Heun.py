import math
import numpy as np

f = lambda t, y: (y ** 2) / (1 + t)
ft = lambda t: -1 / (math.log(1 + t))

answer = np.zeros((11, 4))
answer[0][0] = 0
answer[0][1] = -(1 / (math.log(2)))
answer[0][2] = ft(1)
answer[0][3] = abs(answer[0][2] - answer[0][1])


def midpoint():
    for i in range(1, 11):
        t1 = 1 + 0.1 * (i - 1)
        t2 = 1 + 0.1 * i
        answer[i][0] = i
        w = answer[i - 1][1]
        answer[i][1] = w + (0.1 / 4) * (f(t1, w) + 3 * f((t1 + (2 * 0.1 / 3)),
                                                         w + (2 * 0.1 / 3) * f(t1 + (0.1 / 3),
                                                                               w + (0.1 / 3) * f(t1, w))))
        answer[i][2] = ft(t2)
        answer[i][3] = abs(answer[i][2] - answer[i][1])
    print(answer)


np.set_printoptions(suppress=True, floatmode='fixed')
print("The following are: order, approximation, true value, and actual error")
midpoint()
