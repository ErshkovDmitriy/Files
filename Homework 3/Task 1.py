# Задание 1.
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Cars:

    def __init__(self, model: str, age: int, manufacturer: str, engine: int | float, color: str, price: int):
        self.__model: str = model
        self.__age: str = str(age)
        self.__manufacturer: str = manufacturer
        self.__engine: str = str(engine)
        self.__color: str = color
        self.__price: str = str(price)

    def __str__(self) -> str:
        pass

    def print(self):
        print(f'Модель автомобиля: {self.__model}')
        print(f'Год выпуска: {self.__age}')
        print(f'Производитель: {self.__manufacturer}')
        print(f'Объем двигателя: {self.__engine}')
        print(f'Цвет: {self.__color}')
        print(f'Цена: {self.__price}')


Toyota: Cars = Cars('Camry', 2018, 'Toyota', 3.0, 'белый', 650000)
Toyota.print()

