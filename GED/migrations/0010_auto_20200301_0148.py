# Generated by Django 3.0.3 on 2020-03-01 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GED', '0009_auto_20200227_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='titre_fichier',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]