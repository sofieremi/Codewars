

def function(a, p, q):
    import string
    a = str(a)
    p = int(p)
    q = int(q)
    letters = string.ascii_uppercase
    print(letters)
    # дано число а по основанию p
    # число p - основание, в котором число находится
    # число q - основание, к которому нужно привести
    # смотрим на основание р полученного числа а
    # если число а в десятичной с.с., то приводим его к основанию q
    # деленим его на данное основание и складываем остатки от деления
    # если число в другой с.с., то приводим его в 10
    d = ''
    if p != 10:
        a = int(a, p)
    while True:
        s = int(a) % q
        r = int(a) // q
        a = int(r)
        if s == 0 and r == 0:
            break
        else:
            if s < 10:
                d += str(s)
            else:
                d += letters[s - 10]
    return(d[::-1])
result = function('ABC', 16, 2)
print(result)




