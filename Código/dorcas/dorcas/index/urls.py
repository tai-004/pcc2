from django.urls import path
from . import views

urlpatterns = [
    path('', views.templates, name="templates"),
   
]