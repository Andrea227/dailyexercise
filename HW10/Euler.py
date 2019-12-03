import numpy as np
import math

f = lambda t, y: -y + 1
# (2 * y / t) + (t ** 2) * math.exp(t)
ft = lambda t: 1 - math.exp(-t)
# (t ** 2) * (math.exp(t) - math.exp(1))
h = 0.01
answer = np.zeros((101, 4))


def euler():
    t = 0
    w = 0
    t1 = ft(0)
    print(t, w, t1)
    for i in range(1, 101):
        w = w + h * f(t, w)
        t = 0 + i * 0.01
        t1 = ft(t)
        e = abs(t1 - w)
        answer[i][0] = t
        answer[i][1] = w
        answer[i][2] = t1
        answer[i][3] = e
    print(answer)
    return print("Here starts the second part")


np.set_printoptions(suppress=True, floatmode='fixed')
euler()

######### 2nd part ##########
# f1 = lambda t: answer[1][1] * (t - 1)
# f2 = lambda t: answer[5][1] + ((answer[6][1] - answer[5][1]) * (t - answer[5][0]) / (answer[6][0] - answer[5][0]))
# f3 = lambda t: answer[9][1] + ((answer[10][1] - answer[9][1]) * (t - answer[9][0]) / (answer[10][0] - answer[9][0]))

# ask = [1.04, 1.55, 1.97]
# answer2 = np.zeros((3, 4))
# answer2[0][0] = ask[0]
# answer2[1][0] = ask[1]
# answer2[2][0] = ask[2]
# answer2[0][1] = f1(ask[0])
# answer2[1][1] = f2(ask[1])
# answer2[2][1] = f3(ask[2])
# answer2[0][2] = ft(ask[0])
# answer2[1][2] = ft(ask[1])
# answer2[2][2] = ft(ask[2])
# answer2[0][3] = abs(ft(ask[0])-f1(ask[0]))
# answer2[1][3] = abs(ft(ask[0])-f2(ask[1]))
# answer2[2][3] = abs(ft(ask[0])-f3(ask[2]))

# print(answer2)
