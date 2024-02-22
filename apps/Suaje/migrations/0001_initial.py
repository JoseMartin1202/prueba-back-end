# Generated by Django 3.1.7 on 2023-10-15 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suaje',
            fields=[
                ('idSuaje', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('numero', models.IntegerField(unique=True)),
                ('ancho', models.DecimalField(decimal_places=2, max_digits=5)),
                ('alto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('margen', models.DecimalField(decimal_places=2, max_digits=5)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('numeroCortes', models.IntegerField()),
            ],
        ),
    ]