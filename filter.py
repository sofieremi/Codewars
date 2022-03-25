# # this program is filtering odd nums
# numbers = [1, 2, 4, 5, 7, 8, 10, 11]
#
#
# def filter_odd_num(in_num):
#     if (in_num % 2) == 0:
#         return True
#     else:
#         return False
#
#
# out_filter = filter(filter_odd_num, numbers)

# print("Тип объекта out_filter: ", type(out_filter))
# print("Отфильтрованный список: ", list(out_filter))

# list1 = ["Python", "CSharp", "Java", "Go"]
# list2 = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp"]
#
#
# def filter_duplicate(string_to_check):
#     if string_to_check in ll:
#         return False
#     else:
#         return True
#
#
# # Применение filter() для удаления повторяющихся строк
# ll = list2
# out_filter = list(filter(filter_duplicate, list1))
# ll = list1
# out_filter += list(filter(filter_duplicate, list2))
#
# print("Отфильтрованный список:", out_filter)


# # Список стоп-слов
# list_of_stop_words = ["в", "и", "по", "за"]
#
# # Строка со стоп-словами
# string_to_process = "Сервис по поиску работы и сотрудников HeadHunter опубликовал подборку высокооплачиваемых вакансий в России за август."
#
# # lambda-функция, фильтрующая стоп-слова
# split_str = string_to_process.split()
# filtered_str = ' '.join((filter(lambda s: s not in list_of_stop_words, split_str)))
#
# print("Отфильтрованная строка:", filtered_str)

# Два массива, имеющие общие элементы
# arr1 = ['p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0']
# arr2 = ['p', 'y', 'd', 'e', 'v', ' ', '2', '.', '0']


# Лямбда с использованием filter() для поиска общих значений
# def interSection(arr1, arr2):
#     out = list(filter(lambda it: it in arr1, arr2))
#     return out
#
#
# print(interSection(arr1, arr2))
#
# #
# # функция main
# if __name__ == "__main__":
#     out = interSection(arr1, arr2)
#     print("Отфильтрованный список:", out)


"""
    ????????????????????Вызов функции filter() без функции???????????????????????
    why does 'bool' returns True?
"""

# Список значений, которые могут быть True или False
bools = ['bool', 20, 0, None, True, False, 1, 1 - 1, 2 % 2]

# Передали None вместо функции в filter()
out = filter(None, bools)

# Вывод результата
for iter in out:
    print(iter)