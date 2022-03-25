class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.limbs = 4
    def moved(self):
        print(self.name, 'moved')


nikita = Human('nikita', 25)
print(nikita.age)
nikita.moved()
print(nikita.limbs)
ann = Human('ann', 20)
nikita.moved()
ann.moved()

a = 'abc'
print(a.upper())
print(type(a))
a.upper()



class Clothes:
    def __init__(self, type, color, characteristics, size):
        self.type = type
        self.color = color
        self.characteristics = characteristics
        self.size = size
    def made(self):
        print(self.type, 'made in Morocco')
skirt = Clothes('skirt', 'black', 'midi', 'xs')
print(skirt.color)
print(skirt.made())

a = [1, 2, 3]
a.insert(0, 4)
print(a)
print(a.pop(0))
print(a)
a = [5, 6, 7, 8, 9]
print(a[::3])
a = '12345'
for i in range(5):
    print('hello')
a = 1
while a <= 5:
    print('hello')
    a += 1

