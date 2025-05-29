from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField

# Типы пользователей
class UserRole(models.TextChoices):
    CUSTOMER = 'customer', _('Заказчик')
    EXPERT = 'expert', _('Исполнитель')

# Кастомный пользователь
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=10,
        choices=UserRole.choices,
        default=UserRole.CUSTOMER,
    )
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def is_customer(self):
        return self.role == UserRole.CUSTOMER

    @property
    def is_expert(self):
        return self.role == UserRole.EXPERT

# Профиль заказчика
class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = PhoneNumberField(region='RU', blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)
    education = models.CharField(max_length=150, blank=True)
    faculty = models.CharField(max_length=150, blank=True)
    specialty = models.CharField(max_length=150, blank=True)

# Типы работ
class WorkType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Предметы
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Задания
class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('completed', 'Завершена'),
        ('cancelled', 'Отменена'),
    ]

    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    attached_file = models.FileField(upload_to='tasks/files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    def clean(self):
        if self.deadline < timezone.now().date():
            raise ValidationError({'deadline': 'Срок выполнения не может быть в прошлом.'})

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"

# Профиль исполнителя
class ExpertProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    university = models.CharField(max_length=150)
    specialty = models.CharField(max_length=150)
    graduation_year = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject)
    work_types = models.ManyToManyField(WorkType)
    diploma_image = models.ImageField(upload_to='experts/diplomas/', blank=True, null=True)
    social_link = models.URLField(blank=True, null=True)
