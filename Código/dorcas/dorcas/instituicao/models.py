from django.db import models
from responsavel.models import Responsavel
# Create your models here.
from noti.models import  Tabela_notis
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save

import os

class Tabela(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, null=True,  related_name='donodoperfil')
    notificacao = models.ForeignKey('noti.Notification', on_delete=models.CASCADE, null=True,  related_name='donodoperfil')
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    nota = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)], null=True, blank=True)
    descricao = models.TextField(max_length=1000, null=True, blank=True)



# model referente ao perfil de usuario simples
#class Instituicao(models.Model):

#    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
 #   nome = models.CharField(max_length=100, null=True, blank=True)
  #  telefone = models.CharField(max_length=20, null=True, blank=True)
   # categoria = models.CharField(max_length=100, null=True, blank=True)
    #cnpj = models.CharField(max_length=20, null=True, blank=True)
   # cidade = models.CharField(max_length=150, null=True, blank=True)
    #estado = models.CharField(max_length=150, null=True, blank=True)
    #rua = models.CharField(max_length=150, null=True, blank=True)
    #numero = models.CharField(max_length=10, null=True, blank=True)
   # bairro = models.CharField(max_length=150, null=True, blank=True)
   # cpf = models.IntegerField(null=True, blank=True)
  #  picture = models.ImageField(upload_to=user_directory_path_profile, blank=True, null=True, verbose_name='Picture')
    
   # responsavel = models.ForeignKey(Responsavel,  on_delete=models.CASCADE, blank=True, null=True)
   
    #def save(self, *args, **kwargs):
     #   super().save(*args, **kwargs)
      #  SIZE = 250, 250

       # if self.picture:
        #    pic = Image.open(self.picture.path)
         #   pic.thumbnail(SIZE, Image.LANCZOS)
          #  pic.save(self.picture.path)

 #   def __str__(self):
  #      return self.nome
        

#def create_user_profile(sender, instance, created, **kwargs):
 #   if created:
  #      Instituicao.objects.create(user=instance)

#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()