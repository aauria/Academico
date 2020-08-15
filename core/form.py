from django import forms
from .models import Docente

class Docenteform(forms.ModelForm):
    class Meta:
        model= Docente
        fields=[
            'nombre',
            'apellido',
            'edad',
            'email',
            'sexo',
            'cedula',
            'curso_asignado',
            'titulo_Profesion',
        ]
        labels={
            'nombre':'Nombre',
            'apellido':'Apellido',
            'edad':'Edad',
            'email':'Email',
            'sexo':'Sexo',
            'cedula':'Cedula',
            'curso_asignado':'Curso',
            'titulo_Profesion':'Profesión',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'table-active',}),
            'apellido':forms.TextInput(attrs={'class':'table-active'}),
            'edad':forms.TextInput(attrs={'class':'table-active'}),
            'email':forms.TextInput(attrs={'class':'table-active'}),
            'sexo':forms.Select(attrs={'class':'form-group'}),
            'cedula':forms.TextInput(attrs={'class':'table-active'}),
            'curso_asignado':forms.TextInput(attrs={'class':'table-active'}),
            'titulo_Profesion':forms.TextInput(attrs={'class':'table-active'}),
        }

