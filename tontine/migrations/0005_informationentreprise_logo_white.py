# Generated by Django 5.0.2 on 2024-03-12 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tontine', '0004_informationentreprise'),
    ]

    operations = [
        migrations.AddField(
            model_name='informationentreprise',
            name='logo_white',
            field=models.ImageField(default='', upload_to='logo'),
            preserve_default=False,
        ),
    ]
