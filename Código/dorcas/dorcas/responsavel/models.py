from datetime import datetime
from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Responsavel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    idade = models.DateTimeField(auto_now_add= False, auto_now=False, blank=True, null= True)
    parentesco= models.CharField(max_length=100, null=True, blank=True)
    cpf = models.IntegerField(null=True, blank=True)
    cidade = models.CharField(max_length=150, null=True, blank=True)
    rua = models.CharField(max_length=150, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    bairro = models.CharField(max_length=150, null=True, blank=True)
    telefone = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.nome

class M(models.Model):
    birth_date = models.DateField()
    #other fields

    def get_age(self):
        age = datetime.date.today()-self.birth_date
        return int((age).days/365.25)