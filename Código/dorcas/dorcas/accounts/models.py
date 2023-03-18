
from django.db import models
from responsavel.models import Responsavel
# Create your models here.
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from datetime import datetime
from PIL import Image
from django.conf import settings
from datetime import date
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

# model referente ao diagrama de classes . TAB  USUARIO 
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE, null=True)
    nome = models.CharField(default = 'Dorcas(nome padrão)', max_length=100, null=True)
    emailAdm = models.EmailField(default = 'email@gmail.com', max_length = 254, null=True, blank=True)
    funcaoAdm = models.CharField(default = 'ex.: Leitor', max_length=100, null=True, blank=True)
    dtaDeFuncaoAdm = models.CharField(default = '00/00/0000', max_length=100, null=True, blank=True)
    telefone = models.CharField(default = '55 DDD 000000000', max_length=25, null=True, blank=True)
    formacao = models.CharField(default = 'ex.: Letras', max_length=100, null=True, blank=True)
    sexo = models.CharField(default = 'ex.: Feminino', max_length=20, null=True,blank=True)
    trabalho = models.CharField(default = 'ex.: Professora', max_length=150, null=True, blank=True)
    habilidades = models.CharField(default = 'ex.: Contar histórias', max_length=150, null=True, blank=True)
    cidade = models.CharField(max_length=150, null=True)
    estado = models.CharField(max_length=150, null=True)
    rua = models.CharField(max_length=150, null=True)
    numero = models.CharField(max_length=10, null=True)
    bairro = models.CharField(max_length=150, null=True)
    cpf = models.IntegerField(default = '000000000', null=True, blank=True)
    picture = models.ImageField(upload_to=user_directory_path_profile, blank=True, null=True, verbose_name='Picture')
    banner = models.ImageField(upload_to=user_directory_path_banner, blank=True, null=True, verbose_name='Banner')
    birth_date = models.DateTimeField(null=True, blank = True)

    def gage(self):
        datetime.date.today()
        date.today()
        age = datetime.date.today()-self.birth_date
        return int((age).days/365.25)
        
    
    class Meta:
         permissions = (("use", "use"), ("atual", "atual"), ("exc", "exc"))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 250, 250

        if self.picture:
            pic = Image.open(self.picture.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.picture.path)   

    def __str__(self):
       return self.user.username
    

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
    user = models.OneToOneField(User, on_delete= models.CASCADE, null=True)
    bio = models.TextField(max_length=50000, null=True, blank= True)
    nome = models.CharField(default = 'Dorcas(nome padrão)', max_length=100, null=True)
    eixoInst = models.CharField(default = 'Eixo da Instituição', max_length=150, null=True)
    categoriaInst = models.CharField(default = 'Categoria da Instituição', max_length=150, null=True)
    cidade = models.CharField(max_length=150, null=True)
    estado = models.CharField(max_length=150, null=True)
    rua = models.CharField(max_length=150, null=True)
    numero = models.CharField(max_length=10, null=True)
    bairro = models.CharField(max_length=150, null=True)
    telefone = models.CharField(default = '55 DDD 000000000', max_length=25, null=True, blank=True)
    email = models.EmailField(default = 'email@gmail.com', max_length = 254, null=True, blank=True)
    cnpj = models.IntegerField(null=True)
    picture = models.ImageField(upload_to=user_directory_path_profile, blank=True, null=True, verbose_name='Picture')
    banner = models.ImageField(upload_to=user_directory_path_banner, blank=True, null=True, verbose_name='Banner')
    
    def __str__(self):
       return self.user.username
    class Meta:
         permissions = (("inst", "inst"), ("atualizar", "atualizar"), ("exclude", "exclude"))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 250, 250

        if self.picture:
            pic = Image.open(self.picture.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.picture.path)   

