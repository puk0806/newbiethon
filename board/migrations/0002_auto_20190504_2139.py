# Generated by Django 2.2 on 2019-05-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aicohol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Donkey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='board',
        ),
    ]