# Generated by Django 5.1.3 on 2024-12-12 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_alter_book_genre_delete_genrebook'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gener', models.ManyToManyField(to='management.book')),
            ],
        ),
    ]
