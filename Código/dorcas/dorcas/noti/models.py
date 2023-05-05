from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db.models.signals import post_save, post_delete


class Notificacao(models.Model):
    NOTI = ((1, 'Like'), (2, 'Volu'))

    voluntario = models.ForeignKey('voluntariado.Voluntario', on_delete=models.CASCADE, related_name='notifi_voluntario', blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notidefromuser')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notiparauser')
    data = models.DateTimeField(auto_now_add=True)
    noti = models.IntegerField(choices=NOTI, blank=True, null=True)
    

#quem vai mandar é a instituição e quem vai receber é o usuario comum. 
#models para quem associar, models table de instituição
#user vai ser o usuario que vai receber
#class Tabela_notis(models.Model):
 #   NOTI = ((1, 'Like'), (2, 'Volu'))
   # notificacao = models.ForeignKey('noti.Notificacao', on_delete=models.CASCADE, blank=True, null=True)
  #  sender = models.ForeignKey(User, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #data = models.DateTimeField(auto_now_add=True)
    #noti = models.IntegerField(choices=NOTI, blank=True, null=True)

#class Aceitar(models.Model):
 #   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='noti_infor')
  #  notificacao = models.ForeignKey(Tabela_notis, on_delete=models.CASCADE, related_name='noti_infor')
     
   # def avisarCurtir(sender, instance, *args, **kwargs):
    #    favori = instance
     #   notificacao = favori.notificacao
      #  sender = favori.user
        #noti = Notificacao(notificacao=notificacao, sender=sender, user=notificacao.sender, noti=2)
       # noti.save()

#post_save.connect(Aceitar.avisarCurtir, sender=Aceitar)