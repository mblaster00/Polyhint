# Generated by Django 3.0.3 on 2020-09-08 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GED', '0008_auto_20200908_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='tache_time',
            field=models.DateTimeField(null=True),
        ),
    ]