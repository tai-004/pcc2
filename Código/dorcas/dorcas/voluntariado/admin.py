from django.contrib import admin
from voluntariado.models import BlogPost, Favo ,Voluntario, Informar


# Register your models here.

admin.site.register(Voluntario)



admin.site.register(BlogPost)
admin.site.register(Favo)
admin.site.register(Informar)