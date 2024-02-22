# Generated by Django 3.1.7 on 2024-02-11 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Terminado',
            fields=[
                ('idTerminado', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipoTrabajo', models.CharField(choices=[('Etiquetas', 'Etiquetas'), ('Notas', 'Notas')], default='Etiquetas', max_length=20)),
            ],
        ),
    ]
