size_map = int(input('Введите размеры карты(необходимо ввести одно число:->'))
a = [['*' for i in range(size_map)] for j in range(size_map)]
for i in a:
    print(i)
print('Сейчас необходимо дать координаты для ваших однопалубников:')
for i in range(4):
    coordinates = input('Сначала x, затем y ( без запятых, через пробел)').split()
    a[int(coordinates[0])][int(coordinates[1])] = '1'
    print(coordinates)
for i in a:
    print(i)
print('Сейчас необходимо ввести координаты для ваших двухпалубников:')
for i in range(2):
    coordinates = input('Сначала x, затем y( без запятых, через пробел)').split()
    a[int(coordinates[0])][int(coordinates[1])] = '2'
    coordinates = input('Сначала x, затем y( без запятых, через пробел)').split()
    a[int(coordinates[0])][int(coordinates[1])] = '2'
    print(coordinates)
for i in a:
    print(i)
for i in range(3):
    print('Сейчас необходимо ввести координаты для вашего трёхпалубника:')
    coordinates = input('Сначала x, затем y( без запятых, через пробел)').split()
    a[int(coordinates[0])][int(coordinates[1])] = '3'
    print(coordinates)
for i in a:
    print(i)
