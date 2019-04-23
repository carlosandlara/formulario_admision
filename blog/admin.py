from django.contrib import admin
from .models import Formulario
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.admin import ImportExportActionModelAdmin


class FormularioAdmin(admin.ModelAdmin):
    list_filter = ('ciudad','carrera_post_1', 'colegio', 'colegioadv', )
    list_display = ('rut', 'nombres', 'apellidos', 'nrofono', 'email', 'ciudad', 'colegio', 'colegioadv', 'carrera_post_1', 'carrera_post_2', )
    search_fields = ('rut', 'nombres', 'apellidos',)
    ordering = ('nombres', )


class FormularioResource(resources.ModelResource):
    full_title = Field()

    class Meta:
        model = Formulario
        import_id_fields = ('rut',)
        fields = ('rut', 'nombres', 'apellidos', 'nrofono', 'email', 'ciudad', 'colegio', 'colegioadv', 'carrera_post_1', 'carrera_post_2',)


class FormularioAdmin(ImportExportModelAdmin):
    resource_class = FormularioResource


class FormularioAdmin(ImportExportActionModelAdmin):
    pass


admin.site.register(Formulario, FormularioAdmin)
