from django.db import models

# Create your models here.

class Agenda(models.Model):
    alumnoApellido = models.CharField(max_length=40, verbose_name="Apellido Alumno")
    alumnoNombre = models.CharField(max_length=40, verbose_name="Nombre Alumno")
    materia = models.CharField(max_length=40, verbose_name="Materia")
    fechaAgendada = models.DateField(verbose_name="Fecha Clase")
    HoraAgendada = models.TimeField(verbose_name="Hora Clase")
    cantidadHoras = models.IntegerField(verbose_name="Cantidad Horas")
    fechaAlta = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.materia

class Meta:
    verbose_name = "Agenda"
    verbose_name_plural = "Agendas"
    ordering = "-fechaAlta"