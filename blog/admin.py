from django.contrib import admin
from .models import Post, Formulario

admin.site.register(Post)


class FormularioAdmin(admin.ModelAdmin):
    list_filter = ('ciudad','carrera_post_1',)
    list_display = ('rut', 'nombres', 'ciudad', 'colegio',)


admin.site.register(Formulario, FormularioAdmin)
