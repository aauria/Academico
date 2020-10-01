from django.db import models
from materia.models import Materia
from estudiante.models import Estudiante
from core.models import Docente
from curso.models import Curso

# Create your models here.
class Notas(models.Model):
    Materia=models.ForeignKey(Materia,on_delete=models.CASCADE)
    Estudiante=models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    Docente=models.ForeignKey(Docente,on_delete=models.CASCADE)
    Curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    nota1 = models.FloatField(default=0)
    nota2 = models.FloatField(default=0)
    nota3 = models.FloatField(default=0)
    class Meta:
        unique_together=["Materia","Estudiante","Docente","Curso"]

    def promedio(self):
        resultado=((self.nota1+self.nota2+self.nota3)/3)
        return round(resultado,1)

