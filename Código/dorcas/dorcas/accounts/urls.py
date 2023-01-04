from django.urls import path
from .views import UsuarioCreate

urlpatterns = [
   	path('registrar/', UsuarioCreate.as_view(), name='registrar'),

]