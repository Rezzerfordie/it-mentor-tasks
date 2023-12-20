from abc import ABC, abstractmethod


class DsMOT:    # Дескриптер для транспорта

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class MeansOfTransport:
    color = DsMOT()
    brand = DsMOT()
    num_wheels = DsMOT()

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show_color(self):
        return f'Цвет транспортного средства{self.color}'

    def show_brand(self):
        return f'Марка транспортного средства{self.brand}'


class Car(MeansOfTransport):
    car_drive = 4

    @classmethod
    def num_drive(cls):
        print(cls.car_drive)

    def __new__(cls, *args, **kwargs):
        print(f'Создаются атрибуты класса')

    def __init__(self, num_wheels, weight, vol_tank):
        super().__init__(self.brand, self.color)
        self.num_wheels = num_wheels
        self._weight = weight
        self.__vol_tank = vol_tank

    def __eq__(self, other):
        return self._weight == other._weight

    def __sub__(self, other):
        return self._weight + other._weight

    def __rsub__(self, other):
        return self, other


class Moped(MeansOfTransport):

    def __init__(self, num_wheels):
        super().__init__(self.brand, self.color)
        self.num_wheels = num_wheels

    @staticmethod
    def time(distance, max_speed):
        time = distance/max_speed
        return (f'''Время за которое мопед проедет дистанцию {distance} '
                на максимальной скорости {max_speed} равно {time}''')


class Calculater:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def summ(self):
        return self.x + self.y


class ContCalculater(Calculater):
    def summ(self):
        return str(self.x) + str(self.y)


class Animals(ABC):

    def __init__(self, name, breed, age):
        self.name = str(name)
        self.breed = str(breed)
        self.age = int(age)

    @abstractmethod
    def voice(self):
        pass

    def eat(self):
        return f"{self.__class__.__name__} eat "

    def hobby(self):
        return f'{self.__class__.__name__} like '


class SinglentonForAnimals(ABC):
    __instance = None
    r_name = None
    r_breed = None
    r_age = None

    def __new__(cls, name, breed, age):
        if cls.__instance is None:
            cls.r_name = name
            cls.r_breed = breed
            cls.r_age = age
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, name, breed, age):
        super().__init__(name, breed, age)
        self.name = self.r_name
        self.breed = self.r_breed
        self.age = self.r_age


class Cat(Animals):

    def voice(self):
        return f'{self.__class__.__name__} says mew-mew'

    def eat(self):
        return super().eat() + 'fish'

    def hobby(self):
        return super().hobby() + 'sleep'


class Dog(SinglentonForAnimals, Animals):

    def voice(self):
        return f'{self.__class__.__name__} says woof - woof'

    def eat(self):
        return super().eat() + 'meat'

    def hobby(self):
        return super().hobby() + 'playing'


d = Dog("Шнурок", "Гончая", 13)
d1 = Dog('Bob', 'Bobtail', 7)
d2 = Dog('Cher', 'MaiTai', 8)
print(d.__dict__, d1.__dict__, d2.__dict__)
print(id(d), id(d2), id(d1))
