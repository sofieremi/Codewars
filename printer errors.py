def printer_error(s):
    good = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    bad_sum = 0
    for i in good:
        bad_sum += s.count(i)
        len_s = str(len(s))
        bad_sum_str = str(bad_sum)

    return bad_sum_str + '/' + len_s


print(printer_error('aaabbbbhaijjjm'))

