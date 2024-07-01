# Generated by Django 5.0.6 on 2024-05-21 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 21, 7, 40, 74650)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 21, 7, 40, 75861)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 21, 7, 40, 75706)),
        ),
    ]
