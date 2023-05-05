from django.db import models
from responsavel.models import Responsavel
# Create your models here.
#from noti.models import  Tabela_notis
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models.signals import post_save, post_delete

import os

class Tabela(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, null=True,  related_name='donodoperfil')
    notificacao = models.ForeignKey('noti.Notificacao', on_delete=models.CASCADE, null=True,  related_name='donodoperfil')
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    nota = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)], null=True, blank=True)
    descricao = models.TextField(max_length=1000, null=True, blank=True)


#class Tabela_notis(models.Model):
 #  NOTI = ((1, 'Like'), (2, 'Volu'))
  # notificacao = models.ForeignKey('noti.Notificacao', on_delete=models.CASCADE, blank=True, null=True,  related_name='socorro')
   #sender = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='deusemais')
   #user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='queromorrer')
   #data = models.DateTimeField(auto_now_add=True)
   #noti = models.IntegerField(choices=NOTI, blank=True, null=True)

#class Aceitar(models.Model):
 #   user = models.ForeignKey(User, on_delete=models.CASCADE)
  #  notificacao = models.ForeignKey(Tabela_notis, on_delete=models.CASCADE)
     
   # def avisarCurtir(sender, instance, *args, **kwargs):
    #    favori = instance
     #   notificacao = favori.notificacao
      #  sender = favori.user
       # noti = Tabela_notis(notificacao=notificacao, sender=sender, user=notificacao.sender, noti=2)
        #noti.save()

#post_save.connect(Aceitar.avisarCurtir, sender=Aceitar)