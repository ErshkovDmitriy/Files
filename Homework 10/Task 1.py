# Задача 1.
# Магические методы
#
# Описание: Создайте класс ComplexNumber, который будет представлять комплексное число и реализуйте сложение
# и вычитание комплексных чисел, используя магические методы add() и sub().
#
# Условия:
#
#  • Конструктор должен принимать действительную и мнимую части.
#  • Реализуйте магические методы для сложения и вычитания.
from __future__ import annotations
import math


class ComplexNumber:

    def __init__(self, real_number: float, imaginary_number: float):
        self.__real_number: float = real_number
        self.__imaginary_number: float = imaginary_number

    def __add__(self, other: ComplexNumber) -> ComplexNumber:
        return ComplexNumber(self.__real_number + other.__real_number,
                             self.__imaginary_number + other.__imaginary_number)

    def __sub__(self, other: ComplexNumber) -> ComplexNumber:
        return ComplexNumber(self.__real_number - other.__real_number,
                             self.__imaginary_number - other.__imaginary_number)

    def __str__(self) -> str:
        sign = '+' if self.__imaginary_number >= 0 else '-'
        return f'{self.__real_number} {sign} i{math.fabs(self.__imaginary_number)}'


a = ComplexNumber(1, 5)
b = ComplexNumber(2, -3)
c = a + b
print(a)
print(b)
print(c)