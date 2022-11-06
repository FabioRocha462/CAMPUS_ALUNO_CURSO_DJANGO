from django.db import models
from Professor.models import Professor
# Create your models here.
class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    professores = models.ManyToManyField(Professor)

    def __str__(self):
        return self.nome