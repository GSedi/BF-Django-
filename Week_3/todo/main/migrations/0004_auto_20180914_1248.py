# Generated by Django 2.1.1 on 2018-09-14 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180914_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_owner',
            field=models.CharField(max_length=200),
        ),
    ]
