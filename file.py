x1 = 0
x2 = 0
a = int(input('введите а'))
b = int(input('введите б'))
c = int(input('введите с'))
D = b * b - 4 * a * c
if D < 0:
    print(D, 'ответа нет')
elif D == 0:
    x = -b / (2 * a)
    print(D, x)
else:
    x1 = ((-b + D ** 0.5) / (2 * a))
    x2 = ((-b - D ** 0.5) / (2 * a))
    print(D, x1, x2)
