# Задача 3.
# Абстрактные классы
#
# Описание: Создайте абстрактный класс Shape, который имеет абстрактный метод get_area(). Затем создайте классы
# Square и Triangle, которые наследуются от этого абстрактного класса и реализуют свои версии метода get_area().
#
# Условия:
#
#  • Класс Square должен принимать длину стороны, а класс Triangle — основание и высоту.
#  • Метод get_area() должен возвращать площадь фигуры.
#
# Каждая из этих задач поможет вам лучше понять принципы ООП, такие как инкапсуляция, наследование,
# полиморфизм и абстракция.

from abc import abstractmethod, ABC


class Shape:

    def __init__(self, name: str):
        self.__name: str = name

    @abstractmethod
    def get_area(self):
        raise Exception('Реализуйте метод get_area')


class Square(Shape):

    def __init__(self, name: str, side: float):
        super().__init__(name)
        self.__side: float = side

    def get_area(self):
        return self.__side * self.__side


class Triangle(Shape):

    def __init__(self, name: str, height: float, footing: float):
        super().__init__(name)
        self.__height: float = height
        self.__footing: float = footing

    def get_area(self):
        return (self.__height * self.__footing) / 2


a = Square('Квадрат', 4)
print(a.get_area())

b = Triangle('Треугольник', 10, 5)
print(b.get_area())
