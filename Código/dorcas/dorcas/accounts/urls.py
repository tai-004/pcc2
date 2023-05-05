from django.urls import path
from accounts.views import UsuarioCreate,InstituicaoCreate
from . import views


urlpatterns = [
    path('instituicao/', InstituicaoCreate.as_view(), name='instituicao'),  #url de registro 
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),  #url de registro 
    path('profile/', views.criarprofile, name = 'profile'),
    path('apresenteprofile/', views.lerprofile, name = 'apresenteprofile'),
    path('instituicao_profile/', views.criarinstituicao, name = 'instituicao_profile'),
    path('alert/', views.profilealert, name = 'alert'),  
    path('perfilapresente/', views.lerperfil, name = 'perfilapresente'),
]