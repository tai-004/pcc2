from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notifications(models.Model):
    NOTI = ((1, 'Likes'), (2, 'Volu'))

    voluntariado = models.ForeignKey('voluntariado.Voluntario', on_delete=models.CASCADE, related_name='notifi_voluntario', blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notidefromuser')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notiparauser')
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)