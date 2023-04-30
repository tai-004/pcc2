from django.contrib import admin
from accounts.models import Profile, Instituicao, idade


# Register your models here.

admin.site.register(Profile)

admin.site.register(Instituicao)

admin.site.register(idade)
