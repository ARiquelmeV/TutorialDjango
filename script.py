"""
Pruena para poblar database en django, ya se incluyo Algebra y calculo I, para el resto
se llena un Script para shell que llena la base de datos de manera mas eficiente
Valida para la class Curso, con atributos nombre = String, y creditos = smallint
Correr este script dentro del entorno virtual

echo 'import script.py' | python manage.py shell
"""
import os
os.environ.setdefault("DJANGO_SETTING_MODULE", "TutorialDjango.settings")
from Aplicaciones.Academico.models import Curso

cur = Curso(nombre = "Álgebra I", creditos = 8)
cur.save()
cur = Curso(nombre = "Cálculo I", creditos = 8)
cur.save()
cur = Curso(nombre = "Computación I", creditos =  7)
cur.save()
cur = Curso(nombre = "Introducción a la Ingeniería en Ciencia de la Computación", creditos = 4)
cur.save()
cur = Curso(nombre = "Inglés I", creditos = 3)
cur.save()
cur = Curso(nombre = "Álgebra II", creditos = 8)
cur.save()
cur = Curso(nombre = "Cálculo II", creditos = 8)
cur.save()
cur = Curso(nombre = "Estructuras de Datos", creditos = 8)
cur.save()
cur = Curso(nombre = "Español I", creditos = 8)
cur.save()
cur = Curso(nombre = "Inglés II", creditos = 3)
cur.save()
cur = Curso(nombre = "Algebra Lineal", creditos = 7)
cur.save()
cur = Curso(nombre = "Cálculo III", creditos = 7)
cur.save()
cur = Curso(nombre = "Introducción a la Física", creditos = 6)
cur.save()
cur = Curso(nombre = "Paradigmas de Programación", creditos = 7)
cur.save()
cur = Curso(nombre = "Inglés III", creditos = 3)
cur.save()