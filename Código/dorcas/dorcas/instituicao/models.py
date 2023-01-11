from django.db import models
from responsavel.models import Responsavel
# Create your models here.

from django.contrib.auth.models import User

from PIL import Image
from django.conf import settings
import os


def user_directory_path_profile(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    profile_pic_name = 'user_{0}/instituicao.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
            os.remove(full_path)

    return profile_pic_name



# model referente ao perfil de usuario simples
class Instituicao(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    categoria = models.CharField(max_length=100, null=True, blank=True)
    cnpj = models.CharField(max_length=20, null=True, blank=True)
    cidade = models.CharField(max_length=150, null=True, blank=True)
    estado = models.CharField(max_length=150, null=True, blank=True)
    rua = models.CharField(max_length=150, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    bairro = models.CharField(max_length=150, null=True, blank=True)
    cpf = models.IntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to=user_directory_path_profile, blank=True, null=True, verbose_name='Picture')
    
    responsavel = models.ForeignKey(Responsavel,  on_delete=models.CASCADE, blank=True, null=True)
   
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 250, 250

        if self.picture:
            pic = Image.open(self.picture.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.picture.path)

    def __str__(self):
        return self.nome
        

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Instituicao.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()