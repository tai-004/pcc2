from django.contrib import admin
from voluntariado.models import  Favo, Voluntario, Informar, Curriculo


# Register your models here.

admin.site.register(Voluntario)


admin.site.register(Favo)
admin.site.register(Informar)
admin.site.register(Curriculo)