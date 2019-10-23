def platter(n):
    x = 0
    b = 0
    for i in range(1, 1000):
        if x <= 3*n:
            if i % 4 == 0 and i % 7 != 0:
                x = x + 1
                if x == 3 * n:
                    b = i
            elif i % 7 == 0 and i % 4 != 0:
                x = x - 1
                if x == 3*n:
                    b = i
            elif i % 7 == 0 and i % 4 == 0:
                x = x + 0
                if x == 3*n:
                    b = i
            else:
                pass

        else:
            return b/2


print(platter(2))
print(platter(4))
print(platter(5))
