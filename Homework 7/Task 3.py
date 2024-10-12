# Задание 3.
# Создайте базовый класс Shape для рисования плоских фигур.
# Определите методы:
# ■ Show() — вывод на экран информации о фигуре;
# ■ Save() — сохранение фигуры в файл;
# ■ Load() — считывание фигуры из файла.
# Определите производные классы:
# ■ Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
# ■ Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
# ■ Circle — окружность с заданными координатами центра и радиусом;
# ■ Ellipse — эллипс с заданными координатами верхнего угла описанного вокруг него прямоугольника со сторонами,
# параллельными осям координат, и размерами этого прямоугольника.
# Создайте список фигур, сохраните фигуры в файл,
# загрузите в другой список и отобразите информацию о каждой из фигур.


import math
from abc import abstractmethod


class Shape:

    def __init__(self, x: int, y: int):
        self._x: int = x
        self._y: int = y

    @abstractmethod
    def show(self) -> str:
        raise NotImplemented('Необходимо реализовать метод show!')

    @abstractmethod
    def save(self):
        raise NotImplemented('Необходимо реализовать метод save')

    @abstractmethod
    def load(self):
        raise NotImplemented('Необходимо реализовать метод load')

    def __str__(self):
        return f'Координата х: {self._x}\nКоордината y: {self._y}\n'


class Management:

    def __init__(self):
        self.__shapes: list[Shape] = []

    def add(self, shape: Shape):
        self.__shapes.append(shape)


class Square(Shape):

    def __init__(self, x: int, y: int, length_side: int):
        super().__init__(x, y)
        self._length_side: int = length_side

    def show(self) -> str:
        return super().__str__() + f'Длина стороны: {self._length_side}'

    def save(self):


# class Rectangle(Shape):
#
#     def __init__(self, x: int, y: int, side_a: int, side_b: int):
#         super().__init__(x, y)
#         self._side_a: int = side_a
#         self._side_b: int = side_b
#
#
# class Circle(Shape):
#
#     def __init__(self, x: int, y: int, radius: int):
#         super().__init__(x, y)
#         self._radius: int = radius
#
#
# class Ellipse(Shape):
#     pass


a = Square(2, 2, 5)
print((a.save_square_in_file(5)))
