from django import forms
from .models import Voluntario
from django.forms.widgets import FileInput
from django.contrib.auth.forms import User


class NewVoluntarioForm(forms.ModelForm):
     class Meta:
        model = Voluntario
        fields =   fields = ('titulo', 'horario', 'funcao', 'quantidadepessoas', 'tempo', 'idademinima', 'cidade', 'rua', 'bairro', 'numero', 'telefone')


