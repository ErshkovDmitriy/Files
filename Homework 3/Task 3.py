# Задание 3.
# Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.


class Stadium:

    def __init__(self, title: str, opening_date: int | str, country: str, city: str, capacity: int):
        self.__title: str = title
        self.__opening_date: str = str(opening_date)
        self.__country: str = country
        self.__city: str = city
        self.__capacity: str = str(capacity)

    def __str__(self) -> str:
        pass

    def print(self):
        print(f'Название стадиона : {self.__title}')
        print(f'Дата открытия : {self.__opening_date}')
        print(f'Страна : {self.__country}')
        print(f'Город : {self.__city}')
        print(f'Вместительность : {self.__capacity}')


Toyota: Stadium = Stadium('Santiago Bernabéu Stadium ',   '14 декабря 1947', 'Испания', 'Мадрид', 81044)
Toyota.print()
