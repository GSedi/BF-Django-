# Generated by Django 2.1.1 on 2018-10-11 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Created'),
        ),
    ]
