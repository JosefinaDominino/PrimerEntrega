from django.http import HttpResponse
from django.shortcuts import render
from AppFinal.models import *
from AppFinal.forms import *

# Create your views here.

def inicio(request):
    return render(request, "AppFinal/inicio.html" )

def equipos(request):
    return render(request, "AppFinal/equipos.html" )

def servicios(request):
    return render(request, "AppFinal/servicios.html" )

def contactos(request):
    return render(request, "AppFinal/contacto.html" )



def equiposFormulario(request):

    if request.method== "POST":
        miFormulario=EquiposFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            equip=Equipos(objetivo=info['objetivo'], requerimientos=info['requerimientos'], cantidad=info['cantidad'])
            equip.save()
            return render(request, "AppFinal/equiposFormulario.html",{"mensaje":"Informacion Creada"})
        else:
             return render(request, "AppFinal/equiposFormulario.html",{"mensaje":"Error"})
    else:
        miFormulario= EquiposFormulario()
    return render(request, "AppFinal/equiposFormulario.html", {"formulario":miFormulario})            



def serviciosFormulario(request):

    if request.method== "POST":
        miFormulario=ServiciosFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            equip=Servicio(problema=info['problema'])
            equip.save()
            return render(request, "AppFinal/servicioFormulario.html",{"mensaje":"Informacion Creada"})
        else:
             return render(request, "AppFinal/servicioFormulario.html",{"mensaje":"Error"})
    else:
        miFormulario= ServiciosFormulario()
    return render(request, "AppFinal/servicioFormulario.html", {"formulario":miFormulario})        


def contactoFormulario(request):

    if request.method== "POST":
        miFormulario=ContactoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            equip=Contacto( nombreYapellido=info['nombreYapellido'], nombreIndustria=info['nombreIndustria'], email=info['email'], pais=info['pais'],mensaje=info['mensaje'])
            equip.save()
            return render(request, "AppFinal/contactoFormulario.html",{"mensaje":"Informacion Creada"})
        else:
             return render(request, "AppFinal/contactoFormulario.html",{"mensaje":"Error"})
    else:
        miFormulario= ContactoFormulario()
    return render(request, "AppFinal/contactoFormulario.html", {"formulario":miFormulario}) 





#busqueda equipos

def busquedaEquipos(request):
    return render(request, 'busquedaEquipos.html')
    
def objetivo(request):
    if request.GET.get("objetivo"):
        objetivo=request.GET["objetivo"]
        equiposs= Equipos.objects.filter(objetivo=objetivo)
        if len(equiposs)!= 0:
            return render(request, 'busquedaEquipos.html', {"equipos":equiposs})
        else:
            return render(request, 'busquedaEquipos.html', {"error":f'No hay pedido de "{objetivo}"'})
    else:
        return render(request, 'busquedaEquipos.html', {"error":f'No has ingresado ningún equipo'})

#busqueda servicio

def busquedaServicio(request):
    return render(request, 'busquedaServicio.html')
    
def problema(request):
    if request.GET.get("problema"):
        problema=request.GET.get("problema")
        problems= Servicio.objects.filter(problema=problema)
        if len(problems)!= 0:
            return render(request, 'busquedaServicio.html', {"problema":problema})
        else:
            return render(request, 'busquedaServicio.html', {"error":f'No hay problema "{problema}"'})
    else:
        return render(request, 'busquedaServicio.html', {"error":f'No has ingresado ningún problema'})

#busqueda contacto

def busquedaContacto(request):
    return render(request, 'busquedaContacto.html')
    
def nombreYapellido(request):
    if request.GET.get("nombreYapellido"):
        nombreYapellido=request.GET.get("nombreYapellido")
        noms = Contacto.objects.filter(nombreYapellido=nombreYapellido)
        if len(noms)!= 0:
            return render(request, 'busquedaContacto.html', {"nombreYapellido":nombreYapellido})
        else:
            return render(request, 'busquedaContacto.html', {"error":f'No hay nombre "{nombreYapellido}"'})
    else:
        return render(request, 'busquedaContacto.html', {"error":f'No has ingresado ningún nombre'})