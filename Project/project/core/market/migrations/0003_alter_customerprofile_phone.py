# Generated by Django 5.1.3 on 2025-05-28 07:12

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_remove_customerprofile_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='RU'),
        ),
    ]
