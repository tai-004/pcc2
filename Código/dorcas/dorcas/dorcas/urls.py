from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import  static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('accounts/', include ('accounts.urls')), #url que permite o login e cadastro do user
    path('accounts/', include('django.contrib.auth.urls')), # atributos do accounts 
    path ('', include ('index.urls')), #url da pagina index dlogo apos o login
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

