# Generated by Django 2.2.7 on 2019-11-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_lsd'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
