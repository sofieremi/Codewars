# # № 2
# for x in range(2):
#   for y in range(2):
#     for z in range(2):
#       if (not(x) and y and z) or (not(x) and not(y) and z) or (not(x) and not (y) and not(z)) == 1:
#         print(x, y, z)
#
# # № 2
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if (not(x) and y and z) or (not(x) and not(y) and z) or (not(x) and not(y) and not(z)) == 1:
#                 print(x, y, z)


# № 25
# from math import sqrt
# divs = []
# n = 36
# for d in range(1, round(sqrt(n)) + 1):
#     if n % d == 0:
#         divs += [d, n//d]
# print(*sorted(set(divs)))


# № 25
from math import sqrt

divs = []
n = 36
if int(sqrt(n)) == sqrt(n):
    divs += [int(sqrt(n))]
for d in range(1, round(sqrt(n))):
    if n % d == 0:
        divs += [d, n // d]
print(*sorted(divs))
