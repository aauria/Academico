from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
        class Meta:
            model=Curso
            fields=[
                'nivel',
                'paralelo'
            ]
            labels={
                'nivel':'NIVEL',
                'paralelo':'PARALELO'
            }
            widgets={
                'nivel':forms.TextInput(attrs={'class': 'form-control'}),
                'paralelo':forms.TextInput(attrs={'class': 'form-control'}),
            }