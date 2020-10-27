# Generated by Django 3.1 on 2020-10-10 16:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0005_auto_20201009_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='unlikes',
            field=models.ManyToManyField(related_name='unlike_post', to=settings.AUTH_USER_MODEL),
        ),
    ]