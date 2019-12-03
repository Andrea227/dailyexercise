import numpy as np

f = lambda t, y: (y+y**2)/t
df = lambda t, y: (2*(y**2)*(y+1))/(t**2)

answer = np.zeros((5, 2))
answer[0][0] = 0
answer[0][1] = -2


def taylor():
    for i in range(1, 5):
        t1 = 1 + 0.5 * (i - 1)
        answer[i][0] = i
        w = answer[i - 1][1]
        answer[i][1] = w + 0.5 * (f(t1, w) + (0.5 / 2) * df(t1, w))
    print(answer)


taylor()