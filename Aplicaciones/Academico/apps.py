from django.apps import AppConfig
"""
SE CREA LA APLICACION/MODULO ACADEMICO 

"""

class AcademicoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Arreglo en relacion al video, aqui nativamente solo aparece 'Academico' pero se cambia a 'Aplicaciones.Academico' para que funcione
    name = 'Aplicaciones.Academico'
