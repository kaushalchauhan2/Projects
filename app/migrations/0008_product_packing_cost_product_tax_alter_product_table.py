# Generated by Django 4.1 on 2023-04-20 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='packing_cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tax',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterModelTable(
            name='product',
            table='app_Product',
        ),
    ]
