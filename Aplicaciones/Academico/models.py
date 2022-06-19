from random import choices
from django.db import models
from django.utils.html import format_html
from .choices import generos

# Create your models here.

class Docente(models.Model):
    # verbose_name sirve para que el atributo aparezca de una determinada forma en el panel de admin
    apellido_paterno = models.CharField(max_length=20, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=20, verbose_name='Apellido Materno')
    nombres = models.CharField(max_length=20, verbose_name='Nombres')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Naciminto')
    genero = models.CharField(max_length=1, choices=generos, default='F')

    # Para mostrar el nombre completo en el panel
    def nombre_completo(self):
        return "{} {} {}".format(self.nombres, self.apellido_paterno, self.apellido_materno)

    
    # Retorna el nombre completo
    # PARA HACER UN POST SE DEBE CONSIDERAR EL ID DEL DOCENTE, NO SE CONSIDERA LO A CONTINUACIONS
    def __str__ (self):
        return self.nombre_completo()

    # Personalizar los metadatos en singular y plural, luego se indica el nombre de la tabla y como se indica 
    class Meta:
        verbose_name='Docente'
        verbose_name_plural='Docentes'
        db_table='docente'
        ordering= ['apellido_paterno','-apellido_materno']        

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    # MODIFICACION DE LA CLASE CURSO, LA RELACION ES HACIA EL MODELO DOCENTE, YA QUE UN CURSO DEPENDE DE UN DOCENTE
    docente = models.ForeignKey(Docente, null=True, blank=True, on_delete=models.CASCADE)
    # LA SIGUENTE FUNCION ES UNA REESCRITURA PARA EL PANEL DE ADMINISTRACION DE DJANGO
    
    def __str__(self):
        texto="{0} - ({1})"
        return texto.format(self.nombre,self.creditos)

    def coloreado(self):
        if self.creditos >= 4:
            return format_html('<span style="color:blue;">{0}</span>'.format(self.nombre))
        else:
            return format_html('<span style="color:red;">{0}</span>'.format(self.nombre))    


"""
>>>>ACCIONES CRUD CON SHELL, SQLITE<<<<
# Primero, se abre el shell de python, estando en el entorno virtual y luego en el mismo entorno que el manage.py
python manage.py shell
# Se importa el modelo
from Aplicaciones.Academico.models import Curso

>>> Insercion de registros en los modelos, hasta ahora (CREATE) <<<
# Para insertar, se crea una variable con los datos del modelo
cur1 = Curso(nombre = 'Programación Avanzada', creditos = 5)
# Luego se guarda en la base de datos con .save()
cur1.save()

cur2 = Curso(nombre = 'Teoría de bases de datos', creditos = 4)
cur2.save()

Alternativamente se puede hacer esto en una sola sentencia
cur3 = Curso.objects.create(nombre = 'Redes y conectividad', creditos = 5)

>>> Modificacion de regitros, hasta ahora (UPDATE) <<<
# Para corregir un campo que se haya creado en la misma sesion de shell
cur4 = Curso.objects.create(nombre = 'Sistemas Operativos', creditos = 3)  
# Se accede al campo que queremos modificar, se modifica
cur4.creditos = 5
# Y se guarda
cur4.save()

# Si estamos en otra sesion, creamos un objeto y le asinamos el id del objeto que queremos modificar
cur = Curso.objects.get(id=2)
# Luego le asignamos el registro que queremos cambiar, lo modificamos
cur.creditos = 6
# Y se guarda
cur.save()

>>> Lectura de registros de base de datos (READ) <<<
# Se asigna a una variable todos los registros de la clase con .all()
cursos = Curso.objects.all()
# Print para observar los registros
print(cursos)
# Se devuelve una lista tipo QuerySet
<QuerySet [<Curso: Curso object (1)>, <Curso: Curso object (2)>, <Curso: Curso object (3)>, <Curso: Curso object (4)>]>
# Print para ver el objeto que tenemos
print(cursos[2]) 
Curso object (3)
# Estando el el objeto que queremos, accedemos al campo nombre para ver que curso es
print(cursos[2].nombre) 
Redes y conectividad

>>> Eliminacion de registros (DELETE) <<<
# Se crea un objeto y se le asigna el id del curso a borrar
cursoEliminar = Curso.objects.get(id=3)
# Print para aseguranos que estamos en el registro que queremos eliminar
print(cursoEliminar.nombre)
Redes y conectividad
# Se utiliza el comando .delete() para eliminar el objeto
cursoEliminar.delete()
# Finalmente aparece el registro eliminado
(1, {'Academico.Curso': 1})

- - - - - - - - - - - - - - - - - - - - - - -
CLAVES FORANEAS



"""