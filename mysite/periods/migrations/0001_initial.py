# Generated by Django 2.0.1 on 2018-01-13 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodDef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('period_type', models.CharField(choices=[('Y', 'Year'), ('M', 'Month'), ('W', 'Week'), ('D', 'Day')], max_length=1)),
            ],
        ),
    ]
