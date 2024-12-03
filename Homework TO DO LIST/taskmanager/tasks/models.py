from django.db import models


class Task(models.Model):
    title = models.CharField('Название задачи', max_length=30)
    description = models.TextField('Описание задачи')
    is_completed = models.BooleanField('Статус задачи', default=False)
    created_at = models.DateTimeField('Дата создания задачи',auto_created=True)

    def __str__(self):
        return f'{self.title}, {self.description}, {self.is_completed}'

    def get_absolute_url(self):
        return f'/{self.id}'
