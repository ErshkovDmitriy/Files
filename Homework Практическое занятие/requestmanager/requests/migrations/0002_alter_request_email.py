# Generated by Django 5.1.3 on 2024-12-04 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
    ]
