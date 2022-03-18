def f(x):
    return x * x


def modify_list(L, fn):
    for idx, v in enumerate(L):
        L[idx] = fn(v)


L = [1, 3, 2]
modify_list(L, f)
print(L)

f = lambda x: x * x
print(f(2))

fn = lambda x, y: x * y
print(fn(2, 8))

f = lambda: True
print(f())

L = [1, 2, 3, 4]
print(list(map(lambda x: x ** 2, L)))


print(list(filter(lambda x: x % 2 == 0, [2, 4, 57, 88, 9])))