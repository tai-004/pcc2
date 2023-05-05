from django.db import models
from noti.models import Notificacao
from django.contrib.auth.models import User
# Create your models here.
from accounts.models import Instituicao

from django.db.models.signals import post_save, post_delete

class Voluntario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    horario = models.CharField(max_length=100, null=True, blank=True)
    funcao= models.CharField(max_length=100, null=True, blank=True)
    quantidadepessoas = models.IntegerField(null=True, blank=True)
    tempo = models.IntegerField(null=True, blank=True)
    idademinima = models.IntegerField(null=True, blank=True)
    cidade = models.CharField(max_length=150, null=True, blank=True)
    rua = models.CharField(max_length=150, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    bairro = models.CharField(max_length=150, null=True, blank=True)
    telefone = models.CharField(max_length=150, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    aceitar_count = models.IntegerField(default=0)
    favoC = models.IntegerField(default=0)
  
    class Meta:
         permissions = (("inst", "inst"), ("usua", "usua"))


    def __str__(self):
        return self.titulo


class Informar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_infor')
    voluntario = models.ForeignKey(Voluntario, on_delete=models.CASCADE, related_name='post_infor')
     
    def avisarCurtir(sender, instance, *args, **kwargs):
        favori = instance
        voluntario = favori.voluntario
        sender = favori.user
        noti = Notificacao(voluntario=voluntario, sender=sender, user=voluntario.sender, noti=2)
        noti.save()

post_save.connect(Informar.avisarCurtir, sender=Informar)

class Favo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_favo')
    voluntario = models.ForeignKey(Voluntario, on_delete=models.CASCADE, related_name='post_favo')
     
    def curtir(sender, instance, *args, **kwargs):
        favo = instance
        voluntario = favo.voluntario
        sender = favo.user
        notify = Notificacao(voluntario=voluntario, sender=sender, user=voluntario.user, noti=1)
        notify.save()
    def descurtir(sender, instance, *args, **kwargs):
        favo = instance
        voluntario = favo.voluntario
        sender = favo.user
        notify = Notificacao.objects.filter(voluntario=voluntario, sender=sender, noti=1)
        notify.delete()

post_save.connect(Favo.curtir, sender=Favo)
post_delete.connect(Favo.descurtir, sender=Favo)

