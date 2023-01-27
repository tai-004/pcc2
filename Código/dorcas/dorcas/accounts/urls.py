from django.urls import path
from accounts.views import UsuarioCreate
from . import views


urlpatterns = [

    path('registrar/', UsuarioCreate.as_view(), name='registrar'),  #url de registro 
    path('profile/', views.profile, name = 'profile'),
]