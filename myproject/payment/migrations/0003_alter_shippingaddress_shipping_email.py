# Generated by Django 5.0.6 on 2024-06-15 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_rename_address1_shippingaddress_shipping_address1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='shipping_email',
            field=models.CharField(max_length=255),
        ),
    ]
