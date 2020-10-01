from django.db import models
from curso.models import Curso

# Create your models here.
class Docente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.CharField(max_length=100)
    email= models.EmailField(max_length=200,unique=True)
    sexo = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=sexo, default='M')
    titulo_Profesion= models.CharField(max_length=15)
    cedula=models.CharField(max_length=10,unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        unique_together=["nombre","apellido"]

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)


class CursoDocente(models.Model):
    curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    Docente=models.ForeignKey(Docente,on_delete=models.CASCADE)
    class Meta:
        unique_together=["curso","Docente"]
