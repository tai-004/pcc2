from django.urls import path

from . import views


urlpatterns = [
    path('newpost/', views.NewVoluntario, name='newpost'),  #url de registro 
    path('publicar/', views.publicar, name='publicar'),
    path('excluir/<voluntario_id>', views.excluir, name='excluir'),
    path('editar/<voluntario_id>', views.editar, name='editar'),
    path('<voluntario_id>/like', views.like, name='likes'),
    path('<voluntario_id>/postlike', views.postlike, name='postlikes'),
    path('post/', views.posttudo, name='posttudo'),
   
]