# # n = 123456
# # n = str(n)
# # a = []
# # for i in range(len(n)):
# #     a.append(int(n[i]))
# #     # for j in a:
# #     #      j = int(j)
# # print(list(a[::-1]))
# weapon = input('enter the name of your weapon')
# n = int(input('enter number of streets'))
# bullets = 0
#
# if weapon == 'PT92':
#     bullets = 17
# if weapon == 'M4A1':
#     bullets = 30
# if weapon == 'M16A2':
#     bullets = 30
# if weapon == 'PSG1':
#     bullets = 5
# a = n * 3
# m = a // bullets
# if a % bullets == 0:
#     print(m)
# else:
#     print(m + 1)
# import string
#
# a = input('enter first element')
# b = input('enter second element')
# if a not in string.ascii_letters or b not in string.ascii_letters:
#     print(-1)
# if a.islower() and b.islower() or a.isupper() and b.isupper():
#     print(1)
# if a.islower() and b.isupper() or a.isupper() and b.islower():
#     print(0)

# a = input('enter something')
# print(string.ascii_letters)
# if a not in string.ascii_letters:
#     print(1)

#
# def func(lst, n):
#     for i in range(0, len(lst), n):
#         yield lst[i:i + n]
#
#
# print(list(func([8, 7, 6, 5, 4, 3, 2, 1], 4)))

#
# for i in range(1, 10, 2):
#     print(i, end=" ")
# print('all!')


# def function(arr: list, n: int) -> list:
#     flag = True
#     counter = 0
#     memory = []
#     if n == 1:
#         return [[i] for i in arr]
#     while flag:
#         memory.append(arr[counter:counter + n])
#         counter += n - 1
#         print(memory)
#         flag = False
#     if arr[counter:counter + n] not in memory:
#         memory.append(arr[len(arr) - n: len(arr)])
#         return memory


# print(function([3, 5, 8, 13], 2))
#
# def each_const(name_arr: list, n: int) -> list:
#     flag = True
#     count = 0
#     memory = []
#     if not name_arr:
#         return []
#     if n == 1:
#         return [[i] for i in name_arr]
#     while flag:
#         if len(name_arr[count:count + n]) < n:
#             if name_arr[len(name_arr) - n: len(name_arr)] not in memory:
#                 memory.append(name_arr[len(name_arr) - n: len(name_arr)])
#             flag = False
#             return memory
#         memory.append(name_arr[count:count + n])
#         if count + 2 > len(name_arr):
#             return memory
#         else:
#             count += n - 1
#
#
# print(each_const([], 3))


# name = input('enter your name')
# # for i in range(len(name.split())):
# name = name.split()
# print(name[0][0].upper(), '.', name[1][0].upper())


# def final_grade(exam, projects):
#     grade = 0
#     if exam > 90 and projects > 10:
#         return 100
#     if exam > 75 and projects >= 5:
#         return 90
#     if exam > 50 and projects >= 2:
#         return 75
#     if exam == 0 and projects == 0:
#         return 0
#
#
# print(final_grade(73, ))
# def points(games):
#     point = 0
#     for i in games:
#         if i[0] > i[2]:
#             point += 3
#             continue
#         if i[0] < i[2]:
#             point += 0
#             continue
#         if i[0] == i[2]:
#             point += 1
#             continue
#     return point


# print(points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']))

# import math
#
#
# def new_avg(arr, navg):
#     n = len(arr)
#
#     summ = 0
#     for i in arr:
#         summ += i
#     donation = navg * (n + 1)
#     last = donation - summ
#     if last <= 0:
#         raise ValueError('positive number expected')
#     else:
#         return math.ceil(last)
#
#
# print(new_avg([14, 30, 5, 7, 9, 11, 15], 2))


# def solution(n, d):
#     n = list(str(n))
#     if d > len(n):
#         return n
#     elif d <= 0:
#         return []
#     else:
#         return n[len(n) - d: len(n)]
#
#
# print(solution(1343, 5))

# import math
#
# A = 0
# B = 0
# ticket = 10
# card = 100
# percent = 0.95
# while math.ceil(B + card)  < A:
#     A += ticket
#     B *
#     =
# a = 10
# 10while a < 100:
#     a *= 0.95
#     print(a)
#     continue

# import math
#
# card = 30
# percent = 0.95
# ticket = 10
# price = card
# a = ticket
# while price < 100:
#     a *= percent
#     price += a
#     print(price)
# print('final price:', math.ceil(price))

# import math
#
#
# def movie(card, ticket, percent):
#     B = card
#     price = ticket
#     A = 0
#     times = 0
#     flag = True
#     while flag:
#         if math.ceil(B) >= A:
#             times += 1
#             A += ticket
#             price *= percent
#             B += price
#             print(math.ceil(B))
#             print(A)
#         else:
#             flag = False
#             return times
#
#
# print(movie(2500, 20, 0.9))


n = 0
sentence = input('enter a sentence')
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(len(vowels)):
    n += sentence.count(vowels[i])
print(n)


# s = input('enter a word')
# if len(s) % 2 == 0:
#     print(s[len(s) // 2 - 1:len(s) // 2 + 1])
# if len(s) % 2 != 0:
#     print(s[(len(s) - 1) // 2])


# def function(a, b):
# a = list(input())
# b = list(input())
# a1 = list(a)
# b1 = list(b)
# if a1.sort()
#
# b1.sort()

#
# a = 1
# b = 1

#
# def some_func(string_1: str, string_2: str):
#     first_str = {i: string_1.count(i) for i in string_1}
#     second_str = {i: string_2.count(i) for i in string_2}
#     if first_str.items() == second_str.items():
#         return "Yes"
#     else:
#         return "No"
#
#
# print(some_func('qwe', 'ewq'))
#
#
# def func(str_1: str, str_2: str):
#     return str_1.split().sort() == str_2.split().sort()
#
#
# print(func('asd', 'dsa'))


# print(type(type(type)))

#
# print('kaban'.split().sort() == 'banka'.split().sort())
# print('kaban'.split().sort())
# print('banka'.split().sort())
# print('kaba'.split().sort() == 'banka'.split().sort())


# a = 'qwe'
# b = 'ewq'
# a1 = a.split()
# b1 = b.split()
# print(a1 == b1)
# print(a1, b1)

# a = '312'
# a.split()
# a.sort()
#
# print(a)


# a = list(input())
# b = list(input())
# a.sort()
# b.sort()
# print(a == b)


