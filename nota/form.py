from django import forms
from .models import Notas

class NotaForm(forms.ModelForm):
        class Meta:
            model=Notas
            fields=[
                'Curso',
                'Materia',
                'Docente',
                'Estudiante',
                'nota1',
                'nota2',
                'nota3',

            ]
            labels={
                'Curso': 'CURSO:',
                'Materia':'MATERIA:',
                'Docente':'DOCENTE:',
                'Estudiante': 'ESTUDIANTE:',
                'nota1':'NOTA_1:',
                'nota2':'NOTA_2:',
                'nota3':'NOTA_3:',
            }
            widgets={
                'Curso': forms.Select(attrs={'class': 'form-control'}),
                'Materia': forms.Select(attrs={'class': 'form-control'}),
                'Docente': forms.Select(attrs={'class': 'form-control'}),
                'Estudiante': forms.Select(attrs={'class': 'form-control'}),
                'nota1': forms.TextInput(attrs={'class': "row"}),
                'nota2': forms.TextInput(attrs={'class': "row"}),
                'nota3': forms.TextInput(attrs={'class': "row"}),
            }