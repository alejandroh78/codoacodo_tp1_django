from django.shortcuts import render

# Create your views here.

def home(request):
    ruta = request.path
    return render(request, "core/index.html",{'ruta': ruta})

def experiencia(request):
    ruta = request.path
    return render(request, "core/experiencia.html", {'ruta': ruta})

def clases(request):
    ruta = request.path
    return render(request, "core/clases.html",{'ruta': ruta})

'''def agenda(request):
    ruta = request.path
    return render(request, "core/agenda.html",{'ruta': ruta})
'''

def contacto(request):
    ruta = request.path
    return render(request, "core/contacto.html",{'ruta': ruta})
