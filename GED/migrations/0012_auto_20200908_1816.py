# Generated by Django 3.0.3 on 2020-09-08 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GED', '0011_auto_20200908_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='tache_time',
            field=models.DateField(default=datetime.date(2020, 9, 8)),
        ),
    ]
