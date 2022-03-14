class MotorTransport(object):
    def __init__(self, color, year, auto_type):
        self.color = color
        self.year = year
        self.auto_type = auto_type

    def stop(self):
        print('pressing the brake pedal')

    def drive(self):
        print('WRRRRRUUUUM!')


ferrari_testarossa = MotorTransport('Red', 1987, 'passenger car')
ferrari_testarossa.drive()


class Student:
    def __init__(self, name, surname, group):
        self.name = name
        self.surname = surname
        self.group = group


alex = Student('Alex', 'Ivanov', 'admin')


class Weapon:
    # статический атрибут
    name = 'Default name'

    def __init__(self, weapon_type):
        self.weapon_type = weapon_type
        # динамический атрибут


class SpaceShip:
    def atack(self):
        print('ПИУ!')


star_destroyer = SpaceShip()
star_destroyer.atack()


class AirConditioner:
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity

    def turn_on(self):
        print('***now in the room will be coooool***')

    def turn_off(self):
        print('soo, this way you`ll burn in this room')


ballu = AirConditioner('BPAC-07', 785)
ballu.turn_on()
ballu.turn_off()


class MightiesWeapon:
    name = 'Default name'

    def __init__(self, weapon_type):
        self.weapon_type = weapon_type


# создаем статическое имя для всего класса
# переопределение атрибута name без создания объекта
MightiesWeapon.name = 'Steel Sword'
print(MightiesWeapon.name)
# создаем объект и инициализируем динамический атрибут с помощью конструктора
hero_sword = MightiesWeapon('sword')
# задаем имя для конкретного объекта
hero_sword.name = 'Excalibur'

# статическое имя для всего класса не изменится
print(MightiesWeapon.name)
# печатаем имя конкретного объекта
print(hero_sword.name)


class Animal:
    def make_a_sound(self):
        print('издает животный звук')


class Cat(Animal):
    def drop_everything(self):
        print('вставай скорее, я все уронил!')

    def make_a_sound(self):
        print('ррммяяяууу!')


class Dog(Animal):
    def dig_the_ground(self):
        print('однажды я докопаю до ядра планеты!')

    def make_a_sound(self):
        print('гав-гав!')


Pushok = Cat()
Pushok.make_a_sound()
Pushok.drop_everything()

Sobaken = Dog()
Sobaken.make_a_sound()
Sobaken.dig_the_ground()
