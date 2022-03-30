# x = 1
# print(id(x))
#
# # другая переменная с тем же именем
# x = 2
# print(id(x))
#
# my_str = "пишем кот"
# # my_str[-1] = 'д'
# my_str2 = my_str
# print(id(my_str))
# print(id(my_str2))
# print(my_str is my_str2)
# # на этом моменте я пересоздала переменную my_str => str is immutable
# my_str += '!'
# print(my_str)
# print(id(my_str))
# print(my_str2)
# print(id(my_str2))
#
# my_list = list(my_str)
# print(my_list)
# print(id(my_list))
# my_list[-2] = 'д'
# print(my_list)
# print(id(my_list))
# # => lists are mutable
#
#
# x = 5
#
#
# def add(var):
#     var += 1
#     print(var)
#
#
# print(id(x))
# print(add(x))
#
# # глобальная переменная(находится вне области определения функции)
# # локальной переменной будет называться та, что находится внутри функции)
# y = [1, 2, 3]
#
#
# def change(var):
#     var[0] += 1
#     print(var)
#     return y
#
#
# print(change(y))
# print(id(y))
# # неявное изменение глобальной пременной
# print(y)
#
# string = 'string'
# print(string.replace('s', 'S'))
# print(string.split())
# print(string.upper())
# print(string.lower())
# print(string.title())
# print(string.lstrip())
# print(string.rstrip())
# print(string.strip())
# print(string.count())
# print(string[0])
# print(string[start:stop:step])
# print(string * 6)
# # concatenate
#
#
# array = [1, 2, 3, 4]
# print(list.append())
# # list.copy()
# list.count()
# list.index()
# list.insert(i, x)only delete
# list.pop([])delete and return
# list.remove()
# list.reverse()
# list.sort()

man = {'age': 30, 'sex': 'male'}
man['age'] = 35
print(man)