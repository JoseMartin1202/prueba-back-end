# Generated by Django 3.1.7 on 2024-03-05 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tarea', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='completada',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tarea',
            name='titulo',
            field=models.CharField(default='nueva tarea', max_length=200),
        ),
    ]