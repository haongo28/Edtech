# Generated by Django 3.2.4 on 2021-06-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0010_libcourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='degree',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='facebook',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
