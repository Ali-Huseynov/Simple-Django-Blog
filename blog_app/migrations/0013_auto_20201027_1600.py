# Generated by Django 3.1 on 2020-10-27 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0012_auto_20201021_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog_app.post'),
        ),
    ]
