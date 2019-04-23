from django.contrib import admin
from .models import Formulario
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.admin import ImportExportActionModelAdmin


class FormularioResource(resources.ModelResource):
    class Meta:
        model = Formulario
        fields = ('rut', 'nombres', 'apellidos', 'nrofono', 'email', 'ciudad', 'colegio', 'colegioadv', 'carrera_post_1', 'carrera_post_2', )


class FormularioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = FormularioResource
    list_filter = ('ciudad', 'carrera_post_1', 'colegio', 'colegioadv',)
    list_display = ('rut', 'nombres', 'apellidos', 'nrofono', 'email', 'ciudad', 'colegio', 'colegioadv', 'carrera_post_1', 'carrera_post_2',)
    search_fields = ('rut', 'nombres', 'apellidos',)
    ordering = ('nombres',)



"""class FormularioAdmin(ImportExportActionModelAdmin):
    pass
    """

admin.site.register(Formulario, FormularioAdmin)
