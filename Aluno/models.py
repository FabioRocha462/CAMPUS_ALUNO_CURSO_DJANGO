from django.db import models
from Campus.models import Campus
from Endereco.models import Endereco
# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    matricula = models.CharField(max_length=30)
    campus = models.ForeignKey(Campus, on_delete = models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete = models.CASCADE)

    def __str__(self):
        return self.nome