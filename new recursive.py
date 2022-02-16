
a = int(input())
b = int(input())
if(a + b) % 4 != 0:
    print(-1)
else:
    n = (a + b) // 4
    if a >= n and b >= n:
        print(a - n, b - n)
    else:
        print(-1)


n = int(input('enter s'))
steps = n // 3 + 1
print(steps)



for i in range(1, len(a)):
    if a[i:] == a[i:] [::-1]:
        break
print(a + a[0:i][::-1])