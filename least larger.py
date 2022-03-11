def least_larger(a, i):
    arr = []
    for n in range(len(a)):
        if a[n] > a[i]:
            arr.append(a[n])
    print(arr)
    if not arr:
        return -1
    else:
        return a.index(min(arr))


print(least_larger([1, 3, 2, 5, 4], 0))
