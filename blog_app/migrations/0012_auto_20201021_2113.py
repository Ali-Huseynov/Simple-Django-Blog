# Generated by Django 3.1 on 2020-10-21 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0011_auto_20201021_1648'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-date_time']},
        ),
    ]
