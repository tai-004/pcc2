from django.urls import path
from .views import UsuarioCreate, EditProfile

urlpatterns = [
 path('registrar/', UsuarioCreate.as_view(), name='registrar'),  #url de registro 
 path('editarperfil', EditProfile, name='editarperfil'),
]