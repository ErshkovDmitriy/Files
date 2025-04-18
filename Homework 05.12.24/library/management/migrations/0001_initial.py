# Generated by Django 5.1.3 on 2024-12-09 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название книги')),
                ('author', models.TextField(max_length=30, verbose_name='Автор')),
                ('published_year', models.IntegerField(max_length=4, verbose_name='Дата публикации')),
                ('genre', models.TextField(max_length=30, verbose_name='Жанр')),
                ('is_available', models.BooleanField(default=False, verbose_name='Статус доступности книги')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=30, verbose_name='Имя пользователя')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateField(verbose_name='Дата аренды')),
                ('return_date', models.DateField(verbose_name='Дата возврата')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.user')),
            ],
        ),
    ]
