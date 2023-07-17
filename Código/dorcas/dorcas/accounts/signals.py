from .models import *
from django.contrib.auth.models import User, Group
from responsavel.models import Responsavel
from voluntariado.models import Curriculo
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       created = Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def create_user_inst(sender, instance, created, **kwargs):  
   if created:  
       created = Instituicao.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def create_user_inst(sender, instance, created, **kwargs):  
   if created:  
       created = Instituicao.objects.get_or_create(user=instance)



@receiver(post_save, sender=User)
def create_user_responsavel(sender, instance, created, **kwargs):  
    if created:  
       created = Responsavel.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def create_user_inst(sender, instance, created, **kwargs):  
   if created:  
       created = Curriculo.objects.get_or_create(user=instance)


