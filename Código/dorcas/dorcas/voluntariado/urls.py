from django.urls import path
from voluntariado.views import favo, pedir

from . import views


urlpatterns = [
    path('newpost/', views.criarVoluntariar, name='newpost'),  #url de registro 
    path('publicar/', views.publicar, name='publicar'),
    path('excluir/<voluntario_id>', views.excluir, name='excluir'),
    path('editar/<voluntario_id>', views.editar, name='editar'),
    path('<voluntario_id>/', views.postCurtir, name='postlike'),
    path('<voluntario_id>/curtir', views.curtir, name='curtir'),
    path('', views.postarTudo, name='postarTudo'),
    path('<voluntario_id>/favo', favo, name='favo'),
    path('<voluntario_id>/pedir', pedir, name='pedir'),
    
]

#<!-- <a href="{% url 'postarTudo' notification.voluntariado.id %}">See post</a>-->