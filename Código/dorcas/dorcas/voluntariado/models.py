from django.db import models

from django.contrib.auth.models import User
# Create your models here.
from accounts.models import Instituicao

class Voluntario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    horario = models.IntegerField(null=True, blank=True)
    funcao= models.CharField(max_length=100, null=True, blank=True)
    qnt = models.IntegerField(null=True, blank=True)
    tempo = models.IntegerField(null=True, blank=True)
    idademin = models.IntegerField(null=True, blank=True)
    cidade = models.CharField(max_length=150, null=True, blank=True)
    rua = models.CharField(max_length=150, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    bairro = models.CharField(max_length=150, null=True, blank=True)
    telefone = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.titulo