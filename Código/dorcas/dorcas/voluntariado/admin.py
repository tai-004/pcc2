from django.contrib import admin
from voluntariado.models import Likes,BlogPost, Favo ,Voluntario


# Register your models here.

admin.site.register(Voluntario)

admin.site.register(Likes)

admin.site.register(BlogPost)
admin.site.register(Favo)