# Задание 3.
# Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.) и
# поле для хранения копеек (центы, евроценты, копейки и т.д.).
# Реализовать методы для вывода суммы на экран, задания значений для частей.


class Money:

    def __init__(self, ruble: int, penny: int):
        self._ruble = ruble
        self._penny = penny

    def whole_part(self, ruble):
        self._ruble: int = ruble

    def remains(self, penny):
        self._penny = penny

    def print_result(self):
        print(f'Вывод: {self._ruble} рублей {self._penny} копеек')


a = Money(10, 50)
a.print_result()
