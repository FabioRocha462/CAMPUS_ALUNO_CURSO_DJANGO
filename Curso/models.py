from django.db import models
from Disciplina.models import Disciplina


# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=255)
    disciplinas = models.ManyToManyField(Disciplina)
    alunos = models.ManyToManyField('Aluno.Aluno', blank=True)

    def __str__(self):
        return self.nome