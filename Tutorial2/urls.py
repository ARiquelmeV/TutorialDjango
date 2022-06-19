"""TutorialDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    virtualenv -p python3 name

    Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
#from Aplicaciones.Academico.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # SE IMPORTA INCLUDE PARA PODER REDIRECCIONAR EL SIGUENTE PATH AL ARCHIVO Y LA URL QUE ESTA EN LA APP ACADEMICO
    path('', include('Aplicaciones.Academico.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




"""
Tutoriales
PRIMERA APP Y MIGRACIONES 17-18 
CRUD 19-23
PRIMERA VIEW e INSTALACION BOOTSTRAP  24-25
    TABLA Y BARRA DE NAVEGACION

CONSULTAS SQL CON FILTROS USANDO EL ORM 26

PANEL DE ADMINISTRACION DE DJANGO 27-28-29   
    CREACION SUPER USUARIO
    CRUD EN EL PANEL
    PERSONALIZACION DEL PANEL

VISTAS BASADAS EN MODELOS/CLASES 30   
PANEL DE ADMINISTRACION AVANZADO 31
RELACIONES FORANEAS & GESTION DE USUARIOS y GRUPOS 32-35
    CREACION TABLA DOCENTE
    GESTION DE PERMISOS Y AUTORIZACION
CRUD MEDIANTE ORM DE DJANGO 36-37
CONTROL DE EVENTOS MEDIANTE JAVASCRIPT 38-39

"""