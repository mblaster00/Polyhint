# Generated by Django 3.0.3 on 2020-02-27 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GED', '0008_remove_document_uploader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.CharField(max_length=25),
        ),
    ]
