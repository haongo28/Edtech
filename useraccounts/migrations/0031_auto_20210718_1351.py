# Generated by Django 3.2.4 on 2021-07-18 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0030_blogdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetail',
            name='paragraph1',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='blogdetail',
            name='paragraph2',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='blogdetail',
            name='paragraph3',
            field=models.TextField(default=''),
        ),
    ]
