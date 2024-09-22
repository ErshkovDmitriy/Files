# Задание 2.
# Создайте класс для конвертирования температуры из Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температуры возвращать это значение с помощью статического метода.


class Temperature:

    count: int = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        Temperature.count += 1
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        Temperature.count += 1
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def Counter():
        return Temperature.count


print(f'Температура по Форингейту равна: {Temperature.celsius_to_fahrenheit(20)}')
print(f'Температура по Цельсии равна: {Temperature.fahrenheit_to_celsius(32)}')
print(f'Количество подсчетов {Temperature.Counter()}')
