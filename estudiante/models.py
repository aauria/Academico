from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=200,default='')
    apellido = models.CharField(max_length=200,default='')
    edad = models.CharField(max_length=100,default='')
    email= models.EmailField(max_length=200,default='')
    sexo = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=sexo, default='M')
    cedula=models.CharField(max_length=10,default='')
    curso_asignado=models.CharField(max_length=15,default='')
    materias=models.CharField(max_length=200,default='')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)