from django import forms
from .models import Tabela
from django.forms.widgets import FileInput
from django.contrib.auth.forms import User


class NovaTabelaForm(forms.ModelForm):
     class Meta:
        model = Tabela
        fields =   fields = ('nota', 'descricao')

