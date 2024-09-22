# Задание 3.
# Создайте класс для перевода из метрической системы в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно реализуйте перевод мер длины.


class Convector:

    @staticmethod
    def foot_in_metre(foot):
        return foot / 3.28084

    @staticmethod
    def metre_in_foot(metre):
        return metre * 3.28084


print(f'Переводим футы в метры: {Convector.foot_in_metre(55)}')
print(f'Переводим метры в футы: {Convector.metre_in_foot(40)}')
