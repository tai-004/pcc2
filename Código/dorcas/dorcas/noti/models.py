from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notification(models.Model):
    NOTI = ((1, 'Like'), (2, 'Volu'))

    voluntario = models.ForeignKey('voluntariado.Voluntario', on_delete=models.CASCADE, related_name='notifi_voluntario', blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notidefromuser')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notiparauser')
    date = models.DateTimeField(auto_now_add=True)
    noti = models.IntegerField(choices=NOTI, blank=True, null=True)
    

#quem vai mandar é a instituição e quem vai receber é o usuario comum. 
#models para quem associar, models table de instituição
#user vai ser o usuario que vai receber
class Tabela_notis(models.Model):
    TIPO = ((1, 'Avisa'),)
    tabela = models.ForeignKey('instituicao.Tabela', on_delete=models.CASCADE, related_name='noti_tabela', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parauser')
    data = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inst')
    tipoNoti = models.IntegerField(choices=TIPO, blank=True, null=True)
