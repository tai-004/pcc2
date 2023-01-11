from django.urls import path
from accounts.views import UsuarioCreate, EditProfile
from .views import Editperfil

urlpatterns = [
 path('c/', Editperfil, name='c'),
 path('registrar/', UsuarioCreate.as_view(), name='registrar'),  #url de registro 
 path('registra/', EditProfile, name='registra'),  #url de registro 
]