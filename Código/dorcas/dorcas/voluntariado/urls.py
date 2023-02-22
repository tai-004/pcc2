from django.urls import path

from . import views


urlpatterns = [
    path('newpost/', views.NewVoluntario, name='newpost'),  #url de registro 
    path('publicar', views.publicar, name='publicar'),
   
]