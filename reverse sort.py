n = input().split()
arr = []
for i in n:
    i = int(i)
    arr.append(i)
new_arr = []
test = len(arr)
for j in range(test):
    m = max(arr)
    new_arr.append(m)
    arr.remove(m)
print(new_arr)