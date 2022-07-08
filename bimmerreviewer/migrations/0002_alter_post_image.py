# Generated by Django 3.2.14 on 2022-07-08 01:38

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bimmerreviewer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, null=True, verbose_name='image'),
        ),
    ]
