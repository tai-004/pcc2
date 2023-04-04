from django.urls import path
from voluntariado.views import favo

from . import views


urlpatterns = [
    path('newpost/', views.NewVoluntario, name='newpost'),  #url de registro 
    path('publicar/', views.publicar, name='publicar'),
    path('excluir/<voluntario_id>', views.excluir, name='excluir'),
    path('editar/<voluntario_id>', views.editar, name='editar'),
    path('<voluntario_id>/like', views.like, name='like'),
    path('<voluntario_id>/', views.postlike, name='postlike'),
    path('post/', views.posttudo, name='posttudo'),
    path('<voluntario_id>/favo', favo, name='favo'),
    
]