# Generated by Django 4.2.13 on 2024-06-01 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockcity', '0003_rename_price_product_date_rename_name_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Description',
            field=models.CharField(default='', max_length=50000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='Date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='Title',
            field=models.CharField(max_length=500),
        ),
    ]
