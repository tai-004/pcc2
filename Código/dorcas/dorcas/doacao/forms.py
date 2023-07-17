from django import forms
from .models import DoacaoCampanhaObj, DoacaoCampanhaDinheiro, DoeUser
from django.forms.widgets import FileInput
from django.contrib.auth.forms import User

#formulario de doação de objetos
class DoacaoCampanhaObjForm(forms.ModelForm):
     class Meta:
        model = DoacaoCampanhaObj
        fields =  ('titulo', 'categoria', 'outro', 'descricao', 'finalidade', 'cidade', 'estado', 'rua', 'bairro', 'numero', 'bairro')

#formulario de doação de dinheiro
class DoacaoCampanhaDinheiroForm(forms.ModelForm):
     class Meta:
        model = DoacaoCampanhaDinheiro
        fields =  ('titulo', 'descricao', 'chavePix', 'nomeChave')

#formulario de confirmação de doação
class DoacaoCampanhaObjUserForm(forms.ModelForm):
     class Meta:
        model = DoeUser
        fields =  ('dataEntrega', 'quantidade')
