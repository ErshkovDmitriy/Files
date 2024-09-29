# Задание 1.
# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования, реализуйте класс CoffeeMachine (содержит информацию о кофемашине),
# класс Blender (содержит информацию о блендере), класс MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые для работы методы.


class Device:

    def __init__(self, firm: str, made_in: str):
        self._firm: str = firm
        self._made_in: str = made_in

    def __str__(self) -> str:
        return f'Название фирмы: {self._firm} \nСтрана производителя: {self._made_in}'


class CoffeeMachine(Device):
    
    def __init__(self, firm: str, made_in: str, what_coffee: str):
        super().__init__(firm, made_in)
        self._what_coffee: str = what_coffee

    def __str__(self) -> str:
        return f'Конечный продукт: {self._what_coffee}'


class Blender(Device):

    def __init__(self, firm: str, made_in: str, electricity: int):
        super().__init__(firm, made_in)
        self._electricity: int = electricity

    def __str__(self) -> str:
        return (f'Название фирмы: {self._firm} \nСтрана производителя: {self._made_in} \n'
                f'Рабочий ток: {self._electricity}')


class MeatGrinder(Device):

    def __init__(self, firm: str, made_in: str, nozzle: str):
        super().__init__(firm, made_in)
        self._nozzle: str = nozzle

    def __str__(self) -> str:
        return f'Насадка: {self._nozzle}'


a = Blender('Bosch', 'Russia', 220)
print(a)