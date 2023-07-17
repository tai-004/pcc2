from django.urls import path
from voluntariado.views import favo, pedir
from voluntariado.views import  CurriculoUpdate
from . import views


urlpatterns = [
    path('pesquisar/', views.pesquisa, name='pesquisa'),
    path('criarCurriculo/',  CurriculoUpdate.as_view(), name='criarCurriculo'),  #url de registro 
    path('deletar/<curriculo_id>', views.deletar, name='deletar'),
    path('atualizar/<curriculo_id>', views.atualizar, name='atualizar'),
    path('newpost/', views.criarVoluntariar, name='newpost'),  #url de registro 
    path('publicar/', views.publicar, name='publicarVolunt'),
    path('excluir/<voluntario_id>', views.excluir, name='excluir'),
    path('editar/<voluntario_id>', views.editar, name='editar'),
    path('<voluntario_id>/', views.postCurtir, name='postlike'), #esse
    path('<curriculo_id>/curtir', views.curtir, name='curtir'),#notificação de curriculo
    path('', views.postarTudo, name='postarTudo'), #esse
    path('<voluntario_id>/favo', favo, name='favo'),
    path('<curriculo_id>/pedir', pedir, name='pedir'),#notificação de curriculo
    path('ppp/', views.notiCurriculo, name='notiCurriculo'),
    path('pesquisaVoluntario/', views.pesquisaVoluntario, name='pesquisaVoluntario'),
    
]

