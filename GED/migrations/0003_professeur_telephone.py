# Generated by Django 3.0.3 on 2020-02-23 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GED', '0002_auto_20200223_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='professeur',
            name='telephone',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
