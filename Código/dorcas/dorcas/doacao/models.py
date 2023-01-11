from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Doacao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    descricao = models.TextField(max_length=100, null=True, blank=True)
    titulo = models.CharField(max_length=150, null=True, blank=True)
    

    def __str__(self):
        return self.titulo