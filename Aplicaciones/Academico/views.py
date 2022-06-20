from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso, Docente
from django.views.generic import ListView


# Create your views here.
"""
def home(request):
    #cursosListados = Curso.objects.all().order_by('-nombre')|('nombre')|('creditos', 'nombre')
    #cursosListados = Curso.objects.all()[:5]|[4:9]|
    #cursosListados = Curso.objects.filter
    #cursosListados = Curso.objects.filter|(creditos=3)(creditos__lte=7)|(creditos__gte=4)|(nombre__startswith='C')
    #return HttpResponse("<h1> Hola Mundo! </h1>")
    cursosListados = Curso.objects.all()
    #return render(request, "gestionCursos.html", {"cursos": cursosListados})
    # Otra forma de realizarlo, previamente definiendo un diccionario
    # Diccionario
    data={
        'titulo':'Gestion de Cursos',
        'cursos': cursosListados
    }
    return render(request, "gestionCursos.html", data)
"""
# Inicio
def inicio(request):
    # REDIRECT REDIRECCIONA HACIA LA RUTA RAIZ
    data = {
        'titulo':'Inicio',
    }
    return render(request, "inicio.html", data)


# VISTA DONDE SE AÑADEN CURSOS Y/O DOCENTES
class CrearCurso(ListView):
    model = Docente
    template_name =  "CrearCurso.html"

    # POR DEFECTO ESTO RETORNA CURSO.OBJECTS.ALL PERO SE PUEDEN UTILIZAR FILTROS IGUAL QUE EN LA VIEW HOME
    def get_queryset(self):
        return Docente.objects.all()
        #return Curso.objects.filter(creditos__lte=5)

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        #print(context)
        context['titulo'] = 'Creación de Curso'
        return context  

# Vista basada en clases/modelos
class CursoListView(ListView):
    model = Curso
    template_name =  "ListarCurso.html"

    # POR DEFECTO ESTO RETORNA CURSO.OBJECTS.ALL PERO SE PUEDEN UTILIZAR FILTROS IGUAL QUE EN LA VIEW HOME
    def get_queryset(self):
        return Curso.objects.all()
        #return Curso.objects.filter(creditos__lte=5)

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        #print(context)
        context['titulo'] = 'Listado de Cursos'
        return context


def eliminar_curso(request,id):
    curso=Curso.objects.get(id=id)
    curso.delete()
    # REDIRECT REDIRECCIONA HACIA LA RUTA RAIZ
    return redirect('/ListadoCursos')

def registrar_curso(request):
    # AQUI VAMOS A OBTENER LOS DATOS QUE SE INGRESEN EN LA PAGINA CON EL METODO POST
    # txtNombre es el nombre de variable que esta en gestionCursos.html
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    docente = Docente.objects.get(id=request.POST['numDocente'])
    curso = Curso.objects.create(nombre=nombre, creditos=creditos, docente = docente)
    """
    NECESITAMOS AUTENTICARNOS PARA EVITAR EL PROBLEMA CON CSRF
    """
    return redirect('/ListadoCursos')

# Edicion curso lleva a la pagina de ediciion con el dicionario
def edicion_Curso(request, id):
    curso = Curso.objects.get(id=id)
    docente = Docente.objects.all()
    data = {
        'titulo':'Edición de Curso',
        'curso': curso,
        'docente': docente
    }
    return render(request, "edicionCurso.html", data)

# Editar curso es la funcion que agrega a la base de datos
def editar_curso(request):
    id = int(request.POST['id'])
    idocente = int(request.POST['numDocente'])
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    curso = Curso.objects.get(id=id)
    docente = Docente.objects.get(id=idocente)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.docente = docente
    curso.save()

    return redirect('/ListadoCursos')
    """
    Aqui en views, lo mas importante es mandar al template lo que se requeria filtrado y ordenado,
    esto se puede gracias a los ejemplos de filtros en la documentacion oficial de Django
    Esto funciona gracias al ORM de Django, estas hacen sentencias SQL.

    """
def editar_docente(request): 
    idocente = int(request.POST['idocente'])
    docente = Docente.objects.get(id=idocente)
    nombres = request.POST['txtNombres']
    apellido_paterno = request.POST['txtAPPA']
    apellido_materno = request.POST['txtAPMA']
    fecha_nacimiento = request.POST['txtFECH']
    genero = request.POST['txtGEN']
    docente.nombres = nombres
    docente.apellido_paterno = apellido_paterno 
    docente.apellido_materno = apellido_materno 
    docente.fecha_nacimiento = fecha_nacimiento  
    docente.genero = genero
    docente.save()
    return redirect('/ListadoCursos')   

def registrar_docente(request):
    # AQUI VAMOS A OBTENER LOS DATOS QUE SE INGRESEN EN LA PAGINA GESTION DOCENTE CON EL METODO POST
    nombres = request.POST['txtNombres']
    apellido_paterno = request.POST['txtAPPA']
    apellido_materno = request.POST['txtAPMA']
    fecha_nacimiento = request.POST['txtFECH']
    genero = request.POST['txtGEN']
    docente = Docente.objects.create(nombres = nombres, apellido_paterno = apellido_paterno, apellido_materno = apellido_materno,
    fecha_nacimiento = fecha_nacimiento, genero = genero)
    return redirect('/CrearCurso')
