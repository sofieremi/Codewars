import random
from random import randint


N = int(input('Введите желаемый размер поля'))
a = [['*' for i in range(N)]for j in range(N)]
x = random.randint(0, N)
y = random.randint(0, N)
a[x][y] = 'F'
for i in a:
    print(i)
X = int(N / 2)
for i in range(X):
    print('Введите координаты стен лабиринта')
    coordinates = input('Сначала x, затем y (без запятых, через пробел)').split()
    a[int(coordinates[0])][int(coordinates[1])] = '#'
    print(coordinates)
for i in a:
    print(i)
counter = 1
for i in a:
    print('сделайте ход')
    coordinates = input('Сначала x, затем y (без запятых, через пробел)').split()
    if a[int(coordinates[0])][int(coordinates[1])] == '#':
        break
    elif a[int(coordinates[0])][int(coordinates[1])] == '*':
        a[int(coordinates[0])][int(coordinates[1])] = counter
    elif a[int(coordinates[0])][int(coordinates[1])] == 'F':
        print(counter)
    counter += 1
for i in a:
    print(i)

















