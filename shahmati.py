"""На шахматной доске расположены две пешки. Требуется поставить на доску слона так, чтобы обе пешки оказались под боем.

Шахматная доска имеет размер 8 на 8. Слон бьет ближайшую фигуру на каждом из четырех диагональных направлений от себя."""


def doska(map):
    for i in map:
        print(i)
    print('\n')


a = [['*' for i in range(8)] for j in range(8)]
print('Введите координаты пешек:')
x = int(input('введите х для пешки1'))
y = int(input('введите y для пешки1'))
x1 = int(input('введите х для пешки1'))
y1 = int(input('введите y для пешки1'))
a[x][y] = 'п'
a[x1][y1] = 'п'
doska(map=a)
i_x = x
j_y = y
while True:
    if i_x == 0 or j_y == 7:
        break
    i_x -= 1
    j_y += 1
    if a[i_x][j_y] != '*':
        continue
    else:
        a[i_x][j_y] = "1"
doska(map=a)
i_x = x
j_y = y
while True:
    if i_x == 0 or j_y == 0:
        break
    i_x -= 1
    j_y -= 1
    if a[i_x][j_y] != '*':
        continue
    else:
        a[i_x][j_y] = "1"
doska(map=a)
i_x = x
j_y = y
while True:
    if i_x == 7 or j_y == 0:
        break
    i_x += 1
    j_y -= 1
    if a[i_x][j_y] != '*':
        continue
    else:
        a[i_x][j_y] = "1"
doska(map=a)
i_x = x
j_y = y
while True:
    if i_x == 7 or j_y == 7:
        break
    i_x += 1
    j_y += 1
    if a[i_x][j_y] != '*':
        if a[i_x][j_y] == '1':
            a[i_x][j_y] = "c"
            print('Слон установлен', i_x, j_y)
            break
        continue
    else:
        a[i_x][j_y] = "2"
doska(map=a)
i_x = x1
j_y = y1
while True:
    if i_x == 0 or j_y == 7:
        break
    i_x -= 1
    j_y += 1
    if a[i_x][j_y] != '*':
        if a[i_x][j_y] == '1':
            a[i_x][j_y] = "c"
            print('Слон установлен', i_x, j_y)
            break
        continue
    else:
        a[i_x][j_y] = "2"
doska(map=a)
i_x = x1
j_y = y1
while True:
    if i_x == 0 or j_y == 0:
        break
    i_x -= 1
    j_y -= 1
    if a[i_x][j_y] != '*':
        if a[i_x][j_y] == '1':
            a[i_x][j_y] = "c"
            print('Слон установлен', i_x, j_y)
            break
        continue
    else:
        a[i_x][j_y] = "2"
doska(map=a)
i_x = x1
j_y = y1
while True:
    if i_x == 7 or j_y == 0:
        break
    i_x += 1
    j_y -= 1
    if a[i_x][j_y] != '*':
        if a[i_x][j_y] == '1':
            a[i_x][j_y] = "c"
            print('Слон установлен', i_x, j_y)
            break
        continue
    else:
        a[i_x][j_y] = "2"
doska(map=a)
i_x = x1
j_y = y1
while True:
    if i_x == 7 or j_y == 7:
        break
    i_x += 1
    j_y += 1
    if a[i_x][j_y] != '*':
        if a[i_x][j_y] == '1':
            a[i_x][j_y] = "c"
            print('Слон установлен', i_x, j_y)
            break
        continue
    else:
        a[i_x][j_y] = "2"
doska(map=a)












