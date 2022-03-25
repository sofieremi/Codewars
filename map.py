elements = [1, 2, 3, 4]
elements_by2 = []

for element in elements:
    elements_by2.append(element * 2)

print(elements_by2)

elements = [1, 2, 3, 4]
element_by2 = [element * 2 for element in elements]

print(element_by2)


def multiply(x):
    return x * 2


elements = [1, 2, 3, 4]
elements_by2 = list(map(multiply, elements))

print(elements_by2)


def even_odd(x):
    if x % 2 == 0:
        return 0
    else:
        return x


elements = [1, 2, 3, 4]
elements_new = list(map(even_odd, elements))
print(elements_new)

elements = [1, 2, 3, 4]
elements_by2 = list(map(lambda x: x * 2, elements))
print(elements_by2)

cities = ['madrid', 'munich', 'valencia']
cities_cap = list(map(lambda x: x.title(), cities))
print(cities_cap)

elements = [1, 2, 3, 4]
elements_str = list(map(str, elements))
print(elements_str)

elements = [1.2, 2.5, 4.9, 9.0]
elements_int = list(map(int, elements))
print(elements_int)
