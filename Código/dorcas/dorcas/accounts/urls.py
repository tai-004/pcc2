from django.urls import path
from accounts.views import redefinirSenha 
from . import views 

from django.contrib.auth import views as authViews 

urlpatterns = [
    path('pesquisar/', views.search_users, name='search_users'),

    path('instituicao/', views.InstituicaoCreate, name='instituicao'),  #url de registro 
    path('registrar/', views.UsuarioCreate, name='registrar'),  #url de registro
    path('menor2/', views.MenorCreate, name='menor'),  #url de registro  
    path('profile/', views.criarprofile, name = 'profile'),
    path('perfil_instituicao/', views.lerprofile, name = 'apresenteprofile'),#ler perfil da instiuição
    path('instituicao_profile/', views.criarinstituicao, name = 'instituicao_profile'),
    path('perfil_user_simples/', views.lerperfil, name = 'perfilapresente'),#ler perfil de usuario simples 
    path('usuarioForm/', views.menoresIdade, name = 'menoresIdade'),
    path('sairConta/<id>', views.sairConta, name = 'sairConta'), #desativa a conta
    path('conta/recuperar/', redefinirSenha.as_view(), name='password_reset'),#redefine senha
    path('antesSair/', views.antesSair, name='antesSair'), #antes de desativar a conta
    path('password_reset/done/', views.senhaDone, name='senhaDone'), #redefine senha
    path('profile/<str:username>/', views.perfilInstituicao, name='perfilInstituicao'),#redefine senha 
]

