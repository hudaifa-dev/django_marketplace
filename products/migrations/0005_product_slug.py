# Generated by Django 4.2.2 on 2023-06-08 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_sale_price_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug-field', verbose_name='Slug'),
        ),
    ]