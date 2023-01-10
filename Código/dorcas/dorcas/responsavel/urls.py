from django.urls import path
from .views import EditResponsavel

urlpatterns = [
 path('Editresponsavel', EditResponsavel, name='Editresponsavel'),
]