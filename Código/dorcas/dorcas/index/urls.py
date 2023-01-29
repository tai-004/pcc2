from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.templates, name="templates"),
    path('', views.dorcas, name="dorcas"),
]