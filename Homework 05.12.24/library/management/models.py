from django.db import models


class Genre(models.Model):
    name = models.CharField('Жанр', max_length=30)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):

    title = models.CharField('Название книги', max_length=30)
    author = models.TextField('Автор', max_length=30)
    published_year = models.IntegerField('Дата публикации')
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    is_available = models.BooleanField('Статус доступности книги', default=True)

    def __str__(self):
        return f'{self.title}, {self.author}'


class User(models.Model):

    username = models.TextField('Имя пользователя', max_length=30)
    email = models.EmailField('email')

    def __str__(self):
        return f'{self.username}, {self.email}'


class Rental(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rental_date = models.DateField('Дата аренды')
    return_date = models.DateField('Дата возврата')

    def __str__(self):
        return f'{self.user}, {self.book}'


