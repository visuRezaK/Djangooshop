# Generated by Django 5.0.6 on 2024-05-22 01:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_is_sale_product_sale_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='picute',
            new_name='picture',
        ),
        migrations.AlterField(
            model_name='customer',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 5, 21, 21, 57, 31, 700660)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 5, 21, 21, 57, 31, 700660)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 5, 21, 21, 57, 31, 700660)),
        ),
    ]
