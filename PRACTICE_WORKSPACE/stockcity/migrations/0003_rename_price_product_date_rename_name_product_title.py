# Generated by Django 4.2.13 on 2024-06-01 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockcity', '0002_rename_title_product_name_rename_date_product_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='Title',
        ),
    ]
