# Generated by Django 2.0.1 on 2018-01-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0009_planchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='planchange',
            name='change_reason',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]