# Generated by Django 2.0.1 on 2018-01-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0004_auto_20180109_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='progress',
            field=models.IntegerField(default=0),
        ),
    ]
