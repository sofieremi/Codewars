a = [0, 1]


def fibonacci(n, a):
    if n == 0:
        return a
    else:
        a.append(a[-1] + a[-2])
        return fibonacci(n - 1, a)


print(fibonacci(10, a))






