# Generated by Django 2.0.1 on 2018-01-13 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('periods', '0002_perioddef_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perioddef',
            old_name='created_at',
            new_name='create_time',
        ),
    ]
