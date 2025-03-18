from django.db import models


class User(models.Model):
    name = models.CharField('Имя', max_length=20)

    def __str__(self):
        return f'{self.name}'
