lst = ['1', '2', '3']
a = dict.fromkeys(lst, 'asd')
print(a)
a.clear()
print(a)

d = {True: 1, False: 'Ложь', 'list': [1, 2, 3], 5: 5}
print(d)

d2 = d.copy()
print(d2)

d2['list'] = [5, 6, 7]
print(d2)
print(d)

d2 = dict(d)
print(d2)

print(d.get('list'))  # выводит None при вызове значения несуществующего ключа
print(d['list'])  # в том же случае выводит ошибку
print(d.get(3, False))  # возврат False в случае отсутствия указанного аргумента

print(d.setdefault('list'))  # вызов значения по ключу
print(d)
print(d.setdefault(3))  # добавляем в словарь ключ(дефолтное значение - None)
print(d)
del d[3]  # удаление ключа
print(d)
d.setdefault(3, 'three')  # с помощью этого метода добавляем в словарь ключ и значение(в аргументах)
print(d)

d.pop(3)  # удаление ключа с возможностью его возврата
print(d)

print(d.pop('abc', False))  # возвращает указанное значение, если ключа(первого аргумента) нет в словаре
#  в том же случае, при отсутствии второго аргумента выдает ошибку KeyError

print(d.popitem())  # метод, удаляющий случайно выбранную запись(ключ - значение)
print(d)

a = {'age': 30, 'language': 'spanish'}
print(a.keys())

for i in a:  # обход словаря в цикле по коллекции ключей
    print(i)

print(a.values())

for x in a.values():  # обход словаря с помощью цикла с выводом значений
    print(x)

for i in a.items():  # выводит кортежи в формате ключ - значение
    print(i)

print(a.items())

for key, value in a.items():
    print(key, value)

s = dict(one=1, two=2, three=3, four=4)
print(s)
c = {2: 'неудовлетворительно', 3: 'удовлетворительно', 'four': 'good', 5: 'excellent'}
s.update(c)  # совпадающие ключи перезаписываются
print(s)

d3 = {**c, **s}  # объединение словарей
print(d3)


