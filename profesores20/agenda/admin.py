from django.contrib import admin
from .models import Agenda
# Register your models here.

class AgendaAdmin(admin.ModelAdmin):
    readonly_fields = ('fechaAlta','fechaModificacion')

admin.site.register(Agenda, AgendaAdmin)