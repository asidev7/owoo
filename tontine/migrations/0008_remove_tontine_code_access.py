# Generated by Django 5.0.2 on 2024-03-13 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tontine', '0007_alter_tontine_membres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tontine',
            name='code_access',
        ),
    ]