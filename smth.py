z = [4, 6, 7, 3, 0]
a = 0
while a < 4:
    if z[a]>z[a+1]:
        s = z[a]
        z[a] = z[a+1]
        z[a+1] = s
    a +=1
print(z[a])
наименьшее число
12 урок

