# Generated by Django 3.2.4 on 2021-07-12 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0028_auto_20210711_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='video',
            name='likes',
        ),
        migrations.AddField(
            model_name='courses',
            name='makhoahoc',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='video',
            name='makhoahoc',
            field=models.CharField(default='', max_length=200),
        ),
    ]
