from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
admin.site.register(Equipos)
admin.site.register(Servicio)
admin.site.register(Contacto)
