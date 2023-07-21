from datetime import datetime
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.

 
class Responsavel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    parentesco= models.CharField(max_length=100, null=True, blank=True)
    cpf = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=150, null=True, blank=True)
    rua = models.CharField(max_length=150, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    bairro = models.CharField(max_length=150, null=True, blank=True)
    telefone = models.CharField(max_length=150, null=True, blank=True)



