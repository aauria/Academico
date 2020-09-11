from django import forms
from .models import Notas

class NotaForm(forms.ModelForm):
        class Meta:
            model=Notas
            fields=[
                'Materia',
                'Estudiante',
                'Docente',
                'Curso',
                'nota1',
                'nota2',
                'nota3',
            ]
            labels={
                'Materia':'MATERIA:',
                'Estudiante':'ESTUDIANTE:',
                'Docente':'DOCENTE:',
                'Curso':'CURSO:',
                'nota1':'NOTA_1:',
                'nota2':'NOTA_2:',
                'nota3':'NOTA_3:',
            }
            widgets={
                'Materia': forms.Select(attrs={'class': 'form-control'}),
                'Estudiante': forms.Select(attrs={'class': 'form-control'}),
                'Docente': forms.Select(attrs={'class': 'form-control'}),
                'Curso': forms.Select(attrs={'class': 'form-control'}),
                'nota1': forms.TextInput(attrs={'class': 'form-control'}),
                'nota2': forms.TextInput(attrs={'class': 'form-control'}),
                'nota3': forms.TextInput(attrs={'class': 'form-control'}),
            }