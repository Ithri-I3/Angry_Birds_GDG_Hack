# Generated by Django 4.2.7 on 2024-01-19 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_name_departement_nom_dprt_medecin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_patient', models.CharField(max_length=50)),
                ('prenom_patient', models.CharField(max_length=50)),
                ('Adresse', models.CharField(max_length=50)),
                ('num_tel', models.FloatField(max_length=10)),
                ('date_naissance', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dossier_Medical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Traitement_medical', models.CharField(max_length=1000)),
                ('prescriptions', models.CharField(max_length=50)),
                ('Dpt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.departement')),
                ('pastien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.patient')),
            ],
        ),
    ]
