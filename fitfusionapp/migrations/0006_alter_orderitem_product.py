# Generated by Django 5.1.4 on 2025-01-27 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitfusionapp', '0005_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitfusionapp.bench'),
        ),
    ]
