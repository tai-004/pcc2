from django.db import models

# Create your models here.

from django.contrib.auth.models import User

from PIL import Image
from django.conf import settings
import os


def user_directory_path_profile(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
            os.remove(full_path)

    return profile_pic_name

def user_directory_path_banner(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    banner_pic_name = 'user_{0}/banner.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, banner_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return banner_pic_name

# Create your models here.
class Profile(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das opções"]
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    formacao = models.CharField(max_length=100, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES,  null=True)
    idade = models.DateTimeField(auto_now_add= False, auto_now=False, blank=True, null= True)
    trabalho = models.CharField(max_length=150, null=True, blank=True)
    habilidades = models.CharField(max_length=150, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    cidade = models.CharField(max_length=150, null=True, blank=True)
    estado = models.CharField(max_length=150, null=True, blank=True)
    rua = models.CharField(max_length=150, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    bairro = models.CharField(max_length=150, null=True, blank=True)
    cpf = models.IntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to=user_directory_path_profile, blank=True, null=True, verbose_name='Picture')
    banner = models.ImageField(upload_to=user_directory_path_banner, blank=True, null=True, verbose_name='Banner')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 250, 250

        if self.picture:
            pic = Image.open(self.picture.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.picture.path)

    def __str__(self):
        return self.user.username
        

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()