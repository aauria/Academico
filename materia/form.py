from django import forms
from .models import Materia

class Materiaform(forms.ModelForm):
    class Meta:
        model=Materia
        fields=[
            'nombre',
        ]
        labels={
            'nombre':'NOMBRE MATERIA'
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
        }