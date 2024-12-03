# Generated by Django 5.1.3 on 2024-12-01 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, verbose_name='Дата создания задачи')),
                ('title', models.CharField(max_length=30, verbose_name='Название задачи')),
                ('description', models.TextField(verbose_name='Описание задачи')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Статус задачи')),
            ],
        ),
    ]