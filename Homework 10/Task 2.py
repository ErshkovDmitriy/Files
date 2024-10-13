# Задача 2.
# Инкапсуляция
#
# Описание: Создайте класс Car, который содержит информацию о марке автомобиля, максимальной скорости и
# текущей скорости.
# Инкапсулируйте переменные с текущей скоростью, чтобы нельзя было напрямую её изменять.
#
# Условия:
#
#  • Создайте конструктор, принимающий марку и максимальную скорость.
#  • Создайте методы для увеличения и уменьшения скорости, контролируя, чтобы скорость не превышала максимальную.
#  • Добавьте метод для отображения текущей скорости.
class Car:

    def __init__(self, brand: str, max_speed: int):
        self.__brand: str = brand
        self.__max_speed: int = max_speed
        self.__current_speed: int = 0

    def increase_speed(self, km: int) -> int:
        if self.__current_speed + km <= self.__max_speed:
            self.__current_speed += km
            return self.__current_speed
        else:
            raise Exception('Нельзя превышать максимально допустимую скорость!!!')

    def reduction_speed(self, km: int) -> int:
        if self.__current_speed >= km:
            self.__current_speed -= km
            return self.__current_speed
        raise Exception(f'Нельзя снизить скорость на {km} км/ч. Скорость не может быть отрицательной!')

    def info(self):
        return self.__current_speed


a = Car('BMW', 200)
a.increase_speed(50)
print(a.info())
a.reduction_speed(20)
print(a.info())
a.increase_speed(170)
print(a.info())