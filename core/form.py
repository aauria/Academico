from django import forms
from .models import Docente,CursoDocente

class Docenteform(forms.ModelForm):
    class Meta:
        model= Docente
        fields=[
            'nombre',
            'apellido',
            'edad',
            'email',
            'sexo',
            'titulo_Profesion',
            'cedula',
        ]
        labels={
            'nombre':'Nombre',
            'apellido':'Apellido',
            'edad':'Edad',
            'email':'Email',
            'sexo':'Sexo',
            'titulo_Profesion':'Profesión',
            'cedula': 'Cedula',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'table-active',}),
            'apellido':forms.TextInput(attrs={'class':'table-active'}),
            'edad':forms.TextInput(attrs={'class':'table-active'}),
            'email':forms.TextInput(attrs={'class':'table-active'}),
            'sexo':forms.Select(attrs={'class':'form-group'}),
            'titulo_Profesion':forms.TextInput(attrs={'class':'table-active'}),
            'cedula': forms.TextInput(attrs={'class': 'table-active'}),
        }

class CursoDocenteForm(forms.ModelForm):
        class Meta:
            model =CursoDocente
            fields=[
                'curso',
                'Docente',
            ]
            labels={
                'curso':'CURSO:',
                'Docente':'DOCENTE:',
            }
            widgets={
                'curso': forms.Select(attrs={'class': 'form-control'}),
                'Docente': forms.Select(attrs={'class': 'form-control'}),
            }