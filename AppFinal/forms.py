from django import forms

class EquiposFormulario(forms.Form):
    objetivo=forms.CharField(max_length=10000000)
    requerimientos=forms.CharField(max_length=10000000)
    cantidad=forms.IntegerField()

class ServiciosFormulario(forms.Form):
     problema=forms.CharField(max_length=800)

class ContactoFormulario(forms.Form):
     nombreYapellido=forms.CharField(max_length=80)
     nombreIndustria=forms.CharField(max_length=80)
     email=forms.EmailField(max_length=80)
     pais=forms.CharField(max_length=80)
     mensaje=forms.CharField(max_length=8000)
   