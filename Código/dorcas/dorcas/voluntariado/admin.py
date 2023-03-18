from django.contrib import admin
from voluntariado.models import Likes, Voluntario


# Register your models here.

admin.site.register(Voluntario)

admin.site.register(Likes)