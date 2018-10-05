# Generated by Django 2.1.1 on 2018-10-05 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content')),
                ('rating', models.FloatField(verbose_name='Rating')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('nickname', models.CharField(max_length=50, verbose_name='Nickname')),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Adress')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.User')),
                ('rating', models.FloatField(verbose_name='Rating')),
            ],
            bases=('main.user',),
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.User')),
                ('authors', models.ManyToManyField(to='main.Author', verbose_name='authors')),
            ],
            bases=('main.user',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('text_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Text')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('date_published', models.DateTimeField(auto_now=True, verbose_name='Date Published')),
            ],
            bases=('main.text',),
        ),
        migrations.AddField(
            model_name='text',
            name='author',
            field=models.ManyToManyField(to='main.Author', verbose_name='authors'),
        ),
    ]