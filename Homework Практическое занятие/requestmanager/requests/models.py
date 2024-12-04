from django.db import models


class Request(models.Model):
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('email')
    message = models.TextField('Текстовое поле', max_length=400)
    submitted_at = models.DateTimeField('Дата создания задачи', auto_created=True)

    def __str__(self):
        return f'{self.name}, {self.email}, {self.message}, {self.submitted_at}'
