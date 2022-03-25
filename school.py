# 1
# a + (b * x) + (c * y * z)

# [((a * x) - b) * x + c] * x - d

# ((a + b) / c) + (c / (a * b)

# ((x + y) / a1) * (a2 / (x - y))

# (10 ** 4) * alpha + (3 + 1 / 5) * beta

# (1 + (x / factorial(2)) + (y / factorial(3))) / (1 + (2 / (3 + x * y)))

# 3
# (1 + x) ** 2

# sqrt(1 + x ** 2)

# cos(x ** 2) ** 2

# log((x / 2), 2)

# asin(x)

# (e ** x + e **(-x)) / 2

# x ** sqrt(2)

# (1 + x) ** (1 / 3)

# sqrt(x ** 8 + 8 ** x)

# x * y * z - 3.3 * fabs(x + y ** (1 / 4)) / (10 ** 7 + factorial(log(4, 2.7))

# (beta + sin(pi ** 4) ** 2) / cos(2) + fabs(ctg(y))

# 5
import math

print('a)', type(1 + 0.0))
print('б)', type(20 / 4))
print('в)', type(4 ** 2))
print('г)', type(math.sqrt(16)))
print('д)', type(math.sin(0)))
print('е)', type(int(-3.14)))

# 4
print('а)', int(6.9))
print('б)', int(6.2))
print('в)', 20 // 6)
print('г)', 2 // 5)
print('д)', round(6.9))
print('е)', round(6.2))
print('ж)', 20 % 6)
print('з)', 2 % 5)
print('и)', (((3 * 7) // 2) % (7 / 3)) - int(math.sin(1)))
