# Generated by Django 2.2.7 on 2019-11-21 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_lsd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='lsd',
        ),
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
    ]
