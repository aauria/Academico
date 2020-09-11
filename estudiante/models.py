from django.db import models
from core.models import Docente
from materia.models import Materia
from curso.models import Curso


# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=200,default='')
    apellido = models.CharField(max_length=200,default='')
    edad = models.CharField(max_length=100,default='')
    email= models.EmailField(max_length=200,default='')
    sexo = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=sexo, default='M')
    cedula=models.CharField(max_length=10,default='')
    curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return format(self.nombre,self.apellido)



class EstudianteMateriaDocente(models.Model):
    materia=models.ForeignKey(Materia,on_delete=models.CASCADE)
    estudiante=models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    docente=models.ForeignKey(Docente,on_delete=models.CASCADE)




