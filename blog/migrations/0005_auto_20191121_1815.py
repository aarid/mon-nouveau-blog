# Generated by Django 2.2.7 on 2019-11-21 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191114_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='joueurs',
        ),
        migrations.RemoveField(
            model_name='image',
            name='questions',
        ),
        migrations.RemoveField(
            model_name='question',
            name='reponses',
        ),
        migrations.DeleteModel(
            name='Avis',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Joueur',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Reponse',
        ),
    ]
