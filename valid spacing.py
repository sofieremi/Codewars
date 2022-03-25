def valid_spacing(s):
    answer = ''
    spaces = s.count(' ')
    elements = len(s.split())
    if s == ' ':
        answer = True
    elif spaces == elements - 1:
        answer = True
    else:
        answer = False
    return answer


print(valid_spacing(''))
