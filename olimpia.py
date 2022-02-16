a = str(input())
print(len(a))
for i in range(1, len(a)):
    print(i, a[i])
# returns the number of elements in an object
    if a[i:] == a[i:][::-1]:
        break

print(a + a[0:i][::-1])











slovo = str(input())
a = slovo[::-1]
if slovo == a:
    print('yes')
else:
    print('no')
