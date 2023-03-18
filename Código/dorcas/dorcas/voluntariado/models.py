from django.db import models
from noti.models import Notifications
from django.contrib.auth.models import User
# Create your models here.
from accounts.models import Instituicao

from django.db.models.signals import post_save, post_delete
class Voluntario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    horario = models.IntegerField(null=True, blank=True)
    funcao= models.CharField(max_length=100, null=True, blank=True)
    qnt = models.IntegerField(null=True, blank=True)
    tempo = models.IntegerField(null=True, blank=True)
    idademin = models.IntegerField(null=True, blank=True)
    cidade = models.CharField(max_length=150, null=True, blank=True)
    rua = models.CharField(max_length=150, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    bairro = models.CharField(max_length=150, null=True, blank=True)
    telefone = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    likes_count = models.IntegerField(default=0)
    class Meta:
         permissions = (("inst", "inst"), ("usua", "usua"))


    def __str__(self):
        return self.titulo

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')
    voluntario = models.ForeignKey(Voluntario, on_delete=models.CASCADE, related_name='voluntario_likes')
     
    def user_liked_post(sender, instance, *args, **kwargs):
        like = instance
        voluntario = like.voluntario
        sender = like.user
        notify = Notifications(voluntario=voluntario, sender=sender, user=voluntario.user, noti=1)
        notify.save()
    def user_unlike_post(sender, instance, *args, **kwargs):
        like = instance
        voluntario = like.voluntario
        sender = like.user
        notify = Notifications.objects.filter(voluntario=voluntario, sender=sender, noti=1)
        notify.delete()

post_save.connect(Likes.user_liked_post, sender=Likes)
post_delete.connect(Likes.user_unlike_post, sender=Likes)