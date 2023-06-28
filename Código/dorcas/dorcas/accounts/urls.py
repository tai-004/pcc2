from django.urls import path
from accounts.views import redefinirSenha #InstituicaoCreate, MenorCreate#, UsuarioCreate
from . import views 

from django.contrib.auth import views as authViews 

urlpatterns = [
    path('pesquisar/', views.search_users, name='search_users'),

    path('instituicao/', views.InstituicaoCreate, name='instituicao'),  #url de registro 
    path('registrar/', views.UsuarioCreate, name='registrar'),  #url de registro
    path('menor2/', views.MenorCreate, name='menor'),  #url de registro  
    path('profile/', views.criarprofile, name = 'profile'),
    path('perfil_instituicao/', views.lerprofile, name = 'apresenteprofile'),
    path('instituicao_profile/', views.criarinstituicao, name = 'instituicao_profile'),
    path('alert/', views.profilealert, name = 'alert'),  
    path('perfil_user_simples/', views.lerperfil, name = 'perfilapresente'),
    path('responalert/', views.responalert, name = 'responalert'),
    path('usuarioForm/', views.menoresIdade, name = 'menoresIdade'),
   # path('formJunto/', views.formJunto, name = 'formJunto'),
    #path('profile/', views.formJunto, name = 'profile'),
    path('sairConta/<id>', views.sairConta, name = 'sairConta'),
    path('conta/recuperar/', redefinirSenha.as_view(), name='password_reset'),
    #path('passwordreset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/done/', views.senhaDone, name='senhaDone'),
    path('profile/<str:username>/', views.perfilInstituicao, name='perfilInstituicao'),
]

