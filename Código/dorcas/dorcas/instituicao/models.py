from django.db import models
from responsavel.models import Responsavel
# Create your models here.
#from noti.models import  Tabela_notis
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models.signals import post_save, post_delete

