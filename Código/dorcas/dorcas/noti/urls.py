from django.urls import path

from . import views


urlpatterns = [
   path('', views.apresentaNoti, name='noti'),
   path('notiTabela/', views.notiTabela, name='notiTabela'),
   path('<noti_id>/noti', views.detalhar, name='noti'),  
   path('tabela_notis/', views.tabela_notis, name='tabela_notis'),
   path('cont/', views.countarNoti, name='countarNoti'),
   path('somar/', views.somarNoti, name='somarNoti'),
   path('desempenho/<tabela_notis_id>', views.desempenho, name='desempenho'),
   path('lido/<tabela_notis_id>', views.lido, name='lido'),
]