from django.urls import path
from . import views

from doacao.views import pedir, doar

urlpatterns = [ 

    path('atualizar/<doacaocampanhaobj_id>', views.atualizar, name='atualizarDoacao'), #atualiza camapanha de doação
    path('criar/', views.criarDoacaoCampanhaObj, name='criarDoacaoCampanhaObj'), #criar campanha de doação 
    path('excluir/<doacaocampanhaobj_id>', views.deletar, name='deletarDoacao'), #deleta doação
    path('', views.postarDoacao, name='postarDoacao'), #postar campanha de doação  
    path('publicar/', views.publicarDoacao, name='publicar'), #publicar minhas campanhas de doação
    path('adiciona/', views.criarDoacaoCampanhaDinheiro, name='atualizarDoacaoDinheiro'), #criar campanha de doação de dinheiro
    path('editar/<doacaocampanhadinheiro_id>', views.editar, name='editarDoacaoDinheiro'), #atualiza campanha de doação de dinheiro
    path('apagar/<doacaocampanhadinheiro_id>', views.excluir, name='excluirDoacaoDinheiro'), #deleta doação de dinheiro
    path('tabela/', views.tabelaDoacaoUser, name='tabelaDoacao'), #tabela gerada pelas doações p/ user comum
    path('tabela/intituicao/', views.tabelaDoacaoInst, name='tabelaDoacaoInst'), #tabela gerada pelas doações p/ instituição
    path('<doacaocampanhaobj_id>/doar', doar, name='doar'),#metodo 'curtir'
    path('<doacaocampanhaobj_id>/pedir', pedir, name='pedir2'), #metodocurtir'
    path('doeEdit/<doeuser_id>', views.doeEdit, name='doeEdit'),##edita a data de entrega'
]