from django import forms
from .models import Estudiante ,EstudianteMateriaDocente,EstudianteMateriaCurso

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
            'curso',

        ]
        labels={
            'nombre':'Nombre',
            'apellido':'Apellido',
            'edad':'Edad',
            'email':'Email',
            'sexo':'Sexo',
            'cedula':'Cedula',
            'curso':'Curso Asignado',

        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'table-active',}),
            'apellido':forms.TextInput(attrs={'class':'table-active'}),
            'edad':forms.TextInput(attrs={'class':'table-active'}),
            'email':forms.TextInput(attrs={'class':'table-active'}),
            'sexo':forms.Select(attrs={'class':'form-group'}),
            'cedula':forms.TextInput(attrs={'class':'table-active'}),
            'curso':forms.Select(attrs={'class':'table-active'}),
        }
class EstudianteMateriaDocenteform(forms.ModelForm):
        class Meta:
            model=EstudianteMateriaDocente
            fields=[
                'materia',
                'docente',
                'estudiante',
            ]
            labels={
                'materia':'MATERIA',
                'docente':'DOCENTE',
                'estudiante': 'ESTUDIANTE',
            }
            widgets={
                'materia':forms.Select(attrs={'class': 'form-control'}),
                'docente':forms.Select(attrs={'class': 'form-control'}),
                'estudiante': forms.Select(attrs={'class': 'form-control'}),
            }


class EstudianteMateriaCursoform(forms.ModelForm):
    class Meta:
        model = EstudianteMateriaCurso
        fields = [
            'materia',
            'estudiante',
            'curso',
        ]
        labels = {
            'materia': 'MATERIA',
            'estudiante': 'ESTUDIANTE',
            'curso': 'CURSO',
        }
        widgets = {
            'materia': forms.Select(attrs={'class': 'form-control'}),
            'estudiante': forms.Select(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
        }
