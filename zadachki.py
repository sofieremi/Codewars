# by Dima
from math import sin


def S(a, b, angle):
    s = sin(angle)
    print(s)
    square = (a * b * round(s)) / 2
    return square


print(S(8, 4, 90))

# by Semen
numbers = [1, 45, 56, 87, 977, 996, 4, 567, 900, 907]


def filter_odd_num(in_num):
    if (in_num % 2) == 0:
        return True
    else:
        return False

out_filter = list(filter(filter_odd_num, numbers))
sorted_arr = sorted(out_filter)
print(sorted_arr)

# a = int(input())
# a = int(input())
# b = int(input())
# c = int(input())
# d = a + b + c
# d1 = d * 100 / 300
# if 100 >= d1 > 80:
#     print("5")
# if 80 >= d1 > 60:
#     print('4')
# if 60 >= d1 > 40:
#     print('3')
# if d1 <= 40:
#     print('2')
