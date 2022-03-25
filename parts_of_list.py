def partlist(arr):
    result = []
    start_str = arr[0]
    next_str = ' '.join(arr[1:])
    test = next_str.split()
    for i in range(len(arr) - 1):
        result.append((start_str, ' '.join(test)))
        start_str += ' ' + test[0]
        test.pop(0)
    return result


print(partlist(['I', 'wish', 'I', 'had', 'not', 'come']))
