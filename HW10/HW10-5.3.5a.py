import numpy as np

f = lambda t, y: (y / t) - (y / t) ** 2
df = lambda t, y: -(t - 2 * y) * (y ** 2) / (t ** 4)

answer = np.zeros((11, 2))
answer[0][0] = 0
answer[0][1] = 1


def taylor():
    for i in range(1, 11):
        t1 = 1 + 0.1 * (i - 1)
        answer[i][0] = i
        w = answer[i - 1][1]
        answer[i][1] = w + 0.1 * (f(t1, w) + (0.1 / 2) * df(t1, w))
    print(answer)

