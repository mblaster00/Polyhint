# Generated by Django 3.0.3 on 2020-09-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GED', '0012_auto_20200908_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='tache_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
