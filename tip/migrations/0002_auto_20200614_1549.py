# Generated by Django 3.0.7 on 2020-06-14 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tip', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maketip',
            name='down_votes',
        ),
        migrations.RemoveField(
            model_name='maketip',
            name='info',
        ),
        migrations.RemoveField(
            model_name='maketip',
            name='likes',
        ),
    ]
