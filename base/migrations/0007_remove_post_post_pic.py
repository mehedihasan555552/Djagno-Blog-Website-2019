# Generated by Django 3.0.4 on 2020-04-11 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_post_post_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_pic',
        ),
    ]