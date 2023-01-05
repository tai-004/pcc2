from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('accounts/', include ('accounts.urls')), #url que permite o login e cadastro do user
    path('accounts/', include('django.contrib.auth.urls')), # atributos do accounts 
]
