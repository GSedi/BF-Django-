# Generated by Django 2.1.1 on 2018-10-11 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('due_on', models.DateTimeField(verbose_name='Due on')),
                ('mark', models.BooleanField(default=False, verbose_name='Mark')),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='TODO List')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='todo_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_list', to='main.TodoList'),
        ),
    ]
