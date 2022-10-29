from django.urls import path
from .views import *


urlpatterns=[
    path('equipos/', equipos, name='equipos'),
    path('servicios/', servicios, name='servicio'),
    path('contacto/', contactos, name='contacto'),
    path('', inicio, name='inicio'),
    path('equiposFormulario/', equiposFormulario, name='equiposFormulario'),
    path('servicioFormulario/', serviciosFormulario, name='serviciosFormulario'),
    path('contactoFormulario/', contactoFormulario, name='contactoFormulario'),
    path('busquedaEquipos/', busquedaEquipos, name='busquedaEquipos'),
    path('busquedaServicio/', busquedaServicio, name='busquedaServicio'),
    path('busquedaContacto/', busquedaContacto, name='busquedaContacto'),
    path('busquedaEquipos/objetivo/', objetivo, name='objetivo'),
    path('busquedaServicio/problema/',problema, name='problema'),
    path('busquedamodelo/nombreYapellido/', nombreYapellido, name='nombreYapellido'),
]
