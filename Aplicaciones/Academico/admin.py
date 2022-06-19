from django.contrib import admin
from .models import Curso, Docente
# Register your models here.
"""
AQUI SE IMPORTAN/REGISTRAN LOS MODELOS PARA QUE PUEDAN APARECER EN EL PANEL DE ADMINISTRACION DE DJANGO
PARA PODER REGISTRAR UNA CLASE/MODELO SE DEBE IMPORTAR PRIMERO
"""
# PRIMERO SE REGISTRA
#admin.site.register(Curso)  
@admin.register(Curso)
# LUEGO SE PUEDE CUSTOMIZAR LA SALIDA
class CursoAdmin(admin.ModelAdmin):
    ordering=('id',)
    list_display = ('coloreado','creditos')
    search_fields = ('nombre', 'creditos')
    #list_display_links = ('nombre',)
    #list_filter = ('creditos',)
    #list_per_page = 3
    #exclude = ('creditos',)
    """
    # CONJUNTO DE TUPLAS QUE SE OBSERVAN EN OPCIONES AVANZADAS DENTRO DEL FORMULARIO DE EDICION DEL PANEL
    fieldsets = (
        (None, {
            'fields':('nombre',)
        }),
        ('Advanced options',{
            'classes':('collapse','wide','extrapretty'),
            'fields': ('creditos',)
        })
    )
    """
    # SE CAMBIA A MAYUSCULAS EL NOMBRE DE LOS CURSOS
    def datos(self, obj):
        return obj.nombre.upper()
    # SE PERSONALIZA EL NOMBRE DE LA COLUMNA    
    datos.short_description = "CURSO (MAYUS)"
    datos.admin_order_field = 'nombre'

admin.site.register(Docente)