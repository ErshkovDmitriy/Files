# Generated by Django 5.1.3 on 2024-12-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_genrebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=30, verbose_name='Жанр'),
        ),
        migrations.DeleteModel(
            name='GenreBook',
        ),
    ]
