from django.shortcuts import render
from .models import Agenda
# Create your views here.

def agenda(request):
    ruta = request.path
    agendas = Agenda.objects.all()

    return render(request, "agenda/agenda.html",{'ruta': ruta, 'agendas': agendas})