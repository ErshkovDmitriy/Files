from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as

# Типы пользователей
class UserRole(models.TextChoices):
    CUSTOMER = 'customer', _('Заказчик')
    EXPERT = 'expert', _('Исполнитель')

# Кастомный пользователь
class CustomUser(AbstractUser):
    role = models.CharField(
        max_length=10,
        choices=UserRole.choices,
        default=UserRole.CUSTOMER,
    )
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

# Профиль заказчика
class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100)
    university = models.CharField(max_length=150)
    faculty = models.CharField(max_length=150)
    specialty = models.CharField(max_length=150)

# Типы работ
class WorkType(models.TextChoices):
    TEST = 'Контрольная'
    ESSAY = 'Реферат'
    ESSAY2 = 'Эссе'
    COURSE = 'Курсовая работа'
    DIPLOMA = 'Диплом'
    OTHER = 'Другое'

# Задания
class Task(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    work_type = models.CharField(max_length=50, choices=WorkType.choices)
    subject = models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    attached_file = models.FileField(upload_to='tasks/files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Профиль исполнителя
class ExpertProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    university = models.CharField(max_length=150)
    specialty = models.CharField(max_length=150)
    graduation_year = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    subjects = models.ManyToManyField('Subject')
    work_types = models.ManyToManyField('WorkTypeOption')
    diploma_image = models.ImageField(upload_to='experts/diplomas/', blank=True, null=True)
    social_link = models.URLField(blank=True, null=True)

# Предметы
class Subject(models.Model):
    name = models.CharField(max_length=100)

# Варианты типов работ (многие ко многим)
class WorkTypeOption(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

