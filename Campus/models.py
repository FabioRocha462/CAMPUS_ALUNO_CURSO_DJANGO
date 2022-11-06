from django.db import models
from Curso.models import Curso
# Create your models here.

class Campus(models.Model):
    nome = models.CharField(max_length = 255)
    cursos = models.ManyToManyField(Curso)


    def __str__(self):
        return self.nome