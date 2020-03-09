# Generated by Django 3.0.3 on 2020-02-23 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GED', '0003_professeur_telephone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='comments',
        ),
        migrations.AddField(
            model_name='document',
            name='filiere',
            field=models.CharField(choices=[('GIT', 'GENIE INFORMATIQUE ET TELECOMMUNICATION'), ('GEM', 'GENIE ELECTRO-MÉCANIQUE'), ('GC', 'GÉNIE CIVIL'), ('AERO', 'GÉNIE AÉRONAUTIQUE'), ('TC', 'TRONC-COMMUN')], default='TC', max_length=50),
        ),
        migrations.AddField(
            model_name='document',
            name='niveau',
            field=models.CharField(choices=[('TC1', 'TC1'), ('TC2', 'TC2'), ('DIC1', 'DIC1'), ('DIC2', 'DIC2'), ('DIC3', 'DIC3')], default='TC', max_length=50),
        ),
        migrations.AlterField(
            model_name='document',
            name='fichier',
            field=models.FileField(default='GED/docs_prof/readme.txt', upload_to='GED/docs_prof/'),
        ),
    ]