# Generated by Django 5.0 on 2023-12-08 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumnoApellido', models.CharField(max_length=40)),
                ('alumnoNombre', models.CharField(max_length=40)),
                ('materia', models.CharField(max_length=40)),
                ('fechaAgendada', models.DateField()),
                ('HoraAgendada', models.TimeField()),
                ('cantidadHoras', models.IntegerField()),
                ('fechaAlta', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
