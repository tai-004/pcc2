from django.urls import path
from . import views
from responsavel.views import newresponsavel
#from .views import newresponsavel

urlpatterns = [
    path('responsavel/', newresponsavel.as_view(), name='newresponsavel'),

    #path('responsavel/', views.newresponsavel, name='newresponsavel'),
    path('', views.detalhar, name='detalhar'),
]    