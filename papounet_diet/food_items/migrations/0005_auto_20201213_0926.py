# Generated by Django 3.1.2 on 2020-12-13 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_items', '0004_product_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='energy_kcal',
        ),
        migrations.RemoveField(
            model_name='product',
            name='fat_100g',
        ),
        migrations.RemoveField(
            model_name='product',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sugars_100g',
        ),
    ]