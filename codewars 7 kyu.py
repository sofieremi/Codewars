def is_divisible(*a):
    counter = 1
    flag = True
    while flag:
        if len(a) == 1:
            break
        if counter == len(a):
            break
        b = a[0] % a[counter]
        if b == 0:
            counter += 1
            continue
        else:
            flag = False
    return flag


print(is_divisible(12, 3, 5))
