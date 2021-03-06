# Generated by Django 3.2.14 on 2022-07-10 20:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bimmerreviewer', '0008_alter_comments_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='approve',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='review_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
