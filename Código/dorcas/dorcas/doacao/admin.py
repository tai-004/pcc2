from django.contrib import admin
from doacao.models import DoacaoCampanhaObj, DoacaoCampanhaDinheiro, DoeUser, TabelarDoe
# Register your models here.

admin.site.register(DoacaoCampanhaObj)
admin.site.register(DoacaoCampanhaDinheiro)
admin.site.register(DoeUser)
admin.site.register(TabelarDoe)