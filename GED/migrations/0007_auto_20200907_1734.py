# Generated by Django 3.0.3 on 2020-09-07 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GED', '0006_auto_20200907_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialprofile',
            name='network',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('twitter', 'Twitter'), ('google', 'Google'), ('linkedin', 'Linkedin'), ('instagram', 'Instagram')], max_length=100),
        ),
    ]
