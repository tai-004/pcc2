from django.urls import path
from . import views


urlpatterns = [
    path('responsavel/', views.newresponsavel, name='responsavel'),
    path('', views.detalhar, name='detalhar'),
]    