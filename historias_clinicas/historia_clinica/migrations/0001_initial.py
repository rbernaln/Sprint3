# Generated by Django 4.1.6 on 2023-05-04 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MedicoAuditado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=100)),
                ('usuario_creacion', models.CharField(max_length=100)),
                ('usuario_modificacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=100)),
                ('apellido', models.CharField(default='', max_length=100)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('dni', models.CharField(max_length=20)),
                ('obra_social', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PacienteAuditado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('dni', models.CharField(max_length=20)),
                ('obra_social', models.CharField(max_length=100)),
                ('usuario_creacion', models.CharField(max_length=100)),
                ('usuario_modificacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaClinicaAuditada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('descripcion', models.TextField()),
                ('usuario_creacion', models.CharField(max_length=100)),
                ('usuario_modificacion', models.CharField(max_length=100)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='historia_clinica.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='historia_clinica.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('descripcion', models.TextField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='historia_clinica.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='historia_clinica.paciente')),
            ],
        ),
    ]