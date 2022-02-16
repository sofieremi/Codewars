n = []
n.insert(0, int(input('1')))
n.insert(1, int(input('2')))
n.insert(2, int(input('3')))
a = n[0] + n[1]
b = n[1] * n[2]
print(str(max(a, b)) + str(min(a, b)))


a = int(input('1'))
b = int(input('2'))
c = int(input('3'))
k = 0
while a > 0 and b > 0 and c > 0:
    if a > 0 and c > 0:
        a -= 1
        k += 1
    if b > 0 and c > 0:
        b -= 1
        k += 1
    if a > 0 and c > 0:
        c -= 1
        k += 1
    if a > 0 and b > 0:
        b -= 1
        k += 1
print(k)

