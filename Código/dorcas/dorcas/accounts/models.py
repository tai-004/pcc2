from django.db import models
from responsavel.models import Responsavel
# Create your models here.
from django.db.models.signals import post_save
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

# model referente ao perfil de usuario simples
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE, null=True)
    nome = models.CharField(default = 'Dorcas(nome padrão)', max_length=100, null=True)
    telefone = models.CharField(max_length=20, null=True)
    formacao = models.CharField(max_length=100, null=True)
    sexo = models.CharField(max_length=20, null=True)
    idade = models.DateTimeField(auto_now_add= False, auto_now=False, null= True)
    trabalho = models.CharField(max_length=150, null=True)
    habilidades = models.CharField(max_length=150, null=True)
    #created = models.DateInput(auto_now_add=True)
    cidade = models.CharField(max_length=150, null=True)
    estado = models.CharField(max_length=150, null=True)
    rua = models.CharField(max_length=150, null=True)
    numero = models.CharField(max_length=10, null=True)
    bairro = models.CharField(max_length=150, null=True)
    cpf = models.IntegerField(null=True)
    picture = models.ImageField(upload_to=user_directory_path_profile, blank=True, null=True, verbose_name='Picture')
    banner = models.ImageField(upload_to=user_directory_path_banner, blank=True, null=True, verbose_name='Banner')

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


# model referente ao perfil das instituições
class Instituicao(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE, null=True)
    nomeAdm = models.CharField(default = 'Dorcas(nome padrão)', max_length=100, null=True)
    nomeInst= models.CharField(default = 'Dorcas(nome padrão)', max_length=100, null=True)
    telefonedoAdm = models.CharField(default = 'Telefone do Adiministrador', max_length=20, null=True)
    telefonedoInst = models.CharField(default = 'Telefone de contato do instituição', max_length=20, null=True)
    funcaoAdm = models.CharField(default = 'Função do Administrador na instituição', max_length=100, null=True)
    dtaDeFuncaoAdm = models.DateField(auto_now_add= False, auto_now=False, null= True)
    dtaDenascAdm = models.DateTimeField(auto_now_add= False, auto_now=False, null= True)
    emailAdm = models.EmailField(default = 'Email do Adiministrador', max_length = 254, null=True)
    emailInst = models.EmailField(default = 'Email do Instituiçao', max_length = 254, null =True)
    cidadeAdm = models.CharField(default = 'Cidade do Adiministrador', max_length=150, null=True)
    estadoAdm = models.CharField(default = 'Estado do Adiministrador', max_length=150, null=True)
    ruaAdm = models.CharField(default = 'Rua do Adiministrador', max_length=150, null=True)
    numeroAdm = models.CharField(default = 'Número da casa do Adiministrador', max_length=10, null=True)
    bairroAdm = models.CharField(default = 'Bairro do Adiministrador', max_length=150, null=True)
    cpfAdm = models.IntegerField(null=True)
    cidadeInst = models.CharField(default = 'Cidade da Instituição', max_length=150, null=True)
    estadoInst = models.CharField(default = 'Estado da Instituição', max_length=150, null=True)
    ruaInst = models.CharField(default = 'Rua da Instituição', max_length=150, null=True)
    eixoInst = models.CharField(default = 'Eixo da Instituição', max_length=150, null=True)
    categoriaInst = models.CharField(default = 'Categoria da Instituição', max_length=150, null=True)
    numeroInst = models.CharField(default = 'Número da cede da Instituição', max_length=10, null=True)
    bairroInst = models.CharField(default = 'Bairro da Instituição', max_length=150, null=True)
    cnpj = models.IntegerField(null=True)
    picture = models.ImageField(upload_to=user_directory_path_profile, blank=True, null=True, verbose_name='Picture')
    banner = models.ImageField(upload_to=user_directory_path_banner, blank=True, null=True, verbose_name='Banner')

    class Meta:
         permissions = (("inst", "inst"), ("atual", "atual"), ("exc", "exc"))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 250, 250

        if self.picture:
            pic = Image.open(self.picture.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.picture.path)   

    def __str__(self):
       return self.user.username
    