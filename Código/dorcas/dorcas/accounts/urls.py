from django.urls import path
from accounts.views import UsuarioCreate,InstituicaoCreate
from . import views


urlpatterns = [
    path('instituicao/', InstituicaoCreate.as_view(), name='instituicao'),  #url de registro 
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),  #url de registro 
    path('profile/', views.profile, name = 'profile'),
]