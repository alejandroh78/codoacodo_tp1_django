# Generated by Django 5.0 on 2023-12-08 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='fechaModificacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='HoraAgendada',
            field=models.TimeField(verbose_name='Hora Clase'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='alumnoApellido',
            field=models.CharField(max_length=40, verbose_name='Apellido Alumno'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='alumnoNombre',
            field=models.CharField(max_length=40, verbose_name='Nombre Alumno'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='cantidadHoras',
            field=models.IntegerField(verbose_name='Cantidad Horas'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='fechaAgendada',
            field=models.DateField(verbose_name='Fecha Clase'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='materia',
            field=models.CharField(max_length=40, verbose_name='Materia'),
        ),
    ]
