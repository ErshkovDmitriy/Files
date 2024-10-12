# Задание 1.
# Создать базовый класс Фигура с методом для подсчета площади. Создать производные классы: прямоугольник,
# круг, прямоугольный треугольник, трапеция со своими методами для подсчета площади.
# Задание 2.
# Для классов из задания 1 нужно переопределить магические методы int(возвращает площадь) и str(возвращает
# информацию о фигуре).
import math
from abc import abstractmethod, ABC


class Figure:

    def __init__(self, name: str):
        self.__name: str = name

    def __str__(self):
        return f'Название фигуры: {self.__name}'

    @abstractmethod
    def area(self) -> float:
        raise NotImplemented('Необходимо реализовать метод area!')


class Rectangle(Figure):

    def __init__(self, name: str, side_a: float, side_b: float):
        super().__init__(name)
        self.__side_a: float = side_a
        self.__side_b: float = side_b

    def area(self) -> float:
        return self.__side_a * self.__side_b

    def __str__(self):
        return super().__str__() + f'.\nПлощадь равна: {self.__side_a * self.__side_b}'


class Circle(Figure):

    def __init__(self, name: str, radius: float):
        super().__init__(name)
        self._radius: float = radius

    def area(self) -> float:
        return math.pi * self._radius ** 2

    def __str__(self):
        return super().__str__() + f'.\nПлощадь равна: {math.pi * self._radius ** 2}'


class Triangle(Figure):

    def __init__(self, name_figure: str, side_a: int, side_b: int):
        super().__init__(name_figure)
        self._side_a: int = side_a
        self._side_b: int = side_b

    def area(self) -> float:
        return self._side_a * self._side_b / 2

    def __str__(self):
        return super().__str__() + f'.\nПлощадь равна: {self._side_a * self._side_b / 2}'


class Trapezoid(Figure):

    def __init__(self, name_figure: str, side_a: int, side_b: int, height: int):
        super().__init__(name_figure)
        self._side_a: int = side_a
        self._side_b: int = side_b
        self._height: int = height

    def area(self) -> float:
        return (self._side_a + self._side_b) / 2 * self._height

    def __str__(self):
        return super().__str__() + f'.\nПлощадь равна: {(self._side_a + self._side_b) / 2 * self._height}'


a = Rectangle('Прямоугольник', 3, 5)
print(a)
print(a.area())

