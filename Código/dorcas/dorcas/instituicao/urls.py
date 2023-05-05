from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import  static

from . import views


urlpatterns = [
    #path('novatabela/', views.novaTabelar, name='newtable'),  
    path('tabela/', views.lertabelar, name='tabelar'),  #url de registro 

] 
