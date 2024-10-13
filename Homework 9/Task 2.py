# Задание 2.
# Реализуйте класс стека для работы со строками (стек строк). Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки из стека.
# При старте приложения нужно отобразить меню с помощью, которого пользователь может выбрать необходимую операцию.


class StackStr:

    def __init__(self, long: int):
        self.__long: int = long
        self.__stack_list: list = []

    def add(self, string):
        if len(self.__stack_list) < self.__long:
            self.__stack_list.append(string)
        else:
            raise Exception('Длинна строки больше длинны сводного места в стеке!')

    def pop(self):
        return self.__stack_list.pop()

    def count_str(self):
        return f'Количество строк в стеке: {(len(self.__stack_list))}'

    def empty_stack(self):
        if len(self.__stack_list) > 0:
            return f'Стек не пустой!'
        else:
            return f'Стек пустой'

    def full_stack(self):
        if len(self.__stack_list) == self.__long:
            return f'Стек полный!'
        else:
            return f'Стек не полный!'

    def del_stack_list(self):
        self.__stack_list = []

    def info_list(self) -> list:
        return self.__stack_list

    def top_str(self):
        if len(self.__stack_list) > 0:
            return self.__stack_list[-1]
        else:
            raise Exception('Невозможно получить последнее значение, так как стек пустой!')


def display_menu():
    print('\nМеню:')
    print('1. Поместить строку в стек')
    print('2. Вытолкнуть строку из стека')
    print('3. Подсчитать количество строк в стеке')
    print('4. Проверить, пустой ли стек')
    print('5. Проверить, полный ли стек')
    print('6. Очистить стек')
    print('7. Получить верхнюю строку без удаления')
    print('8. Получить всю информацию о стеке')
    print('9. Выход')


def management_stack():
    long: int = int(input('Введите размер стека: '))
    stack: StackStr = StackStr(long)

    while True:
        display_menu()
        choice: int = int(input('Введите пункт меню: '))

        if choice == 1:
            string = input('Введите строку для добавления в стек: ')
            stack.add(string)

        elif choice == 2:
            stack.pop()

        elif choice == 3:
            print(stack.count_str())

        elif choice == 4:
            print(stack.empty_stack())

        elif choice == 5:
            print(stack.full_stack())

        elif choice == 6:
            stack.pop()

        elif choice == 7:
            print(stack.info_list())

        elif choice == 8:
            print(stack.top_str())

        elif choice == 9:
            print(stack.info_list())

        else:
            print('Введите значение от 1 до 8!')


management_stack()

# a = StackStr(3)
# a.add('hello')
# print(a.info_list())
# a.add('viktor')
# print(a.info_list())
# a.add('как дела у тебя?')
# print(a.info_list())
# a.pop()
# print(a.info_list())
# print(a.count_str())
# print(a.empty_stack())
# print(a.info_list())
# a.add('7')
# print(a.info_list())
# print(a.full_stack())
# print(a.info_list())
# a.del_stack_list()
# print(a.info_list())
# print(a.top_str())































