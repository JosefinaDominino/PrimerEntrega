from django.db import models

# Create your models here.

class Equipos(models.Model):
    objetivo=models.CharField(max_length=80)
    requerimientos=models.CharField(max_length=8000)
    cantidad=models.IntegerField()
    
    def __str__(self):
         return self.objetivo+" "+str(self.requerimientos)

class Servicio(models.Model):
    problema=models.CharField(max_length=800)

    def __str__(self):
         return self.problema

class Contacto(models.Model):
    nombreYapellido=models.CharField(max_length=80)
    nombreIndustria=models.CharField(max_length=80)
    email=models.EmailField(max_length=80)
    pais=models.CharField(max_length=80)
    mensaje=models.CharField(max_length=8000)
   
    def __str__(self):
         return self.nombreYapellido+" "+str(self.nombreIndustria)+" "+str(self.email)+" "+str(self.pais)+" "+str(self.mensaje)
