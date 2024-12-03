# Задача 1. Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте программы происходит загрузка списка сотрудников из
# указанного пользователем файла.

# from __future__ import annotations

name_file = input('Введите название файла: ')

class Office:

    def __init__(self, employees: list):
        self._employees: list = employees

    def add(self, Employee):
        self._employees.append(f'{Employee}')

    def open_file(self):
        with open(name)
    def __str__(self):
        return f'{self._employees}'


class Employee:

    def __init__(self, surname: str, age: int):
        self._surname: str = surname
        self._age: int = age

    def __str__(self):
        return f'surname: {self._surname}, age: {self._age}'

    def dict(self):
        return {'surname': self._surname, 'age': self._age}


    # @staticmethod
    # def input_in_console() -> Employee:
    #     surname: str = input('Введите фамилию сотрудника: ')
    #     age: int = int(input('Введите возраст сотрудника: '))
    #     return Employee(surname, int(age))


empl = Employee('dima', 21)
print(empl)
o = Office([])
o.add(empl)
print(o)
# while True:
#
#     choose = input('Введите пункт меню: ')
#
#     if choose == '1':
#         office.add()
#     else:
#         break
