# Generated by Django 2.0.1 on 2018-01-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0006_plan_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='finished_at',
            field=models.DateTimeField(null=True),
        ),
    ]
