from django.urls import path

from . import views


urlpatterns = [
   path('', views.noti, name='noti'),
   path('<noti_id>/', views.detalhar, name='noti'),  
   path('tabela/nova/<noti_id>', views.notiTabelar, name='notiTabelar'),
  
]