# Generated by Django 5.0.2 on 2024-03-05 00:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tontine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='nom',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='prenom',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_journalier', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_adhesion', models.DateField(auto_now_add=True)),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_paiement', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_paiement', models.DateField(auto_now_add=True)),
                ('participation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tontine.participation')),
            ],
        ),
        migrations.CreateModel(
            name='Tontine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_tontine', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('montant_max', models.PositiveBigIntegerField()),
                ('effectifs_max', models.PositiveIntegerField()),
                ('duree_paiement', models.PositiveIntegerField(choices=[(1, 'Journalière'), (7, 'Hebdomadaire'), (30, 'Mensuelle')])),
                ('code_access', models.PositiveIntegerField(unique=True)),
                ('date_debut', models.DateField(auto_now_add=True)),
                ('gestionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tontines_gerees', to=settings.AUTH_USER_MODEL)),
                ('membres', models.ManyToManyField(related_name='tontines_participees', through='tontine.Participation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Retrait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_retrait', models.DateField(auto_now_add=True)),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tontine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tontine.tontine')),
            ],
        ),
        migrations.AddField(
            model_name='participation',
            name='tontine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tontine.tontine'),
        ),
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_depot', models.DateField(auto_now_add=True)),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tontine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tontine.tontine')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solde', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('membre', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together={('membre', 'tontine')},
        ),
    ]