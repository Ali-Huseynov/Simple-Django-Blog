# Generated by Django 3.1 on 2020-10-21 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_auto_20201021_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='blog_app.post'),
        ),
    ]
