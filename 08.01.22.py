# a = []
# for i in range(10):
#     b = int(input())
#     a.append(b)
# a.sort()
# print(a[-3])


# counter = 0
# J = ['t', 'h', 't', 'u', 'i']
# S = ['a', 'j', 'e', 't', 'y']
# J = set(J)
# for i in J:
#     if i in S:
#         counter += 1
# print(counter)



# ax^2 + bx + c = 0
# ax^2 + bx + c = a(x-x1)(x-x2)
# x1, x2 - корни квадратного уравнения
# D = b^2 - 4ac
# x1 и x2
# x1 = ((-b + D ** 0.5) / (2 * a))
# x2 = ((-b - D ** 0.5) / (2 * a))


# ax^2 + bx + c = 0
x1 = float(input('enter x1'))
x2 = float(input('enter x2'))
b = x2 + x1
c = x1 * x2
if b < 0 and c < 0:
    print('x^2', b, 'x', c, ' = 0')
elif b < 0 and c > 0:
    print('x^2', b, 'x +', c, ' = 0')
elif b > 0 and c < 0:
    print('x^2 +', b, 'x', c, ' = 0')
else:
    print('x^2 +', b, 'x +', c, ' = 0')







