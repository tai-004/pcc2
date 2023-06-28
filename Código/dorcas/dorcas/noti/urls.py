from django.urls import path

from . import views


urlpatterns = [
   path('', views.apresentaNoti, name='noti'),
   path('notiTabela/', views.notiTabela, name='notiTabela'),
  # path('', views.apresentaNoti2, name='noti2'),
   path('nnn/', views.nnn, name='nnn'),
   path('<noti_id>/noti', views.detalhar, name='noti'),  
   path('tabela/nova/<noti_id>', views.notiTabelar, name='notiTabelar'),
   path('tabela_notis/', views.tabela_notis, name='tabela_notis'),
   path('cont/', views.countarNoti, name='countarNoti'),
   path('desempenho/<tabela_notis_id>', views.desempenho, name='desempenho'),
  
] 