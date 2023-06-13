# Generated by Django 4.2.2 on 2023-06-13 04:22

import django.core.files.storage
from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='media',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/hudaifasalih/PycharmProjects/django_marketplace/static_cdn/protected'), upload_to=products.models.download_media_location),
        ),
    ]
