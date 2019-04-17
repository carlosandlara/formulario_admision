from django.contrib import admin
from .models import Formulario


class FormularioAdmin(admin.ModelAdmin):
    list_filter = ('ciudad','carrera_post_1', 'colegio', 'colegioadv', )
    list_display = ('rut', 'nombres', 'apellidos', 'nrofono', 'email', 'ciudad', 'colegio', 'colegioadv', 'carrera_post_1', 'carrera_post_2', )
    search_fields = ('rut', 'nombres', 'apellidos',)
    ordering = ('nombres', )

admin.site.register(Formulario, FormularioAdmin)
