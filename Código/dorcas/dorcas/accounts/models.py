from django.db import models
from django.db.models.signals import pre_delete
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from PIL import Image
from django.conf import settings

import os


class Menores(models.Model):
    idade= models.IntegerField(null=True, blank=True) 
  


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

# model referente ao diagrama de classes . TAB  USUARIO 
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nome = models.CharField(default = 'Dorcas(nome padrão)', max_length=100, null=True)
   # emailAdm = models.EmailField(default = 'email@gmail.com', max_length = 254, null=True, blank=True)
    #funcaoAdm = models.CharField(default = 'ex.: Leitor', max_length=100, null=True, blank=True)
    #dtaDeFuncaoAdm = models.CharField(default = '00/00/0000', max_length=100, null=True, blank=True)
    #telefone = models.CharField(default = '55 DDD 000000000', max_length=25, null=True, blank=True)
    formacao = models.CharField(default = 'ex.: Letras', max_length=100, null=True, blank=True)
    sexo = models.CharField(default = 'ex.: Feminino', max_length=20, null=True,blank=True)
    trabalho = models.CharField(default = 'ex.: Professora', max_length=150, null=True, blank=True)
    habilidades = models.CharField(default = 'ex.: Contar histórias', max_length=150, null=True, blank=True)
    #cidade = models.CharField(max_length=150, null=True)
    #estado = models.CharField(max_length=150, null=True)
    #rua = models.CharField(max_length=150, null=True)
    #numero = models.CharField(max_length=10, null=True)
    #bairro = models.CharField(max_length=150, null=True)
    #cpf = models.IntegerField(default = '000000000', null=True, blank=True)
    picture = models.ImageField(upload_to=user_directory_path_profile, blank=True, null=True, verbose_name='Picture')
    banner = models.ImageField(upload_to=user_directory_path_banner, blank=True, null=True, verbose_name='Banner')
    #dataNascimento = models.DateTimeField(null=True, blank = True)
    
 
  

    class Meta:
         permissions = (("use", "use"), ("atual", "atual"), ("exc", "exc"), ("foto", "foto"), ("menor", "menor"), ("responsavelMenor", "responsavelMenor"))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 250, 250

        if self.picture:
            pic = Image.open(self.picture.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.picture.path)   

    def salva(self, *args, **kwargs):
        super().salva(*args, **kwargs)
        SIZE = 250, 250

        if self.banner:
            pic = Image.open(self.banner.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.salva(self.banner.path) 

    #def __str__(self):
     #  return self.user.username



def user_directory_path_inst(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
         os.remove(full_path)

    return profile_pic_name

def user_directory_path_instbanner(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    banner_pic_name = 'user_{0}/banner.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, banner_pic_name)

    if os.path.exists(full_path):
         os.remove(full_path)

    return banner_pic_name

# model referente ao diagrama de classes . TAB  INSTITUIÇÃO
class Instituicao(models.Model):
    EIXO_CHOICES = (('animais', 'animais'), ('crianças', 'crianças'), ('idosos', 'idosos'), ('religiosa', 'religiosa'), ('outra', 'outra'))

    user = models.OneToOneField(User, on_delete= models.CASCADE, null=True)
    bio = models.CharField(max_length=500, null=True, blank= True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    eixoAtuacao = models.CharField(max_length=15, choices=EIXO_CHOICES,  null=True)
    cidade = models.CharField(max_length=150, null=True)
    estado = models.CharField(max_length=150, null=True)
    rua = models.CharField(max_length=150, null=True)
    numero = models.CharField(max_length=10, null=True)
    bairro = models.CharField(max_length=150, null=True)
    telefone = models.CharField(default = '55 DDD 000000000', max_length=25, null=True, blank=True)
    email = models.EmailField(default = 'email@gmail.com', max_length = 254, null=True, blank=True)
    cnpj = models.CharField(max_length=150, null=True)
    picture = models.ImageField(upload_to=user_directory_path_profile, blank=True, null=True, verbose_name='Picture')
    banner = models.ImageField(upload_to=user_directory_path_banner, blank=True, null=True, verbose_name='Banner')
   
    def __str__(self):
       return self.user.username
    class Meta:
         permissions = (("inst", "inst"), ("atualizar", "atualizar"), ("exclude", "exclude"), ("foto", "foto"))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 250, 250

        if self.picture:
            pic = Image.open(self.picture.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.picture.path) 

    def salva(self, *args, **kwargs):
        super().salva(*args, **kwargs)
        SIZE = 250, 250

        if self.banner:
            pic = Image.open(self.banner.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.salva(self.banner.path)   


