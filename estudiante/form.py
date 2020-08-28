from django import forms
from .models import Estudiante

class Estudianteform(forms.ModelForm):
    class Meta:
        model= Estudiante
        fields=[
            'nombre',
            'apellido',
            'edad',
            'email',
            'sexo',
            'cedula',
            'curso_asignado',
            'materias',
        ]
        labels={
            'nombre':'Nombre',
            'apellido':'Apellido',
            'edad':'Edad',
            'email':'Email',
            'sexo':'Sexo',
            'cedula':'Cedula',
            'curso_asignado':'Curso',
            'materias':'Materias_Asignadas',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'table-active',}),
            'apellido':forms.TextInput(attrs={'class':'table-active'}),
            'edad':forms.TextInput(attrs={'class':'table-active'}),
            'email':forms.TextInput(attrs={'class':'table-active'}),
            'sexo':forms.Select(attrs={'class':'form-group'}),
            'cedula':forms.TextInput(attrs={'class':'table-active'}),
            'curso_asignado':forms.TextInput(attrs={'class':'table-active'}),
            'materias':forms.TextInput(attrs={'class':'table-active'}),
        }