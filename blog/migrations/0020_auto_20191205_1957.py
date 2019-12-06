# Generated by Django 2.2.7 on 2019-12-05 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20191205_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concerner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Question')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='questions',
            field=models.ManyToManyField(through='blog.Concerner', to='blog.Question'),
        ),
    ]