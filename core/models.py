from django.db import models
from curso.models import Curso

# Create your models here.
class Docente(models.Model):
    nombre = models.CharField(max_length=200,default='')
    apellido = models.CharField(max_length=200,default='')
    edad = models.CharField(max_length=100,default='')
    email= models.EmailField(max_length=200,default='')
    sexo = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=sexo, default='M')
    titulo_Profesion= models.CharField(max_length=15,default='')
    cedula=models.CharField(max_length=10,default='')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)


class CursoDocente(models.Model):
    curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    Docente=models.ForeignKey(Docente,on_delete=models.CASCADE)
