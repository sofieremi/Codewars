a =[]
for i in range(1,11):
    a.append(input())
    print(a)
b = a[0]
a[0] = a[1]
a[1] = b
print(a)