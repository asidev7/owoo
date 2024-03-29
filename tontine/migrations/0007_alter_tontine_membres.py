# Generated by Django 5.0.2 on 2024-03-13 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tontine', '0006_membre_alter_depot_membre_alter_participation_membre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tontine',
            name='membres',
            field=models.ManyToManyField(blank=True, related_name='tontines_participees', through='tontine.Participation', to='tontine.membre'),
        ),
    ]
