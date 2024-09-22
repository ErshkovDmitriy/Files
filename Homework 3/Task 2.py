# Задание 2.
# Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

class Book:

    def __init__(self, title: str, age: int, publisher: str, genre: str, author: str, price: int):
        self.__title: str = title
        self.__age: str = str(age)
        self.__publisher: str = publisher
        self.__genre: str = genre
        self.__author: str = author
        self.__price: str = str(price)

    def __str__(self) -> str:
        pass

    def print(self):
        print(f'Название книги: {self.__title}')
        print(f'Год выпуска: {self.__age}')
        print(f'Издательство: {self.__publisher}')
        print(f'Жанр: {self.__genre}')
        print(f'Автор: {self.__author}')
        print(f'Цена: {self.__price}')


War_and_Peace: Book = Book('Война и Мир', 1869, 'Русский вестник', 'Роман', 'Лев Николаевич Толстой', 500)
War_and_Peace.print()

