# Задание 2.
# Создайте класс Ship, который содержит информацию о корабле. С помощью механизма наследования, реализуйте
# класс Frigate (содержит информацию о фрегате), класс Destroyer (содержит информацию об эсминце), класс
# Cruiser (содержит информацию о крейсере). Каждый из классов должен содержать необходимые для работы методы.

class Ship:

    def __init__(self, name: str, made_in: str):
        self._name: str = name
        self._made_in: str = made_in

    def __str__(self) -> str:
        return f'Название корабля: {self._name} \nСтрана производителя: {self._made_in}'


class Frigate(Ship):

    def __init__(self, name: str, made_in: str, displacement: int):
        super().__init__(name, made_in)
        self._displacement: int = displacement

    def __str__(self) -> str:
        return f'Водоизмещение корабля: {self._displacement}'


class Destroyer(Ship):

    def __init__(self, name: str, made_in: str, speed: int):
        super().__init__(name, made_in)
        self._speed: int = speed

    def __str__(self) -> str:
        return (f'Название корабля: {self._name} \nСтрана производителя: {self._made_in} \n'
                f'Скорость корабля: {self._speed}')


class Cruiser(Ship):

    def __init__(self, name: str, made_in: str, long: str):
        super().__init__(name, made_in)
        self._long: str = long

    def __str__(self) -> str:
        return f'Длинна корабля: {self._long}'


a = Destroyer('Титаник', 'Англия', 20)
print(a)