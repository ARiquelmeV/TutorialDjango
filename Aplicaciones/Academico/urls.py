"""
ARCHIVO CREADO MANUALMENTE, COMO BUENA PRACTICA SE RECOMIENDA CREAR UN URLS.PY POR CADA APLICACION QUE
SE AÑADA AL PROYECTO
"""
from django.urls import URLPattern, path
from Aplicaciones.Academico.views import CursoListView, eliminar_curso, registrar_curso, editar_curso, edicion_Curso, registrar_docente, inicio, CrearCurso, editar_docente

urlpatterns = [
    # SE PASA LA CLASE CURSOLISTVIEW COMO VISTA CON LA FUNCION .AS_VIEW()
    path('', inicio),
    path('ListadoCursos/', CursoListView.as_view(), name='gestion_cursos'),
    path('ListadoCursos/eliminacionCurso/<int:id>', eliminar_curso),
    path('ListadoCursos/edicionCurso/<int:id>', edicion_Curso),
    path('CrearCurso/', CrearCurso.as_view(), name='crear_cursos'),
    path('registrarCurso/', registrar_curso),
    path('registrarDocente/', registrar_docente),
    path('editarCurso/', editar_curso),
    path('editarDocente/', editar_docente),
]