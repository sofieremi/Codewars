# number = input().split()
# for i in range(len(number)):
#     number[i] = int(number[i])
# print(number)
# # if number < 0: - доделать
# if number[-1] < 9:
#     number[-1] += 1
# else:
#     number[-2] += 1
#     number[-1] = 0
# print(number)


# number = int(input())
# number += 1
# print(number)


# a = input('enter some numbers').split()
# a.sort()
# i = int(input())
#
#
#
# print(a)

# a = 5678555678903439839484502505855
# str_a = str(a)
# print(set(str_a))

# a = input('enter some numbers').split()
# for i in range(len(a)):
#     a[i] = int(a[i])
# target = int(input('enter a target number'))
# b = 0
# dct = {}
# counter = 0
# for i in range(len(a)):
#     dct[i] = counter
#     b = target - a[i]
#     if b in a:
#         for key, value in dct.items():
#             print(value)
#     counter += 1


nums = [2, 8, 12, 15]
target = 14
required = {}
for i in range(len(nums)):
    if target - nums[i] in required:
        print(required[target - nums[i]], i)
    else:
        required[nums[i]] = i
    print(required)


