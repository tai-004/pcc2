from django.db import models
from noti.models import Notificacao, Tabela_notis
from django.contrib.auth.models import User
# Create your models here.
from accounts.models import Instituicao

from django.db.models.signals import post_save, post_delete


class Curriculo(models.Model):
    user= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    data_nasc = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    tempo_disponivel  = models.CharField(max_length=100, null=True, blank=True)
    motivacao = models.CharField(max_length=700, null=True, blank=True)
    resumo = models.CharField(max_length=1000, null=True, blank=True)
    aceitar_count = models.IntegerField(default=0)
    cidade = models.CharField(max_length=150, null=True)
    estado = models.CharField(max_length=150, null=True)
    rua = models.CharField(max_length=150, null=True)
    numero = models.CharField(max_length=10, null=True)
    bairro = models.CharField(max_length=150, null=True)
    experiencia = models.CharField(max_length=700, null=True, blank=True)
  


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


 

#class referencia de curriculo
class Informar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_infor')
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE, null=True, related_name='post_infor')
     
    def avisarCurtir(sender, instance, *args, **kwargs):
        favori = instance
        curriculo = favori.curriculo
        sender = favori.user
        noti = Tabela_notis(curriculo=curriculo, sender=sender, user=curriculo.user, tabe=2)
        noti.save()

post_save.connect(Informar.avisarCurtir, sender=Informar)

#class referencia de voluntariado
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

