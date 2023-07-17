from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db.models.signals import post_save, post_delete

#notificação referente a class 'voluntario'
#o user comum realiza notificação para class voluntario
class Notificacao(models.Model):
    NOTI = ((1, 'Like'), (2, 'Volu'))

    voluntario = models.ForeignKey('voluntariado.Voluntario', on_delete=models.CASCADE, related_name='notifi_voluntario', blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notidefromuser')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notiparauser')
    data = models.DateTimeField(auto_now_add=True)
    visto = models.BooleanField(default=False)
    apresentar = models.BooleanField(default=False)

    noti = models.IntegerField(choices=NOTI, blank=True, null=True)
    
 
#quem vai mandar é a instituição e quem vai receber é o usuario comum. 
#models para quem associar, models table de instituição
#user vai ser o usuario que vai receber
class Tabela_notis(models.Model):
    TABE = ((1, 'Like'), (2, 'Volu'))
    curriculo = models.ForeignKey('voluntariado.Curriculo', on_delete=models.CASCADE, related_name='notiCurriculo', blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null = True, related_name='envioCurriculo')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    tabe = models.IntegerField(choices=TABE, blank=True, null=True)
    cargo = models.CharField(max_length=150, null=True, blank=True)
    desempenho = models.CharField(max_length=150, null=True, blank=True)
    lido = models.BooleanField(default=False)
    nota = models.IntegerField(null=True, blank=True)



